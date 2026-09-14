# WorkFlow

*19 fields · module: Workflow & Approvals · Postgres: `work_flow`*

The active workflow instance running against a real trigger object (Trigger CodeSQLTable, Trigger Object) — the runtime record one level above WorkFlowStep. 20 Global fields under Statics and Workflow.

Source: `data-fields/work-flow.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 19 |
| Fields with a vendor definition | 18 of 19 inventoried |
| Physical tables | `work_flow` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 5 keys from 5 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in work_flow

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 18 fields carry a vendor definition

**Observed.** 18 of this record's 19 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 6 of this record's fields required; the Data Fields catalogue marks 6; 6 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-012](../rules/PRJ-R-012.md) | A workflow needs to be triggered by a schedule event · `WorkFlow.KickOffTaskID` → `TaskGroup` · Corroborates the GraphQL `KickOffMethod.TASK` enum value (`graphql-api.md`) — a task reaching some state can kick off a workflow. · Derived | Derived |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `InitiatedByMemberID` | Initiated By Member | The member ID of the user who initiated the work flow. | Member ID | Global |  | `work_flow.InitiatedByMemberID · TEXT` | [Member](Member.md) |
| `KickOffTaskID` | Kick Off Task | The ID of the schedule task that kicked off the work flow. | Task/Group ID | Global |  | `work_flow.KickOffTaskID · TEXT` | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `work_flow.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `WFApproverList` | WF Approver List | This field displays a pick list where you can select approvers assigned to the entity to approve the work flow. | Work Flow Step Approver ID | Global |  | `work_flow.WFApproverList · TEXT` | [WorkFlowStepApprover](WorkFlowStepApprover.md) |
| `WorkFlowTemplateID` | Workflow Template | The ID of the work flow. | Work Flow ID | Global | yes | `work_flow.WorkFlowTemplateID · TEXT` | [WorkFlow](WorkFlow.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdhocMemberID` | Ad Hoc Assignee | Select an ad hoc assignee from this field. | Member | Global |  | `work_flow.AdhocMemberID · TEXT` |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeWorkFlowStatusID` | Status | This field displays the status of the work flow on the Work Flows page. | Dropdown (Work Flow Status Code) | Global | yes | `work_flow.CodeWorkFlowStatusID · TEXT` | Work Flow Status Code |
| `WorkFlowCodePriorityID` | Priority | The priority of the work flow. | Dropdown (Priority Code) | Global | yes | `work_flow.WorkFlowCodePriorityID · TEXT` | Priority Code |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `NumberOfDaysOpen` | Number Of Days Open | This field captures how many days the work flow has been open. | Number | Global |  | `work_flow.NumberOfDaysOpen · TEXT` |  |
| `WorkFlowID` | Work Flow RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `work_flow.WorkFlowID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ClosedDate` | Closed Date | The date that the work flow was closed. | Date | Global |  | `work_flow.ClosedDate · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Inactive` | Inactive? | If true, this work flow has been deactivated on the Work Flow page. | Boolean | Global | yes | `work_flow.Inactive · TEXT` |  |
| `IsCompleted` | Is Completed? | If true, this work flow has been completed. | Boolean | Global |  | `work_flow.IsCompleted · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `KickOffIssueID` | Kick Off Form | The ID of the form that kicked off the work flow. | Text | Global |  | `work_flow.KickOffIssueID · TEXT` |  |
| `WorkFlowName` | Name | The name of the work flow. | Text | Global | yes | `work_flow.WorkFlowName · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `work_flow.BOMapClientRecordID · TEXT` |  |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `work_flow.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `work_flow.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `work_flow.ModifiedDate · TEXT` |  |

## What points here (5 keys)

| Record type | Via column |
|---|---|
| [WFStepFullImport](WFStepFullImport.md) | `WorkFlowID` |
| [WorkFlow](WorkFlow.md) | `WorkFlowTemplateID` |
| [WorkFlowStep](WorkFlowStep.md) | `WorkFlowID` |
| [WorkFlowTemplateStep](WorkFlowTemplateStep.md) | `WorkFlowTemplateID` |
| [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) | `KickOffWorkFlowTemplateID` |
