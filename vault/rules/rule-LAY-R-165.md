---
title: "LAY-R-165 — An N-step workflow carries N+1 layouts"
tags: [rule, layouts-and-forms]
evidence: Observed
---

**`LAY-R-165`** · [[module-layouts-and-forms]] · **Observed**

Workflow binds layouts at **two levels**: one kick-off form, plus approver and assignee layouts per
step. So an N-step workflow carries **N+1** layouts.

Which is most of why [[finding-form-layouts-are-hidden|42 form layouts exist outside the registry]]:
13 templates and 62 steps generate a lot of layouts nobody counted.

See [[rule-WF-R-010a]].

See [[rules-layouts-and-forms]] for the full register.
