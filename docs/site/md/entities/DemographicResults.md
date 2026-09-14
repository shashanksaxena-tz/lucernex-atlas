# DemographicResults

*12 fields · module: Facilities, Locations & Sites · Postgres: `demographic_results`*

A saved demographic analysis output for a site — name, description, and an attached results document.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 12 |
| Catalogued fields | 11 (11 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-032](../rules/RPT-R-032.md) | Demographic Reports are the only report family with an explicit asynchronous execution record: `DemographicResults` carries `TimeInitiated`, `TimeFinished`, a status code, a third-party vendor code, and a `DocumentID` for the produced artef | Observed |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentID` | Demographic Results Document | Document ID | Global |  | [Document](Document.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeDemographicResultsTypeID` | Demographic Results Type | Dropdown (Demographic Results Type Code) | Global | yes | Demographic Results Type Code |
| `CodeResultsStatusID` | Results Status | Dropdown (Results Status Code) | Global | yes | Results Status Code |
| `CodeThirdPartyVendorID` | Third Party Vendor | Dropdown (Third Party Vendor Code) | Global |  | Third Party Vendor Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DemographicResultsID` | Demographic Results RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TimeFinished` | Time Finished | Time | Global |  |  |
| `TimeInitiated` | Time Initiated | Time | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DemographicResultsName` | Demographic Results Name | Text | Global |  |  |
| `Description` | Demographic Results Description | Text | Global |  |  |
| `TempLocation` | Temp Location | Text | Global |  |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Demographic Results ClientID | Text | Global | yes |  |
