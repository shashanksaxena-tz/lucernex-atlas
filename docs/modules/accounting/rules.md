# Accounting engine — rules

**Stated up front.** 62 rules, `ACC-R-001` … `ACC-R-062`, in a form a rule engine can consume:
**trigger → inputs → computation/condition → output → confidence**. Confidence is one of
**Observed** (stated in a vendor field definition or directly visible in the schema), **Derived**
(computed or deduced from Observed facts), **Inferred** (domain reasoning; not confirmed). 46 rules
lead with Observed evidence, 6 with Derived and 3 with Inferred; a dozen carry mixed confidence
within a single rule, and those say so inline. Rules marked ⚠ contradict something in the brief, or
something in an obvious first reading of the schema, and should be read before anything is built.

Rules `ACC-R-056` … `ACC-R-062` were added after a live capture of the running tenant at build
`26.08.0.46` on 2026-09-10. That capture also let `ACC-R-001`, `ACC-R-007`, `ACC-R-009` and
`ACC-R-050` be tightened from Inferred/partial to Observed — those four are marked **↑ upgraded**.

Sources, once, for the whole file: vendor field definitions from `_xlsx_lucernex_jcrew.txt`
(sheet `Field Inventory`, column `Definition`) and `_xlsx_feature_list.txt`; field types from
`docs/data-fields/all-fields.csv` and `docs/data-fields/INDEX.md`; object and FK shapes from
`_lucernex_objects_summary.txt`; the admin route from `docs/admin/004-company-administration.md`.

---

## A. Discount rate selection

### ACC-R-001 — Default discount rate resolution ↑ upgraded
- **Trigger**: any calculation that needs a discount rate and finds no contract-level override.
- **Inputs**: **`Program.SLDiscountRate`** (`sTYPE_PERCENTAGE`, the portfolio-level default); `DiscountRate` rows (scoped by `ProgramID`, `CountryID`/`CountryIDList`/`StateProvinceIDList`, `CodeContractUseID`, `CodeAccountingMethodID`, `MinSchedMons`/`MaxSchedMons`, `EffectiveThroughDate`); `Contract.ProgramID`.
- **Computation**: resolve **Portfolio-level rate first; if none exists, Firm-level rate**. Do **not** read the contract-level rate.
- **Output**: `Contract.ComputedSLDiscountRate` (`sTYPE_PERCENTAGE`).
- **Confidence**: **Observed** — *"Lucernex will first use the discount rate at the Portfolio-level, if it exists, otherwise it will use the rate at the Firm-level. This field will not pull the discount rate from the contract-level."* The portfolio-level column is now named: `Program.SLDiscountRate` — *"Enter the default discount rate for your company here. The discount rate is also known as the Interest Rate or Internal Borrower Rate (IBR). To enter a discount rate, enter the number no % or decimal is necessary."* ⚠ Note the entry convention: **no `%` sign and no decimal point** — `5` means 5%, not 0.05. That is a migration parsing rule, not a UI nicety.

### ACC-R-002 — Contract-level discount rate override
- **Trigger**: schedule generation or classification test.
- **Inputs**: `Contract.DiscountRate` (INPUT), `Contract.ComputedSLDiscountRate` (COMPUTED).
- **Condition**: if `Contract.DiscountRate` is populated it is the rate used; otherwise `ComputedSLDiscountRate`.
- **Output**: `SLSummary.DiscountRate`, `ContractFinancialTest.DiscountRate`.
- **Confidence**: **Inferred** — the two fields coexist and `ComputedSLDiscountRate` is explicitly the *default*, but no vendor text states the precedence.

### ACC-R-003 — Asset-level discount rate override
- **Trigger**: schedule generation for an equipment lease.
- **Inputs**: `Asset.DiscountRateOverride` (`sTYPE_PERCENTAGE`).
- **Condition**: if populated, it supersedes ACC-R-001/002 for that asset.
- **Output**: the rate used in the asset's schedule.
- **Confidence**: **Observed** — *"If this equipment uses a different discount rate, enter the discount rate in this field."*

### ACC-R-004 — Discount rate applicability scoping
- **Trigger**: evaluating candidate `DiscountRate` rows.
- **Inputs**: `DiscountRate.CodeAccountingMethodID`, `.CodeContractUseID`, `.CountryID`/`.CountryIDList`/`.StateProvinceIDList`, `.MinSchedMons`, `.MaxSchedMons`, `.EffectiveThroughDate`.
- **Condition**: a blank `CodeAccountingMethodID` matches **both** Finance and Operating. `MinSchedMons`/`MaxSchedMons` bound the schedule length in months for which the rate applies.
- **Output**: the matching rate.
- **Confidence**: **Observed** for the blank-matches-both rule (*"If you leave the field blank, the discount rate will apply to both Finance and Operating."*); **Inferred** for the precedence order when several rows match.

---

## B. ASC 842 classification (`ContractFinancialTest`)

### ACC-R-005 — Test 1: title transfer
- **Trigger**: classification test run.
- **Inputs**: `ContractFinancialTest.DoesTitleRevertToTenant` (`sTYPE_CHECKBOX`).
- **Condition**: `DoesTitleRevertToTenant = true` ⇒ **Fail**; false ⇒ **Pass**.
- **Output**: `Test1Result` (`sTYPE_PASS_FAIL`).
- **Confidence**: **Observed** that this checkbox *is* Test 1; **Derived** for the polarity, from the global rule *"If you 'fail' at least one of the five tests, the lease will be classified as a Finance lease."*

### ACC-R-006 — Test 2: purchase option reasonably certain to be exercised
- **Trigger**: classification test run.
- **Inputs**: `ContractFinancialTest.ContainsBargainPurchaseOption`.
- **Condition**: true ⇒ **Fail**; false ⇒ **Pass**.
- **Output**: `Test2Result`.
- **Confidence**: **Observed** / **Derived** as ACC-R-005.

