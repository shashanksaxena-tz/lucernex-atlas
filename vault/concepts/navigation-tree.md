---
title: The navigation tree
tags: [concept, navigation, core]
evidence: Observed
---

The whole end-user surface is a three-level tree — **root → group → screen** — read out of the
`Lx.ui.MenuTree` ExtJS component.

| Root | Groups | Screens |
|---|---:|---:|
| Portfolio (= [[Program]]) | 6 | 14 |
| [[Location]] | 4 | 12 |
| [[Facility]] | 7 | 17 |
| [[Contract]] | 6 | 39 |
| **[[equipment-contract\|Equipment Contract]]** *(BBW only)* | **5** | **26** |

[[tenant-american-freight|American Freight]]: 4 roots, 109 nodes. [[tenant-bbw|BBW]]: 5 roots, 141
nodes. Over the four shared roots a name-for-name set difference returns **empty in both directions**
— not one group or screen differs, and **109 of 109 nodes carry the same numeric `PageLayoutID`**.
The end-user surface is platform-defined, not firm-configured; see [[finding-platform-seeded-by-id]].

Every root opens with the same six: `Summary · Members/Contacts · Forms · Work Flow · Documents ·
Binders`.

Three things the tree does not tell you:

- **It is not the whole product.** `Lx.ui.MenuTree` carries only the end-user menu; the
  [[feature-administration|57 administration tools]] are a separate surface entirely, and **14 menu
  structures with 892 nodes** exist against the 4–5 that render.
- **Record creation is not in it.** The tree is navigation *within* a record that already exists.
  Creation is a [[screen-contract-wizard|five-step sub-page wizard]].
- **A route is not an addressable URL.** See [[finding-routes-are-not-addressable]].

Which roots render is decided by [[finding-root-renders-iff-record-exists]].

Source: [`screens/003-main-navigation.md`](../../docs/screens/003-main-navigation.md) ·
[`data-model/screen-routing.md`](../../docs/data-model/screen-routing.md)
