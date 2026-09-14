# LinkIssuePartOrder

*16 fields · module: Capital Projects & Scheduling · Postgres: `link_issue_part_order`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 16 declared fields, filed under Capital Projects & Scheduling, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 16 |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-009](../rules/PRJ-R-009.md) | A part is consumed or ordered against a work-order `Issue` · `LinkIssuePart` (cost, labor hours, serial number) vs. `LinkIssuePartOrder` (quantity ordered/received, `CodePartOrderStatusID`) · Two distinct records — one for parts actually us | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `VendorID` |  | Employer ID | — |  | [Employer](Employer.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PartID` |  | Part | — |  |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAssetCategoryID` |  | Dropdown (Asset Category Code) | — |  | Asset Category Code |
| `CodePartOrderStatusID` |  | Dropdown (Part Order Status Code) | — |  | Part Order Status Code |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LinkIssuePartOrderID` |  | Number | — |  |  |
| `QuantityOrdered` |  | Number | — |  |  |
| `QuantityReceived` |  | Number | — |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `NeedByDate` |  | Date | — |  |  |
| `ReceivedDate` |  | Date | — |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IssueID` |  | Text | — |  |  |
| `LinkPartCategoryID` |  | Text | — |  |  |
| `ModelNumber` |  | Text | — |  |  |
| `Notes` |  | Text | — |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
