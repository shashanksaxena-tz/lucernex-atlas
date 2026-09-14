# ParcelAccess

*20 fields · module: Facilities, Locations & Sites · Postgres: `parcel_access`*

An access easement or right-of-way record on a Parcel — effective/expire date and associated document. 19 Global fields under Parcel.

Source: `data-fields/parcel-access.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Fields with a vendor definition | 19 of 20 inventoried |
| Physical tables | `parcel_access` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 19 (19 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in parcel_access

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 19 fields carry a vendor definition

**Observed.** 19 of this record's 20 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 2 fields marked required

**Observed.** The inventory marks 2 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssociatedDocumentID` | Associated Document | The ID of a document associated with this record. | Document ID | Global |  | `parcel_access.AssociatedDocumentID · TEXT` | [Document](Document.md) |
| `FolderID` | Folder | The folder ID of the document connected to the parcel access record. | Folder ID | Global |  | `parcel_access.FolderID · TEXT` | [Folder](Folder.md) |
| `ParcelID` | Parcel | The parcel ID that this parcel access record is associated with. | Parcel ID | Global | yes | `parcel_access.ParcelID · TEXT` | [Parcel](Parcel.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `parcel_access.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeParcelAccessCategoryID` | Parcel Access Category | Select the parcel access category from this field. | Dropdown (Parcel Access Category Code) | Global |  | `parcel_access.CodeParcelAccessCategoryID · TEXT` | Parcel Access Category Code |
| `CodeParcelAccessGroupID` | Parcel Access Group | Select the parcel access group from this field. | Dropdown (Parcel Access Group Code) | Global |  | `parcel_access.CodeParcelAccessGroupID · TEXT` | Parcel Access Group Code |
| `CodeParcelAccessTypeID` | Parcel Access Type | Select the parcel access type from this field. | Dropdown (Parcel Access Type Code) | Global |  | `parcel_access.CodeParcelAccessTypeID · TEXT` | Parcel Access Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ParcelAccessID` | Parcel Access RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `parcel_access.ParcelAccessID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the parcel access record. | Date | Global |  | `parcel_access.EffectiveDate · TEXT` |  |
| `ExpireDate` | Expire Date | Enter the expiration date of the parcel access record. Often times easements will only be valid for a certain period of time. Enter the expiration date in this field. | Date | Global |  | `parcel_access.ExpireDate · TEXT` |  |
| `TicklerDate` | Tickler Date | A Tickler Date is used in reporting to give notice that the expiration date is approaching. If your company uses tickler dates, enter the date in this field. There is no associated functionality with this field. | Date | Global |  | `parcel_access.TicklerDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExistsFlag` | Exists? | Some clients will pre-load a standard set of easements into Lx for all of their parcels. If your company has done this, select this check box if this easement exists for this parcel. | Boolean | Global |  | `parcel_access.ExistsFlag · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseName` | File Name | This field displays the file name of the file attached to the record. | Text | Global |  | `parcel_access.BaseName · TEXT` |  |
| `LineNumber` | Line Number | Enter the relevant line number in the document. | Text | Global |  | `parcel_access.LineNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `parcel_access.Notes · TEXT` |  |
| `PageNumber` | Page Number | Enter the relevant page number in this field. | Text | Global |  | `parcel_access.PageNumber · TEXT` |  |
| `ParagraphNumber` | Paragraph Number | Enter the relevant paragraph number. | Text | Global |  | `parcel_access.ParagraphNumber · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Parcel Access ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `parcel_access.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `parcel_access.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `parcel_access.ModifiedDate · TEXT` |  |
