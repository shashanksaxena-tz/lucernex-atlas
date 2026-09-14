# SLSummary

*134 fields · module: Lease Accounting & Payments · Postgres: `s_l_summary`*

Straight-line rent summary — one record per contract holding forward-looking cash and interest expense projected out fiscal-year by fiscal-year (Current, Beyond Fifth, Beyond Sixth) and quarter by quarter within the current year, used for ASC 842/IFRS 16 disclosure schedules. All 135 fields are Global MONEY values; this is a reporting rollup table, not a transactional one, which is why there are no Boolean flags or codes — every field is a pre-calculated dollar amount for a specific future period.

Source: `data-fields/sl-summary.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 134 |
| Fields with a vendor definition | 101 of 134 inventoried |
| Physical tables | `s_l_summary` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 135 (135 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 8 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 22 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in s_l_summary

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 101 fields carry a vendor definition

**Observed.** 101 of this record's 134 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 133 comparable

**Observed.** Over the 133 fields both captures contain, they agree on 132. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetID` | Equipment | The asset ID of the equipment on your equipment schedule. | Equipment ID | Global |  | `s_l_summary.AssetID · TEXT` | [Asset](Asset.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `s_l_summary.ContractID · TEXT` | [Contract](Contract.md) |
| `NeedsRecalcModifiedByLastMember` | Needs Recalc Modified by Last Member | This field lists the last member whose action would have caused the Recalc? flag to change. | Member ID | Global |  | `s_l_summary.NeedsRecalcModifiedByLastMember · TEXT` | [Member](Member.md) |
| `NeedsRecalcModifiedByMemberIDList` | Needs Recalc Modified by Member List | This field lists all members who have made changes that would cause the Recalc? flag to change. | Member ID | Global |  | `s_l_summary.NeedsRecalcModifiedByMemberIDList · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `s_l_summary.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `RecalcOverrideNotesIDList` | Recalc Override Notes |  | Recalc Override Notes ID | Global |  | `s_l_summary.RecalcOverrideNotesIDList · TEXT` | [RecalcOverrideNotes](RecalcOverrideNotes.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | This is a reporting field that returns data about the asset associated with the entity. | Entity | Global |  | `s_l_summary.AssetAssociatedProjectEntityID · TEXT` |  |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeASC842ScheduleID` | ASC 842 Schedule | The ASC 842 Schedule field is where you select the ASC 842 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (ASC 842 Schedule Type) | Global |  | `s_l_summary.CodeASC842ScheduleID · TEXT` | ASC 842 Schedule Type |
| `CodeAccountingMethodID` | Accounting Method | This field sets the accounting method for your lease accounting schedule. If its value is changed, you will need to remeasure your schedule. | Dropdown (Accounting Method Code) | Global |  | `s_l_summary.CodeAccountingMethodID · TEXT` | Accounting Method Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `s_l_summary.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeIFRS16ScheduleID` | IFRS 16 Schedule | The IFRS 16 Schedule field is where you select the IFRS 16 schedule you want to associate with a record. This field is functional, and changing its value on the Accounting Assumptions page, the Covenants page, or the Recurring Expenses page will set the Recalc? flag to YES. | Dropdown (IFRS 16 Schedule Type) | Global |  | `s_l_summary.CodeIFRS16ScheduleID · TEXT` | IFRS 16 Schedule Type |
| `CodeSLScheduleID` | Straight Line Schedule | This field displays the Straight Line Schedule ID. | Dropdown (Straight Line Schedule Type) | Global |  | `s_l_summary.CodeSLScheduleID · TEXT` | Straight Line Schedule Type |
| `CodeScheduleCreationReasonID` | Schedule Creation Reason | Select the reason the lease accounting schedule was created from this field. | Dropdown (Schedule Creation Reason Code) | Global |  | `s_l_summary.CodeScheduleCreationReasonID · TEXT` | Schedule Creation Reason Code |

### Money (91)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccumulatedAmortizationBalancePriorToImpairment` | Accumulated Amortization Balance Prior to Impairment |  | Currency | Global |  | `s_l_summary.AccumulatedAmortizationBalancePriorToImpairment · TEXT` |  |
| `AssetAmortExpenseAdjustment` | Asset Amortization Expense Adjustment |  | Currency | Global |  | `s_l_summary.AssetAmortExpenseAdjustment · TEXT` |  |
| `AssetAmortizationExpense` | Asset Amortization Expense |  | Currency | Global |  | `s_l_summary.AssetAmortizationExpense · TEXT` |  |
| `BalanceForward` | Balance Forward | The difference between the asset and liability balance at the start of your accounting schedule. | Currency | Global |  | `s_l_summary.BalanceForward · TEXT` |  |
| `BeyondCurrentFiscalYearCashExpense` | Current Fiscal Year and Beyond Cash Expense | The amount of cash expense for the current fiscal year through to the end of the schedule. | Currency | Global |  | `s_l_summary.BeyondCurrentFiscalYearCashExpense · TEXT` |  |
| `BeyondCurrentFiscalYearInterestExpense` | Current Fiscal Year and Beyond Interest Expense | The amount of interest expense for the current fiscal year through to the end of the schedule. | Currency | Global |  | `s_l_summary.BeyondCurrentFiscalYearInterestExpense · TEXT` |  |
| `BeyondFifthFiscalYearCashExpense` | Beyond Fifth Fiscal Year Cash Expense | The amount of cash expense five years beyond the current fiscal year and through to the end of the schedule. | Currency | Global |  | `s_l_summary.BeyondFifthFiscalYearCashExpense · TEXT` |  |
| `BeyondSixthFiscalYearCashExpense` | Beyond Sixth Fiscal Year Cash Expense | The amount of cash expense six years beyond the current fiscal year and through to the end of the schedule. | Currency | Global |  | `s_l_summary.BeyondSixthFiscalYearCashExpense · TEXT` |  |
| `CalcAggValueOfLeaseNoAdjust` | Aggregate Value Of Lease Before Adjustments | This field displays the cash value of the lease between the accounting begin date and end date prior to any accounting assumption adjustments. | Currency | Global |  | `s_l_summary.CalcAggValueOfLeaseNoAdjust · TEXT` |  |
| `CalcAggregateValueOfLease` | Aggregate Value Of Lease | This field displays the cash value of the lease between the accounting begin date and end date with accounting assumption adjustments. | Currency | Global |  | `s_l_summary.CalcAggregateValueOfLease · TEXT` |  |
| `CalcPVOfFinancialTerms` | PV Of Financial Terms | The present value of your financial terms including any accounting assumptions adjustments. | Currency | Global |  | `s_l_summary.CalcPVOfFinancialTerms · TEXT` |  |
| `CalcPVOfFinancialTermsNoAdjust` | PV Of Financial Terms Before Adjustments | The present value of your financial terms prior to any accounting assumptions adjustments. | Currency | Global |  | `s_l_summary.CalcPVOfFinancialTermsNoAdjust · TEXT` |  |
| `CancellationOptionAmount` | Cancellation Option Amount | The cash value of any contractual cancellation options. | Currency | Global |  | `s_l_summary.CancellationOptionAmount · TEXT` |  |
| `CashExpenseAdjustment` | Cash Expense Adjustment |  | Currency | Global |  | `s_l_summary.CashExpenseAdjustment · TEXT` |  |
| `CurrentAssetBalance` | Current Period Asset Balance | The current value of the right of use asset. In Report Builder currency conversions, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of the first accounting period. | Currency | Global |  | `s_l_summary.CurrentAssetBalance · TEXT` |  |
| `CurrentFiscalYearCashExpense` | Current Fiscal Year Cash Expense | The cash expense summed over the current fiscal year. | Currency | Global |  | `s_l_summary.CurrentFiscalYearCashExpense · TEXT` |  |
| `CurrentFiscalYearQ1CashExpense` | Current Fiscal Year Q1 Cash Expense | This field displays the total cash expense for the remaining complete quarters in the fiscal year. This field will only populate if the period the report begins in is period 1. | Currency | Global |  | `s_l_summary.CurrentFiscalYearQ1CashExpense · TEXT` |  |
| `CurrentFiscalYearQ2CashExpense` | Current Fiscal Year Q2 Cash Expense | This field displays the total cash expense for the remaining complete quarters in the fiscal year. This field will only populate if the period the report begins in is period 1 - 4. | Currency | Global |  | `s_l_summary.CurrentFiscalYearQ2CashExpense · TEXT` |  |
| `CurrentFiscalYearQ3CashExpense` | Current Fiscal Year Q3 Cash Expense | This field displays the total cash expense for the remaining complete quarters in the fiscal year. This field will only populate if the period the report begins in is period 1 - 7. | Currency | Global |  | `s_l_summary.CurrentFiscalYearQ3CashExpense · TEXT` |  |
| `CurrentFiscalYearQ4CashExpense` | Current Fiscal Year Q4 Cash Expense | This field displays the total cash expense for the remaining complete quarters in the fiscal year. This field will only populate if the period the report begins in is period 1 - 9. | Currency | Global |  | `s_l_summary.CurrentFiscalYearQ4CashExpense · TEXT` |  |
| `CurrentLiabilityBalance` | Current Period Liability Balance | The current value of the lease liability. In Report Builder currency conversions, this fields will be converted according to the foreign exchange rate record appropriate for each accounting period. That is, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of that accounting period. | Currency | Global |  | `s_l_summary.CurrentLiabilityBalance · TEXT` |  |
| `CurrentRemainingCashBalance` | Current Remaining Balance Lease Payments | This field displays the sum of the current and future remaining lease payments in the rent schedule. | Currency | Global |  | `s_l_summary.CurrentRemainingCashBalance · TEXT` |  |
| `CurrentRemainingCashBalanceAfterReportEnd` | Current Remaining Cash Balance After Report End | This field displays the sum of the future remaining lease payments in the rent schedule, excluding the current period. | Currency | Global |  | `s_l_summary.CurrentRemainingCashBalanceAfterReportEnd · TEXT` |  |
| `DismantlingStorageCostAmount` | Dismantling / Restoring Cost Amount | This field appears in the Create New Schedule window. Enter the cost of any activity necessary to restore the asset to its original state prior to the expiration of the lease. | Currency | Global |  | `s_l_summary.DismantlingStorageCostAmount · TEXT` |  |
| `EndingAccumulatedAmortizationBalance` | Ending Accumulated Amortization Balance |  | Currency | Global |  | `s_l_summary.EndingAccumulatedAmortizationBalance · TEXT` |  |
| `EndingGrossAssetBalance` | Ending Gross Asset Balance |  | Currency | Global |  | `s_l_summary.EndingGrossAssetBalance · TEXT` |  |
| `EndingLeaseLiabilityBalance` | Ending Lease Liability Balance |  | Currency | Global |  | `s_l_summary.EndingLeaseLiabilityBalance · TEXT` |  |
| `FifthFiscalYearCashExpense` | Fifth Fiscal Year Cash Expense | The cash expense of the fiscal year five years after your current fiscal year. | Currency | Global |  | `s_l_summary.FifthFiscalYearCashExpense · TEXT` |  |
| `FinalAssetAmount` | Final Asset Amount | If you want to specify an amount of the total asset balance that should remain after the schedule end date, enter the value in this field. This field is only made available on Finance contracts. | Currency | Global |  | `s_l_summary.FinalAssetAmount · TEXT` |  |
| `Forward12MonthAssetChange` | 12-Month Forward Change in Asset Balance | For period n, The change in the asset balance from period n + 1 to period n + 12. In Report Builder currency conversions, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of the first accounting period. | Currency | Global |  | `s_l_summary.Forward12MonthAssetChange · TEXT` |  |
| `Forward12MonthLiabilityChange` | 12-Month Forward Change in Liability Balance | For period n, The change in the liability balance from period n + 1 to period n + 12. In Report Builder currency conversions, this fields will be converted according to the foreign exchange rate record appropriate for each accounting period. That is, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of that accounting period. | Currency | Global |  | `s_l_summary.Forward12MonthLiabilityChange · TEXT` |  |
| `FourthFiscalYearCashExpense` | Fourth Fiscal Year Cash Expense | The cash expense of the fiscal year four years after your current fiscal year. | Currency | Global |  | `s_l_summary.FourthFiscalYearCashExpense · TEXT` |  |
| `ImpairmentAmount` | Impairment Amount | Enter any deductions related to the diminished value of the asset as a negative number. | Currency | Global |  | `s_l_summary.ImpairmentAmount · TEXT` |  |
| `ImpairmentsAndAccumulatedAmortizationReset` | Impairments and Accumulated Amortization Reset |  | Currency | Global |  | `s_l_summary.ImpairmentsAndAccumulatedAmortizationReset · TEXT` |  |
| `InitialAssetBalance` | Initial Asset Balance | This is a calculated value which contains the initial value over the asset of the lease. In Report Builder currency conversions, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of the first accounting period. | Currency | Global |  | `s_l_summary.InitialAssetBalance · TEXT` |  |
| `InitialAssetBalanceAdjust` | Initial Asset Balance Adjustment | This field pulls the value of any adjustments to the initial asset balance from the ContractFinancialTest table. | Currency | Global |  | `s_l_summary.InitialAssetBalanceAdjust · TEXT` |  |
| `InitialDirectCostAmount` | Initial Direct Cost Amount | This field appears in the Create New Schedule window. Enter the incremental costs of a lease that would not have been incurred if the lease had not been obtained. For example, for contracts broker s fees, certain legal fees, and certain payments to tenants to move out. | Currency | Global |  | `s_l_summary.InitialDirectCostAmount · TEXT` |  |
| `InitialLiabilityBalance` | Initial Liability Balance | This is the total of all of the Period Payment Present Values over the life of the lease. In Report Builder currency conversions, a foreign exchange rate record will be applied that has an effective date between the Begin Date and the End Date of the first accounting period. | Currency | Global |  | `s_l_summary.InitialLiabilityBalance · TEXT` |  |
| `InitialLiabilityBalanceAdjust` | Initial Liability Balance Adjustment | This field pulls the value of any adjustments to the initial liability balance from the ContractFinancialTest table. | Currency | Global |  | `s_l_summary.InitialLiabilityBalanceAdjust · TEXT` |  |
| `InterestBeforeMidRemeasure` | Interest Before Mid-period Remeasurement | The partial interest from the start of the period to the remeasurement date. | Currency | Global |  | `s_l_summary.InterestBeforeMidRemeasure · TEXT` |  |
| `InterestExpense` | Interest Expense |  | Currency | Global |  | `s_l_summary.InterestExpense · TEXT` |  |
| `InterestExpenseAdjustment` | Interest Expense Adjustment |  | Currency | Global |  | `s_l_summary.InterestExpenseAdjustment · TEXT` |  |
| `LastBalancePosted` | Last Balance Posted | This is the asset minus the liability as of the last posted period. | Currency | Global |  | `s_l_summary.LastBalancePosted · TEXT` |  |
| `LastPostedBalanceSheetImpact` | Last Posted Balance Sheet Impact | This is the portion of the last posted balance that is to remain on the balance sheet. | Currency | Global |  | `s_l_summary.LastPostedBalanceSheetImpact · TEXT` |  |
| `LeaseExpirationAccumulatedAmortizationImpact` | Lease Expiration Accumulated Amortization Impact |  | Currency | Global |  | `s_l_summary.LeaseExpirationAccumulatedAmortizationImpact · TEXT` |  |
| `LeaseExpirationGrossAssetBalance` | Lease Expiration Gross Asset Balance |  | Currency | Global |  | `s_l_summary.LeaseExpirationGrossAssetBalance · TEXT` |  |
| `LeaseIncentiveAmount` | Lease Incentive Amount | This field appears in the Create New Schedule window. Enter any incentives that have reduced the cost of the lease. | Currency | Global |  | `s_l_summary.LeaseIncentiveAmount · TEXT` |  |
| `LeaseLiabilityPaymentImpact` | Lease Liability Payment Impact |  | Currency | Global |  | `s_l_summary.LeaseLiabilityPaymentImpact · TEXT` |  |
| `LeaseRemeasurementAccumulatedAmortizationImpact` | Lease Remeasurement Accumulated Amortization Impact |  | Currency | Global |  | `s_l_summary.LeaseRemeasurementAccumulatedAmortizationImpact · TEXT` |  |
| `LeaseRemeasurementLeaseLiabilityImpact` | Lease Remeasurement Lease Liability Impact |  | Currency | Global |  | `s_l_summary.LeaseRemeasurementLeaseLiabilityImpact · TEXT` |  |
| `NewGrossAssetBalances` | New Gross Asset Balances |  | Currency | Global |  | `s_l_summary.NewGrossAssetBalances · TEXT` |  |
| `NewLeaseLiabilities` | New Lease Liabilities |  | Currency | Global |  | `s_l_summary.NewLeaseLiabilities · TEXT` |  |
| `NextFiscalYearCashExpense` | Next Fiscal Year Cash Expense | The cash expense of the fiscal year after your current fiscal year. | Currency | Global |  | `s_l_summary.NextFiscalYearCashExpense · TEXT` |  |
| `PVOfCancellationOption` | PV Of Cancellation Option | Enter the present value of the cancellation option. | Currency | Global |  | `s_l_summary.PVOfCancellationOption · TEXT` |  |
| `PVOfOtherAdjustments` | PV Of Other Adjustments | Enter any other miscellaneous costs that should be accounted for in the schedule. | Currency | Global |  | `s_l_summary.PVOfOtherAdjustments · TEXT` |  |
| `PVOfPurchaseOption` | PV Of Purchase Option | Enter the present value of the purchase option. | Currency | Global |  | `s_l_summary.PVOfPurchaseOption · TEXT` |  |
| `PVOfResidualValueGuarantees` | PV Of Residual Value Guarantees | Enter the present value of the residual value guarantee. | Currency | Global |  | `s_l_summary.PVOfResidualValueGuarantees · TEXT` |  |
| `PVOfStructuringCosts` | PV Of Structuring Costs | Enter any fees paid to the owners of a special-purpose entity for structuring the transaction. | Currency | Global |  | `s_l_summary.PVOfStructuringCosts · TEXT` |  |
| `PeriodAmount` | Period Amount | The total expenses for the period from your recurring expenses. The value of this field is used to perform calculations for your lease accounting schedule. | Currency | Global |  | `s_l_summary.PeriodAmount · TEXT` |  |
| `PostedAssetAdjustment` | Posted Total Asset Adjustment at Mod Input Date | The difference between the Asset Balance of the new schedule and the previous schedule s last posted Asset Balance. | Currency | Global |  | `s_l_summary.PostedAssetAdjustment · TEXT` |  |
| `PostedInitAssetAdj` | Posted Initial Asset Adjustment for Mod Effective Date | The difference between the Initial Asset Balance of the new schedule and the previous schedule s posted Asset Balance as of the Posted End Date. | Currency | Global |  | `s_l_summary.PostedInitAssetAdj · TEXT` |  |
| `PostedInitLiabilityAdj` | Posted Initial Liability Adjustment for Mod Effective Date | The difference between the Initial Liability Balance of the new schedule and the previous schedule s posted Liability Balance as of the Posted End Date. | Currency | Global |  | `s_l_summary.PostedInitLiabilityAdj · TEXT` |  |
| `PostedLiabilityAdjustment` | Posted Total Liability Adjustment at Mod Input Date | The difference between the Liability Balance of the new schedule and the previous schedule s last posted Liability Balance. | Currency | Global |  | `s_l_summary.PostedLiabilityAdjustment · TEXT` |  |
| `PreCommencePayAmount` | Pre Commence Pay Amount | This field appears in the Create New Schedule window. Enter the amount paid towards rent prior to the commencement date, minus any incentives that have reduced the cost of the lease. You should also include your Cumulative Deferred Balance in this value if you are converting from an ASC 840 Straight Line Schedule. | Currency | Global |  | `s_l_summary.PreCommencePayAmount · TEXT` |  |
| `PriorAccumulatedAmortizationBalance` | Prior Accumulated Amortization Balance | The Accumulated Amortization Balance of the accounting period prior to the impairment. | Currency | Global |  | `s_l_summary.PriorAccumulatedAmortizationBalance · TEXT` |  |
| `PriorPeriodAccumulatedAmortizationBalance` | Prior Period Accumulated Amortization Balance |  | Currency | Global |  | `s_l_summary.PriorPeriodAccumulatedAmortizationBalance · TEXT` |  |
| `PriorPeriodGrossAssetBalance` | Prior Period Gross Asset Balance |  | Currency | Global |  | `s_l_summary.PriorPeriodGrossAssetBalance · TEXT` |  |
| `PriorPeriodLeaseLiability` | Prior Period Lease Liability |  | Currency | Global |  | `s_l_summary.PriorPeriodLeaseLiability · TEXT` |  |
| `ProfitAndLossImpact` | Profit And Loss Impact | The portion of the balance forward that will not persist on the balance sheet and is taken as a capital gain or loss. | Currency | Global |  | `s_l_summary.ProfitAndLossImpact · TEXT` |  |
| `PurchaseOptionAmount` | Purchase Option Amount | This field appears in the Create New Schedule window. This field pulls the value of any purchase options from the Covenant table. | Currency | Global |  | `s_l_summary.PurchaseOptionAmount · TEXT` |  |
| `ReclassAccumulatedAmortizationImpact` | Reclass Accumulated Amortization Impact |  | Currency | Global |  | `s_l_summary.ReclassAccumulatedAmortizationImpact · TEXT` |  |
| `ReclassGrossAssetBalanceImpact` | Reclass Gross Asset Balance Impact |  | Currency | Global |  | `s_l_summary.ReclassGrossAssetBalanceImpact · TEXT` |  |
| `ReclassLeaseLiabilityImpact` | Reclass Lease Liability Impact |  | Currency | Global |  | `s_l_summary.ReclassLeaseLiabilityImpact · TEXT` |  |
| `ReclassificationAccumulatedAmortizationImpact` | Reclassification Accumulated Amortization Impact |  | Currency | Global |  | `s_l_summary.ReclassificationAccumulatedAmortizationImpact · TEXT` |  |
| `ReclassificationLeaseLiabilityImpact` | Reclassification Lease Liability Impact |  | Currency | Global |  | `s_l_summary.ReclassificationLeaseLiabilityImpact · TEXT` |  |
| `ReclassificationOfGrossAssetBalance` | Reclassification of Gross Asset Balance |  | Currency | Global |  | `s_l_summary.ReclassificationOfGrossAssetBalance · TEXT` |  |
| `RemeasurementBalanceForward` | Balance Sheet Impact | The portion of the balance forward that does appear on the balance sheet going forward. | Currency | Global |  | `s_l_summary.RemeasurementBalanceForward · TEXT` |  |
| `RemeasurementGrossAssetBalanceImpact` | Remeasurement Gross Asset Balance Impact |  | Currency | Global |  | `s_l_summary.RemeasurementGrossAssetBalanceImpact · TEXT` |  |
| `ResidualValueGuarantees` | Residual Value Guarantees | This field appears in the Create New Schedule window. This field pulls the value of any residual value guarantees from the Covenant table. | Currency | Global |  | `s_l_summary.ResidualValueGuarantees · TEXT` |  |
| `ShortenedLeaseLiabilityDiff` | Shortened Lease Liability Diff | An initial Liability Balance based on the remaining periods of the original schedule over a shortened term minus the original schedule s last posted period s Liability Balance. | Currency | Global |  | `s_l_summary.ShortenedLeaseLiabilityDiff · TEXT` |  |
| `ShortenedSchedInitLiabilityBal` | Shortened Schedule Initial Liability Balance | An initial Liability Balance based on the remaining periods of the original schedule over a shortened term. | Currency | Global |  | `s_l_summary.ShortenedSchedInitLiabilityBal · TEXT` |  |
| `ShortenedTermAssetDiff` | Shortened Term Asset Diff | The sum of the Asset Amortization Expense for the remaining periods in the original schedule over the shortened term multiplied by negative one. | Currency | Global |  | `s_l_summary.ShortenedTermAssetDiff · TEXT` |  |
| `ShortenedTermRentDiff` | Shortened Term Rent Diff | The Initial Liability Balance of the new schedule minus the Initial Liability Balance of the remaining periods in the original schedule over the shortened term. | Currency | Global |  | `s_l_summary.ShortenedTermRentDiff · TEXT` |  |
| `SingleLeaseExpenseAdjustment` | Single Lease Expense Adjustment |  | Currency | Global |  | `s_l_summary.SingleLeaseExpenseAdjustment · TEXT` |  |
| `SixthFiscalYearCashExpense` | Sixth Fiscal Year Cash Expense | The cash expense of the fiscal year six years after your current fiscal year. | Currency | Global |  | `s_l_summary.SixthFiscalYearCashExpense · TEXT` |  |
| `SleBeforeMidRemeasure` | Straight Line Expense Before Mid-period Remeasurement | The partial single lease expense from the start of the period to the remeasurement date. | Currency | Global |  | `s_l_summary.SleBeforeMidRemeasure · TEXT` |  |
| `ThirdFiscalYearCashExpense` | Third Fiscal Year Cash Expense | The cash expense of the fiscal year three years after your current fiscal year. | Currency | Global |  | `s_l_summary.ThirdFiscalYearCashExpense · TEXT` |  |
| `TotalCommitment` | Total Commitment | The sum of all rent payments for the life of the lease. | Currency | Global |  | `s_l_summary.TotalCommitment · TEXT` |  |
| `TotalImpairmentImpact` | Total Impairment Impact | The sum of the impairment and the Prior Accumulated Amortization Balance. | Currency | Global |  | `s_l_summary.TotalImpairmentImpact · TEXT` |  |
| `TranslatedInitialAssetBalance` | Translated Initial Asset Balance |  | Currency | Global |  | `s_l_summary.TranslatedInitialAssetBalance · TEXT` |  |
| `TranslatedInitialLiabilityBalance` | Translated Initial Liability Balance |  | Currency | Global |  | `s_l_summary.TranslatedInitialLiabilityBalance · TEXT` |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DiscountRate` | Discount Rate | This field is where you enter the Discount Rate (also known as the Interest Rate or the Internal Borrower Rate [IBR]). | Percentage | Global |  | `s_l_summary.DiscountRate · TEXT` |  |
| `FinalAssetAllocPercent` | Final Asset Amount Allocation Percentage | If you want to specify a percentage of the total asset balance that should remain after the schedule end date, enter the value in this field. This field is only made available on Finance contracts. | Percentage | Global |  | `s_l_summary.FinalAssetAllocPercent · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PriorLastPostedPeriodID` | Prior Schedule Last Posted Period | This field populaes with the SLSummary ID for the previous accounting schedule when a new schedule is created. | Number | Global |  | `s_l_summary.PriorLastPostedPeriodID · TEXT` |  |
| `SLSummaryID` | Straight Line Summary RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `s_l_summary.SLSummaryID · VARCHAR(64) NOT NULL` |  |
| `SLTermLength` | Straight Line Term Length | The number of periods in the straight line schedule term. | 2-Digit Number | Global |  | `s_l_summary.SLTermLength · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `s_l_summary.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `s_l_summary.EndDate · TEXT` |  |
| `FinalAssetDate` | Final Asset Amount Date | If you want to select a date beyond the schedule end date to amortize to, enter the date in this field. By default, the value of this field is the schedule end date. This field is only made available for Finance contracts. | Date | Global |  | `s_l_summary.FinalAssetDate · TEXT` |  |
| `InactiveDate` | Inactive Date | The date that a schedule became inactive. | Date | Global |  | `s_l_summary.InactiveDate · TEXT` |  |
| `LastPostedDate` | Last Posted Date | This is the begin date of the last posted period. | Date | Global |  | `s_l_summary.LastPostedDate · TEXT` |  |
| `LastPostedEndDate` | Last Posted End Date | This is the end date of the last posted period. | Date | Global |  | `s_l_summary.LastPostedEndDate · TEXT` |  |
| `PostedEndDate` | Posted End Date | The last posted fiscal period End Date of the schedule being modified. | Date | Global |  | `s_l_summary.PostedEndDate · TEXT` |  |
| `RecalcTriggerDate` | Recalculation Trigger Date | The date that the Recalc? flag was triggered. | Date | Global |  | `s_l_summary.RecalcTriggerDate · TEXT` |  |

### Flags (7)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | This flag is applied to a schedule if another lease accounting schedule replaces it. | Boolean | Global | yes | `s_l_summary.Inactive · TEXT` |  |
| `IsASC842Schedule` | Is ASC 842 Schedule? | This flag indicates that the schedule is an ASC 842 schedule. | Boolean | Global |  | `s_l_summary.IsASC842Schedule · TEXT` |  |
| `IsApproved` | Is Approved? | This flag indicates that the schedule has been approved. Once a schedule has been approved, it cannot be un-approved. Please see the Lx Online Help for more information. | Boolean | Global |  | `s_l_summary.IsApproved · TEXT` |  |
| `IsIFRS16Schedule` | Is IFRS 16 Schedule? | This flag indicates that the schedule is an IFRS 16 schedule. | Boolean | Global |  | `s_l_summary.IsIFRS16Schedule · TEXT` |  |
| `IsIncludeInRollForwardReport` | Is Include in Roll Forward Report? |  | Boolean | Global |  | `s_l_summary.IsIncludeInRollForwardReport · TEXT` |  |
| `IsSLSchedule` | Is SL Schedule? | This flag indicates that the schedule is an Straight Line schedule. | Boolean | Global |  | `s_l_summary.IsSLSchedule · TEXT` |  |
| `NeedsRecalculation` | Needs Recalculation | When set to Yes, this flag indicates that the lease accounting schedule must be recalculated. | Boolean | Global |  | `s_l_summary.NeedsRecalculation · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssociatedExpenseSetupIDs` | Associated Expense Setup IDs | The AssociatedExpenseSetupIDs field returns a list of associated expense setup IDs that use the expense type used in the accounting schedule you are viewing. An associated expense setup ID is created when an expense schedule is created for the expense setup. If a new expense setup with an expense schedule is created, the accounting schedule associated with the expense type will have its Recalc? flag flipped to Yes. | Text | Global |  | `s_l_summary.AssociatedExpenseSetupIDs · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `s_l_summary.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Straight Line Summary ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `s_l_summary.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `s_l_summary.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `s_l_summary.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `s_l_summary.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `s_l_summary.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `s_l_summary.RevNumber · TEXT` |  |

### Other (2)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DateRange` | Date Range | This field is not currently being used in Lx. | Date Range | Global |  | `s_l_summary.DateRange · TEXT` |  |
| `SLRemainingAssetBalance` | Remaining Asset Balance | If you want to specify a percentage or amount of the total asset balance that should remain after the schedule end date, enter the value in this field. There are two option buttons: Currency and Percentage. If you enter a value between 0-100, the system will default the option button setting to Percentage. If you enter a value of 100.01 or above, the system will default the option button setting to Currency. You can override the default option button setting. | Percent or Currency | Global |  | `s_l_summary.SLRemainingAssetBalance · TEXT` |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [RecalcOverrideNotes](RecalcOverrideNotes.md) | `SLSummaryID` |
| [SLPeriod](SLPeriod.md) | `SLSummaryID` |
