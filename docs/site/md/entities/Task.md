# Task

*37 fields · module: Capital Projects & Scheduling · Postgres: `task`*

A schedule/project task record — baseline vs. actual dates and durations, lead/lag days, and resource unit tracking, the core row of the project-scheduling module (paired with TaskPredecessor for dependency chains). 37 Global fields under Schedule and Statics.

Source: `data-fields/task.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Catalogued fields | 37 (37 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 5 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [WF-R-016](../rules/WF-R-016.md) | When the named schedule task completes, a WorkFlow row is created with KickOffTaskID pointing at it. | Observed |
| [WF-R-040](../rules/WF-R-040.md) | Vendor definition: "set the work flow step status to 'In Process' when the step starts." Whether this writes Task.CodeTaskStatusID or WorkFlowStep.CodeWorkFlowStatusID is contradicted between the field label and its own definition (OQ-29). | Observed |
| [LAY-R-008](../rules/LAY-R-008.md) | A Work Flow is an ordered sequence of steps, each of type `Form` or `Task`. A `Form` step binds one of the form type's layouts. | Derived |
| [POR-R-016](../rules/POR-R-016.md) | `Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read · `Task/Group ID` FK type · The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, | Derived |
| [PRJ-R-001](../rules/PRJ-R-001.md) | Any object needs to reference a schedule row · `Task/Group ID` FK type · Resolves to `TaskGroup` exclusively — every one of the 18 occurrences of this type across `projects-capital`, `portfolio-transactions`, and `workflow` points at `TaskG | Derived |

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Assignee_MemberID` | Resources | Member ID | Global |  | [Member](Member.md) |
| `ParentTaskID` | Parent Task | Task/Group ID | Global |  | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `TskPredVal_PredecessorTaskID` | Predecessor Task(s) | Task/Group ID | Global |  | [TaskGroup](TaskGroup.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeTaskStatusID` | Task Status | Dropdown (Task Status Code) | Global |  | Task Status Code |
| `TaskEndsCodeDayOfWeekID` | Task Ends On Day | Dropdown (Day Of Week Code) | Global |  | Day Of Week Code |

### Quantities (12)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualDuration` | Forecast/Actual Duration | Number | Global |  |  |
| `ActualResourceUnits` | Actual Resource Units | Number | Global |  |  |
| `DaysAheadOfSchedule` | Days Ahead of Schedule | Number | Global |  |  |
| `OriginalDuration` | Baseline Duration | Number | Global |  |  |
| `OriginalResourceUnits` | Original Resource Units | Number | Global |  |  |
| `PercentComplete` | Percent Complete | Number | Global |  |  |
| `ProjectedDuration` | Projected Duration | Number | Global |  |  |
| `ProjectedResourceUnits` | Projected Resource Units | Number | Global |  |  |
| `TaskID` | Task RecID | Number | Global |  |  |
| `TskPredVal_ActualLeadLagDays` | Forecast/Actual Lead/Lag Days | Number | Global |  |  |
| `TskPredVal_OriginalLeadLagDays` | Baseline Lead/Lag Days | Number | Global |  |  |
| `TskPredVal_ProjectedLeadLagDays` | Projected Lead/Lag Days | Number | Global |  |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` | Forecast/Actual End Date | Date | Global |  |  |
| `ActualStartDate` | Forecast/Actual Start Date | Date | Global |  |  |
| `OriginalEndDate` | Baseline End Date | Date | Global |  |  |
| `OriginalStartDate` | Baseline Start Date | Date | Global |  |  |
| `ProjectedEndDate` | Projected End Date | Date | Global |  |  |
| `ProjectedStartDate` | Projected Start Date | Date | Global |  |  |
| `TskDone_ActualEndDate` | Actual End Date | Date | Global |  |  |
| `TskNotDone_ActualEndDate` | Forecast End Date | Date | Global |  |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EnableForDashboard` | Alert when task Completes | Boolean | Global |  |  |
| `EnableForEMail` | Email when task Completes | Boolean | Global |  |  |
| `IsTaskGroup` | Is Task Group | Boolean | Global | yes |  |
| `OnCriticalPath` | On Critical Path? | Boolean | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `EMailMessage` | Email Message | Text | Global |  |  |
| `TaskName` | Name | Text | Global | yes |  |
| `TskBAndA_NoAccessorConversion` | Baseline with Forecast/Actual End Date | Text | Global |  |  |
| `TskNotDoneCompleted_NoAccessorConversion` | Forecast End Date/Complete | Text | Global |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
