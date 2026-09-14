# PercentageRentBreakpoint

*40 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `percentage_rent_breakpoint`*

The natural-breakpoint configuration for a percentage-rent clause — up to eight numbered Breakpoint Amount/Count slots defining the sales tiers at which the percentage rate changes. 39 Global fields under Contract, the static configuration that VirtualPercentageRentPeriod projects forward period by period.

Source: `data-fields/percentage-rent-breakpoint.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 40 |
| Fields with a vendor definition | 39 of 40 inventoried |
| Physical tables | `percentage_rent_breakpoint` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 39 (39 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in percentage_rent_breakpoint

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 39 fields carry a vendor definition

**Observed.** 39 of this record's 40 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `percentage_rent_breakpoint.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `percentage_rent_breakpoint.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodePortionedSalesGroupID` | Portioned Sales Group | Select the portioned sales group from this field. For more information about Portioned Sales Groups, see the Lx Online Help. | Dropdown (Sales Group) | Global |  | `percentage_rent_breakpoint.CodePortionedSalesGroupID · TEXT` | Sales Group |
| `CodeSalesGroupID` | Sales Group | Select the sales group from this field. | Dropdown (Sales Group) | Global |  | `percentage_rent_breakpoint.CodeSalesGroupID · TEXT` | Sales Group |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointAmount1` | Breakpoint Amount #1 | Enter the breakpoint amount in this field. | Currency | Global |  | `percentage_rent_breakpoint.BreakpointAmount1 · TEXT` |  |
| `BreakpointAmount2` | Breakpoint Amount #2 | Enter the breakpoint amount in this field. | Currency | Global |  | `percentage_rent_breakpoint.BreakpointAmount2 · TEXT` |  |
| `BreakpointAmount3` | Breakpoint Amount #3 | Enter the breakpoint amount in this field. | Currency | Global |  | `percentage_rent_breakpoint.BreakpointAmount3 · TEXT` |  |
| `BreakpointAmount4` | Breakpoint Amount #4 | Enter the breakpoint amount in this field. | Currency | Global |  | `percentage_rent_breakpoint.BreakpointAmount4 · TEXT` |  |
| `BreakpointAmount5` | Breakpoint Amount #5 | Enter the breakpoint amount in this field. | Currency | Global |  | `percentage_rent_breakpoint.BreakpointAmount5 · TEXT` |  |
| `BreakpointAmount6` | Breakpoint Amount #6 | Enter the breakpoint amount in this field. | Currency | Global |  | `percentage_rent_breakpoint.BreakpointAmount6 · TEXT` |  |
| `BreakpointAmount7` | Breakpoint Amount #7 | Enter the breakpoint amount in this field. | Currency | Global |  | `percentage_rent_breakpoint.BreakpointAmount7 · TEXT` |  |
| `BreakpointAmount8` | Breakpoint Amount #8 | Enter the breakpoint amount in this field. | Currency | Global |  | `percentage_rent_breakpoint.BreakpointAmount8 · TEXT` |  |

### Rates & percentages (9)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointRate1` | Breakpoint Rate #1 | Enter the payment rate for the associated breakpoint in this field. | Percentage | Global |  | `percentage_rent_breakpoint.BreakpointRate1 · TEXT` |  |
| `BreakpointRate2` | Breakpoint Rate #2 | Enter the payment rate for the associated breakpoint in this field. | Percentage | Global |  | `percentage_rent_breakpoint.BreakpointRate2 · TEXT` |  |
| `BreakpointRate3` | Breakpoint Rate #3 | Enter the payment rate for the associated breakpoint in this field. | Percentage | Global |  | `percentage_rent_breakpoint.BreakpointRate3 · TEXT` |  |
| `BreakpointRate4` | Breakpoint Rate #4 | Enter the payment rate for the associated breakpoint in this field. | Percentage | Global |  | `percentage_rent_breakpoint.BreakpointRate4 · TEXT` |  |
| `BreakpointRate5` | Breakpoint Rate #5 | Enter the payment rate for the associated breakpoint in this field. | Percentage | Global |  | `percentage_rent_breakpoint.BreakpointRate5 · TEXT` |  |
| `BreakpointRate6` | Breakpoint Rate #6 | Enter the payment rate for the associated breakpoint in this field. | Percentage | Global |  | `percentage_rent_breakpoint.BreakpointRate6 · TEXT` |  |
| `BreakpointRate7` | Breakpoint Rate #7 | Enter the payment rate for the associated breakpoint in this field. | Percentage | Global |  | `percentage_rent_breakpoint.BreakpointRate7 · TEXT` |  |
| `BreakpointRate8` | Breakpoint Rate #8 | Enter the payment rate for the associated breakpoint in this field. | Percentage | Global |  | `percentage_rent_breakpoint.BreakpointRate8 · TEXT` |  |
| `NaturalBreakpointRate` | Natural Breakpoint Rate | Enter your natural rate in this field. Your natural rate is the percent of each dollar you must allocate to meeting your base rent. After you meet your base rent, you will begin to pay your percentage rent. For example, if a tenant knows that for every dollar they make, 5% or 5 cents of that dollar must go to base rent, they would enter their natural rate as .05. | Percentage | Global |  | `percentage_rent_breakpoint.NaturalBreakpointRate · TEXT` |  |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointCount1` | Breakpoint Count #1 | Enter the number of units that must be sold to meet the breakpoint in this field. | Number | Global |  | `percentage_rent_breakpoint.BreakpointCount1 · TEXT` |  |
| `BreakpointCount2` | Breakpoint Count #2 | Enter the number of units that must be sold to meet the breakpoint in this field. | Number | Global |  | `percentage_rent_breakpoint.BreakpointCount2 · TEXT` |  |
| `BreakpointCount3` | Breakpoint Count #3 | Enter the number of units that must be sold to meet the breakpoint in this field. | Number | Global |  | `percentage_rent_breakpoint.BreakpointCount3 · TEXT` |  |
| `BreakpointCount4` | Breakpoint Count #4 | Enter the number of units that must be sold to meet the breakpoint in this field. | Number | Global |  | `percentage_rent_breakpoint.BreakpointCount4 · TEXT` |  |
| `BreakpointCount5` | Breakpoint Count #5 | Enter the number of units that must be sold to meet the breakpoint in this field. | Number | Global |  | `percentage_rent_breakpoint.BreakpointCount5 · TEXT` |  |
| `BreakpointCount6` | Breakpoint Count #6 | Enter the number of units that must be sold to meet the breakpoint in this field. | Number | Global |  | `percentage_rent_breakpoint.BreakpointCount6 · TEXT` |  |
| `BreakpointCount7` | Breakpoint Count #7 | Enter the number of units that must be sold to meet the breakpoint in this field. | Number | Global |  | `percentage_rent_breakpoint.BreakpointCount7 · TEXT` |  |
| `BreakpointCount8` | Breakpoint Count #8 | Enter the number of units that must be sold to meet the breakpoint in this field. | Number | Global |  | `percentage_rent_breakpoint.BreakpointCount8 · TEXT` |  |
| `PercentageRentBreakpointID` | Percentage Rent Breakpoint RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `percentage_rent_breakpoint.PercentageRentBreakpointID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `percentage_rent_breakpoint.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `percentage_rent_breakpoint.EndDate · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `percentage_rent_breakpoint.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `percentage_rent_breakpoint.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Percentage Rent Breakpoint ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `percentage_rent_breakpoint.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `percentage_rent_breakpoint.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `percentage_rent_breakpoint.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `percentage_rent_breakpoint.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `percentage_rent_breakpoint.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `percentage_rent_breakpoint.RevNumber · TEXT` |  |
