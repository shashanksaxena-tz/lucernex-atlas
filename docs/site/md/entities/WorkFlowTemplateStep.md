# WorkFlowTemplateStep

*55 fields · module: Workflow & Approvals · Postgres: `work_flow_template_step`*

One approval step within a reusable workflow template — approver/assignee configuration exposed as four parallel list-type fields per role (Approver Job Title List, Approver Member List, Approver Type, Approver User Class List) so a single step can route to a named person, a job title, a user class, or a mix. 59 Global fields under Company Items; this is template design-time metadata, distinct from WorkFlowStep which is the runtime instance of a step actually executing against a real contract or task.

Source: `data-fields/work-flow-template-step.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 55 |
| Fields with a vendor definition | 55 of 55 inventoried |
| Physical tables | `work_flow_template_step` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 59 (59 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 11 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in work_flow_template_step

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 55 fields carry a vendor definition

**Observed.** 55 of this record's 55 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 55 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 10 are marked required.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-165](../rules/LAY-R-165.md) | Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesI | Observed |
| [PPL-R-013](../rules/PPL-R-013.md) | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) | Derived |

## Fields

### Relationships (foreign keys) (9)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApproverMemberIDList` | Approver Member List | Select the members that should approve this work flow task. | Member ID | Global |  | `work_flow_template_step.ApproverMemberIDList · TEXT` | [Member](Member.md) |
| `AssigneeMemberIDList` | Assignee Member List | Select the members that should be assigned to this work flow task. | Member ID | Global |  | `work_flow_template_step.AssigneeMemberIDList · TEXT` | [Member](Member.md) |
| `NotifieeMemberIDList` | Notifiee Member List | Select the members that should receive a notification once this work flow task is completed. | Member ID | Global |  | `work_flow_template_step.NotifieeMemberIDList · TEXT` | [Member](Member.md) |
| `RunAtCompleteApprover1ID` | At Complete Approver 1 ID | This field is a placeholder for an upcoming feature. | Member ID | Global |  | `work_flow_template_step.RunAtCompleteApprover1ID · TEXT` | [Member](Member.md) |
| `RunAtCompleteApprover2ID` | At Complete Approver 2 ID | This field is a placeholder for an upcoming feature. | Member ID | Global |  | `work_flow_template_step.RunAtCompleteApprover2ID · TEXT` | [Member](Member.md) |
| `RunAtStartApprover1ID` | At Start Approver 1 ID | This field is a placeholder for an upcoming feature. | Member ID | Global |  | `work_flow_template_step.RunAtStartApprover1ID · TEXT` | [Member](Member.md) |
| `RunAtStartApprover2ID` | At Start Approver 2 ID | This field is a placeholder for an upcoming feature. | Member ID | Global |  | `work_flow_template_step.RunAtStartApprover2ID · TEXT` | [Member](Member.md) |
| `UnassignedApproverID` | Unassigned Approver | This field is a placeholder for an upcoming feature. | Member ID | Global |  | `work_flow_template_step.UnassignedApproverID · TEXT` | [Member](Member.md) |
| `WorkFlowTemplateID` | Work Flow Template | The name of the work flow template that this work flow step is associated with. | Work Flow ID | Global | yes | `work_flow_template_step.WorkFlowTemplateID · TEXT` | [WorkFlow](WorkFlow.md) |

