---
title: "WF-R-014 — Four kick-off methods, not three"
tags: [rule, workflow]
evidence: Observed
---

**`WF-R-014`** · [[module-workflow]] · **Observed**

`KickOffMethod: [STEP_ACTION, PAGE_LAYOUT, STATUS_CHANGE, TASK]`.

**The vendor's own help text names only three and omits `STATUS_CHANGE`** — so the documentation
under-describes the product. `TASK` is corroborated by `WorkFlow.KickOffTaskID` → [[TaskGroup]]
([[rule-PRJ-R-012]]).

Workflows also chain — [[q-bbw-07-workflow-kickoff-graph]].

See [[rules-workflow]] for the full register.
