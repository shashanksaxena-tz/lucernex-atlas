# ExpenseSchedule — Data Fields

The recurring expense-billing schedule generated from an ExpenseSetup — per-period billed amounts, adjustment method and type (for escalating charges), and tax amount fields (Calculated Tax Amount #1-3+) for jurisdictions with multiple tax components. 51 Global fields under Contract and Summary Information.

**Table Association:** `ExpenseSchedule` &nbsp;·&nbsp; **Total fields:** 51 (Global: 51, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Account Period | `AccountPeriod` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Schedule |
| Account Year | `AccountYear` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Expense Schedule |
| Adjustment Method | `AdjustmentMethod` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Schedule |
| Adjustment Method Type | `CodeAdjustmentMethodID` | `sCODE_ADJUSTMENT_METHOD` | Global | No | No |  | Contract / Expense Schedule |
| Annual Amount | `AnnualAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Approval Status | `CodeApprovalStatusID` | `sCODE_APPROVAL_STATUS` | Global | No | No |  | Contract / Expense Schedule |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | Yes | No |  | Contract / Expense Schedule |
| Calculated Tax Amount #1 | `CalculatedTaxAmount1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Calculated Tax Amount #2 | `CalculatedTaxAmount2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Calculated Tax Amount #3 | `CalculatedTaxAmount3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Calculated Tax Amount #4 | `CalculatedTaxAmount4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Expense Schedule |
| Contract Term | `ContractTermID` | `sTYPE_CONTRACT_TERM` | Global | No | No |  | Contract / Expense Schedule |
| Daily Rent Rate | `DailyRentRate` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Date Range | `DateRange` | `sTYPE_DATE_RANGE` | Global | No | No |  | Contract / Expense Schedule |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Expense Schedule |
| End Date | `EndDate` | `sTYPE_DATE` | Global | Yes | No |  | Contract / Expense Schedule |
| Equipment | `AssetID` | `sTYPE_EQUIPMENT` | Global | No | No |  | Contract / Expense Schedule |
| Equipment Associated Entity | `AssetAssociatedProjectEntityID` | `sTYPE_MIXEDENTITY` | Global | No | No |  | Contract / Expense Schedule |
| Expense Schedule ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Expense Schedule |
| Expense Schedule RecID | `ExpenseScheduleID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Expense Schedule |
| Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | Yes | No |  | Contract / Expense Schedule |
| First Payment Amount | `FirstPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Hold? | `HoldFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Schedule |
| Is CPI? | `IsCPI` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Schedule |
| Last Approval Change Date | `LastApprovalChangeDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Schedule |
| Last Payment Amount | `LastPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Expense Schedule |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Expense Schedule |
| Next Annual Amount | `NextAnnualAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Next Payment Amount | `NextPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Next Schedule | `NextExpenseScheduleID` | `sTYPE_EXPENSE_SCHEDULE` | Global | No | No |  | Contract / Expense Schedule |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Expense Schedule |
| Option Rent? | `OptionRentFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Schedule |
| Payment Amount | `PaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Payment Rate | `PaymentRate` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Previous Annual Amount | `PreviousAnnualAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Previous Payment Amount | `PreviousPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Previous Schedule | `PreviousExpenseScheduleID` | `sTYPE_EXPENSE_SCHEDULE` | Global | No | No |  | Contract / Expense Schedule |
| Processed Date | `ProcessedDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Expense Schedule |
| Processed? | `ProcessedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Schedule |
| Ready For Payment? | `ReadyForPaymentFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Expense Schedule |
| Tax Amount #1 | `TaxAmount1` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Tax Amount #2 | `TaxAmount2` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Tax Amount #3 | `TaxAmount3` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Tax Amount #4 | `TaxAmount4` | `sTYPE_MONEY` | Global | No | No |  | Contract / Expense Schedule |
| Tax Rate #1 | `CalculatedTaxRate1` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Schedule |
| Tax Rate #2 | `CalculatedTaxRate2` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Schedule |
| Tax Rate #3 | `CalculatedTaxRate3` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Schedule |
| Tax Rate #4 | `CalculatedTaxRate4` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Expense Schedule |
| Calculate Amounts | `CalculateScheduleAmounts` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Summary Information / Summary Page Buttons |
