---
title: PotentialProject
tags: [entity, portfolio, subtype-root, deal-pipeline]
evidence: Observed
---

**`potential_project` · 108 fields · [[module-portfolio-transactions]]**

A candidate site or deal before it becomes anything — the menu calls it **"Site"**. A
[[subtype-root]] that does not render as a navigation root.

Two absences make it strange:

- **Zero inbound foreign keys** anywhere in the 972-edge graph. Nothing points at it.
- **Zero rows** in the [[data-field-catalog|Manage Data Fields]] admin catalog — 108 raw schema fields,
  none admin-exposed.

So **no column traces a [[Facility]] or [[Location]] back to its originating site**
([[rule-POR-R-011]]). The pipeline that [[Program]]'s `SiteToProjectSetupLayoutID` names is not
reconstructible from the data afterwards.

It sits at the head of the pre-lease deal chain: PotentialProject → [[RETransaction]] → [[Scenario]],
which runs before any [[Contract]] exists.

See [`site-pipeline.md`](../../docs/modules/portfolio-transactions/site-pipeline.md)
