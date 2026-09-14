# VirtualPRAccrualPeriod

*20 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_pr_accrual_period`*

The computed period projection of percentage-rent accrual, showing this-period, prior-periods, and total accrual amounts. 19 Global fields under Contract.

Source: `data-fields/virtual-pr-accrual-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Catalogued fields | 19 (19 global, 0 firm) |
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
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MatchingCalendarMonth` | Matching Calendar Month | Dropdown | Global |  |  |

### Money (6)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccrualAmountPriorPeriods` | Accrual Amount Prior Periods | Currency | Global |  |  |
| `AccrualAmountThisPeriod` | Accrual Amount This Period | Currency | Global |  |  |
| `AccrualAmountTotal` | Accrual Amount Total | Currency | Global |  |  |
| `PostedAccrualAmountPriorPeriods` | Posted Accrual Amount Prior Periods | Currency | Global |  |  |
| `PostedAccrualAmountThisPeriod` | Posted Accrual Amount This Period | Currency | Global |  |  |
| `PostedAccrualAmountTotal` | Posted Accrual Amount Total | Currency | Global |  |  |

### Quantities (6)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MatchingCalendarYear` | Matching Calendar Year | Number | Global |  |  |
| `NumberDaysInPeriod` | Number Days In Period | Number | Global |  |  |
| `NumberWeeksInPeriod` | Number Weeks In Period | Number | Global |  |  |
| `Period` | Fiscal Period | Number | Global |  |  |
| `Quarter` |  | Number | Global |  |  |
| `Year` | Fiscal Year | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `FiscalPeriodNameSort` | Fiscal Period/Year Sort | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsPosted` | Is Posted? | Boolean | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FiscalPeriodName` | Fiscal Period Year | Text | Global |  |  |
