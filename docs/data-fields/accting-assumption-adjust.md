# AcctingAssumptionAdjust — Data Fields

A manual adjustment to lease-accounting assumptions used in ASC 842/IFRS 16 calculations — adjustment percent and annual amount, letting an accountant override a calculated assumption. 18 Global fields under Contract.

**Table Association:** `AcctingAssumptionAdjust` &nbsp;·&nbsp; **Total fields:** 18 (Global: 18, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| ASC 842 Schedule | `CodeASC842ScheduleID` | `sCODE_ASC842_SCHEDULE` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Accounting Assumption Adjustment Secondary Rent Schedule Allocation Percent | `SecondaryRentSchedAllocPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Accting Assumption Adjust ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Accounting Assumptions Adjustments |
| Accting Assumption Adjust RecID | `AcctingAssumptionAdjustID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Adjustment Percent | `AdjustmentPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Annual Amount | `AnnualAmount` | `sTYPE_MONEY` | Global | Yes | No |  | Contract / Accounting Assumptions Adjustments |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | Yes | No |  | Contract / Accounting Assumptions Adjustments |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Accounting Assumptions Adjustments |
| End Date | `EndDate` | `sTYPE_DATE` | Global | Yes | No |  | Contract / Accounting Assumptions Adjustments |
| Expense Setup | `ExpenseSetupID` | `sTYPE_EXPENSE_SETUP` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| First Payment Amount | `FirstPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Frequency | `CodeFrequencyID` | `sCODE_FREQUENCY` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| IFRS 16 Schedule | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Last Payment Amount | `LastPaymentAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Payment Amount | `PaymentAmount` | `sTYPE_MONEY` | Global | Yes | No |  | Contract / Accounting Assumptions Adjustments |
| Payment Rate | `PaymentRate` | `sTYPE_MONEY` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
| Proration Method | `CodeProrationMethodID` | `sCODE_PRORATION_METHOD` | Global | No | No |  | Contract / Accounting Assumptions Adjustments |
