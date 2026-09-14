---
title: "WF-R-057 — Only one prior approval round is retained"
tags: [rule, workflow]
evidence: Observed
---

**`WF-R-057`** · [[module-workflow]] · **Observed**

**A third round overwrites the second.**

So a step that goes back and forth more than twice loses its own history — which matters for an audit
trail that is otherwise [[audit-trail|field-level and complete]].

*(Observed, plus Derived for the overwrite behaviour.)* See [[WorkFlowStepApprover]].

See [[rules-workflow]] for the full register.
