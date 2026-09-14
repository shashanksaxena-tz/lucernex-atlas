---
title: "Q-BBW-03 — What does a Task step actually do?"
tags: [open-question, workflow]
evidence: Observed
status: open
---

**Partly answered.** `Task` and `Form` are the two step types, named in the product's own code. But
across two tenants, 13 templates and **62 steps, zero are Task steps** — and
[[tenant-bbw|BBW]] has `TaskTemplate = 0`. See [[finding-no-task-step-anywhere]].

**So the real question is not "how does it work" but "does ASG use it at all?"**

### Why that reframing matters

**The rebuild may not need the concept.** Half the [[workflow-step|workflow step model]] is
unobserved, and building it on spec would be building something neither tenant has ever configured.

### How to settle it

**Ask the business first.** Observing one requires *creating* a Task step, which is a **write** and out
of scope under the read-only rule — [[method-read-only-exploration]].

Note this is unrelated to the [[Task]] record type, which is a different thing and is
[[TaskGroup|one of three byte-identical tables]].
