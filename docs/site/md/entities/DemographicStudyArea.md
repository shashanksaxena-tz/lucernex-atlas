# DemographicStudyArea

*6 fields · module: Facilities, Locations & Sites · Postgres: `demographic_study_area`*

The trade-area definition used for a demographic study — radius in miles or drive time in minutes, an alternative to SiteSurvey's fixed 1/3/5-mile bands.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 6 |
| Fields with a vendor definition | 2 of 6 inventoried |
| Physical tables | `demographic_study_area` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 6 (6 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 0 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### No typed relationships either way

**Derived.** Nothing holds a typed foreign key into this record and it declares none out. Either it is joined by a soft reference the census cannot see, or it is genuinely standalone — worth settling before anything is built on it.

### Lands in demographic_study_area

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 2 fields carry a vendor definition

**Observed.** 2 of this record's 6 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 2; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-033](../rules/RPT-R-033.md) | A Demographic Report's scope is a trade area defined by radius or drive time (`DemographicStudyArea.AreaRadius`, `.AreaDriveTimeInMinutes`, `.CodeRadiusUnitID`) — a site-selection feature, not a lease-accounting one. · Observed · `_lucernex | Observed |
| [FAC-R-020](../rules/FAC-R-020.md) | Input: `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as a reusable, parameterised definition. | Derived |

## Fields

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeRadiusUnitID` | Radius Unit |  | Dropdown (Distance Unit Code) | Global |  | `demographic_study_area.CodeRadiusUnitID · TEXT` | Distance Unit Code |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AreaDriveTimeInMinutes` | Area Drive Time In Minutes |  | Number | Global |  | `demographic_study_area.AreaDriveTimeInMinutes · TEXT` |  |
| `AreaRadius` | Area Radius |  | Number | Global |  | `demographic_study_area.AreaRadius · TEXT` |  |
| `DemographicStudyAreaID` | Demographic Study Area RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `demographic_study_area.DemographicStudyAreaID · VARCHAR(64) NOT NULL` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DemographicStudyAreaName` | Demographic Study Area Name |  | Text | Global | yes | `demographic_study_area.DemographicStudyAreaName · TEXT` |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Demographic Study Area ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `demographic_study_area.BOMapClientRecordID · TEXT` |  |