### ACC-R-007 — Test 3: major part of remaining economic life
- **Trigger**: classification test run.
- **Inputs**: `TestTermLength`, `RemainingLife`, `CodeRemainingLifeFreqUnitID`, `RemainingEconomicLifeThreshold`.
- **Computation**: `ComputedTestTermLengthToRemainingLife = TestTermLength / RemainingLife` (both normalised to `CodeRemainingLifeFreqUnitID`).
- **Condition**: `< RemainingEconomicLifeThreshold` ⇒ **Pass**; otherwise **Fail**. Default threshold *"usually set to 75%"*.
- **Output**: `ComputedTestTermLengthToRemainingLife` (`sTYPE_PERCENTAGE`), `Test3Result`.
- **Threshold source** ↑ upgraded: the default comes from **`Program.RemainingEconomicLifeThreshold`** — *"Enter the fraction of the economic life of the underlying asset that amounts to a major part of the scheduled accounting period. This value is usually set to 75%. **This field is used in the ASC 842 Test.**"* `Contract.RemainingEconomicLifeThreshold` resolves portfolio-level first, then firm-level (ACC-R-004's pattern).
- **Confidence**: **Observed** — *"The value of this field is the Term Length (based on Test) divided by the Remaining Economic Life. The comparison of this percentage to the Remaining Economic Life Threshold determines the pass / fail value displayed for the Test 3 result."*

### ACC-R-008 — Test 3 override: commencement near end of economic life
- **Trigger**: after ACC-R-007.
- **Inputs**: `IsLeaseNearEnd` (`sTYPE_CHECKBOX`).
- **Condition**: `IsLeaseNearEnd = true` ⇒ `Test3Result := Pass`, **unconditionally**.
- **Output**: `Test3Result`.
- **Confidence**: **Observed** — *"If this check box is selected, Test 3's outcome will change to Pass regardless of whether the value the Test Term Length to Remaining Life field is greater than the Remaining Economic Life Threshold field."*

### ACC-R-009 — Test 4: substantially all of fair value
- **Trigger**: classification test run.
- **Inputs**: `FairValueOfAsset`, `PortionOfAssetControlled`, `FairValueThreshold`, an initial liability balance.
- **Computation**:
  ```
  FairValueControlled          = FairValueOfAsset × PortionOfAssetControlled
  ThresholdFairValueControlled = FairValueControlled × FairValueThreshold
  InitLiabilityBalToThreshFairValueCtrld
                               = InitialLiabilityBalance ÷ ThresholdFairValueControlled
  ```
- **Condition**: `InitialLiabilityBalance > ThresholdFairValueControlled` ⇒ **Fail**. Default threshold *"usually set to 90%"*.
- **Output**: `FairValueControlled`, `ThresholdFairValueControlled`, `InitLiabilityBalToThreshFairValueCtrld`, `Test4Result`.
- **Threshold source** ↑ upgraded: the default comes from **`Program.FairValueThreshold`** — *"Enter the fraction of the fair value of the underlying asset that you would like to test against to determine whether to treat this lease as a financing- / purchase-type lease or an operating lease. This value is usually set to 90%. **This field is used in the ASC 842 Test.**"* This is also the first Observed statement that the fair-value test is what decides finance vs. operating.
- **Confidence**: **Observed** for all three formulas and the fail condition. ⚠ **Which** initial liability balance is unresolved — `ASC842InitialLiabilityBalance`, or that plus `InitialLiabilityBalanceAdjust`. The vendor text says *"your Initial Liability Balance (Adjusted)"* in one place and names the plain field in another.

### ACC-R-010 — Test 5: specialised asset
- **Trigger**: classification test run.
- **Inputs**: `IsAssetTooSpecializedForLessor`.
- **Condition**: true ⇒ **Fail**; false ⇒ **Pass**.
- **Output**: `Test5Result`.
- **Confidence**: **Observed** / **Derived** as ACC-R-005.

### ACC-R-011 — ⚠ Final classification (inverted polarity)
- **Trigger**: after ACC-R-005…010.
- **Inputs**: `Test1Result` … `Test5Result`.
- **Condition**: **any** result = Fail ⇒ `Finance`; **all five** = Pass ⇒ `Operating`.
- **Output**: `ContractFinancialTest.FinalResult` (`sTYPE_TEXT`); `CodeAccountingMethodID` set to the matching Accounting Method code.
- **Confidence**: **Observed**, stated on all five test fields. ⚠ Note the polarity is the reverse of the intuitive reading — "passing" the tests means the lease is *operating*.

### ACC-R-012 — Accounting method override
- **Trigger**: after ACC-R-011.
- **Inputs**: `ContractFinancialTest.CodeAcctMethodOverrideID` ("Accounting Type Override"); `Asset.CodeAccountingMethodOverrideID`.
- **Condition**: if populated, the override supersedes the computed `CodeAccountingMethodID`.
- **Output**: the accounting method used by the schedule.
- **Confidence**: **Derived** — the field is labelled "Override" and its definition is *"Select the accounting method you want to use from this field"*, but the precedence is not stated.

### ACC-R-013 — Test locking
- **Trigger**: user sets `IsLocked = true`.
- **Condition**: a locked test cannot be modified and cannot be deleted. Superseding is by creating a new `ContractFinancialTest` row.
- **Output**: immutable test record.
- **Confidence**: **Observed** — *"Locking the test ensures that the test cannot be modified. You cannot delete a classification test once it has been locked, but you can create another test as necessary."*

### ACC-R-014 — Propagation of the authoritative result
- **Trigger**: a `ContractFinancialTest` is locked.
- **Inputs**: all `ContractFinancialTest` rows for the contract with `IsLocked = true`.
- **Computation**: take the **most recently locked** row's `FinalResult`.
- **Output**: `Contract.LatestFinancialTestFinalResult`.
- **Confidence**: **Observed** — *"The final result of the most recently locked ASC 842 test."*

### ACC-R-015 — Auto-computation marker
- **Trigger**: the system runs the test without user entry.
- **Output**: `ContractFinancialTest.AutoComputed := true`.
- **Confidence**: **Observed** — *"This field will have a true value if the ASC 842 test was computed automatically by the system."* The conditions under which the system auto-runs are **not** documented.

### ACC-R-016 — Term-length sourcing
- **Trigger**: classification test run.
- **Inputs**: `Contract.CommenceDate`, `Contract.ExpireDate`, `ContractTerm` rows marked Likely.
- **Computation**:
  - `TermLength = ExpireDate − CommenceDate` (the contractual term);
  - `LikelyTermLength` = length through the last term marked Likely on `Abstract Info > Terms`;
  - `LastLikelyOptionDate` = end date of the last likely term;
  - `TestTermLength` = length of the term selected for the test.
- **Output**: the three term-length fields.
- **Confidence**: **Observed** for each definition; ⚠ **Inferred** that `TestTermLength` defaults to `LikelyTermLength` — the "Test Begin Date"/"Test End Date" fields its definition names do not exist in the schema.

### ACC-R-017 — Accounting date window
- **Trigger**: classification test creation.
- **Inputs**: firm's ASC 842 adoption date; `Contract.PossessionBeginDate`; likely options.
- **Computation**: `Topic842BeginDate = max(adoption date, PossessionBeginDate)`; `Topic842EndDate` = end of accounting including likely options.
- **Output**: `Topic842BeginDate`, `Topic842EndDate`.
- **Confidence**: **Observed** — *"This date is the date your organization is adopting ASC 842, or the Possession Begin Date, whichever is later."*

### ACC-R-018 — Asset-level accounting date override (equipment leases)
- **Trigger**: test or schedule run for an `Asset`.
- **Inputs**: `Asset.AccountingBeginDate`, `Asset.AccountingEndDate`, the asset's expense schedules.
- **Condition**: if the override dates are populated they set the test/schedule window; otherwise the window comes from the expense schedule dates.
- **Confidence**: **Observed** — *"If you do not enter override dates, the test and schedules will run based on the dates of the expense schedules for the asset."*

### ACC-R-019 — Covenant-sourced measurement adjustments
- **Trigger**: classification test or schedule creation.
- **Inputs**: `Covenant.CovenantAmount`, `Covenant.CodeAccountingAdjustmentTypeID`, `Covenant.TotalRVGAmount`, `Covenant.ThirdPartyRVGAmount`.
- **Condition**: the covenant amount is pulled into the accounting assumptions and the accounting schedule **only if** `CodeAccountingAdjustmentTypeID` ∈ {`Purchase Option`, `Cancellation Option`, `Residual Value Guarantee`}.
- **Output**: `ContractFinancialTest.PurchaseOptionAmount` / `.CancellationOptionAmount` / `.ResidualValueGuarantees`, and the same three fields on `SLSummary`.
- **Confidence**: **Observed** — *"This amount will be pulled into your accounting assumptions and accounting schedule if the covenant has one of three accounting adjustment types: Purchase Option, Cancellation Option, or Residual Value guarantee."*

---

## C. Recalculation triggers

### ACC-R-020 — Schedule-type change dirties the schedule
- **Trigger**: `CodeASC842ScheduleID` or `CodeIFRS16ScheduleID` is changed **on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page**.
- **Output**: `SLSummary.NeedsRecalculation := true`.
- **Confidence**: **Observed** — the definition is repeated verbatim on `SLSummary`, `ContractFinancialTest`, `AcctingAssumptionAdjust`, `Covenant` and `CodeExpenseType`: *"This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES."*

### ACC-R-021 — New expense setup dirties the schedule that uses its expense type
- **Trigger**: an `ExpenseSetup` with an `ExpenseSchedule` is created.
- **Inputs**: `ExpenseSetup.CodeExpenseTypeID`; `SLSummary.AssociatedExpenseSetupIDs`.
- **Condition**: the accounting schedule associated with that expense type is dirtied.
- **Output**: `SLSummary.NeedsRecalculation := true`; `AssociatedExpenseSetupIDs` extended.
- **Confidence**: **Observed** — *"If a new expense setup with an expense schedule is created, the accounting schedule associated with the expense type will have its Recalc? flag flipped to Yes."*

### ACC-R-022 — Accounting method change requires remeasurement
- **Trigger**: `SLSummary.CodeAccountingMethodID` is changed.
- **Output**: the schedule must be remeasured.
- **Confidence**: **Observed** — *"If its value is changed, you will need to remeasure your schedule."* ⚠ Note this states the *consequence*, not that `NeedsRecalculation` is set; whether it is, is unconfirmed.

### ACC-R-023 — Recalculation audit trail
- **Trigger**: `NeedsRecalculation` transitions to true.
- **Output**: `RecalcTriggerDate := today`; `NeedsRecalcModifiedByLastMember := current member`; current member appended to `NeedsRecalcModifiedByMemberIDList`.
- **Confidence**: **Observed** — *"The date that the Recalc? flag was triggered"*; *"the last member whose action would have caused the Recalc? flag to change"*; *"all members who have made changes that would cause the Recalc? flag to change."*

### ACC-R-024 — Recalculation override
- **Trigger**: a user declines to recalculate a dirty schedule.
- **Inputs**: free text.
- **Output**: a `RecalcOverrideNotes` row linked by `SLSummaryID`; the id appended to `SLSummary.RecalcOverrideNotesIDList`.
- **Confidence**: **Derived** — the object exists and is described as *"A free-text note explaining why a financial recalculation was manually overridden — an audit-style justification field"* (`docs/data-fields/INDEX.md`), but the workflow that creates it is not documented. Whether creating a note clears `NeedsRecalculation` is unknown.

---

## D. Schedule generation

### ACC-R-025 — Cash-flow routing by expense type
- **Trigger**: schedule generation.
- **Inputs**: `ExpenseSchedule` rows → `ExpenseSetup.CodeExpenseTypeID` → `CodeExpenseType.CodeSLScheduleID` / `.CodeASC842ScheduleID` / `.CodeIFRS16ScheduleID`.
- **Computation**: each period cash flow is routed to the schedule type its **expense type** designates for the standard being generated.
- **Output**: `SLPeriod.PeriodCashAmount` populated on the correct `SLSummary`.
- **Confidence**: **Derived** from the three FK columns on `CodeExpenseType` plus the vendor statement *"Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts."*
- **Live state** ↑ upgraded: in this tenant the routing has exactly one possible destination. `ASC 842 Schedule Type Code` (`TableType` 2162) holds one row, `842 Rent`; `Straight Line Schedule Type Code` (2161) and `IFRS 16 Schedule Type Code` (2163) are both empty. So `CodeExpenseType.CodeSLScheduleID` and `.CodeIFRS16ScheduleID` have no valid target and must be null everywhere, and every cash flow resolves to `842 Rent`. **Observed**, 2026-09-10, `docs/data-model/code-table-registry.md`.

### ACC-R-026 — Secondary schedule allocation
- **Trigger**: an `AcctingAssumptionAdjust` or `Covenant` carries a secondary allocation.
- **Inputs**: `AcctingAssumptionAdjust.SecondaryRentSchedAllocPercent`, `Covenant.SecondaryRentSchedAllocPercent`.
- **Computation**: the stated percentage of the amount is allocated to a secondary schedule; the remainder to the primary.
- **Confidence**: **Observed** that the fields exist and mean an allocation percentage (*"If the expense setup has a secondary schedule allocation percentage, enter the allocation in this field"*); **Inferred** that the remainder goes to the primary.

### ACC-R-027 — Schedule-type flag stamping
- **Trigger**: `GenerateStraightLineRent` / `GenerateFASBSchedule` / `GenerateIFRS16Schedule`.
- **Output**: `SLSummary.IsSLSchedule` / `.IsASC842Schedule` / `.IsIFRS16Schedule := true` respectively.
- **Confidence**: **Derived** — the three buttons and the three flags exist and correspond by name; the vendor defines each flag as *"This flag indicates that the schedule is a … schedule."*
- **Live state**: only `IsASC842Schedule` is reachable today. With the straight-line and IFRS 16 schedule-type tables empty, `GenerateStraightLineRent` and `GenerateIFRS16Schedule` have no schedule type to stamp. Any existing row with `IsSLSchedule` or `IsIFRS16Schedule` true is an orphan whose schedule type was deleted — worth querying as a data-integrity check. **Observed** for the empty tables; **Derived** for the consequence.

### ACC-R-028 — Period row generation
- **Trigger**: schedule generation.
- **Inputs**: `FiscalPeriod` rows for the contract's `ProgramID` covering `SLSummary.BeginDate` … `EndDate`.
- **Computation**: one `SLPeriod` per fiscal period, carrying `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber`.
- **Output**: N `SLPeriod` rows; `SLSummary.SLTermLength` = *"The number of periods in the straight line schedule term."*
- **Confidence**: **Derived** — `FiscalPeriod` is described in `docs/data-fields/INDEX.md` as *"the calendar backbone that SLPeriod, ExpenseSchedule, and Sales fiscal-period fields reference"*, and 12- or 13-period years are documented on `SLPeriod.FiscalPeriod`.

### ACC-R-029 — GL account denormalization
- **Trigger**: `SLPeriod` row creation.
- **Inputs**: the governing schedule type's `ExportAcct1Number` … `ExportAcct20Number`.
- **Output**: copied verbatim onto `SLPeriod.ExportAcct1Number` … `ExportAcct20Number`.
- **Confidence**: **Derived** — the column sets are identical in name and count on the code tables and on `SLPeriod`, and both carry the same vendor definition (*"Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System"*).

### ACC-R-030 — Suppress ROU asset amortization
- **Trigger**: schedule generation.
- **Inputs**: the schedule type's `DontAmortizeAssetValue` (Boolean).
- **Condition**: if true, no asset amortization is recognised for schedules of this type.
- **Output**: `SLPeriod.PeriodAssetAmortizationExpense` suppressed.
- **Confidence**: **Inferred** — the field is the only behavioural switch on the three code tables and its name is unambiguous, but it has **no vendor definition**.
- ⚠ **Inert in this tenant.** The only configured schedule type, `842 Rent`, has `Don't Amortize Asset Value` **unchecked**, and the other two schedule-type tables are empty. The flag therefore has no observable effect on any ASG data, so this rule cannot be validated here and stays permanently Inferred until a vendor answer or a tenant that sets it. **Observed**, 2026-09-10.

---

## E. Measurement

### ACC-R-031 — Initial liability balance
- **Trigger**: schedule generation.
- **Inputs**: `SLPeriod.PVOfPeriodCashAmount` for every period.
- **Computation**: `InitialLiabilityBalance = Σ PVOfPeriodCashAmount`.
- **Output**: `SLSummary.InitialLiabilityBalance`, `SLPeriod.InitialLiabilityBalance`.
- **Confidence**: **Observed** — *"This is the total of all of the Period Payment Present Values over the life of the lease."*

### ACC-R-032 — Present value of a period payment
- **Trigger**: period row generation.
- **Inputs**: `SLPeriod.PeriodCashAmount`, the discount rate (ACC-R-001…003), the period offset.
- **Computation**: discount the cash payment from the period it is made back to the accounting begin date.
- **Output**: `SLPeriod.PVOfPeriodCashAmount`.
- **Confidence**: **Observed** for the intent — *"The Present Value of a future cash payment in today's valuation. This value is discounted to present value from the period that the payment will be made."*; **Inferred** for the compounding convention. `Asset.CodeCompoundingFrequencyID` exists but is undocumented.

### ACC-R-033 — Initial asset balance
- **Trigger**: schedule generation.
- **Inputs**: `InitialLiabilityBalance`, `InitialDirectCostAmount`, `LeaseIncentiveAmount`, `PreCommencePayAmount`, `DismantlingStorageCostAmount`, `InitialAssetBalanceAdjust`.
- **Computation**: **not documented**. The vendor says only *"This is a calculated value which contains the initial value over the asset of the lease."*
- **Output**: `SLSummary.InitialAssetBalance`.
- **Confidence**: **Inferred** — the standard ASC 842-20-30-5 build-up is `liability + prepaid + IDC − incentives`, and all four component fields exist on `SLSummary`, but the actual formula is not stated anywhere offline. ⚠ Do not code this from the schema alone.

### ACC-R-034 — Balance forward and its split
- **Trigger**: schedule creation that carries balances from a prior schedule.
- **Computation**:
  ```
  BalanceForward             = InitialAssetBalance − InitialLiabilityBalance
  BalanceForward             = RemeasurementBalanceForward + ProfitAndLossImpact
  ```
- **Output**: `BalanceForward`, `RemeasurementBalanceForward` (label "Balance Sheet Impact"), `ProfitAndLossImpact`.
- **Confidence**: **Observed** for the first identity (*"The difference between the asset and liability balance at the start of your accounting schedule"*); **Derived** for the split, from *"the portion of the balance forward that does appear on the balance sheet going forward"* and *"the portion of the balance forward that will not persist on the balance sheet and is taken as a capital gain or loss."*

### ACC-R-035 — Total commitment
- **Computation**: `TotalCommitment = Σ` all rent payments for the life of the lease.
- **Output**: `SLSummary.TotalCommitment`.
- **Confidence**: **Observed** — *"The sum of all rent payments for the life of the lease."*

### ACC-R-036 — Remaining cash balance
- **Computation**: `CurrentRemainingCashBalance` = sum of current **and** future remaining lease payments; `CurrentRemainingCashBalanceAfterReportEnd` = the same **excluding the current period**.
- **Confidence**: **Observed** — both definitions are explicit.

---

## F. Period arithmetic (`SLPeriod`)

### ACC-R-037 — Straight-line expense and deferral
- **Trigger**: period row generation.
- **Computation**:
  ```
  PeriodExpenseAmount[n]  = total cash rent straight-lined over the schedule life
  PeriodDeferredAmount[n] = PeriodCashAmount[n] − PeriodExpenseAmount[n]
  CumulativeDeferredBalance[n] = Σ(1..n) PeriodDeferredAmount
  ```
- **Confidence**: **Observed** — *"The cash rent straight lined over the life of the schedule"*; *"The difference between the period cash rent and straight line rent expense"*; *"The sum of the deferred rent from the beginning of the schedule to the current period."* ⚠ The sign of `PeriodDeferredAmount` (cash − expense, or expense − cash) is not stated; the wording implies cash − expense.

### ACC-R-038 — Interest expense
- **Computation**: `PeriodInterestAmount[n]` = interest owed on the liability, at the discount rate.
- **Confidence**: **Observed** for the description (*"The interest owed on the liability based on the discount rate"*); **Inferred** for whether the base is the opening or closing liability balance.

### ACC-R-039 — Accumulated amortization recurrence
- **Computation**:
  ```
  CumulativeAssetAmortExpense[1] = PeriodAssetAmortizationExpense[1]
  CumulativeAssetAmortExpense[n] = PeriodAssetAmortizationExpense[n]
                                 + CumulativeAssetAmortExpense[n−1]
  ```
- **Confidence**: **Observed**, stated verbatim.

### ACC-R-040 — Gross asset balance
- **Computation**: `GrossAssetBalance[n] = AssetAmount[n] + CumulativeAssetAmortExpense[n]`.
- **Confidence**: **Observed** — *"This field's value is equal to the Asset Balance + the Accumulated Amortization Balance."*

### ACC-R-041 — Short-term / long-term split
- **Computation**:
  ```
  Forward12MonthAssetChange[n]     = Σ asset amortization, periods n+1 … n+12
  Forward12MonthLiabilityChange[n] = Σ liability amortization, periods n+1 … n+12
  ShortTermRentExpense[n]          = Σ rent expense, next 12 months
  LongTermRentExpense[n]           = Σ rent expense beyond 12 months
  LongTermLiability[n]             = LiabilityAmount[n] − shortTermLiability[n]
  ```
- **Confidence**: **Observed** for all five. ⚠ Note `SLSummary.Forward12MonthAssetChange` is defined differently from `SLPeriod.Forward12MonthAssetChange`: the summary version is *"the change in the asset balance from period n + 1 to period n + 12"*, the period version is *"the sum of the asset amortization for the next 12 months."* Whether these are the same number expressed two ways is an open question.

### ACC-R-042 — Which short-term liability is reported
- **Trigger**: reporting the short-term liability.
- **Inputs**: firm setting **Short-Term/Long-Term Liability Calculation Method** (`Admin > Manage Company > Financial Settings`).
- **Condition**: `Liability Amortization Based` ⇒ use `Forward12MonthLiabilityAmortBased`; `PV Based` ⇒ use `Forward12MonthLiabilityPVBased`.
- **Confidence**: **Observed** for the switch; the PV-based formula itself is **not available offline**.

### ACC-R-043 — Currency translation
- **Trigger**: FX impact calculated on the Rent Schedule page for a contract with `Contract.IsTranslation = true`.
- **Computation**:
  ```
  AssetTranslationAdjustment     = AssetBalance[n] + AssetAmortizationExpense[n] − AssetBalance[n−1]
  LiabilityTranslationAdjustment = AssetBalance[n] + (Payment[n] − Interest[n]) − AssetBalance[n−1]
  CumulativeTranslationAdjustment = AssetTranslationAdjustment[n] − LiabilityTranslationAdjustment[n]
  LiabilityFXImpact              = (FXrate[n] − FXrate[initial]) × LiabilityBalance[n]
  ```
- **Confidence**: **Observed** — all four formulas are printed verbatim in the vendor definitions. ⚠ The `LiabilityTranslationAdjustment` formula as published references the **asset** balance twice and never the liability balance; it is very likely a documentation error. Do not implement as written.

### ACC-R-044 — Translation vs. revaluation mapping
- **Condition**: `Contract.IsTranslation = true` ⇒ use the Translation mapping on `Admin > Manage Company > Financial Settings`; false ⇒ the Revaluation mapping.
- **Confidence**: **Observed**, stated verbatim.

---

## G. Modification, remeasurement, impairment

### ACC-R-045 — Schedule supersession
- **Trigger**: a replacement `SLSummary` is created for a contract.
- **Output**:
  ```
  new.PriorLastPostedPeriodID := old.SLSummaryID
  new.PostedEndDate           := old.LastPostedEndDate
  new.PostedInitAssetAdj      := new.InitialAssetBalance     − old.AssetBalance(as of PostedEndDate)
  new.PostedInitLiabilityAdj  := new.InitialLiabilityBalance − old.LiabilityBalance(as of PostedEndDate)
  new.PostedAssetAdjustment   := new.AssetBalance      − old.lastPostedAssetBalance
  new.PostedLiabilityAdjustment := new.LiabilityBalance − old.lastPostedLiabilityBalance
  old.Inactive     := true
  old.InactiveDate := today
  ```
- **Confidence**: **Observed** for every one of the six field definitions; **Derived** that they occur together as one transaction.

### ACC-R-046 — Mid-period remeasurement split
- **Trigger**: remeasurement effective mid-period.
- **Output**: `InterestBeforeMidRemeasure` = partial interest from period start to the remeasurement date; `SleBeforeMidRemeasure` = partial single lease expense over the same span.
- **Confidence**: **Observed**.

### ACC-R-047 — Term shortening
- **Trigger**: early termination / term shortening.
- **Computation**:
  ```
  ShortenedSchedInitLiabilityBal = initial liability over the remaining periods of the
                                   original schedule, restated over the shortened term
  ShortenedLeaseLiabilityDiff    = ShortenedSchedInitLiabilityBal
                                   − original.lastPostedPeriod.LiabilityBalance
  ShortenedTermAssetDiff         = −1 × Σ AssetAmortizationExpense over the remaining
                                   periods of the original schedule within the shortened term
  ShortenedTermRentDiff          = new.InitialLiabilityBalance
                                   − ShortenedSchedInitLiabilityBal
  ```
- **Confidence**: **Observed**, all four stated verbatim.

### ACC-R-048 — Impairment
- **Trigger**: an impairment amount is entered.
- **Inputs**: `SLSummary.ImpairmentAmount` / `ContractFinancialTest.ImpairmentsAmount` / `Asset.ImpairmentOverride` — **all three entered as negative numbers**.
- **Computation**: `TotalImpairmentImpact = ImpairmentAmount + PriorAccumulatedAmortizationBalance`, where `PriorAccumulatedAmortizationBalance` is *"the Accumulated Amortization Balance of the accounting period prior to the impairment."*
- **Confidence**: **Observed** for the sign convention and the formula; ⚠ **unresolved** which of the three inputs wins when more than one is populated.

### ACC-R-049 — Final asset amount / residual carve-out
- **Trigger**: schedule generation on a **Finance** contract.
- **Inputs**: `SLSummary.FinalAssetAmount`, `.FinalAssetAllocPercent`, `.FinalAssetDate`, `.SLRemainingAssetBalance`.
- **Condition**: these four fields are *"only made available on Finance contracts"*. `FinalAssetDate` defaults to the schedule end date; a later date amortizes beyond the schedule end.
- **Output**: the asset balance remaining after the schedule end date.
- **Confidence**: **Observed** for the Finance-only restriction and the `FinalAssetDate` default. ⚠ `SLRemainingAssetBalance` is magnitude-typed: 0–100 defaults to Percentage, ≥ 100.01 defaults to Currency, and the user can override — so the stored number does not carry its unit.

---

## H. Approval, posting, and the accrual sub-engine

### ACC-R-050 — Approval is irreversible ↑ upgraded
- **Trigger**: the **ASC 842 Schedule Review/Approval** workflow reaches its third step and the client approver accepts (see `ACC-R-060`).
- **Condition**: `SLSummary.IsApproved := true`, and cannot be reversed through the application.
- **Confidence**: **Observed** — *"Once a schedule has been approved, it cannot be un-approved."* ⚠ Live capture upgrades this rule materially: `IsApproved` is **not** a checkbox a user ticks at will. It is the terminus of a three-step, three-approver workflow. A rebuild that models approval as a Boolean setter has modelled the wrong thing.

### ACC-R-051 — Posting state and the closed cut-line
- **Inputs**: `SLPeriod.RecordStatus` ∈ {posted, not posted, mixed}; `SLPeriod.PostedDate`.
- **Output**: `SLSummary.LastPostedDate` = begin date of the last posted period; `LastPostedEndDate` = its end date; `LastBalancePosted` = *"the asset minus the liability as of the last posted period"*; `LastPostedBalanceSheetImpact` = *"the portion of the last posted balance that is to remain on the balance sheet."*
- **Confidence**: **Observed** for every definition; **Derived** that `LastPostedEndDate` is the closed/open boundary against which ACC-R-045 measures its deltas.

### ACC-R-052 — Accrual amount derivation
- **Trigger**: `ExpenseAccrualSchedule` entry.
- **Inputs**: `AnnualAmount` **or** `PeriodAmount` **or** `AccrualRate`; `ExpenseAccrualSetup.RentableArea`; `DailyAccrualRate` when `ExpenseAccrualSetup.IsDailyRent = true`.
- **Computation**: entering any one of annual amount / period amount / accrual rate auto-populates the other two plus `FirstPaymentAmount` and `LastPaymentAmount`. Rate-based entry requires `RentableArea` to be populated — *"If you are not going to use rentable area, do not enter 0. Leave this field blank."*
- **Output**: `AnnualAmount`, `PeriodAmount`, `AccrualRate`, `FirstPaymentAmount`, `LastPaymentAmount`.
- **Confidence**: **Observed** — *"Enter the annual amount of your accrual in this field. The system will automatically calculate the period amount, the accrual rate, the first period amount, and the last period amount."* and the symmetric statement on `PeriodAmount`. ⚠ The blank-vs-zero distinction on `RentableArea` is a real behavioural difference, not a UI nicety.

### ACC-R-053 — Accrual transaction tax handling
- **Trigger**: `AccrualTransaction` entry.
- **Inputs**: `PeriodAmount`, `TaxAmount1` … `TaxAmount4`, `TaxesIncludedFlag`.
- **Condition**:
  - `TaxesIncludedFlag = false` ⇒ `TotalAmount = PeriodAmount + Σ TaxAmountN`, `TotalAmount` read-only.
  - `TaxesIncludedFlag = true` ⇒ `PeriodAmount` becomes **disabled**, the system subtracts the tax amounts from the period amount, and `TotalAmount` becomes editable.
- **Confidence**: **Observed** — both branches are stated in the definitions of `TaxesIncludedFlag`, `PeriodAmount` and `TotalAmount`.

### ACC-R-054 — Accrual transaction immutability
- **Trigger**: `AccrualTransaction.ProcessedFlag := true`.
- **Condition**: *"Warning - once you mark a transaction as processed, you cannot change it."*
- **Confidence**: **Observed**.

### ACC-R-055 — Alternate-rent hold propagation
- **Trigger**: rent generation while the contract is in an alternate-rent window.
- **Inputs**: `AlternateRentSchedule.SetExpHoldFlag`, `.SetPRHoldFlag`, `.BeginDate`, `.EndDate`.
- **Output**: a hold flag is set on all recurring-expense transactions (resp. percentage-rent transactions) generated during the window.
- **Confidence**: **Observed**. ⚠ These do **not** affect the accounting schedule; they are cash-side controls. `AlternateRentSchedule.SuspendSL` — the one field whose name suggests schedule suspension — is documented as *"no longer used."*

---

## I. Portfolio-level accounting policy (`Program`)

*Added 2026-09-10 from the live tenant. `Program` — the object the UI calls **Portfolio** — is the
accounting engine's policy carrier, and round one of this document missed it. It holds the discount
rate, both ASC 842 thresholds, three amortisation-basis switches, two proration switches, the fiscal
year end, and fourteen FX rate-type selectors. Everything here is **Observed** from vendor field
definitions in `_xlsx_lucernex_jcrew.txt`.*

### ACC-R-056 — Amortisation basis: Per Day or Per Period
- **Trigger**: schedule generation.
- **Inputs**: `Program.SLAssetAmortizeMethod`, `Program.SLCashAmortizeMethod`, `Program.SLExpenseAmortizeMethod` — three **independent** `sTYPE_TEXT` switches, one per schedule column.
- **Condition**:
  - `PER_PERIOD` ⇒ *"distributes the amortization equally among periods"*;
  - `PER_DAY` ⇒ *"distributes the amortization according to the number of days in the period"*, i.e. weight each period by `SLPeriod.NumberDays`.
- **Output**: `SLPeriod.PeriodAssetAmortizationExpense` (asset switch), `SLPeriod.PeriodCashAmount` (cash switch), `SLPeriod.PeriodExpenseAmount` (expense switch).
- **Scope restriction**: ⚠ *"This setting impacts **only ASC 842 Finance leases**."* — stated on the asset switch. The cash and expense switches carry no such restriction.
- **Confidence**: **Observed**. The GraphQL enum `GaapAmortizeMode { PER_DAY, PER_PERIOD }` is the API-level name for the value these three columns hold; the columns themselves are typed `Text` in the schema dump, so the enum is the authoritative value list. *(Sources: `_xlsx_lucernex_jcrew.txt`; `docs/data-model/graphql-api.md`.)*
- **Rebuild note**: three separate switches, not one. A single "amortisation basis" setting in ASG Edge+ would be a behaviour change, and on a 13-period fiscal calendar the Per-Day/Per-Period difference is material in every period.

### ACC-R-057 — 28-day proration of partial first and last periods
- **Trigger**: schedule generation where the first or last period is partial.
- **Inputs**: `Program.SLProrate35As28` (`Boolean`); the partial period's day count.
- **Condition**: when true, prorate the partial period on a **28-day multiplier**; and *"If you have a partial period that is greater than or equal to 28 days, it will be considered a whole period by the system and will not prorate."*
- **Scope restriction**: *"This setting only impacts values calculated **per period**"* — i.e. it interacts with `ACC-R-056`: it is inert on columns set to `PER_DAY`.
- **Confidence**: **Observed**.

### ACC-R-058 — Fiscal / calendar year-end matching
- **Trigger**: schedule generation and the fiscal-year rollups.
- **Inputs**: `Program.SLMatchYearEnds` (`Boolean`), `Program.FiscalYearEnd` (`Date` — month and day).
- **Condition**: *"This field determines if the program allows for matching of fiscal/calendar year rent."*
- **Confidence**: **Observed** that the switch exists and what it is named; ⚠ **Inferred** as to what "matching" does. It is the only setting that could reconcile `SLSummary`'s two parallel rollup families (`Contract`'s `*FiscalYear*` block against its `*CalendarYear*` block). Confirm before building.

