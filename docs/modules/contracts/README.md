# Contracts — the Lucernex contract financial engine

**Stated up front.** Lucernex does not have five financial subsystems. It has **one architectural
pattern applied five times**, plus one outlier. The pattern is a four-layer stack —
**Clause → Schedule → Transaction → Projection** — where a human-entered *clause* record (carrying
`AmendmentID`, `CovenantID`, `Section`, a clause date window and a `RevNumber`) is expanded by an
explicit, operator-invoked generator into a *schedule* of period rows, which a second generator
posts as *transactions* carrying GL account numbers and a vendor, while a fourth layer of
`Virtual*` objects computes forward-looking *projections* that are never stored. Expense billing,
expense accrual, percentage rent, use-based rent and straight-line/ASC 842 all instantiate this
stack. Expense recovery (CAM) is the outlier: it is a **reconciliation grid**, not a schedule, and
its 565 fields are a 9-perspective × 19-measure × Gross/Net cross-product, not 565 distinct
concepts.

For ASG Edge+ this means the contract schema being frozen at Week 12 (ADR-0008) needs **one**
generic four-layer abstraction plus five concrete instantiations — not five bespoke designs. That
is the single most reusable thing in this corpus, and it is written up in
[`setup-schedule-transaction-pattern.md`](setup-schedule-transaction-pattern.md).

## Contents

| Document | Answers |
|---|---|
| [`setup-schedule-transaction-pattern.md`](setup-schedule-transaction-pattern.md) | The Clause/Schedule/Transaction/Projection pattern — confirmed, specified, and given a layer-discriminator test. **Read this first.** |
| [`data-model.md`](data-model.md) | Every object in the financial engine, its field count, its physical table(s), and its FK edges. |
| [`rules.md`](rules.md) | `CON-R-001` … `CON-R-137`. Rule-engine-consumable: trigger, inputs, computation, output, confidence. |
| [`contract-hierarchy.md`](contract-hierarchy.md) | What actually keys a Contract; `MasterContractID` self-reference and the master-lease/sublease implication; the 4-table vertical partition; the Global/Firm 55:45 split. |
| [`percentage-rent.md`](percentage-rent.md) | Breakpoints, natural vs artificial, sales exclusions and their caps, the full period-rent derivation. |
| [`expense-recovery-cam.md`](expense-recovery-cam.md) | Why 565 fields. The Statement Audit grid decoded, and the six-step CAM waterfall recovered from the field labels. |
| [`escalations.md`](escalations.md) | Fixed vs index/CPI; how `EscalationIndex` is applied; the cap/floor/lifetime-collar stack. |
| [`payment-lifecycle.md`](payment-lifecycle.md) | `ExpenseSchedule` → `PaymentTransaction` → `PaymentReceipt` / `LandlordInvoice`; hold/suspend flags; the GL-export contract implied by `AccountNumber1..8`. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What ASG Edge+ should take, what it must build, what it should deliberately not copy, and the `BigDecimal` (Constitution §4.4) hazard register. |

## Scope

Objects covered: `Contract`, `ContractTerm`, `ContractAmendment`, `ExpenseSetup`,
`ExpenseSchedule`, `ExpenseEscalation`, `EscalationIndex`, `ExpenseAllocation`,
`ExpenseVendorAllocation`, `ExpenseAccrualSetup`, `ExpenseAccrualSchedule`, `AccrualTransaction`,
`ExpenseRecovery`, `ExpenseRecoveryItem`, `ExpenseRecoveryItemMapping`, `PercentageRent`,
`PercentageRentBreakpoint`, `Sales`, `SalesExclusion`, `SalesExclusionCap`, `UseBasedRent`,
`UseBasedRentBreakpoint`, `Usage`, `AlternateRentSchedule`, `VariableRentOffset`, `ScheduledOffset`,
`LinkSchedOffsetExpGrpType`, `PaymentTransaction`, `PaymentTransactionFullImport`,
`PaymentReceipt`, `LandlordInvoice`, `LandlordInvoiceItem`, `LinkLandlordInvPaymentTxn`,
`InvoiceIssue`, `InvoiceItem`, `Allowance`, `AllowanceTransaction`, `SecurityDeposit`, `Covenant`,
`CoTenancy`, `FinancialAdjustment`, `CodeExpenseType`, `CodeSLSchedule`, `FiscalPeriod`,
`DiscountRate`, and the eight `Virtual*` projection objects — 55 objects in total.

