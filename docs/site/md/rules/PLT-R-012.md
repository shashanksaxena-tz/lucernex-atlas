# PLT-R-012 — Two unreconciled audit mechanisms coexist

*Platform & Tenancy · Derived*

**162 of 223 objects carry the inline stamps (161 `ModifiedByID`, only 79 `CreatedByID`); it is unknown which objects also emit `AuditColumn` rows.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any change to a tracked field |
| What it reads | `AuditColumn`/`AuditTable` (explicit change log, keyed to the field-registry tree via `GroupID`/`SubGroupID`) and inline `CreatedByID`/`ModifiedByID` stamps present on most objects |
| The test | 162 of 223 objects carry the inline stamps (161 `ModifiedByID`, only 79 `CreatedByID`); it is unknown which objects also emit `AuditColumn` rows |
| What it writes | A rebuild inherits the same open question ASG Edge+'s own unresolved ADR-0020 (in-transaction audit vs. the ADR-0012 outbox) poses — Lx appears to run a version of both, unreconciled |

## What it constrains

[AuditColumn](../entities/AuditColumn.md), [AuditTable](../entities/AuditTable.md)

## Confidence

Derived — `../../data-model/object-catalog.md` open question 4

---

Source: `docs/modules/platform-tenancy/rules.md`
