# PropertyTaxAppealAward — Data Fields

The financial outcome of a PropertyTaxAppeal — actual/estimated award date and award/award-fee amount. 17 Global fields under Parcel.

**Table Association:** `PropertyTaxAppealAward` &nbsp;·&nbsp; **Total fields:** 17 (Global: 17, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Actual Award Date | `ActualAwardDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Award Amount | `AwardAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Award Fee Amount | `AwardFeeAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Estimated Award Date | `EstimatedAwardDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Parcel | `ParcelID` | `sTYPE_PARCEL` | Global | Yes | No |  | Parcel / Property Tax Appeal Award |
| Property Tax Appeal | `PropertyTaxAppealID` | `sTYPE_PROPERTY_TAX_APPEAL` | Global | Yes | No |  | Parcel / Property Tax Appeal Award |
| Property Tax Appeal Award ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Parcel / Property Tax Appeal Award |
| Property Tax Appeal Award RecID | `PropertyTaxAppealAwardID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Tax Paid To | `CodeTaxPaidToID` | `sCODE_TAX_PAID_TO` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Tax Refund Type | `CodeTaxRefundTypeID` | `sCODE_TAX_REFUND_TYPE` | Global | No | No |  | Parcel / Property Tax Appeal Award |
| Vendor | `VendorID` | `sTYPE_EMPLOYER` | Global | No | No |  | Parcel / Property Tax Appeal Award |