`SLSummary`, `SLPeriod`, `ContractFinancialTest` and `AcctingAssumptionAdjust` are named here where
they participate in the pattern, but their internals belong to the **accounting** module.

## Evidence base

| Source | Used for | Confidence |
|---|---|---|
| `_lucernex_objects_summary.txt` — 223 objects / 7,421 fields, exported from Lucernex's own **View Object Model** (`ShowObjectDetails.jsp`) | Every field name, declared type, and FK type in this folder | **Observed** |
| `docs/data-fields/*.md` + `all-fields.csv` — the 6,158-leaf **Manage Data Fields** catalog | Human labels (which carry the formulas), Global/Firm scope, `sTYPE_*` codes, Group/Subgroup taxonomy | **Observed** |
| `_crossmap.tsv` — 6,158 rows joining leaves to Postgres columns for 33 landed tables | The physical Postgres column types (all `TEXT`) | **Observed** |
| [`../../admin/009-related-fields-and-data-model.md`](../../admin/009-related-fields-and-data-model.md) | Contract FK columns, `VendorID`→`Employer`, the aggregate-root hierarchy | **Observed**, inheriting 009's own labels |
| `docs/contracts-explained.html` (BRD-24, ADR-0008) | ASG Edge+ target process PJ-01…PJ-13 and the Week-12 freeze | **Observed** (ASG-side requirement, not Lucernex behaviour) |
| [`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md) — 207 code tables with type IDs, four opened live 2026-09-10 | `Contract Status Code`'s three values; ASC 842 as the only configured standard; the code-table band claim this module tests | **Observed** |

**No live UI was opened by this document set directly**; the offline exports are the base, with two
live findings integrated from `code-table-registry.md` (captured 2026-09-10 by a parallel pass).
Anything that would need a screen to confirm is in each file's `## Open questions`.

## The four headline findings

1. **The pattern is real and it is four layers, not three.** The `Virtual*` objects are a
   first-class layer, not a reporting afterthought — they hold the breakpoint tiers, the cap/floor
   arithmetic and the actual-vs-projected flag (`IsActual`) that percentage rent is derived from.
   See [`setup-schedule-transaction-pattern.md`](setup-schedule-transaction-pattern.md).
2. **The CAM waterfall is recoverable exactly, from the field labels.** Lucernex encoded the
   formula in the UI label of every computed field: `Sub Total #1 (C+NC-D)`,
   `Pass-Through (ST1+AF%+AF+A)`, `Sub Total #2 (PT-R)`, `Net Pass-Through (ST2*PRR)`,
   `Net Amount Due (NPT-PP)`. Six steps, fully specified. See
   [`expense-recovery-cam.md`](expense-recovery-cam.md) and rules `CON-R-080`…`CON-R-086`.
3. **Contract status is not the contract lifecycle.** `Contract Status Code` holds three values —
   `AI Abstracted`, `Active`, `Inactive` — and none is a BRD-24 stage. The lifecycle *is* a real
   state machine, but Lucernex implements it as a template-driven milestone timeline over a
   platform-internal phase enumeration on `ProjectEntity`, with the stages materialised as **date
   fields**. The ASG tenant has already patched around it with a custom `Firm_LeaseStatus` field.
   Two axes, not one. See [`contract-hierarchy.md` §7](contract-hierarchy.md#7-contract-status-vs-the-brd-24-lifecycle--the-answer)
   and the blocking item in [`asg-edgeplus-mapping.md` §5.1](asg-edgeplus-mapping.md#51-blocking--contract-status-is-not-the-contract-lifecycle).
4. **Every landed Postgres column is `TEXT`, including money.** All 1,194 cross-mapped columns
   across 33 tables are `TEXT`; the only exceptions are 31 primary keys typed `VARCHAR(64) NOT NULL`.
   `sales.GrossSalesAmount`, `sales.NetSalesAmount` and all six `sales.SalesAdjustmentN` land as
   `TEXT`. This is the Constitution §4.4 hazard in its most acute form, and it is registered in
   [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md#41-typing-hazard-register-constitution-444).
