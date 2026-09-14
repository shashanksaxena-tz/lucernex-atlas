# UseBasedRentBreakpoint

*31 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `use_based_rent_breakpoint`*

The tiered-cost-per-unit configuration for usage-based rent, mirroring PercentageRentBreakpoint's structure but keyed to consumption cost rather than sales. 30 Global fields under Contract.

Source: `data-fields/use-based-rent-breakpoint.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 30 of 31 inventoried |
| Physical tables | `use_based_rent_breakpoint` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in use_based_rent_breakpoint

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 30 fields carry a vendor definition

**Observed.** 30 of this record's 31 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `use_based_rent_breakpoint.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `use_based_rent_breakpoint.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeUsageGroupID` | Usage Group | Select the usage group from this field. A Usage Group will be used with one and only one Model Type. The model type of a usage group will impact how your use based rent is calculated. | Dropdown (Usage Group Code) | Global |  | `use_based_rent_breakpoint.CodeUsageGroupID · TEXT` | Usage Group Code |
| `CodeUsageUnitTypeID` | Usage Unit Type | This field can be used to create custom unit types for count-based usage groups. | Dropdown (Usage Unit Type Code) | Global |  | `use_based_rent_breakpoint.CodeUsageUnitTypeID · TEXT` | Usage Unit Type Code |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointCost1` | Breakpoint Cost #1 | Enter the unit resource rent rate for this breakpoint in this field. | Currency | Global |  | `use_based_rent_breakpoint.BreakpointCost1 · TEXT` |  |
| `BreakpointCost2` | Breakpoint Cost #2 | Enter the unit resource rent rate for this breakpoint in this field. | Currency | Global |  | `use_based_rent_breakpoint.BreakpointCost2 · TEXT` |  |
| `BreakpointCost3` | Breakpoint Cost #3 | Enter the unit resource rent rate for this breakpoint in this field. | Currency | Global |  | `use_based_rent_breakpoint.BreakpointCost3 · TEXT` |  |
| `BreakpointCost4` | Breakpoint Cost #4 | Enter the unit resource rent rate for this breakpoint in this field. | Currency | Global |  | `use_based_rent_breakpoint.BreakpointCost4 · TEXT` |  |
| `BreakpointCost5` | Breakpoint Cost #5 | Enter the unit resource rent rate for this breakpoint in this field. | Currency | Global |  | `use_based_rent_breakpoint.BreakpointCost5 · TEXT` |  |
| `BreakpointCost6` | Breakpoint Cost #6 | Enter the unit resource rent rate for this breakpoint in this field. | Currency | Global |  | `use_based_rent_breakpoint.BreakpointCost6 · TEXT` |  |
| `BreakpointCost7` | Breakpoint Cost #7 | Enter the unit resource rent rate for this breakpoint in this field. | Currency | Global |  | `use_based_rent_breakpoint.BreakpointCost7 · TEXT` |  |
| `BreakpointCost8` | Breakpoint Cost #8 | Enter the unit resource rent rate for this breakpoint in this field. | Currency | Global |  | `use_based_rent_breakpoint.BreakpointCost8 · TEXT` |  |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointCount1` | Breakpoint Count #1 | Enter your count threshold for this breakpoint in this field. | Number | Global |  | `use_based_rent_breakpoint.BreakpointCount1 · TEXT` |  |
| `BreakpointCount2` | Breakpoint Count #2 | Enter your count threshold for this breakpoint in this field. | Number | Global |  | `use_based_rent_breakpoint.BreakpointCount2 · TEXT` |  |
| `BreakpointCount3` | Breakpoint Count #3 | Enter your count threshold for this breakpoint in this field. | Number | Global |  | `use_based_rent_breakpoint.BreakpointCount3 · TEXT` |  |
| `BreakpointCount4` | Breakpoint Count #4 | Enter your count threshold for this breakpoint in this field. | Number | Global |  | `use_based_rent_breakpoint.BreakpointCount4 · TEXT` |  |
| `BreakpointCount5` | Breakpoint Count #5 | Enter your count threshold for this breakpoint in this field. | Number | Global |  | `use_based_rent_breakpoint.BreakpointCount5 · TEXT` |  |
| `BreakpointCount6` | Breakpoint Count #6 | Enter your count threshold for this breakpoint in this field. | Number | Global |  | `use_based_rent_breakpoint.BreakpointCount6 · TEXT` |  |
| `BreakpointCount7` | Breakpoint Count #7 | Enter your count threshold for this breakpoint in this field. | Number | Global |  | `use_based_rent_breakpoint.BreakpointCount7 · TEXT` |  |
| `BreakpointCount8` | Breakpoint Count #8 | Enter your count threshold for this breakpoint in this field. | Number | Global |  | `use_based_rent_breakpoint.BreakpointCount8 · TEXT` |  |
| `UseBasedRentBreakpointID` | Use Based Rent Breakpoint RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `use_based_rent_breakpoint.UseBasedRentBreakpointID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `use_based_rent_breakpoint.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `use_based_rent_breakpoint.EndDate · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `use_based_rent_breakpoint.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `use_based_rent_breakpoint.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Use Based Rent Breakpoint ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `use_based_rent_breakpoint.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `use_based_rent_breakpoint.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `use_based_rent_breakpoint.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `use_based_rent_breakpoint.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `use_based_rent_breakpoint.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `use_based_rent_breakpoint.RevNumber · TEXT` |  |
