# Jurisdiction

*11 fields · module: Platform & Tenancy · Postgres: `jurisdiction`*

A tax/legal jurisdiction reference record, referenced by Facility, Parcel, and Location address blocks.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 11 |
| Fields with a vendor definition | 10 of 11 inventoried |
| Physical tables | `jurisdiction` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 10 (10 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 17 keys from 16 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in jurisdiction

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 10 fields carry a vendor definition

**Observed.** 10 of this record's 11 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 3; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IStateProvinceCountryID` |  |  | Country, State, County ID | — |  | `jurisdiction.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `StateProvinceCountryID` | State | The state / province associated with this county / jurisdiction. | Country, State, County ID | Global | yes | `jurisdiction.StateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TaxRate1` | Tax Rate #1 | Enter the primary tax rate associated with this county / jurisdiction. | Percentage | Global |  | `jurisdiction.TaxRate1 · TEXT` |  |
| `TaxRate2` | Tax Rate #2 | Enter the secondary tax rate associated with this county / jurisdiction. | Percentage | Global |  | `jurisdiction.TaxRate2 · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `JurisdictionID` | Jurisdiction RecID | The county / province associated with the associated entity's address. | Number | Global |  | `jurisdiction.JurisdictionID · VARCHAR(64) NOT NULL` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Country` |  | The country associated with this county / jurisdiction. | Text | Global |  | `jurisdiction.Country · TEXT` |  |
| `JurisdictionName` | Jurisdiction Name | The name of the county / jurisdiction. | Text | Global | yes | `jurisdiction.JurisdictionName · TEXT` |  |
| `StateProvince` | State Province | The state or province of the associated record. | Text | Global |  | `jurisdiction.StateProvince · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Jurisdiction ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `jurisdiction.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `jurisdiction.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `jurisdiction.ModifiedDate · TEXT` |  |

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
