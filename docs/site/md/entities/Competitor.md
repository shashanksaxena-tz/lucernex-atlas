# Competitor

*26 fields · module: Facilities, Locations & Sites · Postgres: `competitor`*

A competing retailer/property tracked for market analysis — name, type, and building area unit, used in site-selection and demographic comparison work. 25 Global fields under Summary Information.

Source: `data-fields/competitor.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 26 |
| Fields with a vendor definition | 25 of 26 inventoried |
| Physical tables | `competitor` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 25 (25 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in competitor

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 25 fields carry a vendor definition

**Observed.** 25 of this record's 26 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 25 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 2 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-008](../rules/FAC-R-008.md) | Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/cam | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ComplexID` | Complex | The ID of the complex associated with the location where the competitor is located. | Complex ID | Global |  | `competitor.ComplexID · TEXT` | [Complex](Complex.md) |
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | Global |  | `competitor.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `competitor.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global |  | `competitor.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCompetitorTypeID` | Competitor Type | Select the type of competitor from this field. | Dropdown (Competitor Type Code) | Global |  | `competitor.CodeCompetitorTypeID · TEXT` | Competitor Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LastYearSales` | Last Year Annual Sales | Enter the competitor's last year of annual sales in this field. | Currency | Global |  | `competitor.LastYearSales · TEXT` |  |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CompetitorID` | Competitor RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `competitor.CompetitorID · VARCHAR(64) NOT NULL` |  |
| `LatitudeDegrees` | Latitude | The latitude of the competitor's location. | 5-Digit Number | Global |  | `competitor.LatitudeDegrees · TEXT` |  |
| `LongitudeDegrees` | Longitude | The longitude of the competitor's location. | 5-Digit Number | Global |  | `competitor.LongitudeDegrees · TEXT` |  |
| `RentableArea` | Rentable Area | Enter the competitor's rentable area in this field. | Number | Global |  | `competitor.RentableArea · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsAnchorStore` | Is Anchor Store? | This flag indicates whether or not this competitor is an anchor store. | Boolean | Global |  | `competitor.IsAnchorStore · TEXT` |  |

### Text & notes (12)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `City` |  | The city associated with this record. | Text | Global |  | `competitor.City · TEXT` |  |
| `CompetitorName` | Competitor Name | Enter the name of the competitor in this field. | Text | Global | yes | `competitor.CompetitorName · TEXT` |  |
| `CountryID` | Country | Select the country associated with the competitor's address from this field. | Text | Global |  | `competitor.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | Enter the first cross street in this field. | Text | Global |  | `competitor.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | Enter the second cross street in this field. | Text | Global |  | `competitor.CrossStreet2 · TEXT` |  |
| `Distance` |  | Enter the distance between your site and the competitor in this field. | Text | Global |  | `competitor.Distance · TEXT` |  |
| `DriveTime` | Drive Time | Enter the drive time between your site and the competitor in this field. | Text | Global |  | `competitor.DriveTime · TEXT` |  |
| `PostalCode` | Postal Code | Enter the postal code of the competitor's location in this field. | Text | Global |  | `competitor.PostalCode · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `competitor.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `competitor.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `competitor.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `competitor.StreetAddress4 · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Competitor ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `competitor.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `competitor.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `competitor.ModifiedDate · TEXT` |  |