### ACC-R-059 — Per-column FX rate-type selection
- **Trigger**: currency conversion of a schedule column.
- **Inputs**: fourteen `Program` code fields — seven schedule columns × two modes:

  | Schedule column | Revaluation rate type | Translation rate type |
  |---|---|---|
  | Asset amortisation | `CodeAssetAmortFXTypeID` | `CodeAssetAmortSubFXTypeID` |
  | Asset balance | `CodeAssetBalFXTypeID` | `CodeAssetBalSubFXTypeID` |
  | Liability amortisation | `CodeLiabAmortFXTypeID` | `CodeLiabAmortSubFXTypeID` |
  | Liability balance | `CodeLiabilityBalFXTypeID` | `CodeLiabilityBalSubFXTypeID` |
  | Cash expenses | `CodeCashExpensesFXTypeID` | `CodeCashExpensesSubFXTypeID` |
  | Interest | `CodeInterestFXTypeID` | `CodeInterestSubFXTypeID` |
  | Single lease expense | `CodeSingleLeaseFXTypeID` | `CodeSingleLeaseSubFXTypeID` |

- **Condition**: the `Sub` variant applies to *"contracts in need of **translation**"*, the plain variant to *"contracts in need of **revaluation**"* — selected per contract by `Contract.IsTranslation` (`ACC-R-044`).
- **Output**: the exchange rate applied to each `SLPeriod` `*Translated` column.
- **Confidence**: **Observed**, all fourteen definitions.
- **Rebuild note**: this partly answers the `ACC-R-044` open question. The Translation-vs-Revaluation *mapping* referenced by `Contract.IsTranslation` is **portfolio-scoped and column-by-column**, not a single firm-wide toggle. The `Exchange Rate Type Code` values themselves are still unknown.

