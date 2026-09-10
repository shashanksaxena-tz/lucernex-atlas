# Every accounting field, classified INPUT / COMPUTED / CODE-TABLE

**Stated up front.** 666 fields across 17 objects, each classified with its evidence. The headline
ratio: **230 COMPUTED, 251 INPUT, 46 CODE-TABLE, 4 ACTION, 15 DEAD**, plus 84 SYSTEM (audit columns)
and 36 FK. The two objects that matter most are lopsided in opposite directions —
`SLSummary` is **96 COMPUTED to 19 INPUT** (it is an output record with a small assumption header),
while `ContractFinancialTest` is **36 COMPUTED to 38 INPUT** (it is a genuine data-entry form that
computes six derived figures and five verdicts).

## Vendor corroboration: `COMPUTED` is a first-class type in Lucernex's own API

*Added 2026-09-10. **Observed** in the live GraphQL schema at `/servlet/graphql`, tenant build
`26.08.0.46`; full capture in [`../../data-model/graphql-api.md`](../../data-model/graphql-api.md).*

The 448 `sTYPE_*` / `sCODE_*` codes in Manage Data Fields are presentation-layer codes sitting on a
**10-value canonical type system** that the vendor's own GraphQL API exposes as the enum `FieldType`:

```
BOOLEAN  COMPUTED  DATE  DATETIME  FK  FLOAT  INTEGER  MONEY  PERCENTAGE  STRING
```

**`COMPUTED` is one of the ten.** The INPUT/COMPUTED split this file draws is therefore not an
interpretation imposed from outside — it is a distinction Accruent makes in its own type system and
publishes in its API contract. The `sTYPE_MONEY_MATH_OPERATION` / `sTYPE_PERCENT_MATH_OPERATION` /
`sTYPE_DATE_MATH_OPERATION` families are the presentation-layer projection of that single canonical
`COMPUTED` type.

This materially raises the confidence of the whole file:

| Before | After |
|---|---|
| Signals 1–3 rested on the `docs/data-fields/INDEX.md` legend's prose gloss (*"System-calculated … computed, not directly entered"*) | The same distinction is a declared enum value in the vendor's compiled API contract |
| The INPUT/COMPUTED axis was our organising choice | It is the platform's own axis; we are recovering it, not inventing it |
| `FK` as a class was inferred from the `Key Role` column | `FK` is likewise one of the ten canonical types |

Two further corroborations from the same enum:

