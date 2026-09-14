---
title: "WF-R-010a — One layout per step per role"
tags: [rule, workflow]
evidence: Observed
---

**`WF-R-010a`** · [[module-workflow]] · **Observed**

Each [[WorkFlowTemplateStep|step]] binds **one layout per role** — `PageLayoutApproversID` and
`PageLayoutAssigneesID` — and a [[form-vs-page|Form type]] owns many layouts.

This is where the engine's real expressiveness lives: not in branching logic, but in showing a
different form to a different role at a different step.

See [[rules-workflow]] for the full register.
