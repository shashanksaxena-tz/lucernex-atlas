---
title: Workflow steps — Form and Task
tags: [concept, workflow]
evidence: Observed
---

Two step types exist, named in the product's own code: the task link builds a URL with a literal
`&StepType=Task` parameter, so `Task` and `Form` are the vocabulary.

**Across two tenants, 13 templates and 62 steps, every single step reads `Form`.** Not one `Task`
step has ever been observed. And [[tenant-bbw|BBW]] has **`TaskTemplate = 0`** — no task templates at
all, which explains it. See [[finding-no-task-step-anywhere]] and [[q-bbw-03-task-step]].

The step grid exposes six columns — `Step | Step Name | Form/Task | Type | Approval Level | Approver`
— against [[WorkFlowTemplateStep]]'s **55 physical fields**. About 90% of the step model is
unobserved.

- `Approval Level` takes only two values in practice: **`Member`** and **`Ad Hoc`**. The schema enum
  is `MemberNotifyType`; the UI relabels it and adds an unschema'd `Ad Hoc` ([[rule-WF-R-009]]).
- Where `Approval Level = Member`, the approver is **a list of named individuals**, not a role or a
  position. See [[finding-routing-is-to-named-people]]. Their identities are deliberately excluded
  from this vault — [[method-omitting-identities]].
- Each step binds **one layout per role** (`PageLayoutApproversID`, `PageLayoutAssigneesID`), so an
  N-step workflow carries N+1 layouts ([[rule-LAY-R-165]], [[rule-LAY-R-010a]]).

Two failure modes are in the schema: `RequireAllApprovers` **deadlocks with no recovery path** if
approvers choose different actions ([[rule-WF-R-053]]), and only one prior approval round is retained
— a third round overwrites the second ([[rule-WF-R-057]]).

Source: [`modules/workflow/step-actions.md`](../../docs/modules/workflow/step-actions.md) ·
[`features/workflows-forms/`](../../docs/features/workflows-forms/README.md)
