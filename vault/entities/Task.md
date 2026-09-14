---
title: Task
tags: [entity, projects]
evidence: Derived
---

**`task` · 37 fields · [[module-projects-capital]]**

A schedule task, baseline versus actual — and **one of three byte-identical 37-field tables**, with
[[TaskGroup]] and [[TaskItem]].

**Every one of the 18 columns typed `Task/Group ID` across three modules resolves to [[TaskGroup]]
alone.** `Task` and `TaskItem` have **zero inbound edges** in the 972-edge graph
([[rule-PRJ-R-001]]). Three identical tables, one of which does all the work.

Not to be confused with the [[workflow-step|workflow `Task` step]], which is a different concept
entirely and has **never been observed** ([[finding-no-task-step-anywhere]]). `TaskTemplate = 0` in
[[tenant-bbw|BBW]].
