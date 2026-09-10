# VirtualExpenseForecastPeriod — Data Fields

A forward-looking forecast of recoverable expense by calendar month/year and expense category, computed rather than stored. 20 Global fields under Contract.

**Table Association:** `VirtualExpenseForecastPeriod` &nbsp;·&nbsp; **Total fields:** 20 (Global: 20, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Forecast |
| Calendar Month | `MonthName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Forecast |
| Calendar Year | `CalendarYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Expense Forecast |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Contract / Expense Forecast |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Forecast |
| Expense Category | `CodeExpenseCategoryID` | `sCODE_EXPENSE_CATEGORY` | Global | No | No |  | Contract / Expense Forecast |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Expense Forecast |
| Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | No | No |  | Contract / Expense Forecast |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Expense Forecast |
| Fiscal Period | `Period` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Forecast |
| Fiscal Year | `FiscalYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Expense Forecast |
| Ignore Alternate Rent? | `IgnoreAlternateRent` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Expense Forecast |
| In Alternate Rent? | `InAlternateRent` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Expense Forecast |
| Is CPI? | `IsCPI` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Expense Forecast |
| Is Fiscal Forecast? | `IsFiscalForecast` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Expense Forecast |
| Is Obligation? | `IsObligationOnly` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Expense Forecast |
| Paid / Forecast Period Amount | `AdjustedPeriodExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Forecast |
| Period Amount | `PeriodExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Forecast |
| Period Paid Amount | `RentPaid` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Forecast |
| Straight-Line Schedule | `CodeSLScheduleID` | `sCODE_SL_SCHEDULE` | Global | No | No |  | Contract / Expense Forecast |
