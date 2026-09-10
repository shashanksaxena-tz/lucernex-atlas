# ExpenseEscalation — Data Fields

An automatic escalation clause on a recoverable expense — base amount/year, cap amount/percentage, and begin date, distinct from CPI-indexed escalation (see the small CPI entity). 27 Global fields under Contract.

**Table Association:** `ExpenseEscalation` &nbsp;·&nbsp; **Total fields:** 27 (Global: 27, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Base Amount | `BaseAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Escalation |
| Base Year | `BaseYear` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Escalation |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Escalation |
| Cap Amount | `CapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Escalation |
| Cap Percentage | `CapPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Escalation |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Escalation |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Escalation |
| Escalation Category | `CodeEscalationCategoryID` | `sCODE_ESCALATION_CATEGORY` | Global | No | No |  | Contract / Expense Escalation |
| Escalation ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Escalation |
| Escalation Group | `CodeEscalationGroupID` | `sCODE_ESCALATION_GROUP` | Global | No | No |  | Contract / Expense Escalation |
| Escalation Index | `EscalationIndexID` | `sTYPE_ESCALATION_INDEX` | Global | No | No |  | Contract / Expense Escalation |
| Escalation Method | `EscalationMethod` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Escalation |
| Escalation Period | `EscalationPeriod` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Escalation |
| Escalation RecID | `ExpenseEscalationID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Escalation |
| Escalation Type | `CodeEscalationTypeID` | `sCODE_ESCALATION_TYPE` | Global | No | No |  | Contract / Expense Escalation |
| Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | Yes | No |  | Contract / Expense Escalation |
| Fixed Amount | `FixedAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Escalation |
| Frequency | `CodeFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | No | No |  | Contract / Expense Escalation |
| Index Base Factor | `IndexBaseFactor` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Escalation |
| Lifetime Max Percentage | `LifetimeMaxPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Escalation |
| Lifetime Min Percentage | `LifetimeMinPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Escalation |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Escalation |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Escalation |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Escalation |
| Period Max Percentage | `PeriodMaxPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Escalation |
| Period Min Percentage | `PeriodMinPercentage` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Escalation |
| Stop Amount | `StopAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Escalation |
