# AuditColumn

*14 fields · module: Platform & Tenancy · Postgres: `none exported`*

Metadata defining which columns on a table are tracked for audit history — accessor name and audit action per tracked field.

Source: `data-fields/audit-history-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 14 |
| Fields with a vendor definition | 14 of 14 inventoried |
| Physical tables | — |
| Replication database | — |
| Catalogued fields | 14 (14 global, 0 firm) |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 7 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 14 fields carry a vendor definition

**Observed.** 14 of this record's 14 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 14 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 1 are marked required.

### 14 fields excluded from extraction

**Observed.** Observed of the loader. The inventory marks 14 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [LAY-R-201](../rules/LAY-R-201.md) | Field-level value changes are audited in `AuditColumn`, filed under the registry's group and subgroup — so an audit entry inherits the Data Fields taxonomy. · Derived (11-for-11 column match) · 007; | Derived |
| [RPT-R-040](../rules/RPT-R-040.md) | Field-level change audit is stored in `AuditColumn`, with `EntityName`, `CodeSQLTableID`, `ObjectID`, `FieldName`, `AuditAction`, `OldValue`, `NewValue` and the actor/timestamp. · Observed · `all-fields.csv` | Observed |
| [RPT-R-041](../rules/RPT-R-041.md) | Audit entries are filed under the field registry's group tree — `AuditColumn.GroupID` and `.SubGroupID` both point at `ReportGroupData`. An audit report can therefore be grouped by the same taxonomy as a form or a report. | Observed |
| [RPT-R-043](../rules/RPT-R-043.md) | The Audit Log dialog is a generic viewer over `AuditColumn`, reachable from an individual record's editor — not only from a central Audit Reports screen. · Derived · 007 | Derived |
| [PLT-R-012](../rules/PLT-R-012.md) | 162 of 223 objects carry the inline stamps (161 `ModifiedByID`, only 79 `CreatedByID`); it is unknown which objects also emit `AuditColumn` rows | Derived |
| [PLT-R-013](../rules/PLT-R-013.md) | "Group Name"/"Sub-Group" columns a user sees in an Audit Log screen are the same registry group/subgroup names used everywhere else field metadata is organised | Derived |
| [PPL-R-008](../rules/PPL-R-008.md) | This is a distinct audit mechanism from `../platform-tenancy/`'s `AuditColumn` (which logs field-level changes) — `MemberAudit` logs session/security events specifically | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GroupID` |  | The RGAF group ID of the field being audited. | item ID | Global |  | not extracted | unresolved |
| `ProjectEntityID` |  | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Entity ID | Global |  | not extracted | [ProjectEntity](ProjectEntity.md) |
| `SubGroupID` |  | The RGAF subgroup ID of the field being audited. | item ID | Global |  | not extracted | unresolved |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeSQLTableID` |  | The database table name of the field that was updated. | Dropdown (SQL Table Code) | Global |  | not extracted | SQL Table Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ObjectID` |  | The primary key of the record of the field being audited. | Number | Global |  | not extracted |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccessorName` |  | An accessor name is the database column name corresponding to the record being audited. | Text | Global | yes | not extracted |  |
| `AuditAction` |  | The action taken. There are three types of actions: Add, Update, and Delete. | Text | Global |  | not extracted |  |
| `EntityName` |  | The entity name where the field was updated. | Text | Global |  | not extracted |  |
| `FieldName` |  | The user-facing label of the field that was updated. | Text | Global |  | not extracted |  |
| `NewValue` |  | The new value of the field that was updated. | Text | Global |  | not extracted |  |
| `OldValue` |  | The old value of the field that was updated. | Text | Global |  | not extracted |  |
| `ScriptName` |  | The RGAF accessor name of the field being audited. | Text | Global |  | not extracted |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` |  | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | not extracted | [Member](Member.md) |
| `CreatedDate` |  | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | not extracted |  |
