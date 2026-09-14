# SLSummary

*134 fields · module: Lease Accounting & Payments · Postgres: `s_l_summary`*

Straight-line rent summary — one record per contract holding forward-looking cash and interest expense projected out fiscal-year by fiscal-year (Current, Beyond Fifth, Beyond Sixth) and quarter by quarter within the current year, used for ASC 842/IFRS 16 disclosure schedules. All 135 fields are Global MONEY values; this is a reporting rollup table, not a transactional one, which is why there are no Boolean flags or codes — every field is a pre-calculated dollar amount for a specific future period.

Source: `data-fields/sl-summary.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 134 |
| Catalogued fields | 135 (135 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 8 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 22 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-002](../rules/ACC-R-002.md) | if `Contract.DiscountRate` is populated it is the rate used; otherwise `ComputedSLDiscountRate` | Inferred |
| [ACC-R-019](../rules/ACC-R-019.md) | the covenant amount is pulled into the accounting assumptions and the accounting schedule only if `CodeAccountingAdjustmentTypeID` ∈ {`Purchase Option`, `Cancellation Option`, `Residual Value Guarantee`} | Observed |
| [ACC-R-020](../rules/ACC-R-020.md) | `SLSummary.NeedsRecalculation := true` | Observed |
| [ACC-R-021](../rules/ACC-R-021.md) | the accounting schedule associated with that expense type is dirtied | Observed |
| [ACC-R-022](../rules/ACC-R-022.md) | the schedule must be remeasured | Observed |
| [ACC-R-024](../rules/ACC-R-024.md) | a `RecalcOverrideNotes` row linked by `SLSummaryID`; the id appended to `SLSummary.RecalcOverrideNotesIDList` | Derived |
| [ACC-R-025](../rules/ACC-R-025.md) | each period cash flow is routed to the schedule type its expense type designates for the standard being generated | Derived |
| [ACC-R-027](../rules/ACC-R-027.md) | `SLSummary.IsSLSchedule` / `.IsASC842Schedule` / `.IsIFRS16Schedule := true` respectively | Derived |
| [ACC-R-028](../rules/ACC-R-028.md) | one `SLPeriod` per fiscal period, carrying `BeginDate`, `EndDate`, `NumberDays`, `FiscalPeriod`, `FiscalPeriodYear`, `CumulativePeriodNumber` | Derived |
| [ACC-R-031](../rules/ACC-R-031.md) | `InitialLiabilityBalance = Σ PVOfPeriodCashAmount` | Observed |
| [ACC-R-033](../rules/ACC-R-033.md) | not documented. The vendor says only "This is a calculated value which contains the initial value over the asset of the lease." | Inferred |
| [ACC-R-035](../rules/ACC-R-035.md) | `TotalCommitment = Σ` all rent payments for the life of the lease | Observed |
| [ACC-R-041](../rules/ACC-R-041.md) | ``` Forward12MonthAssetChange[n] = Σ asset amortization, periods n+1 … n+12 Forward12MonthLiabilityChange[n] = Σ liability amortization, periods n+1 … n+12 ShortTermRentExpense[n] = Σ rent expense, next 12 months LongTermRentExpense[n] = Σ  | Observed |
| [ACC-R-045](../rules/ACC-R-045.md) | ``` new.PriorLastPostedPeriodID := old.SLSummaryID new.PostedEndDate := old.LastPostedEndDate new.PostedInitAssetAdj := new.InitialAssetBalance − old.AssetBalance(as of PostedEndDate) new.PostedInitLiabilityAdj := new.InitialLiabilityBalanc | Observed |
| [ACC-R-048](../rules/ACC-R-048.md) | `TotalImpairmentImpact = ImpairmentAmount + PriorAccumulatedAmortizationBalance`, where `PriorAccumulatedAmortizationBalance` is "the Accumulated Amortization Balance of the accounting period prior to the impairment." | Observed |
| [ACC-R-049](../rules/ACC-R-049.md) | these four fields are "only made available on Finance contracts". `FinalAssetDate` defaults to the schedule end date; a later date amortizes beyond the schedule end | Observed |
| [ACC-R-051](../rules/ACC-R-051.md) | `SLSummary.LastPostedDate` = begin date of the last posted period; `LastPostedEndDate` = its end date; `LastBalancePosted` = "the asset minus the liability as of the last posted period"; `LastPostedBalanceSheetImpact` = "the portion of the  | Observed |
| [ACC-R-058](../rules/ACC-R-058.md) | "This field determines if the program allows for matching of fiscal/calendar year rent." | Observed |
| [ACC-R-060](../rules/ACC-R-060.md) | on completion of step 3, `SLSummary.IsApproved := true` (`ACC-R-050`) | Observed |
| [CON-R-026](../rules/CON-R-026.md) | Any rollup is read: the rollups are denormalised and can be stale — Contract carries no recalculation flag equivalent to SLSummary's. | Derived |
| [CON-R-130](../rules/CON-R-130.md) | Disclosure scope: SLSummary.IsIncludeInRollForwardReport controls inclusion in the roll-forward disclosure. | Observed |
| [AST-R-006](../rules/AST-R-006.md) | Input: `Asset.RemainingAssetBalance`, field type `sTYPE_PERCENT_OR_AMOUNT`. Effect: A value 0–100 is read as a percentage; | Observed |

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetID` | Equipment | Equipment ID | Global |  | [Asset](Asset.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `NeedsRecalcModifiedByLastMember` | Needs Recalc Modified by Last Member | Member ID | Global |  | [Member](Member.md) |
| `NeedsRecalcModifiedByMemberIDList` | Needs Recalc Modified by Member List | Member ID | Global |  | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `RecalcOverrideNotesIDList` | Recalc Override Notes | Recalc Override Notes ID | Global |  | [RecalcOverrideNotes](RecalcOverrideNotes.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | Entity | Global |  |  |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | Dropdown (ASC 842 Schedule Type) | Global |  | ASC 842 Schedule Type |
| `CodeAccountingMethodID` | Accounting Method | Dropdown (Accounting Method Code) | Global |  | Accounting Method Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule | Dropdown (IFRS 16 Schedule Type) | Global |  | IFRS 16 Schedule Type |
| `CodeSLScheduleID` | Straight Line Schedule | Dropdown (Straight Line Schedule Type) | Global |  | Straight Line Schedule Type |
| `CodeScheduleCreationReasonID` | Schedule Creation Reason | Dropdown (Schedule Creation Reason Code) | Global |  | Schedule Creation Reason Code |

### Money (91)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccumulatedAmortizationBalancePriorToImpairment` | Accumulated Amortization Balance Prior to Impairment | Currency | Global |  |  |
| `AssetAmortExpenseAdjustment` | Asset Amortization Expense Adjustment | Currency | Global |  |  |
| `AssetAmortizationExpense` | Asset Amortization Expense | Currency | Global |  |  |
| `BalanceForward` | Balance Forward | Currency | Global |  |  |
| `BeyondCurrentFiscalYearCashExpense` | Current Fiscal Year and Beyond Cash Expense | Currency | Global |  |  |
| `BeyondCurrentFiscalYearInterestExpense` | Current Fiscal Year and Beyond Interest Expense | Currency | Global |  |  |
| `BeyondFifthFiscalYearCashExpense` | Beyond Fifth Fiscal Year Cash Expense | Currency | Global |  |  |
| `BeyondSixthFiscalYearCashExpense` | Beyond Sixth Fiscal Year Cash Expense | Currency | Global |  |  |
| `CalcAggValueOfLeaseNoAdjust` | Aggregate Value Of Lease Before Adjustments | Currency | Global |  |  |
| `CalcAggregateValueOfLease` | Aggregate Value Of Lease | Currency | Global |  |  |
| `CalcPVOfFinancialTerms` | PV Of Financial Terms | Currency | Global |  |  |
| `CalcPVOfFinancialTermsNoAdjust` | PV Of Financial Terms Before Adjustments | Currency | Global |  |  |
| `CancellationOptionAmount` | Cancellation Option Amount | Currency | Global |  |  |
| `CashExpenseAdjustment` | Cash Expense Adjustment | Currency | Global |  |  |
| `CurrentAssetBalance` | Current Period Asset Balance | Currency | Global |  |  |
| `CurrentFiscalYearCashExpense` | Current Fiscal Year Cash Expense | Currency | Global |  |  |
| `CurrentFiscalYearQ1CashExpense` | Current Fiscal Year Q1 Cash Expense | Currency | Global |  |  |
| `CurrentFiscalYearQ2CashExpense` | Current Fiscal Year Q2 Cash Expense | Currency | Global |  |  |
| `CurrentFiscalYearQ3CashExpense` | Current Fiscal Year Q3 Cash Expense | Currency | Global |  |  |
| `CurrentFiscalYearQ4CashExpense` | Current Fiscal Year Q4 Cash Expense | Currency | Global |  |  |
| `CurrentLiabilityBalance` | Current Period Liability Balance | Currency | Global |  |  |
| `CurrentRemainingCashBalance` | Current Remaining Balance Lease Payments | Currency | Global |  |  |
| `CurrentRemainingCashBalanceAfterReportEnd` | Current Remaining Cash Balance After Report End | Currency | Global |  |  |
| `DismantlingStorageCostAmount` | Dismantling / Restoring Cost Amount | Currency | Global |  |  |
| `EndingAccumulatedAmortizationBalance` | Ending Accumulated Amortization Balance | Currency | Global |  |  |
| `EndingGrossAssetBalance` | Ending Gross Asset Balance | Currency | Global |  |  |
| `EndingLeaseLiabilityBalance` | Ending Lease Liability Balance | Currency | Global |  |  |
| `FifthFiscalYearCashExpense` | Fifth Fiscal Year Cash Expense | Currency | Global |  |  |
| `FinalAssetAmount` | Final Asset Amount | Currency | Global |  |  |
| `Forward12MonthAssetChange` | 12-Month Forward Change in Asset Balance | Currency | Global |  |  |
| `Forward12MonthLiabilityChange` | 12-Month Forward Change in Liability Balance | Currency | Global |  |  |
| `FourthFiscalYearCashExpense` | Fourth Fiscal Year Cash Expense | Currency | Global |  |  |
| `ImpairmentAmount` | Impairment Amount | Currency | Global |  |  |
| `ImpairmentsAndAccumulatedAmortizationReset` | Impairments and Accumulated Amortization Reset | Currency | Global |  |  |
| `InitialAssetBalance` | Initial Asset Balance | Currency | Global |  |  |
| `InitialAssetBalanceAdjust` | Initial Asset Balance Adjustment | Currency | Global |  |  |
| `InitialDirectCostAmount` | Initial Direct Cost Amount | Currency | Global |  |  |
| `InitialLiabilityBalance` | Initial Liability Balance | Currency | Global |  |  |
| `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | Currency | Global |  |  |
| `InterestBeforeMidRemeasure` | Interest Before Mid-period Remeasurement | Currency | Global |  |  |
| `InterestExpense` | Interest Expense | Currency | Global |  |  |
| `InterestExpenseAdjustment` | Interest Expense Adjustment | Currency | Global |  |  |
| `LastBalancePosted` | Last Balance Posted | Currency | Global |  |  |
| `LastPostedBalanceSheetImpact` | Last Posted Balance Sheet Impact | Currency | Global |  |  |
| `LeaseExpirationAccumulatedAmortizationImpact` | Lease Expiration Accumulated Amortization Impact | Currency | Global |  |  |
| `LeaseExpirationGrossAssetBalance` | Lease Expiration Gross Asset Balance | Currency | Global |  |  |
| `LeaseIncentiveAmount` | Lease Incentive Amount | Currency | Global |  |  |
| `LeaseLiabilityPaymentImpact` | Lease Liability Payment Impact | Currency | Global |  |  |
| `LeaseRemeasurementAccumulatedAmortizationImpact` | Lease Remeasurement Accumulated Amortization Impact | Currency | Global |  |  |
| `LeaseRemeasurementLeaseLiabilityImpact` | Lease Remeasurement Lease Liability Impact | Currency | Global |  |  |
| `NewGrossAssetBalances` | New Gross Asset Balances | Currency | Global |  |  |
| `NewLeaseLiabilities` | New Lease Liabilities | Currency | Global |  |  |
| `NextFiscalYearCashExpense` | Next Fiscal Year Cash Expense | Currency | Global |  |  |
| `PVOfCancellationOption` | PV Of Cancellation Option | Currency | Global |  |  |
| `PVOfOtherAdjustments` | PV Of Other Adjustments | Currency | Global |  |  |
| `PVOfPurchaseOption` | PV Of Purchase Option | Currency | Global |  |  |
| `PVOfResidualValueGuarantees` | PV Of Residual Value Guarantees | Currency | Global |  |  |
| `PVOfStructuringCosts` | PV Of Structuring Costs | Currency | Global |  |  |
| `PeriodAmount` | Period Amount | Currency | Global |  |  |
| `PostedAssetAdjustment` | Posted Total Asset Adjustment at Mod Input Date | Currency | Global |  |  |
| `PostedInitAssetAdj` | Posted Initial Asset Adjustment for Mod Effective Date | Currency | Global |  |  |
| `PostedInitLiabilityAdj` | Posted Initial Liability Adjustment for Mod Effective Date | Currency | Global |  |  |
| `PostedLiabilityAdjustment` | Posted Total Liability Adjustment at Mod Input Date | Currency | Global |  |  |
| `PreCommencePayAmount` | Pre Commence Pay Amount | Currency | Global |  |  |
| `PriorAccumulatedAmortizationBalance` | Prior Accumulated Amortization Balance | Currency | Global |  |  |
| `PriorPeriodAccumulatedAmortizationBalance` | Prior Period Accumulated Amortization Balance | Currency | Global |  |  |
| `PriorPeriodGrossAssetBalance` | Prior Period Gross Asset Balance | Currency | Global |  |  |
| `PriorPeriodLeaseLiability` | Prior Period Lease Liability | Currency | Global |  |  |
| `ProfitAndLossImpact` | Profit And Loss Impact | Currency | Global |  |  |
| `PurchaseOptionAmount` | Purchase Option Amount | Currency | Global |  |  |
| `ReclassAccumulatedAmortizationImpact` | Reclass Accumulated Amortization Impact | Currency | Global |  |  |
| `ReclassGrossAssetBalanceImpact` | Reclass Gross Asset Balance Impact | Currency | Global |  |  |
| `ReclassLeaseLiabilityImpact` | Reclass Lease Liability Impact | Currency | Global |  |  |
| `ReclassificationAccumulatedAmortizationImpact` | Reclassification Accumulated Amortization Impact | Currency | Global |  |  |
| `ReclassificationLeaseLiabilityImpact` | Reclassification Lease Liability Impact | Currency | Global |  |  |
| `ReclassificationOfGrossAssetBalance` | Reclassification of Gross Asset Balance | Currency | Global |  |  |
| `RemeasurementBalanceForward` | Balance Sheet Impact | Currency | Global |  |  |
| `RemeasurementGrossAssetBalanceImpact` | Remeasurement Gross Asset Balance Impact | Currency | Global |  |  |
| `ResidualValueGuarantees` | Residual Value Guarantees | Currency | Global |  |  |
| `ShortenedLeaseLiabilityDiff` | Shortened Lease Liability Diff | Currency | Global |  |  |
| `ShortenedSchedInitLiabilityBal` | Shortened Schedule Initial Liability Balance | Currency | Global |  |  |
| `ShortenedTermAssetDiff` | Shortened Term Asset Diff | Currency | Global |  |  |
| `ShortenedTermRentDiff` | Shortened Term Rent Diff | Currency | Global |  |  |
| `SingleLeaseExpenseAdjustment` | Single Lease Expense Adjustment | Currency | Global |  |  |
| `SixthFiscalYearCashExpense` | Sixth Fiscal Year Cash Expense | Currency | Global |  |  |
| `SleBeforeMidRemeasure` | Straight Line Expense Before Mid-period Remeasurement | Currency | Global |  |  |
| `ThirdFiscalYearCashExpense` | Third Fiscal Year Cash Expense | Currency | Global |  |  |
| `TotalCommitment` | Total Commitment | Currency | Global |  |  |
| `TotalImpairmentImpact` | Total Impairment Impact | Currency | Global |  |  |
| `TranslatedInitialAssetBalance` | Translated Initial Asset Balance | Currency | Global |  |  |
| `TranslatedInitialLiabilityBalance` | Translated Initial Liability Balance | Currency | Global |  |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DiscountRate` | Discount Rate | Percentage | Global |  |  |
| `FinalAssetAllocPercent` | Final Asset Amount Allocation Percentage | Percentage | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PriorLastPostedPeriodID` | Prior Schedule Last Posted Period | Number | Global |  |  |
| `SLSummaryID` | Straight Line Summary RecID | Number | Global |  |  |
| `SLTermLength` | Straight Line Term Length | 2-Digit Number | Global |  |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `FinalAssetDate` | Final Asset Amount Date | Date | Global |  |  |
| `InactiveDate` | Inactive Date | Date | Global |  |  |
| `LastPostedDate` | Last Posted Date | Date | Global |  |  |
| `LastPostedEndDate` | Last Posted End Date | Date | Global |  |  |
| `PostedEndDate` | Posted End Date | Date | Global |  |  |
| `RecalcTriggerDate` | Recalculation Trigger Date | Date | Global |  |  |

### Flags (7)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |
| `IsASC842Schedule` | Is ASC 842 Schedule? | Boolean | Global |  |  |
| `IsApproved` | Is Approved? | Boolean | Global |  |  |
| `IsIFRS16Schedule` | Is IFRS 16 Schedule? | Boolean | Global |  |  |
| `IsIncludeInRollForwardReport` | Is Include in Roll Forward Report? | Boolean | Global |  |  |
| `IsSLSchedule` | Is SL Schedule? | Boolean | Global |  |  |
| `NeedsRecalculation` | Needs Recalculation | Boolean | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssociatedExpenseSetupIDs` | Associated Expense Setup IDs | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Straight Line Summary ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

### Other (2)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DateRange` | Date Range | Date Range | Global |  |  |
| `SLRemainingAssetBalance` | Remaining Asset Balance | Percent or Currency | Global |  |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [RecalcOverrideNotes](RecalcOverrideNotes.md) | `SLSummaryID` |
| [SLPeriod](SLPeriod.md) | `SLSummaryID` |
