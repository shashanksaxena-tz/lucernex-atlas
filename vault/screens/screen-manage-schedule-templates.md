---
title: "Manage Schedule Templates"
tags: [screen, administration,projects,configuration]
evidence: Observed
---

`/en/admin/TaskTemplateEdit.jsp`

![Task templates — and the count on this screen explains an absence elsewhere.](../assets/screenshots/bbw-admin/02-manage-schedule-templates.jpg)
`docs/assets/screenshots/bbw-admin/02-manage-schedule-templates.jpg` · `af-admin/03-manage-schedule-templates.jpg`

**`TaskTemplate` = 0 at [[tenant-bbw|BBW]].**

That single zero — read from the [[method-bulk-json-endpoint|bulk JSON endpoint]], not from the
picture — is what explains [[finding-no-task-step-anywhere]]. **There are no Task steps in any
workflow because there is nothing for one to point at.**

The scheduling machinery behind it is [[TaskGroup]], which carries
[[rule-PRJ-R-006|two separate graphs over the same rows]] — a WBS hierarchy and a CPM dependency
network.

See [[module-projects-capital]] · [[q-bbw-03-task-step]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
