# EmployerSite

*20 fields · module: People & Parties · Postgres: `employer_site`*

A specific site/location belonging to an Employer (useful when a vendor has multiple branch offices) — business unit and currency type per site. 20 Global fields under Company Items.

Source: `data-fields/employer-site.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EmployerID` | Employer | Employer ID | Global | yes | [Employer](Employer.md) |
| `StateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EmployerSiteID` | Vendor Site RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |

### Text & notes (13)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BusinessUnit` | Business Unit | Text | Global |  |  |
| `City` |  | Text | Global |  |  |
| `CountryID` | Country | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `VendorSiteCode` | Vendor Site Code | Text | Global |  |  |
| `VendorSiteID` | Vendor Site ID | Text | Global | yes |  |
| `VendorSiteName` | Vendor Site Name | Text | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [Issue](Issue.md) | `EmployerSiteID` |
