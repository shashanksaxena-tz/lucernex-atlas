# TaskItem

*37 fields · module: Capital Projects & Scheduling · Postgres: `task_item`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 37 declared fields, filed under Capital Projects & Scheduling, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [POR-R-016](../rules/POR-R-016.md) | `Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read · `Task/Group ID` FK type · The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, | Derived |
| [PRJ-R-001](../rules/PRJ-R-001.md) | Any object needs to reference a schedule row · `Task/Group ID` FK type · Resolves to `TaskGroup` exclusively — every one of the 18 occurrences of this type across `projects-capital`, `portfolio-transactions`, and `workflow` points at `TaskG | Derived |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Assignee_MemberID` |  | Member ID | — |  | [Member](Member.md) |
| `ParentTaskID` |  | Task/Group ID | — |  | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `TskPredVal_PredecessorTaskID` |  | Task/Group ID | — |  | [TaskGroup](TaskGroup.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeTaskStatusID` |  | Dropdown (Task Status Code) | — |  | Task Status Code |
| `TaskEndsCodeDayOfWeekID` |  | Dropdown (Day Of Week Code) | — |  | Day Of Week Code |

### Quantities (12)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualDuration` |  | Number | — |  |  |
| `ActualResourceUnits` |  | Number | — |  |  |
| `DaysAheadOfSchedule` |  | Number | — |  |  |
| `OriginalDuration` |  | Number | — |  |  |
| `OriginalResourceUnits` |  | Number | — |  |  |
| `PercentComplete` |  | Number | — |  |  |
| `ProjectedDuration` |  | Number | — |  |  |
| `ProjectedResourceUnits` |  | Number | — |  |  |
| `TaskID` |  | Number | — |  |  |
| `TskPredVal_ActualLeadLagDays` |  | Number | — |  |  |
| `TskPredVal_OriginalLeadLagDays` |  | Number | — |  |  |
| `TskPredVal_ProjectedLeadLagDays` |  | Number | — |  |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` |  | Date | — |  |  |
| `ActualStartDate` |  | Date | — |  |  |
| `OriginalEndDate` |  | Date | — |  |  |
| `OriginalStartDate` |  | Date | — |  |  |
| `ProjectedEndDate` |  | Date | — |  |  |
| `ProjectedStartDate` |  | Date | — |  |  |
| `TskDone_ActualEndDate` |  | Date | — |  |  |
| `TskNotDone_ActualEndDate` |  | Date | — |  |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EnableForDashboard` |  | Boolean | — |  |  |
| `EnableForEMail` |  | Boolean | — |  |  |
| `IsTaskGroup` |  | Boolean | — |  |  |
| `OnCriticalPath` |  | Boolean | — |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | — |  |  |
| `EMailMessage` |  | Text | — |  |  |
| `TaskName` |  | Text | — |  |  |
| `TskBAndA_NoAccessorConversion` |  | Text | — |  |  |
| `TskNotDoneCompleted_NoAccessorConversion` |  | Text | — |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
