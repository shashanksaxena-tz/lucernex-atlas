---
title: Subtype roots — the nine things that can be a root
tags: [concept, data-model, core]
evidence: Observed
---

Nine objects carry [[ProjectEntity]]'s 8-column block and so are **subtype roots** — the only record
types that can own other records and appear as a top-level navigation root.

| Object | Fields | Renders as a root? |
|---|---:|---|
| [[Contract]] | 570 | yes — and as `Equipment Contract` too, see [[equipment-contract]] |
| [[Program]] | 180 | yes, **labelled `Portfolio`** — see below |
| [[Parcel]] | 154 | no in either tenant |
| [[Location]] | 141 | yes |
| [[Facility]] | 133 | yes |
| [[Prototype]] | 113 | no |
| [[Project]] | 111 | no |
| [[PotentialProject]] | 108 | no — this is "Site" |
| `BudgetOptionTemplate` | 107 | **false positive**, no physical table |

**The `Program` / `Portfolio` trap.** The root labelled `Portfolio` carries
`requestedProjectEntityType=Program`. There is *also* a separate menu structure genuinely named
`Program` (id `3851`), and it renders in neither tenant, because no row anywhere is typed
`ProjectEntityTypeName = "Program"` — the `Program` table's rows are typed `"Portfolio"`. Reading the
**table** name as the **type** name is exactly what made `Program` look like an unexplained anomaly
and destroyed an earlier three-gate model. See [[finding-root-renders-iff-record-exists]].

The discriminator lives on the row, not the table: an equipment lease is a [[Contract]] row with
`ProjectEntityTypeName = 'Equipment Contract'`.

Source: [`data-model/project-entity.md`](../../docs/data-model/project-entity.md) ·
[`data-model/screen-routing.md`](../../docs/data-model/screen-routing.md)
