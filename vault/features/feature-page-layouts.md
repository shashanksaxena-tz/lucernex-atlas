---
title: Page layouts
tags: [feature, layouts, core]
evidence: Observed
---

The composition engine everything renders from. Start at [[page-layout-concept]].

Concepts: [[layout-modes]] · [[layout-chain]] · [[action-buttons]] · [[conditional-field]]
Entities: [[PageLayout]] · [[PageLayoutField]] · [[PageLayoutFilter]]

What the feature settles:

- **93 layouts is not the total — it is 135.** 42 form layouts are reachable only through Issue Types
  ([[finding-form-layouts-are-hidden]]).
- **Navigation ids and layout ids share zero values** but are one table in two tiers, joined by
  `ParentPageLayoutID`. BBW nav runs 924–108,382; BBW layouts 98,858–102,775.
- **[[finding-publish-then-fork]]** — 80 layouts shared by `(mode, name)`, **0** by id, 0 primary-table
  mismatches, offsets clustered `+2626…+2677` on 58 of 80.
- Of the 19 unshared layouts: **3 real divergence, 2 renames, 5 scratch rows** (`test`, `TABLE`,
  `zdelete`).
- **SUB layouts render as titled sections** and are reused across pages; **action buttons render in a
  right-hand rail and are per-layout** — 13 on a contract Summary, 4 on its Abstract Details, same
  record.
- **[[finding-no-layout-level-required]]** and **[[finding-layouts-over-projections]]**.

Screens: [[screen-manage-page-layouts]] · [[screen-layout-changes]] ·
[[screen-contract-summary]] · [[screen-contract-abstract-details]]

[`features/page-layouts/`](../../docs/features/page-layouts/README.md)
