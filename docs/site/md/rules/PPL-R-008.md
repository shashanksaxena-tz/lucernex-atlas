# PPL-R-008 — `MemberAudit` is login/session audit, not field-change audit

*People & Parties · Observed*

**This is a distinct audit mechanism from `../platform-tenancy/`'s `AuditColumn` (which logs field-level changes) — `MemberAudit` logs session/security events specifically.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | A member logs in, is impersonated (support access), or performs an audited action |
| What it reads | `MemberAudit.CodeMemberActionID`, `AuditDate`, `ImpersonatingMemberID`, `SrcIP`, `UserAgent` |
| What it writes | This is a distinct audit mechanism from `../platform-tenancy/`'s `AuditColumn` (which logs field-level changes) — `MemberAudit` logs session/security events specifically |

## What it constrains

[MemberAudit](../entities/MemberAudit.md), [AuditColumn](../entities/AuditColumn.md)

Columns named: `MemberAudit.CodeMemberActionID`

## Confidence

Observed, field export. ## Security and routing (owned jointly with `platform-tenancy` and `workflow`)

---

Source: `docs/modules/people-parties/rules.md`
