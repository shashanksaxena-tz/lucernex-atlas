# VirtualUseBasedRentPeriod

*23 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_use_based_rent_period`*

The computed period projection of UseBasedRentBreakpoint tiers, following the same Virtual-entity calculation pattern. 22 Global fields under Contract.

Source: `data-fields/virtual-use-based-rent-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Catalogued fields | 22 (22 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
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

### Quantities (8)

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

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | Date | Global |  |  |
| `PeriodEndDate` | Period End Date | Date | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodDateRange` | Period Date Range | Date Range | Global |  |  |
