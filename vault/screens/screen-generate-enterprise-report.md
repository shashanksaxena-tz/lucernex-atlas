---
title: "Generate Enterprise Report File"
tags: [screen, administration,reporting,import-export]
evidence: Observed
---

`/en/admin/GenBaseReport.jsp`

![Enterprise report file generation.](../assets/screenshots/bbw-admin/53-generate-enterprise-report-file.jpg)
`docs/assets/screenshots/bbw-admin/53-generate-enterprise-report-file.jpg` · `af-admin/62-generate-enterprise-report-file.jpg`

One of the few bulk-out paths in a product with
[[finding-no-generic-export|no generic bulk export endpoint]].

Relevant to an unmet ASG requirement: a **report-to-import round trip** ([[rule-RPT-R-063]]). Lx
exports field *metadata* and has no report-data equivalent, and GraphQL carries no report type at all —
so **reports are a hand rebuild**, not a migration.

See [[module-reporting]] · [[feature-import-export]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
