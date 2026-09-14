# WorkFlowStepAssignee

*11 fields · module: Workflow & Approvals · Postgres: `work_flow_step_assignee`*

One assignee's notification/acknowledgment status on a running WorkFlowStep, parallel to WorkFlowStepApprover for the assignee (rather than approver) role.

Source: `data-fields/workflow-notification-ancillary-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 11 |
| Fields with a vendor definition | 10 of 11 inventoried |
| Physical tables | `work_flow_step_assignee` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 10 (10 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in work_flow_step_assignee

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 10 fields carry a vendor definition

**Observed.** 10 of this record's 11 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 10 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 6 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MemberID` | Assignee | The assignee of the work flow step. | Member ID | Global | yes | `work_flow_step_assignee.MemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `work_flow_step_assignee.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `WorkFlowStepID` | Work Flow Step | The ID of the work flow step. | Work Flow Step ID | Global | yes | `work_flow_step_assignee.WorkFlowStepID · TEXT` | [WorkFlowStep](WorkFlowStep.md) |
| `WorkFlowTemplateStepID` | Work Flow Template Step | The ID of the work flow template. | Step ID | Global |  | `work_flow_step_assignee.WorkFlowTemplateStepID · TEXT` | [WorkFlowStep](WorkFlowStep.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `WorkFlowStepAssigneeID` | WF Step Assignee RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `work_flow_step_assignee.WorkFlowStepAssigneeID · VARCHAR(64) NOT NULL` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EMailSentStatus` | Email Sent Status | Indicates whether the assignee has been sent an email about an alert. | Text | Global | yes | `work_flow_step_assignee.EMailSentStatus · TEXT` |  |
| `NotifyAcknowledgedStatus` | Notify Acknowledged Status | Indicates whether the assignee has acknowledged the workflow alert or email. | Text | Global | yes | `work_flow_step_assignee.NotifyAcknowledgedStatus · TEXT` |  |
| `StepMemberResponsibility` | Step Member Responsibility | This field lists step members whose responsibility matches the responsibility for the workflow template step. | Text | Global | yes | `work_flow_step_assignee.StepMemberResponsibility · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | WF Step Assignee ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `work_flow_step_assignee.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `work_flow_step_assignee.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `work_flow_step_assignee.ModifiedDate · TEXT` |  |
