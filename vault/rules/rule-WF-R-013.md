---
title: "WF-R-013 — 35 template fields change running instances"
tags: [rule, workflow]
evidence: Derived
---

**`WF-R-013`** · [[module-workflow]] · **Derived**

**20 fields are snapshotted** into [[WorkFlowStep]] at instantiation ([[rule-WF-R-024]]). **The other
35 are read live** — so editing a template **changes workflows already running**.

The module's stated hazard. A rebuild must decide deliberately which fields snapshot and which do
not, rather than inheriting a split nobody designed.

See [[rules-workflow]] for the full register.
