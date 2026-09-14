# DemographicStudyArea

*6 fields · module: Facilities, Locations & Sites · Postgres: `demographic_study_area`*

The trade-area definition used for a demographic study — radius in miles or drive time in minutes, an alternative to SiteSurvey's fixed 1/3/5-mile bands.

Source: `data-fields/demographics-market-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 6 |
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

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-033](../rules/RPT-R-033.md) | A Demographic Report's scope is a trade area defined by radius or drive time (`DemographicStudyArea.AreaRadius`, `.AreaDriveTimeInMinutes`, `.CodeRadiusUnitID`) — a site-selection feature, not a lease-accounting one. · Observed · `_lucernex | Observed |
| [FAC-R-020](../rules/FAC-R-020.md) | Input: `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as a reusable, parameterised definition. | Derived |

## Fields

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeRadiusUnitID` | Radius Unit | Dropdown (Distance Unit Code) | Global |  | Distance Unit Code |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AreaDriveTimeInMinutes` | Area Drive Time In Minutes | Number | Global |  |  |
| `AreaRadius` | Area Radius | Number | Global |  |  |
| `DemographicStudyAreaID` | Demographic Study Area RecID | Number | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DemographicStudyAreaName` | Demographic Study Area Name | Text | Global | yes |  |

### Audit & record keeping (1)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Demographic Study Area ClientID | Text | Global | yes |  |
