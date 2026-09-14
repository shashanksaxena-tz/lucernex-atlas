---
title: "PRJ-R-002 — ProcessTimeline is a flat milestone list"
tags: [rule, projects-capital]
evidence: Observed
---

**`PRJ-R-002`** · [[module-projects-capital]] · **Observed**

It omits `ParentTaskID`, `TskPredVal_PredecessorTaskID`, `OnCriticalPath`, `IsTaskGroup` and all three
resource fields.

**No hierarchy, no dependencies, no resources.** It is a milestone list, not a schedule network —
unlike [[TaskGroup]] ([[rule-PRJ-R-006]]).

See [[rules-projects-capital]] for the full register.
