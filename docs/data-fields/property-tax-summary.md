# PropertyTaxSummary — Data Fields

The rollup of assessment amount/percent and billing frequency for a Parcel's property tax obligation across bills and appeals. 31 Global fields under Parcel.

**Table Association:** `PropertyTaxSummary` &nbsp;·&nbsp; **Total fields:** 31 (Global: 31, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Assessment Amount | `AssessmentAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Summary |
| Assessment Percent | `AssessmentPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Summary |
| Billing Frequency | `CodeBillingFrequencyID` | `sCODE_FREQUENCY` | Global | No | No |  | Parcel / Property Tax Summary |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Summary |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Summary |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Parcel / Property Tax Summary |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Property Tax Summary |
| Estimated Accrual Amount | `EstimatedAccrualAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Summary |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Parcel / Property Tax Summary |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Parcel / Property Tax Summary |
| Mill Rate | `MillRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Summary |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Summary |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Summary |
| Net Tax Amount | `NetTaxAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Summary |
| Net Tax Percent | `NetTaxPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Summary |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Property Tax Summary |
| Parcel | `ParcelID` | `sTYPE_PARCEL` | Global | Yes | No |  | Parcel / Property Tax Summary |
| Payment Frequency | `CodePaymentFrequencyID` | `sCODE_FREQUENCY` | Global | No | No |  | Parcel / Property Tax Summary |
| Property Tax Summary ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Parcel / Property Tax Summary |
| Property Tax Summary RecID | `PropertyTaxSummaryID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Summary |
| Property Tax Type | `CodePropertyTaxTypeID` | `sCODE_PROPERTY_TAX_TYPE` | Global | No | No |  | Parcel / Property Tax Summary |
| Rate Per | `RatePer` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Summary |
| Recovery Group | `CodeRecoveryGroupID` | `sCODE_RECOVERY_GROUP` | Global | No | No |  | Parcel / Property Tax Summary |
| Recovery Type | `CodeRecoveryTypeID` | `sCODE_RECOVERY_TYPE` | Global | No | No |  | Parcel / Property Tax Summary |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Summary |
| Right To Appeal? | `RightToAppeal` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Property Tax Summary |
| Tax Account Number | `TaxAccountNumber` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Property Tax Summary |
| Tax Authority | `TaxAuthorityID` | `sTYPE_VENDOR` | Global | No | No |  | Parcel / Property Tax Summary |
| Tax Rate Per | `TaxRatePer` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Summary |
| Tickler Date | `TicklerDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Summary |
| Vendor | `VendorID` | `sTYPE_EMPLOYER` | Global | No | No |  | Parcel / Property Tax Summary |
