# LinkLandPurchaseInspection

*8 fields · module: Facilities, Locations & Sites · Postgres: `link_land_purchase_inspection`*

Join table linking a LandPurchaseSummary to a due-diligence inspection — type, duration, and scheduled date.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 8 |
| Fields with a vendor definition | 7 of 8 inventoried |
| Physical tables | `link_land_purchase_inspection` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 8 (8 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_land_purchase_inspection

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 7 fields carry a vendor definition

**Observed.** 7 of this record's 8 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 4 of this record's fields required; the Data Fields catalogue marks 4; 4 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `link_land_purchase_inspection.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeInspectionPeriodStartID` | Inspection To Begin | The period the inspection will start. | Dropdown (Inspection Period Start Code) | Global | yes | `link_land_purchase_inspection.CodeInspectionPeriodStartID · TEXT` | Inspection Period Start Code |
| `CodeInspectionTypeID` | Inspection Type | The inspection type. | Dropdown (Inspection Type Code) | Global | yes | `link_land_purchase_inspection.CodeInspectionTypeID · TEXT` | Inspection Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `InspectionDays` | Inspection Duration | The duration of the inspection. | Number | Global | yes | `link_land_purchase_inspection.InspectionDays · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LandPurchaseSummaryID` | Land Purchase Summary | The ID of the land purchase summary record. | Text | Global | yes | `link_land_purchase_inspection.LandPurchaseSummaryID · TEXT` |  |
| `Notes` | Comments | Add any notes about the record. | Text | Global |  | `link_land_purchase_inspection.Notes · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `link_land_purchase_inspection.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `link_land_purchase_inspection.ModifiedDate · TEXT` |  |
