# LandlordInvoiceItem

*28 fields · module: Lease Accounting & Payments · Postgres: `landlord_invoice_item`*

Line-item detail under a LandlordInvoice — allocated vs. unallocated amount and comments per line. 28 Global fields under Contract.

Source: `data-fields/landlord-invoice-item.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Fields with a vendor definition | 0 of 28 inventoried |
| Physical tables | `landlord_invoice_item` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 28 (28 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in landlord_invoice_item

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required-ness: 2 disagree of 28 comparable

**Observed.** Over the 28 fields both captures contain, they agree on 26. The exceptions are ContractID, ProjectEntityID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-133](../rules/CON-R-133.md) | Migrating LandlordInvoiceItem: money, date and boolean are all stored as text on this reconciliation grid; replace the seven PayTrans* mirror fields with a join. | Observed |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract |  | Contract ID | Global | yes | `landlord_invoice_item.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` | Project Entity |  | Entity ID | Global | yes | `landlord_invoice_item.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeExpenseCategoryID` | Expense Category |  | Dropdown (Expense Category Code) | Global |  | `landlord_invoice_item.CodeExpenseCategoryID · TEXT` | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group |  | Dropdown (Expense Group Code) | Global |  | `landlord_invoice_item.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type |  | Dropdown (Expense Type Code) | Global |  | `landlord_invoice_item.CodeExpenseTypeID · TEXT` | Expense Type Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmountNotAllocated` | Amount Not Allocated |  | Currency | Global |  | `landlord_invoice_item.AmountNotAllocated · TEXT` |  |
| `LineItemAmount` | Line Item Amount |  | Currency | Global | yes | `landlord_invoice_item.LineItemAmount · TEXT` |  |
| `TaxAmount` | Tax Amount |  | Currency | Global |  | `landlord_invoice_item.TaxAmount · TEXT` |  |
| `TotalAmount` | Total Amount |  | Currency | Global | yes | `landlord_invoice_item.TotalAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TaxRate` | Tax Rate |  | Percentage | Global |  | `landlord_invoice_item.TaxRate · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SequenceNumber` | Sequence Number |  | Number | Global |  | `landlord_invoice_item.SequenceNumber · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ItemDate` | Item Date |  | Date | Global |  | `landlord_invoice_item.ItemDate · TEXT` |  |

### Text & notes (12)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Comments` |  |  | Text | Global |  | `landlord_invoice_item.Comments · TEXT` |  |
| `LandlordInvoiceID` | Landlord Invoice |  | Text | Global | yes | `landlord_invoice_item.LandlordInvoiceID · TEXT` |  |
| `LineItemDescription` | Line Item Description |  | Text | Global |  | `landlord_invoice_item.LineItemDescription · TEXT` |  |
| `LinkAmountAllocated` | Amount Allocated |  | Text | Global |  | `landlord_invoice_item.LinkAmountAllocated · TEXT` |  |
| `PayTransCategory` | Payment Transaction Expense Category |  | Text | Global |  | `landlord_invoice_item.PayTransCategory · TEXT` |  |
| `PayTransEffectiveDate` | Payment Transaction Effective Date |  | Text | Global |  | `landlord_invoice_item.PayTransEffectiveDate · TEXT` |  |
| `PayTransExpenseGroup` | Payment Transaction Expense Group |  | Text | Global |  | `landlord_invoice_item.PayTransExpenseGroup · TEXT` |  |
| `PayTransExpenseType` | Payment Transaction Expense Type |  | Text | Global |  | `landlord_invoice_item.PayTransExpenseType · TEXT` |  |
| `PayTransIsReceivable` | Payment Transaction Is Receivable |  | Text | Global |  | `landlord_invoice_item.PayTransIsReceivable · TEXT` |  |
| `PayTransTotalAmount` | Payment Transaction Total Amount |  | Text | Global |  | `landlord_invoice_item.PayTransTotalAmount · TEXT` |  |
| `PayTransVendor` | Payment Transaction Vendor |  | Text | Global |  | `landlord_invoice_item.PayTransVendor · TEXT` |  |
| `RemitMessage` | Remit Message |  | Text | Global |  | `landlord_invoice_item.RemitMessage · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By |  | Member ID | Global |  | `landlord_invoice_item.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date |  | Time | Global |  | `landlord_invoice_item.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `landlord_invoice_item.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `landlord_invoice_item.ModifiedDate · TEXT` |  |
