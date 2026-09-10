# ASG Edge+ mapping

**Stated up front.** Take **three** things from Lucernex's contract financial engine and reject
**four**.

**Take:** (1) the four-layer Clause/Schedule/Transaction/Projection pattern, generic once and
instantiated five times; (2) the CAM waterfall, which is fully specified in `CON-R-080`…`CON-R-086`
and is the hardest domain logic in the module; (3) `LinkLandlordInvPaymentTxn`'s shape — a
many-to-many allocation carrying the variance **and its reason** on the join.

**Reject:** (1) field-per-variant modelling — `ExpenseRecovery`'s 502-cell grid should be rows, not
columns; (2) the eight fixed breakpoint slots — should be a tier collection; (3) the 120
denormalised rent rollups on `Contract`; (4) `TEXT`-typed money everywhere, which is a direct
Constitution §4.4 violation.

**One thing needs a decision, not a copy:** ASG Edge+'s BRD-24 PJ-12 assumes a contract-level
vendor. Lucernex has none. That is a deliberate divergence and needs an ADR.

---

## 1. Direct correspondence to the ASG Edge+ build

`docs/contracts-explained.html` (BRD-24, ADR-0008) defines 13 process steps and names three
downstream components that consume the contract schema. Mapping them onto this corpus:

| ASG component | BRD-24 ref | Lucernex source | Documents |
|---|---|---|---|
| **#21 Payment Processing** | PJ-13 "process 1st month of rent" | `ExpenseSetup` → `ExpenseSchedule` → `PaymentTransaction` → `PaymentReceipt`/`LandlordInvoice` | [`payment-lifecycle.md`](payment-lifecycle.md), `CON-R-030`–`CON-R-039`, `CON-R-103`–`CON-R-124` |
| **#22 Percentage Rent & Sales** | PJ-04 "expenses, % rent, breakpoints, exclusions captured" | `PercentageRent` + breakpoints + `Sales` + exclusions + the `Virtual*` layer | [`percentage-rent.md`](percentage-rent.md), `CON-R-050`–`CON-R-079` |
| **#23 ASC 842 Accounting** | — | `ContractFinancialTest`, `SLSummary`, `SLPeriod`, `Contract / Cap Lease Test`, `CodeExpenseType`'s treatment bindings | **accounting module** — this folder supplies the inputs only |

| BRD-24 step | Lucernex equivalent | Gap |
|---|---|---|
| PJ-02 Center linking wizard | `Contract.FacilityID` / `LocationID` / `ComplexID` | Lucernex has no wizard-enforced order; BRD-24 mandates one |
| PJ-03 Contract shell via wizard + templates | `Covenant.CodeCovenantTemplateID`, `AddCovenantFromTemplate`, `AddResponsibilityFromTemplate`, `BudgetTemplateID` | Template seeding exists; atomic creation does not |
| PJ-04 Initial financial abstraction | Expense Setup Wizard + Contract Terms Wizard + `PercentageRent` | Present |
| PJ-05–PJ-09 Abstraction workflow, QA, client approval | `WorkFlow` (nested under Contract per 009), `CodeApprovalStatusID` families | **workflow module** |
| PJ-10 Store opens, status adjust | `CodeContractStatusID`, `StatusEffectiveDate`, `ActualStartDate` | Present |
| PJ-11 Critical dates review | `KeyDate` (41 fields), `ContractTerm`, the 11 date pairs on `Contract` | Present |
| **PJ-12 Vendor record setup** | **No contract-level vendor exists** | **Divergence — see §5** |
| PJ-13 Process 1st month of rent | `GENERATE_RENT` → `PROCESS_PAYMENT` | Present |

---

## 2. What already exists in ASG Edge+

