---
title: "Q-BBW-05 — What backs the EquipmentContract type?"
tags: [open-question, equipment, data-model]
evidence: Observed
status: open
---

**Answered in part.** [[equipment-contract|Equipment Contract]] has its own
`requestedProjectEntityType` — **`EquipmentContract`** — a distinct [[ProjectEntity]] type, not
[[Contract]] with a discriminator at the navigation layer. The four shared roots resolve to
[[Program]] / [[Location]] / [[Facility]] / [[Contract]], confirming
[[subtype-root|"Portfolio" is `Program`]].

**The follow-on is the real question.** The 223-object census contains **no `EquipmentContract`
object** — and neither does the 227-table picker, nor the 25 refused tables.

Meanwhile `GET /rest/businessObject/EquipmentContract` returns **2,017 links to the same `Contract`
records**, which reads as an alias or view; `EquipContract` returns 400.

**So either the census is incomplete, or the type maps onto `Contract` at the storage layer** — and
the second is much the more likely, since equipment contracts are demonstrably `Contract` rows
discriminated by `ProjectEntityTypeName = 'Equipment Contract'`.

### How to settle it

Resolve against a schema export. **There is no BBW equivalent of `_lucernex_objects_summary.txt`**, so
this cannot be settled from the navigation alone — see [[method-read-only-exploration]].
