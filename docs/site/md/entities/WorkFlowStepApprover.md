# WorkFlowStepApprover

*20 fields · module: Workflow & Approvals · Postgres: `work_flow_step_approver`*

One named approver's action on a running WorkFlowStep — action comment, action taken, and has-approved flag, the audit trail of an individual approval decision. 19 Global fields under Workflow.

Source: `data-fields/work-flow-step-approver.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Fields with a vendor definition | 19 of 20 inventoried |
| Physical tables | `work_flow_step_approver` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 19 (19 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in work_flow_step_approver

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 19 fields carry a vendor definition

**Observed.** 19 of this record's 20 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 5 of this record's fields required; the Data Fields catalogue marks 5; 5 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MemberID` | Approver | The member ID of the approver. | Member ID | Global | yes | `work_flow_step_approver.MemberID · TEXT` | [Member](Member.md) |
| `PriorWFTemplateStepActionID` | Prior WF Step Action | The action that a previous approver took on this work flow step. | Action ID | Global |  | `work_flow_step_approver.PriorWFTemplateStepActionID · TEXT` | [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `work_flow_step_approver.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `WorkFlowStepID` | Work Flow Step | The ID of the work flow step. | Work Flow Step ID | Global | yes | `work_flow_step_approver.WorkFlowStepID · TEXT` | [WorkFlowStep](WorkFlowStep.md) |
| `WorkFlowTemplateStepActionID` | WF Step Action | The approver should select the appropriate action for the work flow step from this field. | Action ID | Global |  | `work_flow_step_approver.WorkFlowTemplateStepActionID · TEXT` | [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) |
| `WorkFlowTemplateStepID` | Work Flow Template Step | The ID of the work flow template. | Step ID | Global |  | `work_flow_step_approver.WorkFlowTemplateStepID · TEXT` | [WorkFlowStep](WorkFlowStep.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `WorkFlowStepApproverID` | WF Step Approver RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `work_flow_step_approver.WorkFlowStepApproverID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActionTakenDate` | Action Taken Date | The date the approver took action on the work flow step. | Date | Global |  | `work_flow_step_approver.ActionTakenDate · TEXT` |  |
| `PriorActionTakenDate` | Prior Action Taken Date | The date that a previous action was taken on the work flow step. | Date | Global |  | `work_flow_step_approver.PriorActionTakenDate · TEXT` |  |
| `SignatureDate` | Signature Date | The date an approver's signature was applied to a work flow form step. | Date | Global |  | `work_flow_step_approver.SignatureDate · TEXT` |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HasApproved` | Has Approved? | If this value is true, the work flow step has been approved. | Boolean | Global |  | `work_flow_step_approver.HasApproved · TEXT` |  |
| `HasTakenAction` | Has Taken Action? | If this value is true, the approver has taken action on the work flow step. | Boolean | Global |  | `work_flow_step_approver.HasTakenAction · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActionComment` | Action Comment | Enter any comments about the action taken on the work flow step. | Text | Global |  | `work_flow_step_approver.ActionComment · TEXT` |  |
| `ActionTakenName` | Action Taken | The name of the action taken on the work flow step. | Text | Global |  | `work_flow_step_approver.ActionTakenName · TEXT` |  |
| `EMailSentStatus` | Email Sent Status | Indicates whether the assignee has been sent an email about an alert. | Text | Global | yes | `work_flow_step_approver.EMailSentStatus · TEXT` |  |
| `NotifyAcknowledgedStatus` | Notify Acknowledged Status | Indicates whether the approver has acknowledged the workflow alert or email. | Text | Global | yes | `work_flow_step_approver.NotifyAcknowledgedStatus · TEXT` |  |
| `PriorActionComment` | Prior Action Comment | The previous comment added about an action taken on the work flow step. | Text | Global |  | `work_flow_step_approver.PriorActionComment · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | WF Step Approver ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `work_flow_step_approver.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `work_flow_step_approver.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `work_flow_step_approver.ModifiedDate · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [WorkFlow](WorkFlow.md) | `WFApproverList` |
