# TaskGroup

*37 fields · module: Capital Projects & Scheduling · Postgres: `task_group`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so nothing in the corpus explains it in the vendor's own words. What is known is structural — 37 declared fields, filed under Capital Projects & Scheduling, 18 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 18 keys from 12 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 9 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [POR-R-016](../rules/POR-R-016.md) | `Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read · `Task/Group ID` FK type · The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, | Derived |
| [PRJ-R-001](../rules/PRJ-R-001.md) | Any object needs to reference a schedule row · `Task/Group ID` FK type · Resolves to `TaskGroup` exclusively — every one of the 18 occurrences of this type across `projects-capital`, `portfolio-transactions`, and `workflow` points at `TaskG | Derived |
| [PRJ-R-002](../rules/PRJ-R-002.md) | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierar | Observed |
| [PRJ-R-005](../rules/PRJ-R-005.md) | A task's dates need working-day calculation · `HolidaySchedule` → `HolidayDate`, `Program.DefaultHolidayScheduleID` (`portfolio-transactions`), `Program.DefaultWorkWeekends`, `TaskGroup.TaskEndsCodeDayOfWeekID` · The portfolio's default cal | Derived |
| [PRJ-R-006](../rules/PRJ-R-006.md) | A `TaskGroup` row's schedule position is computed · `ParentTaskID` (hierarchy) vs. `TaskPredecessor.PredecessorTaskID`/`SuccessorTaskID` (dependency network) · Two independent graphs. | Derived |
| [PRJ-R-007](../rules/PRJ-R-007.md) | The Gantt engine (`TaskGantt2.jsp`) needs a task's critical-path status · `TaskGroup.OnCriticalPath`, `DaysAheadOfSchedule` · Plausibly computed by walking the `TaskPredecessor` graph; no formula or screen confirms the exact computation. | Inferred |
| [PRJ-R-011](../rules/PRJ-R-011.md) | A task needs a named assignee · `LinkTaskMember.MemberID` · Assigns a specific `Member`, alongside `TaskGroup.Assignee_MemberID`'s own direct field — two mechanisms for the same concept exist side by side. · Observed | Observed |
| [PRJ-R-012](../rules/PRJ-R-012.md) | A workflow needs to be triggered by a schedule event · `WorkFlow.KickOffTaskID` → `TaskGroup` · Corroborates the GraphQL `KickOffMethod.TASK` enum value (`graphql-api.md`) — a task reaching some state can kick off a workflow. · Derived | Derived |
| [PRJ-R-013](../rules/PRJ-R-013.md) | A real-estate deal step needs its own schedule · `RETransaction.DealSchedule`/`ActiveDealStepTaskIDList`, `Scenario.DealSchedule`/`ActiveDealStepTaskIDList` (`portfolio-transactions`) · Both reuse `TaskGroup` directly — the deal pipeline ha | Observed |

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

## What points here (18 keys)

| Record type | Via column |
|---|---|
| [RETransaction](RETransaction.md) | `ActiveDealStepTaskIDList`, `DealSchedule` |
| [Scenario](Scenario.md) | `ActiveDealStepTaskIDList`, `DealSchedule` |
| [Task](Task.md) | `ParentTaskID`, `TskPredVal_PredecessorTaskID` |
| [TaskGroup](TaskGroup.md) | `ParentTaskID`, `TskPredVal_PredecessorTaskID` |
| [TaskItem](TaskItem.md) | `ParentTaskID`, `TskPredVal_PredecessorTaskID` |
| [TaskPredecessor](TaskPredecessor.md) | `PredecessorTaskID`, `SuccessorTaskID` |
| [Issue](Issue.md) | `TaskIDList` |
| [LinkTaskByCodeMember](LinkTaskByCodeMember.md) | `TaskID` |
| [LinkTaskMember](LinkTaskMember.md) | `TaskID` |
| [WFStepFullImport](WFStepFullImport.md) | `TaskID` |
| [WorkFlow](WorkFlow.md) | `KickOffTaskID` |
| [WorkFlowStep](WorkFlowStep.md) | `TaskID` |
