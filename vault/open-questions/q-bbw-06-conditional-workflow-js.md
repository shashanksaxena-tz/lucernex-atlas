---
title: "Q-BBW-06 — What is Conditional Workflow JS?"
tags: [open-question, workflow, rules]
evidence: Observed
status: open
---

[[WorkFlowTemplate]] carries a field named **`Conditional Workflow JS`**.

That implies **workflow-level conditional logic held as raw JavaScript** — a second and completely
separate rule mechanism from the field-level [[conditional-field|`conditionalFieldsConfig`]], and it is
**documented nowhere in this corpus**.

It is one of **two JavaScript escape hatches**, and neither has ever been read:

| Hatch | Where | Note |
|---|---|---|
| `IsEnabledLxJSCode` | [[WorkFlowTemplateStepAction\|step action]] | [[rule-WF-R-012]] calls it **the engine's only conditional-logic mechanism** |
| `Conditional Workflow JS` | [[WorkFlowTemplate\|template]] | this question |

If both exist, [[rule-WF-R-012]] is understating the surface — and a rebuild that reproduces the
[[workflow-template|declarative router]] without them reproduces a different product.

### How to settle it

Open a template that populates it. `ASC 842 Tracking` (2475) or `Cotenancy Update` (2478) are the
likeliest candidates — both are small, recent and non-standard.
