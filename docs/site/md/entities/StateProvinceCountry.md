# StateProvinceCountry

*11 fields · module: Platform & Tenancy · Postgres: `state_province_country`*

Master geography reference with ISO Alpha-2/3 country codes, backing every address field across Facility, Location, and Parcel.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 11 |
| Fields with a vendor definition | 11 of 11 inventoried |
| Physical tables | `state_province_country` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 11 (11 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 26 keys from 22 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### A hub: 26 keys point here

**Observed.** 22 record types hold a foreign key into this one, so it sits at the centre of the relationship graph. Changing its key or its identity is a change to BudgetOptionTemplate, Competitor, Complex, Contract and 18 others.

### Lands in state_province_country

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 11 fields carry a vendor definition

**Observed.** 11 of this record's 11 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 11 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 5 are marked required.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |

## Fields

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TaxRate1` | Tax Rate 1 | The first tax rate for a given StateProvinceCountry record. | Percentage | Global |  | `state_province_country.TaxRate1 · TEXT` |  |
| `TaxRate2` | Tax Rate 2 | The second tax rate for a given StateProvinceCountry record. | Percentage | Global |  | `state_province_country.TaxRate2 · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `StateProvinceCountryID` | State Province Country RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `state_province_country.StateProvinceCountryID · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Country` |  | This field determines the country of the StateProvinceCountry record. | Text | Global | yes | `state_province_country.Country · TEXT` |  |
| `ISOAlpha2Code` | ISO Alpha #2 Code | The ISO Alpha 2 Code of the given StateProvinceCountry record (such as US, MX, CA). | Text | Global | yes | `state_province_country.ISOAlpha2Code · TEXT` |  |
| `ISOAlpha3Code` | ISO Alpha #3 Code | The ISO Alpha 3 Code of the given StateProvinceCountry record (such as USA, MEX, CAN). | Text | Global | yes | `state_province_country.ISOAlpha3Code · TEXT` |  |
| `StateProvince` | State Province | The State / Province abbreviation, such as TX for Texas. | Text | Global | yes | `state_province_country.StateProvince · TEXT` |  |
| `StateProvinceCountryName` | State Province Country | The state/province and country, separated by a comma (such as Tx, United States). | Text | Global |  | `state_province_country.StateProvinceCountryName · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | State Province Country ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `state_province_country.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | Text that has both the state/province and country, separated by a comma. (e.g. Tx, United States) | Member ID | Global |  | `state_province_country.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `state_province_country.ModifiedDate · TEXT` |  |

## What points here (26 keys)

| Record type | Via column |
|---|---|
| [DiscountRate](DiscountRate.md) | `CountryID`, `CountryIDList`, `StateProvinceIDList` |
| [Jurisdiction](Jurisdiction.md) | `IStateProvinceCountryID`, `StateProvinceCountryID` |
| [Member](Member.md) | `IStateProvinceCountryID`, `StateProvinceCountryID` |
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `IStateProvinceCountryID` |
| [Competitor](Competitor.md) | `IStateProvinceCountryID` |
| [Complex](Complex.md) | `IStateProvinceCountryID` |
| [Contract](Contract.md) | `IStateProvinceCountryID` |
| [Employer](Employer.md) | `IStateProvinceCountryID` |
| [EmployerSite](EmployerSite.md) | `StateProvinceCountryID` |
| [Facility](Facility.md) | `IStateProvinceCountryID` |
| [LinkReTransScenContact](LinkReTransScenContact.md) | `StateProvinceCountryID` |
| [Location](Location.md) | `IStateProvinceCountryID` |
| [NonMember](NonMember.md) | `IStateProvinceCountryID` |
| [Parcel](Parcel.md) | `IStateProvinceCountryID` |
| [Person](Person.md) | `IStateProvinceCountryID` |
| [PotentialProject](PotentialProject.md) | `IStateProvinceCountryID` |
| [Program](Program.md) | `IStateProvinceCountryID` |
| [Project](Project.md) | `IStateProvinceCountryID` |
| [ProjectEntity](ProjectEntity.md) | `IStateProvinceCountryID` |
| [Prototype](Prototype.md) | `IStateProvinceCountryID` |
| [ReTransScenContact](ReTransScenContact.md) | `StateProvinceCountryID` |
| [Tenant](Tenant.md) | `IStateProvinceCountryID` |
