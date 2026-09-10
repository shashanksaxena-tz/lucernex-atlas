# ExpenseAccrualSchedule — Data Fields

The generated period-by-period accrual schedule from an ExpenseAccrualSetup — accrual rate and annual amount per begin period/year. 30 Global fields under Contract.

**Table Association:** `ExpenseAccrualSchedule` &nbsp;·&nbsp; **Total fields:** 30 (Global: 30, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Accrual Rate | `AccrualRate` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Annual Amount | `AnnualAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Begin Period | `BeginPeriod` | `sTYPE_DROPDOWN_PERIOD` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Begin Period / Year | `BeginPeriodName` | `sTYPE_PERIOD_YEAR` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Begin Year | `BeginYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Accrual Schedule |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Daily Accrual Rate | `DailyAccrualRate` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Accrual Schedule |
| End Period | `EndPeriod` | `sTYPE_DROPDOWN_PERIOD` | Global | No | No |  | Contract / Expense Accrual Schedule |
| End Period / Year | `EndPeriodName` | `sTYPE_PERIOD_YEAR` | Global | No | No |  | Contract / Expense Accrual Schedule |
| End Year | `EndYear` | `sTYPE_DROPDOWN_YEAR` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Expense Accrual Schedule ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Accrual Schedule |
| Expense Accrual Schedule RecID | `ExpenseAccrualScheduleID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Expense Accrual Setup | `ExpenseAccrualSetupID` | `sTYPE_EXPENSE_ACCRUAL_SETUP` | Global | Yes | No |  | Contract / Expense Accrual Schedule |
| First Payment Amount | `FirstPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Forecast Adjustment | `ForecastAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Forecast Cap Percent | `ForecastCapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Forecast Growth Percent | `ForecastGrowthPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Last Payment Amount | `LastPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Period Amount | `PeriodAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Plan Adjustment | `PlanAdjustment` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Plan Cap Percent | `PlanCapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Plan Growth Percent | `PlanGrowthPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Planning and Forecasting Notes | `PlanForecastNotes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Accrual Schedule |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Accrual Schedule |
