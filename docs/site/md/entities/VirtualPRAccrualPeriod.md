# VirtualPRAccrualPeriod

*20 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_pr_accrual_period`*

The computed period projection of percentage-rent accrual, showing this-period, prior-periods, and total accrual amounts. 19 Global fields under Contract.

Source: `data-fields/virtual-pr-accrual-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Fields with a vendor definition | 18 of 20 inventoried |
| Physical tables | `virtual_pr_accrual_period` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_pr_accrual_period

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 18 fields carry a vendor definition

**Observed.** 18 of this record's 20 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID associated with this record. The Contract ID is a unique identifier that belongs to a contract. | Contract ID | Global |  | `virtual_pr_accrual_period.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `virtual_pr_accrual_period.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MatchingCalendarMonth` | Matching Calendar Month | The matching calendar month (1-12) for this accrual period. | Dropdown | Global |  | `virtual_pr_accrual_period.MatchingCalendarMonth · TEXT` |  |

### Money (6)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccrualAmountPriorPeriods` | Accrual Amount Prior Periods | The accrual amount for prior periods. This value is used in calculating the Accrual Amount Total. | Currency | Global |  | `virtual_pr_accrual_period.AccrualAmountPriorPeriods · TEXT` |  |
| `AccrualAmountThisPeriod` | Accrual Amount This Period | The accrual amount for this period. This value is used in calculating the Accrual Amount Total. | Currency | Global |  | `virtual_pr_accrual_period.AccrualAmountThisPeriod · TEXT` |  |
| `AccrualAmountTotal` | Accrual Amount Total | The total accrual amount for this period. This field is calculated as AccrualAmountPriorPeriods + AccrualAmountThisPeriod. | Currency | Global |  | `virtual_pr_accrual_period.AccrualAmountTotal · TEXT` |  |
| `PostedAccrualAmountPriorPeriods` | Posted Accrual Amount Prior Periods | The posted accrual amount for prior periods. | Currency | Global |  | `virtual_pr_accrual_period.PostedAccrualAmountPriorPeriods · TEXT` |  |
| `PostedAccrualAmountThisPeriod` | Posted Accrual Amount This Period | The posted accrual amount for this period. | Currency | Global |  | `virtual_pr_accrual_period.PostedAccrualAmountThisPeriod · TEXT` |  |
| `PostedAccrualAmountTotal` | Posted Accrual Amount Total | This field is calculated as PostedAccrualAmountPriorPeriods + PostedAccrualAmountThisPeriod. This value is used in calculating accruals for future periods. | Currency | Global |  | `virtual_pr_accrual_period.PostedAccrualAmountTotal · TEXT` |  |

### Quantities (6)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MatchingCalendarYear` | Matching Calendar Year | The matching calendar year for this accrual period. | Number | Global |  | `virtual_pr_accrual_period.MatchingCalendarYear · TEXT` |  |
| `NumberDaysInPeriod` | Number Days In Period | Calculates the number of days in the period. | Number | Global |  | `virtual_pr_accrual_period.NumberDaysInPeriod · TEXT` |  |
| `NumberWeeksInPeriod` | Number Weeks In Period | Calculates the number of weeks in the period. | Number | Global |  | `virtual_pr_accrual_period.NumberWeeksInPeriod · TEXT` |  |
| `Period` | Fiscal Period | The fiscal period of the percentage rent accrual period. | Number | Global |  | `virtual_pr_accrual_period.Period · TEXT` |  |
| `Quarter` |  | The quarter of the percentage rent accrual period. | Number | Global |  | `virtual_pr_accrual_period.Quarter · TEXT` |  |
| `Year` | Fiscal Year | The fiscal year of the percentage rent accrual period. | Number | Global |  | `virtual_pr_accrual_period.Year · TEXT` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The begin date of the percentage rent accrual period. | Date | Global |  | `virtual_pr_accrual_period.BeginDate · TEXT` |  |
| `EndDate` | End Date | The end date of the percentage rent accrual period. | Date | Global |  | `virtual_pr_accrual_period.EndDate · TEXT` |  |
| `FiscalPeriodNameSort` | Fiscal Period/Year Sort |  | Date | Global |  | `virtual_pr_accrual_period.FiscalPeriodNameSort · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsPosted` | Is Posted? | Indicates whether the accrual period is posted. | Boolean | Global |  | `virtual_pr_accrual_period.IsPosted · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FiscalPeriodName` | Fiscal Period Year | The period and year for the accrual period. | Text | Global |  | `virtual_pr_accrual_period.FiscalPeriodName · TEXT` |  |