---

## J. The ASC 842 approval workflow

*Added 2026-09-10 from the live tenant. The full capture is in
`docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md`.*

### ACC-R-060 — ⚠ Schedules are not auto-published
- **Trigger**: an ASC 842 schedule is generated and submitted for review.
- **Process**: the tenant runs a live workflow named **"ASC 842 Schedule Review/Approval"**, three ordered steps, every step `Type = Form`, every step `Approval Level = Member`:

  | # | Step | Bound form layout |
  |---:|---|---|
  | — | (submission) | `ASR Submit ASC 842 Schedules` |
  | 1 | Initial Review of ASC 842 Schedules | `ASR Initial Review of ASC 842 Schedule` |
  | 2 | Approve ASC 842 Schedules (ASG) | `ASR Approve ASC 842 Schedules (ASG)` |
  | 3 | Approve ASC 842 Schedules (Client) | `ASR Approve ASC 842 Schedules (Client)` |

- **Output**: on completion of step 3, `SLSummary.IsApproved := true` (`ACC-R-050`).
- **Confidence**: **Observed** for the workflow, its three steps, their order, their approval levels and their bound layouts (`Manage Work Flows`, `/en/workflow/WorkFlowTemplateEdit.jsp`, tenant build `26.08.0.46`, 2026-09-10). **Derived** for the link to `SLSummary.IsApproved` — the workflow and the flag are the only two approval mechanisms in the product and it would be strange for them to be unrelated, but the binding column was not observed.
- **Rebuild note**: ⚠ **This is the single most consequential live finding for this module.** The accounting engine's output is not published by the calculation. It is generated, reviewed once, approved by ASG, then approved by the client — a two-party sign-off with an internal review ahead of it. A schedule therefore has a *state*, not a Boolean: `draft → submitted → under review → ASG-approved → client-approved`. Nothing in the offline schema shows this; `SLSummary` has only `IsApproved`, so the intermediate states live in the workflow instance, not on the schedule.

