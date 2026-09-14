# Space

*27 fields · module: Facilities, Locations & Sites · Postgres: `space`*

A leasable space/suite record within a Facility — area unit and Contract linkage, more granular than Facility itself for multi-tenant buildings. 26 Global fields under Facility.

Source: `data-fields/space.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 27 |
| Catalogued fields | 26 (26 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-015](../rules/FAC-R-015.md) | Input: `Space.FacilityID`, Required = Yes. Confidence: Observed (`../../data-fields/space.md`). | Observed |
| [FAC-R-016](../rules/FAC-R-016.md) | Input: `Space.ContractID`, Required = No. Effect: A Space can be defined on a Facility before any lease references it — e.g., during Space Management setup ahead of leasing. | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `FacilityID` | Facility | Facility ID | Global | yes | [Facility](Facility.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeSpaceGroupID` | Space Group | Dropdown (Space Group Code) | Global |  | Space Group Code |
| `CodeSpaceStatusID` | Space Status | Dropdown (Space Status Code) | Global |  | Space Status Code |
| `CodeSpaceTypeID` | Space Type | Dropdown (Space Type Code) | Global |  | Space Type Code |
| `CodeSpaceUseID` | Space Use | Dropdown (Space Use Code) | Global |  | Space Use Code |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossArea` | Gross Area | Number | Global |  |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |
| `SpaceID` | Space RecID | Number | Global |  |  |
| `TotalHeadCount` | Total Head Count | Number | Global |  |  |
| `UsableArea` | Usable Area | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ClientNumber` | Client Number | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `FloorNumber` | Floor Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `RoomNumber` | Room Number | Text | Global |  |  |
| `SpaceName` | Space Name | Text | Global | yes |  |
| `SuiteNumber` | Suite Number | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Space ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [Tenant](Tenant.md) | `SpaceID` |
