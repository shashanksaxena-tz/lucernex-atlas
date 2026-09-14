---
title: WorkFlowTemplateStep
tags: [entity, workflow]
evidence: Observed
---

**`work_flow_template_step` · 55 fields · [[module-workflow]]**

One approval step in a [[WorkFlowTemplate]], keyed by an integer `StepNumber`, with **four parallel
routing lists per role**.

**The admin grid surfaces six of its 55 fields**, so roughly 90% of the step model has never been
observed. See [[workflow-step]].

It carries **two layout foreign keys** — `PageLayoutApproversID` and `PageLayoutAssigneesID` — which is
where the engine's real expressiveness lives: one layout per step *per role*, so an N-step workflow
carries N+1 layouts ([[rule-LAY-R-165]]).

20 of its fields are snapshotted into [[WorkFlowStep]] at instantiation; the other 35 are read live
([[rule-WF-R-013]]).

Every one of the 62 configured steps across both tenants is type `Form` —
[[finding-no-task-step-anywhere]].
