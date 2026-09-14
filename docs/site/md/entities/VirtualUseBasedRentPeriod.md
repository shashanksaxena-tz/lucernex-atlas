# VirtualUseBasedRentPeriod

*23 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_use_based_rent_period`*

The computed period projection of UseBasedRentBreakpoint tiers, following the same Virtual-entity calculation pattern. 22 Global fields under Contract.

Source: `data-fields/virtual-use-based-rent-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Fields with a vendor definition | 22 of 23 inventoried |
| Physical tables | `virtual_use_based_rent_period` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_use_based_rent_period

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 22 fields carry a vendor definition

**Observed.** 22 of this record's 23 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `virtual_use_based_rent_period.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `virtual_use_based_rent_period.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeUsageGroupID` | Usage Group | The usage group for the period. A Usage Group will be used with one and only one Model Type. The model type of a usage group will impact how your use based rent is calculated. | Dropdown (Usage Group Code) | Global |  | `virtual_use_based_rent_period.CodeUsageGroupID · TEXT` | Usage Group Code |
| `CodeUsageUnitTypeID` | Usage Unit Type | This field can be used to create custom unit types for count-based usage groups. | Dropdown (Usage Unit Type Code) | Global |  | `virtual_use_based_rent_period.CodeUsageUnitTypeID · TEXT` | Usage Unit Type Code |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointCost1` | Breakpoint Cost #1 | The cost for breakpoint #1. | Currency | Global |  | `virtual_use_based_rent_period.BreakpointCost1 · TEXT` |  |
| `BreakpointCost2` | Breakpoint Cost #2 | The cost for breakpoint #2. | Currency | Global |  | `virtual_use_based_rent_period.BreakpointCost2 · TEXT` |  |
| `BreakpointCost3` | Breakpoint Cost #3 | The cost for breakpoint #3. | Currency | Global |  | `virtual_use_based_rent_period.BreakpointCost3 · TEXT` |  |
| `BreakpointCost4` | Breakpoint Cost #4 | The cost for breakpoint #4. | Currency | Global |  | `virtual_use_based_rent_period.BreakpointCost4 · TEXT` |  |
| `BreakpointCost5` | Breakpoint Cost #5 | The cost for breakpoint #5. | Currency | Global |  | `virtual_use_based_rent_period.BreakpointCost5 · TEXT` |  |
| `BreakpointCost6` | Breakpoint Cost #6 | The cost for breakpoint #6. | Currency | Global |  | `virtual_use_based_rent_period.BreakpointCost6 · TEXT` |  |
| `BreakpointCost7` | Breakpoint Cost #7 | The cost for breakpoint #7. | Currency | Global |  | `virtual_use_based_rent_period.BreakpointCost7 · TEXT` |  |
| `BreakpointCost8` | Breakpoint Cost #8 | The cost for breakpoint #8. | Currency | Global |  | `virtual_use_based_rent_period.BreakpointCost8 · TEXT` |  |

### Quantities (8)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointCount1` | Breakpoint Count #1 | The count for breakpoint #1. | Number | Global |  | `virtual_use_based_rent_period.BreakpointCount1 · TEXT` |  |
| `BreakpointCount2` | Breakpoint Count #2 | The count for breakpoint #2. | Number | Global |  | `virtual_use_based_rent_period.BreakpointCount2 · TEXT` |  |
| `BreakpointCount3` | Breakpoint Count #3 | The count for breakpoint #3. | Number | Global |  | `virtual_use_based_rent_period.BreakpointCount3 · TEXT` |  |
| `BreakpointCount4` | Breakpoint Count #4 | The count for breakpoint #4. | Number | Global |  | `virtual_use_based_rent_period.BreakpointCount4 · TEXT` |  |
| `BreakpointCount5` | Breakpoint Count #5 | The count for breakpoint #5. | Number | Global |  | `virtual_use_based_rent_period.BreakpointCount5 · TEXT` |  |
| `BreakpointCount6` | Breakpoint Count #6 | The count for breakpoint #6. | Number | Global |  | `virtual_use_based_rent_period.BreakpointCount6 · TEXT` |  |
| `BreakpointCount7` | Breakpoint Count #7 | The count for breakpoint #7. | Number | Global |  | `virtual_use_based_rent_period.BreakpointCount7 · TEXT` |  |
| `BreakpointCount8` | Breakpoint Count #8 | The count for breakpoint #8. | Number | Global |  | `virtual_use_based_rent_period.BreakpointCount8 · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | The period begin date. | Date | Global |  | `virtual_use_based_rent_period.PeriodBeginDate · TEXT` |  |
| `PeriodEndDate` | Period End Date | The period end date. | Date | Global |  | `virtual_use_based_rent_period.PeriodEndDate · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodDateRange` | Period Date Range | The date range for the current period. | Date Range | Global |  | `virtual_use_based_rent_period.PeriodDateRange · TEXT` |  |
