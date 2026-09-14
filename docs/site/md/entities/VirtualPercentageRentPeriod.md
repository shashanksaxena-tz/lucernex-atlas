# VirtualPercentageRentPeriod

*38 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_percentage_rent_period`*

The computed period-by-period projection of PercentageRentBreakpoint tiers, following the same Virtual-entity pattern as VirtualSalesPeriod. 37 Global fields under Contract.

Source: `data-fields/virtual-percentage-rent-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 38 |
| Fields with a vendor definition | 37 of 38 inventoried |
| Physical tables | `virtual_percentage_rent_period` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_percentage_rent_period

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 37 fields carry a vendor definition

**Observed.** 37 of this record's 38 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-065](../rules/CON-R-065.md) | A natural breakpoint is derived: the configured rate and the effective rate are stored separately as the derivation's own audit trail. | Derived |
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `virtual_percentage_rent_period.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `virtual_percentage_rent_period.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCapFrequencyID` | Cap Frequency | The cap frequency for the percentage rent record. For example, the cap frequency could determine whether a cap is applied monthly, quarterly, or annually. If no cap frequency is specified, the cap amount is assumed to be the amount that applies for each percentage rent payment period. | Dropdown (Frequency Code) | Global |  | `virtual_percentage_rent_period.CodeCapFrequencyID · TEXT` | Frequency Code |
| `CodeSalesGroupID` | Sales Group | The sales group that this percentage rent record is associated with. | Dropdown (Sales Group) | Global |  | `virtual_percentage_rent_period.CodeSalesGroupID · TEXT` | Sales Group |

### Money (11)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualNetSalesAmount` | Current Net Sales Amount | The total Percentage Rent Period Sales amount for actual, non-forecasted periods. | Currency | Global |  | `virtual_percentage_rent_period.ActualNetSalesAmount · TEXT` |  |
| `BreakpointAmount1` | Breakpoint Amount #1 | The breakpoint amount for breakpoint #1. | Currency | Global |  | `virtual_percentage_rent_period.BreakpointAmount1 · TEXT` |  |
| `BreakpointAmount2` | Breakpoint Amount #2 | The breakpoint amount for breakpoint #2. | Currency | Global |  | `virtual_percentage_rent_period.BreakpointAmount2 · TEXT` |  |
| `BreakpointAmount3` | Breakpoint Amount #3 | The breakpoint amount for breakpoint #3. | Currency | Global |  | `virtual_percentage_rent_period.BreakpointAmount3 · TEXT` |  |
| `BreakpointAmount4` | Breakpoint Amount #4 | The breakpoint amount for breakpoint #4. | Currency | Global |  | `virtual_percentage_rent_period.BreakpointAmount4 · TEXT` |  |
| `BreakpointAmount5` | Breakpoint Amount #5 | The breakpoint amount for breakpoint #5. | Currency | Global |  | `virtual_percentage_rent_period.BreakpointAmount5 · TEXT` |  |
| `BreakpointAmount6` | Breakpoint Amount #6 | The breakpoint amount for breakpoint #6. | Currency | Global |  | `virtual_percentage_rent_period.BreakpointAmount6 · TEXT` |  |
| `BreakpointAmount7` | Breakpoint Amount #7 | The breakpoint amount for breakpoint #7. | Currency | Global |  | `virtual_percentage_rent_period.BreakpointAmount7 · TEXT` |  |
| `BreakpointAmount8` | Breakpoint Amount #8 | The breakpoint amount for breakpoint #8. | Currency | Global |  | `virtual_percentage_rent_period.BreakpointAmount8 · TEXT` |  |
| `CapAmount` | Cap Amount | The cap amount for the period. | Currency | Global |  | `virtual_percentage_rent_period.CapAmount · TEXT` |  |
| `FloorAmount` | Floor Amount | The floor amount for the period. | Currency | Global |  | `virtual_percentage_rent_period.FloorAmount · TEXT` |  |

