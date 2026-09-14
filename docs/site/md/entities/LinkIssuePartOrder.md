# LinkIssuePartOrder

*16 fields · module: Capital Projects & Scheduling · Postgres: `link_issue_part_order`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 16 declared fields, filed under Capital Projects & Scheduling, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 15 of its 16 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Fields with a vendor definition | 15 of 16 inventoried |
| Physical tables | `link_issue_part_order` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_issue_part_order

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 15 fields carry a vendor definition

**Observed.** 15 of this record's 16 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 6 of this record's fields required; the Data Fields catalogue marks 0; 0 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-009](../rules/PRJ-R-009.md) | A part is consumed or ordered against a work-order `Issue` · `LinkIssuePart` (cost, labor hours, serial number) vs. `LinkIssuePartOrder` (quantity ordered/received, `CodePartOrderStatusID`) · Two distinct records — one for parts actually us | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `link_issue_part_order.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `VendorID` | Vendor | The vendor ID of the vendor who provided the parts for the order. | Employer ID | — |  | `link_issue_part_order.VendorID · TEXT` | [Employer](Employer.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PartID` | Part Name | The ID of the part. | Part | — |  | `link_issue_part_order.PartID · TEXT` |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAssetCategoryID` | Maintenance Category | The maintenance category of the part. | Dropdown (Asset Category Code) | — |  | `link_issue_part_order.CodeAssetCategoryID · TEXT` | Asset Category Code |
| `CodePartOrderStatusID` | Status | The status of the part order. | Dropdown (Part Order Status Code) | — | yes | `link_issue_part_order.CodePartOrderStatusID · TEXT` | Part Order Status Code |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkIssuePartOrderID` | Part Order RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | `link_issue_part_order.LinkIssuePartOrderID · VARCHAR(64) NOT NULL` |  |
| `QuantityOrdered` | Quantity Ordered | The quantity of parts ordered. | Number | — | yes | `link_issue_part_order.QuantityOrdered · TEXT` |  |
| `QuantityReceived` | Quantity Received | The quantity of parts received. | Number | — | yes | `link_issue_part_order.QuantityReceived · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `NeedByDate` | Need By Date | The date the part is needed by. | Date | — | yes | `link_issue_part_order.NeedByDate · TEXT` |  |
| `ReceivedDate` | Receipt Date | The receipt date for the parts order. | Date | — |  | `link_issue_part_order.ReceivedDate · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IssueID` | Issue | The ID of the form associated with the order. | Text | — | yes | `link_issue_part_order.IssueID · TEXT` |  |
| `LinkPartCategoryID` | Link Part Category | The category of the part. | Text | — | yes | `link_issue_part_order.LinkPartCategoryID · TEXT` |  |
| `ModelNumber` | Part # Ordered | The model number of the part. | Text | — |  | `link_issue_part_order.ModelNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | — |  | `link_issue_part_order.Notes · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `link_issue_part_order.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `link_issue_part_order.ModifiedDate · TEXT` |  |
