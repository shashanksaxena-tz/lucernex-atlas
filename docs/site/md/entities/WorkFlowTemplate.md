# WorkFlowTemplate

*25 fields · module: Workflow & Approvals · Postgres: `work_flow_template`*

The top-level workflow definition (the container for WorkFlowTemplateStep records) — active layout, associated task, and auto-assignment rules for the initiator. 25 Global fields under Company Items.

Source: `data-fields/work-flow-template.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 25 |
| Fields with a vendor definition | 23 of 25 inventoried |
| Physical tables | `work_flow_template` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 25 (25 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in work_flow_template

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 23 fields carry a vendor definition

**Observed.** 23 of this record's 25 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 9 fields marked required

**Observed.** The inventory marks 9 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [WF-R-005](../rules/WF-R-005.md) | The workflow's own attachability is whatever its kick-off form's Form Type declares. WorkFlowTemplate carries no IsValidFor* columns of its own — the chain runs through PageLayoutID to the layout's Form Type. | Derived |
| [LAY-R-165](../rules/LAY-R-165.md) | Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesI | Observed |

## Fields

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CollaboratorJobTitleIDList` | Collaborator Job Title List |  | Dropdown (Job Title Code) | Global |  | `work_flow_template.CollaboratorJobTitleIDList · TEXT` | Job Title Code |
| `DefaultWFCodePriorityID` | Default Work Flow Priority | Select the priority of the work flow from this field. | Dropdown (Priority Code) | Global | yes | `work_flow_template.DefaultWFCodePriorityID · TEXT` | Priority Code |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `KickOffID` | Work Flow Kick-off Record | Displays the workflow template kickoff ID. | Number | Global |  | `work_flow_template.KickOffID · TEXT` |  |
| `StatusChangeID` | Status Change ID | Gives the status change id of the workflow template kick off. | Number | Global |  | `work_flow_template.StatusChangeID · TEXT` |  |
| `StatusChangeType` | Status Change Type | Gives the status change type of the workflow template kick off. | Number | Global |  | `work_flow_template.StatusChangeType · TEXT` |  |
| `WorkFlowTemplateID` | Work Flow Template RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `work_flow_template.WorkFlowTemplateID · VARCHAR(64) NOT NULL` |  |

### Flags (6)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AutoAssignInitiator` | Auto Assign Initiator as Ad Hoc Assignee | When selected, the system will automatically assign the person who kicks off the work flow as an ad hoc assignee to the kickoff step or form, and on any step that requires an ad hoc assignee in the work flow. For more information about this functionality, see the Manage Work Flows page in the Lx Online Help. | Boolean | Global | yes | `work_flow_template.AutoAssignInitiator · TEXT` |  |
| `EnableVendorCollaboration` | Enable Vendor Collaboration |  | Boolean | Global | yes | `work_flow_template.EnableVendorCollaboration · TEXT` |  |
| `LimitByEntity` | Limit By Entity? | If this value is 1, the work flow template is only available for certain portfolios. If this value is 0, the work flow template is available for all portfolios. | Boolean | Global | yes | `work_flow_template.LimitByEntity · TEXT` |  |
| `NotifyAllApproversComplete` | Notify All Approvers When Complete? | Select this check box if you want to send an email notification to prior work flow approvers when the work flow is complete. | Boolean | Global | yes | `work_flow_template.NotifyAllApproversComplete · TEXT` |  |
| `NotifyAllAssigneesComplete` | Notify All Assignees When Complete? | Select this check box if you want to send and email notification to prior work flow assignees when the work flow is complete. | Boolean | Global | yes | `work_flow_template.NotifyAllAssigneesComplete · TEXT` |  |
| `NotifyInitiatorComplete` | Notify Initiator When Complete? | Select this check box if you want to send an email notification to the work flow initiator when the work flow is complete. | Boolean | Global | yes | `work_flow_template.NotifyInitiatorComplete · TEXT` |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `work_flow_template.Description · TEXT` |  |
| `IsEnabledLxJSCode` | Javascript Source Code | This field is where you will enter your custom JavaScript used to kick off conditional work flows. | Text | Global |  | `work_flow_template.IsEnabledLxJSCode · TEXT` |  |
| `KickOffDescription` | Description of KickOff | Contains the text description of the kick off step or form. | Text | Global |  | `work_flow_template.KickOffDescription · TEXT` |  |
| `KickOffMethod` | Kick-off Method | There are three ways a work flow can be kicked off: by completion of an action in another work flow, by completion of a schedule task, or by completion of a form. | Text | Global |  | `work_flow_template.KickOffMethod · TEXT` |  |
| `PageLayoutID` | Active Layout | Select the form whose completion you want to have kick off this work flow. | Text | Global |  | `work_flow_template.PageLayoutID · TEXT` |  |
| `TaskName` | Associated Task | Select the schedule task whose completion you want to have kick off this work flow. | Text | Global |  | `work_flow_template.TaskName · TEXT` |  |
| `WorkFlowTemplateName` | Work Flow Template Name | Enter the name of your work flow template in this field. | Text | Global | yes | `work_flow_template.WorkFlowTemplateName · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Template ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `work_flow_template.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `work_flow_template.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `work_flow_template.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `work_flow_template.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `work_flow_template.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `work_flow_template.RevNumber · TEXT` |  |
