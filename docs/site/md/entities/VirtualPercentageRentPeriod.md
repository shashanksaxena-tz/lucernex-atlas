# VirtualPercentageRentPeriod

*38 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_percentage_rent_period`*

The computed period-by-period projection of PercentageRentBreakpoint tiers, following the same Virtual-entity pattern as VirtualSalesPeriod. 37 Global fields under Contract.

Source: `data-fields/virtual-percentage-rent-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 38 |
| Catalogued fields | 37 (37 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-065](../rules/CON-R-065.md) | A natural breakpoint is derived: the configured rate and the effective rate are stored separately as the derivation's own audit trail. | Derived |
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
| `CodeCapFrequencyID` | Cap Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |

### Money (11)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualNetSalesAmount` | Current Net Sales Amount | Currency | Global |  |  |
| `BreakpointAmount1` | Breakpoint Amount #1 | Currency | Global |  |  |
| `BreakpointAmount2` | Breakpoint Amount #2 | Currency | Global |  |  |
| `BreakpointAmount3` | Breakpoint Amount #3 | Currency | Global |  |  |
| `BreakpointAmount4` | Breakpoint Amount #4 | Currency | Global |  |  |
| `BreakpointAmount5` | Breakpoint Amount #5 | Currency | Global |  |  |
| `BreakpointAmount6` | Breakpoint Amount #6 | Currency | Global |  |  |
| `BreakpointAmount7` | Breakpoint Amount #7 | Currency | Global |  |  |
| `BreakpointAmount8` | Breakpoint Amount #8 | Currency | Global |  |  |
| `CapAmount` | Cap Amount | Currency | Global |  |  |
| `FloorAmount` | Floor Amount | Currency | Global |  |  |

### Rates & percentages (10)

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
| `ConfiguredBreakpointRate1` | Configured Breakpoint Rate #1 | Percentage | Global |  |  |
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
| `TrailingSalesMultiplier` | Trailing Sales Multiplier | 5-Digit Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | Date | Global |  |  |
| `PeriodEndDate` | Period End Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsPartialTerm` | Is Partial Term? | Boolean | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PeriodDateRange` | Period Date Range | Date Range | Global |  |  |
