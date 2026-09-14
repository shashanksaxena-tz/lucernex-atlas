# TaskGroup

*37 fields · module: Capital Projects & Scheduling · Postgres: `task_group`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 37 declared fields, filed under Capital Projects & Scheduling, 18 foreign keys pointing at it. Its fields are documented even though the record is not: 36 of its 37 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Fields with a vendor definition | 36 of 37 inventoried |
| Physical tables | `task_group` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 18 keys from 12 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 9 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in task_group

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 36 fields carry a vendor definition

**Observed.** 36 of this record's 37 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 0; 0 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Assignee_MemberID` | Resources | The member ID of the task assignee. | Member ID | — |  | `task_group.Assignee_MemberID · TEXT` | [Member](Member.md) |
| `ParentTaskID` | Parent Task | The ID of the parent task of the given task. | Task/Group ID | — |  | `task_group.ParentTaskID · TEXT` | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `task_group.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `TskPredVal_PredecessorTaskID` | Predecessor Task(s) | The ID of the predecessor task of a given task. | Task/Group ID | — |  | `task_group.TskPredVal_PredecessorTaskID · TEXT` | [TaskGroup](TaskGroup.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeTaskStatusID` | Task Status | The status of the task group. | Dropdown (Task Status Code) | — |  | `task_group.CodeTaskStatusID · TEXT` | Task Status Code |
| `TaskEndsCodeDayOfWeekID` | Task Ends On Day | The day of the week that the task ends. | Dropdown (Day Of Week Code) | — |  | `task_group.TaskEndsCodeDayOfWeekID · TEXT` | Day Of Week Code |

### Quantities (12)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualDuration` | Forecast/Actual Duration | The number of days this group of tasks is predicted to take. | Number | — |  | `task_group.ActualDuration · TEXT` |  |
| `ActualResourceUnits` | Actual Resource Units | The total actual resource units of the task group. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. | Number | — |  | `task_group.ActualResourceUnits · TEXT` |  |
| `DaysAheadOfSchedule` | Days Ahead of Schedule | The value of this field equals the original / baseline end date - the actual end date. | Number | — |  | `task_group.DaysAheadOfSchedule · TEXT` |  |
| `OriginalDuration` | Baseline Duration | The original or baseline duration of the task. This field's value cannot be negative. | Number | — |  | `task_group.OriginalDuration · TEXT` |  |
| `OriginalResourceUnits` | Original Resource Units | The total original resource units of the task group. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. | Number | — |  | `task_group.OriginalResourceUnits · TEXT` |  |
| `PercentComplete` | Percent Complete | Calculates the percentage completion of the task group. | Number | — |  | `task_group.PercentComplete · TEXT` |  |
| `ProjectedDuration` | Projected Duration | Calculates the projected duration of the task group. | Number | — |  | `task_group.ProjectedDuration · TEXT` |  |
| `ProjectedResourceUnits` | Projected Resource Units | The total projected resource units of the task group. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. | Number | — |  | `task_group.ProjectedResourceUnits · TEXT` |  |
| `TaskID` | Task RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | `task_group.TaskID · VARCHAR(64) NOT NULL` |  |
| `TskPredVal_ActualLeadLagDays` | Forecast/Actual Lead/Lag Days | This field computes the actual lead / lag days of this task's predecessor. This value is used when a task checks if all of its predecessors have completed (where all of their lead days are < 0). | Number | — |  | `task_group.TskPredVal_ActualLeadLagDays · TEXT` |  |
| `TskPredVal_OriginalLeadLagDays` | Baseline Lead/Lag Days | The original lead / lag days of the task predecessor. | Number | — |  | `task_group.TskPredVal_OriginalLeadLagDays · TEXT` |  |
| `TskPredVal_ProjectedLeadLagDays` | Projected Lead/Lag Days | The number of lead or lag days of the predecessor task. | Number | — |  | `task_group.TskPredVal_ProjectedLeadLagDays · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Forecast/Actual End Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | — |  | `task_group.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | — |  | `task_group.ActualStartDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `task_group.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `task_group.OriginalStartDate · TEXT` |  |
| `ProjectedEndDate` | Projected End Date | Enter the end date you are aiming for in this field. You can think of your projected dates as your goal dates. | Date | — |  | `task_group.ProjectedEndDate · TEXT` |  |
| `ProjectedStartDate` | Projected Start Date | Enter the start date you are aiming for in this field. You can think of your projected dates as your goal dates. | Date | — |  | `task_group.ProjectedStartDate · TEXT` |  |
| `TskDone_ActualEndDate` | Actual End Date | The task end date. If a task is canceled, this field will either be blank or will contain the word "canceled". | Date | — |  | `task_group.TskDone_ActualEndDate · TEXT` |  |
| `TskNotDone_ActualEndDate` | Forecast End Date | The forecasted end date of the task. This field only displays for non-complete tasks. | Date | — |  | `task_group.TskNotDone_ActualEndDate · TEXT` |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EnableForDashboard` | Alert when task Completes | This flag is used to determine if the dashboard will receive an alert when the task is completed. | Boolean | — |  | `task_group.EnableForDashboard · TEXT` |  |
| `EnableForEMail` | Email when task Completes | This flag is used to determine if an email will be sent when the task is completed. | Boolean | — |  | `task_group.EnableForEMail · TEXT` |  |
| `IsTaskGroup` | Is Task Group | If this value is true, the record is a task group. If this value is false, this record is a task. | Boolean | — | yes | `task_group.IsTaskGroup · TEXT` |  |
| `OnCriticalPath` | On Critical Path? | This flag indicates whether the task is on a critical path or not. | Boolean | — |  | `task_group.OnCriticalPath · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | — |  | `task_group.Description · TEXT` |  |
| `EMailMessage` | Email Message | The email message associated with the given task. | Text | — |  | `task_group.EMailMessage · TEXT` |  |
| `TaskName` | Name | Enter the task name in this field. | Text | — | yes | `task_group.TaskName · TEXT` |  |
| `TskBAndA_NoAccessorConversion` | Baseline with Forecast/Actual End Date | Displays both the baseline and forecast /actual end dates. The baseline date is indicated with a (b), the forecast date is indicated with a (f), and the actual date is indicated with an (a). | Text | — |  | `task_group.TskBAndA_NoAccessorConversion · TEXT` |  |
| `TskNotDoneCompleted_NoAccessorConversion` | Forecast End Date/Complete | If the task is complete, this field displays "complete". If the task is canceled, the field displays "canceled". Otherwise, the field displays the forecasted end date. | Text | — |  | `task_group.TskNotDoneCompleted_NoAccessorConversion · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `task_group.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `task_group.ModifiedDate · TEXT` |  |

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
