# VirtualExpAccrualForecastPeriod

*13 fields · module: Lease Accounting & Payments · Postgres: `virtual_exp_accrual_forecast_period`*

A computed forward forecast of an expense accrual by period, referencing the ExpenseAccrualSchedule/Setup it projects from.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Fields with a vendor definition | 13 of 13 inventoried |
| Physical tables | `virtual_exp_accrual_forecast_period` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 13 (13 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in virtual_exp_accrual_forecast_period

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 13 fields carry a vendor definition

**Observed.** 13 of this record's 13 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. Loaded per parent from contract_admin.ContractID That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID associated with the expense accrual period. The Contract ID is a unique identifier that belongs to a contract. | Contract ID | Global |  | `virtual_exp_accrual_forecast_period.ContractID · TEXT` | [Contract](Contract.md) |
| `ExpenseAccrualScheduleID` | Accrual Schedule | The ID of the expense accrual schedule record. | Expense Accrual Schedule ID | Global |  | `virtual_exp_accrual_forecast_period.ExpenseAccrualScheduleID · TEXT` | [ExpenseAccrualSchedule](ExpenseAccrualSchedule.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAccrualTypeID` | Accrual Type | The accrual type of the expense accrual forecast period record. | Dropdown (Accrual Type Code) | Global |  | `virtual_exp_accrual_forecast_period.CodeAccrualTypeID · TEXT` | Accrual Type Code |
| `CodeExpenseCategoryID` | Expense Category | The expense category associated with this accrual. The Expense Category field allows you to associate your record with a pre-configured expense category. Categories are the children of types, and the grandchildren of groups. | Dropdown (Expense Category Code) | Global |  | `virtual_exp_accrual_forecast_period.CodeExpenseCategoryID · TEXT` | Expense Category Code |
| `CodeExpenseGroupID` | Expense Group | The expense group associated with this accrual. Expense groups are used to categorize expense types. | Dropdown (Expense Group Code) | Global |  | `virtual_exp_accrual_forecast_period.CodeExpenseGroupID · TEXT` | Expense Group Code |
| `CodeExpenseTypeID` | Expense Type | The expense type associated with this accrual. Expense Types are used to associate records with lease accounting schedules, AP export numbers, expense accrual accounts, percentage rent accrual accounts, and real estate tax accounts. | Dropdown (Expense Type Code) | Global |  | `virtual_exp_accrual_forecast_period.CodeExpenseTypeID · TEXT` | Expense Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PeriodExpense` | Period Amount | This field computes the total expenses for the period. | Currency | Global |  | `virtual_exp_accrual_forecast_period.PeriodExpense · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Period` | Fiscal Period | The fiscal period of the accrual. | Number | Global |  | `virtual_exp_accrual_forecast_period.Period · TEXT` |  |
| `Year` | Fiscal Year | The fiscal year of the accrual. | Number | Global |  | `virtual_exp_accrual_forecast_period.Year · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The begin date of the expense accrual forecast period. | Date | Global |  | `virtual_exp_accrual_forecast_period.BeginDate · TEXT` |  |
| `EndDate` | End Date | The total expenses for the period. | Date | Global |  | `virtual_exp_accrual_forecast_period.EndDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExpenseAccrualSetupID` | Accrual Setup | The ID of the expense accrual setup record. | Text | Global |  | `virtual_exp_accrual_forecast_period.ExpenseAccrualSetupID · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DateRange` | Date Range | This field computes the date range of the expense accrual forecast period. | Date Range | Global |  | `virtual_exp_accrual_forecast_period.DateRange · TEXT` |  |
