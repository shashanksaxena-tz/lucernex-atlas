---
title: The foreign-key graph under-counts by about 9%
tags: [finding, data-model]
evidence: Observed
---

The [[foreign-key-graph]] (972 edges) is built by matching column **types** — a column counts as a
foreign key when its declared type names a target object. **That rule misses columns *named* like a
key but *typed* as a scalar.**

| | |
|---|---:|
| Columns named `*ID` with a typed object FK | 864 |
| Columns named `*ID` but scalar-typed | 523 |
| …of those, matching a real object name | 237 |
| …less the table's own primary key | **−150** |
| **True missed edges** | **87** |
| Source tables affected | 60 |
| Target objects under-counted | 30 |
| **Under-count against 972** | **~9%** |

The hidden types are not only `Text` (59) — also `Number` (13), `Part` (5), `Parts Package` (3),
`Currency` (2), `Holiday Calendar` (2), `Contact` (2), `Entity` (1). The pattern is *"named like a
foreign key, typed as something that is not a reference"*.

**The under-counted targets are central, not peripheral:** [[Issue]] by 13, [[Firm]] by 12,
**[[ProjectEntity]] by 9**, then `BudgetLineItem` 5, `Part` 5, `BudgetColumn` 4, [[Person]] 4.

> **For the rebuild: a model derived from declared column types rather than naming convention silently
> loses 87 relationships.**

The `Punch List` family is the extreme case — all three children reference their parent through a
`Text`-typed `PunchListID`, so the family renders as **four disconnected tables**. That artefact is
what made the pattern visible at all.

**The spine classification survives, with one exception** — [[AssetHistory]], flagged and not changed.

*Computed over a global-only capture, so **87 is itself a lower bound**.* See also
[[soft-reference]].
