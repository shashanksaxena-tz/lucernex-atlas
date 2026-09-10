# VariableRentOffset — Data Fields

A rent offset tied to a variable expense group/type (rent that adjusts based on a specific expense category rather than CPI or sales). 19 Global fields under Contract.

**Table Association:** `VariableRentOffset` &nbsp;·&nbsp; **Total fields:** 19 (Global: 19, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Aggregate Expense Group | `CodePRAggregateExpGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Expense Offset |
| Aggregate Expense Type | `CodePRAggregateExpTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Expense Offset |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Offset |
| Cap Amount | `CapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Offset |
| Cap Percent | `CapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Offset |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Offset |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Expense Offset |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Offset |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Expense Offset |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Expense Offset |
| Fixed Offset Amount | `FixedOffsetAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Offset |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Offset |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Offset |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Offset |
| Offset ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Offset |
| Offset Group | `CodeOffsetGroupID` | `sCODE_OFFSET_GROUP` | Global | No | No |  | Contract / Expense Offset |
| Offset RecID | `VariableRentOffsetID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Offset |
| Offset Type | `CodeOffsetTypeID` | `sCODE_OFFSET_TYPE` | Global | No | No |  | Contract / Expense Offset |
| Sales Group | `CodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | No | No |  | Contract / Expense Offset |
