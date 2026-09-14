# WorkFlowStep

*47 fields · module: Workflow & Approvals · Postgres: `work_flow_step`*

The runtime instance of one workflow step executing against a real record — computed alert/warn/due dates for approvers and assignees, checkout tracking (CheckedOutByMemberID), and a pointer back to the WorkFlowTemplateStep it was instantiated from. 53 Global fields spanning Statics and Workflow groups.

Source: `data-fields/work-flow-step.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 47 |
| Catalogued fields | 53 (53 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 7 keys from 5 record types |
| Points at | 11 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApproverMemberIDList` | WF Approver(s) | Member ID | Global |  | [Member](Member.md) |
| `AssigneeMemberIDList` | WF Assignee(s) | Member ID | Global |  | [Member](Member.md) |
| `CurrentStepMemberIDList` | Current Step Members | Member ID | Global |  | [Member](Member.md) |
| `NotifieeMemberIDList` | WF Notify List | Member ID | Global |  | [Member](Member.md) |
| `PageLayoutApproversID` | Page Layout Approvers | item ID | Global |  | unresolved |
| `PageLayoutAssigneesID` | Page Layout Assignees | item ID | Global |  | unresolved |
| `PriorSubmitByMemberID` | Prior Submit By Member | Member ID | Global |  | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `SubmitForApprovalByMemberID` | Submit For Approval By Member | Member ID | Global |  | [Member](Member.md) |
| `TaskID` | Associated Task | Task/Group ID | Global |  | [TaskGroup](TaskGroup.md) |
| `WorkFlowID` | Work Flow | Work Flow ID | Global | yes | [WorkFlow](WorkFlow.md) |
| `WorkFlowTemplateStepID` | Workflow Template Step | Step ID | Global |  | [WorkFlowStep](WorkFlowStep.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeWorkFlowStatusID` | Step Status | Dropdown (Work Flow Status Code) | Global | yes | Work Flow Status Code |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DaysUntilAlertApprovers` | Days Until Alert Approvers | Number | Global |  |  |
| `DaysUntilAlertAssignees` | Days Until Alert Assignees | Number | Global |  |  |
| `DaysUntilWarnApprovers` | Days Until Warn Approvers | Number | Global |  |  |
| `DaysUntilWarnAssignees` | Days Until Warn Assignees | Number | Global |  |  |
| `DurationDaysApprovers` | Duration Days Approvers | Number | Global |  |  |
| `DurationDaysAssignees` | Duration Days Assignees | Number | Global |  |  |
| `Priority` |  | Number | Global |  |  |
| `StepNumber` | Step Number | Number | Global | yes |  |
| `WorkFlowStepID` | Work Flow Step RecID | Number | Global |  |  |

### Dates & timestamps (7)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CompleteDate` | Complete Date | Date | Global |  |  |
| `DueDate` | Due Date | Date | Global |  |  |
| `DueDateApprovers` | WF Approver Due Date | Date | Global |  |  |
| `DueDateAssignees` | WF Assignee Due Date | Date | Global |  |  |
| `PriorSubmitForApprovalDate` | Prior Submit For Approval Date | Date | Global |  |  |
| `StartDate` | Start Date | Date | Global |  |  |
| `SubmitForApprovalDate` | Submit For Approval Date | Date | Global |  |  |

### Flags (9)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EMailAlertApprovers` | EMail Alert Approvers | Boolean | Global |  |  |
| `EMailAlertAssignees` | EMail Alert Assignees | Boolean | Global |  |  |
| `EnableForDashboard` | Enable For Dashboard | Boolean | Global |  |  |
| `EnableForEMail` | Enable For Email | Boolean | Global |  |  |
| `IsCompleted` | Is Completed? | Boolean | Global |  |  |
| `IsFormStep` | Is Form Step | Boolean | Global |  |  |
| `IsNotifyClosed` | Is Notify Closed? | Boolean | Global |  |  |
| `IsReDo` | Re Do? | Boolean | Global | yes |  |
| `IsReadOnly` | Read Only? | Boolean | Global | yes |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EMailMessage` | Email Message | Text | Global |  |  |
| `IssueID` | Issue | Text | Global |  |  |
| `SubmitForApprovalByMemberName` | Submit For Approval By Member Name | Text | Global |  |  |
| `TaskName` | Associated Task Name | Text | Global |  |  |
| `WFStepNotificationLink` | WF Step Notification Link | Text | Global |  |  |
| `WorkFlowStepName` | Step Name | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Step ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (7 keys)

| Record type | Via column |
|---|---|
| [WorkFlowStepApprover](WorkFlowStepApprover.md) | `WorkFlowStepID`, `WorkFlowTemplateStepID` |
| [WorkFlowStepAssignee](WorkFlowStepAssignee.md) | `WorkFlowStepID`, `WorkFlowTemplateStepID` |
| [WFStepFullImport](WFStepFullImport.md) | `WorkFlowTemplateStepID` |
| [WorkFlowStep](WorkFlowStep.md) | `WorkFlowTemplateStepID` |
| [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) | `WorkFlowTemplateStepID` |
