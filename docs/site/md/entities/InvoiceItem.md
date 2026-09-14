# InvoiceItem

*18 fields · module: Lease Accounting & Payments · Postgres: `invoice_item`*

Line-item detail under an InvoiceIssue batch — GL number and invoice amount per line. 17 Global fields under Specialized Forms.

Source: `data-fields/invoice-item.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 18 |
| Catalogued fields | 17 (17 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Money (5)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `InvoiceAmount` | Invoice Amount | Currency | Global |  |  |
| `TaxAmount1` | Tax Amount #1 | Currency | Global |  |  |
| `TaxAmount2` | Tax Amount #2 | Currency | Global |  |  |
| `TotalAmount` | Total Amount | Currency | Global |  |  |
| `UnitCost` | Unit Cost | Currency | Global |  |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `InvoiceItemID` | Invoice Item RecID | Number | Global |  |  |
| `Quantity` |  | Number | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `GLNumber` | GL Number | Text | Global |  |  |
| `InvoiceIssueID` | Invoice Issue | Text | Global | yes |  |
| `SubAccount` | Sub Account | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Invoice Item ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
