# IFRS 16 — and exactly where it diverges from ASC 842

**Stated up front.** In the Lucernex data model IFRS 16 is **not a second engine** — and in the live
tenant **it is not configured at all**. The `IFRS 16 Schedule Type Code` table (`TableType` 2163) is
empty: "No rows to display". With no schedule type to point at, no IFRS 16 schedule can be generated
and no expense type can route to one. There is also no IFRS 16 approval workflow, where ASC 842 has
one. The capability is present in the product and unused by ASG.

**So the question this page answers has changed.** It is no longer "how does Lucernex do IFRS 16" —
it is "should ASG Edge+ build IFRS 16 at all". That is a business decision, not a technical one, and
everything below is the technical input to it. It is a second
*schedule type family* (`CodeIFRS16Schedule`), a second *routing FK* on five objects
(`CodeIFRS16ScheduleID`), a second *measurement column set* on `ContractFinancialTest` (`IFRS16*`),
and a *flag* on the schedule header (`SLSummary.IsIFRS16Schedule`). Everything else — the five
classification tests, the period row, the roll-forward, the maturity ladder, the GL export — is
shared verbatim. There is **no IFRS-16-specific classification test, no IFRS-16 practical-expedient
gate, and no IFRS-16 single-lease-expense flag** anywhere in the 223-object dump.

*Evidence class: **Observed** — `_lucernex_objects_summary.txt` (the complete field lists of all 223
objects), cross-checked against `docs/data-fields/all-fields.csv` (all 6,158 catalogued leaves) and
the vendor definitions in `_xlsx_lucernex_jcrew.txt`. The claim that no IFRS-16-only mechanism exists
is a negative result from exhaustive search, not an assumption.*

## The live configuration state

**Observed**, 2026-09-10, `FirmCodeEdit.jsp` (`docs/data-model/code-table-registry.md`):

| `TableType` | Code table | Rows in this tenant |
|---:|---|---|
| 2163 | IFRS 16 Schedule Type Code | **0** — "No rows to display" |
| 2162 | ASC 842 Schedule Type Code | 1 — `842 Rent` |
| 2161 | Straight Line Schedule Type Code | **0** |

Consequences, all **Derived** from that plus the schema:

| Consequence | Why |
|---|---|
| No IFRS 16 schedule can exist | `SLSummary.CodeIFRS16ScheduleID` has nothing valid to point at |
| `SLSummary.IsIFRS16Schedule` should be false on every row | ⚠ a true row would mean a schedule survived deletion of its schedule type — worth querying |
| `CodeExpenseType.CodeIFRS16ScheduleID` must be null everywhere | no target rows exist |
| The `Generate IFRS 16 Rent Schedule` button is inoperable | it would have no schedule type to stamp |
| The seven `IFRS16*` measurement columns on `ContractFinancialTest` are the only IFRS 16 artefacts that could hold data | they are computed on the test record, independently of any schedule |

That last row is the one live technical question: the measurement columns are computed per test
regardless of configuration, so they may well be populated even though no IFRS 16 schedule has ever
been produced.

## The complete IFRS 16 surface

Twelve fields and one code table — and the code table is empty. That is the whole of it.

| Object | Field | Type | Note |
|---|---|---|---|
| `CodeIFRS16Schedule` | (24 columns) | code table | Structurally **identical** to `CodeASC842Schedule` and `CodeSLSchedule`: `ShortName`, `ActualLongName`, `Inactive`, `DontAmortizeAssetValue`, `ExportAcct1Number`…`ExportAcct20Number` |
| `SLSummary` | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Routing |
| `SLSummary` | `IsIFRS16Schedule` | `sTYPE_CHECKBOX` | *"This flag indicates that the schedule is an IFRS 16 schedule."* |
| `ContractFinancialTest` | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Labelled "IFRS 16 Schedule **Selector**" |
| `ContractFinancialTest` | `IFRS16CalcAggValOfLeaseNoAdj` | `sTYPE_MONEY` | |
| `ContractFinancialTest` | `IFRS16CalcAggValueOfLease` | `sTYPE_MONEY` | |
| `ContractFinancialTest` | `IFRS16CalcPVOfFinTermsNoAdj` | `sTYPE_MONEY` | |
| `ContractFinancialTest` | `IFRS16CalcPVOfFinancialTerms` | `sTYPE_MONEY` | |
| `ContractFinancialTest` | `IFRS16InitialAssetBalance` | `sTYPE_MONEY_MATH_OPERATION` | |
| `ContractFinancialTest` | `IFRS16InitialLiabilityBalance` | `sTYPE_MONEY_MATH_OPERATION` | |
| `ContractFinancialTest` | `IFRS16NetLeaseLiabilityBalance` | `sTYPE_MONEY_MATH_OPERATION` | |
| `AcctingAssumptionAdjust` | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Routing |
| `Covenant` | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Routing |
| `CodeExpenseType` | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Routing |
| `Contract` | `GenerateIFRS16Schedule` | `sTYPE_SUBMITBUTTON` | Label "Generate IFRS 16 Rent Schedule" |

