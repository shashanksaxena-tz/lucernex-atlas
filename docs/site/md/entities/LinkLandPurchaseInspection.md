# LinkLandPurchaseInspection

*8 fields · module: Facilities, Locations & Sites · Postgres: `link_land_purchase_inspection`*

Join table linking a LandPurchaseSummary to a due-diligence inspection — type, duration, and scheduled date.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 8 |
| Catalogued fields | 8 (8 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeInspectionPeriodStartID` | Inspection To Begin | Dropdown (Inspection Period Start Code) | Global | yes | Inspection Period Start Code |
| `CodeInspectionTypeID` | Inspection Type | Dropdown (Inspection Type Code) | Global | yes | Inspection Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `InspectionDays` | Inspection Duration | Number | Global | yes |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LandPurchaseSummaryID` | Land Purchase Summary | Text | Global | yes |  |
| `Notes` | Comments | Text | Global |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