### ACC-R-061 — What an ASC 842 review request may be raised against
- **Trigger**: creating an `ASC 842 Schedule Review/Approval` request.
- **Condition**: the form type declares attachability as a Boolean per entity kind. For this form type, only **`Portfolio` = Yes** and **`RE Contract` = Yes**; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` and **`Equipment Contract`** are all `No`.
- **Confidence**: **Observed**.
- **Rebuild note**: ⚠ **`Equipment Contract` is `No`.** Equipment leases generate ASC 842 schedules (`Asset` carries the full classification field set, and `Contract.GenerateFASBSchedule` exists on equipment contracts) but cannot be routed through this review workflow. Either equipment schedules bypass the approval gate entirely, or they are reviewed at the portfolio level. This is a real process gap and is now the top open question below.

### ACC-R-062 — Approver resolution
- **Trigger**: a workflow step activates.
- **Inputs**: the step's `Approval Level` ∈ {`Member`, `Job Title`, `Ad Hoc`}.
- **Condition**: all three ASC 842 steps use `Member` — a named approver, resolved at configuration time rather than by org-chart position.
- **Confidence**: **Observed**.
- **Cross-reference**: the GraphQL `AssigneeType` enum (`ALL`, `PARENT`, `REGION1`, `REGION2`, `MARKET`, `JOB_TITLE`) shows the platform supports position-based routing generally; the ASC 842 workflow does not use it. *(Source: `docs/data-model/graphql-api.md`.)*

---

## Rules that intentionally do **not** exist

Stating these explicitly, because their absence is itself a finding.

| Expected rule | Status |
|---|---|
| An IFRS 16 classification test | **Does not exist.** IFRS 16 has no lessee classification; Lucernex models none. |
| A short-term / low-value practical-expedient gate that skips schedule generation | **Does not exist as a rule.** `IsShortTerm` and `IsLowAssetValue` are stored on both `Contract` and `Asset` but nothing documents them driving any behaviour. |
| A straight-line suspension rule | **Does not exist.** `SuspendSL` is dead (ACC-R-055). |
| A rule preventing two active schedules of the same standard on one contract | **Does not exist in the schema.** Three independent Booleans, no uniqueness constraint. |
| An enforced link between an ASC 842 schedule and its IFRS 16 sibling | **Does not exist.** |

---

## Open questions

Ranked by how badly they block the rule engine. Items added or resolved by the 2026-09-10 live
capture are marked **(new)** / **(resolved)**.

0a. **(resolved 2026-09-10)** *What are the schedule-type code table values?* — `ASC 842 Schedule
   Type Code` (2162) has **one** row, `842 Rent`, with `Don't Amortize Asset Value` unchecked;
   `Straight Line Schedule Type Code` (2161) and `IFRS 16 Schedule Type Code` (2163) are **empty**.
   Consequences fold into `ACC-R-025`, `ACC-R-027` and `ACC-R-030` above.
