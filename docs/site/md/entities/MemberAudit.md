# MemberAudit

*12 fields · module: People & Parties · Postgres: `member_audit`*

Login/session audit trail for internal Members — action name, audit date, and impersonation tracking for support access.

Source: `data-fields/audit-history-tables.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 12 |
| Catalogued fields | 11 (11 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-042](../rules/RPT-R-042.md) | Login, lockout and impersonation events are audited separately in `MemberAudit`, with `SrcIP` and `UserAgent`. · Observed · `_lucernex_objects_summary.txt` | Observed |
| [PPL-R-008](../rules/PPL-R-008.md) | This is a distinct audit mechanism from `../platform-tenancy/`'s `AuditColumn` (which logs field-level changes) — `MemberAudit` logs session/security events specifically | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ImpersonatingMemberID` | Impersonating Member | Member ID | Global |  | [Member](Member.md) |
| `MemberID` | Member | Member ID | Global | yes | [Member](Member.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeLockOutReasonID` | Login Status | Dropdown (Lock Out Reason Code) | Global |  | Lock Out Reason Code |
| `CodeMemberActionID` | Action Name | Dropdown (Member Action Code) | Global | yes | Member Action Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MemberAuditID` | Member Audit RecID | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AuditDate` | Audit Date | Time | Global | yes |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LogInfo` | Action Details | Text | Global |  |  |
| `SrcIP` | Source IP | Text | Global |  |  |
| `UserAgent` | User Agent | Text | Global |  |  |

### Audit & record keeping (2)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
