# StateProvinceCountry

*11 fields · module: Platform & Tenancy · Postgres: `state_province_country`*

Master geography reference with ISO Alpha-2/3 country codes, backing every address field across Facility, Location, and Parcel.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 11 |
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

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |

## Fields

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TaxRate1` | Tax Rate 1 | Percentage | Global |  |  |
| `TaxRate2` | Tax Rate 2 | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `StateProvinceCountryID` | State Province Country RecID | Number | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Country` |  | Text | Global | yes |  |
| `ISOAlpha2Code` | ISO Alpha #2 Code | Text | Global | yes |  |
| `ISOAlpha3Code` | ISO Alpha #3 Code | Text | Global | yes |  |
| `StateProvince` | State Province | Text | Global | yes |  |
| `StateProvinceCountryName` | State Province Country | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | State Province Country ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

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
