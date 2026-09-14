---
title: AssetHistory
tags: [entity, assets]
evidence: Observed
---

**`asset_history` · 13 fields · [[module-assets-equipment]]**

A point-in-time snapshot of an [[Asset]]'s financial state before recalculation. The module's **only
internal FK edge**.

It is also the [[entity-spine]]'s one **false negative**: it carries `ProjectEntityID` typed soft
`Entity` rather than hard `Entity ID`, so it classes `firm_global` when it plausibly should be
`entity_scoped`.

The corpus **flagged it and did not change it**, and the reason is worth keeping: it is a snapshot of
an Asset, so whether it is scoped to the entity or to the asset is a **data-model judgement**, not
something a column type settles.