- **`MONEY` and `PERCENTAGE` are distinct from `FLOAT`.** Lucernex does not treat money as a float at
  the type level, and the GraphQL scalar list includes **`BigDecimal`**. See
  [`asg-edgeplus-mapping.md`](asg-edgeplus-mapping.md#4-every-non-key-source-column-is-text) — the
  all-`TEXT` Postgres columns are a persistence-layer artefact, not the intended design.
- The canonical set has no equivalent of `sTYPE_PERCENT_OR_AMOUNT`. The magnitude-typed
  Percent-or-Currency field (hazard 2 below) does not map cleanly onto any of the ten, which is
  further reason to treat it as an anomaly rather than a pattern to reproduce.

**Open question raised by this**: does the GraphQL schema expose `FieldType` **per field**? If it
does, the entire 666-row classification below can be verified against the vendor's own answer in one
introspection query, rather than inferred from help text. That would be the single highest-value
follow-up for this file.

## How each class was assigned

The classification is not a judgement call for most rows. Four independent signals were used, in
priority order:

Every signal below is a projection of the canonical `FieldType` enum described above.

| Priority | Signal | Source | Meaning |
|---:|---|---|---|
| 1 | Field type is `sTYPE_MONEY_MATH_OPERATION`, `sTYPE_PERCENT_MATH_OPERATION`, `sTYPE_DATE_MATH_OPERATION`, `sTYPE_MATH_OPERATION`, `sTYPE_TOTAL_MATH_OPERATION` | `docs/data-fields/all-fields.csv`; legend at `docs/data-fields/INDEX.md` lines 36, 42, 54, 80, 472 | **COMPUTED** — the legend defines these as *"System-calculated … (computed, not directly entered)"* |
| 2 | Field type is `sTYPE_PASS_FAIL` | same | **COMPUTED** — a test verdict |
| 3 | Field type is `sTYPE_SUBMITBUTTON` | legend line 44: *"Form action button that triggers a server-side process — not a stored data value"* | **ACTION** |
| 4 | Field type is `sCODE_*`, or Lucernex type is `Dropdown (…)` | `all-fields.csv` / `_lucernex_objects_summary.txt` | **CODE-TABLE** |
| 5 | Vendor definition opens with *"Enter…"*, *"Select…"*, *"Write…"*, *"Add…"*, *"If you…"*, *"This check box…"* | `_xlsx_lucernex_jcrew.txt`, `Definition` column | **INPUT** |
| 6 | Vendor definition contains *"calculated by the system"*, *"This field displays"*, *"This field pulls"*, *"auto-populate"*, *"The sum of"*, *"The difference between"*, *"is equal to"*, *"This flag indicates"*, … | same | **COMPUTED** |
| 7 | Vendor definition says *"no longer used"*, *"not currently being used"*, *"not implemented"*, *"legacy field"*, *"informational-only"*, *"record keeping purposes only"*, *"placeholder in preparation"* | same | **DEAD** |
| 8 | `Key Role = Foreign key (ID reference)` | `_xlsx_lucernex_jcrew.txt` | **FK** |
| 9 | `CreatedByID`, `CreatedDate`, `ModifiedByID`, `ModifiedDate`, `RevNumber`, `BOMapClientRecordID`, `ProjectEntityID`, `<Object>ID` | naming convention, confirmed by vendor definitions | **SYSTEM** |

A small number of rows were reclassified by hand where the automatic signals conflicted; those are
listed explicitly below so the judgement is auditable.

### The `Functional Field` column

`_xlsx_lucernex_jcrew.txt` carries a vendor-supplied `Functional Field` Yes/No flag. It is reproduced
in the `Fn` column of every table. **`Fn = No` does not mean "computed"** — it means the field has no
functional effect on the engine. It marks descriptions, page/section references, reporting-only
lookups, and genuinely dead fields. All 36 `Fn = No` rows in the four core objects are:

| Object | Count | What they are |
|---|---:|---|
| `ContractFinancialTest` | 17 | 8 paired `*Desc` description fields, `PageNumber`/`ParagraphNumber`/`LineNumber`/`SectionNumber` document references, `BaseName`, `Notes`, `YearBuilt`, `FairValueSource`, `CodeAssetTypeTestID` (dead), `AssetAssociatedProjectEntityID` (reporting) |
| `SLSummary` | 9 | `Notes`, `DateRange` (dead), `CodeSLScheduleID`, `CodeScheduleCreationReasonID`, the four `CurrentFiscalYearQ*CashExpense` quarterly fields, `AssetAssociatedProjectEntityID` |
| `AlternateRentSchedule` | 6 | `SuspendSL` (dead), `CodeAltRentMathID` (dead), `SetExpHoldFlag`, `SetPRHoldFlag`, `Description`, `Notes` |
| `SLPeriod` | 2 | `SLPeriodAllocations`, `AssetAssociatedProjectEntityID` |
| `AcctingAssumptionAdjust` | 2 | `AdjustmentPercent` (dead), `Notes` |

Two of these are worth pausing on: `SLSummary.CodeScheduleCreationReasonID` is marked non-functional
even though it is the only record of *why* a schedule exists, and the four quarterly cash-expense
fields are non-functional because they are conditionally populated report fields.

## Manual reclassifications

Every row where the automatic signal was overridden, with the reason.

| Object.Field | Auto | Assigned | Reason |
|---|---|---|---|
| `SLSummary.IsASC842Schedule`, `.IsIFRS16Schedule`, `.IsSLSchedule` | INPUT | **COMPUTED** | Vendor: *"This flag **indicates** that the schedule is a … schedule"* — set at generation by whichever button ran |
| `SLSummary.Inactive` | INPUT | **COMPUTED** | Vendor: *"This flag **is applied to** a schedule if another lease accounting schedule replaces it"* |
| `SLSummary.NeedsRecalculation` | INPUT | **COMPUTED** | Set by the trigger rules in [`rules.md`](rules.md) `ACC-R-020`…`ACC-R-023`, not typed by a user |
| `SLSummary.IsApproved` | — | **INPUT** | A deliberate, irreversible user action |
| `SLSummary.PurchaseOptionAmount`, `.ResidualValueGuarantees` | INPUT | **COMPUTED** | Vendor: *"This field pulls the value … from the Covenant table"* |
| `SLSummary.InitialAssetBalanceAdjust`, `.InitialLiabilityBalanceAdjust` | INPUT | **COMPUTED** | Vendor: *"This field pulls the value … from the ContractFinancialTest table"* |
| `SLSummary.CancellationOptionAmount`, `.CalcPVOfFinancialTerms`, `.CalcPVOfFinancialTermsNoAdjust`, `.ShortenedTermRentDiff` | INPUT? | **COMPUTED** | Definitions are declarative statements of a derived value |
| `SLSummary.DiscountRate`, `.DismantlingStorageCostAmount`, `.InitialDirectCostAmount`, `.LeaseIncentiveAmount`, `.PreCommencePayAmount`, `.FinalAssetAmount`, `.FinalAssetAllocPercent`, `.FinalAssetDate`, `.SLRemainingAssetBalance` | INPUT? | **INPUT** | Vendor: *"This field appears in the Create New Schedule window. Enter …"* |
| `SLSummary` roll-forward block (25 fields) | COMPUTED? | **COMPUTED** | No vendor definition, but all are `sTYPE_MONEY` in the `Contract / Roll Forward Report` subgroup — aggregates over `SLPeriod`. **Derived, not Observed.** |
| `SLPeriod.BeginDate`, `.EndDate`, `.FiscalPeriod`, `.FiscalPeriodYear` | INPUT | **COMPUTED** | Generated from the `FiscalPeriod` calendar when the schedule is built, not typed |
| `SLPeriod.ExportAcct1..20Number`, `.SLExportAcct1..3Number` | INPUT | **COMPUTED** | Denormalized copies of the schedule type's `ExportAcctNNumber` values, written at generation |
| `SLPeriod.PostedDate`, `.RecordStatus`, `.ConversionRate*`, `.FXGainLoss`, `.ScheduleCumulativeAmortExpense` | mixed | **COMPUTED** | Set by posting and FX processes |
| `Contract.Test1Result`…`Test5bResult`, `.FinalResult`, `.LatestFinancialTestFinalResult`, `.CurrentStraightLine*`, `.ComputedSLDiscountRate`, `.FairValueThreshold`, `.RemainingEconomicLifeThreshold`, `.InAlternateRent`, `.TermLength` | INPUT? | **COMPUTED** | Definitions are all declarative (*"This field computes…"*, *"The final result of…"*, *"The … balance value from the first active period"*, *"returns true if…"*) |
| `ContractFinancialTest.AutoComputed` | INPUT | **COMPUTED** | Vendor: *"This field will have a true value if the ASC 842 test was computed automatically by the system"* |
| `ContractFinancialTest.CommenceDate`, `.ExpireDate`, `.LastLikelyOptionDate`, `.CancellationOptionAmount`, `.PurchaseOptionAmount`, `.ResidualValueGuarantees` | INPUT | **COMPUTED** | All *"This field pulls…"* |
| `AcctingAssumptionAdjust.AnnualAmount`, `.FirstPaymentAmount`, `.LastPaymentAmount` | INPUT | **COMPUTED** | Vendor: *"will auto-populate depending upon the value you enter in the Payment Amount field and the frequency you select"* |
| `AccrualTransaction.AccountNumber1..8`, `.APExport*`, `.ExpAccrualAcct*`, `.PercentRentAccrualAcct*`, `.RETaxAccrualAcct*` (23 fields) | INPUT? | **COMPUTED** | Vendor: *"You can edit these account numbers at the organization-level"* / *"configured at the expense type level"* — denormalized copies |
| `FiscalPeriod.NumberDaysInPeriod`, `.NumberWeeksInPeriod` | INPUT? | **COMPUTED** | Vendor: *"Calculates how many days/weeks are in the period"* |

## The 15 DEAD fields

Do not rebuild any of these. All are **Observed** from explicit vendor statements.

| Object.Field | Vendor statement |
|---|---|
| `AlternateRentSchedule.SuspendSL` | *"This field is no longer used."* |
| `AlternateRentSchedule.CodeAltRentMathID` | *"This field is for record keeping purposes only. It has no functional impact on the generated payment."* |
| `SLSummary.DateRange` | *"This field is not currently being used in Lucernex."* |
| `ContractFinancialTest.CodeAssetTypeTestID` | *"This field is no longer in use."* |
| `ContractFinancialTest.SectionNumber` | *"This field is no longer in use."* |
| `AcctingAssumptionAdjust.AdjustmentPercent` | *"This field is a placeholder in preparation for an upcoming enhancement."* |
| `Contract.RatioTermAutoRenewToLife`, `.RatioTermBargainRenewToLife`, `.RatioLeaseAutoRenewToFMV`, `.RatioLeaseBargainRenewToFMV` | *"This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test."* |
| `Contract.AutomaticRenewalInLease`, `.AutomaticRenewalOption`, `.BargainRenewalInLease`, `.BargainRenewalOption` | *"This field is not implemented for contracts or equipment contracts."* |
| `Contract.CodeProrationMethodID` | *"This field is related to the ExpenseSetup database table. It is not implemented at the contract- or equipment contract-level."* |
| `FiscalPeriod.FiscalPeriodName` | *"This field is not implemented."* |
| `ExpenseAccrualSetup.HoldFlag`, `AccrualTransaction.HoldFlag` | *"This flag is informational-only."* (retained as INPUT in the tables — they are stored and settable, just inert) |

## The four ACTION fields

`sTYPE_SUBMITBUTTON` fields on `Contract` — server-side processes, not data. These are the entry
points of the whole engine.

| Field | Label | Entry point for |
|---|---|---|
| `GenerateStraightLineRent` | Generate Straight-line Rent Schedule | Creates an `SLSummary` with `IsSLSchedule = true` + its `SLPeriod` rows |
| `GenerateFASBSchedule` | Generate 842 Rent Schedule | Creates an `SLSummary` with `IsASC842Schedule = true` + its `SLPeriod` rows |
| `GenerateIFRS16Schedule` | Generate IFRS 16 Rent Schedule | Creates an `SLSummary` with `IsIFRS16Schedule = true` + its `SLPeriod` rows |
| `ModifyStraightLineStatus` | Modify Straight-Line Status | Unknown — see [`straight-line.md`](straight-line.md#modify-straight-line-status) |

Seven further accrual-side buttons on `Contract` are in scope for the accrual sub-engine:
`GENERATE_ACCRUALS`, `GENERATE_ESTIMATED_ACCRUALS`, `GENERATE_EXPENSE_ACCRUALS`,
`GENERATE_PERCENTAGE_RENT_ACCRUALS`, `GENERATE_ASSET_RENT`, `DELETE_ACCRUAL_PAYMENTS`,
`PLAN_FORECAST`. None has a vendor definition.

## Rebuild hazards visible in this table

| Hazard | Where | Why it matters for ASG Edge+ |
|---|---|---|
| **Every non-key PG column is `TEXT`** | 6,882 of 7,069 typed columns in `_xlsx_lucernex_jcrew.txt`; the other 187 are `VARCHAR(64) NOT NULL` primary keys | There is no numeric typing to inherit. Constitution §4.4 requires `BigDecimal`; every migrated value must be parsed and validated, and every parse failure is a data-quality finding, not an exception to swallow. |
| **`sTYPE_PERCENT_OR_AMOUNT` — magnitude-typed** | `SLSummary.SLRemainingAssetBalance`, `Asset.RemainingAssetBalance` (`Percent or Currency`, max size 2147483647) | Vendor: *"If you enter a value between 0-100, the system will default the option button setting to Percentage. If you enter a value of 100.01 or above, the system will default the option button setting to Currency. You can override the default option button setting."* The stored value **does not carry its own unit**, and the user can override the guess. A migration cannot recover the intent from the number alone. |
| **`Percentage` max size 999999** | every `sTYPE_PERCENTAGE` field | Percentages are stored to 6 significant digits — enough for a rate like `4.375000`, but the scale is not declared. Pin the scale explicitly. |
| **`Currency` max size 999999999999999** | every `sTYPE_MONEY` field | 15 digits, scale undeclared. `BigDecimal(19,4)` covers it; `double` does not, and would silently lose cents at that magnitude. |
| **`2-Digit Number` / `5-Digit Number` declared max 2147483647** | `SLSummary.SLTermLength`, `ContractFinancialTest.RemainingLife`, `SLPeriod.ConversionRate*` | The label promises 2 or 5 digits; the declared bound is `Integer.MAX_VALUE`. The label is a display hint, not a constraint. |
| **Three-state vs. two-state Booleans of the same name** | `Asset.IsShortTerm` / `.IsLowAssetValue` are `sTYPE_NULL_CHECKBOX`; `Contract.IsShortTerm` / `.IsLowAssetValue` are `sTYPE_CHECKBOX` | `Boolean` on one, `Boolean` (nullable, with a meaningful null) on the other. Modelling both as primitive `boolean` destroys the "unset" state. |
| **List-in-a-text-column** | `SLSummary.AssociatedExpenseSetupIDs`, `SLSummary.RecalcOverrideNotesIDList`, `SLSummary.NeedsRecalcModifiedByMemberIDList`, `ExpenseSetup.VendorAllocationList` | Multi-valued relationships stored as delimited text. Rebuild as join tables; the delimiter is not documented. |
| **Untyped parent keys** | `ExpenseAccrualSchedule.ExpenseAccrualSetupID(Text)`, `AccrualTransaction.ExpenseAccrualSetupID(Text)` | Every sibling FK is typed; these two are not. Expect orphans. |
| **20 unnamed GL slots** | `ExportAcct1Number`…`ExportAcct20Number` on three code tables and on `SLPeriod`, plus 16 more account slots on `AccrualTransaction` | Numbered, not named. The semantics are pure tenant convention and are not in the schema. |

---

## Classification tables

Columns: **Class** · **Field** · **Label** (Lucernex UI label) · **Lucernex type** (from
`_xlsx_lucernex_jcrew.txt`) · **Data-Fields type** (`sTYPE_*` / `sCODE_*` from
`docs/data-fields/all-fields.csv`; `-` where the field is not exposed as a Manage Data Fields leaf) ·
**Fn** (vendor `Functional Field` flag) · **Evidence**.

### Contract — accounting-bearing fields only (`contract_admin` / `contract_financial`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `ComputedSLDiscountRate` | Computed Discount Rate | Percentage | `sTYPE_PERCENTAGE` | No | Functional=No; vendor help: "The default discount rate. Lucernex will first use the discount rate at the Portfolio-level, if it exists, otherwise it will use the rate at the Firm-" |
| **COMPUTED** | `CurrentStraightLineAssetBalance` | Current Straight Line Asset Balance | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "The asset balance value from the first active period." |
| **COMPUTED** | `CurrentStraightLineLiabilityBalance` | Current Straight Line Liability Balance | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "The liability balance value from the first active period." |
| **COMPUTED** | `FairValueThreshold` | Fair Value Threshold | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "This field computes the default fair value threshold to use for the contract. The system uses the portfolio-level value if one exists, otherwise it us" |
| **COMPUTED** | `FinalResult` | Final Result | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "The final result of the ASC 842 test." |
| **COMPUTED** | `InAlternateRent` | In Alternate Rent? | Boolean | `sTYPE_BOOLEAN` | Yes | vendor help: "This field returns true if this contract has any alternate rent records which are impacting amounts owed." |
| **COMPUTED** | `LatestFinancialTestFinalResult` | Latest Financial Test Result | Text | `sTYPE_TEXT` | Yes | vendor help: "The final result of the most recently locked ASC 842 test." |
| **COMPUTED** | `RemainingEconomicLifeThreshold` | Remaining Economic Life Threshold | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "This field computes the default value of the remaining economic life threshold field to use for this contract. The field first searches for a portfoli" |
| **COMPUTED** | `TermLength` | Term Length | Number | `sTYPE_DATE_MATH_OPERATION` | Yes | type `sTYPE_DATE_MATH_OPERATION`; vendor help: "The contract term length in years." |
| **COMPUTED** | `Test1Result` | Test #1 Result | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains result 1 of the Capital Lease test for the contract." |
| **COMPUTED** | `Test2Result` | Test #2 Result | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains result 2 of the Capital Lease test for the contract." |
| **COMPUTED** | `Test3Result` | Test #3 Result | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains result 3 of the Capital Lease test for the contract." |
| **COMPUTED** | `Test4Result` | Test #4 Result | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains result 4 of the Capital Lease test for the contract." |
| **COMPUTED** | `Test5aResult` | Test #5a Result | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains result 5 of the Capital Lease test for the contract." |
| **COMPUTED** | `Test5bResult` | Test #5b Result | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains result 6 of the Capital Lease test for the contract." |
| **INPUT** | `AggregateNNNBaseRentNPV` | Aggregate NNN Base Rent NPV | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the present value of NNN rent over the analysis period the "lease term"." |
| **INPUT** | `BaseYearOperatingExpenses` | Base Year Operating Expenses | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the amount of operating expenses included in the base rent." |
| **INPUT** | `BaseYearOtherExpenses` | Base Year Other Expenses | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the amount of any exclusions, other than operating expenses and taxes, from base ren" |
| **INPUT** | `BaseYearRETax` | Base Year RE Tax | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the amount of real estate taxes included in the base rent." |
| **INPUT** | `CommenceDate` | Commence Date | Date | `sTYPE_DATE` | Yes | vendor help: "Enter the date when the first term for the lease started in this field. The Commencement Date and the Expiration Date must be populated in order to us" |
| **INPUT** | `ContainsBargainPurchaseOption` | Contains Bargain Purchase Option? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This check box appears in Test 2 of the Capital Lease Test. Select the check box if the lease contains a purchase option that the tenant is likely to" |
| **INPUT** | `DiscountRate` | Contract Discount Rate | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "This field is where you enter the Discount Rate (also known as the Interest Rate or the Internal Borrower Rate [IBR])." |
| **INPUT** | `DoesTitleRevertToTenant` | Does Title Revert To Tenant? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This check box appears in Test 1 of the Capital Lease Test. Select the check box if the ownership of the asset reverts to the tenant at the end of the" |
| **INPUT** | `ExpireDate` | Expire Date | Date | `sTYPE_DATE` | Yes | vendor help: "Enter the current expiration date (excluding options) in this field. The Commencement Date and the Expiration Date must be populated in order to use t" |
| **INPUT** | `FMVOfBuilding` | FMV Of Building | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the price at which the property would change hands between a willing buyer and a wil" |
| **INPUT** | `FMVOfLand` | FMV Of Land | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the fair market value of the land." |
| **INPUT** | `FMVSource` | FMV Source | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the name of the person who assessed the fair value of the asset." |
| **INPUT** | `IsLowAssetValue` | Is Low Asset Value | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "Select this check box if the asset is low value." |
| **INPUT** | `IsShortTerm` | Is Short Term | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "Select this check box if the contract is short-term." |
| **INPUT** | `IsTranslation` | Is Translation | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Select this check box if you want to convert currency fields according to the Translation mapping specified on the Admin > Manage Company > Financial" |
| **INPUT** | `LeasedLandArea` | Leased Land Area | Number | `sTYPE_AREA` | Yes | vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the area of any additional land that may be leased under the contract. For example," |
| **INPUT** | `MonthToMonth` | Month To Month? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "Select this check box to indicate that your contract is month-to-month. You will also need to mark your expenses as month-to-month." |
| **INPUT** | `ProjectLandArea` | Project Land Area | Number | `sTYPE_AREA` | Yes | vendor help: "This field is included in Test 4 of the Capital Lease Test. Enter the total area of the lot that the building occupies." |
| **INPUT** | `RemainingLife` | Remaining Life | Number | `sTYPE_NUMBER` | Yes | vendor help: "This field appears in Test 3 of the Capital Lease Test. Enter the remaining useful life in this field. The Economic Useful Life is the estimated remai" |
| **INPUT** | `YearBuilt` | Year Built | Number | `sTYPE_DROPDOWN_YEAR` | Yes | vendor help: "This field appears in Test 3 of the Capital Lease Test. Select the year that the asset was built or the year that the asset's useful life began from t" |
| **ACTION** | `GenerateFASBSchedule` | Generate 842 Rent Schedule | Action button | `sTYPE_SUBMITBUTTON` | - | type `sTYPE_SUBMITBUTTON`; vendor help: "Form action button that triggers a server-side process — not a stored data value." |
| **ACTION** | `GenerateIFRS16Schedule` | Generate IFRS 16 Rent Schedule | Action button | `sTYPE_SUBMITBUTTON` | - | type `sTYPE_SUBMITBUTTON`; vendor help: "Form action button that triggers a server-side process — not a stored data value." |
| **ACTION** | `GenerateStraightLineRent` | Generate Straight-line Rent Schedule | Action button | `sTYPE_SUBMITBUTTON` | - | type `sTYPE_SUBMITBUTTON`; vendor help: "Form action button that triggers a server-side process — not a stored data value." |
| **ACTION** | `ModifyStraightLineStatus` | Modify Straight-Line Status | Action button | `sTYPE_SUBMITBUTTON` | - | type `sTYPE_SUBMITBUTTON`; vendor help: "Form action button that triggers a server-side process — not a stored data value." |
| **DEAD** | `AutomaticRenewalInLease` | Automatic Renewal In Lease? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This field is not implemented for contracts or equipment contracts." |
| **DEAD** | `AutomaticRenewalOption` | Automatic Renewal Option? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This field is not implemented for contracts or equipment contracts." |
| **DEAD** | `BargainRenewalInLease` | Bargain Renewal In Lease? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This field is not implemented for contracts or equipment contracts." |
| **DEAD** | `BargainRenewalOption` | Bargain Renewal Option? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This field is not implemented for contracts or equipment contracts." |
| **DEAD** | `RatioLeaseAutoRenewToFMV` | Ratio Lease w/ Auto Renewal To FMV | Percentage | `sTYPE_PERCENTAGE` | No | Functional=No; vendor help: "This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test." |
| **DEAD** | `RatioLeaseBargainRenewToFMV` | Ratio Lease w/ Bargain Renewal To FMV | Percentage | `sTYPE_PERCENTAGE` | No | Functional=No; vendor help: "This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test." |
| **DEAD** | `RatioTermAutoRenewToLife` | Ratio Term w/ Auto Renewal To Life | Percentage | `sTYPE_PERCENTAGE` | No | Functional=No; vendor help: "This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test." |
| **DEAD** | `RatioTermBargainRenewToLife` | Ratio Term w/ Bargain Renewal To Life | Percentage | `sTYPE_PERCENTAGE` | No | Functional=No; vendor help: "This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test." |

### ContractFinancialTest — the ASC 842 / IFRS 16 classification record (`contract_financial_test`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `ASC842CalcAggValOfLeaseNoAdj` | ASC 842 Aggregate Value Of Lease Before Adjustments | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the cash value of the lease between the accounting begin date and end date." |
| **COMPUTED** | `ASC842CalcAggValueOfLease` | ASC 842 Aggregate Value Of Lease | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the cash value of the lease between the accounting begin date and end date with accounting assumption adjustments." |
| **COMPUTED** | `ASC842CalcPVOfFinTermsNoAdj` | ASC 842 PV Of Financial Terms Before Adjustments | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the present value of your financial terms as of your accounting begin date, prior to any accounting assumption adjustments." |
| **COMPUTED** | `ASC842CalcPVOfFinancialTerms` | ASC 842 PV Of Financial Terms | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the present value of your financial terms of your accounting begin date, after accounting assumption adjustments." |
| **COMPUTED** | `ASC842InitialAssetBalance` | ASC 842 Initial Asset Balance | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "This field displays the asset balance as of the accounting begin date." |
| **COMPUTED** | `ASC842InitialLiabilityBalance` | ASC 842 Initial Liability Balance | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "This field displays the liability balance as of the accounting begin date." |
| **COMPUTED** | `ASC842NetLeaseLiabilityBalance` | ASC 842 Net Lease Liability Balance | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "This field displays the cash value of lease payments plus any adjustments due to covenants." |
| **COMPUTED** | `AutoComputed` | Auto Computed? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This field will have a true value if the ASC 842 test was computed automatically by the system." |
| **COMPUTED** | `BaseName` | Base Name | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "This field displays the file name of the file attached to the record." |
| **COMPUTED** | `CancellationOptionAmount` | Cancellation Option Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field pulls the value of any cancellation options from the Covenants table." |
| **COMPUTED** | `CommenceDate` | Commence Date | Date | `sTYPE_DATE` | Yes | vendor help: "This field pulls the commencement date of the lease entered on the Contract / Equipment Contract > Details > Summary page." |
| **COMPUTED** | `ComputedTestTermLengthToRemainingLife` | Test Term Length to Remaining Life | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "This value is calculated by the system. The value of this field is the Term Length (based on Test) divided by the Remaining Economic Life. The compari" |
| **COMPUTED** | `ExpireDate` | Expire Date | Date | `sTYPE_DATE` | Yes | vendor help: "This field pulls the expiration date of the lease entered on the Contract / Equipment Contract > Details > Summary page." |
| **COMPUTED** | `FairValueControlled` | Fair Value Controlled | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "The Fair Value of the Asset multiplied by the Portion of the Asset Controlled. The value in this field is used to set the overall market value of your" |
| **COMPUTED** | `FinalResult` | Final Result | Text | `sTYPE_TEXT` | Yes | vendor help: "The final result of the ASC 842 test. If you "failed" at least one of the five tests, your lease is considered a Finance lease. If you "passed" all fi" |
| **COMPUTED** | `IFRS16CalcAggValOfLeaseNoAdj` | IFRS 16 Aggregate Value Of Lease Before Adjustments | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the cash value of the lease between the accounting begin date and end date." |
| **COMPUTED** | `IFRS16CalcAggValueOfLease` | IFRS 16 Aggregate Value Of Lease | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the cash value of the lease between the accounting begin date and end date with accounting assumption adjustments." |
| **COMPUTED** | `IFRS16CalcPVOfFinTermsNoAdj` | IFRS 16 PV Of Financial Terms Before Adjustments | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the present value of your financial terms as of your accounting begin date, prior to any accounting assumption adjustments." |
| **COMPUTED** | `IFRS16CalcPVOfFinancialTerms` | IFRS 16 PV Of Financial Terms | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the present value of your financial terms of your accounting begin date, after accounting assumption adjustments." |
| **COMPUTED** | `IFRS16InitialAssetBalance` | IFRS 16 Initial Asset Balance | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "This field displays the asset balance as of the accounting begin date." |
| **COMPUTED** | `IFRS16InitialLiabilityBalance` | IFRS 16 Initial Liability Balance | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "This field displays the liability balance as of the accounting begin date." |
| **COMPUTED** | `IFRS16NetLeaseLiabilityBalance` | IFRS 16 Net Lease Liability Balance | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "This field displays the cash value of lease payments plus any adjustments due to covenants." |
| **COMPUTED** | `InitLiabilityBalToThreshFairValueCtrld` | Initial Liability Balance to Threshold Fair Value Controlled | Percentage | `sTYPE_PERCENT_MATH_OPERATION` | Yes | type `sTYPE_PERCENT_MATH_OPERATION`; vendor help: "The value of this field is equal to the Initial Liability Balance divided by the Threshold Fair Value Controlled. The value of this field is displayed" |
| **COMPUTED** | `LastLikelyOptionDate` | Last Likely Option Date | Date | `sTYPE_DATE` | Yes | vendor help: "If you have marked any terms as Likely on the Abstract Info > Terms page, this field will pull the end date of the last likely term." |
| **COMPUTED** | `LikelyTermLength` | Likely Term Length | Number | `sTYPE_DATE_MATH_OPERATION` | Yes | type `sTYPE_DATE_MATH_OPERATION`; vendor help: "If you have marked any terms as Likely on the Abstract Info > Terms page, this field will calculate the length of your likely term." |
| **COMPUTED** | `PVOfFinancialTermsWithAdjustments` | PV Of Financial Terms With Adjustments | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "This field displays the present value of your financial terms minus any accounting assumption adjustments added to the Accounting Assumption Adjustmen" |
| **COMPUTED** | `PurchaseOptionAmount` | Purchase Option Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field pulls the value of any purchase options from the Covenant table." |
| **COMPUTED** | `ResidualValueGuarantees` | Residual Value Guarantees | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field pulls the value of any residual value guarantees from the Covenant table." |
| **COMPUTED** | `TermLength` | Term Length | Number | `sTYPE_DATE_MATH_OPERATION` | Yes | type `sTYPE_DATE_MATH_OPERATION`; vendor help: "This field displays the term length of your lease based upon the difference between the Commencement Date and the Expiration Date of the lease. This v" |
| **COMPUTED** | `Test1Result` | Test #1 Result | Boolean | `sTYPE_PASS_FAIL` | Yes | type `sTYPE_PASS_FAIL`; vendor help: "This field displays the results of Test 1 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance" |
| **COMPUTED** | `Test2Result` | Test #2 Result | Boolean | `sTYPE_PASS_FAIL` | Yes | type `sTYPE_PASS_FAIL`; vendor help: "This field displays the results of Test 2 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance" |
| **COMPUTED** | `Test3Result` | Test #3 Result | Boolean | `sTYPE_PASS_FAIL` | Yes | type `sTYPE_PASS_FAIL`; vendor help: "This field displays the results of Test 3 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance" |
| **COMPUTED** | `Test4Result` | Test #4 Result | Boolean | `sTYPE_PASS_FAIL` | Yes | type `sTYPE_PASS_FAIL`; vendor help: "This field displays the results of Test 4 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance" |
| **COMPUTED** | `Test5Result` | Test #5 Result | Boolean | `sTYPE_PASS_FAIL` | Yes | type `sTYPE_PASS_FAIL`; vendor help: "This field displays the results of Test 5 of the ASC 842 Test. If you "fail" at least one of the five tests, the lease will be classified as a Finance" |
| **COMPUTED** | `TestTermLength` | Test Term Length | Number | `sTYPE_DATE_MATH_OPERATION` | Yes | type `sTYPE_DATE_MATH_OPERATION`; vendor help: "This field displays the length of the test term that you have selected using the Test Begin Date and Test End Date fields. It is automatically calulca" |
| **COMPUTED** | `ThresholdFairValueControlled` | Threshold Fair Value Controlled | Currency | `sTYPE_MONEY_MATH_OPERATION` | Yes | type `sTYPE_MONEY_MATH_OPERATION`; vendor help: "The value in this field is the Fair Value Controlled multiplied by the Fair Value Threshold. This value sets the benchmark to which you will compare y" |
| **INPUT** | `ContainsBargainPurchaseOption` | Contains Bargain Purchase Option? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This check box is Test 2 of the ASC 842 Test. Select this check box if the lease contains a purchase option that the tenant is likely to exercise." |
| **INPUT** | `DiscountRate` | Discount Rate | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "This field is where you enter the Discount Rate (also known as the Interest Rate or the Internal Borrower Rate [IBR])." |
| **INPUT** | `DismantlingStorageCostAmount` | Dismantling / Restoring Cost Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the cost of any activity necessary to restore the asset to its original state prior to the expiration of the lease." |
| **INPUT** | `DismantlingStorageCostDesc` | Dismantling / Restoring Cost Desc | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter a description of the cost of any activity necessary to restore the asset to its original state prior to the expiration of the lease." |
| **INPUT** | `DoesTitleRevertToTenant` | Does Ownership Revert To Tenant? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This check box is Test 1 of the ASC 842 test. Select this check box if the ownership of the asset reverts to the tenant at the end of the lease term." |
| **INPUT** | `FairValueOfAsset` | Fair Value Of Asset | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the fair value of the asset. FASB 842.10.20 defines fair value as the price that would be received to sell an asset or paid to transfer a liabil" |
| **INPUT** | `FairValueSource` | Fair Value Source | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter the name of the person who assessed the fair value of the asset." |
| **INPUT** | `FairValueThreshold` | Fair Value Threshold | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "Enter the fraction of the fair value of the underlying asset that amounts to substantially all of its fair value. This value is usually set to 90%." |
| **INPUT** | `ImpairmentsAmount` | Impairments Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any deductions related to the diminished value of the asset as a negative number." |
| **INPUT** | `ImpairmentsDesc` | Impairments Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter a description of the costs related to the diminished value of the asset." |
| **INPUT** | `InitialDirectCostsAmount` | Initial Direct Costs Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the incremental costs of a lease that would not have been incurred if the lease had not been obtained. For example, for contracts broker s fees," |
| **INPUT** | `InitialDirectCostsDesc` | Initial Direct Costs Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter a description of the incremental costs of a lease that would not have been incurred if the lease had not been obtained." |
| **INPUT** | `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any adjustments to the initial liability for the asset in this field." |
| **INPUT** | `IsAssetTooSpecializedForLessor` | Is Asset Too Specialized For Lessor? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This check box is Test 5 of the ASC 842 Test. Select this check box if the asset has a specialized use, such as that the lessor will have no alternati" |
| **INPUT** | `IsLeaseNearEnd` | Is the lease commencement at or near the end of the economic life of the asset? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This check box is in Test 3 of the ASC 842 Test. Select this check box if the lease commencement is at or near the end of the economic life of the ass" |
| **INPUT** | `IsLocked` | Is Locked? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Once you are certain that the results of your ASC 842 Test are correct, select this check box. Locking the test ensures that the test cannot be modifi" |
| **INPUT** | `LeaseIncentivesAmount` | Lease Incentives Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any incentives that have reduced the cost of the lease." |
| **INPUT** | `LeaseIncentivesDesc` | Lease Incentives Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter a description of any incentive amounts that have reduced the cost of the lease." |
| **INPUT** | `LineNumber` | Line Number | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter the line number where the fair value is referenced in the lease document." |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `PVOfCancellationOption` | PV Of Cancellation Option | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the present value of the cancellation option." |
| **INPUT** | `PVOfOtherAdjustments` | PV Of Other Adjustments | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any other miscellaneous costs that should be accounted for in the schedule." |
| **INPUT** | `PVOfOtherAdjustmentsDesc` | Other Adjustments Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter a description of any other miscellaneous costs that should be accounted for in the schedule." |
| **INPUT** | `PVOfPurchaseOption` | PV Of Purchase Option | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the present value of the purchase option." |
| **INPUT** | `PVOfResidualValueGuarantees` | PV Of Residual Value Guarantees | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the present value of the residual value guarantee." |
| **INPUT** | `PVOfStructuringCosts` | PV Of Structuring Costs | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any fees paid to the owners of a special-purpose entity for structuring the transaction." |
| **INPUT** | `PVOfStructuringCostsDesc` | Structuring Costs Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter a description of any fees paid to the owners of a special-purpose entity for structuring the transaction." |
| **INPUT** | `PageNumber` | Page Number | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter the page number where the fair value is referenced in the lease document." |
| **INPUT** | `ParagraphNumber` | Paragraph Number | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter the paragraph number where the fair value is referenced in the lease document." |
| **INPUT** | `PortionOfAssetControlled` | Portion Of Asset Controlled | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "Enter the percentage based upon the rentable area divided by the total area of the asset." |
| **INPUT** | `PreCommencePayAmount` | Pre-Commencement Payments Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the amount paid towards rent prior to the commencement date, minus any incentives that have reduced the cost of the lease. You should also inclu" |
| **INPUT** | `PreCommencePayDesc` | Pre-Commencement Payments Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter a description of the amount paid towards rent prior to the commencement date, minus any incentives that have reduced the cost of the lease." |
| **INPUT** | `RemainingEconomicLifeThreshold` | Remaining Economic Life Threshold | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "Enter the fraction of the economic life of the underlying asset that amounts to a major part of that remaining economic life. This value is usually se" |
| **INPUT** | `RemainingLife` | Remaining Life | 2-Digit Number | `sTYPE_NUMBER_FRACTION2DIGITS` | Yes | vendor help: "Enter the number value of the remaining economic life in this field." |
| **INPUT** | `SectionNumber` | Section Number | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "This field is no longer in use." |
| **INPUT** | `Topic842BeginDate` | Accounting Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "This date is the date your organization is adopting ASC 842, or the Possession Begin Date, whichever is later." |
| **INPUT** | `Topic842EndDate` | Accounting End Date | Date | `sTYPE_DATE` | Yes | vendor help: "This is the end date of your ASC 842 financial accounting for the contract, including any likely options." |
| **INPUT** | `YearBuilt` | Year Built | Number | `sTYPE_DROPDOWN_YEAR` | No | Functional=No; vendor help: "Select the year that the asset's useful life began, or the year the asset was built from the field." |
| **CODE-TABLE** | `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | `sCODE_ASC842_SCHEDULE` | Yes | vendor help: "The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeAccountingMethodID` | Accounting Method | Dropdown (Accounting Method Code) | `sCODE_ACCOUNTING_METHOD` | Yes | vendor help: "Select whether you want to calculate your schedule as an Operating schedule or a Finance schedule from this field." |
| **CODE-TABLE** | `CodeAcctMethodOverrideID` | Accounting Type Override | Dropdown (Accounting Method Code) | `sCODE_ACCOUNTING_METHOD` | Yes | vendor help: "Select the accounting method you want to use from this field." |
| **CODE-TABLE** | `CodeAssetTypeTestID` | Asset Type Tested | Dropdown (Asset Type Test Code) | `sCODE_ASSET_TYPE_TEST` | No | Functional=No; vendor help: "This field is no longer in use." |
| **CODE-TABLE** | `CodeIFRS16ScheduleID` | IFRS 16 Schedule Selector | Dropdown (IFRS 16 Schedule Type) | `sCODE_IFRS16_SCHEDULE` | Yes | vendor help: "The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeRemainingLifeFreqUnitID` | Remaining Life Freq Unit | Dropdown (Frequency Unit Code) | `sCODE_FREQUENCY_UNIT` | Yes | vendor help: "Select the frequency unit used to describe the remaining economic life of the asset. Example frequency units are weeks, months, and years." |
| **FK** | `AssetAssociatedProjectEntityID` | Asset Associated Entity | Entity | `sTYPE_MIXEDENTITY` | No | Functional=No; vendor help: "This is a reporting field that returns data about the asset associated with the entity." |
| **FK** | `AssetID` | Asset | Equipment ID | `sTYPE_ASSET` | Yes | vendor help: "The asset ID of the associated equipment asset." |
| **FK** | `AssociatedDocumentID` | Associated Document | Document ID | `sTYPE_DOCUMENT` | Yes | vendor help: "The ID of a document associated with this record." |
| **FK** | `ContractID` | ContractID | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **FK** | `FolderID` | Folder | Folder ID | `sTYPE_DOCUMENT` | Yes | vendor help: "The folder ID of the document connected to the fair value source on your ASC 842 Test." |
| **SYSTEM** | `BOMapClientRecordID` | Contract Financial Test ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `ContractFinancialTestID` | Contract Financial Test RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |

### SLSummary — the schedule header (`s_l_summary`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `AccumulatedAmortizationBalancePriorToImpairment` | Accumulated Amortization Balance Prior to Impairment | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `AssetAmortExpenseAdjustment` | Asset Amortization Expense Adjustment | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `AssetAmortizationExpense` | Asset Amortization Expense | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `AssociatedExpenseSetupIDs` | Associated Expense Setup IDs | Text | `sTYPE_TEXT` | Yes | vendor help: "The AssociatedExpenseSetupIDs field returns a list of associated expense setup IDs that use the expense type used in the accounting schedule you are v" |
| **COMPUTED** | `BalanceForward` | Balance Forward | Currency | `sTYPE_MONEY` | Yes | vendor help: "The difference between the asset and liability balance at the start of your accounting schedule." |
| **COMPUTED** | `BeyondCurrentFiscalYearCashExpense` | Current Fiscal Year and Beyond Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The amount of cash expense for the current fiscal year through to the end of the schedule." |
| **COMPUTED** | `BeyondCurrentFiscalYearInterestExpense` | Current Fiscal Year and Beyond Interest Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The amount of interest expense for the current fiscal year through to the end of the schedule." |
| **COMPUTED** | `BeyondFifthFiscalYearCashExpense` | Beyond Fifth Fiscal Year Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The amount of cash expense five years beyond the current fiscal year and through to the end of the schedule." |
| **COMPUTED** | `BeyondSixthFiscalYearCashExpense` | Beyond Sixth Fiscal Year Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The amount of cash expense six years beyond the current fiscal year and through to the end of the schedule." |
| **COMPUTED** | `CalcAggValueOfLeaseNoAdjust` | Aggregate Value Of Lease Before Adjustments | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the cash value of the lease between the accounting begin date and end date prior to any accounting assumption adjustments." |
| **COMPUTED** | `CalcAggregateValueOfLease` | Aggregate Value Of Lease | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the cash value of the lease between the accounting begin date and end date with accounting assumption adjustments." |
| **COMPUTED** | `CalcPVOfFinancialTerms` | PV Of Financial Terms | Currency | `sTYPE_MONEY` | Yes | vendor help: "The present value of your financial terms including any accounting assumptions adjustments." |
| **COMPUTED** | `CalcPVOfFinancialTermsNoAdjust` | PV Of Financial Terms Before Adjustments | Currency | `sTYPE_MONEY` | Yes | vendor help: "The present value of your financial terms prior to any accounting assumptions adjustments." |
| **COMPUTED** | `CancellationOptionAmount` | Cancellation Option Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The cash value of any contractual cancellation options." |
| **COMPUTED** | `CashExpenseAdjustment` | Cash Expense Adjustment | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `CurrentAssetBalance` | Current Period Asset Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "The current value of the right of use asset. In Report Builder currency conversions, a foreign exchange rate record will be applied that has an effect" |
| **COMPUTED** | `CurrentFiscalYearCashExpense` | Current Fiscal Year Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The cash expense summed over the current fiscal year." |
| **COMPUTED** | `CurrentFiscalYearQ1CashExpense` | Current Fiscal Year Q1 Cash Expense | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "This field displays the total cash expense for the remaining complete quarters in the fiscal year. This field will only populate if the period the rep" |
| **COMPUTED** | `CurrentFiscalYearQ2CashExpense` | Current Fiscal Year Q2 Cash Expense | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "This field displays the total cash expense for the remaining complete quarters in the fiscal year. This field will only populate if the period the rep" |
| **COMPUTED** | `CurrentFiscalYearQ3CashExpense` | Current Fiscal Year Q3 Cash Expense | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "This field displays the total cash expense for the remaining complete quarters in the fiscal year. This field will only populate if the period the rep" |
| **COMPUTED** | `CurrentFiscalYearQ4CashExpense` | Current Fiscal Year Q4 Cash Expense | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "This field displays the total cash expense for the remaining complete quarters in the fiscal year. This field will only populate if the period the rep" |
| **COMPUTED** | `CurrentLiabilityBalance` | Current Period Liability Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "The current value of the lease liability. In Report Builder currency conversions, this fields will be converted according to the foreign exchange rate" |
| **COMPUTED** | `CurrentRemainingCashBalance` | Current Remaining Balance Lease Payments | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the sum of the current and future remaining lease payments in the rent schedule." |
| **COMPUTED** | `CurrentRemainingCashBalanceAfterReportEnd` | Current Remaining Cash Balance After Report End | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field displays the sum of the future remaining lease payments in the rent schedule, excluding the current period." |
| **COMPUTED** | `EndingAccumulatedAmortizationBalance` | Ending Accumulated Amortization Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `EndingGrossAssetBalance` | Ending Gross Asset Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `EndingLeaseLiabilityBalance` | Ending Lease Liability Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `FifthFiscalYearCashExpense` | Fifth Fiscal Year Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The cash expense of the fiscal year five years after your current fiscal year." |
| **COMPUTED** | `Forward12MonthAssetChange` | 12-Month Forward Change in Asset Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "For period n, The change in the asset balance from period n + 1 to period n + 12. In Report Builder currency conversions, a foreign exchange rate reco" |
| **COMPUTED** | `Forward12MonthLiabilityChange` | 12-Month Forward Change in Liability Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "For period n, The change in the liability balance from period n + 1 to period n + 12. In Report Builder currency conversions, this fields will be conv" |
| **COMPUTED** | `FourthFiscalYearCashExpense` | Fourth Fiscal Year Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The cash expense of the fiscal year four years after your current fiscal year." |
| **COMPUTED** | `ImpairmentsAndAccumulatedAmortizationReset` | Impairments and Accumulated Amortization Reset | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `Inactive` | Is Inactive? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This flag is applied to a schedule if another lease accounting schedule replaces it." |
| **COMPUTED** | `InactiveDate` | Inactive Date | Date | `sTYPE_DATE` | Yes | vendor help: "The date that a schedule became inactive." |
| **COMPUTED** | `InitialAssetBalance` | Initial Asset Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is a calculated value which contains the initial value over the asset of the lease. In Report Builder currency conversions, a foreign exchange ra" |
| **COMPUTED** | `InitialAssetBalanceAdjust` | Initial Asset Balance Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field pulls the value of any adjustments to the initial asset balance from the ContractFinancialTest table." |
| **COMPUTED** | `InitialLiabilityBalance` | Initial Liability Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the total of all of the Period Payment Present Values over the life of the lease. In Report Builder currency conversions, a foreign exchange r" |
| **COMPUTED** | `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field pulls the value of any adjustments to the initial liability balance from the ContractFinancialTest table." |
| **COMPUTED** | `InterestBeforeMidRemeasure` | Interest Before Mid-period Remeasurement | Currency | `sTYPE_MONEY` | Yes | vendor help: "The partial interest from the start of the period to the remeasurement date." |
| **COMPUTED** | `InterestExpense` | Interest Expense | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `InterestExpenseAdjustment` | Interest Expense Adjustment | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `IsASC842Schedule` | Is ASC 842 Schedule? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This flag indicates that the schedule is an ASC 842 schedule." |
| **COMPUTED** | `IsIFRS16Schedule` | Is IFRS 16 Schedule? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This flag indicates that the schedule is an IFRS 16 schedule." |
| **COMPUTED** | `IsIncludeInRollForwardReport` | Is Include in Roll Forward Report? | Boolean | `sTYPE_BOOLEAN` | - | no vendor help text |
| **COMPUTED** | `IsSLSchedule` | Is SL Schedule? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This flag indicates that the schedule is an Straight Line schedule." |
| **COMPUTED** | `LastBalancePosted` | Last Balance Posted | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the asset minus the liability as of the last posted period." |
| **COMPUTED** | `LastPostedBalanceSheetImpact` | Last Posted Balance Sheet Impact | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the portion of the last posted balance that is to remain on the balance sheet." |
| **COMPUTED** | `LastPostedDate` | Last Posted Date | Date | `sTYPE_DATE` | Yes | vendor help: "This is the begin date of the last posted period." |
| **COMPUTED** | `LastPostedEndDate` | Last Posted End Date | Date | `sTYPE_DATE` | Yes | vendor help: "This is the end date of the last posted period." |
| **COMPUTED** | `LeaseExpirationAccumulatedAmortizationImpact` | Lease Expiration Accumulated Amortization Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `LeaseExpirationGrossAssetBalance` | Lease Expiration Gross Asset Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `LeaseLiabilityPaymentImpact` | Lease Liability Payment Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `LeaseRemeasurementAccumulatedAmortizationImpact` | Lease Remeasurement Accumulated Amortization Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `LeaseRemeasurementLeaseLiabilityImpact` | Lease Remeasurement Lease Liability Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `NeedsRecalcModifiedByLastMember` | Needs Recalc Modified by Last Member | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "This field lists the last member whose action would have caused the Recalc? flag to change." |
| **COMPUTED** | `NeedsRecalcModifiedByMemberIDList` | Needs Recalc Modified by Member List | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "This field lists all members who have made changes that would cause the Recalc? flag to change." |
| **COMPUTED** | `NeedsRecalculation` | Needs Recalculation | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "When set to Yes, this flag indicates that the lease accounting schedule must be recalculated." |
| **COMPUTED** | `NewGrossAssetBalances` | New Gross Asset Balances | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `NewLeaseLiabilities` | New Lease Liabilities | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `NextFiscalYearCashExpense` | Next Fiscal Year Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The cash expense of the fiscal year after your current fiscal year." |
| **COMPUTED** | `PeriodAmount` | Period Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The total expenses for the period from your recurring expenses. The value of this field is used to perform calculations for your lease accounting sche" |
| **COMPUTED** | `PostedAssetAdjustment` | Posted Total Asset Adjustment at Mod Input Date | Currency | `sTYPE_MONEY` | Yes | vendor help: "The difference between the Asset Balance of the new schedule and the previous schedule s last posted Asset Balance." |
| **COMPUTED** | `PostedEndDate` | Posted End Date | Date | `sTYPE_DATE` | Yes | vendor help: "The last posted fiscal period End Date of the schedule being modified." |
| **COMPUTED** | `PostedInitAssetAdj` | Posted Initial Asset Adjustment for Mod Effective Date | Currency | `sTYPE_MONEY` | Yes | vendor help: "The difference between the Initial Asset Balance of the new schedule and the previous schedule s posted Asset Balance as of the Posted End Date." |
| **COMPUTED** | `PostedInitLiabilityAdj` | Posted Initial Liability Adjustment for Mod Effective Date | Currency | `sTYPE_MONEY` | Yes | vendor help: "The difference between the Initial Liability Balance of the new schedule and the previous schedule s posted Liability Balance as of the Posted End Dat" |
| **COMPUTED** | `PostedLiabilityAdjustment` | Posted Total Liability Adjustment at Mod Input Date | Currency | `sTYPE_MONEY` | Yes | vendor help: "The difference between the Liability Balance of the new schedule and the previous schedule s last posted Liability Balance." |
| **COMPUTED** | `PriorAccumulatedAmortizationBalance` | Prior Accumulated Amortization Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "The Accumulated Amortization Balance of the accounting period prior to the impairment." |
| **COMPUTED** | `PriorPeriodAccumulatedAmortizationBalance` | Prior Period Accumulated Amortization Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `PriorPeriodGrossAssetBalance` | Prior Period Gross Asset Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `PriorPeriodLeaseLiability` | Prior Period Lease Liability | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `ProfitAndLossImpact` | Profit And Loss Impact | Currency | `sTYPE_MONEY` | Yes | vendor help: "The portion of the balance forward that will not persist on the balance sheet and is taken as a capital gain or loss." |
| **COMPUTED** | `PurchaseOptionAmount` | Purchase Option Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Create New Schedule window. This field pulls the value of any purchase options from the Covenant table." |
| **COMPUTED** | `RecalcOverrideNotesIDList` | Recalc Override Notes | Recalc Override Notes ID | `sTYPE_RECALC_NOTES` | - | no vendor help text |
| **COMPUTED** | `RecalcTriggerDate` | Recalculation Trigger Date | Date | `sTYPE_DATE` | Yes | vendor help: "The date that the Recalc? flag was triggered." |
| **COMPUTED** | `ReclassAccumulatedAmortizationImpact` | Reclass Accumulated Amortization Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `ReclassGrossAssetBalanceImpact` | Reclass Gross Asset Balance Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `ReclassLeaseLiabilityImpact` | Reclass Lease Liability Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `ReclassificationAccumulatedAmortizationImpact` | Reclassification Accumulated Amortization Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `ReclassificationLeaseLiabilityImpact` | Reclassification Lease Liability Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `ReclassificationOfGrossAssetBalance` | Reclassification of Gross Asset Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `RemeasurementBalanceForward` | Balance Sheet Impact | Currency | `sTYPE_MONEY` | Yes | vendor help: "The portion of the balance forward that does appear on the balance sheet going forward." |
| **COMPUTED** | `RemeasurementGrossAssetBalanceImpact` | Remeasurement Gross Asset Balance Impact | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `ResidualValueGuarantees` | Residual Value Guarantees | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Create New Schedule window. This field pulls the value of any residual value guarantees from the Covenant table." |
| **COMPUTED** | `SLTermLength` | Straight Line Term Length | 2-Digit Number | `sTYPE_NUMBER_FRACTION2DIGITS` | Yes | vendor help: "The number of periods in the straight line schedule term." |
| **COMPUTED** | `ShortenedLeaseLiabilityDiff` | Shortened Lease Liability Diff | Currency | `sTYPE_MONEY` | Yes | vendor help: "An initial Liability Balance based on the remaining periods of the original schedule over a shortened term minus the original schedule s last posted p" |
| **COMPUTED** | `ShortenedSchedInitLiabilityBal` | Shortened Schedule Initial Liability Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "An initial Liability Balance based on the remaining periods of the original schedule over a shortened term." |
| **COMPUTED** | `ShortenedTermAssetDiff` | Shortened Term Asset Diff | Currency | `sTYPE_MONEY` | Yes | vendor help: "The sum of the Asset Amortization Expense for the remaining periods in the original schedule over the shortened term multiplied by negative one." |
| **COMPUTED** | `ShortenedTermRentDiff` | Shortened Term Rent Diff | Currency | `sTYPE_MONEY` | Yes | vendor help: "The Initial Liability Balance of the new schedule minus the Initial Liability Balance of the remaining periods in the original schedule over the short" |
| **COMPUTED** | `SingleLeaseExpenseAdjustment` | Single Lease Expense Adjustment | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `SixthFiscalYearCashExpense` | Sixth Fiscal Year Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The cash expense of the fiscal year six years after your current fiscal year." |
| **COMPUTED** | `SleBeforeMidRemeasure` | Straight Line Expense Before Mid-period Remeasurement | Currency | `sTYPE_MONEY` | Yes | vendor help: "The partial single lease expense from the start of the period to the remeasurement date." |
| **COMPUTED** | `ThirdFiscalYearCashExpense` | Third Fiscal Year Cash Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The cash expense of the fiscal year three years after your current fiscal year." |
| **COMPUTED** | `TotalCommitment` | Total Commitment | Currency | `sTYPE_MONEY` | Yes | vendor help: "The sum of all rent payments for the life of the lease." |
| **COMPUTED** | `TotalImpairmentImpact` | Total Impairment Impact | Currency | `sTYPE_MONEY` | Yes | vendor help: "The sum of the impairment and the Prior Accumulated Amortization Balance." |
| **COMPUTED** | `TranslatedInitialAssetBalance` | Translated Initial Asset Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `TranslatedInitialLiabilityBalance` | Translated Initial Liability Balance | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **INPUT** | `BeginDate` | Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "The Begin Date field allows you to select a begin date for the record." |
| **INPUT** | `DiscountRate` | Discount Rate | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "This field is where you enter the Discount Rate (also known as the Interest Rate or the Internal Borrower Rate [IBR])." |
| **INPUT** | `DismantlingStorageCostAmount` | Dismantling / Restoring Cost Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Create New Schedule window. Enter the cost of any activity necessary to restore the asset to its original state prior to the" |
| **INPUT** | `EndDate` | End Date | Date | `sTYPE_DATE` | Yes | vendor help: "The End Date field allows you to select an end date for the record." |
| **INPUT** | `FinalAssetAllocPercent` | Final Asset Amount Allocation Percentage | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "If you want to specify a percentage of the total asset balance that should remain after the schedule end date, enter the value in this field. This fie" |
| **INPUT** | `FinalAssetAmount` | Final Asset Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "If you want to specify an amount of the total asset balance that should remain after the schedule end date, enter the value in this field. This field" |
| **INPUT** | `FinalAssetDate` | Final Asset Amount Date | Date | `sTYPE_DATE` | Yes | vendor help: "If you want to select a date beyond the schedule end date to amortize to, enter the date in this field. By default, the value of this field is the sch" |
| **INPUT** | `ImpairmentAmount` | Impairment Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any deductions related to the diminished value of the asset as a negative number." |
| **INPUT** | `InitialDirectCostAmount` | Initial Direct Cost Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Create New Schedule window. Enter the incremental costs of a lease that would not have been incurred if the lease had not be" |
| **INPUT** | `IsApproved` | Is Approved? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "This flag indicates that the schedule has been approved. Once a schedule has been approved, it cannot be un-approved. Please see the Lucernex Online H" |
| **INPUT** | `LeaseIncentiveAmount` | Lease Incentive Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Create New Schedule window. Enter any incentives that have reduced the cost of the lease." |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `PVOfCancellationOption` | PV Of Cancellation Option | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the present value of the cancellation option." |
| **INPUT** | `PVOfOtherAdjustments` | PV Of Other Adjustments | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any other miscellaneous costs that should be accounted for in the schedule." |
| **INPUT** | `PVOfPurchaseOption` | PV Of Purchase Option | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the present value of the purchase option." |
| **INPUT** | `PVOfResidualValueGuarantees` | PV Of Residual Value Guarantees | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the present value of the residual value guarantee." |
| **INPUT** | `PVOfStructuringCosts` | PV Of Structuring Costs | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any fees paid to the owners of a special-purpose entity for structuring the transaction." |
| **INPUT** | `PreCommencePayAmount` | Pre Commence Pay Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Create New Schedule window. Enter the amount paid towards rent prior to the commencement date, minus any incentives that hav" |
| **INPUT** | `SLRemainingAssetBalance` | Remaining Asset Balance | Percent or Currency | `sTYPE_PERCENT_OR_AMOUNT` | Yes | vendor help: "If you want to specify a percentage or amount of the total asset balance that should remain after the schedule end date, enter the value in this field" |
| **CODE-TABLE** | `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | `sCODE_ASC842_SCHEDULE` | Yes | vendor help: "The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeAccountingMethodID` | Accounting Method | Dropdown (Accounting Method Code) | `sCODE_ACCOUNTING_METHOD` | Yes | vendor help: "This field sets the accounting method for your lease accounting schedule. If its value is changed, you will need to remeasure your schedule." |
| **CODE-TABLE** | `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | `sCODE_CURRENCY_TYPE` | Yes | vendor help: "The Currency Type field allows you to select a currency type to be used on a record." |
| **CODE-TABLE** | `CodeIFRS16ScheduleID` | IFRS 16 Schedule | Dropdown (IFRS 16 Schedule Type) | `sCODE_IFRS16_SCHEDULE` | Yes | vendor help: "The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeSLScheduleID` | Straight Line Schedule | Dropdown (Straight Line Schedule Type) | `sCODE_SL_SCHEDULE` | No | Functional=No; vendor help: "This field displays the Straight Line Schedule ID." |
| **CODE-TABLE** | `CodeScheduleCreationReasonID` | Schedule Creation Reason | Dropdown (Schedule Creation Reason Code) | `sCODE_SCHEDULE_CREATION_REASON` | No | Functional=No; vendor help: "Select the reason the lease accounting schedule was created from this field." |
| **DEAD** | `DateRange` | Date Range | Date Range | `sTYPE_DATE_RANGE` | No | Functional=No; vendor help: "This field is not currently being used in Lucernex." |
| **FK** | `AssetAssociatedProjectEntityID` | Equipment Associated Entity | Entity | `sTYPE_MIXEDENTITY` | No | Functional=No; vendor help: "This is a reporting field that returns data about the asset associated with the entity." |
| **FK** | `AssetID` | Equipment | Equipment ID | `sTYPE_EQUIPMENT` | Yes | vendor help: "The asset ID of the equipment on your equipment schedule." |
| **FK** | `ContractID` | ContractID | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **FK** | `PriorLastPostedPeriodID` | Prior Schedule Last Posted Period | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field populaes with the SLSummary ID for the previous accounting schedule when a new schedule is created." |
| **SYSTEM** | `BOMapClientRecordID` | Straight Line Summary ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |
| **SYSTEM** | `SLSummaryID` | Straight Line Summary RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |

### SLPeriod — the per-period schedule row (`s_l_period`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `AssetAmount` | Asset Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the current value of the rented asset. The value of your asset is dependent upon whether you are calculating your lease as a Finance or Operat" |
| **COMPUTED** | `AssetTranslationAdjustment` | Asset Translation Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Fiscal Details grid when you calculate the FX Impact on the Rent Schedule page when a contract or equipment contract is mark" |
| **COMPUTED** | `BeginDate` | Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "The Begin Date field allows you to select a begin date for the record." |
| **COMPUTED** | `CashPaymentTranslated` | Cash Payment - Translated | Currency | `sTYPE_MONEY` | Yes | vendor help: "The translated value of the Cash Expense column in your lease accounting schedule." |
| **COMPUTED** | `ConversionRateAverage` | Period Average Rate | 5-Digit Number | `sTYPE_NUMBER_FRACTION6DIGITS` | Yes | vendor help: "The period average rate." |
| **COMPUTED** | `ConversionRateMonthEnd` | Cash Rate | 5-Digit Number | `sTYPE_NUMBER_FRACTION6DIGITS` | Yes | vendor help: "The cash rate." |
| **COMPUTED** | `CumulativeAssetAmortExpense` | Accumulated Amortization Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "For the first period of your schedule, this field's value is equal to the Asset Amortization Expense. For each subsequent period, this field's value i" |
| **COMPUTED** | `CumulativeDeferredBalance` | Cumulative Deferred Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "The sum of the deferred rent from the beginning of the schedule to the current period in the straight line schedule." |
| **COMPUTED** | `CumulativeTranslationAdjustment` | Cumulative Translation Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Fiscal Details grid when you calculate the FX Impact on the Rent Schedule page when a contract or equipment contract is mark" |
| **COMPUTED** | `EndDate` | End Date | Date | `sTYPE_DATE` | Yes | vendor help: "The End Date field allows you to select an end date for the record." |
| **COMPUTED** | `FXGainLoss` | FX Gain (Loss) | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `FiscalPeriod` | Fiscal Period | Number | `sTYPE_NUMBER` | Yes | vendor help: "This is the period number for your fiscal year. There are normally 12 periods in a year, except if you use 13-period accounting." |
| **COMPUTED** | `FiscalPeriodYear` | Fiscal Period Year | Number | `sTYPE_DROPDOWN_YEAR` | Yes | vendor help: "This is your fiscal year." |
| **COMPUTED** | `Forward12MonthAssetChange` | 12-Month Forward Change in Asset Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the sum of the asset amortization for the next 12 months." |
| **COMPUTED** | `Forward12MonthLiabilityAmortBased` | Short Term Liability (Amortization Based) | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the 12-Month Forward Change in Liability Balance if you have selected Liability Amortization Based as your setting for the Short-Term/Long-Ter" |
| **COMPUTED** | `Forward12MonthLiabilityChange` | 12-Month Forward Change in Liability Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the sum of the liability amortization for the next 12 months." |
| **COMPUTED** | `Forward12MonthLiabilityPVBased` | Short Term Liability (PV Based) | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the 12-Month Forward Change in Liability Balance if you have selected PV Based as your setting for the Short-Term/Long-Term Liability Calculat" |
| **COMPUTED** | `GrossAssetBalance` | Gross Asset Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field s value is equal to the Asset Balance + the Accumulated Amortization Balance." |
| **COMPUTED** | `InitialAssetBalance` | Initial Asset Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is a calculated value which contains the initial value over the asset of the lease." |
| **COMPUTED** | `InitialLiabilityBalance` | Initial Liability Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the total of all of the Period Payment Present Values over the life of the lease." |
| **COMPUTED** | `LiabilityAmount` | Liability Balance | Currency | `sTYPE_MONEY` | Yes | vendor help: "This is the current value of the liability. The value of your liability is dependent upon whether you are calculating your lease as a Finance or Opera" |
| **COMPUTED** | `LiabilityTranslationAdjustment` | Liability Translation Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field appears in the Fiscal Details grid when you calculate the FX Impact on the Rent Schedule page when a contract or equipment contract is mark" |
| **COMPUTED** | `LongTermLiability` | Long Term Liability | Currency | `sTYPE_MONEY` | Yes | vendor help: "The long-term liability is the current liability balance minus the short-term liability." |
| **COMPUTED** | `LongTermRentExpense` | Long Term Rent Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The sum of all rent expenses beyond 12 months." |
| **COMPUTED** | `PeriodAssetAmortizationExpense` | Period Asset Amortization Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The amount that the asset value is reduced from one period to the next. In Report Builder currency conversions, a foreign exchange rate record will be" |
| **COMPUTED** | `PeriodCashAmount` | Period Cash Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The amount of cash payments made during the period." |
| **COMPUTED** | `PeriodDeferredAmount` | Period Deferred Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The difference between the period cash rent and straight line rent expense." |
| **COMPUTED** | `PeriodLiabilityAmortizationExpense` | Period Liability Amortization Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The amount that the liability value is reduced from one period to the next. In Report Builder currency conversions, this fields will be converted acco" |
| **COMPUTED** | `PostedDate` | Posted Date | Date | `sTYPE_DATE` | Yes | vendor help: "The date that the Accounts Receivable transaction was posted." |
| **COMPUTED** | `RecordStatus` | Record Status | Text | `sTYPE_TEXT` | Yes | vendor help: "This field displays the current status of the period--either posted, not posted, or mixed." |
| **COMPUTED** | `SLExportAcct1Number` | SL Schedule Export Account #1 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an export account number. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **COMPUTED** | `SLExportAcct2Number` | SL Schedule Export Account #2 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an export account number. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **COMPUTED** | `SLExportAcct3Number` | SL Schedule Export Account #3 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an export account number. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **COMPUTED** | `ScheduleCumulativeAmortExpense` | Schedule Asset Amortization | Currency | `sTYPE_MONEY` | - | no vendor help text |
| **COMPUTED** | `ShortTermRentExpense` | Short Term Rent Expense | Currency | `sTYPE_MONEY` | Yes | vendor help: "The sum of all the rent expenses for the next 12 months." |
| **INPUT** | `AssetAmortizationExpenseTranslated` | Asset Amortization Expense - Translated | Currency | `sTYPE_MONEY` | Yes | vendor help: "The translated value of the Asset Amortization Expense column in your lease accounting schedule." |
| **INPUT** | `AssetAmountTranslated` | Asset Balance - Translated | Currency | `sTYPE_MONEY` | Yes | vendor help: "The translated value of the Asset Balance column in your lease accounting schedule." |
| **INPUT** | `ContractID` | Contract | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **INPUT** | `CumulativePeriodNumber` | Cumulative Period Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The current period number out of the total cumulative number of periods in the lease." |
| **INPUT** | `ExportAcct10Number` | Schedule Export Account #10 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct11Number` | Schedule Export Account #11 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct12Number` | Schedule Export Account #12 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct13Number` | Schedule Export Account #13 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct14Number` | Schedule Export Account #14 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct15Number` | Schedule Export Account #15 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct16Number` | Schedule Export Account #16 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct17Number` | Schedule Export Account #17 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct18Number` | Schedule Export Account #18 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct19Number` | Schedule Export Account #19 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct1Number` | Schedule Export Account #1 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct20Number` | Schedule Export Account #20 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct2Number` | Schedule Export Account #2 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct3Number` | Schedule Export Account #3 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct4Number` | Schedule Export Account #4 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct5Number` | Schedule Export Account #5 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct6Number` | Schedule Export Account #6 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct7Number` | Schedule Export Account #7 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct8Number` | Schedule Export Account #8 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct9Number` | Schedule Export Account #9 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `InterestTranslated` | Interest - Translated | Currency | `sTYPE_MONEY` | Yes | vendor help: "The translated value of the Interest Expense column in your lease accounting schedule." |
| **INPUT** | `LeaseLiabilityTranslated` | Lease Liability - Translated | Currency | `sTYPE_MONEY` | Yes | vendor help: "The translated value of the Lease Liability column in your lease accounting schedule." |
| **INPUT** | `LiabilityFXImpact` | Liability FX Impact | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field allows you to report the foreign exchange liability impact. The calculation for this field is Period Liability FX Impact = (FX rate for thi" |
| **INPUT** | `NumberDays` | Number Days | Number | `sTYPE_NUMBER` | Yes | vendor help: "The length of the period in days." |
| **INPUT** | `PVOfPeriodCashAmount` | PV Of Period Cash Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The Present Value of a future cash payment in today's valuation. This value is discounted to present value from the period that the payment will be ma" |
| **INPUT** | `PeriodExpenseAmount` | Period Expense Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The cash rent straight lined over the life of the schedule." |
| **INPUT** | `PeriodInterestAmount` | Period Interest Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The interest owed on the liability based on the discount rate." |
| **INPUT** | `SLPeriodAllocations` | Allocations | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter any straight line period allocations in this field." |
| **CODE-TABLE** | `CodeSLScheduleID` | Straight Line Schedule | Dropdown (Straight Line Schedule Type) | `sCODE_SL_SCHEDULE` | Yes | vendor help: "This field displays the Straight Line Schedule ID." |
| **FK** | `AssetAssociatedProjectEntityID` | Equipment Associated Entity | Entity | `sTYPE_MIXEDENTITY` | No | Functional=No; vendor help: "This is a reporting field that returns data about the asset associated with the entity." |
| **FK** | `AssetID` | Equipment | Equipment ID | `sTYPE_EQUIPMENT` | Yes | vendor help: "The asset ID of the equipment associated with this period." |
| **FK** | `SLSummaryID` | Straight Line Summary | Straight-Line Schedule ID | `sTYPE_SL_SUMMARY` | Yes | vendor help: "The ID of the lease accounting schedule associated with this period." |
| **SYSTEM** | `BOMapClientRecordID` | Straight Line Period ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |
| **SYSTEM** | `SLPeriodID` | Straight Line Period RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |

### AcctingAssumptionAdjust (`accting_assumption_adjust`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `AnnualAmount` | Annual Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The Annual Amount field is where the system will store the annual amount of the accounting assumption adjustment. The First Payment Amount, Last Payme" |
| **COMPUTED** | `FirstPaymentAmount` | First Payment Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The First Payment Amount field is where the system will store the first payment amount. The First Payment Amount, Last Payment Amount, and Annual Amou" |
| **COMPUTED** | `LastPaymentAmount` | Last Payment Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The Last Payment Amount field is where the system will store the last payment amount. The First Payment Amount, Last Payment Amount, and Annual Amount" |
| **INPUT** | `BeginDate` | Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "The Begin Date field allows you to select a begin date for the record." |
| **INPUT** | `EndDate` | End Date | Date | `sTYPE_DATE` | Yes | vendor help: "The End Date field allows you to select an end date for the record." |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `PaymentAmount` | Payment Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter your payment amount for the accounting assumption adjustment in this field." |
| **INPUT** | `PaymentRate` | Payment Rate | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the payment rate in this field. The payment rate is a currency value: for example, $1.00 per square foot." |
| **INPUT** | `SecondaryRentSchedAllocPercent` | Accounting Assumption Adjustment Secondary Rent Schedule Allocation Percent | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "If the expense setup has a secondary schedule allocation percentage, enter the allocation in this field." |
| **CODE-TABLE** | `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | `sCODE_ASC842_SCHEDULE` | Yes | vendor help: "The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeFrequencyID` | Frequency | Dropdown (Frequency Code) | `sCODE_FREQUENCY` | Yes | vendor help: "Select the frequency of your payment from this field." |
| **CODE-TABLE** | `CodeIFRS16ScheduleID` | IFRS 16 Schedule | Dropdown (IFRS 16 Schedule Type) | `sCODE_IFRS16_SCHEDULE` | Yes | vendor help: "The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeProrationMethodID` | Proration Method | Dropdown (Proration Method Code) | `sCODE_PRORATION_METHOD` | Yes | vendor help: "Select a proration method from this field. The proration method you choose tells the system how much a day is worth, when your cost period does not en" |
| **DEAD** | `AdjustmentPercent` | Adjustment Percent | Percentage | `sTYPE_PERCENTAGE` | No | Functional=No; vendor help: "This field is a placeholder in preparation for an upcoming enhancement." |
| **FK** | `ContractID` | ContractID | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **FK** | `ExpenseSetupID` | Expense Setup | Expense Setup ID | `sTYPE_EXPENSE_SETUP` | Yes | vendor help: "The ExpenseSetupID field is used to associate an accounting assumption adjustment with an expense setup record." |
| **SYSTEM** | `AcctingAssumptionAdjustID` | Accting Assumption Adjust RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `BOMapClientRecordID` | Accting Assumption Adjust ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |

### FinancialAdjustment (`financial_adjustment`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **INPUT** | `Amount` | Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the amount of the accounting assumption adjustment of the asset in this field. This field appears on the Equipment Contract > Payment Info > Rec" |
| **INPUT** | `EffectiveDate` | Effective Date | Date | `sTYPE_DATE` | Yes | vendor help: "Enter the effective date of the accounting assumption adjustment for the asset in this field. This field appears on the Equipment Contract > Payment I" |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `ThirdPartyRVGAmount` | Portion Guaranteed By 3rd Party | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "The total value of the residual value guarantee, positive or negative." |
| **INPUT** | `TotalRVGAmount` | Total Residual Value Guarantee | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "The residual value guarantee amount which is guaranteed by a third party, positive or negative. Both positive and negative numbers can be entered in t" |
| **CODE-TABLE** | `CodeAccountingAdjustmentTypeID` | Accounting Adjustment Type | Dropdown (Accounting Adjustment Type Code) | `sCODE_ACCOUNTING_ADJUSTMENT_TYPE` | No | Functional=No; vendor help: "Select the accounting adjustment type from this field. The available options are Cancellation Option, Residual Value Guarantee, and Purchase Option." |
| **CODE-TABLE** | `CodeFinancialAdjustmentStatusID` | Financial Adjustment Status | Dropdown (Financial Adjustment Status Code) | `sCODE_FINANCIAL_ADJUSTMENT_STATUS` | No | Functional=No; vendor help: "Select the status of the accounting assumption adjustment from the field." |
| **FK** | `AssetAssociatedProjectEntityID` | Asset Associated Entity | Entity | `sTYPE_MIXEDENTITY` | No | Functional=No; vendor help: "This is a reporting field that returns data about the asset associated with the entity." |
| **FK** | `AssetID` | Asset | Equipment ID | `sTYPE_ASSET` | Yes | vendor help: "The asset ID of the associated equipment asset." |
| **FK** | `ContractID` | Contract | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **FK** | `CovenantID` | Covenant | Covenant ID | `sTYPE_COVENANT` | No | Functional=No; vendor help: "Select the covenant that the record is associated with from this field." |
| **SYSTEM** | `BOMapClientRecordID` | Financial Adjustment ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `FinancialAdjustmentID` | Financial Adjustment RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |

### Covenant — ASC 842 / IFRS 16 fields only (`covenant`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `HoldAmountInSchedLiability` | Hold Amount in Rent Schedule Liability | Boolean | `sTYPE_CHECKBOX` | - | no vendor help text |
| **INPUT** | `CovenantAmount` | Covenant Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "If there is a financial amount associated with this covenant, enter the amount in this field. This amount will be pulled into your accounting assumpti" |
| **INPUT** | `CovenantDate` | Covenant Date | Date | `sTYPE_DATE` | No | Functional=No; vendor help: "Enter the effective date of the covenant in this field." |
| **INPUT** | `ExistsFlag` | Exists? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Select this check box to indicate that the covenant currently exists in the lease. A common use case for this check box is for customers who implement" |
| **INPUT** | `SecondaryRentSchedAllocPercent` | Covenant Secondary Rent Schedule Allocation Percent | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "If you will be allocating a percentage of a covenant expense to a secondary schedule, enter the allocation percentage in this field." |
| **INPUT** | `ThirdPartyRVGAmount` | Portion Guaranteed By 3rd Party | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "The total value of the residual value guarantee, positive or negative. This field only appears if a Covenant Type of Residual Value Guarantee is creat" |
| **INPUT** | `TotalRVGAmount` | Total Residual Value Guarantee | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "The residual value guarantee amount which is guaranteed by a third party, positive or negative. This field only appears if a Covenant Type of Residual" |
| **CODE-TABLE** | `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | `sCODE_ASC842_SCHEDULE` | Yes | vendor help: "The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeAccountingAdjustmentTypeID` | Accounting Adjustment Type | Dropdown (Accounting Adjustment Type Code) | `sCODE_ACCOUNTING_ADJUSTMENT_TYPE` | Yes | vendor help: "If this covenant is related to an accounting adjustment such as a purchase option, cancellation, or residual value guarantee select the appropriate ac" |
| **CODE-TABLE** | `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | `sCODE_CURRENCY_TYPE` | Yes | vendor help: "The Currency Type field allows you to select a currency type to be used on a record." |
| **CODE-TABLE** | `CodeIFRS16ScheduleID` | IFRS 16 Schedule | Dropdown (IFRS 16 Schedule Type) | `sCODE_IFRS16_SCHEDULE` | Yes | vendor help: "The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its va" |
| **FK** | `ContractID` | ContractID | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **SYSTEM** | `CovenantID` | Covenant RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |

### Asset — Financial Information group only (`asset`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `PortionOfAssetControlled` | Portion Of Asset Controlled | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "Enter the portion of the asset you control in this field." |
| **COMPUTED** | `RemainingAssetBalance` | Remaining Asset Balance | Percent or Currency | `sTYPE_PERCENT_OR_AMOUNT` | - | no vendor help text |
| **INPUT** | `AccountingBeginDate` | Accounting Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "If applicable, enter the accounting begin date override in this field. The purpose of this field is to change the dates that the test and rent schedul" |
| **INPUT** | `AccountingEndDate` | Accounting End Date | Date | `sTYPE_DATE` | Yes | vendor help: "If applicable, enter the accounting begin date override in this field. The purpose of this field is to change the dates that the test and rent schedul" |
| **INPUT** | `AssetSalePrice` | Asset Sale Price | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "Enter the sale price of the asset in this field." |
| **INPUT** | `CurrentAnnualPayment` | Current Annual Payment | Currency | `sTYPE_MONEY` | Yes | vendor help: "Calculates your current annual payment for the asset." |
| **INPUT** | `CurrentMonthlyPayment` | Current Monthly Payment | Currency | `sTYPE_MONEY` | Yes | vendor help: "Calculates your current monthly payment for the asset." |
| **INPUT** | `DepreciationEndDate` | Depreciation End Date | Date | `sTYPE_DATE` | No | Functional=No; vendor help: "Enter the depreciation end date in this field." |
| **INPUT** | `DiscountRateOverride` | Discount Rate Override | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "If this equipment uses a different discount rate, enter the discount rate in this field. The discount rate is also known as the Interest Rate or the I" |
| **INPUT** | `DispositionDate` | Disposition Date | Date | `sTYPE_DATE` | No | Functional=No; vendor help: "Enter the date the asset was sold in this field." |
| **INPUT** | `DoesTitleRevertToTenant` | Does Ownership Revert To Tenant? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Select this check box if the ownership of the asset reverts to the tenant at the termination of the lease term." |
| **INPUT** | `ExpectedLife` | Expected Life | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Enter any notes about the expected life in this field." |
| **INPUT** | `FairValueOfAsset` | Fair Value Of Asset | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the fair value of the asset into this field. FASB 842.10.20 defines fair value as the price that would be received to sell an asset or paid to t" |
| **INPUT** | `FairValueSource` | Fair Value Source | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter the name of the person who assessed the fair value of the asset in this field." |
| **INPUT** | `FirstYearBonusDepreciation` | First Year Bonus Depreciation | Percentage | `sTYPE_PERCENTAGE` | No | Functional=No; vendor help: "If the asset will depreciate at a different rate within the first year, enter a flag for indicating additional first year depreciation, or enter the f" |
| **INPUT** | `HasBuyoutOption` | Has Buyout Option? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "Select this check box if you have the option to buy the asset at the end of the lease term." |
| **INPUT** | `ImpairmentOverride` | Impairment Override Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any deductions related to the diminished value of the asset as a negative number." |
| **INPUT** | `InServiceDate` | In-Service Date | Date | `sTYPE_DATE` | No | Functional=No; vendor help: "Enter the date this asset was brought into service in this field." |
| **INPUT** | `InitialAssetBalanceAdjust` | Initial Asset Balance Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any adjustments to the initial asset balance in this field." |
| **INPUT** | `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter any adjustments to the initial liability balance in this field." |
| **INPUT** | `IsAssetTooSpecializedForLessor` | Is Asset Too Specialized For Lessor? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Select this check box if the asset has a specialized use, such that the lessor will have no alternative use for it." |
| **INPUT** | `IsLowAssetValue` | Is Low Asset Value | Boolean | `sTYPE_NULL_CHECKBOX` | No | Functional=No; vendor help: "Select this check box if the asset is low value." |
| **INPUT** | `IsShortTerm` | Is Short Term | Boolean | `sTYPE_NULL_CHECKBOX` | No | Functional=No; vendor help: "Select this check box if this asset is short-term." |
| **INPUT** | `LOAMonths` | LOA Months | Number | `sTYPE_NUMBER` | No | Functional=No; vendor help: "Enter the life of the asset in months in this field." |
| **INPUT** | `MonthToMonth` | Month To Month? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "If the equipment payment is going to be month-to-month, select this check box." |
| **INPUT** | `PaymentsBeginDate` | Payments Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "The payment begin date for the asset." |
| **INPUT** | `PaymentsEndDate` | Payments End Date | Date | `sTYPE_DATE` | Yes | vendor help: "The payment end date for the asset." |
| **INPUT** | `PlanToBuyAtEndOfTerm` | Plan To Buy At End Of Term? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "Select this check box if you plan to buy the asset at the end of the lease term." |
| **INPUT** | `PurchaseDate` | Purchase Date | Date | `sTYPE_DATE` | No | Functional=No; vendor help: "Enter the purchase date of the asset in this field." |
| **INPUT** | `PurchasePrice` | Purchase Price | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "Enter the purchase price in this field." |
| **INPUT** | `RemainingLife` | Remaining Life | Number | `sTYPE_NUMBER` | Yes | vendor help: "Enter the numerical value of the remaining economic life of the asset in this field." |
| **INPUT** | `Residual` | Residual | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "Enter the estimated value of the asset at the end of the lease." |
| **INPUT** | `StartingDepreciationCost` | Starting Depreciation Cost | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "If the asset will depreciate at a different rate within the first year, enter a flag for indicating additional first year depreciation, or enter the f" |
| **INPUT** | `YearsOfDepreciableLife` | Years Of Depreciable Life | Number | `sTYPE_NUMBER` | No | Functional=No; vendor help: "Enter the number of years the asset will be usable in this field." |
| **CODE-TABLE** | `CodeAccountingMethodOverrideID` | Accounting Method Override | Dropdown (Accounting Method Code) | `sCODE_ACCOUNTING_METHOD` | Yes | vendor help: "If you want to override the accounting method for your asset, select the accounting method you want to use from this field." |
| **CODE-TABLE** | `CodeAssetSuspensionStatusID` | Asset Suspension Status | Dropdown (Asset Suspension Status Code) | `sCODE_ASSET_SUSPENSION_STATUS` | No | Functional=No; vendor help: "Select the asset suspension status from this field." |
| **CODE-TABLE** | `CodeCompoundingFrequencyID` | Compounding Frequency | Dropdown (Frequency Code) | `sCODE_MONTH_FREQUENCY` | No | Functional=No; vendor help: "Select the compounding frequency from this field." |
| **CODE-TABLE** | `CodeRemainingLifeFreqUnitID` | Remaining Life Freq Unit | Dropdown (Frequency Unit Code) | `sCODE_FREQUENCY_UNIT` | Yes | vendor help: "Select the unit used to measure the remaining economic life of the asset from this field. Example units include days, weeks, months, and years." |
| **FK** | `FinancialContractID` | Financial Contract | Contract ID | `sTYPE_EQUIPMENT_CONTRACT` | Yes | vendor help: "Select the associated equipment contract from this field." |
| **SYSTEM** | `AssetID` | Asset RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |

### DiscountRate (`discount_rate`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **INPUT** | `CountryIDList` | Country List | Country, State, County ID | `sTYPE_COUNTRY_ONLY` | Yes | vendor help: "The countries this discount rate applies to, if there are multiple countries." |
| **INPUT** | `DiscountRate` | Discount Rate | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "Enter the discount rate in this field." |
| **INPUT** | `EffectiveThroughDate` | Effective End Date | Date | `sTYPE_DATE` | Yes | vendor help: "Enter the last date that the discount rate is effective in this field." |
| **INPUT** | `MaxSchedMons` | Maximum Schedule Length (months) | Number | `sTYPE_NUMBER` | Yes | vendor help: "Enter the maximum term length in months." |
| **INPUT** | `MinSchedMons` | Minimum Schedule Length (months) | Number | `sTYPE_NUMBER` | Yes | vendor help: "Enter the minimum term length in months." |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `StateProvinceIDList` | State Province | Country, State, County ID | `sTYPE_STATE_PROVINCE_LIST` | Yes | vendor help: "The states or provinces this discount rate applies to." |
| **CODE-TABLE** | `CodeAccountingMethodID` | Accounting Method | Dropdown (Accounting Method Code) | `sCODE_ACCOUNTING_METHOD` | Yes | vendor help: "Select the accounting method this discount rate should apply to. If you leave the field blank, the discount rate will apply to both Finance and Operat" |
| **CODE-TABLE** | `CodeContractUseID` | Contract Use | Dropdown (Contract Use Code) | `sCODE_CONTRACT_USE` | Yes | vendor help: "Select the use type of the lease from this field." |
| **FK** | `CountryID` | Country | Country, State, County ID | `sTYPE_COUNTRY_ONLY` | Yes | vendor help: "The country this discount rate applies to, if there is only one country." |
| **FK** | `ProgramID` | Program | Portfolio ID | `sTYPE_PROGRAM` | Yes | vendor help: "Select the portfolio this discount rate applies to." |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |

### CodeASC842Schedule / CodeIFRS16Schedule / CodeSLSchedule — structurally identical; one table shown (`code_a_s_c842_schedule`, `code_i_f_r_s16_schedule`, `code_s_l_schedule`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `ActualLongName` | Description | Text | `-` | - | no vendor help text |
| **COMPUTED** | `Inactive` | Inactive | Boolean | `-` | - | no vendor help text |
| **COMPUTED** | `ShortName` | Name | Text | `-` | - | no vendor help text |
| **INPUT** | `DontAmortizeAssetValue` | Don't Amortize Asset Value | Boolean | `sTYPE_BOOLEAN` | Yes | vendor help: "When selected, the system will not amortize the asset to zero in the lease accounting schedule. See the Amortization of the Asset in Contracts article" |
| **INPUT** | `ExportAcct10Number` | Export Account #10 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct11Number` | Export Account #11 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct12Number` | Export Account #12 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct13Number` | Export Account #13 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct14Number` | Export Account #14 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct15Number` | Export Account #15 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct16Number` | Export Account #16 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct17Number` | Export Account #17 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct18Number` | Export Account #18 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct19Number` | Export Account #19 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct1Number` | Export Account #1 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct20Number` | Export Account #20 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct2Number` | Export Account #2 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct3Number` | Export Account #3 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct4Number` | Export Account #4 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct5Number` | Export Account #5 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct6Number` | Export Account #6 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct7Number` | Export Account #7 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct8Number` | Export Account #8 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |
| **INPUT** | `ExportAcct9Number` | Export Account #9 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a export account number in this field. Export Accounts are tied to GL accounts in your Enterprise Resource Planning (ERP) System." |

### CodeExpenseType — schedule-routing and GL-account fields (`code_expense_type`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `ActualLongName` | Description | Text | `-` | - | no vendor help text |
| **COMPUTED** | `Inactive` | Inactive | Boolean | `-` | - | no vendor help text |
| **COMPUTED** | `ShortName` | Name | Text | `sTYPE_TEXT` | - | no vendor help text |
| **INPUT** | `APExportBaseNumber` | AP Export Base Number | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter the account number for your expenses." |
| **INPUT** | `APExportPrepaidNumber` | AP Export Prepaid Number | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter the account number for your prepaid expenses (if applicable)." |
| **INPUT** | `APExportTax1Number` | AP Export Tax #1 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter the account number for your accounts payable export taxes." |
| **INPUT** | `APExportTax2Number` | AP Export Tax #2 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter the account number for your accounts payable export taxes." |
| **INPUT** | `APExportTax3Number` | AP Export Tax #3 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter the account number for your accounts payable export taxes." |
| **INPUT** | `APExportTax4Number` | AP Export Tax #4 | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter the account number for your accounts payable export taxes." |
| **CODE-TABLE** | `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | `sCODE_ASC842_SCHEDULE` | Yes | vendor help: "The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | `sCODE_EXPENSE_CATEGORY` | Yes | vendor help: "This setting links this expense type to a particular expense category." |
| **CODE-TABLE** | `CodeIFRS16ScheduleID` | IFRS 16 Schedule | Dropdown (IFRS 16 Schedule Type) | `sCODE_IFRS16_SCHEDULE` | Yes | vendor help: "The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its va" |
| **CODE-TABLE** | `CodeSLScheduleID` | Straight-Line Schedule | Dropdown (Straight Line Schedule Type) | `sCODE_SL_SCHEDULE` | Yes | vendor help: "The Straight-Line Schedule field is where you select the Straight Line schedule you want to associate with a record." |
| **CODE-TABLE** | `ParentCodeExpenseGroupID` | Parent Group | Dropdown (Expense Group Code) | `sCODE_EXPENSE_GROUP` | Yes | vendor help: "Select the expense group that this expense type should be associated with. Groups are parents to types." |
| **CODE-TABLE** | `ParentID` | Expense Group Code | Dropdown (Expense Group Code) | `sCODE_EXPENSE_GROUP` | - | no vendor help text |
| **FK** | `CodeID` | Expense Type RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |

### AlternateRentSchedule (`alternate_rent_schedule`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **INPUT** | `BeginDate` | Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "The Begin Date field allows you to select a begin date for the record." |
| **INPUT** | `CapAmount` | Monthly Max Cap(Ceiling) | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the maximum, or ceiling cap for alternate rent in this field." |
| **INPUT** | `Description` | Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Write a description of the record." |
| **INPUT** | `EndDate` | End Date | Date | `sTYPE_DATE` | Yes | vendor help: "The End Date field allows you to select an end date for the record." |
| **INPUT** | `ExpenseReductionAmount` | Expense Reduction Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field reduces the amount of a generated transaction by a fixed amount. Enter the fixed amount in this field. This field does not appear until the" |
| **INPUT** | `ExpenseReductionPercent` | Expense Reduction Percent | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "This field reduces the amount of a generated transaction by a percentage amount. Enter the percentage amount in this field. This field does not appear" |
| **INPUT** | `FloorAmount` | Monthly Min Cap(Floor) | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the minimum, or floor cap for alternate rent in this field." |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `PRDeductExclusions` | Deduct Exclusions? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Select this check box if you would like to continue to deduct exclusions from your percentage rent." |
| **INPUT** | `PercentRentRate` | Percent Rent Rate | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "Enter the percent rent rate you would like to pay while your contract is in alternate rent and you are paying a percentage of gross sales in this fiel" |
| **INPUT** | `SetExpHoldFlag` | Set payments for Recurring Expenses on Hold | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This check box sets a Hold flag on all recurring expense transactions generated while the contract is in alternate rent." |
| **INPUT** | `SetPRHoldFlag` | Set payments for Percent Rent on Hold | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This check box sets a Hold flag on all percentage rent transactions generated while the contract is in alternate rent." |
| **CODE-TABLE** | `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | `sCODE_SALES_GROUP` | Yes | vendor help: "In alternate rent scenarios, different sales figures can apply. Select the appropriate sales group from the Sales Group field. Any percentage rent sch" |
| **DEAD** | `CodeAltRentMathID` | Alt Rent Math | Dropdown (Alt Rent Math Code) | `sCODE_ALT_RENT_MATH` | No | Functional=No; vendor help: "This field is for record keeping purposes only. It has no functional impact on the generated payment. Select how your alternate rent should be calcula" |
| **DEAD** | `SuspendSL` | Suspend SL? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This field is no longer used." |
| **FK** | `ContractID` | ContractID | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **FK** | `ExpenseSetupID` | Expense Setup | Expense Setup ID | `sTYPE_EXPENSE_SETUP` | Yes | vendor help: "The ExpenseSetupID field is used to associate an alternate rent record with an expense setup record." |
| **SYSTEM** | `AlternateRentScheduleID` | Alternate Rent Schedule RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `BOMapClientRecordID` | Alternate Rent Schedule ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |

### ExpenseAccrualSetup (`expense_accrual_setup`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `CurrentAnnualExpense` | Current Annual Expense | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "The sum of annual amounts for your current expense schedule records for a given expense setup record." |
| **COMPUTED** | `CurrentPeriodExpense` | Current Period Expense | Currency | `sTYPE_MONEY` | No | Functional=No; vendor help: "The sum of period amounts for your current expense schedule records for a given expense setup record." |
| **INPUT** | `AccrualMessage` | Accrual Message | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "If you'd like to add a message on your accrual, enter the message in this field." |
| **INPUT** | `BeginDate` | Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "The Begin Date field allows you to select a begin date for the record." |
| **INPUT** | `BeginPeriodName` | Begin Period / Year | Text | `sTYPE_TEXT` | Yes | vendor help: "Select the beginning period from this field." |
| **INPUT** | `Description` | Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Write a description of the record." |
| **INPUT** | `EndDate` | End Date | Date | `sTYPE_DATE` | Yes | vendor help: "The End Date field allows you to select an end date for the record." |
| **INPUT** | `EndPeriodName` | End Period / Year | Text | `sTYPE_TEXT` | Yes | vendor help: "Select the ending period from this field." |
| **INPUT** | `IsDailyRent` | Daily Rent | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Select this check box to indicate that this expense accrual is for daily rent." |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `RentableArea` | Rentable Area | Number | `sTYPE_AREA` | Yes | vendor help: "The Rentable Area field must be populated in order for the system to calculate your rate. The system will remember your rentable area and populate thi" |
| **INPUT** | `Section` | Section | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Enter the section of the covenant that pertains to this record in this field." |
| **CODE-TABLE** | `CodeAccrualTypeID` | Record Type | Dropdown (Accrual Type Code) | `sCODE_ACCRUAL_TYPE` | No | Functional=No; vendor help: "Select whether this is an accrual, a forecast, or a plan from this field." |
| **CODE-TABLE** | `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | `sCODE_BUILDING_AREA_UNIT` | Yes | vendor help: "Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your" |
| **CODE-TABLE** | `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | `sCODE_CURRENCY_TYPE` | Yes | vendor help: "The Currency Type field allows you to select a currency type to be used on a record." |
| **CODE-TABLE** | `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | `sCODE_EXPENSE_CATEGORY` | No | Functional=No; vendor help: "The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the g" |
| **CODE-TABLE** | `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | `sCODE_EXPENSE_GROUP` | No | Functional=No; vendor help: "The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types." |
| **CODE-TABLE** | `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | `sCODE_EXPENSE_TYPE` | Yes | vendor help: "The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease" |
| **DEAD** | `HoldFlag` | Hold? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This flag is informational-only. Select this check box to mark this expense accrual setup as being on hold." |
| **FK** | `AmendmentID` | Amendment | Contract Amendment ID | `sTYPE_CONTRACT_AMENDMENT` | No | Functional=No; vendor help: "Select the amendment that the record is associated with from this field." |
| **FK** | `ContractID` | ContractID | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **FK** | `CovenantID` | Covenant | Covenant ID | `sTYPE_COVENANT` | No | Functional=No; vendor help: "Select the covenant that the record is associated with from this field." |
| **FK** | `ExpenseSetupID` | Expense Setup | Expense Setup ID | `sTYPE_EXPENSE_SETUP` | Yes | vendor help: "The ExpenseSetupID field is used to associate an expense accrual setup record with an expense setup record." |
| **SYSTEM** | `BOMapClientRecordID` | Expense Accrual Setup ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `ExpenseAccrualSetupID` | Expense Accrual Setup RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |

### ExpenseAccrualSchedule (`expense_accrual_schedule`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `AnnualAmount` | Annual Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the annual amount of your accrual in this field. The system will automatically calculate the period amount, the accrual rate, the first period a" |
| **COMPUTED** | `BeginPeriodName` | Begin Period / Year | Date | `sTYPE_PERIOD_YEAR` | No | Functional=No; vendor help: "The name of the first fiscal period, for example 7/2019." |
| **COMPUTED** | `BeginYear` | Begin Year | Number | `sTYPE_DROPDOWN_YEAR` | Yes | vendor help: "Returns name of the last fiscal period for examle 7/2019" |
| **COMPUTED** | `EndPeriodName` | End Period / Year | Date | `sTYPE_PERIOD_YEAR` | No | Functional=No; vendor help: "The name of the last fiscal period, for example 7/2019." |
| **COMPUTED** | `EndYear` | End Year | Number | `sTYPE_DROPDOWN_YEAR` | Yes | vendor help: "Returns name of the last fiscal period for examle 7/2019" |
| **COMPUTED** | `FirstPaymentAmount` | First Payment Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The system will automatically calculate your first payment when you enter your annual amount in the Annual Amount field. You may modify the value in t" |
| **COMPUTED** | `LastPaymentAmount` | Last Payment Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "The system will automatically calculate your last payment when you enter your annual amount in the Annual Amount field. You may modify the value in th" |
| **COMPUTED** | `PeriodAmount` | Period Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the period amount of your accrual in this field. The system will automatically calculate the annual amount, the accrual rate, the first period a" |
| **INPUT** | `AccrualRate` | Accrual Rate | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field is where you enter your accrual rate. If you have entered your rentable area at the contract-level, the system will pre-populate the other" |
| **INPUT** | `BeginPeriod` | Begin Period | Number | `sTYPE_DROPDOWN_PERIOD` | Yes | vendor help: "Select the beginning period from this field." |
| **INPUT** | `DailyAccrualRate` | Daily Accrual Rate | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the daily rent expense accrual rate in this field." |
| **INPUT** | `Description` | Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Write a description of the record." |
| **INPUT** | `EndPeriod` | End Period | Number | `sTYPE_DROPDOWN_PERIOD` | Yes | vendor help: "Select the ending period from this field." |
| **INPUT** | `ForecastAdjustment` | Forecast Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "If you need to make a monetary adjustment to your forecast, enter the forecast adjustment in this field." |
| **INPUT** | `ForecastCapPercent` | Forecast Cap Percent | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "If you want to put a cap on your forecast, enter the cap percentage in this field." |
| **INPUT** | `ForecastGrowthPercent` | Forecast Growth Percent | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "If you want to put a cap on the growth of your forecast, enter the cap percentage in this field." |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `PlanAdjustment` | Plan Adjustment | Currency | `sTYPE_MONEY` | Yes | vendor help: "If you need to make a monetary adjustment to your plan, enter the plan adjustment in this field." |
| **INPUT** | `PlanCapPercent` | Plan Cap Percent | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "If you want to put a cap on your plan, enter the cap percentage in this field." |
| **INPUT** | `PlanForecastNotes` | Planning and Forecasting Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `PlanGrowthPercent` | Plan Growth Percent | Percentage | `sTYPE_PERCENTAGE` | Yes | vendor help: "If you want to put a cap on the growth of your plan, enter the cap percentage in this field." |
| **FK** | `ContractID` | Contract | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **FK** | `ExpenseAccrualSetupID` | Expense Accrual Setup | Text | `sTYPE_EXPENSE_ACCRUAL_SETUP` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `BOMapClientRecordID` | Expense Accrual Schedule ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `ExpenseAccrualScheduleID` | Expense Accrual Schedule RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |

### AccrualTransaction (`accrual_transaction`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `APExportBaseNumber` | AP Export Base Number | Text | `sTYPE_TEXT` | Yes | vendor help: "The account number for your expenses. The account number is configured at the expense type level." |
| **COMPUTED** | `APExportPrepaidNumber` | AP Export Prepaid Number | Text | `sTYPE_TEXT` | Yes | vendor help: "The account number for your prepaid expenses (if applicable). The account number is configured at the expense type level." |
| **COMPUTED** | `AccountNumber1` | Account Number #1 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number associated with the organization. You can edit these account numbers at the organization-level." |
| **COMPUTED** | `AccountNumber2` | Account Number #2 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number associated with the organization. You can edit these account numbers at the organization-level." |
| **COMPUTED** | `AccountNumber3` | Account Number #3 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number associated with the organization. You can edit these account numbers at the organization-level." |
| **COMPUTED** | `AccountNumber4` | Account Number #4 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number associated with the organization. You can edit these account numbers at the organization-level." |
| **COMPUTED** | `AccountNumber5` | Account Number #5 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number associated with the organization. You can edit these account numbers at the organization-level." |
| **COMPUTED** | `AccountNumber6` | Account Number #6 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number associated with the organization. You can edit these account numbers at the organization-level." |
| **COMPUTED** | `AccountNumber7` | Account Number #7 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number associated with the organization. You can edit these account numbers at the organization-level." |
| **COMPUTED** | `AccountNumber8` | Account Number #8 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number associated with the organization. You can edit these account numbers at the organization-level." |
| **COMPUTED** | `ExpAccrualAcct1Number` | Exp Accrual Acct #1 Number | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your expense accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `ExpAccrualAcct2Number` | Exp Accrual Acct #2 Number | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your expense accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `ExpAccrualAcct3Number` | Exp Accrual Acct #3 Number | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your expense accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `ExpAccrualAcct4Number` | Exp Accrual Acct #4 Number | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your expense accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `PercentRentAccrualAcct1Number` | Percent Rent Accrual Acct #1 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your percent rent accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `PercentRentAccrualAcct2Number` | Percent Rent Accrual Acct #2 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your percent rent accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `PercentRentAccrualAcct3Number` | Percent Rent Accrual Acct #3 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your percent rent accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `PercentRentAccrualAcct4Number` | Percent Rent Accrual Acct #4 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your percent rent accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `PeriodAmount` | Period Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the amount that is being accrued for the period in this field. This field will be disabled if you select the Include Taxes in Total Amount? Flag" |
| **COMPUTED** | `RETaxAccrualAcct1Number` | RE Tax Accrual Acct #1 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `RETaxAccrualAcct2Number` | RE Tax Accrual Acct #2 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `RETaxAccrualAcct3Number` | RE Tax Accrual Acct #3 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level." |
| **COMPUTED** | `RETaxAccrualAcct4Number` | RE Tax Accrual Acct #4 | Text | `sTYPE_TEXT` | Yes | vendor help: "This field contains an account number for your real estate tax accruals. The account number is configured at the expense type level." |
| **INPUT** | `AccrualMessage` | Accrual Message | Text | `sTYPE_TEXT` | Yes | vendor help: "Enter a message for the memo line in this field." |
| **INPUT** | `Description` | Description | Text | `sTYPE_TEXT` | No | Functional=No; vendor help: "Write a description of the record." |
| **INPUT** | `Notes` | Notes | Text | `sTYPE_TEXTAREA` | No | Functional=No; vendor help: "Add any notes about the record." |
| **INPUT** | `PeriodBeginDate` | Period Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "Enter or use the calendar picker to select the begin date of the transaction period." |
| **INPUT** | `PeriodEndDate` | Period End Date | Date | `sTYPE_DATE` | Yes | vendor help: "Enter or use the calendar picker to select the end date of the transaction period." |
| **INPUT** | `PeriodNumber` | Period Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "Enter the period number as a two-digit number in this field." |
| **INPUT** | `PeriodYear` | Period Year | Number | `sTYPE_DROPDOWN_YEAR` | Yes | vendor help: "Select the year of the transaction period from this field." |
| **INPUT** | `PostingDate` | Posting Date | Date | `sTYPE_DATE` | Yes | vendor help: "Enter or use the calendar picker to select the posting date of the transaction." |
| **INPUT** | `ProcessedFlag` | Processed? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Select this check box once you have processed your accrual transaction. Warning - once you mark a transaction as processed, you cannot change it." |
| **INPUT** | `SourceEntityTable` | Source Entity Table | Text | `sTYPE_TEXT` | Yes | vendor help: "The batch ID for your accrual payment transaction." |
| **INPUT** | `TaxAmount1` | Tax Amount #1 | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the primary tax amount in currency in this field." |
| **INPUT** | `TaxAmount2` | Tax Amount #2 | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the secondary tax amount in currency in this field." |
| **INPUT** | `TaxAmount3` | Tax Amount #3 | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the third tax amount in currency in this field." |
| **INPUT** | `TaxAmount4` | Tax Amount #4 | Currency | `sTYPE_MONEY` | Yes | vendor help: "Enter the fourth tax amount in currency in this field." |
| **INPUT** | `TaxesIncludedFlag` | Taxes Included In Amount? | Boolean | `sTYPE_CHECKBOX` | Yes | vendor help: "Select this check box if taxes are included in the value you entered in the Period Amount field. The system will then subtract the tax amounts from th" |
| **INPUT** | `TotalAmount` | Total Amount | Currency | `sTYPE_MONEY` | Yes | vendor help: "This field will only be editable if the Taxes Included in Amount? flag is selected. The total amount is the period amount plus any taxes." |
| **CODE-TABLE** | `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | `sCODE_CURRENCY_TYPE` | Yes | vendor help: "The Currency Type field allows you to select a currency type to be used on a record." |
| **CODE-TABLE** | `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | `sCODE_EXPENSE_CATEGORY` | No | Functional=No; vendor help: "The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the g" |
| **CODE-TABLE** | `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | `sCODE_EXPENSE_GROUP` | No | Functional=No; vendor help: "The Expense Group field allows you to associate your record with a pre-configured expense group. Expense groups are used to categorize expense types." |
| **CODE-TABLE** | `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | `sCODE_EXPENSE_TYPE` | Yes | vendor help: "The Expense Type field allows you to associate your record with a pre-configured expense type. Expense Types are used to associate records with lease" |
| **DEAD** | `HoldFlag` | Hold? | Boolean | `sTYPE_CHECKBOX` | No | Functional=No; vendor help: "This flag is informational-only. Select this check box to mark this accrual transaction as being on hold." |
| **FK** | `ContractID` | ContractID | Contract ID | `sTYPE_CONTRACT` | Yes | vendor help: "The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Sum" |
| **FK** | `ExpenseAccrualSetupID` | Expense Accrual Setup | Text | `sTYPE_EXPENSE_ACCRUAL_SETUP` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **FK** | `OrganizationID` | Organization | Organization ID | `sTYPE_ORGANIZATION` | Yes | vendor help: "Select the organization from which this payment should be debited from this field." |
| **SYSTEM** | `AccrualTransactionID` | Accrual Transaction RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `BOMapClientRecordID` | Accrual Transaction ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Created By field is a system-populated field which captures the name of the member making changes to a record." |
| **SYSTEM** | `CreatedDate` | Created Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Created Date field is a system-populated field which captures the date that a record was created." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |
| **SYSTEM** | `RevNumber` | Rev Number | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified." |

### FiscalPeriod (`fiscal_period`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `NumberDaysInPeriod` | Days In Period | Number | `sTYPE_NUMBER` | Yes | vendor help: "Calculates how many days are in the period." |
| **COMPUTED** | `NumberWeeksInPeriod` | Weeks In Period | Number | `sTYPE_NUMBER` | Yes | vendor help: "Calculates how many weeks are in the period." |
| **INPUT** | `BeginDate` | Begin Date | Date | `sTYPE_DATE` | Yes | vendor help: "The Begin Date field allows you to select a begin date for the record." |
| **INPUT** | `EndDate` | End Date | Date | `sTYPE_DATE` | Yes | vendor help: "The End Date field allows you to select an end date for the record." |
| **INPUT** | `Is4or5WeekPeriod` | Is 4 or 5 Week Period? | Boolean | `sTYPE_BOOLEAN` | Yes | vendor help: "This field determines how many weeks are in the fiscal period. It has two potential values: 4 weeks or 5 weeks." |
| **INPUT** | `MatchingCalendarMonth` | Matching Calendar Month | Dropdown | `sTYPE_MONTH` | Yes | vendor help: "The calendar month that this fiscal period overlaps with." |
| **INPUT** | `MatchingCalendarYear` | Matching Calendar Year | Number | `sTYPE_NUMBER` | Yes | vendor help: "The calendar year that this fiscal period overlaps with." |
| **INPUT** | `Period` | Period | Number | `sTYPE_NUMBER` | Yes | vendor help: "The period number." |
| **INPUT** | `Quarter` | Quarter | Number | `sTYPE_NUMBER` | Yes | vendor help: "The quarter number." |
| **INPUT** | `Year` | Year | Number | `sTYPE_NUMBER` | Yes | vendor help: "The fiscal year." |
| **DEAD** | `FiscalPeriodName` | Fiscal Period Name | Text | `sTYPE_TEXT` | Yes | vendor help: "This field is not implemented." |
| **FK** | `ProgramID` | Portfolio | Portfolio ID | `sTYPE_PROGRAM` | Yes | vendor help: "Select the Portfolio that the record belongs to from this field." |
| **SYSTEM** | `BOMapClientRecordID` | Fiscal Period ClientID | Text | `sTYPE_TEXT` | Yes | vendor help: "The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can" |
| **SYSTEM** | `FiscalPeriodID` | Fiscal Period RecID | Number | `sTYPE_UNFORMATTED_NUMBER` | Yes | vendor help: "This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable." |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | Yes | vendor help: "The Modified By field is a system-populated field which captures the name of the member who made a change to a record." |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | Yes | vendor help: "The Modified Date field is a system-populated field which captures the date that a modification is made to a record." |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |

### RecalcOverrideNotes (`recalc_override_notes`)

| Class | Field | Label | Lucernex type | Data-Fields type | Fn | Evidence |
|---|---|---|---|---|---|---|
| **COMPUTED** | `Notes` | Override Note | Text | `sTYPE_TEXTAREA` | - | no vendor help text |
| **FK** | `SLSummaryID` | Straight Line Summary | Straight-Line Schedule ID | `sTYPE_SL_SUMMARY` | - | no vendor help text |
| **SYSTEM** | `CreatedByID` | Created By | Member ID | `sTYPE_MEMBER` | - | no vendor help text |
| **SYSTEM** | `CreatedDate` | Date of entry | Time | `sTYPE_TIME` | - | no vendor help text |
| **SYSTEM** | `ModifiedByID` | Modified By | Member ID | `sTYPE_MEMBER` | - | no vendor help text |
| **SYSTEM** | `ModifiedDate` | Modified Date | Time | `sTYPE_TIME` | - | no vendor help text |
| **SYSTEM** | `ProjectEntityID` | ProjectEntityID | Entity ID | `-` | - | no vendor help text |

## Open questions

1. **(new) Does the GraphQL schema expose the canonical `FieldType` per field?** If so, one
   introspection query verifies all 666 rows against the vendor's own classification. Highest-value
   follow-up for this file by a wide margin.
2. **Are the 25 undocumented roll-forward fields on `SLSummary` genuinely computed, or are any of
   them manual overrides?** They are the largest block classified COMPUTED on **Derived** evidence
   alone. Open a contract's Roll Forward Report and check whether any cell is editable.
3. **Which of the twenty `ExportAcctNNumber` slots corresponds to which GL concept?** Open a
   configured ASC 842 Schedule Type record in `Admin > Manage Firm Drop Downs` and read the labels.
4. **Is `sTYPE_PERCENT_OR_AMOUNT` stored with a companion unit flag anywhere?** The vendor text
   describes an option button in the UI; if that selection is persisted, the column holding it is not
   in the object dump. This determines whether the migration is safe or lossy.
5. **What delimiter do the `*IDList` / `AssociatedExpenseSetupIDs` text columns use?**
6. **Do `ExpenseAccrualSetup.HoldFlag` / `AccrualTransaction.HoldFlag` really have no effect?** Both
   are documented as informational-only, but `HoldFlag` on `ExpenseSchedule` and `PaymentTransaction`
   is set programmatically by `AlternateRentSchedule.SetExpHoldFlag` / `.SetPRHoldFlag`, which implies
   *some* hold flag is functional.
7. **Is `ContractFinancialTest.YearBuilt` really non-functional?** It is `Fn = No` on
   `ContractFinancialTest` but is documented as a Test 3 input on `Contract`.
