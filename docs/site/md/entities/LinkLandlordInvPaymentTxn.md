# LinkLandlordInvPaymentTxn

*13 fields · module: Lease Accounting & Payments · Postgres: `link_landlord_inv_payment_txn`*

Join table linking a LandlordInvoiceItem to the PaymentTransaction that paid it — allocation amount and date.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Fields with a vendor definition | 0 of 13 inventoried |
| Physical tables | `link_landlord_inv_payment_txn` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_landlord_inv_payment_txn

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required: the two captures disagree

**Observed.** The field inventory marks 5 of this record's fields required; the Data Fields catalogue marks 6; 5 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-115](../rules/CON-R-115.md) | An invoice line is matched to a payment: LinkLandlordInvPaymentTxn allocates AllocationAmount/AllocationDate between LandlordInvoiceItemID and PaymentTransactionID. | Observed |
| [CON-R-116](../rules/CON-R-116.md) | A match has a difference: VarianceAmount and VarianceReason are stored on the join itself, alongside ReconciliationStatus. | Observed |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PaymentTransactionID` | Payment Transaction |  | Payment Transaction ID | Global | yes | `link_landlord_inv_payment_txn.PaymentTransactionID · TEXT` | [PaymentTransaction](PaymentTransaction.md) |
| `ProjectEntityID` | Project Entity |  | Entity ID | Global | yes | `link_landlord_inv_payment_txn.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllocationAmount` | Allocation Amount |  | Currency | Global | yes | `link_landlord_inv_payment_txn.AllocationAmount · TEXT` |  |
| `VarianceAmount` | Variance Amount |  | Currency | Global |  | `link_landlord_inv_payment_txn.VarianceAmount · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllocationDate` | Allocation Date |  | Date | Global | yes | `link_landlord_inv_payment_txn.AllocationDate · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LandlordInvoiceItemID` | Landlord Invoice Item |  | Text | Global | yes | `link_landlord_inv_payment_txn.LandlordInvoiceItemID · TEXT` |  |
| `Notes` |  |  | Text | Global |  | `link_landlord_inv_payment_txn.Notes · TEXT` |  |
| `ReconciliationStatus` | Reconciliation Status |  | Text | Global | yes | `link_landlord_inv_payment_txn.ReconciliationStatus · TEXT` |  |
| `VarianceReason` | Variance Reason |  | Text | Global |  | `link_landlord_inv_payment_txn.VarianceReason · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By |  | Member ID | Global |  | `link_landlord_inv_payment_txn.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date |  | Time | Global |  | `link_landlord_inv_payment_txn.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `link_landlord_inv_payment_txn.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `link_landlord_inv_payment_txn.ModifiedDate · TEXT` |  |
