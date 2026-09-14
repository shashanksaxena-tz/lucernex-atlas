# PLT-R-003 — `ProjectEntityID` survives database-per-tenant; `FirmID` does not need to

*Platform & Tenancy · Derived*

**The target architecture is database-per-tenant (one Spoke database per firm).**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any migration of a `ProjectEntityID`-scoped record into a per-tenant Spoke database |
| What it reads | The record's `ProjectEntityID` |
| The test | The target architecture is database-per-tenant (one Spoke database per firm) |
| What it writes | `ProjectEntityID` must be retained — it is the intra-tenant partition and access-control unit (`LinkMemberProjectEntity`), not a tenant-scoping column being replaced. Only `FirmID`'s job (which physical database) is subsumed by the database boundary itself |

## What it constrains

[LinkMemberProjectEntity](../entities/LinkMemberProjectEntity.md)

## Confidence

Derived — `tenancy-model.md`, `project-entity.md` §5.3. ## Extensibility and configuration

---

Source: `docs/modules/platform-tenancy/rules.md`
