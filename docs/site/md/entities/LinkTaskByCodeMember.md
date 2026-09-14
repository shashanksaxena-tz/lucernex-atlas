# LinkTaskByCodeMember

*8 fields · module: Capital Projects & Scheduling · Postgres: `link_task_by_code_member`*

Join table assigning a Task to a Member by job title/org-chart level rather than by name.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 8 |
| Fields with a vendor definition | 7 of 8 inventoried |
| Physical tables | `link_task_by_code_member` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 7 (7 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_task_by_code_member

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 7 fields carry a vendor definition

**Observed.** 7 of this record's 8 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 7 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 2 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-010](../rules/PRJ-R-010.md) | A task needs an assignee, but not a named individual · `LinkTaskByCodeMember.CodeJobTitleID`, `OrgChartLevel` · Assigns by job title / org-chart level rather than by `Member`, matching the `AssigneeType` = `JOB_TITLE` routing option (`graph | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `link_task_by_code_member.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `TaskID` | Task | The task ID. | Task/Group ID | Global | yes | `link_task_by_code_member.TaskID · TEXT` | [TaskGroup](TaskGroup.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeJobTitleID` | Job Title | The job title that should be automatically assigned to a task. | Dropdown (Job Title Code) | Global |  | `link_task_by_code_member.CodeJobTitleID · TEXT` | Job Title Code |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `LinkTaskByCodeMemberID` | Template Auto-Assignment RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `link_task_by_code_member.LinkTaskByCodeMemberID · VARCHAR(64) NOT NULL` |  |
| `OrgChartLevel` | Org Chart Level | The org chart level that should be automatically assigned to a task. | Number | Global |  | `link_task_by_code_member.OrgChartLevel · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Template Auto-Assignmen ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `link_task_by_code_member.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `link_task_by_code_member.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `link_task_by_code_member.ModifiedDate · TEXT` |  |