### Coded values (drop-downs) (8)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApproverJobTitleIDList` | Approver Job Title List | Select the job titles that should approve this work flow task. | Dropdown (Job Title Code) | Global |  | `work_flow_template_step.ApproverJobTitleIDList · TEXT` | Job Title Code |
| `ApproverUserClassIDList` | Approver User Class List | Select the user classes that should approve this work flow task. | Dropdown (User Class) | Global |  | `work_flow_template_step.ApproverUserClassIDList · TEXT` | User Class |
| `AssigneeJobTitleIDList` | Assignee Job Title List | Select the job titles that should be assigned to this work flow task. | Dropdown (Job Title Code) | Global |  | `work_flow_template_step.AssigneeJobTitleIDList · TEXT` | Job Title Code |
| `AssigneeUserClassIDList` | Assignee User Class List | Select the user classes that should be assigned to this work flow task. | Dropdown (User Class) | Global |  | `work_flow_template_step.AssigneeUserClassIDList · TEXT` | User Class |
| `NotifieeJobTitleIDList` | Notifiee Job Title List | Select the job titles that should receive a notification once this work flow task is completed. | Dropdown (Job Title Code) | Global |  | `work_flow_template_step.NotifieeJobTitleIDList · TEXT` | Job Title Code |
| `NotifieeUserClassIDList` | Notifiee User Class List | Select the user classes that should receive a notification once this work flow task is completed. | Dropdown (User Class) | Global |  | `work_flow_template_step.NotifieeUserClassIDList · TEXT` | User Class |
| `ReassignApproversJobTitleIDList` | Reassign Approvers Job Title List | When added to a form, this field allows users with appropriate permissions to reassign approvers by job title. | Dropdown (Job Title Code) | Global |  | `work_flow_template_step.ReassignApproversJobTitleIDList · TEXT` | Job Title Code |
| `ReassignAssigneesJobTitleIDList` | Reassign Assignees Job Title List | When added to a form, this field allows users with appropriate permissions to reassign assignees by job title. | Dropdown (Job Title Code) | Global |  | `work_flow_template_step.ReassignAssigneesJobTitleIDList · TEXT` | Job Title Code |

### Quantities (13)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApproverType` | Approver Type | Select the category of approver you want to use, such as by Job Title, User Class, Member, or Org Chart Level. | Number | Global |  | `work_flow_template_step.ApproverType · TEXT` |  |
| `AssigneeType` | Assignee Type | Select the category of assignee you want to use, such as by Job Title, User Class, Member, or Org Chart Level. | Number | Global |  | `work_flow_template_step.AssigneeType · TEXT` |  |
| `DaysUntilAlertApprovers` | Days Until Alert Approvers | Enter how many days there will be before a manager is notified that this step has not been completed in this field. | Number | Global |  | `work_flow_template_step.DaysUntilAlertApprovers · TEXT` |  |
| `DaysUntilAlertAssignees` | Days Until Alert Assignees | Enter how many days there will be before a manager is notified that this step has not been completed in this field. | Number | Global |  | `work_flow_template_step.DaysUntilAlertAssignees · TEXT` |  |
| `DaysUntilNotification` | Days Until Notification | Enter the number of days after the form completion date a notification should be sent in this field. | Number | Global |  | `work_flow_template_step.DaysUntilNotification · TEXT` |  |
| `DaysUntilWarnApprovers` | Days Until Warn Approvers | Enter how many days there will be before an approver receives a notification that this step has not been completed in this field. | Number | Global |  | `work_flow_template_step.DaysUntilWarnApprovers · TEXT` |  |
| `DaysUntilWarnAssignees` | Days Until Warn Assignees | Enter how many days there will be before an assignee receives a notification that this step has not been completed in this field. | Number | Global |  | `work_flow_template_step.DaysUntilWarnAssignees · TEXT` |  |
| `DurationDaysApprovers` | Number of Days for Approvers to Act | Enter how long in days an approver has to complete a step in this field. | Number | Global |  | `work_flow_template_step.DurationDaysApprovers · TEXT` |  |
| `DurationDaysAssignees` | Number of Days For Assignees to Act | Enter how long in days an assignee has to complete a step in this field. | Number | Global |  | `work_flow_template_step.DurationDaysAssignees · TEXT` |  |
| `NotifieeType` | Notifiee Type | Select the category of notifiee you want to use, such as by Job Title, User Class, Member, or Org Chart Level. | Number | Global |  | `work_flow_template_step.NotifieeType · TEXT` |  |
| `Priority` | Relative Priority | Select the priority of this task from this field. | Number | Global |  | `work_flow_template_step.Priority · TEXT` |  |
| `StepNumber` | Step Number | Enter the step number in this field. | Number | Global | yes | `work_flow_template_step.StepNumber · TEXT` |  |
| `WorkFlowTemplateStepID` | Work Flow Template Step RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `work_flow_template_step.WorkFlowTemplateStepID · VARCHAR(64) NOT NULL` |  |

