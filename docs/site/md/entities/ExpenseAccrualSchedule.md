# ExpenseAccrualSchedule

*31 fields · module: Lease Accounting & Payments · Postgres: `expense_accrual_schedule`*

The generated period-by-period accrual schedule from an ExpenseAccrualSetup — accrual rate and annual amount per begin period/year. 30 Global fields under Contract.

Source: `data-fields/expense-accrual-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 30 of 31 inventoried |
| Physical tables | `expense_accrual_schedule` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in expense_accrual_schedule

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 30 fields carry a vendor definition

**Observed.** 30 of this record's 31 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 30 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `expense_accrual_schedule.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `expense_accrual_schedule.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccrualRate` | Accrual Rate | This field is where you enter your accrual rate. If you have entered your rentable area at the contract-level, the system will pre-populate the other payment values after you enter your accrual rate. | Currency | Global |  | `expense_accrual_schedule.AccrualRate · TEXT` |  |
| `AnnualAmount` | Annual Amount | Enter the annual amount of your accrual in this field. The system will automatically calculate the period amount, the accrual rate, the first period amount, and the last period amount. | Currency | Global |  | `expense_accrual_schedule.AnnualAmount · TEXT` |  |
| `DailyAccrualRate` | Daily Accrual Rate | Enter the daily rent expense accrual rate in this field. | Currency | Global |  | `expense_accrual_schedule.DailyAccrualRate · TEXT` |  |
| `FirstPaymentAmount` | First Payment Amount | The system will automatically calculate your first payment when you enter your annual amount in the Annual Amount field. You may modify the value in this field if necessary. | Currency | Global |  | `expense_accrual_schedule.FirstPaymentAmount · TEXT` |  |
| `ForecastAdjustment` | Forecast Adjustment | If you need to make a monetary adjustment to your forecast, enter the forecast adjustment in this field. | Currency | Global |  | `expense_accrual_schedule.ForecastAdjustment · TEXT` |  |
| `LastPaymentAmount` | Last Payment Amount | The system will automatically calculate your last payment when you enter your annual amount in the Annual Amount field. You may modify the value in this field if necessary. | Currency | Global |  | `expense_accrual_schedule.LastPaymentAmount · TEXT` |  |
| `PeriodAmount` | Period Amount | Enter the period amount of your accrual in this field. The system will automatically calculate the annual amount, the accrual rate, the first period amount, and the last period amount. | Currency | Global |  | `expense_accrual_schedule.PeriodAmount · TEXT` |  |
| `PlanAdjustment` | Plan Adjustment | If you need to make a monetary adjustment to your plan, enter the plan adjustment in this field. | Currency | Global |  | `expense_accrual_schedule.PlanAdjustment · TEXT` |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ForecastCapPercent` | Forecast Cap Percent | If you want to put a cap on your forecast, enter the cap percentage in this field. | Percentage | Global |  | `expense_accrual_schedule.ForecastCapPercent · TEXT` |  |
| `ForecastGrowthPercent` | Forecast Growth Percent | If you want to put a cap on the growth of your forecast, enter the cap percentage in this field. | Percentage | Global |  | `expense_accrual_schedule.ForecastGrowthPercent · TEXT` |  |
| `PlanCapPercent` | Plan Cap Percent | If you want to put a cap on your plan, enter the cap percentage in this field. | Percentage | Global |  | `expense_accrual_schedule.PlanCapPercent · TEXT` |  |
| `PlanGrowthPercent` | Plan Growth Percent | If you want to put a cap on the growth of your plan, enter the cap percentage in this field. | Percentage | Global |  | `expense_accrual_schedule.PlanGrowthPercent · TEXT` |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginPeriod` | Begin Period | Select the beginning period from this field. | Number | Global |  | `expense_accrual_schedule.BeginPeriod · TEXT` |  |
| `BeginYear` | Begin Year | Returns name of the last fiscal period for examle 7/2019 | Number | Global |  | `expense_accrual_schedule.BeginYear · TEXT` |  |
| `EndPeriod` | End Period | Select the ending period from this field. | Number | Global |  | `expense_accrual_schedule.EndPeriod · TEXT` |  |
| `EndYear` | End Year | Returns name of the last fiscal period for examle 7/2019 | Number | Global |  | `expense_accrual_schedule.EndYear · TEXT` |  |
| `ExpenseAccrualScheduleID` | Expense Accrual Schedule RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `expense_accrual_schedule.ExpenseAccrualScheduleID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginPeriodName` | Begin Period / Year | The name of the first fiscal period, for example 7/2019. | Date | Global |  | `expense_accrual_schedule.BeginPeriodName · TEXT` |  |
| `EndPeriodName` | End Period / Year | The name of the last fiscal period, for example 7/2019. | Date | Global |  | `expense_accrual_schedule.EndPeriodName · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `expense_accrual_schedule.Description · TEXT` |  |
| `ExpenseAccrualSetupID` | Expense Accrual Setup | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Text | Global | yes | `expense_accrual_schedule.ExpenseAccrualSetupID · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `expense_accrual_schedule.Notes · TEXT` |  |
| `PlanForecastNotes` | Planning and Forecasting Notes | Add any notes about the record. | Text | Global |  | `expense_accrual_schedule.PlanForecastNotes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Accrual Schedule ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `expense_accrual_schedule.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `expense_accrual_schedule.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `expense_accrual_schedule.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `expense_accrual_schedule.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `expense_accrual_schedule.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `expense_accrual_schedule.RevNumber · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [VirtualExpAccrualForecastPeriod](VirtualExpAccrualForecastPeriod.md) | `ExpenseAccrualScheduleID` |
