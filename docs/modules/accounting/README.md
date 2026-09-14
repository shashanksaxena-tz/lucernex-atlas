# Accounting engine — module overview

**Stated up front.** Lucernex does not have "an ASC 842 module" and "an IFRS 16 module". It has **one
lease-accounting engine** built on a single summary/period pair — `SLSummary` (`s_l_summary`, 134
fields) and `SLPeriod` (`s_l_period`, 79 fields) — and three mutually exclusive boolean flags on the
summary (`IsSLSchedule`, `IsASC842Schedule`, `IsIFRS16Schedule`) that say which standard a given
schedule was generated under. Classification (operating vs. finance) is a *separate* record,
`ContractFinancialTest` (`contract_financial_test`, 93 fields), which runs the five ASC 842 tests and
holds both the ASC 842 and IFRS 16 measurement results side by side. A *third*, older test — the
"Cap Lease Test" — still lives directly on `Contract` as `Test1Result`…`Test5aResult`/`Test5bResult`
and is the ASC 840 predecessor. All three coexist in the schema.

Everything else in this module is plumbing around those two facts: where the cash flows come from
(`ExpenseSetup` → `ExpenseSchedule`, routed to a schedule by `CodeExpenseType`), what adjusts them
(`AcctingAssumptionAdjust`, `FinancialAdjustment`, `Covenant`), what rate discounts them
(`DiscountRate` → `Contract.ComputedSLDiscountRate`), when the engine must re-run
(`SLSummary.NeedsRecalculation`), and how the result reaches the GL (twenty numbered
`ExportAcctNNumber` slots per schedule type).

And the engine's output is **not auto-published**: the tenant runs a three-step
`ASC 842 Schedule Review/Approval` workflow — internal review, ASG approval, then client approval —
before a schedule counts. In production ASG uses **one** of the three standards: the ASC 842
schedule-type table holds a single row, and the straight-line and IFRS 16 tables are empty.

*Evidence class for this paragraph: **Observed** — `_lucernex_objects_summary.txt`;
`_xlsx_lucernex_jcrew.txt` "Field Inventory" sheet (vendor field definitions);
`docs/data-fields/all-fields.csv`; and, for the workflow, the running tenant at build `26.08.0.46`
captured 2026-09-10 (`docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`).*

## Contents

| File | What it holds |
|---|---|
| [`data-model.md`](data-model.md) | The 19 objects this module owns, their PG tables, field counts, and FK edges. |
| [`rules.md`](rules.md) | `ACC-R-001`…`ACC-R-045` — every rule in trigger / input / computation / output / confidence form. |
| [`asc-842.md`](asc-842.md) | The five classification tests, the measurement surface, schedule types, remeasurement/modification. |
| [`ifrs-16.md`](ifrs-16.md) | IFRS 16 and — precisely — the four places the data model diverges from ASC 842. |
| [`straight-line.md`](straight-line.md) | The summary/period pattern, what a period row holds, suspension and hold flags, "Modify Straight Line Status". |
| [`computed-vs-input-fields.md`](computed-vs-input-fields.md) | **666 accounting fields classified INPUT / COMPUTED / CODE-TABLE / ACTION / DEAD / FK / SYSTEM, with evidence per row.** The primary input to the ASG Edge+ rule engine. |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | What ASG Edge+ has, must build, should deliberately differ on, and the decisions blocking it. |
| [`../../mindmap/accounting-tree.json`](../../mindmap/accounting-tree.json) | The module as a nested tree for the interactive mind map — drills from the module down to individual fields, types, constraints and `ACC-R-NNN` rules. |

## The engine in one picture


```
CodeExpenseType ──(CodeSLScheduleID / CodeASC842ScheduleID / CodeIFRS16ScheduleID)──┐
       │                                                                            │  routes each
       ▼                                                                            │  cash flow to
ExpenseSetup ──1:N──► ExpenseSchedule  ── period cash amounts ─────────────────┐     │  a schedule
       │                                                                       │     │
       ├──► AcctingAssumptionAdjust  (payment-level accounting-only overlay)   │     │
       │                                                                       ▼     ▼
Covenant ──(Purchase Option / Cancellation Option / RVG)──► ContractFinancialTest ──► SLSummary ──1:N──► SLPeriod
       │                                                        │  five tests            │ header             │ one row per
FinancialAdjustment ────────────────────────────────────────────┘  → Operating|Finance   │                    │ fiscal period
                                                                                         │                    │
DiscountRate (Portfolio → Firm) ──► Contract.ComputedSLDiscountRate ─────────────────────┤                    ▼
                                                                                         │            ExportAcctNNumber ×20 → ERP GL
FiscalPeriod (fiscal calendar, 12- or 13-period) ────────────────────────────────────────┴──► RecalcOverrideNotes

Program (Portfolio) ── SLDiscountRate · FairValueThreshold · RemainingEconomicLifeThreshold
                    ── SL{Asset,Cash,Expense}AmortizeMethod  (PER_DAY | PER_PERIOD)
                    ── SLProrate35As28 · SLMatchYearEnds · FiscalYearEnd · 14 FX rate types
                       └──► defaults every policy the schedule above is generated under

SLSummary ──► "ASC 842 Schedule Review/Approval" workflow ──► IsApproved
              submit ► initial review ► approve (ASG) ► approve (Client)
```

