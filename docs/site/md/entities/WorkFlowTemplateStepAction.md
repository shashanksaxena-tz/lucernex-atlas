# WorkFlowTemplateStepAction

*37 fields · module: Workflow & Approvals · Postgres: `work_flow_template_step_action`*

The button/action definition available at a workflow template step (Approve, Reject, Send Back) — Boolean flags controlling what the action does to the workflow (Should Close Work Flow?, Should Move to Next Step, Should Restart the Step?) plus finance-specific behavior like FIFO pay-app validation and auto-copy of amounts. 39 Global fields under Company Items and Statics.

Source: `data-fields/work-flow-template-step-action.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Fields with a vendor definition | 33 of 37 inventoried |
| Physical tables | `work_flow_template_step_action` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 39 (39 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 1 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in work_flow_template_step_action

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 33 fields carry a vendor definition

**Observed.** 33 of this record's 37 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 15 of this record's fields required; the Data Fields catalogue marks 15; 15 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PPL-R-013](../rules/PPL-R-013.md) | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) | Derived |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `KickOffWorkFlowTemplateID` | Kick Off Work Flow Template | If you want to kick off another work flow with the completion of this action, select the work flow from this field. | Work Flow ID | Global |  | `work_flow_template_step_action.KickOffWorkFlowTemplateID · TEXT` | [WorkFlow](WorkFlow.md) |
| `ProjectEntityID` | WF Step Action Entity | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Entity ID | Global |  | `work_flow_template_step_action.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `WorkFlowTemplateStepID` | Work Flow Template Step | The ID of the work flow step that this action is associated with. | Step ID | Global |  | `work_flow_template_step_action.WorkFlowTemplateStepID · TEXT` | [WorkFlowStep](WorkFlowStep.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeLastActionStatusID` | Last Action Status |  | Dropdown (Last Action Status Code) | Global |  | `work_flow_template_step_action.CodeLastActionStatusID · TEXT` | Last Action Status Code |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `KickOffTargetWFTemplateID` | Kick Off Work Flow Template Trigger | Returns the workflow template kickoff trigger value, a number associated with a workflow template. | Number | Global |  | `work_flow_template_step_action.KickOffTargetWFTemplateID · TEXT` |  |
| `MoveToStepNumber` | Action Should Move to Next Step Number | If you want to move to a specific step number with the completion of this action, enter the step number in this field. | Number | Global |  | `work_flow_template_step_action.MoveToStepNumber · TEXT` |  |
| `WorkFlowTemplateKickOffID` | Work Flow Template Kick Off | Specifies the action type and the WorkFlow that gets kicked off. | Number | Global |  | `work_flow_template_step_action.WorkFlowTemplateKickOffID · TEXT` |  |
| `WorkFlowTemplateStepActionID` | Workflow Template Step Action | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `work_flow_template_step_action.WorkFlowTemplateStepActionID · VARCHAR(64) NOT NULL` |  |

### Flags (18)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AutoClearAmounts` | Auto Clear Amounts |  | Boolean | Global |  | `work_flow_template_step_action.AutoClearAmounts · TEXT` |  |
| `AutoCopyAmounts` | Auto Copy Amounts | This setting automatically copies budget-impacting values into a custom list in the next step of the work flow. This feature works together with the existing Copy To functionality for custom lists, and is recommended when using Budget Custom Lists in your work flow. | Boolean | Global |  | `work_flow_template_step_action.AutoCopyAmounts · TEXT` |  |
| `CloseWorkFlow` | Action Should Close Work Flow? | This setting will close the current work flow after this step has been completed. | Boolean | Global | yes | `work_flow_template_step_action.CloseWorkFlow · TEXT` |  |
| `DisableEditAfterDecision` | Action Should Disable Edit? | This setting prevents users from making any more changes after the step status is changed to Approved or Denied. | Boolean | Global | yes | `work_flow_template_step_action.DisableEditAfterDecision · TEXT` |  |
| `FifoPayApp` | Apply FIFO Pay App Validation |  | Boolean | Global |  | `work_flow_template_step_action.FifoPayApp · TEXT` |  |
| `GenPurchOrderLineSeqNum` | Generate Purchase Order Line Sequence Number |  | Boolean | Global |  | `work_flow_template_step_action.GenPurchOrderLineSeqNum · TEXT` |  |
| `IsApprovalAction` | Is Approval Action? | Specifies whether the current action is an approval or not. If it is not, then the step is either restarted or denied. | Boolean | Global | yes | `work_flow_template_step_action.IsApprovalAction · TEXT` |  |
| `NotifyInitiatorComplete` | Notify Initiator on Complete? | Select this check box if you want to send a notification to the initiator of this step once the step is complete. | Boolean | Global | yes | `work_flow_template_step_action.NotifyInitiatorComplete · TEXT` |  |
| `NotifyPriorApproversComplete` | Notify Prior Approvers on Complete? | Select this check box if you want to send a notification to all prior approvers of this step once this step is complete. | Boolean | Global | yes | `work_flow_template_step_action.NotifyPriorApproversComplete · TEXT` |  |
| `NotifyPriorAssigneesComplete` | Notify Prior Assignees on Complete? | If set to true, prior assignees are notified by email when the workflow step is completed. | Boolean | Global | yes | `work_flow_template_step_action.NotifyPriorAssigneesComplete · TEXT` |  |
| `NotifyStepApproversComplete` | Notify Step Approvers on Complete? | If set to true, step approvers are notified by email when the workflow step is completed. | Boolean | Global | yes | `work_flow_template_step_action.NotifyStepApproversComplete · TEXT` |  |
| `NotifyStepAssigneesComplete` | Notify Step Assignees on Complete? | If set to true, step assignees are notified by email when the workflow step is completed. | Boolean | Global | yes | `work_flow_template_step_action.NotifyStepAssigneesComplete · TEXT` |  |
| `PassAdhocToNewWF` | Pass Adhoc Assignee To New Work Flow? | This setting will assign the ad hoc member assigned to this task to the first task in the new work flow kicked off by this step. | Boolean | Global | yes | `work_flow_template_step_action.PassAdhocToNewWF · TEXT` |  |
| `PassPriorityToNewWF` | Pass Priority To New Work Flow? | This setting will transfer the priority level of this work flow to a new work flow that is kicked off by this step. | Boolean | Global | yes | `work_flow_template_step_action.PassPriorityToNewWF · TEXT` |  |
| `RequireAllApprovers` | Require All Approvers? | Select this check box if you want to require all qualified approvers on the entity to take the same action on the work flow step for the work flow to progress. | Boolean | Global | yes | `work_flow_template_step_action.RequireAllApprovers · TEXT` |  |
| `RequireApproverSig` | Require Approver Signature | Select this check box if you want to require an approver signature for an action on a work flow step. | Boolean | Global |  | `work_flow_template_step_action.RequireApproverSig · TEXT` |  |
| `RestartStep` | Action Should Restart the Step? | Select this option button if this action should trigger the step to restart. | Boolean | Global | yes | `work_flow_template_step_action.RestartStep · TEXT` |  |
| `SendPaymentInfo` | Send Payment Info? | This field is not implemented. | Boolean | Global | yes | `work_flow_template_step_action.SendPaymentInfo · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActionComment` | Action Comment | This field captures any comments left by the approver on the approver's action. | Text | Global |  | `work_flow_template_step_action.ActionComment · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `work_flow_template_step_action.Description · TEXT` |  |
| `IsEnabledLxJSCode` | Javascript Source Code | If you are creating a custom action using JavaScript, enter the JavaScript in this field. | Text | Global |  | `work_flow_template_step_action.IsEnabledLxJSCode · TEXT` |  |
| `KickOffDescription` | Kick Off Description | The description of the work flow kick off trigger. | Text | Global |  | `work_flow_template_step_action.KickOffDescription · TEXT` |  |
| `WorkFlowTemplateStepActionName` | Action Name | Enter the name of the action in this field. | Text | Global | yes | `work_flow_template_step_action.WorkFlowTemplateStepActionName · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Template Step Action ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `work_flow_template_step_action.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `work_flow_template_step_action.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `work_flow_template_step_action.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `work_flow_template_step_action.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `work_flow_template_step_action.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `work_flow_template_step_action.RevNumber · TEXT` |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [WorkFlowStepApprover](WorkFlowStepApprover.md) | `PriorWFTemplateStepActionID`, `WorkFlowTemplateStepActionID` |
