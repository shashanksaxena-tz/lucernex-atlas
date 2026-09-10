# VirtualSalesPeriod — Data Fields

A computed (non-stored, 'Virtual') period record projecting percentage-rent breakpoints and sales-based rent obligations forward — up to eight numbered Breakpoint Amount/Rate slots per period. 66 Global fields under Contract; 'Virtual' entities in this catalog are calculated projections generated at read-time rather than persisted transactional rows, which is why none of them appear in Firm scope (a tenant cannot customize a calculation the platform generates).

**Table Association:** `VirtualSalesPeriod` &nbsp;·&nbsp; **Total fields:** 66 (Global: 66, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Breakpoint Amount #1 | `PRPBreakpointAmount1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Amount #2 | `PRPBreakpointAmount2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Amount #3 | `PRPBreakpointAmount3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Amount #4 | `PRPBreakpointAmount4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Amount #5 | `PRPBreakpointAmount5` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Amount #6 | `PRPBreakpointAmount6` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Amount #7 | `PRPBreakpointAmount7` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Amount #8 | `PRPBreakpointAmount8` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rate #1 | `PRPBreakpointRate1` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rate #2 | `PRPBreakpointRate2` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rate #3 | `PRPBreakpointRate3` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rate #4 | `PRPBreakpointRate4` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rate #5 | `PRPBreakpointRate5` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rate #6 | `PRPBreakpointRate6` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rate #7 | `PRPBreakpointRate7` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rate #8 | `PRPBreakpointRate8` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Sales Period |
| Breakpoint Rent | `PRPBreakpointRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Calendar Month | `SalesMonth` | `sTYPE_TEXT` | Global | No | No |  | Contract / Sales Period |
| Calendar Month/Year | `SalesMonthYearText` | `sTYPE_TEXT` | Global | No | No |  | Contract / Sales Period |
| Calendar Month/Year Date | `SalesMonthYearSort` | `sTYPE_MONTHS_YEAR` | Global | No | No |  | Contract / Sales Period |
| Calendar Year | `SalesYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Sales Period |
| Cap / Floor Adjusted Rent | `PRPCapFloorAdjustedRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Contract / Sales Period |
| Excluded Sales Amount | `ExcludedSalesPeriodAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Excluded Sales Count | `ExcludedSalesPeriodCount` | `sTYPE_NUMBER_FRACTION0DIGITS` | Global | No | No |  | Contract / Sales Period |
| Fiscal Period Year | `SalesPeriodSort` | `sTYPE_PERIOD_YEAR` | Global | No | No |  | Contract / Sales Period |
| Gross Sales Amount | `GrossSalesPeriodAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Gross Sales Count | `GrossSalesPeriodCount` | `sTYPE_NUMBER_FRACTION0DIGITS` | Global | No | No |  | Contract / Sales Period |
| Is Actual? | `IsActual` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Sales Period |
| Matching Fiscal Period/Year | `SalesPeriodText` | `sTYPE_TEXT` | Global | No | No |  | Contract / Sales Period |
| Net Sales Amount | `NetSalesPeriodAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Net Sales Count | `NetSalesPeriodCount` | `sTYPE_NUMBER_FRACTION0DIGITS` | Global | No | No |  | Contract / Sales Period |
| Period Rent Paid | `SalesPeriodRentPaid` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Due #1 | `PRPBreakpointRentDue1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Due #2 | `PRPBreakpointRentDue2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Due #3 | `PRPBreakpointRentDue3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Due #4 | `PRPBreakpointRentDue4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Due #5 | `PRPBreakpointRentDue5` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Due #6 | `PRPBreakpointRentDue6` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Due #7 | `PRPBreakpointRentDue7` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Due #8 | `PRPBreakpointRentDue8` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Period Begin Date | `BillingBucketBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Period |
| Rent Period Cap Amount | `BillingBucketCapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Period End Date | `BillingBucketEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Period |
| Rent Period Floor Amount | `BillingBucketFloorAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Period Payment Due Date | `BillingBucketDueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Period |
| Rent Period Sales Amount | `PRPSalesAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Rent Period Sales Count | `PRPSalesCount` | `sTYPE_NUMBER_FRACTION0DIGITS` | Global | No | No |  | Contract / Sales Period |
| Reporting Period Begin Date | `ReportingBucketBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Period |
| Reporting Period Due Date | `ReportingBucketDueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Period |
| Reporting Period End Date | `ReportingBucketEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Period |
| Reporting Period Gross Sales Amount | `ReportingBucketGrossSalesAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Reporting Period Net Sales Amount | `ReportingBucketNetSalesAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Group | `CodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | No | No |  | Contract / Sales Period |
| Sales Past Breakpoint #1 | `PRPSalesPastBreakpoint1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Past Breakpoint #2 | `PRPSalesPastBreakpoint2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Past Breakpoint #3 | `PRPSalesPastBreakpoint3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Past Breakpoint #4 | `PRPSalesPastBreakpoint4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Past Breakpoint #5 | `PRPSalesPastBreakpoint5` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Past Breakpoint #6 | `PRPSalesPastBreakpoint6` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Past Breakpoint #7 | `PRPSalesPastBreakpoint7` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Past Breakpoint #8 | `PRPSalesPastBreakpoint8` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Sales Period Begin Date | `PeriodBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Period |
| Sales Period End Date | `PeriodEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Sales Period |
| Total Rent | `PRPTotalRent` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
| Total Rent Due | `PRPRentDue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Sales Period |
