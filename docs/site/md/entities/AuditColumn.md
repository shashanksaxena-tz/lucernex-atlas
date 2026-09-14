# AuditColumn

*14 fields · module: Platform & Tenancy · Postgres: `none exported`*

Metadata defining which columns on a table are tracked for audit history — accessor name and audit action per tracked field.

Source: `data-fields/audit-history-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 14 |
| Catalogued fields | 14 (14 global, 0 firm) |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 7 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GroupID` |  | item ID | Global |  | unresolved |
| `ProjectEntityID` |  | Entity ID | Global |  | [ProjectEntity](ProjectEntity.md) |
| `SubGroupID` |  | item ID | Global |  | unresolved |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeSQLTableID` |  | Dropdown (SQL Table Code) | Global |  | SQL Table Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ObjectID` |  | Number | Global |  |  |

### Text & notes (7)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccessorName` |  | Text | Global | yes |  |
| `AuditAction` |  | Text | Global |  |  |
| `EntityName` |  | Text | Global |  |  |
| `FieldName` |  | Text | Global |  |  |
| `NewValue` |  | Text | Global |  |  |
| `OldValue` |  | Text | Global |  |  |
| `ScriptName` |  | Text | Global |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` |  | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` |  | Time | Global |  |  |