| ASG Edge+ asset | Relevance |
|---|---|
| `asg-edgeplus-starter-identity` and the gateway's `X-Tenant-Id` model | The financial engine is tenant-scoped throughout; every object carries `ProjectEntityID` and the fiscal calendar is portfolio-scoped (`CON-R-023`) |
| Configuration-Service Masters (MDM-01) | The ~40 `Dropdown (… Code)` lists this module depends on — Expense Type/Group/Category, Frequency, Proration Method, Cap Type, Recovery Type, Sales Group/Type, Percentage Rent Type, Escalation Type, Index Type/Source, Payment Method, Approval Status, Source Entity, Alt Rent Math, Accrual Type — are Masters |
| Page/List Layouts (PAGE-LAYOUTS-01) | `Related Fields` vs `List Layouts` maps exactly onto referenced-lookup vs owned-child ([`contract-hierarchy.md` §4](contract-hierarchy.md#4-walkhierarchyjsps-composition-tree--what-a-contract-owns)) |
| Constitution §4.4 (`BigDecimal` only) | Directly engaged — see §4 |
| ADR-0008 Week-12 schema freeze | This document set is the input |

### Two live findings that change Masters scoping

Both **Observed**, captured 2026-09-10, from
[`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md).

**This tenant runs ASC 842 only.** `ASC 842 Schedule Type Code` (2162) holds exactly one value,
`842 Rent`. `Straight Line Schedule Type Code` (2161) and `IFRS 16 Schedule Type Code` (2163) are
both **empty**. The engine supports all three standards — the three code tables and their three
backing objects (`CodeSLSchedule`, `CodeASC842Schedule`, `CodeIFRS16Schedule`) are structurally
identical, 24 fields each — but ASG uses one. Consequences for this module: `CodeExpenseType`'s
`CodeSLScheduleID` and `CodeIFRS16ScheduleID` FKs will be **null on every row** in a migration, and
the 20 `ExportAcct1..20Number` GL slots exist exactly once, on `842 Rent`. Confirm with the business
before building IFRS 16; the capability is present in the incumbent and unused.

**The 2000/3000 code-table band does not predict behaviour** — see
[`data-model.md` §8](data-model.md#8-the-code-table-bands-refuted-with-a-better-predictor). The
better predictor is *"does the code table have a dedicated object in the catalogue?"* — 11 of 207 do,
and those 11 are the ones that cannot be modelled as `(code, label, active)`. Size the Masters model
against that 11, not against the 17-table 3000 band.

**`CodeExpenseType` is the single most important Master.** It carries 20 GL account slots and the
three accounting-treatment bindings (`CON-R-109`). It is not a simple code list and must not be
modelled as one. Its correct home is the Hub (global) with firm-level overrides for the account
numbers — which is exactly the Hub/Spoke publish/accept problem the workspace `CLAUDE.md` flags as
not yet written down.

---

## 3. What must be built

### 3.1 The generic four-layer abstraction — build once

Specified in
[`setup-schedule-transaction-pattern.md` §5](setup-schedule-transaction-pattern.md#5-the-pattern-specified-for-asg-edge). Build order:

| # | Instance | Blocks |
|---|---|---|
| 1 | Recurring expense (`FinancialClause` → `ScheduleRow` → `PostedTransaction`) | ASG #21 |
| 2 | Escalation (modifier on the clause; materialised onto the schedule) | correctness of #1 |
| 3 | Percentage rent (computed schedule) | ASG #22 |
| 4 | Accrual (parallel schedule + transaction) | ASG #23 |
| 5 | Use-based rent (same engine as #3, different measure) | near-free after #3 |

### 3.2 Replace field-per-variant with rows

| Lucernex | ASG Edge+ | Why |
|---|---|---|
| `ExpenseRecovery` 502-cell grid | `RecoveryStatementLine(recoveryId, measure, perspective, basis, amount)` — where `perspective` ∈ {REPORTED, APPROVED, BUDGETED} × {CURRENT, PRIOR} and `basis` ∈ {GROSS, NET}. Variances become a **query**, not 396 stored columns | 63% of the grid is `*_MATH_OPERATION` (derived). Storing derived values in columns is what forced `expense_recovery_part1..4` |
| `BreakpointAmount1..8` / `Count1..8` / `Rate1..8` | `RentTier(clauseId, ordinal, threshold, thresholdKind, rate)` | Eight is arbitrary; a nine-tier lease is unrepresentable today |
| `AccountNumber1..8`, `APExportTax1..4Number`, `ExpAccrualAcct1..4Number`, `PercentRentAccrualAcct1..4Number`, `RETaxAccrualAcct1..4Number` | `GlCodingLine(transactionId, purpose, segment, value)` — but **resolve `CON-R-111` first** | 20 slots per row is unmaintainable, but the segments-vs-split-lines question changes the shape |
| `TaxAmount1..4`, `ContractTaxRate1..4`, `ApplyTax1..4Flag` | `TaxComponent(scope, ordinal, rate, amount, applies)` | Four is arbitrary |
| `SalesAdjustment1..6` | `SalesAdjustment(salesId, kind, amount)` | Six is arbitrary |
| `ClientAmount1..3`, `ClientDate1..3`, `ClientText1..3` | Extension attributes | Generic slots are a custom-fields problem |

### 3.3 Structured exclusions for expense recovery

Lucernex has `RecoveryExclusions(Textarea)` — free text (`CON-R-098`) — while percentage rent has a
proper `SalesExclusion`/`SalesExclusionCap` model. The ASG tenant worked around it with
`Firm_CAM*ExclusionsYN`/`…Reference` fields. **Build the structured model Lucernex lacks**, using
`SalesExclusion`/`SalesExclusionCap` as the template.

### 3.4 A receipt allocation table

`CON-R-118`: there is no FK or link table from `PaymentReceipt` to `PaymentTransaction`. Build
`ReceiptAllocation(receiptId, transactionId, amount, date, variance, reason, status)` — the same
shape as `LinkLandlordInvPaymentTxn`.

### 3.5 Separate the lease abstract from the computation config

The finding from [`expense-recovery-cam.md` §5](expense-recovery-cam.md#5-what-the-asg-tenant-added-on-top-91-firm-fields-on-contract)
and [`contract-hierarchy.md` §5](contract-hierarchy.md#5-contracts-physical-shape-570-fields-4-tables-45-tenant-custom):
121 fields on `Contract` are 100% Firm-scope lease abstract, in a rigid repeating shape:

```
{Provision}YN            — is this provision in the lease?
{Provision}Percent/Amount — the negotiated value
{Provision}TextReference / Document / Page / Section — where it says so
{Provision}Comment / Status / Notes — the abstractor's note and state
```

Model this as a first-class **`AbstractedProvision`** entity — provision type, present flag, value,
document/page/section citation, abstractor note, verification status — and derive the computation
configuration from it. This is exactly what BRD-24's PJ-04 → PJ-06 split implies, and it is the
single biggest structural improvement ASG Edge+ can make over Lucernex.

### 3.6 Explicit projection refresh

`SLSummary` already carries `NeedsRecalculation`, `RecalcTriggerDate`,
`NeedsRecalcModifiedByMemberIDList`, `NeedsRecalcModifiedByLastMember` and
`RecalcOverrideNotesIDList` — Lucernex needed a recalculation queue and bolted one on for
straight-line only. `Contract`'s 120 rollups have no equivalent. Build the invalidation/refresh
mechanism once, for every projection, from the start.

---

## 4. What should deliberately differ

| # | Lucernex | ASG Edge+ | Rationale |
|---|---|---|---|
| 1 | 120 denormalised rent rollups on `Contract` | Materialised projection with explicit refresh | Staleness + recomputation cost; Lucernex already needed `NeedsRecalculation` |
| 2 | `Contract` split across 4 physical tables, 45% tenant custom columns | One contract table + a typed extension mechanism | 258 `Firm_*` columns on the aggregate root is a schema-per-tenant pattern in disguise, incompatible with a shared platform schema |
| 3 | `ExpenseRecovery` across `part1..part4` | One entity, grid as rows | The split is a column-count workaround (`ExpenseRecoveryID` literally appears 4× in the export) |
| 4 | Seven `Text`-typed FKs | Real FKs with an orphan policy | `CON-R-134` |
| 5 | `DELETE_PAYMENTS` + regenerate as the correction path | Append-only ledger with explicit reversals | SOX/SOC 2. **Contingent on `CON-R-010`/open question 1 — confirm Lucernex's actual behaviour first** |
| 6 | `PayTrans*` denormalised mirror on `LandlordInvoiceItem` | A join | `CON-R-133` |
| 7 | Bank account/routing numbers stored plaintext on `PaymentTransaction` and `PaymentReceipt` | Tokenised or vaulted | PCI-adjacent data on a transaction row; also engages Constitution §4.12 |
| 8 | Two escalation engines with no shared vocabulary (`ExpenseEscalation` vs `ExpenseRecovery`'s cap escalation) | Keep both, name them distinctly (`AmountEscalation` vs `CapEscalation`) | They genuinely differ; conflating them would be worse than duplicating |
| 9 | `Contract.Test1Result`…`Test5bResult` as `Text` | Typed enum + a structured test-result record | ASC 842 classification results driving accounting must not be free text |
| 10 | Three platform typos in internal names (`StartingAmout`, `FindStartingAmout`, `ESCALTION`) | Correct spellings, with a migration alias map | Preserve the aliases; do not preserve the typos |

---

## 4.1 Typing hazard register (Constitution §4.4)

Every row **Observed**. Ordered by severity.

| # | Hazard | Location | Severity | Remedy |
|---|---|---|---|---|
| 1 | **Every landed Postgres column is `TEXT`** — 1,163 of 1,194 cross-mapped columns; the other 31 are `VARCHAR(64)` PKs. No numeric, date or boolean column exists in the landed schema | All 33 tables in `_crossmap.tsv`, incl. `sales.GrossSalesAmount`, `sales.NetSalesAmount`, `sales.SalesAdjustment1..6` | **Critical** | Parse and validate every value on ingest; reject unparseable money rather than defaulting to zero. `CON-R-131` |
| 2 | Money fields declared `Text` in the object model itself | `PaymentTransaction.AmountInvoiced`, `.AmountReceived` | **Critical** | Parse to `BigDecimal`; reconcile against `InvoiceAmount` / `ReceivedAmount`. `CON-R-132` |
| 3 | Money, date and boolean as text on the reconciliation grid | `LandlordInvoiceItem.PayTransTotalAmount`, `.LinkAmountAllocated`, `.PayTransEffectiveDate`, `.PayTransIsReceivable` | **High** | Replace the seven `PayTrans*` mirrors with a join. `CON-R-133` |
| 4 | 6-decimal unit rates × large counts | `sTYPE_NUMBER_FRACTION6DIGITS` on `VirtualUsagePeriod`, `UseBasedRentBreakpoint.BreakpointCost1..8` | **High** | `BigDecimal` with explicit scale and `RoundingMode`; never `double`. `CON-R-135` |
| 5 | 188 `sTYPE_PERCENTAGE` fields multiply money in the pro-rata, breakpoint and CPI paths | `ProRataShareRate`, `BreakpointRate1..8`, `IndexBaseFactor`, `CapPercent`, `AllocationPercentage`, `PaymentPercentage` | **High** | Fix scale and rounding at every multiplication step; define a single rounding policy. `CON-R-136` |
| 6 | Seven parent-child FKs declared `Text` | `CON-R-134`'s list | **High** | Real FKs; orphan policy |
| 7 | `NoZeroDef` fields imply zero ≠ unset, but the platform's other 500 measures have no such distinction | `ExpenseRecovery`, `ExpenseRecoveryItem` | Medium | Nullable `BigDecimal` for all recovery measures. `CON-R-137` |
| 8 | `ExpenseRecovery.BaseYear` typed `Text`, not a year | `ExpenseRecovery` | Medium | Typed year |
| 9 | `ExpenseEscalation.EscalationMethod` free `Text` as a behavioural discriminator | `ExpenseEscalation` | Medium | Enum. Value space unknown — open question |
| 10 | `SLSummary.SLRemainingAssetBalance` typed `Percent or Currency` — one field, two units | `SLSummary` | Medium | Two fields, or a value+unit pair |
| 11 | `EscalationIndex.IndexAmount` typed `Percentage` for what is normally an index level | `EscalationIndex` | Medium | Resolve level-vs-rate first (`CON-R-042`), then type accordingly |
| 12 | Check currency may differ from transaction currency with no FX rate on the row | `PaymentTransaction.CodeCheckCurrencyTypeID` vs `CodeCurrencyTypeID` | Medium | Carry rate + gain/loss, as `SLPeriod` already does |
| 13 | `Contract.Test1Result`…`Test5bResult`, `FinalResult`, `ContractAmendment`/`ExpenseSchedule.AdjustmentMethod` all `Text` | `Contract`, `ExpenseSchedule` | Low | Enums |
| 14 | JSON blob with no schema | `ExpenseRecoveryItemMapping.JSONConfigText` | Low | Per Constitution §4.4, JSON numerics stored as strings and parsed — applies here directly |

**Note on §4.4's second clause.** The Constitution requires JSON numeric attributes to be *stored as
strings and parsed*. Lucernex's landed schema does something superficially similar — everything as
`TEXT` — but without the discipline: there is no schema, no validation, and no distinction between
"deliberately a string that will be parsed as a decimal" and "untyped". ASG Edge+ should not read
hazard #1 as precedent for §4.4's approach; it is the failure mode §4.4 exists to prevent.

---

## 5. Blocking items

### 5.1 Blocking — contract status is not the contract lifecycle

**This blocks the Week-12 freeze.** Live capture on 2026-09-10
([`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md)) found
`Contract Status Code` holds **three** values — `AI Abstracted`, `Active`, `Inactive` — none of
which is one of BRD-24 FR-010's five lifecycle stages (Open → Active → Possession → Paying Rent →
Closed). The full investigation is in
[`contract-hierarchy.md` §7](contract-hierarchy.md#7-contract-status-vs-the-brd-24-lifecycle--the-answer).
The finding in one line: **Lucernex has two status axes and ASG Edge+ has been treating them as
one.**

| Axis | Lucernex | ASG Edge+ must |
|---|---|---|
| **Record state** | `CodeContractStatusID` — 3 values, `Active` platform-protected against deletion | Keep as a small seeded enum with undeletable values. **Split `AI Abstracted` out** — it is provenance, not state; a contract can be AI-abstracted *and* active |
| **Lifecycle stage** | Not stored. Derived from `PossessionBeginDate`/`PaymentsBeginDate`/`ActualStartDate`/`ExpireDate`, over `ProjectEntity`'s six-phase `Project Phase Code` enumeration driven by `ProcessTimelineTemplate` → `ProcessTimeline` milestones | **Store it explicitly** as FR-010's five-state machine, with the dates as *evidence* for each transition rather than as the state itself |

Three facts make this actionable rather than speculative:

1. **The ASG tenant already built the missing field.** `Contract.Firm_LeaseStatus`
   (`sTYPE_CUSTOM_CODE_FIELD`, Firm scope) with a `Firm_LeaseStatusNotes` companion sits in the same
   `Contract / Contract Info` sub-group as the platform's `CodeContractStatusID`. A tenant does not
   duplicate a platform field unless the platform field cannot express what they need. **Observed.**
   This is the third possibility the registry did not list: BRD-24 describes a real requirement the
   incumbent does not satisfy, and the tenant has already patched around it.
2. **`Project Phase Code` is not tenant-editable.** It is absent from the 207 Firm Drop Downs while
   being used by eleven objects. Same pattern as `Work Flow Status Code`. A rebuild that treats
   lifecycle stage as a configurable master list will diverge from the incumbent's model, which
   treats it as engine-governed. **Observed.**
3. **`AI Abstracted` says the automated abstraction path is already in production.** BRD-24's
   abstraction workflow (PJ-05 → PJ-09, and the Lease Admin Request's "Abstract Lease Document"
   step) must represent human-versus-AI abstraction as a first-class distinction, not as a status
   value. **Observed.**

**Recommendation.** Invert Lucernex's design: store the state, record the date and the actor that
justified each transition. A derived state has nowhere to hang FR-029's "who, what, when, why" audit
requirement; a stored state machine does. Model:

```
ContractLifecycleState   enum { OPEN, ACTIVE, POSSESSION, PAYING_RENT, CLOSED }   // FR-010, stored
ContractRecordState      enum { ACTIVE, INACTIVE }                                // seeded, protected
abstractionSource        enum { HUMAN, AI, MIXED }                                // was "AI Abstracted"
ContractStateTransition  { fromState, toState, effectiveDate, evidenceDateField,
                           actorId, reason, occurredAt }                          // FR-029
```

**Open before the freeze:** the value list of `Project Phase Code`, and the value list of the
tenant's `Firm_LeaseStatus` Client Drop Down. If the latter already matches FR-010's five stages,
FR-010 is half-specified by the incumbent and the mapping is mechanical. Both are in
[`contract-hierarchy.md`](contract-hierarchy.md#open-questions) open questions 1 and 2.

One naming trap: **BRD-24's "Open" is ambiguous.** Lucernex's `OpenYear` / `ActualStartDate` mean
*store* opening (PJ-10 "Store opens"), which sits **after** Possession, not before Active. If
FR-010's "Open" means "contract record created", the two orderings conflict. Confirm with the
business.

### 5.2 The one thing that needs a decision

**Does ASG Edge+ store a contract-level primary vendor?**

Lucernex does not (`CON-R-020`). Vendors live on `PaymentTransaction`, `ExpenseSetup`,
`ExpenseVendorAllocation`, `ScheduledOffset`, `LandlordInvoice` and `SecurityDeposit`. BRD-24's
PJ-12 — *"Create or link a vendor. Capture client-specific payment details, AP details"* — reads as
a contract-level step.

| Option | Consequence |
|---|---|
| **A. Match Lucernex** — no contract-level vendor; PJ-12 creates/links the vendor and sets it as the default on the contract's expense clauses | Faithful to the source; a contract's vendor set stays derived and can legitimately differ per clause. PJ-12's "is this contract ready to pay?" check becomes "do all clauses have a payee?" |
| **B. Add a contract-level primary vendor** | Simpler UI and a cleaner readiness check, but creates a second source of truth that will drift from the per-clause vendors, and complicates a master-lease/sublease where landlord and subtenant are different parties |

**Recommendation: A**, with an explicit `contractPaymentReadiness` derived check. B's readiness
benefit is achievable without the drift risk. Either way this needs an ADR, because it is a
deliberate divergence from the source system and it lands inside the Week-12 freeze.

---

## 6. Master data this module depends on (Configuration-Service, MDM-01)

Roughly 40 code lists. **None of their members are known** — this is the largest single body of
missing information in the module, and all of it is readable from screen 007's routes
(`FirmCodeList.jsp` / `CustomCodeTableEdit.jsp`).

| Domain | Code lists |
|---|---|
| Expense classification | Expense Group, Expense Type, Expense Category, Expense Acct |
| Frequency & timing | Frequency Code, PR Frequency, Month Frequency, Proration Method |
| Percentage rent | Percentage Rent Type, Sales Group, Sales Type, Sales Category, Unit Sales Type, Store Type, Exclusion Cap |
| Use-based rent | Usage Group, Usage Type, Usage Category, Usage Unit Type, Use Rent Model Type |
| Recovery | Recovery Type, Recovery Group, Recovery Item Group, Recovery Item Type, Recovery Section, Cap Type, Calculation Method, Exp Rec Based On, Pro Rata Share Method, Base Year Amount Type, Escalation Payment Method, Approval Status (Expense Recovery) |
| Escalation | Escalation Type, Escalation Category, Escalation Group, Index Type, Index Source, Index Group, CPI Index, Adjustment Method |
| Payment | Payment Method, Approval Status, Source Entity, Currency Type, Receipt Type, Invoice Status |
| Accounting | ASC 842 Schedule Type, IFRS 16 Schedule Type, Straight Line Schedule Type, Accounting Method, Accounting Adjustment Type, Accrual Type |
| Contract | Contract Type/Group/Category/Use, Agreement Type, Holding Interest, Deal Type, Asset Class, Contract Status, Term Type, Term Status, Amendment Type/Group, Building Area Unit |
| Other | Covenant Category/Group/Status/Type/Template, Co Tenancy Group/Type, Security Deposit Group/Status/Type, Guarantee Type, Allowance Group/Type, Alt Rent Math, Offset Group/Type, Financial Adjustment Status, Plan Forecast Based On, Plan Forecast Group |

Three of these — **Percentage Rent Type**, **Source Entity**, **Agreement Type** — are load-bearing
for the schema itself, not just for validation. They appear in the top-five open questions.

---

## 7. What to freeze at Week 12, and what can stay additive

| Freeze now (structural) | Can be additive later |
|---|---|
| **Two separate status fields** — `ContractRecordState` and `ContractLifecycleState` — plus `abstractionSource` and a `ContractStateTransition` log (§5.1) | Additional lifecycle stages, additional record states |
| The four-layer pattern and its layer discriminators | Additional clause instantiations beyond the five |
| `Contract`'s FK set and the `masterContractId` self-reference (with the hierarchy decision from `contract-hierarchy.md` open question 1) | Contract classification code lists |
| Payable/receivable direction on money, not on the contract (`CON-R-019`) | Additional payment methods |
| The five date axes on a posted transaction (`CON-R-103`) | Additional date fields |
| Tier collection instead of eight slots | More tiers |
| The recovery statement as rows, with `perspective` and `basis` as data | More measures, more perspectives |
| The GL coding shape — **blocked on `CON-R-111`** | More account segments |
| `BigDecimal` with a fixed rounding policy everywhere | — |
| The receipt allocation table (`CON-R-118`) | — |
| `AbstractedProvision` as a first-class entity (§3.5) | More provision types |

**The four questions that block the freeze**, because their answers change the schema rather than
its contents:

0. **§5.1 — is contract lifecycle a stored state machine or a derived one?** Answered here:
   it must be stored, and it must be a *second* field alongside record state. What remains open is
   the value list of `Project Phase Code` and of the tenant's `Firm_LeaseStatus`.
1. `contract-hierarchy.md` open question 1 — does anything use `MasterContractID` beyond layout
   display? Determines whether the contract entity needs a hierarchy path, an edge allocation
   percentage and a cycle guard.
2. `CON-R-111` / `payment-lifecycle.md` open question 2 — are `AccountNumber1..8` eight segments of
   one account or eight split-coding lines? Determines the GL coding entity's shape and cardinality.
3. `setup-schedule-transaction-pattern.md` open question 6 — is the `Virtual*` layer a query, a
   materialised view, or a cached table? Determines whether L3 needs persistence and invalidation
   at all.

---

## Open questions

Ranked by what most blocks the Week-12 freeze.

1. **What is the value list of `Project Phase Code`, and of the tenant's `Firm_LeaseStatus`?**
   (§5.1.) Together they settle whether FR-010's five stages already exist in the incumbent in some
   form. `Project Phase Code` is not tenant-editable and cannot be read from `FirmCodeList.jsp`;
   `Firm_LeaseStatus` is a Client Drop Down, readable from `CustomCodeTableEdit.jsp`.
2. **Does `MasterContractID` drive any financial behaviour?** (Rollup, allocation, depth > 1.)
3. **`AccountNumber1..8` — segments or split lines?** (`CON-R-111`.)
4. **Is `Virtual*` a query, a view, or a cached table?**
5. **Contract-level vendor: option A or B?** (§5 — needs an ADR either way.)
6. **`CON-R-058` — marginal band or simple excess for percentage-rent tiers?** Does not change the
   schema, but every percentage-rent number depends on it and it blocks ASG component #22's test
   corpus.
7. **`CON-R-094` / `CON-R-095` — where do the CAM cap and base year enter the waterfall?** Same:
   not schema, but blocks the CAM test corpus.
8. **Which of the ~40 code lists are Hub-global and which are firm-overridable?** Directly engages
   the unwritten Hub→Spoke publish/accept mechanism. `CodeExpenseType` is the hard case: its GL
   account numbers are unavoidably firm-specific while its accounting-treatment bindings should be
   global.
9. **Do the core financial tables (`payment_transaction`, `expense_setup`, `expense_schedule`,
   `expense_recovery_part*`) land as `TEXT` like the 33 tables in `_crossmap.tsv`?** None of them
   appear there. If they do, hazard #1 applies to the whole migration; if they are properly typed,
   it applies only to the reference tables.
