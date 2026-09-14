# Tenant

*42 fields · module: Facilities, Locations & Sites · Postgres: `tenant`*

The sub-tenant/occupant record under a Facility (for landlords or sub-lease scenarios) — headcount capacity fields (Capacity #1-4, calcTotalHeadcount) and a Contract linkage. 41 Global fields under Facility.

Source: `data-fields/tenant.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 42 |
| Fields with a vendor definition | 41 of 42 inventoried |
| Physical tables | `tenant` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 41 (41 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 8 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in tenant

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 41 fields carry a vendor definition

**Observed.** 41 of this record's 42 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 3; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-017](../rules/FAC-R-017.md) | Input: `Tenant.SpaceID`, typed `Space ID`. Confidence: Derived — the FK type is declared and every `Tenant` field (headcount, capacity, move-in/out dates) is scoped around occupying one space; | Derived |
| [PPL-R-004](../rules/PPL-R-004.md) | No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema | Observed |

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CompanyID` | Company | Select the tenant use from this field. | Employer ID | Global |  | `tenant.CompanyID · TEXT` | [Employer](Employer.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `tenant.ContractID · TEXT` | [Contract](Contract.md) |
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | Global |  | `tenant.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `OrganizationID` | Organization | Select the organization where payments should be debited from this field. | Organization ID | Global |  | `tenant.OrganizationID · TEXT` | [Organization](Organization.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `tenant.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `SpaceID` | Space | Enter the ID of the space in this field. | Space ID | Global | yes | `tenant.SpaceID · TEXT` | [Space](Space.md) |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeTenantCategoryID` | Tenant Category | Select the tenant category from this field. Categories are the third level of organization in Lx. Categories are the children of types, and grandchildren of groups. Groups, types, and categories are used to simplify reporting. | Dropdown (Tenant Category Code) | Global |  | `tenant.CodeTenantCategoryID · TEXT` | Tenant Category Code |
| `CodeTenantGroupID` | Tenant Group | Select the tenant group from this field. Groups are the first level of organization in Lx. Groups are the parents of types, and grandparents of Categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Tenant Group Code) | Global |  | `tenant.CodeTenantGroupID · TEXT` | Tenant Group Code |
| `CodeTenantStatusID` | Tenant Status | Select the tenant status from this field. | Dropdown (Tenant Status Code) | Global |  | `tenant.CodeTenantStatusID · TEXT` | Tenant Status Code |
| `CodeTenantTypeID` | Tenant Type | Select the tenant type from this field. Types are the second level of organization in Lx. Types are the children of groups, and parents of categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Tenant Type Code) | Global |  | `tenant.CodeTenantTypeID · TEXT` | Tenant Type Code |
| `CodeTenantUseID` | Tenant Use | Select the tenant type from this field. | Dropdown (Tenant Use Code) | Global |  | `tenant.CodeTenantUseID · TEXT` | Tenant Use Code |

### Quantities (11)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Capacity1` | Capacity #1 | If you track capacity in tiers, enter the total capacity for tier 1 in this field. Tiers are levels of organization. Some clients use tiers to distinguish between full-time employees, part-time employees, and managers, while other clients use tiers to distinguish between different departments. | Number | Global |  | `tenant.Capacity1 · TEXT` |  |
| `Capacity2` | Capacity #2 | If you track capacity in tiers, enter the total capacity for tier 2 in this field. Tiers are levels of organization. Some clients use tiers to distinguish between full-time employees, part-time employees, and managers, while other clients use tiers to distinguish between different departments. | Number | Global |  | `tenant.Capacity2 · TEXT` |  |
| `Capacity3` | Capacity #3 | If you track capacity in tiers, enter the total capacity for tier 3 in this field. Tiers are levels of organization. Some clients use tiers to distinguish between full-time employees, part-time employees, and managers, while other clients use tiers to distinguish between different departments. | Number | Global |  | `tenant.Capacity3 · TEXT` |  |
| `Capacity4` | Capacity #4 | If you track capacity in tiers, enter the total capacity for tier 4 in this field. Tiers are levels of organization. Some clients use tiers to distinguish between full-time employees, part-time employees, and managers, while other clients use tiers to distinguish between different departments. | Number | Global |  | `tenant.Capacity4 · TEXT` |  |
| `HeadCount1` | Head Count #1 | Enter the total headcount for tier 1 in this field. | Number | Global |  | `tenant.HeadCount1 · TEXT` |  |
| `HeadCount2` | Head Count #2 | Enter the total headcount for tier 2 in this field. | Number | Global |  | `tenant.HeadCount2 · TEXT` |  |
| `HeadCount3` | Head Count #3 | Enter the total headcount for tier 3 in this field. | Number | Global |  | `tenant.HeadCount3 · TEXT` |  |
| `HeadCount4` | Head Count #4 | Enter the total headcount for tier 4 in this field. | Number | Global |  | `tenant.HeadCount4 · TEXT` |  |
| `TenantID` | Tenant RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `tenant.TenantID · VARCHAR(64) NOT NULL` |  |
| `TotalCapacity` | Total Capacity | Enter the total capacity of the space in this field. | Number | Global |  | `tenant.TotalCapacity · TEXT` |  |
| `math_calcTotalCapacity_1` | calcTotalHeadcount | Calculates the total headcount. | Number | Global |  | `tenant.math_calcTotalCapacity_1 · TEXT` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the tenancy record in this field. | Date | Global |  | `tenant.EffectiveDate · TEXT` |  |
| `MoveInDate` | Move In Date | Enter the date the tenant moved in. | Date | Global |  | `tenant.MoveInDate · TEXT` |  |
| `MoveOutDate` | Move Out Date | Enter the date the tenant moved out. | Date | Global |  | `tenant.MoveOutDate · TEXT` |  |

### Text & notes (11)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `City` |  | The city associated with this record. | Text | Global |  | `tenant.City · TEXT` |  |
| `CountryID` | Country | Select the country from this field. | Text | Global |  | `tenant.CountryID · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `tenant.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `tenant.Notes · TEXT` |  |
| `PostalCode` | Postal Code | Enter the postal code of the tenant in this field. | Text | Global |  | `tenant.PostalCode · TEXT` |  |
| `StateProvince` | State Province | The state or province of the associated record. | Text | Global |  | `tenant.StateProvince · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `tenant.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `tenant.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `tenant.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `tenant.StreetAddress4 · TEXT` |  |
| `TenantName` | Tenant Name | Enter the name of the tenant in this field. | Text | Global | yes | `tenant.TenantName · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Tenant ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `tenant.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `tenant.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `tenant.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `tenant.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `tenant.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `tenant.RevNumber · TEXT` |  |
