# SLPeriod — Data Fields

Period-level straight-line rent detail underlying SLSummary — one record per accounting period per contract carrying asset/liability balance, amortization expense, and both the current-currency and '- Translated' value pair for every monetary field, plus 12-Month Forward Change figures used for disclosure roll-forwards. 78 Global fields; where SLSummary is the fiscal-year rollup, SLPeriod is the period-by-period ledger that rollup is built from.

**Table Association:** `SLPeriod` &nbsp;·&nbsp; **Total fields:** 78 (Global: 78, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| 12-Month Forward Change in Asset Balance | `Forward12MonthAssetChange` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| 12-Month Forward Change in Liability Balance | `Forward12MonthLiabilityChange` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Accumulated Amortization Balance | `CumulativeAssetAmortExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Allocations | `SLPeriodAllocations` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Asset Amortization Expense - Translated | `AssetAmortizationExpenseTranslated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Asset Balance | `AssetAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Asset Balance - Translated | `AssetAmountTranslated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Asset Translation Adjustment | `AssetTranslationAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Period |
| Cash Payment - Translated | `CashPaymentTranslated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Cash Rate | `ConversionRateMonthEnd` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Straight Line Period |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Straight Line Period |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Straight Line Period |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Straight Line Period |
| Cumulative Deferred Balance | `CumulativeDeferredBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Cumulative Period Number | `CumulativePeriodNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Straight Line Period |
| Cumulative Translation Adjustment | `CumulativeTranslationAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Period |
| Equipment | `AssetID` | `sTYPE_EQUIPMENT` | Global | No | No |  | Contract / Straight Line Period |
| Equipment Associated Entity | `AssetAssociatedProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Contract / Straight Line Period |
| FX Gain (Loss) | `FXGainLoss` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Fiscal Period | `FiscalPeriod` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Straight Line Period |
| Fiscal Period Year | `FiscalPeriodYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Straight Line Period |
| Gross Asset Balance | `GrossAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Initial Asset Balance | `InitialAssetBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Initial Liability Balance | `InitialLiabilityBalance` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Interest - Translated | `InterestTranslated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Lease Liability - Translated | `LeaseLiabilityTranslated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Liability Balance | `LiabilityAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Liability FX Impact | `LiabilityFXImpact` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Liability Translation Adjustment | `LiabilityTranslationAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Long Term Liability | `LongTermLiability` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Long Term Rent Expense | `LongTermRentExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Straight Line Period |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Straight Line Period |
| Number Days | `NumberDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Straight Line Period |
| PV Of Period Cash Amount | `PVOfPeriodCashAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Period Asset Amortization Expense | `PeriodAssetAmortizationExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Period Average Rate | `ConversionRateAverage` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Straight Line Period |
| Period Cash Amount | `PeriodCashAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Period Deferred Amount | `PeriodDeferredAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Period Expense Amount | `PeriodExpenseAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Period Interest Amount | `PeriodInterestAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Period Liability Amortization Expense | `PeriodLiabilityAmortizationExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Posted Date | `PostedDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Straight Line Period |
| Record Status | `RecordStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Straight Line Period |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Straight Line Period |
| SL Schedule Export Account #1 | `SLExportAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| SL Schedule Export Account #2 | `SLExportAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| SL Schedule Export Account #3 | `SLExportAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Asset Amortization | `ScheduleCumulativeAmortExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #1 | `ExportAcct1Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #10 | `ExportAcct10Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #11 | `ExportAcct11Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #12 | `ExportAcct12Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #13 | `ExportAcct13Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #14 | `ExportAcct14Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #15 | `ExportAcct15Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #16 | `ExportAcct16Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #17 | `ExportAcct17Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #18 | `ExportAcct18Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #19 | `ExportAcct19Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #2 | `ExportAcct2Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #20 | `ExportAcct20Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #3 | `ExportAcct3Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #4 | `ExportAcct4Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #5 | `ExportAcct5Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #6 | `ExportAcct6Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #7 | `ExportAcct7Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #8 | `ExportAcct8Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Schedule Export Account #9 | `ExportAcct9Number` | `sTYPE_TEXT` | Global | No | No |  | Contract / Straight Line Period |
| Short Term Liability (Amortization Based) | `Forward12MonthLiabilityAmortBased` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Short Term Liability (PV Based) | `Forward12MonthLiabilityPVBased` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Short Term Rent Expense | `ShortTermRentExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Straight Line Period |
| Straight Line Period ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Straight Line Period |
| Straight Line Period RecID | `SLPeriodID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Straight Line Period |
| Straight Line Schedule | `CodeSLScheduleID` | `sCODE_SL_SCHEDULE` | Global | No | No |  | Contract / Straight Line Period |
| Straight Line Summary | `SLSummaryID` | `sTYPE_SL_SUMMARY` | Global | Yes | No |  | Contract / Straight Line Period |
