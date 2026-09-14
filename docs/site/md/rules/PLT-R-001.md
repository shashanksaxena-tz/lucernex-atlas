# PLT-R-001 — Tenant isolation is one join deep

*Platform & Tenancy · Derived*

**The record is one of the 161 `entity_scoped` objects (not `ProjectEntity` itself or one of its 9 subtype roots).**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any tenant-scoped read or write |
| What it reads | `ProjectEntityID` on the record; `FirmID` on the `ProjectEntity` row it points at |
| The test | The record is one of the 161 `entity_scoped` objects (not `ProjectEntity` itself or one of its 9 subtype roots) |
| What it writes | The record carries no `FirmID` of its own. Tenant scoping must be enforced by joining to `ProjectEntity` and filtering on its `FirmID`, or not at all |

## What it constrains

[ProjectEntity](../entities/ProjectEntity.md)

## Confidence

Derived — exhaustive field-list check, `../../data-model/project-entity.md` §4

---

Source: `docs/modules/platform-tenancy/rules.md`
