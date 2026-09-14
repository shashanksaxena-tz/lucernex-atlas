# VirtualExpenseForecastPeriod

*20 fields · module: Lease Accounting & Payments · Postgres: `virtual_expense_forecast_period`*

A forward-looking forecast of recoverable expense by calendar month/year and expense category, computed rather than stored. 20 Global fields under Contract.

Source: `data-fields/virtual-expense-forecast-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Fields with a vendor definition | 20 of 20 inventoried |
| Physical tables | `virtual_expense_forecast_period` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_expense_forecast_period

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 20 fields carry a vendor definition

**Observed.** 20 of this record's 20 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [CON-R-127](../rules/CON-R-127.md) | Forecast inclusion: only ExpenseSetup rows flagged IncludeInPlanForecast appear in VirtualExpenseForecastPeriod. | Observed |
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID associated with the expense forecast. The Contract ID is a unique identifier that belongs to a contract. | Contract ID | Global |  | `virtual_expense_forecast_period.ContractID · TEXT` | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | The ID of the expense setup associated with the expense forecast period. | Expense Setup ID | Global |  | `virtual_expense_forecast_period.ExpenseSetupID · TEXT` | [ExpenseSetup](ExpenseSetup.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeExpenseCategoryID` | Expense Category | The expense category associated with this forecast. The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the grandchildren of groups. | Dropdown (Expense Category Code) | Global |  | `virtual_expense_forecast_period.CodeExpenseCategoryID · TEXT` | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | The expense group associated with this forecast. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `virtual_expense_forecast_period.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The expense type associated with this forecast. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `virtual_expense_forecast_period.CodeExpenseTypeID · TEXT` | Expense Type Code |
| `CodeSLScheduleID` | Straight-Line Schedule | This field returned the linked straight line schedule record. | Dropdown (Straight Line Schedule Type) | Global |  | `virtual_expense_forecast_period.CodeSLScheduleID · TEXT` | Straight Line Schedule Type |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdjustedPeriodExpense` | Paid / Forecast Period Amount | The value of this field is equal to the rent paid amount if it exists or the forecast amount if it doesn't. | Currency | Global |  | `virtual_expense_forecast_period.AdjustedPeriodExpense · TEXT` |  |
| `PeriodExpense` | Period Amount | Calculates the period amount for the expense forecast period. | Currency | Global |  | `virtual_expense_forecast_period.PeriodExpense · TEXT` |  |
| `RentPaid` | Period Paid Amount | The value of this field equals the sum total of all payment transactions within the date range with matching expense groups or expense types. | Currency | Global |  | `virtual_expense_forecast_period.RentPaid · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CalendarYear` | Calendar Year | The calendar year of the expense forecast period. | Number | Global |  | `virtual_expense_forecast_period.CalendarYear · TEXT` |  |
| `FiscalYear` | Fiscal Year | The fiscal year of the expense forecast period. | Number | Global |  | `virtual_expense_forecast_period.FiscalYear · TEXT` |  |
| `Period` | Fiscal Period | The period number of the expense forecast period. | Number | Global |  | `virtual_expense_forecast_period.Period · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The begin date of the expense forecast period. | Date | Global |  | `virtual_expense_forecast_period.BeginDate · TEXT` |  |
| `EndDate` | End Date | The end date of the expense forecast period. | Date | Global |  | `virtual_expense_forecast_period.EndDate · TEXT` |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IgnoreAlternateRent` | Ignore Alternate Rent? | If this value is true, the expense forecast will ignore alternate rent records. | Boolean | Global |  | `virtual_expense_forecast_period.IgnoreAlternateRent · TEXT` |  |
| `InAlternateRent` | In Alternate Rent? | If this value is true, the contract is in alternate rent. | Boolean | Global |  | `virtual_expense_forecast_period.InAlternateRent · TEXT` |  |
| `IsCPI` | Is CPI? | If this value is true, CPI adjustments are included in the forecast amount. | Boolean | Global |  | `virtual_expense_forecast_period.IsCPI · TEXT` |  |
| `IsFiscalForecast` | Is Fiscal Forecast? | The value of this field is true if the period is a fiscal forecast or false if it is a calendar forecast. | Boolean | Global |  | `virtual_expense_forecast_period.IsFiscalForecast · TEXT` |  |
| `IsObligationOnly` | Is Obligation? | If this value is true, the expenses occur before the Obligation Date specified at the contract-level. | Boolean | Global |  | `virtual_expense_forecast_period.IsObligationOnly · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MonthName` | Calendar Month | The month of the expense forecast period. | Text | Global |  | `virtual_expense_forecast_period.MonthName · TEXT` |  |
