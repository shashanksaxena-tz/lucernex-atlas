# Contract financial engine — rules

**Stated up front.** 161 rules, numbered `CON-R-001` … `CON-R-161`, each stated so a rule engine can
consume it: **trigger**, **inputs**, **computation or condition**, **output**, **confidence**.
Downstream modules (accounting, reporting, workflow) should cite these IDs rather than restating the
logic.

## Confidence labels

Per [`../../CONVENTIONS.md`](../../CONVENTIONS.md):

| Label | Meaning here |
|---|---|
| **Observed** | The rule is literally stated by a field name, a UI label, or a declared type in `_lucernex_objects_summary.txt` / `docs/data-fields/`. Includes formulas Lucernex encoded in its own labels (e.g. `Sub Total #1 (C+NC-D)`). |
| **Derived** | Computed or deduced from Observed data — counting, cross-referencing two sources, or a reading with no plausible alternative. |
| **Inferred** | Domain reasoning, naming convention, or analogy. **Not confirmed.** Anything Inferred that touches money must be verified before it becomes code. |

**No rule below was verified against a running Lucernex instance.** Every `Inferred` rule that
affects a monetary result appears in the owning document's `## Open questions`.

---

## 1. The Clause / Schedule / Transaction / Projection pattern

`CON-R-001` … `CON-R-014` — see [`setup-schedule-transaction-pattern.md`](setup-schedule-transaction-pattern.md).

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-001** | Classifying any financial record | The record's field set | If it carries **both** `AmendmentID` **and** `Section`, it is an L0 clause record | `layer = CLAUSE` | Observed |
| **CON-R-002** | Classifying any financial record | The record's field set | If it carries an FK to an L0 object **and** `ProcessedFlag`, it is an L1 schedule row | `layer = SCHEDULE` | Observed |
| **CON-R-003** | Classifying any financial record | The record's field set | If it carries `PostingDate` **and** GL account slots **and** a counterparty FK, it is an L2 transaction | `layer = TRANSACTION` | Observed |
| **CON-R-004** | Classifying any financial record | The object name and field set | If the name is prefixed `Virtual` **and** it has no `RevNumber`/`ModifiedByID`/Firm-scope field, it is an L3 projection | `layer = PROJECTION` | Observed |
| **CON-R-005** | An L0 clause is created or edited | `AmendmentID`, `BeginDate`, `EndDate`, `RevNumber` | A clause's validity window is its own `BeginDate`..`EndDate`; a new `RevNumber` supersedes the prior revision | Effective clause version for a date | Derived |
| **CON-R-006** | Operator invokes a generator command | The L0 clause + its modifiers | The generator materialises L1 rows spanning the clause window | N × L1 rows | Observed (commands exist as `sTYPE_SUBMITBUTTON`) |
| **CON-R-007** | Operator invokes `GENERATE_RENT` (or a sibling) | L1 rows where `ProcessedFlag = false` | Generate L2 transactions from each eligible row; set `ProcessedFlag = true`, `ProcessedDate = now` | N × L2 rows | Derived |
| **CON-R-008** | Generation is requested | `ExpenseSetup.ReadyForPaymentFlag`, `ExpenseSchedule.ReadyForPaymentFlag` | Both must be true for the row to generate | Gate result | Observed (fields exist); gate semantics Inferred |
| **CON-R-009** | Generation is requested | `HoldFlag` at L0, L1 and L2 | Any `HoldFlag = true` in the chain suppresses the row | Suppression | Observed (fields); propagation Inferred |
| **CON-R-010** | Correcting generated output | `DELETE_PAYMENTS`, then `GENERATE_RENT` | The supported correction path is delete-then-regenerate, not in-place edit | Rebuilt L2 set | Derived |
| **CON-R-011** | An L2 row has left the system | `ExportBatchNumber`, `CheckNumber`, `CheckDate` | A row carrying any of these has been exported/settled | Immutability candidate | Observed (fields); enforcement **unverified** |
| **CON-R-012** | Reading an L3 projection | The L0 clause + L1 rows + reported facts | Projections are computed, not authored; a tenant cannot customise them (no Firm-scope fields exist on any `Virtual*` object) | Projection rows | Observed |
| **CON-R-013** | An escalation step is materialised | `PreviousExpenseScheduleID`, `NextExpenseScheduleID` | L1 rows form a doubly-linked list; each row carries `PreviousAnnualAmount`/`AnnualAmount`/`NextAnnualAmount` | Auditable step chain | Observed |
| **CON-R-014** | An L2 row is written | `SourceEntityTable`, `CodeSourceEntityID` | Every transaction records which generator produced it | Provenance | Observed |

---

## 2. Contract identity and hierarchy

