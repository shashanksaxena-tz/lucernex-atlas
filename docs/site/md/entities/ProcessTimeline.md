# ProcessTimeline

*31 fields · module: Capital Projects & Scheduling · Postgres: `process_timeline`*

A generic milestone/phase timeline attached to a Location or ProjectEntity — actual vs. baseline vs. original end dates and duration, spanning the Location and Milestones groups since timelines apply to both site selection and construction phases. 30 Global fields.

Source: `data-fields/process-timeline.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 30 of 31 inventoried |
| Physical tables | `process_timeline` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in process_timeline

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 30 fields carry a vendor definition

**Observed.** 30 of this record's 31 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. Loaded per parent from contract_admin.ProjectEntityID That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-142](../rules/CON-R-142.md) | A contract advances through its process: ProcessTimelineTemplate forms a linked list of phase-bound milestone templates, instantiated per entity as ProcessTimeline rows with their own status/percent-complete/date-triple fields — the real st | Derived |
| [PRJ-R-002](../rules/PRJ-R-002.md) | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierar | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Assignee_MemberID` | Members | The member ID of the task assignee. | Member ID | Global |  | `process_timeline.Assignee_MemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `process_timeline.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeTaskStatusID` | Task Status | The status of the task group. | Dropdown (Task Status Code) | Global |  | `process_timeline.CodeTaskStatusID · TEXT` | Task Status Code |

### Quantities (10)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualDuration` | Forecast/Actual Duration | The number of days this milestone is predicted to take. | Number | Global |  | `process_timeline.ActualDuration · TEXT` |  |
| `DaysAheadOfSchedule` | Days Ahead of Schedule | The value of this field equals the original / baseline end date - the actual end date. | Number | Global |  | `process_timeline.DaysAheadOfSchedule · TEXT` |  |
| `OriginalDuration` | Baseline Duration | The original or baseline duration of the task. This field's value cannot be negative. | Number | Global |  | `process_timeline.OriginalDuration · TEXT` |  |
| `PercentComplete` | Percent Complete | The percentage of the task completed. | Number | Global |  | `process_timeline.PercentComplete · TEXT` |  |
| `ProcessTimelineID` | Process Timeline RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `process_timeline.ProcessTimelineID · VARCHAR(64) NOT NULL` |  |
| `ProjectedDuration` | Projected Duration | Calculates the projected duration of the task. | Number | Global |  | `process_timeline.ProjectedDuration · TEXT` |  |
| `RemainingDays` | Remaining Days | The number of days remaining for the task. | Number | Global |  | `process_timeline.RemainingDays · TEXT` |  |
| `TskPredVal_ActualLeadLagDays` | Forecast/Actual Lead/Lag Days | This field computes the actual lead / lag days of this task's predecessor. This value is used when a task checks if all of its predecessors have completed (where all of their lead days are < 0). | Number | Global |  | `process_timeline.TskPredVal_ActualLeadLagDays · TEXT` |  |
| `TskPredVal_OriginalLeadLagDays` | Baseline Lead/Lag Days | The original lead / lag days of the task predecessor. | Number | Global |  | `process_timeline.TskPredVal_OriginalLeadLagDays · TEXT` |  |
| `TskPredVal_ProjectedLeadLagDays` | Projected Lead/Lag Days | The number of lead or lag days of the predecessor task. | Number | Global |  | `process_timeline.TskPredVal_ProjectedLeadLagDays · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Forecast/Actual End Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | Global |  | `process_timeline.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | Global |  | `process_timeline.ActualStartDate · TEXT` |  |
| `OriginalEndDate` | Original End Date | The baseline end date of a schedule task on the entity. | Date | Global |  | `process_timeline.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | Global |  | `process_timeline.OriginalStartDate · TEXT` |  |
| `ProjectedEndDate` | Projected End Date | The goal end date. | Date | Global |  | `process_timeline.ProjectedEndDate · TEXT` |  |
| `ProjectedStartDate` | Projected Start Date | The start date or goal date of the task. | Date | Global |  | `process_timeline.ProjectedStartDate · TEXT` |  |
| `TskDone_ActualEndDate` | Actual End Date | The task end date. If a task is canceled, this field will either be blank or will contain the word "canceled". | Date | Global |  | `process_timeline.TskDone_ActualEndDate · TEXT` |  |
| `TskNotDone_ActualEndDate` | Forecast End Date | The forecasted end date of the task. This field only displays for non-complete tasks. | Date | Global |  | `process_timeline.TskNotDone_ActualEndDate · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EnableForDashboard` | Alert when task Completes | This flag is used to determine if the dashboard will receive an alert when the milestone is completed. | Boolean | Global |  | `process_timeline.EnableForDashboard · TEXT` |  |
| `EnableForEMail` | Email when task Completes | This flag is used to determine if an email will be sent when the milestone is completed. | Boolean | Global |  | `process_timeline.EnableForEMail · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `process_timeline.Description · TEXT` |  |
| `EMailMessage` | Email Message | The email message associated with the given task. | Text | Global |  | `process_timeline.EMailMessage · TEXT` |  |
| `ProcessTimelineTemplateName` | Milestone Name | The milestone name. | Text | Global |  | `process_timeline.ProcessTimelineTemplateName · TEXT` |  |
| `TaskName` | Task Name | The name of the schedule task. | Text | Global |  | `process_timeline.TaskName · TEXT` |  |
| `TskBAndA_NoAccessorConversion` | Baseline with Forecast/Actual End Date | Displays both the baseline and forecast /actual end dates. The baseline date is indicated with a (b), the forecast date is indicated with a (f), and the actual date is indicated with an (a). | Text | Global |  | `process_timeline.TskBAndA_NoAccessorConversion · TEXT` |  |
| `TskNotDoneCompleted_NoAccessorConversion` | Forecast End Date/Complete | If the task is complete, this field displays "complete". If the task is canceled, the field displays "canceled". Otherwise, the field displays the forecasted end date. | Text | Global |  | `process_timeline.TskNotDoneCompleted_NoAccessorConversion · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `process_timeline.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `process_timeline.ModifiedDate · TEXT` |  |
