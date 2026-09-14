# WorkFlow

*19 fields · module: Workflow & Approvals · Postgres: `work_flow`*

The active workflow instance running against a real trigger object (Trigger CodeSQLTable, Trigger Object) — the runtime record one level above WorkFlowStep. 20 Global fields under Statics and Workflow.

Source: `data-fields/work-flow.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 5 keys from 5 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-012](../rules/PRJ-R-012.md) | A workflow needs to be triggered by a schedule event · `WorkFlow.KickOffTaskID` → `TaskGroup` · Corroborates the GraphQL `KickOffMethod.TASK` enum value (`graphql-api.md`) — a task reaching some state can kick off a workflow. · Derived | Derived |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `InitiatedByMemberID` | Initiated By Member | Member ID | Global |  | [Member](Member.md) |
| `KickOffTaskID` | Kick Off Task | Task/Group ID | Global |  | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `WFApproverList` | WF Approver List | Work Flow Step Approver ID | Global |  | [WorkFlowStepApprover](WorkFlowStepApprover.md) |
| `WorkFlowTemplateID` | Workflow Template | Work Flow ID | Global | yes | [WorkFlow](WorkFlow.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdhocMemberID` | Ad Hoc Assignee | Member | Global |  |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeWorkFlowStatusID` | Status | Dropdown (Work Flow Status Code) | Global | yes | Work Flow Status Code |
| `WorkFlowCodePriorityID` | Priority | Dropdown (Priority Code) | Global | yes | Priority Code |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `NumberOfDaysOpen` | Number Of Days Open | Number | Global |  |  |
| `WorkFlowID` | Work Flow RecID | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ClosedDate` | Closed Date | Date | Global |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` | Inactive? | Boolean | Global | yes |  |
| `IsCompleted` | Is Completed? | Boolean | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `KickOffIssueID` | Kick Off Form | Text | Global |  |  |
| `WorkFlowName` | Name | Text | Global | yes |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow ClientID | Text | Global | yes |  |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (5 keys)

| Record type | Via column |
|---|---|
| [WFStepFullImport](WFStepFullImport.md) | `WorkFlowID` |
| [WorkFlow](WorkFlow.md) | `WorkFlowTemplateID` |
| [WorkFlowStep](WorkFlowStep.md) | `WorkFlowID` |
| [WorkFlowTemplateStep](WorkFlowTemplateStep.md) | `WorkFlowTemplateID` |
| [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) | `KickOffWorkFlowTemplateID` |
