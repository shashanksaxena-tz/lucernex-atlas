---
title: "PRJ-R-013 — The deal pipeline has no scheduling engine"
tags: [rule, projects-capital]
evidence: Observed
---

**`PRJ-R-013`** · [[module-projects-capital]] · **Observed**

[[RETransaction]] and [[Scenario]] deal schedules **reuse [[TaskGroup]] directly**. The pre-lease
pipeline borrows the capital-project scheduler rather than having one.

See [[rules-projects-capital]] for the full register.
