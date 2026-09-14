---
title: TaskItem
tags: [entity, projects]
evidence: Derived
---

**`task_item` · 37 fields · [[module-projects-capital]]**

The leaf row within a [[TaskGroup]] — and byte-identical to [[Task]] and `TaskGroup`, all three 37
fields with matching types.

**Zero inbound foreign keys.** Like [[Task]], nothing in the 972-edge graph points at it
([[rule-PRJ-R-001]]).

Three identical tables where one would do is the kind of thing a rebuild should decide about
deliberately rather than migrate faithfully.
