# VirtualExpenseForecastPeriod

*20 fields · module: Lease Accounting & Payments · Postgres: `virtual_expense_forecast_period`*

A forward-looking forecast of recoverable expense by calendar month/year and expense category, computed rather than stored. 20 Global fields under Contract.

Source: `data-fields/virtual-expense-forecast-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 3 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [CON-R-127](../rules/CON-R-127.md) | Forecast inclusion: only ExpenseSetup rows flagged IncludeInPlanForecast appear in VirtualExpenseForecastPeriod. | Observed |
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | Expense Setup ID | Global |  | [ExpenseSetup](ExpenseSetup.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeExpenseCategoryID` | Expense Category | Dropdown (Expense Category Code) | Global |  | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | Dropdown (Expense Group Code) | Global |  | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | Dropdown (Expense Type Code) | Global |  | Expense Type Code |
| `CodeSLScheduleID` | Straight-Line Schedule | Dropdown (Straight Line Schedule Type) | Global |  | Straight Line Schedule Type |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdjustedPeriodExpense` | Paid / Forecast Period Amount | Currency | Global |  |  |
| `PeriodExpense` | Period Amount | Currency | Global |  |  |
| `RentPaid` | Period Paid Amount | Currency | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CalendarYear` | Calendar Year | Number | Global |  |  |
| `FiscalYear` | Fiscal Year | Number | Global |  |  |
| `Period` | Fiscal Period | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IgnoreAlternateRent` | Ignore Alternate Rent? | Boolean | Global |  |  |
| `InAlternateRent` | In Alternate Rent? | Boolean | Global |  |  |
| `IsCPI` | Is CPI? | Boolean | Global |  |  |
| `IsFiscalForecast` | Is Fiscal Forecast? | Boolean | Global |  |  |
| `IsObligationOnly` | Is Obligation? | Boolean | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MonthName` | Calendar Month | Text | Global |  |  |
