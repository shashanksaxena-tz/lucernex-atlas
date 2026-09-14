# WorkFlowStep

*47 fields · module: Workflow & Approvals · Postgres: `work_flow_step`*

The runtime instance of one workflow step executing against a real record — computed alert/warn/due dates for approvers and assignees, checkout tracking (CheckedOutByMemberID), and a pointer back to the WorkFlowTemplateStep it was instantiated from. 53 Global fields spanning Statics and Workflow groups.

Source: `data-fields/work-flow-step.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 47 |
| Fields with a vendor definition | 43 of 47 inventoried |
| Physical tables | `work_flow_step` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 53 (53 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 7 keys from 5 record types |
| Points at | 11 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in work_flow_step

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 43 fields carry a vendor definition

**Observed.** 43 of this record's 47 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 6 fields marked required

**Observed.** The inventory marks 6 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApproverMemberIDList` | WF Approver(s) | This field gets a list of the approvers that can be assigned to this work flow step. | Member ID | Global |  | `work_flow_step.ApproverMemberIDList · TEXT` | [Member](Member.md) |
| `AssigneeMemberIDList` | WF Assignee(s) | This field gets a list of the assignees that can be assigned to this work flow step. | Member ID | Global |  | `work_flow_step.AssigneeMemberIDList · TEXT` | [Member](Member.md) |
| `CurrentStepMemberIDList` | Current Step Members | The members associated with the current workflow step. | Member ID | Global |  | `work_flow_step.CurrentStepMemberIDList · TEXT` | [Member](Member.md) |
| `NotifieeMemberIDList` | WF Notify List | If a notification has been set up for this work flow step, this field returns a list of the users who will receive the notification. | Member ID | Global |  | `work_flow_step.NotifieeMemberIDList · TEXT` | [Member](Member.md) |
| `PageLayoutApproversID` | Page Layout Approvers | The ID of the page layout used for approvers. | item ID | Global |  | `work_flow_step.PageLayoutApproversID · TEXT` | unresolved |
| `PageLayoutAssigneesID` | Page Layout Assignees | The ID of the page layout used for assignees. | item ID | Global |  | `work_flow_step.PageLayoutAssigneesID · TEXT` | unresolved |
| `PriorSubmitByMemberID` | Prior Submit By Member | The member ID of the person who previously submitted the form for approval. | Member ID | Global |  | `work_flow_step.PriorSubmitByMemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `work_flow_step.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `SubmitForApprovalByMemberID` | Submit For Approval By Member |  | Member ID | Global |  | `work_flow_step.SubmitForApprovalByMemberID · TEXT` | [Member](Member.md) |
| `TaskID` | Associated Task |  | Task/Group ID | Global |  | `work_flow_step.TaskID · TEXT` | [TaskGroup](TaskGroup.md) |
| `WorkFlowID` | Work Flow | The ID of the work flow this step is associated with. | Work Flow ID | Global | yes | `work_flow_step.WorkFlowID · TEXT` | [WorkFlow](WorkFlow.md) |
| `WorkFlowTemplateStepID` | Workflow Template Step | The ID of the work flow step from the work flow template. | Step ID | Global |  | `work_flow_step.WorkFlowTemplateStepID · TEXT` | [WorkFlowStep](WorkFlowStep.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeWorkFlowStatusID` | Step Status | The status of the work flow step. | Dropdown (Work Flow Status Code) | Global | yes | `work_flow_step.CodeWorkFlowStatusID · TEXT` | Work Flow Status Code |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DaysUntilAlertApprovers` | Days Until Alert Approvers | This field contains how many days there will be before a manager is notified that this step has not been completed. | Number | Global |  | `work_flow_step.DaysUntilAlertApprovers · TEXT` |  |
| `DaysUntilAlertAssignees` | Days Until Alert Assignees | This field contains how many days there will be before a manager is notified that this step has not been completed. | Number | Global |  | `work_flow_step.DaysUntilAlertAssignees · TEXT` |  |
| `DaysUntilWarnApprovers` | Days Until Warn Approvers | This field contains how many days there will be before an approver receives a notification that this step has not been completed. | Number | Global |  | `work_flow_step.DaysUntilWarnApprovers · TEXT` |  |
| `DaysUntilWarnAssignees` | Days Until Warn Assignees | This field contains how many days there will be before an assignee receives a notification that this step has not been completed. | Number | Global |  | `work_flow_step.DaysUntilWarnAssignees · TEXT` |  |
| `DurationDaysApprovers` | Duration Days Approvers | Calculates the duration of this work flow step for approvers. | Number | Global |  | `work_flow_step.DurationDaysApprovers · TEXT` |  |
| `DurationDaysAssignees` | Duration Days Assignees | Calculates the duration of this work flow step for assignees. | Number | Global |  | `work_flow_step.DurationDaysAssignees · TEXT` |  |
| `Priority` |  | The priority of the work flow step. | Number | Global |  | `work_flow_step.Priority · TEXT` |  |
| `StepNumber` | Step Number | The work flow step number. | Number | Global | yes | `work_flow_step.StepNumber · TEXT` |  |
| `WorkFlowStepID` | Work Flow Step RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `work_flow_step.WorkFlowStepID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (7)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CompleteDate` | Complete Date | The date the work flow step was completed. | Date | Global |  | `work_flow_step.CompleteDate · TEXT` |  |
| `DueDate` | Due Date | Calculates the due date of the work flow step. | Date | Global |  | `work_flow_step.DueDate · TEXT` |  |
| `DueDateApprovers` | WF Approver Due Date | Calculates the due date of the work flow step for approvers. | Date | Global |  | `work_flow_step.DueDateApprovers · TEXT` |  |
| `DueDateAssignees` | WF Assignee Due Date | Calculates the due date of the work flow step for assignees. | Date | Global |  | `work_flow_step.DueDateAssignees · TEXT` |  |
| `PriorSubmitForApprovalDate` | Prior Submit For Approval Date | The date the previous person submitted the form for approval. | Date | Global |  | `work_flow_step.PriorSubmitForApprovalDate · TEXT` |  |
| `StartDate` | Start Date | The date the work flow step started. | Date | Global |  | `work_flow_step.StartDate · TEXT` |  |
| `SubmitForApprovalDate` | Submit For Approval Date | The date the person submitted the form for approval. | Date | Global |  | `work_flow_step.SubmitForApprovalDate · TEXT` |  |

### Flags (9)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EMailAlertApprovers` | EMail Alert Approvers | If set to true, a dashboard alert will be sent to the approver of this task when the task starts. | Boolean | Global |  | `work_flow_step.EMailAlertApprovers · TEXT` |  |
| `EMailAlertAssignees` | EMail Alert Assignees | If set to true, a dashboard alert will be sent to the assignee of this task when the task starts. | Boolean | Global |  | `work_flow_step.EMailAlertAssignees · TEXT` |  |
| `EnableForDashboard` | Enable For Dashboard | This setting will be set to true if your system administrator set the notification to be sent as a Dashboard alert. | Boolean | Global |  | `work_flow_step.EnableForDashboard · TEXT` |  |
| `EnableForEMail` | Enable For Email | This setting will be set to true if your system administrator set the notification to be sent as an email. | Boolean | Global |  | `work_flow_step.EnableForEMail · TEXT` |  |
| `IsCompleted` | Is Completed? | If this step is completed, this value of this field is true. If this step is not complete, the value of this field is false. | Boolean | Global |  | `work_flow_step.IsCompleted · TEXT` |  |
| `IsFormStep` | Is Form Step | If this step is a form step, this value of this field is true. If this step is a task step, the value of this field is false. | Boolean | Global |  | `work_flow_step.IsFormStep · TEXT` |  |
| `IsNotifyClosed` | Is Notify Closed? | Indicates whether the workflow step has notifications configured. | Boolean | Global |  | `work_flow_step.IsNotifyClosed · TEXT` |  |
| `IsReDo` | Re Do? | If this value is true, the step must be completed again. If this value is false, the step can be completed and the user can progress to the next step in the work flow. This is related to the action the approver takes on the step. | Boolean | Global | yes | `work_flow_step.IsReDo · TEXT` |  |
| `IsReadOnly` | Read Only? | If this step is read-only, this value of this field is true. If this step is not read-only, the value of this field is false. | Boolean | Global | yes | `work_flow_step.IsReadOnly · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EMailMessage` | Email Message | This field contains additional information to be included in the notification email. | Text | Global |  | `work_flow_step.EMailMessage · TEXT` |  |
| `IssueID` | Issue | The ID of the form associated with this work flow step. | Text | Global |  | `work_flow_step.IssueID · TEXT` |  |
| `SubmitForApprovalByMemberName` | Submit For Approval By Member Name | The member ID of the person who submitted the form for approval. | Text | Global |  | `work_flow_step.SubmitForApprovalByMemberName · TEXT` |  |
| `TaskName` | Associated Task Name | The name of the schedule task this work flow step is associated with. | Text | Global |  | `work_flow_step.TaskName · TEXT` |  |
| `WFStepNotificationLink` | WF Step Notification Link |  | Text | Global |  | `work_flow_step.WFStepNotificationLink · TEXT` |  |
| `WorkFlowStepName` | Step Name | The name of the work flow step from the work flow template. | Text | Global |  | `work_flow_step.WorkFlowStepName · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Step ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `work_flow_step.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `work_flow_step.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `work_flow_step.ModifiedDate · TEXT` |  |

## What points here (7 keys)

| Record type | Via column |
|---|---|
| [WorkFlowStepApprover](WorkFlowStepApprover.md) | `WorkFlowStepID`, `WorkFlowTemplateStepID` |
| [WorkFlowStepAssignee](WorkFlowStepAssignee.md) | `WorkFlowStepID`, `WorkFlowTemplateStepID` |
| [WFStepFullImport](WFStepFullImport.md) | `WorkFlowTemplateStepID` |
| [WorkFlowStep](WorkFlowStep.md) | `WorkFlowTemplateStepID` |
| [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) | `WorkFlowTemplateStepID` |
