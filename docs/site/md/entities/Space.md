# Space

*27 fields · module: Facilities, Locations & Sites · Postgres: `space`*

A leasable space/suite record within a Facility — area unit and Contract linkage, more granular than Facility itself for multi-tenant buildings. 26 Global fields under Facility.

Source: `data-fields/space.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 27 |
| Fields with a vendor definition | 26 of 27 inventoried |
| Physical tables | `space` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 26 (26 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in space

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 26 fields carry a vendor definition

**Observed.** 26 of this record's 27 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 26 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [FAC-R-015](../rules/FAC-R-015.md) | Input: `Space.FacilityID`, Required = Yes. Confidence: Observed (`../../data-fields/space.md`). | Observed |
| [FAC-R-016](../rules/FAC-R-016.md) | Input: `Space.ContractID`, Required = No. Effect: A Space can be defined on a Facility before any lease references it — e.g., during Space Management setup ahead of leasing. | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `space.ContractID · TEXT` | [Contract](Contract.md) |
| `FacilityID` | Facility | Select the facility that your record will be associated with from this field. | Facility ID | Global | yes | `space.FacilityID · TEXT` | [Facility](Facility.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `space.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global |  | `space.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeSpaceGroupID` | Space Group | Select the space group from this field. Groups are the first level of organization in Lx. Groups are the parents of types, and grandparents of Categories. Groups, types, and categories are used to simplify reporting. | Dropdown (Space Group Code) | Global |  | `space.CodeSpaceGroupID · TEXT` | Space Group Code |
| `CodeSpaceStatusID` | Space Status | Select the space status from this field. | Dropdown (Space Status Code) | Global |  | `space.CodeSpaceStatusID · TEXT` | Space Status Code |
| `CodeSpaceTypeID` | Space Type | Select the space type from this field. Types are the second level of organization in Lx. Types are the children of groups. Groups and types are used to simplify reporting. | Dropdown (Space Type Code) | Global |  | `space.CodeSpaceTypeID · TEXT` | Space Type Code |
| `CodeSpaceUseID` | Space Use | Select the space use from this field. | Dropdown (Space Use Code) | Global |  | `space.CodeSpaceUseID · TEXT` | Space Use Code |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossArea` | Gross Area | Enter the gross area in this field. | Number | Global |  | `space.GrossArea · TEXT` |  |
| `RentableArea` | Rentable Area | Enter the rentable area in this field. | Number | Global |  | `space.RentableArea · TEXT` |  |
| `SpaceID` | Space RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `space.SpaceID · VARCHAR(64) NOT NULL` |  |
| `TotalHeadCount` | Total Head Count | Enter the total headcount of the space in this field. | Number | Global |  | `space.TotalHeadCount · TEXT` |  |
| `UsableArea` | Usable Area | Enter the usable area. | Number | Global |  | `space.UsableArea · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of this record in this field. | Date | Global |  | `space.EffectiveDate · TEXT` |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ClientNumber` | Client Number | Enter the space number in this field. | Text | Global |  | `space.ClientNumber · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `space.Description · TEXT` |  |
| `FloorNumber` | Floor Number | Enter the floor number of the space in this field. | Text | Global |  | `space.FloorNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `space.Notes · TEXT` |  |
| `RoomNumber` | Room Number | Enter the room number of the space in this field. | Text | Global |  | `space.RoomNumber · TEXT` |  |
| `SpaceName` | Space Name | Enter the name of the space in this field. | Text | Global | yes | `space.SpaceName · TEXT` |  |
| `SuiteNumber` | Suite Number | Enter the suite number of the space in this field. | Text | Global |  | `space.SuiteNumber · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Space ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `space.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `space.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `space.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `space.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `space.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `space.RevNumber · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [Tenant](Tenant.md) | `SpaceID` |
