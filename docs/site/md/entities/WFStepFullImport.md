# WFStepFullImport

*47 fields · module: Workflow & Approvals · Postgres: `w_f_step_full_import`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 47 declared fields, filed under Workflow & Approvals, 0 foreign keys pointing at it.

Source: `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 47 |
| Fields with a vendor definition | 0 of 47 inventoried |
| Physical tables | `w_f_step_full_import` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 11 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in w_f_step_full_import

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### Required: the two captures disagree

**Observed.** The field inventory marks 6 of this record's fields required; the Data Fields catalogue marks 0; 0 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApproverMemberIDList` | WF Approver(s) |  | Member ID | — |  | `w_f_step_full_import.ApproverMemberIDList · TEXT` | [Member](Member.md) |
| `AssigneeMemberIDList` | WF Assignee(s) |  | Member ID | — |  | `w_f_step_full_import.AssigneeMemberIDList · TEXT` | [Member](Member.md) |
| `CurrentStepMemberIDList` | Current Step Members |  | Member ID | — |  | `w_f_step_full_import.CurrentStepMemberIDList · TEXT` | [Member](Member.md) |
| `NotifieeMemberIDList` | WF Notify List |  | Member ID | — |  | `w_f_step_full_import.NotifieeMemberIDList · TEXT` | [Member](Member.md) |
| `PageLayoutApproversID` | Page Layout Approvers |  | item ID | — |  | `w_f_step_full_import.PageLayoutApproversID · TEXT` | unresolved |
| `PageLayoutAssigneesID` | Page Layout Assignees |  | item ID | — |  | `w_f_step_full_import.PageLayoutAssigneesID · TEXT` | unresolved |
| `PriorSubmitByMemberID` | Prior Submit By Member |  | Member ID | — |  | `w_f_step_full_import.PriorSubmitByMemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `w_f_step_full_import.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `SubmitForApprovalByMemberID` | Submit For Approval By Member |  | Member ID | — |  | `w_f_step_full_import.SubmitForApprovalByMemberID · TEXT` | [Member](Member.md) |
| `TaskID` | Associated Task |  | Task/Group ID | — |  | `w_f_step_full_import.TaskID · TEXT` | [TaskGroup](TaskGroup.md) |
| `WorkFlowID` | Work Flow |  | Work Flow ID | — | yes | `w_f_step_full_import.WorkFlowID · TEXT` | [WorkFlow](WorkFlow.md) |
| `WorkFlowTemplateStepID` | Workflow Template Step |  | Step ID | — |  | `w_f_step_full_import.WorkFlowTemplateStepID · TEXT` | [WorkFlowStep](WorkFlowStep.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeWorkFlowStatusID` | Step Status |  | Dropdown (Work Flow Status Code) | — | yes | `w_f_step_full_import.CodeWorkFlowStatusID · TEXT` | Work Flow Status Code |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DaysUntilAlertApprovers` | Days Until Alert Approvers |  | Number | — |  | `w_f_step_full_import.DaysUntilAlertApprovers · TEXT` |  |
| `DaysUntilAlertAssignees` | Days Until Alert Assignees |  | Number | — |  | `w_f_step_full_import.DaysUntilAlertAssignees · TEXT` |  |
| `DaysUntilWarnApprovers` | Days Until Warn Approvers |  | Number | — |  | `w_f_step_full_import.DaysUntilWarnApprovers · TEXT` |  |
| `DaysUntilWarnAssignees` | Days Until Warn Assignees |  | Number | — |  | `w_f_step_full_import.DaysUntilWarnAssignees · TEXT` |  |
| `DurationDaysApprovers` | Duration Days Approvers |  | Number | — |  | `w_f_step_full_import.DurationDaysApprovers · TEXT` |  |
| `DurationDaysAssignees` | Duration Days Assignees |  | Number | — |  | `w_f_step_full_import.DurationDaysAssignees · TEXT` |  |
| `Priority` |  |  | Number | — |  | `w_f_step_full_import.Priority · TEXT` |  |
| `StepNumber` | Step Number |  | Number | — | yes | `w_f_step_full_import.StepNumber · TEXT` |  |
| `WorkFlowStepID` | Work Flow Step RecID |  | Number | — |  | `w_f_step_full_import.WorkFlowStepID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (7)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CompleteDate` | Complete Date |  | Date | — |  | `w_f_step_full_import.CompleteDate · TEXT` |  |
| `DueDate` | Due Date |  | Date | — |  | `w_f_step_full_import.DueDate · TEXT` |  |
| `DueDateApprovers` | WF Approver Due Date |  | Date | — |  | `w_f_step_full_import.DueDateApprovers · TEXT` |  |
| `DueDateAssignees` | WF Assignee Due Date |  | Date | — |  | `w_f_step_full_import.DueDateAssignees · TEXT` |  |
| `PriorSubmitForApprovalDate` | Prior Submit For Approval Date |  | Date | — |  | `w_f_step_full_import.PriorSubmitForApprovalDate · TEXT` |  |
| `StartDate` | Start Date |  | Date | — |  | `w_f_step_full_import.StartDate · TEXT` |  |
| `SubmitForApprovalDate` | Submit For Approval Date |  | Date | — |  | `w_f_step_full_import.SubmitForApprovalDate · TEXT` |  |

### Flags (9)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EMailAlertApprovers` | EMail Alert Approvers |  | Boolean | — |  | `w_f_step_full_import.EMailAlertApprovers · TEXT` |  |
| `EMailAlertAssignees` | EMail Alert Assignees |  | Boolean | — |  | `w_f_step_full_import.EMailAlertAssignees · TEXT` |  |
| `EnableForDashboard` | Enable For Dashboard |  | Boolean | — |  | `w_f_step_full_import.EnableForDashboard · TEXT` |  |
| `EnableForEMail` | Enable For Email |  | Boolean | — |  | `w_f_step_full_import.EnableForEMail · TEXT` |  |
| `IsCompleted` | Is Completed? |  | Boolean | — |  | `w_f_step_full_import.IsCompleted · TEXT` |  |
| `IsFormStep` | Is Form Step |  | Boolean | — |  | `w_f_step_full_import.IsFormStep · TEXT` |  |
| `IsNotifyClosed` | Is Notify Closed? |  | Boolean | — |  | `w_f_step_full_import.IsNotifyClosed · TEXT` |  |
| `IsReDo` | Re Do? |  | Boolean | — | yes | `w_f_step_full_import.IsReDo · TEXT` |  |
| `IsReadOnly` | Read Only? |  | Boolean | — | yes | `w_f_step_full_import.IsReadOnly · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EMailMessage` | Email Message |  | Text | — |  | `w_f_step_full_import.EMailMessage · TEXT` |  |
| `IssueID` | Issue |  | Text | — |  | `w_f_step_full_import.IssueID · TEXT` |  |
| `SubmitForApprovalByMemberName` | Submit For Approval By Member Name |  | Text | — |  | `w_f_step_full_import.SubmitForApprovalByMemberName · TEXT` |  |
| `TaskName` | Associated Task Name |  | Text | — |  | `w_f_step_full_import.TaskName · TEXT` |  |
| `WFStepNotificationLink` | WF Step Notification Link |  | Text | — |  | `w_f_step_full_import.WFStepNotificationLink · TEXT` |  |
| `WorkFlowStepName` | Step Name |  | Text | — |  | `w_f_step_full_import.WorkFlowStepName · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Step ClientID |  | Text | — | yes | `w_f_step_full_import.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | — |  | `w_f_step_full_import.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | — |  | `w_f_step_full_import.ModifiedDate · TEXT` |  |
