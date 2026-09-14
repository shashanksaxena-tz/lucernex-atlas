---
title: "Manage Milestone Timeline"
tags: [screen, administration,projects,configuration]
evidence: Observed
---

`/en/admin/ProcessTimelineEdit.jsp`

![Milestone timeline templates — also zero rows.](../assets/screenshots/bbw-admin/03-manage-milestone-timeline.jpg)
`docs/assets/screenshots/bbw-admin/03-manage-milestone-timeline.jpg` · `af-admin/04-manage-milestone-timeline.jpg`

**`ProcessTimelineTemplate` = 0** at [[tenant-bbw|BBW]], alongside
[[screen-manage-schedule-templates|`TaskTemplate` = 0]].

`ProcessTimeline` is **31 fields** and omits `ParentTaskID`, `TskPredVal_PredecessorTaskID`,
`OnCriticalPath`, `IsTaskGroup` and all three resource fields — so it produces **a flat milestone list,
not a schedule network** ([[rule-PRJ-R-002]]).

Two scheduling mechanisms, neither configured. Consistent with
[[module-projects-capital|projects and capital being out of scope]] by the BRDs' own architecture.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
