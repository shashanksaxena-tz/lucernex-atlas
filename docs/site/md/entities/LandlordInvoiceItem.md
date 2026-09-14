# LandlordInvoiceItem

*28 fields · module: Lease Accounting & Payments · Postgres: `landlord_invoice_item`*

Line-item detail under a LandlordInvoice — allocated vs. unallocated amount and comments per line. 28 Global fields under Contract.

Source: `data-fields/landlord-invoice-item.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Catalogued fields | 28 (28 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-133](../rules/CON-R-133.md) | Migrating LandlordInvoiceItem: money, date and boolean are all stored as text on this reconciliation grid; replace the seven PayTrans* mirror fields with a join. | Observed |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` | Project Entity | Entity ID | Global | yes | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | Global |  | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |

### Money (4)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmountNotAllocated` | Amount Not Allocated | Currency | Global |  |  |
| `LineItemAmount` | Line Item Amount | Currency | Global | yes |  |
| `TaxAmount` | Tax Amount | Currency | Global |  |  |
| `TotalAmount` | Total Amount | Currency | Global | yes |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TaxRate` | Tax Rate | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SequenceNumber` | Sequence Number | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ItemDate` | Item Date | Date | Global |  |  |

### Text & notes (12)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Comments` |  | Text | Global |  |  |
| `LandlordInvoiceID` | Landlord Invoice | Text | Global | yes |  |
| `LineItemDescription` | Line Item Description | Text | Global |  |  |
| `LinkAmountAllocated` | Amount Allocated | Text | Global |  |  |
| `PayTransCategory` | Payment Transaction Expense Category | Text | Global |  |  |
| `PayTransEffectiveDate` | Payment Transaction Effective Date | Text | Global |  |  |
| `PayTransExpenseGroup` | Payment Transaction Expense Group | Text | Global |  |  |
| `PayTransExpenseType` | Payment Transaction Expense Type | Text | Global |  |  |
| `PayTransIsReceivable` | Payment Transaction Is Receivable | Text | Global |  |  |
| `PayTransTotalAmount` | Payment Transaction Total Amount | Text | Global |  |  |
| `PayTransVendor` | Payment Transaction Vendor | Text | Global |  |  |
| `RemitMessage` | Remit Message | Text | Global |  |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
