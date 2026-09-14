# Tenant

*42 fields · module: Facilities, Locations & Sites · Postgres: `tenant`*

The sub-tenant/occupant record under a Facility (for landlords or sub-lease scenarios) — headcount capacity fields (Capacity #1-4, calcTotalHeadcount) and a Contract linkage. 41 Global fields under Facility.

Source: `data-fields/tenant.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 42 |
| Catalogued fields | 41 (41 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 8 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-017](../rules/FAC-R-017.md) | Input: `Tenant.SpaceID`, typed `Space ID`. Confidence: Derived — the FK type is declared and every `Tenant` field (headcount, capacity, move-in/out dates) is scoped around occupying one space; | Derived |
| [PPL-R-004](../rules/PPL-R-004.md) | No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema | Observed |

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CompanyID` | Company | Employer ID | Global |  | [Employer](Employer.md) |
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `OrganizationID` | Organization | Organization ID | Global |  | [Organization](Organization.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `SpaceID` | Space | Space ID | Global | yes | [Space](Space.md) |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeTenantCategoryID` | Tenant Category | Dropdown (Tenant Category Code) | Global |  | Tenant Category Code |
| `CodeTenantGroupID` | Tenant Group | Dropdown (Tenant Group Code) | Global |  | Tenant Group Code |
| `CodeTenantStatusID` | Tenant Status | Dropdown (Tenant Status Code) | Global |  | Tenant Status Code |
| `CodeTenantTypeID` | Tenant Type | Dropdown (Tenant Type Code) | Global |  | Tenant Type Code |
| `CodeTenantUseID` | Tenant Use | Dropdown (Tenant Use Code) | Global |  | Tenant Use Code |

### Quantities (11)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Capacity1` | Capacity #1 | Number | Global |  |  |
| `Capacity2` | Capacity #2 | Number | Global |  |  |
| `Capacity3` | Capacity #3 | Number | Global |  |  |
| `Capacity4` | Capacity #4 | Number | Global |  |  |
| `HeadCount1` | Head Count #1 | Number | Global |  |  |
| `HeadCount2` | Head Count #2 | Number | Global |  |  |
| `HeadCount3` | Head Count #3 | Number | Global |  |  |
| `HeadCount4` | Head Count #4 | Number | Global |  |  |
| `TenantID` | Tenant RecID | Number | Global |  |  |
| `TotalCapacity` | Total Capacity | Number | Global |  |  |
| `math_calcTotalCapacity_1` | calcTotalHeadcount | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `MoveInDate` | Move In Date | Date | Global |  |  |
| `MoveOutDate` | Move Out Date | Date | Global |  |  |

### Text & notes (11)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `City` |  | Text | Global |  |  |
| `CountryID` | Country | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `StateProvince` | State Province | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `TenantName` | Tenant Name | Text | Global | yes |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Tenant ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
