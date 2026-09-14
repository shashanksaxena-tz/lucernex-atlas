# EmployerSite

*20 fields · module: People & Parties · Postgres: `employer_site`*

A specific site/location belonging to an Employer (useful when a vendor has multiple branch offices) — business unit and currency type per site. 20 Global fields under Company Items.

Source: `data-fields/employer-site.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Fields with a vendor definition | 0 of 20 inventoried |
| Physical tables | `employer_site` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in employer_site

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required-ness: the captures agree

**Observed.** Over the 20 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EmployerID` | Employer |  | Employer ID | Global | yes | `employer_site.EmployerID · TEXT` | [Employer](Employer.md) |
| `StateProvinceCountryID` | State |  | Country, State, County ID | Global |  | `employer_site.StateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type |  | Dropdown (Currency Type Code) | Global |  | `employer_site.CodeCurrencyTypeID · TEXT` | Currency Type Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EmployerSiteID` | Vendor Site RecID |  | Number | Global |  | `employer_site.EmployerSiteID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date |  | Date | Global |  | `employer_site.BeginDate · TEXT` |  |
| `EndDate` | End Date |  | Date | Global |  | `employer_site.EndDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Is Inactive? |  | Boolean | Global | yes | `employer_site.Inactive · TEXT` |  |

### Text & notes (13)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BusinessUnit` | Business Unit |  | Text | Global |  | `employer_site.BusinessUnit · TEXT` |  |
| `City` |  |  | Text | Global |  | `employer_site.City · TEXT` |  |
| `CountryID` | Country |  | Text | Global |  | `employer_site.CountryID · TEXT` |  |
| `Notes` |  |  | Text | Global |  | `employer_site.Notes · TEXT` |  |
| `Phone` |  |  | Text | Global |  | `employer_site.Phone · TEXT` |  |
| `PostalCode` | Postal Code |  | Text | Global |  | `employer_site.PostalCode · TEXT` |  |
| `StreetAddress1` | Street Address #1 |  | Text | Global |  | `employer_site.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 |  | Text | Global |  | `employer_site.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 |  | Text | Global |  | `employer_site.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 |  | Text | Global |  | `employer_site.StreetAddress4 · TEXT` |  |
| `VendorSiteCode` | Vendor Site Code |  | Text | Global |  | `employer_site.VendorSiteCode · TEXT` |  |
| `VendorSiteID` | Vendor Site ID |  | Text | Global | yes | `employer_site.VendorSiteID · TEXT` |  |
| `VendorSiteName` | Vendor Site Name |  | Text | Global |  | `employer_site.VendorSiteName · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [Issue](Issue.md) | `EmployerSiteID` |
