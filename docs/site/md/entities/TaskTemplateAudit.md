# TaskTemplateAudit

*18 fields · module: Capital Projects & Scheduling · Postgres: `task_template_audit`*

Not covered by the Data Fields catalogue: this record type appears in the 223-object census but has no row in the catalogue of 6,158 configurable fields, so no document describes the record as a whole. What is known is structural — 18 declared fields, filed under Capital Projects & Scheduling, 0 foreign keys pointing at it. Its fields are documented even though the record is not: 17 of its 18 inventoried fields carry a definition written by the vendor. Open the field groups below and read them — that is the best account of this record available.

Source: `data-model/pg/bbw-field-inventory.csv`, `_lucernex_objects_summary.txt`

## At a glance

|  | Value |
|---|---|
| Fields declared | 18 |
| Fields with a vendor definition | 17 of 18 inventoried |
| Physical tables | `task_template_audit` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | not in the catalogue |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 7 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in task_template_audit

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 17 fields carry a vendor definition

**Observed.** 17 of this record's 18 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetEntityTemplateID` | Budget Template | The ID of the budget template that was applied to the entity. | Template ID | — |  | `task_template_audit.BudgetEntityTemplateID · TEXT` | [EntityTemplate](EntityTemplate.md) |
| `EntityTemplateID` | Entity Template | The ID of the template type. | Template ID | — | yes | `task_template_audit.EntityTemplateID · TEXT` | [EntityTemplate](EntityTemplate.md) |
| `FolderEntityTemplateID` | Folder Template | The ID of the folder template that was applied to the entity. | Template ID | — |  | `task_template_audit.FolderEntityTemplateID · TEXT` | [EntityTemplate](EntityTemplate.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `task_template_audit.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `TaskEntityTemplateID` | Task Template | The ID of the schedule template that was applied to the entity. | Template ID | — |  | `task_template_audit.TaskEntityTemplateID · TEXT` | [EntityTemplate](EntityTemplate.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeFolderActionIDList` | Folder Template Action List | This field is not implemented for this table. | Dropdown (Folder Template Action Code) | — |  | `task_template_audit.CodeFolderActionIDList · TEXT` | Folder Template Action Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `TemplateAuditID` | Template Audit RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | — |  | `task_template_audit.TemplateAuditID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AppliedDate` | Applied Date | The date when the schedule template was applied to an entity. | Time | — | yes | `task_template_audit.AppliedDate · TEXT` |  |
| `ScheduleEndDate` | Schedule End Date | The end date of the schedule. | Date | — |  | `task_template_audit.ScheduleEndDate · TEXT` |  |
| `ScheduleStartDate` | Schedule Start Date | The start date of the schedule. | Date | — |  | `task_template_audit.ScheduleStartDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CopyFolderStructure` | Copy Folder Structure? | If the value of this field is true, a folder template has been applied. | Boolean | — |  | `task_template_audit.CopyFolderStructure · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EntityTemplateTypeName` | Entity Template Type | The plain text name of the template type. | Text | — |  | `task_template_audit.EntityTemplateTypeName · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Template Audit ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | — | yes | `task_template_audit.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | — |  | `task_template_audit.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `task_template_audit.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `task_template_audit.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `task_template_audit.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | `task_template_audit.RevNumber · TEXT` |  |
