# PLT-R-016 — `Project` and `ProjectEntity` are both live, unreconciled candidates for "the spine"

*Platform & Tenancy · Derived*

**Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity` and is the authority for the spine, but `Project`'s role remains genuinely open.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any decision about which object is the entity supertype |
| What it reads | Both objects are classified `subtype_root`-shaped by the same mechanical test; field counts (111 vs. 107) and Data-Fields leaf counts (6 vs. 170) disagree about which is "lightweight." |
| What it writes | Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity` and is the authority for the spine, but `Project`'s role remains genuinely open |

## What it constrains

[ProjectEntity](../entities/ProjectEntity.md), [Project](../entities/Project.md)

## Confidence

Derived — `object-catalog.md` open question 2, unresolved by this module's own pass

---

Source: `docs/modules/platform-tenancy/rules.md`
