# VirtualUsagePeriod — Data Fields

The usage-based-rent counterpart to VirtualSalesPeriod — projects breakpoint cost tiers (with 6-decimal-precision `NUMBER_FRACTION6DIGITS` fields for unit-cost rates) period by period for contracts billed on usage/consumption rather than sales volume. 66 Global fields under Contract.

**Table Association:** `VirtualUsagePeriod` &nbsp;·&nbsp; **Total fields:** 66 (Global: 66, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Breakpoint Amount #1 | `UBRPBreakpointAmount1` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Amount #2 | `UBRPBreakpointAmount2` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Amount #3 | `UBRPBreakpointAmount3` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Amount #4 | `UBRPBreakpointAmount4` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Amount #5 | `UBRPBreakpointAmount5` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Amount #6 | `UBRPBreakpointAmount6` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Amount #7 | `UBRPBreakpointAmount7` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Amount #8 | `UBRPBreakpointAmount8` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Cost #1 | `UBRPBreakpointCost1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Cost #2 | `UBRPBreakpointCost2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Cost #3 | `UBRPBreakpointCost3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Cost #4 | `UBRPBreakpointCost4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Cost #5 | `UBRPBreakpointCost5` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Cost #6 | `UBRPBreakpointCost6` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Cost #7 | `UBRPBreakpointCost7` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Cost #8 | `UBRPBreakpointCost8` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Breakpoint Rent | `UBRPBreakpointRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Calendar Month | `UsageMonth` | `sTYPE_TEXT` | Global | No | No |  | Contract / Usage Period |
| Calendar Month/Year | `UsageMonthYearText` | `sTYPE_TEXT` | Global | No | No |  | Contract / Usage Period |
| Calendar Month/Year Date | `UsageMonthYearSort` | `sTYPE_MONTHS_YEAR` | Global | No | No |  | Contract / Usage Period |
| Calendar Year | `UsageYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Usage Period |
| Cap / Floor Adjusted Rent | `UBRPCapFloorAdjustedRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Contract / Usage Period |
| Is Actual? | `IsActual` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Usage Period |
| Matching Fiscal Period/Year | `UsagePeriodText` | `sTYPE_TEXT` | Global | No | No |  | Contract / Usage Period |
| Net Usage Amount | `NetUsagePeriodAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Net Usage Count | `NetUsagePeriodCount` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Net Usage Share | `NetUsagePeriodShare` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Period Rent Paid | `UsagePeriodRentPaid` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Due #1 | `UBRPBreakpointRentDue1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Due #2 | `UBRPBreakpointRentDue2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Due #3 | `UBRPBreakpointRentDue3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Due #4 | `UBRPBreakpointRentDue4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Due #5 | `UBRPBreakpointRentDue5` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Due #6 | `UBRPBreakpointRentDue6` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Due #7 | `UBRPBreakpointRentDue7` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Due #8 | `UBRPBreakpointRentDue8` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Period Begin Date | `BillingBucketBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage Period |
| Rent Period Cap Amount | `BillingBucketCapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Period End Date | `BillingBucketEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage Period |
| Rent Period Payment Due Date | `BillingBucketDueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage Period |
| Rent Period Usage Amount | `UBRPUsageAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Rent Period Usage Count | `UBRPUsageCount` | `sTYPE_NUMBER_FRACTION0DIGITS` | Global | No | No |  | Contract / Usage Period |
| Rent Period Usage Share | `UBRPUsageShare` | `sTYPE_NUMBER_FRACTION0DIGITS` | Global | No | No |  | Contract / Usage Period |
| Reporting Period Begin Date | `ReportingBucketBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage Period |
| Reporting Period Due Date | `ReportingBucketDueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage Period |
| Reporting Period End Date | `ReportingBucketEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage Period |
| Reporting Period Net Usage Amount | `ReportingBucketNetUsageAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Reporting Period Usage Amount | `ReportingBucketGrossUsageAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Total Rent | `UBRPTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Total Rent Due | `UBRPRentDue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Usage Amount | `GrossUsagePeriodAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Usage Period |
| Usage Count | `GrossUsagePeriodCount` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Group | `CodeUsageGroupID` | `sCODE_USAGE_GROUP` | Global | No | No |  | Contract / Usage Period |
| Usage Past Breakpoint #1 | `UBRPUsagePastBreakpoint1` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Past Breakpoint #2 | `UBRPUsagePastBreakpoint2` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Past Breakpoint #3 | `UBRPUsagePastBreakpoint3` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Past Breakpoint #4 | `UBRPUsagePastBreakpoint4` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Past Breakpoint #5 | `UBRPUsagePastBreakpoint5` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Past Breakpoint #6 | `UBRPUsagePastBreakpoint6` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Past Breakpoint #7 | `UBRPUsagePastBreakpoint7` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Past Breakpoint #8 | `UBRPUsagePastBreakpoint8` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Period Begin Date | `PeriodBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage Period |
| Usage Period End Date | `PeriodEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Usage Period |
| Usage Share | `GrossUsagePeriodShare` | `sTYPE_NUMBER_FRACTION6DIGITS` | Global | No | No |  | Contract / Usage Period |
| Usage Unit Type | `CodeUsageUnitTypeID` | `sCODE_USAGE_UNIT_TYPE` | Global | No | No |  | Contract / Usage Period |
