# LinkTaskMember

*5 fields · module: Capital Projects & Scheduling · Postgres: `link_task_member`*

Join table assigning a specific Member to a specific Task on a ProjectEntity.

Source: `data-fields/link-relationship-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 5 |
| Fields with a vendor definition | 2 of 5 inventoried |
| Physical tables | `link_task_member` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 5 (5 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_task_member

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 2 fields carry a vendor definition

**Observed.** 2 of this record's 5 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 5 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 3 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [PRJ-R-011](../rules/PRJ-R-011.md) | A task needs a named assignee · `LinkTaskMember.MemberID` · Assigns a specific `Member`, alongside `TaskGroup.Assignee_MemberID`'s own direct field — two mechanisms for the same concept exist side by side. · Observed | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MemberID` | Member | The member ID of the user assigned to a task. | Member ID | Global | yes | `link_task_member.MemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` | Project Entity | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Entity ID | Global | yes | `link_task_member.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `TaskID` | Task |  | Task/Group ID | Global | yes | `link_task_member.TaskID · TEXT` | [TaskGroup](TaskGroup.md) |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `link_task_member.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `link_task_member.ModifiedDate · TEXT` |  |
