# ParcelAccess

*20 fields · module: Facilities, Locations & Sites · Postgres: `parcel_access`*

An access easement or right-of-way record on a Parcel — effective/expire date and associated document. 19 Global fields under Parcel.

Source: `data-fields/parcel-access.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Catalogued fields | 19 (19 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssociatedDocumentID` | Associated Document | Document ID | Global |  | [Document](Document.md) |
| `FolderID` | Folder | Folder ID | Global |  | [Folder](Folder.md) |
| `ParcelID` | Parcel | Parcel ID | Global | yes | [Parcel](Parcel.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeParcelAccessCategoryID` | Parcel Access Category | Dropdown (Parcel Access Category Code) | Global |  | Parcel Access Category Code |
| `CodeParcelAccessGroupID` | Parcel Access Group | Dropdown (Parcel Access Group Code) | Global |  | Parcel Access Group Code |
| `CodeParcelAccessTypeID` | Parcel Access Type | Dropdown (Parcel Access Type Code) | Global |  | Parcel Access Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ParcelAccessID` | Parcel Access RecID | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `ExpireDate` | Expire Date | Date | Global |  |  |
| `TicklerDate` | Tickler Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExistsFlag` | Exists? | Boolean | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseName` | File Name | Text | Global |  |  |
| `LineNumber` | Line Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PageNumber` | Page Number | Text | Global |  |  |
| `ParagraphNumber` | Paragraph Number | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Parcel Access ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
