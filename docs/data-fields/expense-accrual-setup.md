# ExpenseAccrualSetup — Data Fields

The configuration for accruing an expense ahead of its billing (common for property tax and insurance accrued monthly against an annual bill) — accrual message, area-unit basis, and begin period. 30 Global fields under Contract.

**Table Association:** `ExpenseAccrualSetup` &nbsp;·&nbsp; **Total fields:** 30 (Global: 30, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Accrual Message | `AccrualMessage` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Accrual Setup |
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Expense Accrual Setup |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Accrual Setup |
| Begin Period / Year | `BeginPeriodName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Accrual Setup |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Contract / Expense Accrual Setup |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Accrual Setup |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Expense Accrual Setup |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Accrual Setup |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Accrual Setup |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Expense Accrual Setup |
| Current Annual Expense | `CurrentAnnualExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Setup |
| Current Period Expense | `CurrentPeriodExpense` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Accrual Setup |
| Daily Rent | `IsDailyRent` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Accrual Setup |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Accrual Setup |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Accrual Setup |
| End Period / Year | `EndPeriodName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Accrual Setup |
| Expense Accrual Setup ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Accrual Setup |
| Expense Accrual Setup RecID | `ExpenseAccrualSetupID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Accrual Setup |
| Expense Category | `CodeExpenseCategoryID` | `sCODE_EXPENSE_CATEGORY` | Global | No | No |  | Contract / Expense Accrual Setup |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Expense Accrual Setup |
| Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | No | No |  | Contract / Expense Accrual Setup |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Expense Accrual Setup |
| Hold? | `HoldFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Accrual Setup |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Accrual Setup |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Accrual Setup |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Accrual Setup |
| Record Type | `CodeAccrualTypeID` | `sCODE_ACCRUAL_TYPE` | Global | Yes | No |  | Contract / Expense Accrual Setup |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Expense Accrual Setup |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Accrual Setup |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Accrual Setup |
