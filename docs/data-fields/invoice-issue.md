# InvoiceIssue — Data Fields

An invoice batch header for accounts-payable processing — batch date/number and currency type, anchoring InvoiceItem as line-level detail. 22 Global fields under Specialized Forms.

**Table Association:** `InvoiceIssue` &nbsp;·&nbsp; **Total fields:** 22 (Global: 22, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Batch Date | `BatchDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Invoices |
| Batch Number | `BatchNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Invoices |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Invoices |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Invoices |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Specialized Forms / Invoices |
| Invoice Amount | `InvoiceAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Invoices |
| Invoice ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Invoices |
| Invoice Date | `InvoiceDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Invoices |
| Invoice Issue | `IssueID` | `sTYPE_ISSUE` | Global | Yes | No |  | Specialized Forms / Invoices |
| Invoice Number | `InvoiceNumber` | `sTYPE_TEXT` | Global | No | No |  | Specialized Forms / Invoices |
| Invoice RecID | `InvoiceIssueID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Invoices |
| Invoice Status | `CodeInvoiceStatusID` | `sCODE_INVOICE_STATUS` | Global | No | No |  | Specialized Forms / Invoices |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Specialized Forms / Invoices |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Specialized Forms / Invoices |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Specialized Forms / Invoices |
| Number | `SequenceNumber` | `sTYPE_TEXT` | Global | Yes | No |  | Specialized Forms / Invoices |
| Paid Date | `PaidDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Invoices |
| Received Date | `ReceivedDate` | `sTYPE_DATE` | Global | No | No |  | Specialized Forms / Invoices |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Specialized Forms / Invoices |
| Tax Amount #1 | `TaxAmount1` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Invoices |
| Tax Amount #2 | `TaxAmount2` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Invoices |
| Total Amount | `TotalAmount` | `sTYPE_MONEY` | Global | No | No |  | Specialized Forms / Invoices |