`CON-R-015` … `CON-R-029` — see [`contract-hierarchy.md`](contract-hierarchy.md).

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-015** | A contract is created | `FacilityID`, `LocationID`, `OrganizationID`, `ProgramID` | These four FKs key the contract to building, site, debiting org and portfolio | Contract keys | Observed |
| **CON-R-016** | A contract is created | `OrganizationID` | The organization is *"where payments should be debited"* — it determines the GL debit side | GL routing | Observed (Lucernex's own field definition, via 009) |
| **CON-R-017** | A sublease is created | `MasterContractID` | Points at the master lease's `ContractID`. Null ⇒ not a sublease | Hierarchy edge | Observed |
| **CON-R-018** | Traversing `MasterContractID` | The edge | No depth limit, no cycle guard, no role discriminator and no allocation percentage exist on the edge | Hierarchy is unconstrained | Observed (by absence) |
| **CON-R-019** | Determining payable vs receivable | `ExpenseSetup.IsReceivable`, `PaymentTransaction.IsReceivable` | Direction is carried per-clause and per-transaction, **not** on the contract. One contract may be both | Money direction | Observed |
| **CON-R-020** | Resolving a contract's vendors | `PaymentTransaction.VendorID`, `ExpenseSetup.VendorID`, `ExpenseVendorAllocation.VendorID`, `ScheduledOffset.VendorID`, `LandlordInvoice.EmployerID`, `SecurityDeposit.PartyID` | `Contract` has **no** vendor FK; the set is derived from children | Derived vendor set | Observed |
| **CON-R-021** | Resolving a "Vendor" | `VendorID` declared type | `Vendor` is a relabelled `Employer`; `VendorID` has declared type `Employer ID` | Employer record | Observed (009) |
| **CON-R-022** | Determining the discount rate | `CodeAccountingMethodID`, `CodeContractUseID`, geography, schedule length | Look up `DiscountRate` by method + use + country/state + `MinSchedMons`..`MaxSchedMons` band; stamp onto `Contract.DiscountRate` | Discount rate | Derived |
| **CON-R-023** | Determining the fiscal calendar | `Contract.ProgramID` → `FiscalPeriod.ProgramID` | The fiscal calendar is owned by the **portfolio**, not the firm | Period definitions | Observed |
| **CON-R-024** | A retail fiscal period is used | `FiscalPeriod.Is4or5WeekPeriod`, `NumberWeeksInPeriod`, `NumberDaysInPeriod` | Periods may be 4 or 5 weeks (retail 4-5-4), not calendar months | Period length | Observed |
| **CON-R-025** | Computing rent rollups | `ExpenseSchedule` rows | 120 denormalised `sTYPE_MONEY` fields on `Contract` across `{Calendar, Fiscal} × {Base, Total} × {with, without tax} × {Aggregate, Current Annual/Monthly/Period, Next, 3rd–6th, Beyond 5th/6th, Remaining Obligation, Q1–Q4}` | Precomputed rollups | Observed |
| **CON-R-026** | Any rollup is read | — | The rollups are **denormalised and can be stale**; `SLSummary` has explicit `NeedsRecalculation`/`RecalcTriggerDate`, `Contract` has no equivalent | Staleness risk | Derived |
| **CON-R-027** | Applying contract-level tax | `Contract.ContractTaxRate1..4`, `ExpenseSetup.ApplyTax1..4Flag` | Four parallel tax components; each expense clause opts in per component | `CalculatedTaxRate1..4` on the schedule | Derived |
| **CON-R-028** | A contract term option is created | `ContractTermWizard_TermLength`, `_OptionNumber`, `_TermCoverageBeginDate`, `GenerateContractTerms` | Generates N `ContractTerm` rows of the stated length from the stated start | N × `ContractTerm` | Observed |
| **CON-R-029** | Accruing over an option term | `ContractTerm.IncludeTermForAccruals` | Only terms flagged true participate in accrual schedules | Accrual scope | Observed |

---

## 3. Recurring expense: setup and schedule

`CON-R-030` … `CON-R-039` — see [`payment-lifecycle.md`](payment-lifecycle.md).

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-030** | Authoring a recurring expense | `ExpenseSetupWizard_StartDate`, `_EndDate`, `_StartingAmout`, `_AmountType`, `_TypeOfEscalation`, `_EscalateEvery`, `_EscalateAmountRate`, `GenerateExpenseSetup` | The wizard materialises `ExpenseSetup` + `ExpenseEscalation` + the full `ExpenseSchedule` | Clause + schedule | Observed |
| **CON-R-031** | `ExpenseSetupWizard_FindStartingAmout = true` | A known later amount + the escalation rule | Work backwards to derive the starting amount | Starting amount | Inferred (from the label *"Find Starting Amount"*) |
| **CON-R-032** | Determining billing frequency | `ExpenseSetup.CodeFrequencyID`, `NumberOfPayments`, `PaymentDueDay` | Drives the number and spacing of `ExpenseSchedule` rows | Period grid | Derived |
| **CON-R-033** | `ExpenseSetup.IsCustomPaymentCoverage = true` | `CoverageBeginAnnual`, `CoverageBeginQ1..Q4`, `CoverageBeginSemiAnnual1..2`, `PaymentDueAnnual`, `PaymentDueQ1..Q4`, `PaymentDueSemiAnnual1..2` | The same setup record supports annual, quarterly or semi-annual coverage without schema change; explicit month-and-day markers per frequency | Coverage/due grid | Observed |
| **CON-R-034** | `ExpenseSetup.IsPayArrears = true` | The coverage window | Payment is due **after** the coverage period rather than in advance | Due-date shift | Inferred (from the label *"Pay in Arrears?"*) |
| **CON-R-035** | `ExpenseSetup.IsDailyRent = true` | `ExpenseSchedule.DailyRentRate`, period day count | Amount = daily rate × days in period, rather than a fixed period amount | Period amount | Derived |
| **CON-R-036** | A partial first or last period | `CodeProrationMethodID`, `ExpenseSchedule.FirstPaymentAmount`, `LastPaymentAmount` | Stub periods carry their own prorated amounts | Stub amounts | Observed |
| **CON-R-037** | `CalculateScheduleAmounts` is invoked | The `ExpenseSetup` + its escalation + tax config | Recomputes the schedule's amounts **in place** | Updated L1 rows | Observed |
| **CON-R-038** | Splitting an expense across orgs | `ExpenseAllocation.OrganizationID`, `.AllocationPercentage`, `.ExpenseSetupID` | Allocates one clause across organizations by percentage | Allocation set | Observed |
| **CON-R-039** | Splitting an expense across vendors | `ExpenseVendorAllocation.VendorID`, `.PaymentPercentage`, `.APVendorNumber`, `.ExpenseSetupID` | Allocates one clause's payments across vendors by percentage; `CHANGE_EXPENSE_ALLOCATION_VENDOR` rewrites it | Vendor allocation set | Observed |

---

## 4. Escalations

`CON-R-040` … `CON-R-049` — see [`escalations.md`](escalations.md).

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-040** | An escalation step falls due | `ExpenseEscalation.EscalationPeriod`, `CodeFrequencyID`, `BeginDate`, `EndDate` | A step occurs every `EscalationPeriod` × frequency units inside the window | Step dates | Derived |
| **CON-R-041** | The driver is fixed | `CodeEscalationTypeID`, `EscalationMethod(Text)`, `FixedAmount`, `BaseAmount` | New amount = f(base or current, `FixedAmount`, `EscalationMethod`). **`EscalationMethod` is free text — its value space is unknown** | New amount | Observed (fields); formula Inferred |
| **CON-R-042** | The driver is index-based | `EscalationIndexID` → `EscalationIndex.IndexAmount`, `IndexBaseFactor` | `rawChange = (IndexAmount / IndexBaseFactor) − 1` | Raw index change | **Inferred** — depends on whether `IndexAmount` is a level or a rate (open) |
| **CON-R-043** | An index change is applied | `ExpenseSetup.CPIMultiplier` | `applied = rawChange × CPIMultiplier` | Applied change | Inferred |
| **CON-R-044** | A per-step collar exists | `PeriodMinPercentage`, `PeriodMaxPercentage` | `collared = clamp(applied, min, max)` | Collared change | Derived |
| **CON-R-045** | `ExpenseSetup.IsCPICompounding` | The flag | `true` ⇒ escalate from the **current** amount; `false` ⇒ from `BaseAmount` | Escalation base | Derived |
| **CON-R-046** | A lifetime collar exists | `LifetimeMinPercentage`, `LifetimeMaxPercentage` | Cumulative change across all steps is clamped | Cumulative bound | Derived |
| **CON-R-047** | An absolute ceiling exists | `CapAmount`, `CapPercentage` | The escalated amount is capped absolutely | Capped amount | Observed (fields); order vs collar unknown |
| **CON-R-048** | An expense stop exists | `StopAmount` | Cost above `StopAmount` transfers rather than escalating | Stop behaviour | Inferred |
| **CON-R-049** | Increase/decrease asymmetry | `ExpenseSetup.AmountIncreaseCap`, `AmountDecreaseCap`, `PercentIncreaseCap`, `PercentDecreaseCap` | Separate caps for upward and downward movement, in addition to `ExpenseEscalation`'s min/max. **Precedence unspecified** | Bounded amount | Observed |

---

## 5. Percentage rent

`CON-R-050` … `CON-R-069` — see [`percentage-rent.md`](percentage-rent.md).

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-050** | A percentage-rent period is projected | `CodeReportingFrequencyID`, `CodeBillingFrequencyID`, `PeriodReportDueDays`, `PeriodPaymentDueDays`, `AnnualReportDueDays`, `AnnualPaymentDueDays` | Two independent buckets: `ReportingBucket{Begin,End,Due}Date` and `BillingBucket{Begin,End,Due}Date` | Two date windows | Observed |
| **CON-R-051** | Sales are reported | `Sales.GrossSalesAmount`, `.UnitSalesCount`, `.SalesPeriod`, `.SalesYear` | `GrossSalesPeriodAmount = Σ GrossSalesAmount` over the sales period; likewise counts | Gross sales | Derived |
| **CON-R-052** | An exclusion applies | `SalesExclusion.CodeSalesTypeID`, `.CodeSalesGroupID`, `.ExclusionRate` | `rawExcluded = salesOfType × ExclusionRate` | Raw exclusion | Derived |
| **CON-R-053** | Exclusions share a cap group | `SalesExclusion.ExclusionGroupCapID` → `SalesExclusionCap` | `PRPGrossExcludedAmount = Σ rawExcluded` in the group | Pre-cap total | Derived |
| **CON-R-054** | A cap group is evaluated | `SalesExclusionCap.CapAmount`, `.CapPercent`, `.PRPGrossSalesAmount` | `PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent)` | Effective cap | Inferred |
| **CON-R-055** | The cap is applied | `PRPGrossExcludedAmount`, `PRPComputedCapAmount` | `PRPNetExcludedAmount = min(gross, cap)`; `PRPExcessExcludedAmount = gross − net` | Allowed / disallowed exclusion | Derived (both fields exist as separate stored values) |
| **CON-R-056** | Net sales are computed | Gross sales, `ExcludedSalesPeriodAmount` | `NetSalesPeriodAmount = GrossSalesPeriodAmount − ExcludedSalesPeriodAmount`; likewise counts | Net sales | Derived |
| **CON-R-057** | Sales periods roll into a rent period | Net sales per sales period, `BillingBucket{Begin,End}Date` | `PRPSalesAmount = Σ NetSalesPeriodAmount` inside the billing bucket | Rent-period sales | Derived |
| **CON-R-058** | Tiering the sales | `PRPBreakpointAmount1..8` (or `BreakpointCount1..8` when `UseCountBasedRate`) | `PRPSalesPastBreakpoint_N` = the portion of `PRPSalesAmount` in tier N. **Marginal-band reading assumed; simple-excess is the alternative** | Per-tier sales | **Inferred — highest-risk rule in the module** |
| **CON-R-059** | Tier rent is computed | `PRPSalesPastBreakpoint_N`, `PRPBreakpointRate_N` | `PRPBreakpointRentDue_N = past_N × rate_N`; `PRPBreakpointRent = Σ` | Tier rent | Derived |
| **CON-R-060** | Cap and floor are applied | `BillingBucketCapAmount`, `BillingBucketFloorAmount`, `CodeCapFrequencyID` | `PRPCapFloorAdjustedRent = clamp(PRPBreakpointRent, floor, cap)` | Clamped rent | Derived |
| **CON-R-061** | Offsets are applied | `VariableRentOffset`, `ScheduledOffset`, `VirtualPRPAggregate.VariableRentOffsetAmount`, `APPLY_OFFSETS` | Offsets reduce the rent-year obligation | `CurrentRentObligation` | Derived |
| **CON-R-062** | Rent already paid is credited | `SalesPeriodRentPaid`, `VirtualPRPAggregate.CurrentRentPaid` | `PRPRentDue = PRPTotalRent − rent already billed − offsets` | Rent due | Inferred |
| **CON-R-063** | Percentage rent is billed | `PRPRentDue`, `PercentageRent.CodeExpenseTypeID`/`CodeExpenseGroupID` | A `PaymentTransaction` carrying `PercentageRentID` is generated | L2 row | Derived |
| **CON-R-064** | `NaturalBreakpointFlag = true` | `NaturalBreakpointRate`, the contract's annual minimum rent | `naturalBreakpoint = annualMinimumRent / NaturalBreakpointRate`. **The numerator source is unconfirmed** | Derived tier-1 threshold | **Inferred** |
| **CON-R-065** | A natural breakpoint is derived | `ConfiguredBreakpointRate1` vs `BreakpointRate1` on `VirtualPercentageRentPeriod` | The configured rate and the effective rate are stored separately as the derivation's audit trail | Audit pair | Observed |
| **CON-R-066** | `UseTrailing12MonthSales = true` | `TrailingSalesMultiplier`, rolling 12-month sales | Replace the bucket sum with a rolling 12-month window, scaled by the multiplier for partial history | Trailing sales | Inferred |
| **CON-R-067** | `AnnualizeRent = true` | Partial-period sales, period length | Scale sales to a full year, tier, then scale the rent back | Annualised rent | Inferred |
| **CON-R-068** | `CumulativeFlag = true` | Year-to-date sales and rent billed | Accumulate YTD and credit rent already billed rather than treating each period independently | Cumulative rent | Inferred |
| **CON-R-069** | `ExtFinalPeriodToLeaseExpDt = true` | `Contract.ExpireDate` | The final percentage-rent period extends to lease expiry rather than truncating at the period boundary | Final period end | Observed (label) |

---

## 6. Alternate rent and offsets

`CON-R-070` … `CON-R-076`.

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-070** | An `AlternateRentSchedule` window is active | `BeginDate`, `EndDate`, `CodeAltRentMathID`, `PercentRentRate` | A substitute rent formula replaces the normal one for the window | Alternate rent | Observed |
| **CON-R-071** | Alternate rent begins | `SetExpHoldFlag`, `SetPRHoldFlag`, `SuspendSL` | Holds the expense schedule, holds percentage rent, suspends straight-line accounting | Three suppressions | Observed (fields); release mechanism unknown |
| **CON-R-072** | A payment is generated under alternate rent | `PaymentTransaction.InAlternateRent`, `.AlternateRentScheduleID`, `.PreAltRentInvoiceAmount` | Records what **would** have been invoiced without the concession | Concession audit trail | Observed |
| **CON-R-073** | Alternate rent reduces expenses | `ExpenseReductionAmount`, `ExpenseReductionPercent` | Reduces the fixed expense side as well as the variable | Reduced expense | Observed |
| **CON-R-074** | `PRDeductExclusions` is set | The flag | Determines whether sales exclusions still apply under alternate rent | Exclusion behaviour | Observed (field); semantics Inferred |
| **CON-R-075** | A `VariableRentOffset` applies | `CodeOffsetGroupID`, `CodeOffsetTypeID`, `CodePRAggregateExpGroupID`, `CodePRAggregateExpTypeID`, `FixedOffsetAmount`, `CapAmount`, `CapPercent` | Reduce percentage rent by amounts paid in a named expense group/type, subject to its own cap | Offset amount | Derived |
| **CON-R-076** | A `ScheduledOffset` is drawn down | `TotalAmount`, `CapAmountPerMonth`, `CapPercent`, `AmountAllocated`, `AmountNotAllocated`, `LinkSchedOffsetExpGrpType`, `APPLY_OFFSETS` | A landlord credit is drawn down over time, capped per month, against named expense group/types | Draw-down | Derived |

---

## 7. Use-based rent

`CON-R-077` … `CON-R-079`.

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-077** | Usage-based rent is computed | `Usage.UsageCount`, `.UsageShare`, `UseBasedRentBreakpoint.BreakpointCount1..8`, `.BreakpointCost1..8` | Structurally identical to `CON-R-050`…`CON-R-063` with `Sales`→`Usage` and `PRP`→`UBRP`. Tier value is a **unit cost**, not a percentage rate | `UBRPRentDue`, `UBRPTotalRent` | Derived (field-for-field mirror confirmed) |
| **CON-R-078** | Unit rates are stored | `sTYPE_NUMBER_FRACTION6DIGITS`, `5-Digit Number` | Usage unit costs carry **6 decimal places**; usage counts 5. **Precision loss here is a direct §4.4 violation** | Precision requirement | Observed |
| **CON-R-079** | A use-rent model is selected | `CodeUseRentModelTypeID` | Selects the usage rent variant. Members unknown | Model variant | Observed |

---

## 8. Expense recovery / CAM

`CON-R-080` … `CON-R-099` — see [`expense-recovery-cam.md`](expense-recovery-cam.md).

### The waterfall (formulas taken verbatim from Lucernex's own field labels)

| ID | Trigger | Inputs | Computation | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-080** | A recovery statement is valued | `{P}ControllableExpenses{G/N}`, `{P}NonControllableExpenses{G/N}`, `{P}Deductions{G/N}` | `ST1 = C + NC − D` | `{P}SubTotal1{G/N}` | **Observed** — label `Sub Total #1 (C+NC-D)` |
| **CON-R-081** | An admin-fee rate exists | `{P}SubTotal1`, `{P}AdminFeePercentage` | `AF%amt = ST1 × AF%` | `{P}AdminFeePercentageAmount{G/N}` | Derived |
| **CON-R-082** | Fees and additions are added | `ST1`, `AF%amt`, `{P}AdministrationFees`, `{P}Additions` | `PT = ST1 + AF%amt + AF + A` | `{P}PassThrough{G/N}` | **Observed** — label `Pass-Through (ST1+AF%+AF+A)` |
| **CON-R-083** | Other recoveries are netted | `PT`, `{P}Recoveries{G/N}` | `ST2 = PT − R` | `{P}SubTotal2{G/N}` | **Observed** — label `Sub Total #2 (PT-R)` |
| **CON-R-084** | The tenant's share is taken | `ST2`, `{P}ProRataShareRate` | `NPT = ST2 × PRR` | `{P}NetPassThrough{G/N}` | **Observed** — label `Net Pass-Through (ST2*PRR)` |
| **CON-R-085** | Escrow is credited | `NPT`, `{P}PrePaidAmount` | `NAD = NPT − PP` | `{P}NetAmountDue{G/N}` | **Observed** — label `Net Amount Due (NPT-PP)` |
| **CON-R-086** | A manual adjustment is made | `NAD`, `{P}AdjustmentAmount` | `RNAD = NAD + Adj` | `{P}RevisedNetAmountDue{G/N}` | **Observed** — label `Revised Amount Due (Net+Adj)` |

`{P}` ∈ {`Reported`, `Approved`, `Budgeted`, `PriorReported`, `PriorApproved`, `PriorBudgeted`};
`{G/N}` ∈ {`Gross`, `Net`}. The same six steps run for every perspective.

### Grid structure and variances

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-087** | A recovery record is stored | — | 565 fields = **63 configuration + 502 grid**, where grid = 9 perspectives × ~19 measures × {Gross, Net} | Grid shape | Derived |
| **CON-R-088** | A within-year variance is computed | `Reported*`, `Approved*` | `RAVariance{M}{G/N} = Reported{M} − Approved{M}` | 36 fields | Derived |
| **CON-R-089** | A within-year variance is computed | `Approved*`, `Budgeted*` | `ABVariance{M}{G/N} = Approved{M} − Budgeted{M}` | 36 fields | Derived |
| **CON-R-090** | A year-over-year variance is computed | `{P}*`, `Prior{P}*` | `{P}PVariance{M}{G/N} = {P}{M} − Prior{P}{M}`, and `{P}PVariancePct` as the percentage form. Applies to R, A and B | 6 × 36 fields | Derived |
| **CON-R-091** | Variance families are enumerated | — | Only the three *year-over-year* families carry `%` siblings at the **header**; at the **line item** all five carry both Amount and Percent | Asymmetry | Observed |
| **CON-R-092** | A measure is unset | Fields suffixed `NoZeroDef` | Return null/blank rather than 0, so a genuine zero is distinguishable from unentered — preventing spurious 100% variances | Nullable semantics | **Inferred** (from the name) |
| **CON-R-093** | A recovery cap applies | `CodeCapTypeID`, `CapPercentage`, `CapAmountChangePercent`, `CapAmountChangeValue`, `IsRecoveryCapEscalationNonCum` | The cap is a **growing** cap: a starting amount escalating per period by a percentage or a value, cumulatively or not | Effective cap | Derived |
| **CON-R-094** | The cap is applied to the waterfall | The cap, the waterfall | **Where in the waterfall the clamp lands is not observable.** Strong prior: controllables only (`C`), which is why C and NC are separate measures | Clamp point | **Inferred — unresolved** |
| **CON-R-095** | A base year applies | `BaseYear(Text)`, `BaseYearAmount`, `CodeBaseYearAmountTypeID` | An expense stop subtracts the base-year level. **Where it enters the waterfall is unobserved** | Base-year adjustment | **Inferred — unresolved** |
| **CON-R-096** | A gross-up applies | `GrossupRate`, `OccupancyAdjustedThreshold` (computed Occupancy Factor) | Variable expenses are grossed up to a notional occupancy | Grossed-up expense | Inferred |
| **CON-R-097** | Escrow is trued up | `CurrentEscrowPayment`, `EscalationPercentage`, `NewEscalationPayment`, `ProposedEscalationPayment`, `CatchUpNumberOfMonths`, `CatchUpPaymentAmount`, `ProposedCatchUpPaymentAmount`, `UPDATE_ESCROW` | Reconcile, propose a new estimate, spread the shortfall over N months | New escrow + catch-up | Derived |
| **CON-R-098** | Recovery exclusions are recorded | `RecoveryExclusions(Textarea)` | **Free text only.** There is no structured exclusion model for expense recovery | Unstructured | Observed |
| **CON-R-099** | A recovery is settled | `ReconciledFlag`, `ReconciledDate`, `TenantDueDate`, `TenantSavingsAmount`, `RECONCILE` | The audit outcome, including what the audit saved the tenant | Settlement | Observed |

### Line-item level

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-100** | A recovery line item is valued | `ReportedAmount{,Gross,Net}`, `ApprovedAmount`, `BudgetedAmount{,Gross,Net}`, `Prior*AmountNoZeroDef` | Same perspectives as the header, at line-item cardinality | Item values | Observed |
| **CON-R-101** | A line item's approved total is computed | `ApprovedAmount`, `ApprovedAdminFeeAmtNoZeroDef`, `ApprovedAdminFeePrcntNoZeroDef`, `ApprovedCapAmountNoZeroDef`, `ApprovedCapPercentNoZeroDef` | `ComputedApprovedTotalAmount{,Gross,Net}` — **admin fee and cap apply per line item**, not only at the header | Item total | Derived |
| **CON-R-102** | A landlord statement is ingested | `ExpenseRecoveryItemMapping.InvoiceLineItemName`, `.DocumentID`, `.JSONConfigText` | Maps a free-text statement line to a structured `ExpenseRecoveryItem` | Item mapping | Inferred |

---

## 9. Payment lifecycle

`CON-R-103` … `CON-R-124` — see [`payment-lifecycle.md`](payment-lifecycle.md).

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-103** | A payment is posted | `PostingDate`, `EffectiveDate`, `DueDate`, `BillingDate`, `CoverageBeginDate`, `CoverageEndDate`, `InvoiceDate`, `CheckDate` | **Five independent date axes** must be representable simultaneously: GL period, economic effect, cash due, service coverage, settlement | Date model | Observed |
| **CON-R-104** | Direction is determined | `IsReceivable` | One ledger serves payables and receivables | Direction | Observed |
| **CON-R-105** | A credit is issued | `CreditFlag`, `AppliedToPayTranID` | A credit transaction points at the transaction it offsets | Credit application | Observed |
| **CON-R-106** | Tax is applied | `TaxAmount1..4`, `TaxesIncludedFlag` | Four parallel tax components; the flag says whether they are inside or additional to `TotalAmount` | Tax treatment | Observed |
| **CON-R-107** | Aging is computed | `AgingAmountForMonth1..3`, `AgingAmountRemainder` | Buckets 0-30 / 31-60 / 61-90 / 90+ from the invoice/effective date | Aging ladder A | Observed (labels); base date Inferred |
| **CON-R-108** | Due-date aging is computed | `DueDateAgingAmountForMonth1..3`, `DueDateAgingAmountRemainder` | The same buckets measured from `DueDate` | Aging ladder B | Observed |
| **CON-R-109** | An expense type is chosen | `CodeExpenseTypeID` → `CodeExpenseType` | Selects **both** the GL account set **and** the accounting treatment (`CodeASC842ScheduleID`, `CodeIFRS16ScheduleID`, `CodeSLScheduleID`) | GL + treatment | Observed |
| **CON-R-110** | A transaction is posted | `CodeExpenseType.APExportBase/Prepaid/Tax1..4Number`, `.ExpAccrualAcct1..4Number`, `.PercentRentAccrualAcct1..4Number`, `.RETaxAccrualAcct1..4Number` | The account numbers are **snapshotted onto the transaction row**, not looked up at export | Frozen GL coding | Derived |
| **CON-R-111** | Eight-segment coding is applied | `AccountNumber1..8` | Present on `PaymentTransaction` and `AccrualTransaction`, **absent** from `CodeExpenseType`; `Organization` carries `Account Number #1–8`. **Whether these are 8 segments of one account or 8 split-coding lines is unresolved** | Account string | **Inferred — unresolved** |
| **CON-R-112** | A batch is exported | `ExportBatchNumber` | Set when the row leaves for AP | Export marker | Observed |
| **CON-R-113** | AP settles a payment | `CheckNumber`, `CheckDate`, `CheckAmount`, `CodeCheckCurrencyTypeID` | Settlement details written back. **Check currency may differ from transaction currency, with no FX rate field on the transaction** | Settlement | Observed |
| **CON-R-114** | A landlord invoice is imported | `IMPORT_INVOICE`, `LandlordInvoice.VendorName/Address/TaxID`, `CustomerName/Address/TaxID` | Extracted values are kept as `Text` alongside the resolved `EmployerID` FK | Invoice + extraction record | Derived |
| **CON-R-115** | An invoice line is matched to a payment | `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`, `.PaymentTransactionID`, `.AllocationAmount`, `.AllocationDate` | Many-to-many allocation | Match | Observed |
| **CON-R-116** | A match has a difference | `LinkLandlordInvPaymentTxn.VarianceAmount`, `.VarianceReason`, `.ReconciliationStatus` | The variance **and its explanation** are stored on the join | Explained variance | Observed |
| **CON-R-117** | A payment is fully matched | `PaymentTransaction.IsInvoiceReconciled` | Set when the three-way match completes | Reconciled flag | Observed |
| **CON-R-118** | Money is received | `PaymentReceipt.ReceivedAmount`, `.AmountAllocated`, `.AmountNotAllocated`, `RECONCILE_RECEIPT` | **There is no FK or link table from `PaymentReceipt` to `PaymentTransaction`** — only allocated/unallocated totals on each side | Receipt allocation | Observed (by absence) — **schema gap** |
| **CON-R-119** | An accrual is posted | `AccrualTransaction.PeriodAmount`, `.PeriodBeginDate`, `.PeriodEndDate`, `.PeriodNumber`, `.PeriodYear`, `.PostingDate`, `GENERATE_ACCRUALS` | Period-scoped accrual with its own GL slots | Accrual posting | Observed |
| **CON-R-120** | An accrual clause is configured | `ExpenseAccrualSetup.CodeAccrualTypeID`, `.CurrentAnnualExpense`, `.CurrentPeriodExpense`, `.BeginPeriodName`, `.EndPeriodName`, `.IsDailyRent`, `.RentableArea` | Accrue an expense ahead of its billing (property tax, insurance) | Accrual clause | Observed |
| **CON-R-121** | An accrual schedule is generated | `ExpenseAccrualSchedule.AccrualRate`, `.DailyAccrualRate`, `.PeriodAmount`, `.AnnualAmount`, `.BeginPeriod/Year`, `.EndPeriod/Year` | Period-by-period accrual amounts, with daily-rate support | L1 accrual rows | Observed |
| **CON-R-122** | Accruals are forecast | `ExpenseAccrualSchedule.ForecastCapPercent`, `.ForecastGrowthPercent`, `.ForecastAdjustment`, `.PlanCapPercent`, `.PlanGrowthPercent`, `.PlanAdjustment` | Planning/forecast growth is **independent of contractual escalation** | Forecast amounts | Observed |
| **CON-R-123** | Percentage-rent accrual is reconciled | `VirtualPRAccrualPeriod.AccrualAmount{ThisPeriod,PriorPeriods,Total}` vs `PostedAccrualAmount{…}`, `IsPosted` | Recomputed accrual is displayed against what was actually posted | Reconciliation pair | Observed |
| **CON-R-124** | Bulk payments are imported | `PaymentTransactionFullImport` (118 fields, no PG table) | A field-for-field staging mirror of `PaymentTransaction` | Import buffer | Observed |

---

## 10. Suppression and gating

`CON-R-125` … `CON-R-130`.

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-125** | Any generation or posting | `HoldFlag` on `ExpenseSetup`, `ExpenseSchedule`, `ExpenseAccrualSetup`, `PaymentTransaction`, `AccrualTransaction` | Negative gate at every layer | Suppression | Observed |
| **CON-R-126** | Any generation | `ReadyForPaymentFlag` on `ExpenseSetup`, `ExpenseSchedule` | Positive gate — must be true | Permission | Observed |
| **CON-R-127** | Forecast inclusion | `ExpenseSetup.IncludeInPlanForecast`, `CodePlanForecastBasedOnID`, `CodePlanForecastGroupID` | Only flagged clauses appear in `VirtualExpenseForecastPeriod` | Forecast scope | Observed |
| **CON-R-128** | Accrual scope | `ContractTerm.IncludeTermForAccruals` | Only flagged option terms are accrued | Accrual scope | Observed |
| **CON-R-129** | Liability scope | `Covenant.HoldAmountInSchedLiability` | Excludes a covenant amount from the ASC 842 scheduled liability | Liability scope | Observed |
| **CON-R-130** | Disclosure scope | `SLSummary.IsIncludeInRollForwardReport` | Controls inclusion in the roll-forward disclosure | Report scope | Observed |

---

## 11. Typing and integrity rules for the rebuild (Constitution §4.4)

`CON-R-131` … `CON-R-137`. These are **requirements on ASG Edge+**, derived from Observed hazards.

| ID | Trigger | Inputs | Condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-131** | Migrating any landed Postgres column | `_crossmap.tsv` | **Every** landed column across 33 tables is `TEXT` (1,163) except 31 `VARCHAR(64)` primary keys. No numeric, date or boolean column exists | Every value must be parsed and validated on ingest | Observed |
| **CON-R-132** | Migrating `PaymentTransaction` | `AmountInvoiced(Text)`, `AmountReceived(Text)` | Two money fields on the central ledger are declared `Text` while their siblings are `Currency` | Parse to `BigDecimal`; reconcile against `InvoiceAmount` and `PaymentReceipt.ReceivedAmount` | Observed |
| **CON-R-133** | Migrating `LandlordInvoiceItem` | `PayTransTotalAmount(Text)`, `LinkAmountAllocated(Text)`, `PayTransEffectiveDate(Text)`, `PayTransIsReceivable(Text)` | Money, date and boolean all stored as text on a reconciliation grid | Replace the seven `PayTrans*` mirror fields with a join | Observed |
| **CON-R-134** | Migrating any parent-child edge | Seven `Text`-typed FKs (`PaymentTransaction.ExpenseRecoveryID`, `.ScheduledOffsetID`, `ExpenseSchedule.Previous/NextExpenseScheduleID`, `ExpenseAccrualSchedule.ExpenseAccrualSetupID`, `AccrualTransaction.ExpenseAccrualSetupID`, `ExpenseRecoveryItem.ExpenseRecoveryID`, `LandlordInvoiceItem.LandlordInvoiceID`, `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`) | Declared `Text` rather than a typed FK, though the target's FK type exists elsewhere | Model as real FKs; define an orphan-handling policy | Observed |
| **CON-R-135** | Any usage-based rent arithmetic | `sTYPE_NUMBER_FRACTION6DIGITS` unit rates × large usage counts | 6-decimal precision is required; binary floating point loses money here | `BigDecimal` with explicit scale and rounding mode | Observed |
| **CON-R-136** | Any percentage arithmetic | `sTYPE_PERCENTAGE` fields (188 catalog-wide) used as multipliers in `CON-R-059`, `CON-R-084`, `CON-R-042` | Rates multiply money in the pro-rata share, breakpoint and CPI paths | Store as `BigDecimal`; fix scale and rounding at each step; never `double` | Observed hazard, Judgement on remedy |
| **CON-R-137** | Any recovery measure is unset | `NoZeroDef`-suffixed fields | A zero default produces spurious 100% variances | Model recovery measures as **nullable** `BigDecimal`, not zero-defaulted | Inferred |

---

## 12. Contract status and lifecycle

`CON-R-138` … `CON-R-144` — see [`contract-hierarchy.md` §7](contract-hierarchy.md#7-contract-status-vs-the-brd-24-lifecycle--the-answer).
Live capture 2026-09-10, [`../../data-model/code-table-registry.md`](../../data-model/code-table-registry.md).

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-138** | A contract's status is set | `CodeContractStatusID` → `Contract Status Code` (2094) | The enum has exactly **three** values: `AI Abstracted`, `Active`, `Inactive`. None is a BRD-24 lifecycle stage | Record state | Observed |
| **CON-R-139** | A status value is deleted | Row actions on `Contract Status Code` | `Active` carries **no delete action** — the platform protects at least one seeded value as system-required | Deletion refused | Observed |
| **CON-R-140** | Recording how a contract was abstracted | `CodeContractStatusID = AI Abstracted` | The tenant encodes **provenance** as a **state** value. A contract can be AI-abstracted *and* active, so the two axes are conflated | Provenance (mis-)recorded as state | Observed value; Derived reading |
| **CON-R-141** | Determining a contract's lifecycle stage | `ActualStartDate`/`OpenYear` (Open), `StatusEffectiveDate` (Active), `PossessionBeginDate`/`PossessionEndDate` (Possession), `PaymentsBeginDate`/`PaymentsEndDate` (Paying Rent), `ExpireDate`/`ActualEndDate`/`IsDead`/`Inactive` (Closed) | Lucernex **derives** stage from dates rather than storing it. No enum holds BRD-24's five stages | Derived stage | Derived |
| **CON-R-142** | A contract advances through its process | `ProcessTimelineTemplate.CodeProjectPhaseID`, `.InProcessPhaseStatus`, `.CompletedPhaseStatus`, `.PreviousProcessTimelineID`; `ProcessTimeline.CodeTaskStatusID`, `.PercentComplete`, Original/Projected/Actual date triples | A **linked list of phase-bound milestone templates**, instantiated per entity, each declaring the status text for its in-progress and completed states. This is the real state machine | `CurrentPhaseStatus`, `CurrentMilestone`, `NextMilestone`, `PreviousMilestone` (all `Text`, derived display) | Observed fields; Derived mechanism |
| **CON-R-143** | Resolving the phase enumeration | `Project Phase Code` | **Not among the 207 Firm Drop Downs**, yet used by 11 objects. A platform-internal enumeration not exposed for tenant editing — the same pattern as `Work Flow Status Code` | Engine-governed, not configurable | Observed (presence in the object export, absence from the registry) |
| **CON-R-144** | The tenant needs a lifecycle status | `Contract.Firm_LeaseStatus` (`sTYPE_CUSTOM_CODE_FIELD`, Firm) + `Firm_LeaseStatusNotes` | ASG added its **own** contract-status field in the same `Contract / Contract Info` sub-group as the platform's. **Do not confuse with `LeaseInfo.CodeLeaseStatusID`** (`Lease Status Code` 2043), which is used by exactly one object and that object has no `ContractID` column | Tenant-authored lifecycle | Observed |

---

## Rule index by document

| Document | Rules |
|---|---|
| [`setup-schedule-transaction-pattern.md`](setup-schedule-transaction-pattern.md) | `CON-R-001`–`CON-R-014` |
| [`contract-hierarchy.md`](contract-hierarchy.md) | `CON-R-015`–`CON-R-029`, `CON-R-138`–`CON-R-144` |
| [`payment-lifecycle.md`](payment-lifecycle.md) | `CON-R-030`–`CON-R-039`, `CON-R-103`–`CON-R-124` |
| [`escalations.md`](escalations.md) | `CON-R-040`–`CON-R-049` |
| [`percentage-rent.md`](percentage-rent.md) | `CON-R-050`–`CON-R-079` |
| [`expense-recovery-cam.md`](expense-recovery-cam.md) | `CON-R-080`–`CON-R-102` |
| Cross-cutting | `CON-R-125`–`CON-R-130` |
| [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md) | `CON-R-131`–`CON-R-137` |
| [`contract-hierarchy.md` §7](contract-hierarchy.md#7-contract-status-vs-the-brd-24-lifecycle--the-answer) | `CON-R-138`–`CON-R-144` |

## The seven rules that must be verified before they become code

Every one of these is `Inferred`, touches money, and changes results materially if wrong.

| Rank | Rule | What to check | Where |
|---:|---|---|---|
| 1 | `CON-R-058` | Marginal band vs simple excess in `PRPSalesPastBreakpoint_N` | Sales Period list, two-tier breakpoint |
| 2 | `CON-R-094` | Where the CAM cap clamps — `C`, `ST1`, or `NAD` | Recovery record with a binding cap |
| 3 | `CON-R-042` | Is `EscalationIndex.IndexAmount` a level or a rate | Two consecutive months of a known index |
| 4 | `CON-R-064` | The numerator in the natural-breakpoint derivation | Compare derived `PRPBreakpointAmount1` against candidates |
| 5 | `CON-R-095` | Where `BaseYearAmount` enters the waterfall | Recovery record with a base-year stop |
| 6 | `CON-R-111` | `AccountNumber1..8` — segments or split lines | One posted transaction vs its organization |
| 7 | `CON-R-118` | How a `PaymentReceipt` is matched to transactions | The Reconcile Receipt screen |

## §13 Rent generation

`CON-R-145` … `CON-R-152` — established 2026-09-11 by opening the **Generate Payments** dialog and
characterising the 11,426 payment transactions the engine had already produced. Full write-up in
[`rent-generation.md`](rent-generation.md); the button itself was never pressed.

| ID | Trigger | Inputs | Condition / computation | Effect | Confidence |
|---|---|---|---|---|---|
| **CON-R-145** | A user invokes `Generate Rent` | `ExpenseSchedule` rows for the contract | Generation reads the **Schedule** layer, not the **Setup** layer | A contract with Expense Setups but an empty Expense Schedule generates nothing | Derived |
| **CON-R-146** | The Generate Payments dialog opens | Period (month + year), Posting Date, Batch Date | A batch number is minted as `RNT<yyyymmdd>-<sequence>` | The run is identified by that batch number | Observed |
| **CON-R-147** | A user selects a generation scope | `Generate Option` | One of `Single Contract`, `Payables — All Contracts`, `Receivables — All Contracts`, `All Contracts` | Three of the four run across every contract in scope; payables and receivables are separately runnable | Observed |
| **CON-R-148** | A transaction is generated | Expense type, period, proration method | Description is `<MNEMONIC> MM/YYYY`, or `<MNEMONIC> - PRS <from>-<to>` when prorated | The row records how it was computed. Mnemonics observed: `BRNT`, `RET`, `CAM - PRS`, `CAM - FIXED`, `INS`, `INS - PRS`, `ELEC`, `UTIL`, `WTR`, `MISC` | Observed |
| **CON-R-149** | A transaction is generated | `invoiceAmount`, `primaryTax`, `APExportTax1..4Number` | `totalAmount` = `invoiceAmount` + tax | Up to four tax components are carried per transaction | Observed |
| **CON-R-150** | A transaction is generated | — | In this tenant every generated row arrives `processedFlag = true` and approval status `Approved` | Whether that is tenant configuration or engine behaviour is **unresolved** | Observed / Inferred |
| **CON-R-151** | A transaction is generated | `exportBatchNumber` | Generation does **not** set it — null on every row sampled | GL export is a separate, later stage from generation | Derived |
| **CON-R-152** | An Expense Setup is generated from | `ExpenseVendorAllocation` rows, each with a `Payment Percentage` and its own begin/end dates | One setup fans out to one transaction per allocation | The vendor split can change mid-term | Observed |

## §14 The CAM recovery waterfall

`CON-R-153` … `CON-R-161` — established 2026-09-11 from the **View Object Model** tool
(`/en/admin/ShowObjectDetails.jsp?sqlTableID=&limitFieldFilter=Math`), which lists every computed
field in the product. Lucernex encodes the formulas directly in its UI labels, so these are
**Observed**, not derived. Full write-up in [`cam-waterfall.md`](cam-waterfall.md).

| ID | Trigger | Inputs | Computation / condition | Output | Confidence |
|---|---|---|---|---|---|
| **CON-R-153** | A recovery period is calculated | Controllable, Non-Controllable, Deductions | `Sub Total #1 = C + NC − D` | `SubTotal1{Gross,Net}` | Observed |
| **CON-R-154** | Sub Total #1 is known | Admin Fee % amount, Admin Fee, Additions | `Pass-Through = ST1 + AF% + AF + A` | `PassThrough{Gross,Net}` | Observed |
| **CON-R-155** | Pass-Through is known | Recoveries | `Sub Total #2 = PT − R` | `SubTotal2{Gross,Net}` | Observed |
| **CON-R-156** | Sub Total #2 is known | Pro Rata Share Rate; Occupancy Factor | `Net Pass-Through = ST2 × PRR` on Budgeted/Reported/Prior, but `ST2 × PRS × Occ` on **Approved** — the gross-up provision | `NetPassThrough{Gross,Net}` | Observed |
| **CON-R-157** | Net Pass-Through is known | Pre-Paid Amount | `Net Amount Due = NPT − PP` | `NetAmountDue{Gross,Net}` | Observed |
| **CON-R-158** | Net Amount Due is known | Adjustments | `Revised Amount Due = Net + Adj` | `RevisedNetAmountDue{Gross,Net}` | Observed |
| **CON-R-159** | Any recovery figure is stored | — | Four bases (Budgeted, Reported, Approved, Prior) × {Gross, Net}, with five pairwise variances (A-B, A-P, B-P, R-A, R-P) materialised as both amount and percentage for every waterfall line | ~379 stored columns | Observed |
| **CON-R-160** | A prior-period measure is absent | `…NoZeroDef` columns | Prior measures are **nullable, never zero-defaulted** — a missing prior period is unknown, not zero, or every first-year reconciliation reports spurious 100% variances | Nullable `BigDecimal` | Observed |
| **CON-R-161** | Classifying any field | View Object Model filters | Of 7,047 fields: 3,437 editable (49%), 1,804 non-math computed (26%), 422 math (6%). **90% of all formula fields live on `ExpenseRecovery`** | Field classification | Observed |
