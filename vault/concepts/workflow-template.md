---
title: Workflow template and instance
tags: [concept, workflow, core]
evidence: Observed
---

A step-numbered, template-instantiated **approval router** — not a general-purpose BPM engine. A
[[WorkFlowTemplate]] owns ordered [[WorkFlowTemplateStep]] rows keyed by an integer `StepNumber`, and
each step publishes [[WorkFlowTemplateStepAction]] buttons that are declarative bundles of booleans.
**The branching predicate is the human's choice of button.**

Template and instance live in the *same* tables, distinguished by self-reference
(`WorkFlow.WorkFlowTemplateID`, `WorkFlowStep.WorkFlowTemplateStepID`). Correspondence is
**20 copied, 35 template-only, 30 instance-only** fields — and the split is a hazard: the 35
template-only fields are **read live and change running instances**, while the 20 snapshotted ones do
not ([[rule-WF-R-013]], [[rule-WF-R-024]]).

Four kick-off methods, not three: `STEP_ACTION`, `PAGE_LAYOUT`, `STATUS_CHANGE`, `TASK` — the vendor's
own help text omits `STATUS_CHANGE` ([[rule-WF-R-014]]). And workflows **chain**: one template is
kicked off by another, which the corpus did not record until [[tenant-bbw|BBW]]
([[q-bbw-07-workflow-kickoff-graph]]).

**Versioning is a naming convention, not a feature.** The current template is the unsuffixed one;
`v1` and `v2` are archived predecessors, and the archival fact is **free text in the description
field** ("Workflow has been archived and replaced on 09.22.25") — not a status, not an effective-date
range, not a supersession key. See [[finding-workflow-versioning-is-naming]].

What the engine cannot do is as important as what it can: no conditional branching, no quorum, no
delegation, no parallel branches, no timer-driven state change, **no mechanism for passing field
values between steps** ([[rule-LAY-R-166e]]).

Source: [`modules/workflow/template-vs-instance.md`](../../docs/modules/workflow/template-vs-instance.md)