The `sCODE_IFRS16_SCHEDULE` field type appears exactly **5 times** in the whole 6,158-leaf Data Fields
catalog — the same count as `sCODE_ASC842_SCHEDULE`, one more than `sCODE_SL_SCHEDULE` (4). *(Observed,
`docs/data-fields/INDEX.md` field-type legend, lines 105–107 and 123.)*

## The nine divergence points

| # | Divergence | ASC 842 side | IFRS 16 side | Confidence |
|---|---|---|---|---|
| 1 | **Accounting dates** | `ContractFinancialTest.Topic842BeginDate` / `Topic842EndDate` are explicitly ASC-842-named (*"the date your organization is adopting ASC 842"*) | **No IFRS 16 equivalent exists.** The IFRS 16 measurement columns must therefore share the Topic 842 dates | **Observed** (the fields simply do not exist) |
| 2 | **Classification** | Five tests, `Test1Result`…`Test5Result`, `FinalResult` = Operating \| Finance | **Nothing.** No IFRS-16 classification record. IFRS 16 has no lessee classification, so this is arguably correct | **Observed** |
| 3 | **Practical expedients** | `Contract.IsShortTerm`, `Contract.IsLowAssetValue` (both `sTYPE_CHECKBOX`); `Asset.IsShortTerm`, `Asset.IsLowAssetValue` (both `sTYPE_NULL_CHECKBOX`, i.e. **three-state**) | Same two fields — they are **not** namespaced to either standard, even though short-term and low-value are IFRS 16 § 5–6 exemptions | **Observed**; that they are unnamespaced is the finding |
| 4 | **Asset three-state vs. contract two-state** | `Contract.IsShortTerm` / `Contract.IsLowAssetValue` = `sTYPE_CHECKBOX` (true/false) | `Asset.IsShortTerm` / `Asset.IsLowAssetValue` = `sTYPE_NULL_CHECKBOX` (true/false/**unset**) | **Observed**, `all-fields.csv` lines 1167–1168 and 3654–3655 |
| 5 | **Single lease expense** | ASC 842 operating leases produce a single straight-line lease cost | `SLSummary.SingleLeaseExpenseAdjustment` and `SleBeforeMidRemeasure` ("Straight Line Expense Before Mid-period Remeasurement") exist but are **not** IFRS-16-scoped; IFRS 16 has no single-lease-expense model for lessees at all | **Observed** field names; **Inferred** that these are ASC 842 operating-lease fields |
| 6 | **Discount rate** | `DiscountRate.CodeAccountingMethodID` scopes a rate to Finance or Operating; vendor: *"If you leave the field blank, the discount rate will apply to both Finance and Operating."* | **No standard dimension on `DiscountRate` at all.** A tenant reporting under both standards with different IBRs has nowhere to put the second rate except a contract-level override | **Observed** |
| 7 | **Schedule type behaviour** | `CodeASC842Schedule.DontAmortizeAssetValue` | `CodeIFRS16Schedule.DontAmortizeAssetValue` — identical column, independent value | **Observed** |
| 8 | **Review / approval gate** | A live workflow, `ASC 842 Schedule Review/Approval`, with three form steps and four `ASR` layouts | **No IFRS 16 equivalent exists.** `Manage Work Flows` lists exactly four workflows in this tenant — ASC 842 Schedule Review/Approval, Lease Admin Request, Rent Payment Review/Approval, User Request — and none is IFRS-16-named | **Observed**, tenant build `26.08.0.46`, 2026-09-10 |
| 9 | **Amortisation basis** | `Program.SLAssetAmortizeMethod` is explicitly scoped: *"This setting impacts only ASC 842 Finance leases."* | **Undefined for IFRS 16.** The cash and expense switches carry no standard restriction, but the asset one names ASC 842 only — so what governs IFRS 16 asset amortisation is unstated | **Observed** for the restriction; the IFRS 16 gap is a negative result |

## What "runs both standards" actually means here

`ContractFinancialTest` computes and stores the ASC 842 *and* IFRS 16 measurement columns on every
test record, unconditionally — the `docs/data-fields/INDEX.md` entry for the object states it:
*"the near-identical field pairs prefixed 'ASC 842' and (by pattern) 'IFRS 16' show Lucernex runs the
same lease-accounting calculation twice per contract, once under each standard, so a tenant reporting
under only one standard still carries both sets of fields."*

But the **schedule** side is not symmetric. `SLSummary` has one `CodeAccountingMethodID`, one
`DiscountRate`, one set of balances, and three mutually-suggestive-but-not-mutually-exclusive flags.
So:

- **Measurement** is computed twice per contract, in one row. *(Observed.)*
- **Schedules** are generated separately per standard, into separate `SLSummary` rows, by separate
  buttons (`GenerateFASBSchedule`, `GenerateIFRS16Schedule`, `GenerateStraightLineRent`). *(Observed —
  three distinct `sTYPE_SUBMITBUTTON` fields on `Contract`.)*
- Nothing in the schema **links** an IFRS 16 `SLSummary` to its ASC 842 sibling. They are siblings
  only by sharing a `ContractID`. *(Observed — no cross-reference column exists.)*

## What a rebuild must add that Lucernex does not have

*Evidence class: **Inferred** — accounting-standard reasoning applied to the observed schema gaps.
Every item here is a gap, not a copy target.*

1. **An IFRS 16 accounting begin/end date pair.** Reusing `Topic842BeginDate` forces the IFRS 16
   transition date to equal the ASC 842 adoption date, which is wrong for any entity that adopted the
   two standards on different dates (IFRS 16: 2019; ASC 842: 2019 public / 2022 private).
2. **Standard-scoped practical-expedient elections.** Short-term and low-value are IFRS 16 exemptions
   with specific thresholds; ASC 842 has only the short-term expedient and no low-value expedient at
   all. One shared `IsLowAssetValue` checkbox cannot express both policies.
3. **A standard dimension on the discount rate.** IFRS 16 § 26 and ASC 842-20-30-3 permit different
   rates; `DiscountRate` cannot hold both.
4. **An explicit standard discriminator on the schedule**, replacing three independent Booleans, so
   that "one active schedule per standard per contract" is enforceable rather than conventional.
5. **A sibling link between the standards' schedules for the same contract and period**, so a
   dual-reporting entity can reconcile them.

## Open questions

Ranked.

1. **⚠ Does ASG report under IFRS 16 at all — and does it intend to?** With the schedule-type table
   empty and no IFRS 16 workflow, the incumbent is not doing it today. **This is a business question
   and it decides whether any of this page becomes code.** Everything below is contingent on it.
2. **(resolved 2026-09-10)** *Is IFRS 16 configured?* — **No.** `TableType` 2163 is empty.
3. **(resolved 2026-09-10)** *Is there an IFRS 16 review/approval process?* — **No.** Four live
   workflows, one ASC-842-named, no IFRS-16 counterpart.
4. **Are the IFRS 16 measurement columns nonetheless populated?** They are computed on the test
   record independently of schedule configuration, so they may hold data even with no schedule type
   configured. Query `contract_financial_test` for non-null `IFRS16InitialLiabilityBalance`. **The
   sharpest remaining technical question on this page** — it separates "IFRS 16 is dead schema" from
   "IFRS 16 measurement runs silently and nobody looks at it".
5. **What governs IFRS 16 asset amortisation?** `Program.SLAssetAmortizeMethod` says it affects
   *"only ASC 842 Finance leases"*, and there is no IFRS 16 counterpart column.
6. **(blocked) Does the IFRS 16 schedule use `Topic842BeginDate` / `Topic842EndDate`?** Cannot be
   tested in this tenant — with no IFRS 16 schedule type configured, no IFRS 16 schedule can be
   generated. Needs a tenant where IFRS 16 is set up, or a vendor answer.
7. **Do `Asset.IsShortTerm` / `Asset.IsLowAssetValue` (three-state) override
   `Contract.IsShortTerm` / `Contract.IsLowAssetValue` (two-state), or the reverse?** The three-state
   type strongly suggests "unset ⇒ inherit from contract", but nothing documents it.
8. **(blocked) What actually differs between an ASC 842 schedule and an IFRS 16 schedule at run
   time?** Given identical code tables and an identical period row, the only observable difference
   the schema permits is the accounting method and the GL account slots. Not testable here for the
   same reason as question 6.
9. **(blocked) Is `SingleLeaseExpenseAdjustment` used on IFRS 16 schedules?** If it were, that would
   be a bug — IFRS 16 lessees have no single-lease-expense model. No IFRS 16 schedule exists to check.
10. **Can `IsASC842Schedule` and `IsIFRS16Schedule` both be true on one `SLSummary`?** Nothing in the
    schema prevents it. In this tenant both should be false for IFRS 16 on every row — a true value
    would indicate a schedule that outlived deletion of its schedule type, which is worth querying
    for as a data-integrity check regardless.
