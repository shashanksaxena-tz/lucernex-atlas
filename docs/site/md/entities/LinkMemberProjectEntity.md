# LinkMemberProjectEntity

*7 fields · module: Platform & Tenancy · Postgres: `link_member_project_entity`*

A join record linking an internal Member to a ProjectEntity in an org-chart role — manager name/title and job function, despite the Link-style name it carries enough project-team detail (24 fields) to warrant standalone treatment. 24 Global fields spanning Statics and Summary Information.

Source: `data-fields/link-member-project-entity.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 7 |
| Catalogued fields | 24 (24 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MemberID` | Member | Member ID | Global | yes | [Member](Member.md) |
| `ProjectEntityID` | Entity | Entity ID | Global | yes | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssignedCodeJobTitleIDList` | Entity Assigned Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `CodeJobTitleIDList` | Entity Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsManager` | Is Manager? | Boolean | Global | yes |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
