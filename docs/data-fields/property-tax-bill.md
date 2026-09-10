# PropertyTaxBill — Data Fields

A property tax bill issued against a Parcel — discount amount/date/rate for early-payment discounts, feeding into PropertyTaxSummary. 31 Global fields under Parcel.

**Table Association:** `PropertyTaxBill` &nbsp;·&nbsp; **Total fields:** 31 (Global: 31, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Auto Calc? | `AutoCalcFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Property Tax Bill |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Bill |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Bill |
| Discount Amount | `DiscountAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Bill |
| Discount Date | `DiscountDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Bill |
| Discount Rate | `DiscountRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Bill |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Bill |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Bill |
| Equalization Factor | `EqualizationFactor` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Bill |
| Equalization Value | `EqualizationValue` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Bill |
| Hold? | `HoldFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Property Tax Bill |
| Invoice Date | `InvoiceDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Bill |
| Invoice Number | `InvoiceNumber` | `sTYPE_TEXT` | Global | No | No |  | Parcel / Property Tax Bill |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Parcel / Property Tax Bill |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Parcel / Property Tax Bill |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Parcel / Property Tax Bill |
| Parcel | `ParcelID` | `sTYPE_PARCEL` | Global | Yes | No |  | Parcel / Property Tax Bill |
| Payment Due Date | `PaymentDueDate` | `sTYPE_DATE` | Global | No | No |  | Parcel / Property Tax Bill |
| Processed? | `ProcessedFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Parcel / Property Tax Bill |
| Property Tax Assessment | `PropertyTaxAssessmentID` | `sTYPE_PROPERTY_TAX_ASSESSMENT` | Global | Yes | No |  | Parcel / Property Tax Bill |
| Property Tax Bill ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Parcel / Property Tax Bill |
| Property Tax Bill RecID | `PropertyTaxBillID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Bill |
| Property Tax Status | `CodePropertyTaxStatusID` | `sCODE_PROPERTY_TAX_STATUS` | Global | No | No |  | Parcel / Property Tax Bill |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Parcel / Property Tax Bill |
| Tax Adjustment Amount | `TaxAdjustmentAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Bill |
| Tax Balance Due | `TaxBalanceDue` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Bill |
| Tax Mill Rate | `TaxMillRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Bill |
| Tax Net Amount | `TaxNetAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Bill |
| Tax Prior Paid Amount | `TaxPriorPaidAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Bill |
| Tax Rate | `TaxRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Parcel / Property Tax Bill |
| Tax Total Amount | `TaxTotalAmount` | `sTYPE_MONEY` | Global | No | No |  | Parcel / Property Tax Bill |
