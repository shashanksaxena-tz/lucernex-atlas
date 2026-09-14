# WorkFlowTemplateStep

*55 fields · module: Workflow & Approvals · Postgres: `work_flow_template_step`*

One approval step within a reusable workflow template — approver/assignee configuration exposed as four parallel list-type fields per role (Approver Job Title List, Approver Member List, Approver Type, Approver User Class List) so a single step can route to a named person, a job title, a user class, or a mix. 59 Global fields under Company Items; this is template design-time metadata, distinct from WorkFlowStep which is the runtime instance of a step actually executing against a real contract or task.

Source: `data-fields/work-flow-template-step.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 55 |
| Catalogued fields | 59 (59 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 11 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-165](../rules/LAY-R-165.md) | Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesI | Observed |
| [PPL-R-013](../rules/PPL-R-013.md) | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) | Derived |

## Fields

### Relationships (foreign keys) (9)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApproverMemberIDList` | Approver Member List | Member ID | Global |  | [Member](Member.md) |
| `AssigneeMemberIDList` | Assignee Member List | Member ID | Global |  | [Member](Member.md) |
| `NotifieeMemberIDList` | Notifiee Member List | Member ID | Global |  | [Member](Member.md) |
| `RunAtCompleteApprover1ID` | At Complete Approver 1 ID | Member ID | Global |  | [Member](Member.md) |
| `RunAtCompleteApprover2ID` | At Complete Approver 2 ID | Member ID | Global |  | [Member](Member.md) |
| `RunAtStartApprover1ID` | At Start Approver 1 ID | Member ID | Global |  | [Member](Member.md) |
| `RunAtStartApprover2ID` | At Start Approver 2 ID | Member ID | Global |  | [Member](Member.md) |
| `UnassignedApproverID` | Unassigned Approver | Member ID | Global |  | [Member](Member.md) |
| `WorkFlowTemplateID` | Work Flow Template | Work Flow ID | Global | yes | [WorkFlow](WorkFlow.md) |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApproverJobTitleIDList` | Approver Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `ApproverUserClassIDList` | Approver User Class List | Dropdown (User Class) | Global |  | User Class |
| `AssigneeJobTitleIDList` | Assignee Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `AssigneeUserClassIDList` | Assignee User Class List | Dropdown (User Class) | Global |  | User Class |
| `NotifieeJobTitleIDList` | Notifiee Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `NotifieeUserClassIDList` | Notifiee User Class List | Dropdown (User Class) | Global |  | User Class |
| `ReassignApproversJobTitleIDList` | Reassign Approvers Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `ReassignAssigneesJobTitleIDList` | Reassign Assignees Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |

### Quantities (13)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApproverType` | Approver Type | Number | Global |  |  |
| `AssigneeType` | Assignee Type | Number | Global |  |  |
| `DaysUntilAlertApprovers` | Days Until Alert Approvers | Number | Global |  |  |
| `DaysUntilAlertAssignees` | Days Until Alert Assignees | Number | Global |  |  |
| `DaysUntilNotification` | Days Until Notification | Number | Global |  |  |
| `DaysUntilWarnApprovers` | Days Until Warn Approvers | Number | Global |  |  |
| `DaysUntilWarnAssignees` | Days Until Warn Assignees | Number | Global |  |  |
| `DurationDaysApprovers` | Number of Days for Approvers to Act | Number | Global |  |  |
| `DurationDaysAssignees` | Number of Days For Assignees to Act | Number | Global |  |  |
| `NotifieeType` | Notifiee Type | Number | Global |  |  |
| `Priority` | Relative Priority | Number | Global |  |  |
| `StepNumber` | Step Number | Number | Global | yes |  |
| `WorkFlowTemplateStepID` | Work Flow Template Step RecID | Number | Global |  |  |

### Flags (13)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AutoAdjustTaskDates` | Automatically Adjust Task Dates to WF Step | Boolean | Global | yes |  |
| `AutoLaunchNextStep` | Automatically Transition to Next Step | Boolean | Global | yes |  |
| `ComputedRequiresApprovers` | Requires Approvers? | Boolean | Global |  |  |
| `ComputedRequiresAssignees` | Requires Assignees? | Boolean | Global |  |  |
| `EMailAlertApprovers` | Should Alert Approvers? | Boolean | Global |  |  |
| `EMailAlertAssignees` | Should Email Assignees? | Boolean | Global |  |  |
| `EnableForDashboard` | Step Enabled for Dashboard | Boolean | Global |  |  |
| `EnableForEMail` | Should Send Email? | Boolean | Global |  |  |
| `IsFormStep` | Is a Form Step (vs Task Step) | Boolean | Global |  |  |
| `NotifyStepApproversStarted` | Notify Step Approvers When Started | Boolean | Global | yes |  |
| `NotifyStepAssigneesStarted` | Notify Step Assignees When Started | Boolean | Global | yes |  |
| `SetTaskCanceled` | Cancel Task When Step is Canceled | Boolean | Global | yes |  |
| `SetTaskInProcess` | Mark Task In Progress When Step Starts | Boolean | Global | yes |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `EMailMessage` | Text of Email to Send | Text | Global |  |  |
| `PageLayoutApproversID` | Layout To Use With Approvers | Text | Global |  |  |
| `PageLayoutAssigneesID` | Layout To Use With Assignees | Text | Global |  |  |
| `TaskName` | Associated Task Name | Text | Global |  |  |
| `WorkFlowTemplateStepName` | Step Name | Text | Global | yes |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Template Step ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
