---
title: Page layout — the thing every screen is
tags: [concept, layouts, core]
evidence: Observed
---

Almost every screen in Lx is a **page layout**: a row in one table with a set of field placements
under it. Summary pages, sub-pages, list grids, forms, wizards, map popups, reports and dashboard
tiles are *all* `PageLayout` rows ([[rule-LAY-R-101]]).

- [[PageLayout]] — 17 columns recovered over REST, 42 columns in the vendor's own catalog. Booleans
  decide what kind of thing a layout is: `IsReport = true` makes it a report ([[rule-RPT-R-001]]);
  a non-null `CodeIssueTypeID` makes it a [[form-vs-page|form layout]].
- [[PageLayoutField]] — 20 columns, one row per placement. It carries the geometry as **three
  parallel coordinate sets** (`Edit*`, `View*`, `Header*`, with `-1` meaning "not placed") and a
  free-form `JSONConfigText` blob holding 29 distinct per-placement keys.
- [[PageLayoutFilter]] — run-mode filters. **Zero rows in BBW.** Built and unused.

Three things a rebuild must not get wrong:

1. There are three [[layout-modes]], and sub-pages are **composition units, not destinations**.
2. Several layouts on one navigation node form an ordered [[layout-chain]], not a set.
3. There is **no per-placement required flag** — see [[finding-no-layout-level-required]].

A layout does not have to sit over a table. Four of them target a [[virtual-projection]], which means
the layout engine must be able to render a read model ([[finding-layouts-over-projections]]).

`PageLayout` is **absent from the 223-object census** — the schema viewer refuses it — which is why
the reporting module's central claim rested on a table nobody could see until it was recovered over
[[rest-business-object|REST]].

Source: [`features/page-layouts/`](../../docs/features/page-layouts/README.md) ·
[`modules/layouts-and-forms/`](../../docs/modules/layouts-and-forms/README.md)
