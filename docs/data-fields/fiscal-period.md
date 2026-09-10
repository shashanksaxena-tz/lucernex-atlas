# FiscalPeriod — Data Fields

The fiscal calendar definition — begin/end date and days-in-period per named fiscal period, the calendar backbone that SLPeriod, ExpenseSchedule, and Sales fiscal-period fields reference. 16 Global fields under Company Items.

**Table Association:** `FiscalPeriod` &nbsp;·&nbsp; **Total fields:** 16 (Global: 16, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | Yes | No |  | Company Items / Fiscal Period |
| Days In Period | `NumberDaysInPeriod` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Fiscal Period |
| End Date | `EndDate` | `sTYPE_DATE` | Global | Yes | No |  | Company Items / Fiscal Period |
| Fiscal Period ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Fiscal Period |
| Fiscal Period Name | `FiscalPeriodName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Fiscal Period |
| Fiscal Period RecID | `FiscalPeriodID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Fiscal Period |
| Is 4 or 5 Week Period? | `Is4or5WeekPeriod` | `sTYPE_BOOLEAN` | Global | No | No |  | Company Items / Fiscal Period |
| Matching Calendar Month | `MatchingCalendarMonth` | `sTYPE_MONTH` | Global | No | No |  | Company Items / Fiscal Period |
| Matching Calendar Year | `MatchingCalendarYear` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Fiscal Period |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Fiscal Period |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Fiscal Period |
| Period | `Period` | `sTYPE_NUMBER` | Global | Yes | No |  | Company Items / Fiscal Period |
| Portfolio | `ProgramID` | `sTYPE_PROGRAM` | Global | No | No |  | Company Items / Fiscal Period |
| Quarter | `Quarter` | `sTYPE_NUMBER` | Global | Yes | No |  | Company Items / Fiscal Period |
| Weeks In Period | `NumberWeeksInPeriod` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Fiscal Period |
| Year | `Year` | `sTYPE_NUMBER` | Global | Yes | No |  | Company Items / Fiscal Period |
