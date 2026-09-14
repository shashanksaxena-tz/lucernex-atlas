---
title: "Report Log"
tags: [screen, administration,diagnostics,reporting]
evidence: Observed
---

`/en/admin/JobLogEdit.jsp`

![The report log — and note the route.](../assets/screenshots/bbw-admin/49-report-log.jpg)
`docs/assets/screenshots/bbw-admin/49-report-log.jpg` · `af-admin/55-report-log.jpg`

**`Report Log` and [[screen-job-log|`Job Log`]] are the same screen** — both `JobLogEdit.jsp`. Two
entries on the admin dashboard, one file.

Which matters because [[module-reporting]] records that **there is no report run-history table**:
[[PageLayout]] keeps a single most-recent `LastRunBy` / `LastRunDate` stamp. Whatever history exists is
here, in the job log, not on the report.

`Scheduled Report` appears as a job type among the 818 entries.

See [[feature-administration]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
