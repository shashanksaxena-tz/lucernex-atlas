# DemographicResults

*12 fields · module: Facilities, Locations & Sites · Postgres: `demographic_results`*

A saved demographic analysis output for a site — name, description, and an attached results document.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 12 |
| Fields with a vendor definition | 3 of 12 inventoried |
| Physical tables | `demographic_results` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 11 (11 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in demographic_results

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 3 fields carry a vendor definition

**Observed.** 3 of this record's 12 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-032](../rules/RPT-R-032.md) | Demographic Reports are the only report family with an explicit asynchronous execution record: `DemographicResults` carries `TimeInitiated`, `TimeFinished`, a status code, a third-party vendor code, and a `DocumentID` for the produced artef | Observed |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentID` | Demographic Results Document |  | Document ID | Global |  | `demographic_results.DocumentID · TEXT` | [Document](Document.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `demographic_results.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeDemographicResultsTypeID` | Demographic Results Type |  | Dropdown (Demographic Results Type Code) | Global | yes | `demographic_results.CodeDemographicResultsTypeID · TEXT` | Demographic Results Type Code |
| `CodeResultsStatusID` | Results Status |  | Dropdown (Results Status Code) | Global | yes | `demographic_results.CodeResultsStatusID · TEXT` | Results Status Code |
| `CodeThirdPartyVendorID` | Third Party Vendor |  | Dropdown (Third Party Vendor Code) | Global |  | `demographic_results.CodeThirdPartyVendorID · TEXT` | Third Party Vendor Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DemographicResultsID` | Demographic Results RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `demographic_results.DemographicResultsID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TimeFinished` | Time Finished |  | Time | Global |  | `demographic_results.TimeFinished · TEXT` |  |
| `TimeInitiated` | Time Initiated |  | Time | Global |  | `demographic_results.TimeInitiated · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DemographicResultsName` | Demographic Results Name |  | Text | Global |  | `demographic_results.DemographicResultsName · TEXT` |  |
| `Description` | Demographic Results Description | Write a description of the record. | Text | Global |  | `demographic_results.Description · TEXT` |  |
| `TempLocation` | Temp Location |  | Text | Global |  | `demographic_results.TempLocation · TEXT` |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Demographic Results ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `demographic_results.BOMapClientRecordID · TEXT` |  |
