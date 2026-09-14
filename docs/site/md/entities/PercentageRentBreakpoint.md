# PercentageRentBreakpoint

*40 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `percentage_rent_breakpoint`*

The natural-breakpoint configuration for a percentage-rent clause — up to eight numbered Breakpoint Amount/Count slots defining the sales tiers at which the percentage rate changes. 39 Global fields under Contract, the static configuration that VirtualPercentageRentPeriod projects forward period by period.

Source: `data-fields/percentage-rent-breakpoint.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 40 |
| Catalogued fields | 39 (39 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodePortionedSalesGroupID` | Portioned Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |
| `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BreakpointAmount1` | Breakpoint Amount #1 | Currency | Global |  |  |
| `BreakpointAmount2` | Breakpoint Amount #2 | Currency | Global |  |  |
| `BreakpointAmount3` | Breakpoint Amount #3 | Currency | Global |  |  |
| `BreakpointAmount4` | Breakpoint Amount #4 | Currency | Global |  |  |
| `BreakpointAmount5` | Breakpoint Amount #5 | Currency | Global |  |  |
| `BreakpointAmount6` | Breakpoint Amount #6 | Currency | Global |  |  |
| `BreakpointAmount7` | Breakpoint Amount #7 | Currency | Global |  |  |
| `BreakpointAmount8` | Breakpoint Amount #8 | Currency | Global |  |  |

### Rates & percentages (9)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BreakpointRate1` | Breakpoint Rate #1 | Percentage | Global |  |  |
| `BreakpointRate2` | Breakpoint Rate #2 | Percentage | Global |  |  |
| `BreakpointRate3` | Breakpoint Rate #3 | Percentage | Global |  |  |
| `BreakpointRate4` | Breakpoint Rate #4 | Percentage | Global |  |  |
| `BreakpointRate5` | Breakpoint Rate #5 | Percentage | Global |  |  |
| `BreakpointRate6` | Breakpoint Rate #6 | Percentage | Global |  |  |
| `BreakpointRate7` | Breakpoint Rate #7 | Percentage | Global |  |  |
| `BreakpointRate8` | Breakpoint Rate #8 | Percentage | Global |  |  |
| `NaturalBreakpointRate` | Natural Breakpoint Rate | Percentage | Global |  |  |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BreakpointCount1` | Breakpoint Count #1 | Number | Global |  |  |
| `BreakpointCount2` | Breakpoint Count #2 | Number | Global |  |  |
| `BreakpointCount3` | Breakpoint Count #3 | Number | Global |  |  |
| `BreakpointCount4` | Breakpoint Count #4 | Number | Global |  |  |
| `BreakpointCount5` | Breakpoint Count #5 | Number | Global |  |  |
| `BreakpointCount6` | Breakpoint Count #6 | Number | Global |  |  |
| `BreakpointCount7` | Breakpoint Count #7 | Number | Global |  |  |
| `BreakpointCount8` | Breakpoint Count #8 | Number | Global |  |  |
| `PercentageRentBreakpointID` | Percentage Rent Breakpoint RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Percentage Rent Breakpoint ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
