# AlternateRentSchedule — Data Fields

An alternate/contingency rent calculation method available on a contract — alt rent math formula selection and begin date. 24 Global fields under Contract.

**Table Association:** `AlternateRentSchedule` &nbsp;·&nbsp; **Total fields:** 24 (Global: 24, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Alt Rent Math | `CodeAltRentMathID` | `sCODE_ALT_RENT_MATH` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Alternate Rent Schedule ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Alternate Rent Schedule |
| Alternate Rent Schedule RecID | `AlternateRentScheduleID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | Yes | No |  | Contract / Alternate Rent Schedule |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Alternate Rent Schedule |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Deduct Exclusions? | `PRDeductExclusions` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Alternate Rent Schedule |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Expense Reduction Amount | `ExpenseReductionAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Expense Reduction Percent | `ExpenseReductionPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Monthly Max Cap(Ceiling) | `CapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Monthly Min Cap(Floor) | `FloorAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Percent Rent Rate | `PercentRentRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Sales Group | `CodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Set payments for Percent Rent on Hold | `SetPRHoldFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Set payments for Recurring Expenses on Hold | `SetExpHoldFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Alternate Rent Schedule |
| Suspend SL? | `SuspendSL` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Alternate Rent Schedule |