0b. **(resolved)** *Where does `GaapAmortizeMode` bind?* — `Program.SLAssetAmortizeMethod`,
   `.SLCashAmortizeMethod`, `.SLExpenseAmortizeMethod`. See `ACC-R-056`. What remains open is the
   **stored representation**: the three columns are `Text` in Postgres while the API enum is
   `PER_DAY` / `PER_PERIOD`. Confirm whether the column stores the enum name, a display string
   (*"Per Day"*), or a code.
1. **(new) ⚠ How are equipment-lease ASC 842 schedules approved?** The review workflow's form type
   has `Equipment Contract = No` (`ACC-R-061`), yet equipment leases produce schedules. Either they
   skip the gate or they are approved at portfolio level. Blocks the approval-state design.
2. **ACC-R-033 — what is the initial-asset-balance formula?** The single most important undocumented
   computation in the module. Every component field exists; the arithmetic does not. Open a schedule
   in the UI with known IDC/incentive/prepaid values and back it out.
3. **ACC-R-009 — adjusted or unadjusted initial liability in Test 4?** Open an ASC 842 Test with a
   non-zero `InitialLiabilityBalanceAdjust`.
4. **What are the `Schedule Creation Reason Code` values?** Determines whether ACC-R-045 fires on
   every recalculation or only on modifications.
