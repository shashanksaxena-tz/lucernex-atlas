---
title: WorkFlowTemplateStepAction
tags: [entity, workflow]
evidence: Observed
---

**`work_flow_template_step_action` · 37 fields · [[module-workflow]]**

The buttons a step publishes — Approve, Reject, Send Back — as **declarative bundles of booleans**.
This is what makes the engine a router rather than a rules engine: **the branching predicate is the
human's choice of button** ([[workflow-template]]).

The full 39-field action catalog and its eight-category taxonomy are documented and **entirely
unobserved in the UI** — nobody has opened one.

`IsEnabledLxJSCode` is one of the two JavaScript escape hatches in the product, and
[[rule-WF-R-012]] calls it **the engine's only conditional-logic mechanism**. The other is
`Conditional Workflow JS` on the template ([[q-bbw-06-conditional-workflow-js]]). Neither has been
read.

See [`step-actions.md`](../../docs/modules/workflow/step-actions.md)
