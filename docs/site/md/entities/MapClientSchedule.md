# MapClientSchedule

*10 fields · module: Platform & Tenancy · Postgres: `map_client_schedule`*

Links a RETransaction/schedule to auto-push forecast behavior and percent-complete tracking.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 10 |
| Fields with a vendor definition | 9 of 10 inventoried |
| Physical tables | `map_client_schedule` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 11 (11 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in map_client_schedule

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 9 fields carry a vendor definition

**Observed.** 9 of this record's 10 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-014](../rules/PLT-R-014.md) | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture | Derived |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `map_client_schedule.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `RETransactionID` | RETransaction | This field is a placeholder for an upcoming feature. | RE Transaction ID | Global |  | `map_client_schedule.RETransactionID · TEXT` | [RETransaction](RETransaction.md) |
| `ScenarioID` | Scenario | This field is a placeholder for an upcoming feature. | Scenario ID | Global |  | `map_client_schedule.ScenarioID · TEXT` | [Scenario](Scenario.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HolidayScheduleID` | Holiday Schedule | Select the default holiday calendar you want to use from this field. | Holiday Calendar | Global |  | `map_client_schedule.HolidayScheduleID · TEXT` |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeTaskStatusID` | Task Status | The value of this field is equal to the aggregate task status for the given schedule. | Dropdown (Task Status Code) | Global |  | `map_client_schedule.CodeTaskStatusID · TEXT` | Task Status Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ComputedPercentComplete` | Percent Complete | Calculates the percentage completion of the schedule. | Number | Global |  | `map_client_schedule.ComputedPercentComplete · TEXT` |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AutoPushForecastEndDate` | Auto Push Forecast End Date? | Select this check box if you want to increment schedule tasks by one day each day that a task is late. This setting only applies to the forecast / actual date. | Boolean | Global | yes | `map_client_schedule.AutoPushForecastEndDate · TEXT` |  |
| `IsCompleted` | Is Completed? | The value of this field will be true is the schedule is completed. | Boolean | Global |  | `map_client_schedule.IsCompleted · TEXT` |  |
| `WorkHolidays` | Work Holidays? | Select this check box if you want the schedule to include holidays as working days. | Boolean | Global | yes | `map_client_schedule.WorkHolidays · TEXT` |  |
| `WorkWeekends` | Work Weekends? | Select this check box if you want the schedule to include weekends as working days. | Boolean | Global | yes | `map_client_schedule.WorkWeekends · TEXT` |  |
