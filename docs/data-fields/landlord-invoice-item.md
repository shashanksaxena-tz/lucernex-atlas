# LandlordInvoiceItem — Data Fields

Line-item detail under a LandlordInvoice — allocated vs. unallocated amount and comments per line. 28 Global fields under Contract.

**Table Association:** `LandlordInvoiceItem` &nbsp;·&nbsp; **Total fields:** 28 (Global: 28, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amount Allocated | `LinkAmountAllocated` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Amount Not Allocated | `AmountNotAllocated` | `sTYPE_MONEY` | Global | No | No |  | Contract / Landlord Invoice Item |
| Comments | `Comments` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Landlord Invoice Item |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Landlord Invoice Item |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Landlord Invoice Item |
| Expense Category | `CodeExpenseCategoryID` | `sCODE_EXPENSE_CATEGORY` | Global | No | No |  | Contract / Landlord Invoice Item |
| Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Landlord Invoice Item |
| Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Landlord Invoice Item |
| Item Date | `ItemDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Landlord Invoice Item |
| Landlord Invoice | `LandlordInvoiceID` | `sTYPE_LANDLORD_INVOICE` | Global | Yes | No |  | Contract / Landlord Invoice Item |
| Line Item Amount | `LineItemAmount` | `sTYPE_MONEY` | Global | Yes | No |  | Contract / Landlord Invoice Item |
| Line Item Description | `LineItemDescription` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Landlord Invoice Item |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Landlord Invoice Item |
| Payment Transaction Effective Date | `PayTransEffectiveDate` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Payment Transaction Expense Category | `PayTransCategory` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Payment Transaction Expense Group | `PayTransExpenseGroup` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Payment Transaction Expense Type | `PayTransExpenseType` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Payment Transaction Is Receivable | `PayTransIsReceivable` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Payment Transaction Total Amount | `PayTransTotalAmount` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Payment Transaction Vendor | `PayTransVendor` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Project Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Contract / Landlord Invoice Item |
| Remit Message | `RemitMessage` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Item |
| Sequence Number | `SequenceNumber` | `sTYPE_NUMBER` | Global | No | No |  | Contract / Landlord Invoice Item |
| Tax Amount | `TaxAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Landlord Invoice Item |
| Tax Rate | `TaxRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Landlord Invoice Item |
| Total Amount | `TotalAmount` | `sTYPE_MONEY` | Global | Yes | No |  | Contract / Landlord Invoice Item |
