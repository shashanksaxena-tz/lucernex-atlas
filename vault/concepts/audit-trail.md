---
title: The audit trail
tags: [concept, security, platform]
evidence: Observed
---

Field-level, with old and new values, written **synchronously and in-transaction** — no outbox, no
queue. The tables are `AuditMaster` / `AuditTable` / `AuditColumn`, surfaced through
[[screen-audit-reports|Audit Reports]] and through a per-value audit log on
[[client-drop-down|client drop-downs]].

This bears directly on an open ASG Edge+ decision: **ADR-0020 (in-transaction audit) versus ADR-0012
(the outbox, still only a `NoOpOutboxPublisher`)**. The incumbent chose in-transaction. That is not an
argument that ASG Edge+ should, but it is evidence about what the behaviour looks like in production.

**Two unreconciled audit mechanisms coexist** ([[rule-PLT-R-012]]):

- `AuditColumn` / `AuditTable` — the field-change trail above.
- Inline `CreatedByID` / `ModifiedByID` / `CreatedDate` / `ModifiedDate` stamps on the rows
  themselves — **162 of 223** objects carry at least one, but only **79** carry `CreatedByID` against
  **161** carrying `ModifiedByID`.

A third, separate thing is `MemberAudit`, which is login, session and impersonation audit — not field
change ([[rule-PPL-R-008]]).

The inline stamps are also why [[Member]] looks like the schema's biggest hub and is not:
**240 of its 290 inbound foreign keys are just the `CreatedByID`/`ModifiedByID` pair** — one
cross-cutting concern, not 161 relationships ([[rule-PPL-R-007]]).

Source: [`features/security-access/`](../../docs/features/security-access/README.md)
