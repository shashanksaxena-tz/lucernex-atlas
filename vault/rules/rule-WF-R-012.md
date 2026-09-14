---
title: "WF-R-012 — Custom JavaScript is the only conditional logic"
tags: [rule, workflow]
evidence: Observed
---

**`WF-R-012`** · [[module-workflow]] · **Observed**

`IsEnabledLxJSCode` on a [[WorkFlowTemplateStepAction|step action]] is described as **the engine's
only conditional-logic mechanism**.

**That may understate it** — `Conditional Workflow JS` exists on the template too, and neither has
been read ([[q-bbw-06-conditional-workflow-js]]).

Either way: the branching in this engine is a human's button choice plus an escape hatch into raw JS.

See [[rules-workflow]] for the full register.
