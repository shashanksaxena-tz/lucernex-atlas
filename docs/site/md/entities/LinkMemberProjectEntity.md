# LinkMemberProjectEntity

*7 fields · module: Platform & Tenancy · Postgres: `link_member_project_entity`*

A join record linking an internal Member to a ProjectEntity in an org-chart role — manager name/title and job function, despite the Link-style name it carries enough project-team detail (24 fields) to warrant standalone treatment. 24 Global fields spanning Statics and Summary Information.

Source: `data-fields/link-member-project-entity.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 7 |
| Fields with a vendor definition | 7 of 7 inventoried |
| Physical tables | `link_member_project_entity` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 24 (24 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in link_member_project_entity

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 7 fields carry a vendor definition

**Observed.** 7 of this record's 7 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 4; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [WF-R-026](../rules/WF-R-026.md) | The step's ApproverJobTitleIDList is intersected against the roster of the entity the workflow is running on, filtered to members holding a matching job title, and the resulting flat member list is frozen onto the running step as WorkFlowSt | Derived |
| [PLT-R-003](../rules/PLT-R-003.md) | The target architecture is database-per-tenant (one Spoke database per firm) | Derived |
| [PPL-R-009](../rules/PPL-R-009.md) | A person can be selected by class, by title (global or entity-specific), or by reporting-line position, and these three do not have to agree with each other | Observed |
| [PPL-R-010](../rules/PPL-R-010.md) | Differs from `Member.CodeJobTitleID` | Inferred |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MemberID` | Member | The member ID of the user on the entity. | Member ID | Global | yes | `link_member_project_entity.MemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` | Entity | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Entity ID | Global | yes | `link_member_project_entity.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssignedCodeJobTitleIDList` | Entity Assigned Job Title List | This field updates the database to include the job titles that override the member's default job title. | Dropdown (Job Title Code) | Global |  | `link_member_project_entity.AssignedCodeJobTitleIDList · TEXT` | Job Title Code |
| `CodeJobTitleIDList` | Entity Job Title List | This field lists the job titles currently configured for the member on this entity. | Dropdown (Job Title Code) | Global |  | `link_member_project_entity.CodeJobTitleIDList · TEXT` | Job Title Code |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsManager` | Is Manager? | If this field's value is true, the member is a manager on the entity. | Boolean | Global | yes | `link_member_project_entity.IsManager · TEXT` |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `link_member_project_entity.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `link_member_project_entity.ModifiedDate · TEXT` |  |
