# SLSummary — Data Fields

Straight-line rent summary — one record per contract holding forward-looking cash and interest expense projected out fiscal-year by fiscal-year (Current, Beyond Fifth, Beyond Sixth) and quarter by quarter within the current year, used for ASC 842/IFRS 16 disclosure schedules. All 135 fields are Global `MONEY` values; this is a reporting rollup table, not a transactional one, which is why there are no Boolean flags or codes — every field is a pre-calculated dollar amount for a specific future period.

**Table Association:** `SLSummary` &nbsp;·&nbsp; **Total fields:** 135 (Global: 135, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Beyond Fifth Fiscal Year Cash Expense | `BeyondFifthFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Beyond Sixth Fiscal Year Cash Expense | `BeyondSixthFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Current Fiscal Year Cash Expense | `CurrentFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Current Fiscal Year Q1 Cash Expense | `CurrentFiscalYearQ1CashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Current Fiscal Year Q2 Cash Expense | `CurrentFiscalYearQ2CashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Current Fiscal Year Q3 Cash Expense | `CurrentFiscalYearQ3CashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Current Fiscal Year Q4 Cash Expense | `CurrentFiscalYearQ4CashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Current Fiscal Year and Beyond Cash Expense | `BeyondCurrentFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Current Fiscal Year and Beyond Interest Expense | `BeyondCurrentFiscalYearInterestExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Fifth Fiscal Year Cash Expense | `FifthFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Fourth Fiscal Year Cash Expense | `FourthFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Next Fiscal Year Cash Expense | `NextFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Sixth Fiscal Year Cash Expense | `SixthFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Third Fiscal Year Cash Expense | `ThirdFiscalYearCashExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Financial - Rent Schedule |
| Accumulated Amortization Balance Prior to Impairment | `AccumulatedAmortizationBalancePriorToImpairment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Asset Amortization Expense | `AssetAmortizationExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Ending Accumulated Amortization Balance | `EndingAccumulatedAmortizationBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Ending Gross Asset Balance | `EndingGrossAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Ending Lease Liability Balance | `EndingLeaseLiabilityBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Impairments and Accumulated Amortization Reset | `ImpairmentsAndAccumulatedAmortizationReset` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Interest Expense | `InterestExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Is Include in Roll Forward Report? | `IsIncludeInRollForwardReport` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Roll Forward Report |
| Lease Expiration Accumulated Amortization Impact | `LeaseExpirationAccumulatedAmortizationImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Lease Expiration Gross Asset Balance | `LeaseExpirationGrossAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Lease Liability Payment Impact | `LeaseLiabilityPaymentImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Lease Remeasurement Accumulated Amortization Impact | `LeaseRemeasurementAccumulatedAmortizationImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Lease Remeasurement Lease Liability Impact | `LeaseRemeasurementLeaseLiabilityImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| New Gross Asset Balances | `NewGrossAssetBalances` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| New Lease Liabilities | `NewLeaseLiabilities` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Prior Period Accumulated Amortization Balance | `PriorPeriodAccumulatedAmortizationBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Prior Period Gross Asset Balance | `PriorPeriodGrossAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Prior Period Lease Liability | `PriorPeriodLeaseLiability` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Reclass Accumulated Amortization Impact | `ReclassAccumulatedAmortizationImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Reclass Gross Asset Balance Impact | `ReclassGrossAssetBalanceImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Reclass Lease Liability Impact | `ReclassLeaseLiabilityImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Reclassification Accumulated Amortization Impact | `ReclassificationAccumulatedAmortizationImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Reclassification Lease Liability Impact | `ReclassificationLeaseLiabilityImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Reclassification of Gross Asset Balance | `ReclassificationOfGrossAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| Remeasurement Gross Asset Balance Impact | `RemeasurementGrossAssetBalanceImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Roll Forward Report |
| 12-Month Forward Change in Asset Balance | `Forward12MonthAssetChange` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| 12-Month Forward Change in Liability Balance | `Forward12MonthLiabilityChange` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| ASC 842 Schedule | `CodeASC842ScheduleID` | `sCODE_ASC842_SCHEDULE` | Global | No | No |  | Contract / Straight Line Summary |
| Accounting Method | `CodeAccountingMethodID` | `sCODE_ACCOUNTING_METHOD` | Global | No | No |  | Contract / Straight Line Summary |
| Aggregate Value Of Lease | `CalcAggregateValueOfLease` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Aggregate Value Of Lease Before Adjustments | `CalcAggValueOfLeaseNoAdjust` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Asset Amortization Expense Adjustment | `AssetAmortExpenseAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Associated Expense Setup IDs | `AssociatedExpenseSetupIDs` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Summary |
| Balance Forward | `BalanceForward` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Balance Sheet Impact | `RemeasurementBalanceForward` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Summary |
| Cancellation Option Amount | `CancellationOptionAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Cash Expense Adjustment | `CashExpenseAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Straight Line Summary |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Straight Line Summary |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Straight Line Summary |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Straight Line Summary |
| Current Period Asset Balance | `CurrentAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Current Period Liability Balance | `CurrentLiabilityBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Current Remaining Balance Lease Payments | `CurrentRemainingCashBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Current Remaining Cash Balance After Report End | `CurrentRemainingCashBalanceAfterReportEnd` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Date Range | `DateRange` | `sTYPE_DATE_RANGE` | Global | No | No |  | Contract / Straight Line Summary |
| Discount Rate | `DiscountRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Straight Line Summary |
| Dismantling / Restoring Cost Amount | `DismantlingStorageCostAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Summary |
| Equipment | `AssetID` | `sTYPE_EQUIPMENT` | Global | No | No |  | Contract / Straight Line Summary |
| Equipment Associated Entity | `AssetAssociatedProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Contract / Straight Line Summary |
| Final Asset Amount | `FinalAssetAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Final Asset Amount Allocation Percentage | `FinalAssetAllocPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Straight Line Summary |
| Final Asset Amount Date | `FinalAssetDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Summary |
| IFRS 16 Schedule | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Global | No | No |  | Contract / Straight Line Summary |
| Impairment Amount | `ImpairmentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Inactive Date | `InactiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Summary |
| Initial Asset Balance | `InitialAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Initial Asset Balance Adjustment | `InitialAssetBalanceAdjust` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Initial Asset Balance Currency Rate | `InitialAssetBalanceCurrencyRate` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Straight Line Summary |
| Initial Direct Cost Amount | `InitialDirectCostAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Initial Liability Balance | `InitialLiabilityBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Initial Liability Balance Adjustment | `InitialLiabilityBalanceAdjust` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Initial Liability Balance Currency Rate | `InitialLiabilityBalanceCurrencyRate` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Straight Line Summary |
| Interest Before Mid-period Remeasurement | `InterestBeforeMidRemeasure` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Interest Expense Adjustment | `InterestExpenseAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Is ASC 842 Schedule? | `IsASC842Schedule` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Straight Line Summary |
| Is Approved? | `IsApproved` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Straight Line Summary |
| Is IFRS 16 Schedule? | `IsIFRS16Schedule` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Straight Line Summary |
| Is Inactive? | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Contract / Straight Line Summary |
| Is SL Schedule? | `IsSLSchedule` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Straight Line Summary |
| Last Balance Posted | `LastBalancePosted` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Last Posted Balance Sheet Impact | `LastPostedBalanceSheetImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Last Posted Date | `LastPostedDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Summary |
| Last Posted End Date | `LastPostedEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Summary |
| Lease Incentive Amount | `LeaseIncentiveAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Straight Line Summary |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Straight Line Summary |
| Needs Recalc Modified by Last Member | `NeedsRecalcModifiedByLastMember` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Straight Line Summary |
| Needs Recalc Modified by Member List | `NeedsRecalcModifiedByMemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Straight Line Summary |
| Needs Recalculation | `NeedsRecalculation` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Straight Line Summary |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Straight Line Summary |
| PV Of Cancellation Option | `PVOfCancellationOption` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| PV Of Financial Terms | `CalcPVOfFinancialTerms` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| PV Of Financial Terms Before Adjustments | `CalcPVOfFinancialTermsNoAdjust` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| PV Of Other Adjustments | `PVOfOtherAdjustments` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| PV Of Purchase Option | `PVOfPurchaseOption` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| PV Of Residual Value Guarantees | `PVOfResidualValueGuarantees` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| PV Of Structuring Costs | `PVOfStructuringCosts` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Period Amount | `PeriodAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Posted End Date | `PostedEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Summary |
| Posted Initial Asset Adjustment for Mod Effective Date | `PostedInitAssetAdj` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Posted Initial Liability Adjustment for Mod Effective Date | `PostedInitLiabilityAdj` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Posted Total Asset Adjustment at Mod Input Date | `PostedAssetAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Posted Total Liability Adjustment at Mod Input Date | `PostedLiabilityAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Pre Commence Pay Amount | `PreCommencePayAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Prior Accumulated Amortization Balance | `PriorAccumulatedAmortizationBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Prior Schedule Last Posted Period | `PriorLastPostedPeriodID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Straight Line Summary |
| Profit And Loss Impact | `ProfitAndLossImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Purchase Option Amount | `PurchaseOptionAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Recalc Override Notes | `RecalcOverrideNotesIDList` | `sTYPE_RECALC_NOTES` | Global | No | No |  | Contract / Straight Line Summary |
| Recalculation Trigger Date | `RecalcTriggerDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Summary |
| Remaining Asset Balance | `SLRemainingAssetBalance` | `sTYPE_PERCENT_OR_AMOUNT` | Global | No | No |  | Contract / Straight Line Summary |
| Residual Value Guarantees | `ResidualValueGuarantees` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Straight Line Summary |
| Schedule Creation Reason | `CodeScheduleCreationReasonID` | `sCODE_SCHEDULE_CREATION_REASON` | Global | No | No |  | Contract / Straight Line Summary |
| Shortened Lease Liability Diff | `ShortenedLeaseLiabilityDiff` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Shortened Schedule Initial Liability Balance | `ShortenedSchedInitLiabilityBal` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Shortened Term Asset Diff | `ShortenedTermAssetDiff` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Shortened Term Rent Diff | `ShortenedTermRentDiff` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Single Lease Expense Adjustment | `SingleLeaseExpenseAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Straight Line Expense Before Mid-period Remeasurement | `SleBeforeMidRemeasure` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Straight Line Schedule | `CodeSLScheduleID` | `sCODE_SL_SCHEDULE` | Global | No | No |  | Contract / Straight Line Summary |
| Straight Line Summary ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Straight Line Summary |
| Straight Line Summary RecID | `SLSummaryID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Straight Line Summary |
| Straight Line Term Length | `SLTermLength` | `sTYPE_NUMBER_FRACTION2DIGITS` | Global | No | No |  | Contract / Straight Line Summary |
| Total Commitment | `TotalCommitment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Total Impairment Impact | `TotalImpairmentImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Translated Initial Asset Balance | `TranslatedInitialAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
| Translated Initial Liability Balance | `TranslatedInitialLiabilityBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Summary |
