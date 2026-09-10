# UseBasedRent — Data Fields

The usage-based rent clause header (e.g., per-unit, per-transaction rent) — billing frequency and currency type, the clause-level record UseBasedRentBreakpoint and VirtualUseBasedRentPeriod project from. 22 Global fields under Contract.

**Table Association:** `UseBasedRent` &nbsp;·&nbsp; **Total fields:** 22 (Global: 22, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Use Based Rent |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Use Based Rent |
| Billing Frequency | `CodeBillingFrequencyID` | `sCODE_FREQUENCY` | Global | No | No |  | Contract / Use Based Rent |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Use Based Rent |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Use Based Rent |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Use Based Rent |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Use Based Rent |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Use Based Rent |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Use Based Rent |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Use Based Rent |
| Model Type | `CodeUseRentModelTypeID` | `sCODE_USE_RENT_MODEL_TYPE` | Global | Yes | No |  | Contract / Use Based Rent |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Use Based Rent |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Use Based Rent |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Use Based Rent |
| Period Payment Due Days | `PeriodPaymentDueDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Use Based Rent |
| Period Report Due Days | `PeriodReportDueDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Use Based Rent |
| Rent Year Start Month | `RentYearStartMonth` | `sTYPE_MONTH` | Global | No | No |  | Contract / Use Based Rent |
| Reporting Frequency | `CodeReportingFrequencyID` | `sCODE_FREQUENCY` | Global | No | No |  | Contract / Use Based Rent |
| Usage Group | `CodeUsageGroupID` | `sCODE_USAGE_GROUP` | Global | No | No |  | Contract / Use Based Rent |
| Usage Unit Type | `CodeUsageUnitTypeID` | `sCODE_USAGE_UNIT_TYPE` | Global | No | No |  | Contract / Use Based Rent |
| Use Based Rent ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Use Based Rent |
| Use Based Rent RecID | `UseBasedRentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Use Based Rent |
