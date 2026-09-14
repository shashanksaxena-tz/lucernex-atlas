---
title: The Task step is offered everywhere and used nowhere
tags: [finding, workflow]
evidence: Observed
---

**Two step types exist**, named in the product's own code: every template row carries
`edit | delete | add task step | add form step`, and the task link builds a URL with a literal
`&StepType=Task` parameter.

**Across two tenants, 13 templates and 62 steps, the `Type` column reads `Form`. Every time.** Zero of
19 steps at [[tenant-american-freight|AF]], zero of 62 at [[tenant-bbw|BBW]].

**And the explanation is in the inventory:** BBW has **`TaskTemplate = 0`** — no task templates at all.
There are no Task steps because there is nothing for one to point at.

So the vocabulary is settled and **the behaviour of a Task step is completely unobserved**. The
likeliest reading (*Inferred*) is that ASG's configuration simply does not use them.

**That is decision-relevant in itself: the rebuild may not need the concept, and somebody should
confirm that with the business rather than build it on spec.**

Observing one would require **creating** a Task step, which is a write and out of scope under the
read-only rule — [[q-bbw-03-task-step]].

Not to be confused with the [[Task]] record type, a different thing entirely — and one of
[[TaskGroup|three byte-identical tables]].

See [[workflow-step]]
