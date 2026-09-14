# ExpenseAccrualSchedule

*31 fields · module: Lease Accounting & Payments · Postgres: `expense_accrual_schedule`*

The generated period-by-period accrual schedule from an ExpenseAccrualSetup — accrual rate and annual amount per begin period/year. 30 Global fields under Contract.

Source: `data-fields/expense-accrual-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-052](../rules/ACC-R-052.md) | entering any one of annual amount / period amount / accrual rate auto-populates the other two plus `FirstPaymentAmount` and `LastPaymentAmount`. Rate-based entry requires `RentableArea` to be populated — "If you are not going to use rentabl | Observed |
| [CON-R-121](../rules/CON-R-121.md) | An accrual schedule is generated: period-by-period accrual amounts are produced from AccrualRate/DailyAccrualRate, with the same daily-rate support as recurring expense. | Observed |
| [CON-R-122](../rules/CON-R-122.md) | Accruals are forecast: ForecastCapPercent/ForecastGrowthPercent/ForecastAdjustment and their Plan* twins grow the accrual independently of the contract's own escalation. | Observed |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccrualRate` | Accrual Rate | Currency | Global |  |  |
| `AnnualAmount` | Annual Amount | Currency | Global |  |  |
| `DailyAccrualRate` | Daily Accrual Rate | Currency | Global |  |  |
| `FirstPaymentAmount` | First Payment Amount | Currency | Global |  |  |
| `ForecastAdjustment` | Forecast Adjustment | Currency | Global |  |  |
| `LastPaymentAmount` | Last Payment Amount | Currency | Global |  |  |
| `PeriodAmount` | Period Amount | Currency | Global |  |  |
| `PlanAdjustment` | Plan Adjustment | Currency | Global |  |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ForecastCapPercent` | Forecast Cap Percent | Percentage | Global |  |  |
| `ForecastGrowthPercent` | Forecast Growth Percent | Percentage | Global |  |  |
| `PlanCapPercent` | Plan Cap Percent | Percentage | Global |  |  |
| `PlanGrowthPercent` | Plan Growth Percent | Percentage | Global |  |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginPeriod` | Begin Period | Number | Global |  |  |
| `BeginYear` | Begin Year | Number | Global |  |  |
| `EndPeriod` | End Period | Number | Global |  |  |
| `EndYear` | End Year | Number | Global |  |  |
| `ExpenseAccrualScheduleID` | Expense Accrual Schedule RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginPeriodName` | Begin Period / Year | Date | Global |  |  |
| `EndPeriodName` | End Period / Year | Date | Global |  |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `ExpenseAccrualSetupID` | Expense Accrual Setup | Text | Global | yes |  |
| `Notes` |  | Text | Global |  |  |
| `PlanForecastNotes` | Planning and Forecasting Notes | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Accrual Schedule ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [VirtualExpAccrualForecastPeriod](VirtualExpAccrualForecastPeriod.md) | `ExpenseAccrualScheduleID` |
