---
title: "WF-R-062 — Closing a workflow"
tags: [rule, workflow]
evidence: Observed
---

**`WF-R-062`** · [[module-workflow]] · **Observed**

`CloseWorkFlow` sets `IsCompleted`, `ClosedDate` and a terminal status, and fires **three template
notify flags** — notify the initiator, notify all prior assignees, notify all prior approvers.

All three read `No` on the template that was inspected. See [[WorkFlow]] · [[WorkFlowTemplate]].

See [[rules-workflow]] for the full register.
