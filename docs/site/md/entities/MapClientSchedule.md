# MapClientSchedule

*10 fields · module: Platform & Tenancy · Postgres: `map_client_schedule`*

Links a RETransaction/schedule to auto-push forecast behavior and percent-complete tracking.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 10 |
| Catalogued fields | 11 (11 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PLT-R-014](../rules/PLT-R-014.md) | These are join/marker tables or the export is truncating them; either way, do not model them as one-column tables in the rebuild without a targeted schema-browser capture | Derived |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `RETransactionID` | RETransaction | RE Transaction ID | Global |  | [RETransaction](RETransaction.md) |
| `ScenarioID` | Scenario | Scenario ID | Global |  | [Scenario](Scenario.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HolidayScheduleID` | Holiday Schedule | Holiday Calendar | Global |  |  |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeTaskStatusID` | Task Status | Dropdown (Task Status Code) | Global |  | Task Status Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ComputedPercentComplete` | Percent Complete | Number | Global |  |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AutoPushForecastEndDate` | Auto Push Forecast End Date? | Boolean | Global | yes |  |
| `IsCompleted` | Is Completed? | Boolean | Global |  |  |
| `WorkHolidays` | Work Holidays? | Boolean | Global | yes |  |
| `WorkWeekends` | Work Weekends? | Boolean | Global | yes |  |
