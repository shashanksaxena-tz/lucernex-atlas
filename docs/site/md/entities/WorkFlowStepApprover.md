# WorkFlowStepApprover

*20 fields · module: Workflow & Approvals · Postgres: `work_flow_step_approver`*

One named approver's action on a running WorkFlowStep — action comment, action taken, and has-approved flag, the audit trail of an individual approval decision. 19 Global fields under Workflow.

Source: `data-fields/work-flow-step-approver.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Catalogued fields | 19 (19 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MemberID` | Approver | Member ID | Global | yes | [Member](Member.md) |
| `PriorWFTemplateStepActionID` | Prior WF Step Action | Action ID | Global |  | [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `WorkFlowStepID` | Work Flow Step | Work Flow Step ID | Global | yes | [WorkFlowStep](WorkFlowStep.md) |
| `WorkFlowTemplateStepActionID` | WF Step Action | Action ID | Global |  | [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) |
| `WorkFlowTemplateStepID` | Work Flow Template Step | Step ID | Global |  | [WorkFlowStep](WorkFlowStep.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `WorkFlowStepApproverID` | WF Step Approver RecID | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActionTakenDate` | Action Taken Date | Date | Global |  |  |
| `PriorActionTakenDate` | Prior Action Taken Date | Date | Global |  |  |
| `SignatureDate` | Signature Date | Date | Global |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HasApproved` | Has Approved? | Boolean | Global |  |  |
| `HasTakenAction` | Has Taken Action? | Boolean | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActionComment` | Action Comment | Text | Global |  |  |
| `ActionTakenName` | Action Taken | Text | Global |  |  |
| `EMailSentStatus` | Email Sent Status | Text | Global | yes |  |
| `NotifyAcknowledgedStatus` | Notify Acknowledged Status | Text | Global | yes |  |
| `PriorActionComment` | Prior Action Comment | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | WF Step Approver ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [WorkFlow](WorkFlow.md) | `WFApproverList` |
