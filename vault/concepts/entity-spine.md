---
title: The entity spine
tags: [concept, data-model, core]
evidence: Derived
---

Every ownable thing in Lx is a row in one universal supertype, [[ProjectEntity]] (107 fields), and
every other object relates to the spine in one of four ways. The classification covers all 223
objects with no remainder:

| Class | Objects | Fields | What it means |
|---|---:|---:|---|
| `supertype` | 1 | 107 | [[ProjectEntity]] itself |
| [[subtype-root]] | 9 | 1,617 | Carries the supertype's 8-column block, `ProjectEntityID` typed `Number` |
| `entity_scoped` | 161 | 4,644 | Carries a `ProjectEntityID` typed `Entity ID` — a hard FK to the spine |
| `firm_global` | 52 | 1,053 | Neither. Lives above the spine, scoped only by [[firm-tenancy|FirmID]] |

The shared 8-column block is `EntityId`, `ProjectEntityID`, `ProjectEntityName`,
**`ProjectEntityTypeName`**, `ClientEntityID`, `EntityEmail`, `EntityPhoto`,
`LinkProjectEntityContactListData`. `ProjectEntityTypeName` is the discriminator — and it is what
[[finding-root-renders-iff-record-exists|decides whether a navigation root renders at all]].

Two caveats worth carrying:

- `AssetHistory` is a **false negative** — it carries `ProjectEntityID` typed soft `Entity`, not hard
  `Entity ID`, so it classes `firm_global`. Whether it is scoped to the entity or to its [[Asset]] is
  a data-model judgement a column type cannot settle. Flagged, not changed.
- `BudgetOptionTemplate` is a **false positive** subtype root — it carries the block but has no
  physical table and keys on `BudgetTemplateID`. So there are **8 genuine subtypes**, not 9.

Of the 52 firm-global objects, 5 are out of scope, leaving **47 in-scope [[hub-and-spoke|Hub]]
candidates**.

Source: [`data-model/project-entity.md`](../../docs/data-model/project-entity.md) · see also
[[entity-scoped-vs-firm-global]], [[map-of-entities]]