*Evidence class: **Derived** from the FK types in `_lucernex_objects_summary.txt` and the vendor field
definitions in `_xlsx_lucernex_jcrew.txt`. The arrows are the documented relationships; the ordering
of engine steps is inferred and is called out where it matters in [`rules.md`](rules.md).*

### The same engine, as the user meets it

![The `Accounting Info` group on a live BBW contract. The engine above is split across seven screens: `Accounting Details`, `Capital Lease Test`, `Straight-Line Rent`, `Accounting Assumptions`, `ASC 842 Test`, `ASC 842 Rent Schedule`, `IFRS 16 Rent Schedule`. ASC 842 and IFRS 16 get separate schedule screens, and the legacy `Capital Lease Test` sits alongside the current `ASC 842 Test` rather than being replaced by it.](../../assets/screenshots/bbw-enduser/ct-28-capital-lease-test.jpg)

**Observed**, one contract, `(ASG)BBW`, build `26.09.0.113`. Also visible: the `Actions` rail on this
screen carries only `Edit`, `Printable View`, `Save to Document` and `Link` — none of the generator
buttons that appear on Contract Summary. **Derived:** the accounting screens *read* the engine; the
commands that drive it are placed on a different layout
([`../../features/page-layouts/`](../../features/page-layouts/#action-buttons-render-in-a-right-hand-actions-rail-and-they-are-per-layout)).

## Where this module's boundary sits

**In scope.** Lease classification (both the ASC 842 five-test and the legacy Cap Lease Test), initial
and subsequent measurement, the straight-line/ASC 842/IFRS 16 period schedules, accounting
assumptions and their adjustments, discount-rate selection, impairment, remeasurement and
modification, the roll-forward disclosure surface, expense accruals, and the GL export account
mapping.

**Out of scope but adjacent** (documented only where the accounting engine consumes them):
`ExpenseSetup`/`ExpenseSchedule` (the rent engine that produces the cash flows),
`PaymentTransaction` (cash out), `PercentageRent`/`UseBasedRent`/`Sales` (variable rent),
`ExpenseRecovery` (CAM reconciliation, 565 fields — the single largest object in the product),
`PropertyTax*`.

## Non-obvious findings a rebuild must not miss

1. **The three schedule-type code tables are byte-identical in shape.** `CodeASC842Schedule`,
   `CodeIFRS16Schedule` and `CodeSLSchedule` each carry exactly `ShortName`, `ActualLongName`,
   `Inactive`, `DontAmortizeAssetValue`, and `ExportAcct1Number`…`ExportAcct20Number`. Nothing
   distinguishes them structurally — the difference is entirely which FK column points at them.
   Confirmed from the UI on 2026-09-10: all three render the same four columns, `Type*`,
   `Description`, `Don't Amortize Asset Value`, `Inactive`. *(Observed,
   `_lucernex_objects_summary.txt` and `docs/data-model/code-table-registry.md`.)*
2. **`AlternateRentSchedule.SuspendSL` is dead.** Vendor definition: *"This field is no longer used."*
   Do not rebuild suspension from it. *(Observed, `_xlsx_lucernex_jcrew.txt`.)*
3. **Every non-key column in the PostgreSQL export is `TEXT`.** Of 7,069 typed columns in the jcrew
   export, 6,882 are `TEXT` — currency and percentage included — and the other 187 are
   `VARCHAR(64) NOT NULL`, every one of them a primary key (`SLSummaryID`, `ContractID`, …).
   Lucernex's own persistence layer gives you no numeric typing to inherit.
   *(Observed, `_xlsx_lucernex_jcrew.txt`, `PG Data Type` column.)*
4. **`SLSummary.SLRemainingAssetBalance` and `Asset.RemainingAssetBalance` are magnitude-typed.**
   Value 0–100 ⇒ interpreted as a percentage; ≥ 100.01 ⇒ interpreted as currency; the user may
   override the guess. This is a genuine data-integrity hazard and is called out in
   [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md). *(Observed, vendor help text.)*
5. **Two "Modify Straight Line Status" controls exist**, and they are not the same thing — one is an
   admin utility at `/en/admin/lxadmin/SLDemoTweaks.jsp`, one is a Contract summary-page button
   (`Contract.ModifyStraightLineStatus`, `sTYPE_SUBMITBUTTON`). See
   [`straight-line.md`](straight-line.md#modify-straight-line-status).

*Findings 6–10 come from live captures of the running tenant on 2026-09-10 and outrank anything
inferred from the offline dumps.*

6. **A generated schedule is a candidate, not a result.** The tenant runs a live workflow,
   `ASC 842 Schedule Review/Approval`, with three ordered form steps — Initial Review → Approve (ASG)
   → Approve (Client) — each bound to its own `ASR` form layout. `SLSummary.IsApproved` is the
   terminus of that chain, not a checkbox. A schedule therefore has a *state*
   (`draft → submitted → under review → ASG-approved → client-approved`), and only the last of the
   five is representable in the schema. ⚠ The form type is attachable to `Portfolio` and
   `RE Contract` but **not** `Equipment Contract`, so how equipment schedules get approved is an open
   question. *(Observed; `docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`.)*
7. **`Program` — the Portfolio — is the accounting engine's policy carrier**, and the first version of
   this folder missed it. It holds the default discount rate, both ASC 842 thresholds, **three**
   independent amortisation-basis switches (`PER_DAY` / `PER_PERIOD`, the live API's
   `GaapAmortizeMode`), a 28-day proration switch, the fiscal year end, and fourteen FX rate-type
   selectors — seven schedule columns × revaluation/translation. See
   [`data-model.md`](data-model.md#program--the-portfolio-level-policy-carrier) and `ACC-R-056`…`059`.
   *(Observed, `_xlsx_lucernex_jcrew.txt` + `docs/data-model/graphql-api.md`.)*
8. **`COMPUTED` is a first-class type in Lucernex's own API.** The 448 `sTYPE_*` codes project onto a
   10-value canonical `FieldType` enum — `BOOLEAN COMPUTED DATE DATETIME FK FLOAT INTEGER MONEY
   PERCENTAGE STRING` — which means the INPUT/COMPUTED split in
   [`computed-vs-input-fields.md`](computed-vs-input-fields.md) is the platform's own distinction,
   not one imposed from outside. `MONEY` and `PERCENTAGE` are distinct from `FLOAT`, and `BigDecimal`
   is a declared scalar. *(Observed, `docs/data-model/graphql-api.md`.)*
9. **⚠ The engine supports three standards; ASG runs one.** The three schedule-type code tables were
   opened directly: `ASC 842 Schedule Type Code` (`TableType` 2162) holds **exactly one row**,
   `842 Rent`, with `Don't Amortize Asset Value` unchecked. `Straight Line Schedule Type Code` (2161)
   and `IFRS 16 Schedule Type Code` (2163) are both **empty**. Four consequences run through this
   folder: there is one set of twenty GL export slots in play rather than a matrix; `ACC-R-030`
   (`DontAmortizeAssetValue`) is **inert in production** and can never be validated against ASG's
   data; every expense type's routing resolves to `842 Rent`; and any `SLSummary` row with
   `IsSLSchedule` or `IsIFRS16Schedule` true is an orphan whose schedule type was deleted. Whether
   ASG Edge+ builds IFRS 16 at all is now a **business** question, not a technical one.
   *(Observed 2026-09-10; `docs/data-model/code-table-registry.md`.)*
10. **The `TableType` 2000/3000 band hypothesis does not hold for this module.** The registry
   proposes that 3000-band code tables are the behaviour-bearing ones. Checked against the eleven
   `Code*` objects in the schema dump, it is **refuted**: the three schedule-type tables (2161–2163,
   24 fields each, a behaviour flag plus twenty GL slots) and `Issue Type` (2035, 19 fields) are all
   2000-band, while `Sales Type` (3012) is a bare three-column lookup and `Problem` (3001) is close
   to one. Only `Expense Type` (3013) supports the claim. **Derived: the band is a registration-order
   artefact.** Behaviour-bearing-ness must be read per object — which matters for sizing MDM-01.
   See [`data-model.md`](data-model.md#the-20003000-tabletype-band-hypothesis--refuted).
