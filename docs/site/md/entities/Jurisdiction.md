# Jurisdiction

*11 fields · module: Platform & Tenancy · Postgres: `jurisdiction`*

A tax/legal jurisdiction reference record, referenced by Facility, Parcel, and Location address blocks.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 11 |
| Catalogued fields | 10 (10 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 17 keys from 16 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IStateProvinceCountryID` |  | Country, State, County ID | — |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `StateProvinceCountryID` | State | Country, State, County ID | Global | yes | [StateProvinceCountry](StateProvinceCountry.md) |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `TaxRate1` | Tax Rate #1 | Percentage | Global |  |  |
| `TaxRate2` | Tax Rate #2 | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `JurisdictionID` | Jurisdiction RecID | Number | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Country` |  | Text | Global |  |  |
| `JurisdictionName` | Jurisdiction Name | Text | Global | yes |  |
| `StateProvince` | State Province | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Jurisdiction ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (17 keys)

| Record type | Via column |
|---|---|
| [Parcel](Parcel.md) | `JurisdictionID`, `TaxJurisdictionID` |
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `JurisdictionID` |
| [Complex](Complex.md) | `JurisdictionID` |
| [Contract](Contract.md) | `JurisdictionID` |
| [Facility](Facility.md) | `JurisdictionID` |
| [LinkReTransScenContact](LinkReTransScenContact.md) | `JurisdictionID` |
| [Location](Location.md) | `JurisdictionID` |
| [Member](Member.md) | `JurisdictionID` |
| [NonMember](NonMember.md) | `JurisdictionID` |
| [Person](Person.md) | `JurisdictionID` |
| [PotentialProject](PotentialProject.md) | `JurisdictionID` |
| [Program](Program.md) | `JurisdictionID` |
| [Project](Project.md) | `JurisdictionID` |
| [ProjectEntity](ProjectEntity.md) | `JurisdictionID` |
| [Prototype](Prototype.md) | `JurisdictionID` |
| [ReTransScenContact](ReTransScenContact.md) | `JurisdictionID` |
