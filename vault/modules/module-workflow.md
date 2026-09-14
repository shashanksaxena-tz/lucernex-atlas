---
title: Workflow
tags: [module, workflow]
evidence: Observed
---

**rules `WF-R-001`…`WF-R-062`** plus seven suffixed additions — 69 defined in all.

A **step-numbered approval router**, not a BPM engine. See [[workflow-template]] and
[[workflow-step]].

Entities: [[WorkFlow]] · [[WorkFlowStep]] · [[WorkFlowStepApprover]] · [[WorkFlowTemplate]] ·
[[WorkFlowTemplateStep]] · [[WorkFlowTemplateStepAction]] · [[Issue]] · [[CodeIssueType]]

What it settles:

- **[[finding-form-workflow-not-1-1]]** — the 1:1 claim was an American Freight coincidence.
- **[[finding-no-task-step-anywhere]]** — 62 steps across two tenants, not one `Task`.
- **[[finding-routing-is-to-named-people]]** — routing resolves to lists of individuals.
- **[[finding-workflow-versioning-is-naming]]** — a name suffix and a sentence in a description field.

The most useful part of the module is its **23-row "rules that do not exist" table**: no conditional
branching, no quorum, no delegation, no parallel branches, no timer-driven state change, no template
versioning, and **no mechanism for passing field values between steps** ([[rule-LAY-R-166e]]). All
Derived by exhaustive field inspection — which is the only way to prove an absence.

Ten user-reported engine defects are catalogued, and two of them are in the schema:
[[rule-WF-R-053]] (deadlock) and [[rule-WF-R-057]] (lost approval round).

Rules: [[rules-workflow]] · [`modules/workflow/`](../../docs/modules/workflow/README.md)
