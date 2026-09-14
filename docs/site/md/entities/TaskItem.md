# TaskItem

*37 fields · module: Capital Projects & Scheduling · Postgres: `task_item`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 37 declared fields, filed under Capital Projects & Scheduling, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 36 of its 37 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Fields with a vendor definition | 36 of 37 inventoried |
| Physical tables | `task_item` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in task_item

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

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Assignee_MemberID` | Resources | The member ID of the task assignee. | Member ID | — |  | `task_item.Assignee_MemberID · TEXT` | [Member](Member.md) |
| `ParentTaskID` | Parent Task | The ID of the parent task of the given task. | Task/Group ID | — |  | `task_item.ParentTaskID · TEXT` | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `task_item.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `TskPredVal_PredecessorTaskID` | Predecessor Task(s) | The ID of the predecessor task of a given task. | Task/Group ID | — |  | `task_item.TskPredVal_PredecessorTaskID · TEXT` | [TaskGroup](TaskGroup.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeTaskStatusID` | Task Status | Select the task status from this field. By default, this value is set to Not Begun. If you select Canceled, the duration is set to 0. If you select Completed, the Percent Complete changes to 100%. If you select In-Process, the Percent Complete is set to 99%, but can be changed if necessary. | Dropdown (Task Status Code) | — |  | `task_item.CodeTaskStatusID · TEXT` | Task Status Code |
| `TaskEndsCodeDayOfWeekID` | Task Ends On Day | If the task should end on a particular weekday, select the weekday from this field. If you use this field, the Forecast / Actual End date field will not be editable. The system will automatically calculate the value for the Forecast / Actual End date using the Forecast / Actual Start and End Weekday. | Dropdown (Day Of Week Code) | — |  | `task_item.TaskEndsCodeDayOfWeekID · TEXT` | Day Of Week Code |

### Quantities (12)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualDuration` | Forecast/Actual Duration | Enter the number of days this task is predicted to take. Entering a value in this field automatically changes the value in the Forecast / Actual End date field. A Duration of 1 day means that the task ends on the same day that it was started. Duration refers to working days only, and tasks cannot have a duration of 0. | Number | — |  | `task_item.ActualDuration · TEXT` |  |
| `ActualResourceUnits` | Actual Resource Units | The actual resource units of the task. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. The value of this field is used to calculate a task item's Remaining Resource Units, using this formula: Actual Resource Units * (1 - Computed Percent Complete). | Number | — |  | `task_item.ActualResourceUnits · TEXT` |  |
| `DaysAheadOfSchedule` | Days Ahead of Schedule | The value of this field equals the original / baseline end date - the actual end date. | Number | — |  | `task_item.DaysAheadOfSchedule · TEXT` |  |
| `OriginalDuration` | Baseline Duration | The original or baseline duration of the task. This field's value cannot be negative. | Number | — |  | `task_item.OriginalDuration · TEXT` |  |
| `OriginalResourceUnits` | Original Resource Units | The original resource units of the task. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. | Number | — |  | `task_item.OriginalResourceUnits · TEXT` |  |
| `PercentComplete` | Percent Complete | The percentage of the task completed. | Number | — |  | `task_item.PercentComplete · TEXT` |  |
| `ProjectedDuration` | Projected Duration | Calculates the projected duration of the task. | Number | — |  | `task_item.ProjectedDuration · TEXT` |  |
| `ProjectedResourceUnits` | Projected Resource Units | The projected resource units of the task. A resource unit is the percentages of the assigned resource's time spent on the task. For example, if two resources were assigned to a task, each spending 25% of their time on the task, the resource units of the task would be 50%. | Number | — |  | `task_item.ProjectedResourceUnits · TEXT` |  |
| `TaskID` | Task RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | `task_item.TaskID · VARCHAR(64) NOT NULL` |  |
| `TskPredVal_ActualLeadLagDays` | Forecast/Actual Lead/Lag Days | This field computes the actual lead / lag days of this task's predecessor. This value is used when a task checks if all of its predecessors have completed (where all of their lead days are < 0). | Number | — |  | `task_item.TskPredVal_ActualLeadLagDays · TEXT` |  |
| `TskPredVal_OriginalLeadLagDays` | Baseline Lead/Lag Days | The original lead / lag days of the task predecessor. | Number | — |  | `task_item.TskPredVal_OriginalLeadLagDays · TEXT` |  |
| `TskPredVal_ProjectedLeadLagDays` | Projected Lead/Lag Days | The number of lead or lag days of the predecessor task. | Number | — |  | `task_item.TskPredVal_ProjectedLeadLagDays · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Forecast/Actual End Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | — |  | `task_item.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | — |  | `task_item.ActualStartDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `task_item.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `task_item.OriginalStartDate · TEXT` |  |
| `ProjectedEndDate` | Projected End Date | Enter the end date you are aiming for in this field. You can think of your projected dates as your goal dates. | Date | — |  | `task_item.ProjectedEndDate · TEXT` |  |
| `ProjectedStartDate` | Projected Start Date | Enter the start date you are aiming for in this field. You can think of your projected dates as your goal dates. | Date | — |  | `task_item.ProjectedStartDate · TEXT` |  |
| `TskDone_ActualEndDate` | Actual End Date | The task end date. If a task is canceled, this field will either be blank or will contain the word "canceled". | Date | — |  | `task_item.TskDone_ActualEndDate · TEXT` |  |
| `TskNotDone_ActualEndDate` | Forecast End Date | The forecasted end date of the task. This field only displays for non-complete tasks. | Date | — |  | `task_item.TskNotDone_ActualEndDate · TEXT` |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EnableForDashboard` | Alert when task Completes | This flag is used to determine if the dashboard will receive an alert when the task is completed. | Boolean | — |  | `task_item.EnableForDashboard · TEXT` |  |
| `EnableForEMail` | Email when task Completes | This flag is used to determine if an email will be sent when the task is completed. | Boolean | — |  | `task_item.EnableForEMail · TEXT` |  |
| `IsTaskGroup` | Is Task Group | If this value is true, the record is a task group. If this value is false, this record is a task. | Boolean | — | yes | `task_item.IsTaskGroup · TEXT` |  |
| `OnCriticalPath` | On Critical Path? | This flag indicates whether the task is on a critical path or not. | Boolean | — |  | `task_item.OnCriticalPath · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | — |  | `task_item.Description · TEXT` |  |
| `EMailMessage` | Email Message | The email message associated with the given task. | Text | — |  | `task_item.EMailMessage · TEXT` |  |
| `TaskName` | Name | Enter the task name in this field. | Text | — | yes | `task_item.TaskName · TEXT` |  |
| `TskBAndA_NoAccessorConversion` | Baseline with Forecast/Actual End Date | Displays both the baseline and forecast /actual end dates. The baseline date is indicated with a (b), the forecast date is indicated with a (f), and the actual date is indicated with an (a). | Text | — |  | `task_item.TskBAndA_NoAccessorConversion · TEXT` |  |
| `TskNotDoneCompleted_NoAccessorConversion` | Forecast End Date/Complete | If the task is complete, this field displays "complete". If the task is canceled, the field displays "canceled". Otherwise, the field displays the forecasted end date. | Text | — |  | `task_item.TskNotDoneCompleted_NoAccessorConversion · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `task_item.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `task_item.ModifiedDate · TEXT` |  |