### Flags (13)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AutoAdjustTaskDates` | Automatically Adjust Task Dates to WF Step | Select this check box if you want Lx to automatically adjust the task dates to match the step durations. | Boolean | Global | yes | `work_flow_template_step.AutoAdjustTaskDates · TEXT` |  |
| `AutoLaunchNextStep` | Automatically Transition to Next Step | Select this check box if you want Lx to automatically launch the next step if it is a form. | Boolean | Global | yes | `work_flow_template_step.AutoLaunchNextStep · TEXT` |  |
| `ComputedRequiresApprovers` | Requires Approvers? | The value of this field is true if the work flow step requires approvers. | Boolean | Global |  | `work_flow_template_step.ComputedRequiresApprovers · TEXT` |  |
| `ComputedRequiresAssignees` | Requires Assignees? | The value of this field is true if the work flow step requires assignees. | Boolean | Global |  | `work_flow_template_step.ComputedRequiresAssignees · TEXT` |  |
| `EMailAlertApprovers` | Should Alert Approvers? | Select this check box if you want to send a dashboard alert to the approver of this task when the task starts. | Boolean | Global |  | `work_flow_template_step.EMailAlertApprovers · TEXT` |  |
| `EMailAlertAssignees` | Should Email Assignees? | Select this check box if you want to send a dashboard alert to the assignee of this task when the task starts. | Boolean | Global |  | `work_flow_template_step.EMailAlertAssignees · TEXT` |  |
| `EnableForDashboard` | Step Enabled for Dashboard | Select this check box if you would like the notification to be sent as a Dashboard alert. | Boolean | Global |  | `work_flow_template_step.EnableForDashboard · TEXT` |  |
| `EnableForEMail` | Should Send Email? | Select this check box if you would like the notification to be sent as an email. | Boolean | Global |  | `work_flow_template_step.EnableForEMail · TEXT` |  |
| `IsFormStep` | Is a Form Step (vs Task Step) | This field has one of two values: Form Step or Task Step. | Boolean | Global |  | `work_flow_template_step.IsFormStep · TEXT` |  |
| `NotifyStepApproversStarted` | Notify Step Approvers When Started | Select this check box if you want Lx to send an email notification to the task approver when the step starts. | Boolean | Global | yes | `work_flow_template_step.NotifyStepApproversStarted · TEXT` |  |
| `NotifyStepAssigneesStarted` | Notify Step Assignees When Started | Select this check box if you want Lx to send an email notification to the task assignee when the step starts. | Boolean | Global | yes | `work_flow_template_step.NotifyStepAssigneesStarted · TEXT` |  |
| `SetTaskCanceled` | Cancel Task When Step is Canceled | Select this check box if you want to set the work flow step status to "Canceled" when the user cancels the step. | Boolean | Global | yes | `work_flow_template_step.SetTaskCanceled · TEXT` |  |
| `SetTaskInProcess` | Mark Task In Progress When Step Starts | Select this check box if you want to set the work flow step status to "In Process" when the step starts. | Boolean | Global | yes | `work_flow_template_step.SetTaskInProcess · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `work_flow_template_step.Description · TEXT` |  |
| `EMailMessage` | Text of Email to Send | Enter any additional information you want to include in the notification email in this field. | Text | Global |  | `work_flow_template_step.EMailMessage · TEXT` |  |
| `PageLayoutApproversID` | Layout To Use With Approvers | Select which form layout approvers should see for this step. | Text | Global |  | `work_flow_template_step.PageLayoutApproversID · TEXT` |  |
| `PageLayoutAssigneesID` | Layout To Use With Assignees | Select which form layout assignees should see for this step. | Text | Global |  | `work_flow_template_step.PageLayoutAssigneesID · TEXT` |  |
| `TaskName` | Associated Task Name | Select the schedule task that this work flow step should be associated with from this field. | Text | Global |  | `work_flow_template_step.TaskName · TEXT` |  |
| `WorkFlowTemplateStepName` | Step Name | Enter the name of the work flow step in this field. | Text | Global | yes | `work_flow_template_step.WorkFlowTemplateStepName · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Template Step ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `work_flow_template_step.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `work_flow_template_step.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `work_flow_template_step.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `work_flow_template_step.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `work_flow_template_step.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `work_flow_template_step.RevNumber · TEXT` |  |
