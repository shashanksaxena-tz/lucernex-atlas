---
title: "WF-R-009 — Approval Level is a relabelled enum plus one"
tags: [rule, workflow]
evidence: Observed
---

**`WF-R-009`** · [[module-workflow]] · **Observed**

The schema enum is `MemberNotifyType`. **The live UI renders it "Approval Level" and adds an
unschema'd `Ad Hoc`.**

*(Both halves Observed; the mapping between them is Derived.)*

Only two values are ever seen in practice — `Member` and `Ad Hoc` — see [[workflow-step]].

See [[rules-workflow]] for the full register.
