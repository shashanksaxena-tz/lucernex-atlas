# WorkFlowStepAssignee

*11 fields · module: Workflow & Approvals · Postgres: `work_flow_step_assignee`*

One assignee's notification/acknowledgment status on a running WorkFlowStep, parallel to WorkFlowStepApprover for the assignee (rather than approver) role.

Source: `data-fields/workflow-notification-ancillary-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 11 |
| Catalogued fields | 10 (10 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MemberID` | Assignee | Member ID | Global | yes | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `WorkFlowStepID` | Work Flow Step | Work Flow Step ID | Global | yes | [WorkFlowStep](WorkFlowStep.md) |
| `WorkFlowTemplateStepID` | Work Flow Template Step | Step ID | Global |  | [WorkFlowStep](WorkFlowStep.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `WorkFlowStepAssigneeID` | WF Step Assignee RecID | Number | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EMailSentStatus` | Email Sent Status | Text | Global | yes |  |
| `NotifyAcknowledgedStatus` | Notify Acknowledged Status | Text | Global | yes |  |
| `StepMemberResponsibility` | Step Member Responsibility | Text | Global | yes |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | WF Step Assignee ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
