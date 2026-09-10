# InvoiceItem — Data Fields

Line-item detail under an InvoiceIssue batch — GL number and invoice amount per line. 17 Global fields under Specialized Forms.

**Table Association:** `InvoiceItem` &nbsp;·&nbsp; **Total fields:** 17 (Global: 17, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Invoice Items |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Invoice Items |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Invoice Items |
| GL Number | `GLNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Invoice Items |
| Invoice Amount | `InvoiceAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Specialized Forms / Invoice Items |
| Invoice Issue | `InvoiceIssueID` | `sTYPE_INVOICE_ISSUE` | Global | Yes | No |  | Specialized Forms / Invoice Items |
| Invoice Item ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Invoice Items |
| Invoice Item RecID | `InvoiceItemID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Invoice Items |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Invoice Items |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Invoice Items |
| Quantity | `Quantity` | `sTYPE_NUMBER` | Global | No | No |  | Specialized Forms / Invoice Items |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Invoice Items |
| Sub Account | `SubAccount` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Invoice Items |
| Tax Amount #1 | `TaxAmount1` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Invoice Items |
| Tax Amount #2 | `TaxAmount2` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Invoice Items |
| Total Amount | `TotalAmount` | `sTYPE_MONEY_MATH_OPERATION` | Global | No | No |  | Specialized Forms / Invoice Items |
| Unit Cost | `UnitCost` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Invoice Items |
