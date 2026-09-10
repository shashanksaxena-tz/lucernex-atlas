# PercentageRent — Data Fields

The percentage/sales-based rent clause on a retail lease — cap amount/frequency, audit-right flag, and billing frequency, linked to Covenant for cross-referencing compliance obligations tied to the same clause. 44 fields (41 Global, 3 Firm) under Contract; it is the clause-level configuration that VirtualSalesPeriod and PercentageRentBreakpoint project forward from.

**Table Association:** `PercentageRent` &nbsp;·&nbsp; **Total fields:** 44 (Global: 41, Firm: 3)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Percentage Rent |
| Annual Report Due Days | `AnnualReportDueDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Percentage Rent |
| Annualize Rent | `AnnualizeRent` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
| Audit Right? | `AuditRightFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Percentage Rent |
| Billing Frequency | `CodeBillingFrequencyID` | `sCODE_PR_FREQUENCY` | Global | No | No |  | Contract / Percentage Rent |
| Cap Amount | `CapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Percentage Rent |
| Cap Frequency | `CodeCapFrequencyID` | `sCODE_MONTH_FREQUENCY` | Global | No | No |  | Contract / Percentage Rent |
| Certified Sales | `Firm_CertifiedSales` | `sTYPE_CHECKBOX` | Firm | No | No |  | Contract / Percentage Rent |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Percentage Rent |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Percentage Rent |
| Cumulative? | `CumulativeFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Percentage Rent |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Percentage Rent |
| Document | `Firm_PercentRentDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Percentage Rent |
| Due Date | `DueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Percentage Rent |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Percentage Rent |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Percentage Rent |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Percentage Rent |
| Extend Final Period to Lease Expiration Date | `ExtFinalPeriodToLeaseExpDt` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
| Floor Amount | `FloorAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Percentage Rent |
| Is Mid Month? | `IsMidMonth` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
| Is Partial Term? | `IsPartialTerm` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
| Last Payment Due Offset Days | `AnnualPaymentDueDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Percentage Rent |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Percentage Rent |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Percentage Rent |
| Natural Breakpoint? | `NaturalBreakpointFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Percentage Rent |
| Offset Amount | `OffsetAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Percentage Rent |
| Page | `Firm_PercentRentPage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Percentage Rent |
| Percentage Rent ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Percentage Rent |
| Percentage Rent RecID | `PercentageRentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Percentage Rent |
| Percentage Rent Type | `CodePercentageRentTypeID` | `sCODE_PERCENTAGE_RENT_TYPE` | Global | No | No |  | Contract / Percentage Rent |
| Period Payment Due Offset Days | `PeriodPaymentDueDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Percentage Rent |
| Period Report Due Days | `PeriodReportDueDays` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Percentage Rent |
| Proration Method | `CodeProrationMethodID` | `sCODE_PRORATION_METHOD` | Global | No | No |  | Contract / Percentage Rent |
| Rent Year Start Month | `RentYearStartMonth` | `sTYPE_MONTH` | Global | No | No |  | Contract / Percentage Rent |
| Reporting Frequency | `CodeReportingFrequencyID` | `sCODE_PR_FREQUENCY` | Global | No | No |  | Contract / Percentage Rent |
| Sales Group | `CodeSalesGroupID` | `sCODE_SALES_GROUP` | Global | No | No |  | Contract / Percentage Rent |
| Sales Year End Date | `SalesYearEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Percentage Rent |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Percentage Rent |
| Store Type | `CodeStoreTypeID` | `sCODE_STORE_TYPE` | Global | No | No |  | Contract / Percentage Rent |
| Use Count Based Rate? | `UseCountBasedRate` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
| Use Trailing #12 Month Sales? | `UseTrailing12MonthSales` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Percentage Rent |
