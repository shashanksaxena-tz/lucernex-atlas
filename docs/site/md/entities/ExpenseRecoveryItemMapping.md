# ExpenseRecoveryItemMapping

*6 fields · module: Expense Recovery (CAM / Reconciliation) · Postgres: `expense_recovery_item_mapping`*

Maps an ExpenseRecoveryItem to an external invoice line item name and a JSON configuration blob, likely supporting invoice-import matching.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 6 |
| Fields with a vendor definition | 5 of 6 inventoried |
| Physical tables | `expense_recovery_item_mapping` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 5 (5 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in expense_recovery_item_mapping

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 5 fields carry a vendor definition

**Observed.** 5 of this record's 6 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 3; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-102](../rules/CON-R-102.md) | A landlord statement is ingested: ExpenseRecoveryItemMapping maps a free-text statement line (InvoiceLineItemName, JSONConfigText) to a structured recovery item. | Inferred |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `expense_recovery_item_mapping.ContractID · TEXT` | [Contract](Contract.md) |
| `DocumentID` | Document | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Document ID | Global | yes | `expense_recovery_item_mapping.DocumentID · TEXT` | [Document](Document.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `expense_recovery_item_mapping.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExpenseRecoveryItemID` | Expense Recovery Item | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Text | Global | yes | `expense_recovery_item_mapping.ExpenseRecoveryItemID · TEXT` |  |
| `InvoiceLineItemName` | Invoice Line Item Name | The name of the invoice line item that was extracted from the document you analyzed in the Invoice Import tool. | Text | Global |  | `expense_recovery_item_mapping.InvoiceLineItemName · TEXT` |  |
| `JSONConfigText` | JSON Config | This is an internal field that will be used for a future enhancement. | Text | Global |  | `expense_recovery_item_mapping.JSONConfigText · TEXT` |  |
