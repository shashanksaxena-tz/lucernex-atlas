# Complex

*45 fields · module: Facilities, Locations & Sites · Postgres: `complex`*

A multi-building property complex/campus record sitting above Facility in the property hierarchy — complex-level classification and status fields plus a linked Person (likely site or leasing contact). 45 Global fields under its own Complex group.

Source: `data-fields/complex.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 45 |
| Catalogued fields | 45 (45 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 11 keys from 11 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-008](../rules/FAC-R-008.md) | Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/cam | Observed |
| [FAC-R-009](../rules/FAC-R-009.md) | Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DeveloperID` | Developer | Contact | Global |  |  |
| `LandlordID` | Landlord | Contact | Global |  |  |
| `PropertyManagerID` | Property Manager | Contact | Global |  |  |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeComplexClassID` | Complex Class | Dropdown (Building Class Code) | Global |  | Building Class Code |
| `CodeComplexStatusID` | Complex Status | Dropdown (Complex Status Code) | Global |  | Complex Status Code |
| `CodeComplexTypeID` | Complex Type | Dropdown (Complex Type Code) | Global |  | Complex Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SalesPerArea` | Sales Per Area | Currency | Global |  |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `OccupancyPercentage` | Occupancy Percentage | Percentage | Global |  |  |
| `VacancyRate` | Vacancy Rate | Percentage | Global |  |  |

### Quantities (8)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ComplexID` | Complex RecID | Number | Global |  |  |
| `GLAExcludingAnchors` | GLA Excluding Anchors | Number | Global |  |  |
| `GrossLeaseArea` | Gross Lease Area | Number | Global |  |  |
| `NumberLevels` | Number Levels | Number | Global |  |  |
| `NumberOutparcels` | Number Outparcels | Number | Global |  |  |
| `NumberParkingSpaces` | Number Parking Spaces | Number | Global |  |  |
| `NumberStores` | Number Stores | Number | Global |  |  |
| `YearBuilt` | Year Built | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExpansionPlanDate` | Expansion Plan Date | Date | Global |  |  |
| `RenovationPlanDate` | Renovation Plan Date | Date | Global |  |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HasFoodCourt` | Has Food Court? | Boolean | Global |  |  |
| `IsEnclosed` | Is Enclosed? | Boolean | Global |  |  |
| `IsExpansionPlanned` | Is Expansion Planned? | Boolean | Global |  |  |
| `IsRenovationPlanned` | Is Renovation Planned? | Boolean | Global |  |  |
| `IsSpaceAvailable` | Is Space Available? | Boolean | Global |  |  |

### Text & notes (15)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `City` |  | Text | Global |  |  |
| `ClientNumber` | Client Number | Text | Global |  |  |
| `ComplexName` | Complex Name | Text | Global | yes |  |
| `CountryID` | Country | Text | Global |  |  |
| `HoursOfOperation` | Hours Of Operation | Text | Global |  |  |
| `LastRenovated` | Last Renovated | Text | Global |  |  |
| `NearestCompetition` | Nearest Competition | Text | Global |  |  |
| `NotableTenants` | Notable Tenants | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Complex ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (11 keys)

| Record type | Via column |
|---|---|
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `ComplexID` |
| [Competitor](Competitor.md) | `ComplexID` |
| [Contract](Contract.md) | `ComplexID` |
| [Facility](Facility.md) | `ComplexID` |
| [Location](Location.md) | `ComplexID` |
| [Parcel](Parcel.md) | `ComplexID` |
| [PotentialProject](PotentialProject.md) | `ComplexID` |
| [Program](Program.md) | `ComplexID` |
| [Project](Project.md) | `ComplexID` |
| [ProjectEntity](ProjectEntity.md) | `ComplexID` |
| [Prototype](Prototype.md) | `ComplexID` |
