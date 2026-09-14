# WorkFlowTemplate

*25 fields · module: Workflow & Approvals · Postgres: `work_flow_template`*

The top-level workflow definition (the container for WorkFlowTemplateStep records) — active layout, associated task, and auto-assignment rules for the initiator. 25 Global fields under Company Items.

Source: `data-fields/work-flow-template.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 25 |
| Catalogued fields | 25 (25 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | firm_global |
| Rules that name it | 2 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [WF-R-005](../rules/WF-R-005.md) | The workflow's own attachability is whatever its kick-off form's Form Type declares. WorkFlowTemplate carries no IsValidFor* columns of its own — the chain runs through PageLayoutID to the layout's Form Type. | Derived |
| [LAY-R-165](../rules/LAY-R-165.md) | Forms are the workflow engine's rendering surface, bound at two levels: `WorkFlowTemplate.PageLayoutID` is the single kick-off/Submit form for the whole workflow, while `WorkFlowTemplateStep.PageLayoutApproversID` and `.PageLayoutAssigneesI | Observed |

## Fields

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CollaboratorJobTitleIDList` | Collaborator Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `DefaultWFCodePriorityID` | Default Work Flow Priority | Dropdown (Priority Code) | Global | yes | Priority Code |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `KickOffID` | Work Flow Kick-off Record | Number | Global |  |  |
| `StatusChangeID` | Status Change ID | Number | Global |  |  |
| `StatusChangeType` | Status Change Type | Number | Global |  |  |
| `WorkFlowTemplateID` | Work Flow Template RecID | Number | Global |  |  |

### Flags (6)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AutoAssignInitiator` | Auto Assign Initiator as Ad Hoc Assignee | Boolean | Global | yes |  |
| `EnableVendorCollaboration` | Enable Vendor Collaboration | Boolean | Global | yes |  |
| `LimitByEntity` | Limit By Entity? | Boolean | Global | yes |  |
| `NotifyAllApproversComplete` | Notify All Approvers When Complete? | Boolean | Global | yes |  |
| `NotifyAllAssigneesComplete` | Notify All Assignees When Complete? | Boolean | Global | yes |  |
| `NotifyInitiatorComplete` | Notify Initiator When Complete? | Boolean | Global | yes |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `IsEnabledLxJSCode` | Javascript Source Code | Text | Global |  |  |
| `KickOffDescription` | Description of KickOff | Text | Global |  |  |
| `KickOffMethod` | Kick-off Method | Text | Global |  |  |
| `PageLayoutID` | Active Layout | Text | Global |  |  |
| `TaskName` | Associated Task | Text | Global |  |  |
| `WorkFlowTemplateName` | Work Flow Template Name | Text | Global | yes |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Work Flow Template ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
