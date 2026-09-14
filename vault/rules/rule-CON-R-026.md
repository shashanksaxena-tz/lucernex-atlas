---
title: "CON-R-026 — Contract rollups can go stale silently"
tags: [rule, contracts]
evidence: Derived
---

**`CON-R-026`** · [[module-contracts]] · **Derived**

[[Contract]] carries **120 denormalised rollup fields** and — unlike [[SLSummary]] — has **no
`NeedsRecalculation` flag** ([[rule-ACC-R-020]]).

So the header can disagree with its children and nothing marks it. Any migration reading those 120
fields as truth is reading a cache.

See [[rules-contracts]] for the full register.
