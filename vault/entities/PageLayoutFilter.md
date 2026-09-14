---
title: PageLayoutFilter
tags: [entity, layouts, reporting]
evidence: Observed
---

**layouts-forms-reporting** — a valid [[rest-business-object|REST]] type with **zero rows in BBW**.
Genuinely empty, not inferred: the table's columns could not be recovered at all because there was
nothing to serialise.

It is the **run-mode filter** store, and also the *grouping* store — the same row that filters also
groups (`RowOrderBy` / `ColumnOrderBy`), which is why reporting in this product is **pivot-shaped,
not flat-list** ([[rule-RPT-R-023]]).

**It is not the [[conditional-field]] store.** Those are JSON blobs on [[PageLayoutField]]
([[rule-RPT-R-020]]). Confusing the two is easy and would produce a wrong rebuild of both features.

So layout-level run-mode filtering is **built and entirely unused** — see
[[feature-search-filtering]].
