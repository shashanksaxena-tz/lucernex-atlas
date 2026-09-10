# LandlordInvoice — Data Fields

An invoice received from a landlord for billing outside the standard recovery/rent cycle — coverage period and allocation-status amounts, anchoring LandlordInvoiceItem as its line-item detail. 31 Global fields under Contract.

**Table Association:** `LandlordInvoice` &nbsp;·&nbsp; **Total fields:** 31 (Global: 31, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amount Allocated | `AmountAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Landlord Invoice |
| Amount Not Allocated | `AmountNotAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Landlord Invoice |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Landlord Invoice |
| Coverage Begin Date | `ServicePeriodStartDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Landlord Invoice |
| Coverage End Date | `ServicePeriodEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Landlord Invoice |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Landlord Invoice |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Landlord Invoice |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Landlord Invoice |
| Customer Address | `CustomerAddress` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Customer Address Recipient | `CustomerAddressRecipient` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Customer Name | `CustomerName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Customer Tax ID | `CustomerTaxID` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| CustomerID | `CustomerID` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Document | `AssociatedDocumentID` | `sTYPE_DOCUMENT` | Global | No | No |  | Contract / Landlord Invoice |
| Due Date | `DueDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Landlord Invoice |
| Folder | `FolderID` | `sTYPE_DOCUMENT` | Global | No | No |  | Contract / Landlord Invoice |
| Invoice Date | `InvoiceDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Landlord Invoice |
| Invoice Number | `InvoiceNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Invoice Total | `InvoiceTotal` | `sTYPE_MONEY` | Global | No | No |  | Contract / Landlord Invoice |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Landlord Invoice |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Landlord Invoice |
| Notes | `Notes` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Payment Term | `PaymentTerm` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Project Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Contract / Landlord Invoice |
| Sub Total | `SubTotal` | `sTYPE_MONEY` | Global | No | No |  | Contract / Landlord Invoice |
| Total Tax | `TotalTax` | `sTYPE_MONEY` | Global | No | No |  | Contract / Landlord Invoice |
| Vendor | `EmployerID` | `sTYPE_EMPLOYER` | Global | No | No |  | Contract / Landlord Invoice |
| Vendor Address | `VendorAddress` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Vendor Address Recipient | `VendorAddressRecipient` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Vendor Name | `VendorName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
| Vendor Tax ID | `VendorTaxID` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice |
