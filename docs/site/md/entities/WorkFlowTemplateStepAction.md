# WorkFlowTemplateStepAction

*37 fields · module: Workflow & Approvals · Postgres: `work_flow_template_step_action`*

The button/action definition available at a workflow template step (Approve, Reject, Send Back) — Boolean flags controlling what the action does to the workflow (Should Close Work Flow?, Should Move to Next Step, Should Restart the Step?) plus finance-specific behavior like FIFO pay-app validation and auto-copy of amounts. 39 Global fields under Company Items and Statics.

Source: `data-fields/work-flow-template-step-action.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 37 |
| Catalogued fields | 39 (39 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 1 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PPL-R-013](../rules/PPL-R-013.md) | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) | Derived |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `KickOffWorkFlowTemplateID` | Kick Off Work Flow Template | Work Flow ID | Global |  | [WorkFlow](WorkFlow.md) |
| `ProjectEntityID` | WF Step Action Entity | Entity ID | Global |  | [ProjectEntity](ProjectEntity.md) |
| `WorkFlowTemplateStepID` | Work Flow Template Step | Step ID | Global |  | [WorkFlowStep](WorkFlowStep.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeLastActionStatusID` | Last Action Status | Dropdown (Last Action Status Code) | Global |  | Last Action Status Code |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `KickOffTargetWFTemplateID` | Kick Off Work Flow Template Trigger | Number | Global |  |  |
| `MoveToStepNumber` | Action Should Move to Next Step Number | Number | Global |  |  |
| `WorkFlowTemplateKickOffID` | Work Flow Template Kick Off | Number | Global |  |  |
| `WorkFlowTemplateStepActionID` | Workflow Template Step Action | Number | Global |  |  |

### Flags (18)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AutoClearAmounts` | Auto Clear Amounts | Boolean | Global |  |  |
| `AutoCopyAmounts` | Auto Copy Amounts | Boolean | Global |  |  |
| `CloseWorkFlow` | Action Should Close Work Flow? | Boolean | Global | yes |  |
| `DisableEditAfterDecision` | Action Should Disable Edit? | Boolean | Global | yes |  |
| `FifoPayApp` | Apply FIFO Pay App Validation | Boolean | Global |  |  |
| `GenPurchOrderLineSeqNum` | Generate Purchase Order Line Sequence Number | Boolean | Global |  |  |
| `IsApprovalAction` | Is Approval Action? | Boolean | Global | yes |  |
| `NotifyInitiatorComplete` | Notify Initiator on Complete? | Boolean | Global | yes |  |
| `NotifyPriorApproversComplete` | Notify Prior Approvers on Complete? | Boolean | Global | yes |  |
| `NotifyPriorAssigneesComplete` | Notify Prior Assignees on Complete? | Boolean | Global | yes |  |
| `NotifyStepApproversComplete` | Notify Step Approvers on Complete? | Boolean | Global | yes |  |
| `NotifyStepAssigneesComplete` | Notify Step Assignees on Complete? | Boolean | Global | yes |  |
| `PassAdhocToNewWF` | Pass Adhoc Assignee To New Work Flow? | Boolean | Global | yes |  |
| `PassPriorityToNewWF` | Pass Priority To New Work Flow? | Boolean | Global | yes |  |
| `RequireAllApprovers` | Require All Approvers? | Boolean | Global | yes |  |
| `RequireApproverSig` | Require Approver Signature | Boolean | Global |  |  |
| `RestartStep` | Action Should Restart the Step? | Boolean | Global | yes |  |
| `SendPaymentInfo` | Send Payment Info? | Boolean | Global | yes |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActionComment` | Action Comment | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `IsEnabledLxJSCode` | Javascript Source Code | Text | Global |  |  |
| `KickOffDescription` | Kick Off Description | Text | Global |  |  |
| `WorkFlowTemplateStepActionName` | Action Name | Text | Global | yes |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Template Step Action ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [WorkFlowStepApprover](WorkFlowStepApprover.md) | `PriorWFTemplateStepActionID`, `WorkFlowTemplateStepActionID` |
