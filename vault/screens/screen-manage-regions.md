---
title: "Manage Regions / Org Chart"
tags: [screen, administration,people,platform]
evidence: Observed
---

`/en/admin/OrgChartEdit.jsp`

![The region hierarchy and reporting org chart.](../assets/screenshots/bbw-admin/30-manage-regions-org-chart.jpg)
`docs/assets/screenshots/bbw-admin/30-manage-regions-org-chart.jpg` · `af-admin/31-manage-regions-org-chart.jpg`

**This screen is the proof that [[Region]] is an export gap rather than a one-field table.** The
hierarchy plainly exists here; the schema export shows [[Region]] with **one declared field**, while
**12 objects reference it across 34 columns** ([[rule-PLT-R-009]], [[rule-PLT-R-014]]).

`Program.OrgChartProgramID` is the self-reference that nests portfolios.

**Careful:** `Market Area Code` (`TableType 2049`, 213 values — the second-largest
[[code-table|code table]] in the product) is a `MARKET` routing level and **not** a Region level.

It is also served as an end-user screen by the same file, `OrgChartEdit.jsp`
([[finding-two-files-serve-56-percent]]).

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
