---
title: "Manage Dashboard Reports"
tags: [screen, administration,reporting]
evidence: Observed
---

`/en/reports/ManageDashboardModules.jsp`

![Dashboard tile administration.](../assets/screenshots/bbw-admin/11-manage-dashboard-reports.jpg)
`docs/assets/screenshots/bbw-admin/11-manage-dashboard-reports.jpg` · `af-admin/12-manage-dashboard-reports.jpg`

Dashboard tiles are [[PageLayout]] rows like everything else ([[rule-LAY-R-101]]).

**And they are secured by title string, not by record id** — so **renaming a tile breaks its grants**
([[rule-RPT-R-051]]). The same defect shape as
[[finding-rules-store-labels-not-ids|conditional rules storing labels]], in a second unrelated
subsystem — which suggests a house style rather than an oversight. **Design both out.**

Nine dashboard admin tools are catalogued in
[`modules/reporting/admin-tools.md`](../../docs/modules/reporting/admin-tools.md), with ASG's
required/reviewed decision for each.

See [[module-reporting]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
