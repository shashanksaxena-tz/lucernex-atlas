---
title: "WF-R-024 — Exactly 20 fields are copied at instantiation"
tags: [rule, workflow]
evidence: Derived
---

**`WF-R-024`** · [[module-workflow]] · **Derived**

**20** configuration fields are copied from [[WorkFlowTemplateStep]] to [[WorkFlowStep]] when a step
is instantiated. **35** stay template-only and **30** are instance-only.

*(Derived from field-level comparison, plus Observed field lists.)* The hazard this creates is
[[rule-WF-R-013]].

See [[rules-workflow]] for the full register.
