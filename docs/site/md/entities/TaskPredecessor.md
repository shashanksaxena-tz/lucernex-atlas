# TaskPredecessor

*15 fields · module: Capital Projects & Scheduling · Postgres: `task_predecessor`*

Defines a dependency between two Task records, with actual lead/lag days — the scheduling-network edge beneath Task.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 15 |
| Fields with a vendor definition | 14 of 15 inventoried |
| Physical tables | `task_predecessor` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 14 (14 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in task_predecessor

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 14 fields carry a vendor definition

**Observed.** 14 of this record's 15 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 6 fields marked required

**Observed.** The inventory marks 6 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-006](../rules/PRJ-R-006.md) | A `TaskGroup` row's schedule position is computed · `ParentTaskID` (hierarchy) vs. `TaskPredecessor.PredecessorTaskID`/`SuccessorTaskID` (dependency network) · Two independent graphs. | Derived |
| [PRJ-R-007](../rules/PRJ-R-007.md) | The Gantt engine (`TaskGantt2.jsp`) needs a task's critical-path status · `TaskGroup.OnCriticalPath`, `DaysAheadOfSchedule` · Plausibly computed by walking the `TaskPredecessor` graph; no formula or screen confirms the exact computation. | Inferred |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PredecessorTaskID` | Predecessor Task | Select the predecessor task from this field. | Task/Group ID | Global |  | `task_predecessor.PredecessorTaskID · TEXT` | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `task_predecessor.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `SuccessorTaskID` | Successor Task | Select the successor task from this field. | Task/Group ID | Global | yes | `task_predecessor.SuccessorTaskID · TEXT` | [TaskGroup](TaskGroup.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeTaskLeadLagTypeID` | Task Lead Lag Type | Select the relationship type of the two tasks from this field. If this value is Start-to-Start, the start date of the successor task is dependent upon the start date of the predecessor task. If this value is Finish-to-Start, the start date of the successor task is dependent upon the finish date of the predecessor task. | Dropdown (Task Lead Lag Type Code) | Global | yes | `task_predecessor.CodeTaskLeadLagTypeID · TEXT` | Task Lead Lag Type Code |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualLeadLagDays` | Actual Lead Lag Days | The actual lead / lag days of the task predecessor. This value is used when a task checks if all of its predecessors have completed (where all of their lead days are < 0). | Number | Global | yes | `task_predecessor.ActualLeadLagDays · TEXT` |  |
| `OriginalLeadLagDays` | Original Lead Lag Days | The original lead / lag days of the task predecessor. | Number | Global | yes | `task_predecessor.OriginalLeadLagDays · TEXT` |  |
| `ProjectedLeadLagDays` | Projected Lead/Lag Days | Enter the number of lead or lag days in this field. | Number | Global | yes | `task_predecessor.ProjectedLeadLagDays · TEXT` |  |
| `TaskPredecessorID` | Task Predecessor RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `task_predecessor.TaskPredecessorID · VARCHAR(64) NOT NULL` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PredecessorTemplateTaskName` | Predecessor Task Name | This field displays the name of the predecessor task. | Text | Global |  | `task_predecessor.PredecessorTemplateTaskName · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Task Predecessor ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `task_predecessor.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `task_predecessor.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `task_predecessor.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `task_predecessor.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `task_predecessor.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `task_predecessor.RevNumber · TEXT` |  |