5. **ACC-R-024 — does creating a `RecalcOverrideNotes` clear `NeedsRecalculation`?**
6. **ACC-R-038 — is period interest computed on the opening or closing liability balance?** A
   one-period difference that compounds across the whole schedule.
7. **ACC-R-032 — what compounding convention discounts a period payment?** `Asset.CodeCompoundingFrequencyID` exists and is undocumented; is there a contract-level equivalent?
8. **ACC-R-043 — is the published `LiabilityTranslationAdjustment` formula wrong?**
9. **ACC-R-042 — what is the PV-based short-term-liability formula?** Read
   `Admin > Manage Company > Financial Settings`.
10. **ACC-R-030 — what does `DontAmortizeAssetValue` actually suppress?** No vendor definition.
11. **ACC-R-048 — which of the three impairment inputs wins?**
12. **ACC-R-012 — does `CodeAcctMethodOverrideID` beat the computed `FinalResult`, and does
    `Asset.CodeAccountingMethodOverrideID` beat both?**
13. **ACC-R-041 — are `SLSummary.Forward12Month*` and `SLPeriod.Forward12Month*` the same quantity?**
    The two definitions differ ("change in balance" vs "sum of amortization").
14. **ACC-R-026 — where does the non-secondary remainder of an allocation go?**
15. **ACC-R-037 — sign convention on `PeriodDeferredAmount`.**
16. **Do `IsShortTerm` / `IsLowAssetValue` gate anything at all?** If they do not, ASG Edge+ must build
    the practical-expedient logic from scratch.