### Rates & percentages (10)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointRate1` | Breakpoint Rate #1 | The payment rate for breakpoint #1. | Percentage | Global |  | `virtual_percentage_rent_period.BreakpointRate1 · TEXT` |  |
| `BreakpointRate2` | Breakpoint Rate #2 | The payment rate for breakpoint #2. | Percentage | Global |  | `virtual_percentage_rent_period.BreakpointRate2 · TEXT` |  |
| `BreakpointRate3` | Breakpoint Rate #3 | The payment rate for breakpoint #3. | Percentage | Global |  | `virtual_percentage_rent_period.BreakpointRate3 · TEXT` |  |
| `BreakpointRate4` | Breakpoint Rate #4 | The payment rate for breakpoint #4. | Percentage | Global |  | `virtual_percentage_rent_period.BreakpointRate4 · TEXT` |  |
| `BreakpointRate5` | Breakpoint Rate #5 | The payment rate for breakpoint #5. | Percentage | Global |  | `virtual_percentage_rent_period.BreakpointRate5 · TEXT` |  |
| `BreakpointRate6` | Breakpoint Rate #6 | The payment rate for breakpoint #6. | Percentage | Global |  | `virtual_percentage_rent_period.BreakpointRate6 · TEXT` |  |
| `BreakpointRate7` | Breakpoint Rate #7 | The payment rate for breakpoint #7. | Percentage | Global |  | `virtual_percentage_rent_period.BreakpointRate7 · TEXT` |  |
| `BreakpointRate8` | Breakpoint Rate #8 | The payment rate for breakpoint #8. | Percentage | Global |  | `virtual_percentage_rent_period.BreakpointRate8 · TEXT` |  |
| `ConfiguredBreakpointRate1` | Configured Breakpoint Rate #1 | The configured rate for breakpoint 1 ignoring any count-based rate adjustments. This value is used in various percent rent calculations to obtain the rent due. | Percentage | Global |  | `virtual_percentage_rent_period.ConfiguredBreakpointRate1 · TEXT` |  |
| `NaturalBreakpointRate` | Natural Breakpoint Rate | The natural breakpoint rate. For more information about natural and artificial breakpoints, see the Lx Online Help. | Percentage | Global |  | `virtual_percentage_rent_period.NaturalBreakpointRate · TEXT` |  |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BreakpointCount1` | Breakpoint Count #1 | The unit count for breakpoint #1. | Number | Global |  | `virtual_percentage_rent_period.BreakpointCount1 · TEXT` |  |
| `BreakpointCount2` | Breakpoint Count #2 | The unit count for breakpoint #2. | Number | Global |  | `virtual_percentage_rent_period.BreakpointCount2 · TEXT` |  |
| `BreakpointCount3` | Breakpoint Count #3 | The unit count for breakpoint #3. | Number | Global |  | `virtual_percentage_rent_period.BreakpointCount3 · TEXT` |  |
| `BreakpointCount4` | Breakpoint Count #4 | The unit count for breakpoint #4. | Number | Global |  | `virtual_percentage_rent_period.BreakpointCount4 · TEXT` |  |
| `BreakpointCount5` | Breakpoint Count #5 | The unit count for breakpoint #5. | Number | Global |  | `virtual_percentage_rent_period.BreakpointCount5 · TEXT` |  |
| `BreakpointCount6` | Breakpoint Count #6 | The unit count for breakpoint #6. | Number | Global |  | `virtual_percentage_rent_period.BreakpointCount6 · TEXT` |  |
| `BreakpointCount7` | Breakpoint Count #7 | The unit count for breakpoint #7. | Number | Global |  | `virtual_percentage_rent_period.BreakpointCount7 · TEXT` |  |
| `BreakpointCount8` | Breakpoint Count #8 | The unit count for breakpoint #8. | Number | Global |  | `virtual_percentage_rent_period.BreakpointCount8 · TEXT` |  |
| `TrailingSalesMultiplier` | Trailing Sales Multiplier | If trailing sales is configured, this field is equal to the multiplier used to compute the Rent Due from what would be due if this were a full percentage rent period. | 5-Digit Number | Global |  | `virtual_percentage_rent_period.TrailingSalesMultiplier · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodBeginDate` | Period Begin Date | The begin date of the percentage rent period. | Date | Global |  | `virtual_percentage_rent_period.PeriodBeginDate · TEXT` |  |
| `PeriodEndDate` | Period End Date | The end date of the percentage rent period. | Date | Global |  | `virtual_percentage_rent_period.PeriodEndDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsPartialTerm` | Is Partial Term? | Indicates whether the percentage rent period is a partial term. This setting is used to determine whether to prorate or use full periods in calculations. | Boolean | Global |  | `virtual_percentage_rent_period.IsPartialTerm · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodDateRange` | Period Date Range | The date range of the period. | Date Range | Global |  | `virtual_percentage_rent_period.PeriodDateRange · TEXT` |  |
