---
title: "WF-R-053 — RequireAllApprovers can deadlock with no recovery"
tags: [rule, workflow]
evidence: Observed
---

**`WF-R-053`** · [[module-workflow]] · **Observed**

> If approvers choose **different** actions on a step with `RequireAllApprovers`, **the step deadlocks
> and there is no recovery path.**

Both the rule and the failure are Observed. It is one of ten catalogued engine defects, and one of two
that are in the schema rather than in a configuration.

See [[WorkFlowStepApprover]] · [[rule-WF-R-057]].

See [[rules-workflow]] for the full register.
