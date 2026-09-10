# VirtualPRPAggregate — Data Fields

An aggregated percentage-rent obligation projection across a contract's full term — current offset amount and current percentage rent obligation/paid. 15 Global fields under Contract.

**Table Association:** `VirtualPRPAggregate` &nbsp;·&nbsp; **Total fields:** 15 (Global: 15, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Billing Frequency | `CodeBillingFrequencyID` | `sCODE_PR_FREQUENCY` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Current Offset Amount | `VariableRentOffsetAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Current Percentage Rent | `CurrentRentDue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Current Percentage Rent Obligation | `CurrentRentObligation` | `sTYPE_MONEY` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Current Percentage Rent Paid | `CurrentRentPaid` | `sTYPE_MONEY` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Net Percentage Rent Due | `NetSalesRentDue` | `sTYPE_MONEY` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Percentage Rent Type | `CodePercentageRentTypeID` | `sCODE_PERCENTAGE_RENT_TYPE` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Period Begin Date | `PeriodBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Period End Date | `PeriodEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Rent Year Begin Date | `RentYearBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Rent Year End Date | `RentYearEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
| Rent Year Has Alternate Rent? | `RentYearHasAltRent` | `sTYPE_BOOLEAN` | Global | No | No |  | Contract / Percentage Rent Summary Schedule |
