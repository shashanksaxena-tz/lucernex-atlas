# Complex

*45 fields · module: Facilities, Locations & Sites · Postgres: `complex`*

A multi-building property complex/campus record sitting above Facility in the property hierarchy — complex-level classification and status fields plus a linked Person (likely site or leasing contact). 45 Global fields under its own Complex group.

Source: `data-fields/complex.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 45 |
| Fields with a vendor definition | 45 of 45 inventoried |
| Physical tables | `complex` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 45 (45 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 11 keys from 11 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in complex

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 45 fields carry a vendor definition

**Observed.** 45 of this record's 45 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 2; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-008](../rules/FAC-R-008.md) | Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/cam | Observed |
| [FAC-R-009](../rules/FAC-R-009.md) | Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | Global |  | `complex.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | Select the county that this location belongs to from this field. Contact Support if you need to have counties added to the system. | County ID | Global |  | `complex.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DeveloperID` | Developer | Select the developer of the complex from this field. | Contact | Global |  | `complex.DeveloperID · TEXT` |  |
| `LandlordID` | Landlord | Select the landlord of the complex from this field. | Contact | Global |  | `complex.LandlordID · TEXT` |  |
| `PropertyManagerID` | Property Manager | Select the property manager of the complex from this field. | Contact | Global |  | `complex.PropertyManagerID · TEXT` |  |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global |  | `complex.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeComplexClassID` | Complex Class | Select the scheme of the complex from this field. Example schemes include regional malls, strip / convenience, or neighborhood centers. | Dropdown (Building Class Code) | Global |  | `complex.CodeComplexClassID · TEXT` | Building Class Code |
| `CodeComplexStatusID` | Complex Status | Select the status of the center or complex from this field. | Dropdown (Complex Status Code) | Global |  | `complex.CodeComplexStatusID · TEXT` | Complex Status Code |
| `CodeComplexTypeID` | Complex Type | Select the format of the complex from this field. Example formats include malls or open-air centers. | Dropdown (Complex Type Code) | Global |  | `complex.CodeComplexTypeID · TEXT` | Complex Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SalesPerArea` | Sales Per Area | Enter the estimated sales / rentable area of the complex in this field. | Currency | Global |  | `complex.SalesPerArea · TEXT` |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `OccupancyPercentage` | Occupancy Percentage | Enter the occupancy percentage of the complex in this field. | Percentage | Global |  | `complex.OccupancyPercentage · TEXT` |  |
| `VacancyRate` | Vacancy Rate | The Vacancy Rate is the percentage of the complex that is vacant. This percentage is calculated as 100% - the Occupancy Percentage. | Percentage | Global |  | `complex.VacancyRate · TEXT` |  |

### Quantities (8)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ComplexID` | Complex RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `complex.ComplexID · VARCHAR(64) NOT NULL` |  |
| `GLAExcludingAnchors` | GLA Excluding Anchors | Enter the gross leaseable area of the complex excluding anchor stores. An example of an anchor store would be a big chain department store. | Number | Global |  | `complex.GLAExcludingAnchors · TEXT` |  |
| `GrossLeaseArea` | Gross Lease Area | Enter the gross leaseable area of the complex. | Number | Global |  | `complex.GrossLeaseArea · TEXT` |  |
| `NumberLevels` | Number Levels | Enter the number of floors this complex has in this field. | Number | Global |  | `complex.NumberLevels · TEXT` |  |
| `NumberOutparcels` | Number Outparcels | Enter the number of storefronts on the lot in this field. For example, there may be a lot with several buildings that is owned by one parent company. Each of these buildings may have a different company that is leasing the space. | Number | Global |  | `complex.NumberOutparcels · TEXT` |  |
| `NumberParkingSpaces` | Number Parking Spaces | Enter the number of parking spaces the complex has in this field. | Number | Global |  | `complex.NumberParkingSpaces · TEXT` |  |
| `NumberStores` | Number Stores | Enter the number of stores in the complex in this field. | Number | Global |  | `complex.NumberStores · TEXT` |  |
| `YearBuilt` | Year Built | Enter the year built in this field. | Number | Global |  | `complex.YearBuilt · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExpansionPlanDate` | Expansion Plan Date | Enter the planned start date of the expansion. | Date | Global |  | `complex.ExpansionPlanDate · TEXT` |  |
| `RenovationPlanDate` | Renovation Plan Date | Enter the planned start date of the renovation. | Date | Global |  | `complex.RenovationPlanDate · TEXT` |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HasFoodCourt` | Has Food Court? | Select this check box if the complex has a food court. | Boolean | Global |  | `complex.HasFoodCourt · TEXT` |  |
| `IsEnclosed` | Is Enclosed? | Select this check box if the complex is enclosed for example, an indoor mall. | Boolean | Global |  | `complex.IsEnclosed · TEXT` |  |
| `IsExpansionPlanned` | Is Expansion Planned? | Select this check box if there is a expansion planned for the complex. | Boolean | Global |  | `complex.IsExpansionPlanned · TEXT` |  |
| `IsRenovationPlanned` | Is Renovation Planned? | Select this check box if there is a renovation planned for the complex. | Boolean | Global |  | `complex.IsRenovationPlanned · TEXT` |  |
| `IsSpaceAvailable` | Is Space Available? | Select this check box if there is space available in the complex. | Boolean | Global |  | `complex.IsSpaceAvailable · TEXT` |  |

### Text & notes (15)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `City` |  | The city associated with this record. | Text | Global |  | `complex.City · TEXT` |  |
| `ClientNumber` | Client Number | Enter a reference number for the complex in this field. | Text | Global |  | `complex.ClientNumber · TEXT` |  |
| `ComplexName` | Complex Name | Enter the complex's name in this field. | Text | Global | yes | `complex.ComplexName · TEXT` |  |
| `CountryID` | Country | Select the country from this field. | Text | Global |  | `complex.CountryID · TEXT` |  |
| `HoursOfOperation` | Hours Of Operation | Enter the hours of operation of the complex in this field. | Text | Global |  | `complex.HoursOfOperation · TEXT` |  |
| `LastRenovated` | Last Renovated | Enter the date of the last renovation. | Text | Global |  | `complex.LastRenovated · TEXT` |  |
| `NearestCompetition` | Nearest Competition | Enter the nearest competition in this field. | Text | Global |  | `complex.NearestCompetition · TEXT` |  |
| `NotableTenants` | Notable Tenants | Enter the names of any notable tenants of the complex in this field. | Text | Global |  | `complex.NotableTenants · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `complex.Notes · TEXT` |  |
| `Phone` |  | Enter the phone number of the complex in this field. | Text | Global |  | `complex.Phone · TEXT` |  |
| `PostalCode` | Postal Code | Enter the postal code of the complex in this field. | Text | Global |  | `complex.PostalCode · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `complex.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `complex.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `complex.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `complex.StreetAddress4 · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Complex ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `complex.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `complex.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `complex.ModifiedDate · TEXT` |  |

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