17. **(new) ACC-R-058 — what does `Program.SLMatchYearEnds` actually match?** The only candidate is
    reconciling `Contract`'s parallel `*FiscalYear*` and `*CalendarYear*` rollup blocks.
18. **(new) ACC-R-059 — what are the `Exchange Rate Type Code` values?** Fourteen `Program` columns
    select from it and none of the values is available offline.
19. **(new) ACC-R-060 — what does an `ASR` form layout collect at each step?** Four layouts exist
    (`Submit`, `Initial Review`, `Approve (ASG)`, `Approve (Client)`). Their field sets define the
    approval record ASG Edge+ must reproduce, and none has been opened.
20. **(new) ACC-R-060 — what happens on rejection at step 2 or 3?** Does the schedule return to
    draft, stay generated-but-unapproved, or get deleted? No rollback path is documented.
21. **(new) ⚠ Are there `SLSummary` rows whose schedule type no longer exists?** With 2161 and 2163
    empty, any row with `IsSLSchedule` or `IsIFRS16Schedule` true is orphaned but still carrying
    balances. One query; real migration consequences.
22. **(new) What are the twenty `ExportAcctNNumber` values on `842 Rent`?** Now a single row to read
    at `FirmCodeEdit.jsp?TableType=2162`, not a matrix. This is the cheapest remaining high-value
    capture in the module.
23. **(new) What are the `Schedule Creation Reason Code` (2160) values?** Confirmed to be one of the
    207 Firm Drop Downs, so it is directly readable at `FirmCodeEdit.jsp?TableType=2160`. This is the
    same question as #4 above, now with an exact route.
24. **(new) Are Accounting Method, Accounting Adjustment Type, Accrual Type, Proration Method,
    Frequency and Frequency Unit platform-internal enums rather than Masters rows?** None of the six
    is among the 207 Firm Drop Downs. If they are fixed by accounting semantics rather than
    configurable, ASG Edge+ should model them as hard-coded enums, which is a different build
    decision from the tenant-editable schedule types.

**Negative check, recorded deliberately:** `Work Flow Status Code` is **not** among the 207 Firm Drop
Downs. No rule in this file depended on it — `ACC-R-060`…`ACC-R-062` take their `Member` / `Job
Title` / `Ad Hoc` vocabulary from the workflow-step screen, and `SLSummary`'s only status-like code
reference is `CodeScheduleCreationReasonID` (2160), which *is* in the registry. Nothing here needs
revisiting.
