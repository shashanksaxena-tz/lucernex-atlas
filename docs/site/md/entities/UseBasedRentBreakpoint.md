# UseBasedRentBreakpoint

*31 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `use_based_rent_breakpoint`*

The tiered-cost-per-unit configuration for usage-based rent, mirroring PercentageRentBreakpoint's structure but keyed to consumption cost rather than sales. 30 Global fields under Contract.

Source: `data-fields/use-based-rent-breakpoint.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Catalogued fields | 30 (30 global, 0 firm) |
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
| `CodeUsageGroupID` | Usage Group | Dropdown (Usage Group Code) | Global |  | Usage Group Code |
| `CodeUsageUnitTypeID` | Usage Unit Type | Dropdown (Usage Unit Type Code) | Global |  | Usage Unit Type Code |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BreakpointCost1` | Breakpoint Cost #1 | Currency | Global |  |  |
| `BreakpointCost2` | Breakpoint Cost #2 | Currency | Global |  |  |
| `BreakpointCost3` | Breakpoint Cost #3 | Currency | Global |  |  |
| `BreakpointCost4` | Breakpoint Cost #4 | Currency | Global |  |  |
| `BreakpointCost5` | Breakpoint Cost #5 | Currency | Global |  |  |
| `BreakpointCost6` | Breakpoint Cost #6 | Currency | Global |  |  |
| `BreakpointCost7` | Breakpoint Cost #7 | Currency | Global |  |  |
| `BreakpointCost8` | Breakpoint Cost #8 | Currency | Global |  |  |

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
| `UseBasedRentBreakpointID` | Use Based Rent Breakpoint RecID | Number | Global |  |  |

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
| `BOMapClientRecordID` | Use Based Rent Breakpoint ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
