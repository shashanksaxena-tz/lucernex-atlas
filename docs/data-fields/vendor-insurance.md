# VendorInsurance — Data Fields

The actual insurance policy detail for a vendor/employer (as opposed to Insurance, which is the lease's required-coverage terms) — aggregate occurrence amount and policy type/dates. 15 Global fields under Company Items.

**Table Association:** `VendorInsurance` &nbsp;·&nbsp; **Total fields:** 15 (Global: 15, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Aggregate Occurrence Amt | `AggregateOccurrenceAmt` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Vendor Insurance |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Vendor Insurance |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Vendor Insurance |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Vendor Insurance |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Vendor Insurance |
| Insurance Policy Type | `CodeInsurancePolicyTypeID` | `sCODE_INSURANCE_POLICY_TYPE` | Global | No | No |  | Company Items / Vendor Insurance |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Vendor Insurance |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Vendor Insurance |
| Policy | `Policy` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Vendor Insurance |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Vendor Insurance |
| Single Occurrence Amt | `SingleOccurrenceAmt` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Vendor Insurance |
| Vendor | `VendorID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Company Items / Vendor Insurance |
| Vendor Insurance ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Vendor Insurance |
| Vendor Insurance RecID | `VendorInsuranceID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Vendor Insurance |
| Verified Date | `VerifiedDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Vendor Insurance |
