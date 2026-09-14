# ProcessTimeline

*31 fields · module: Capital Projects & Scheduling · Postgres: `process_timeline`*

A generic milestone/phase timeline attached to a Location or ProjectEntity — actual vs. baseline vs. original end dates and duration, spanning the Location and Milestones groups since timelines apply to both site selection and construction phases. 30 Global fields.

Source: `data-fields/process-timeline.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-142](../rules/CON-R-142.md) | A contract advances through its process: ProcessTimelineTemplate forms a linked list of phase-bound milestone templates, instantiated per entity as ProcessTimeline rows with their own status/percent-complete/date-triple fields — the real st | Derived |
| [PRJ-R-002](../rules/PRJ-R-002.md) | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierar | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Assignee_MemberID` | Members | Member ID | Global |  | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeTaskStatusID` | Task Status | Dropdown (Task Status Code) | Global |  | Task Status Code |

### Quantities (10)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualDuration` | Forecast/Actual Duration | Number | Global |  |  |
| `DaysAheadOfSchedule` | Days Ahead of Schedule | Number | Global |  |  |
| `OriginalDuration` | Baseline Duration | Number | Global |  |  |
| `PercentComplete` | Percent Complete | Number | Global |  |  |
| `ProcessTimelineID` | Process Timeline RecID | Number | Global |  |  |
| `ProjectedDuration` | Projected Duration | Number | Global |  |  |
| `RemainingDays` | Remaining Days | Number | Global |  |  |
| `TskPredVal_ActualLeadLagDays` | Forecast/Actual Lead/Lag Days | Number | Global |  |  |
| `TskPredVal_OriginalLeadLagDays` | Baseline Lead/Lag Days | Number | Global |  |  |
| `TskPredVal_ProjectedLeadLagDays` | Projected Lead/Lag Days | Number | Global |  |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` | Forecast/Actual End Date | Date | Global |  |  |
| `ActualStartDate` | Forecast/Actual Start Date | Date | Global |  |  |
| `OriginalEndDate` | Original End Date | Date | Global |  |  |
| `OriginalStartDate` | Baseline Start Date | Date | Global |  |  |
| `ProjectedEndDate` | Projected End Date | Date | Global |  |  |
| `ProjectedStartDate` | Projected Start Date | Date | Global |  |  |
| `TskDone_ActualEndDate` | Actual End Date | Date | Global |  |  |
| `TskNotDone_ActualEndDate` | Forecast End Date | Date | Global |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EnableForDashboard` | Alert when task Completes | Boolean | Global |  |  |
| `EnableForEMail` | Email when task Completes | Boolean | Global |  |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `EMailMessage` | Email Message | Text | Global |  |  |
| `ProcessTimelineTemplateName` | Milestone Name | Text | Global |  |  |
| `TaskName` | Task Name | Text | Global |  |  |
| `TskBAndA_NoAccessorConversion` | Baseline with Forecast/Actual End Date | Text | Global |  |  |
| `TskNotDoneCompleted_NoAccessorConversion` | Forecast End Date/Complete | Text | Global |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
