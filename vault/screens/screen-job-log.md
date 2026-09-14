---
title: "Job Log"
tags: [screen, administration,import-export,diagnostics]
evidence: Observed
---

`/en/admin/JobLogEdit.jsp`

![818 entries — the first evidence anywhere in this corpus of the product actually running. The hourly rows are an external system posting transaction data.](../assets/screenshots/bbw-admin/15-job-log.jpg)
`docs/assets/screenshots/bbw-admin/15-job-log.jpg` · `af-admin/16-job-log.jpg`

**818 entries at [[tenant-bbw|BBW]].** Job types `Generate Payments`, `Data Import`,
`Scheduled Report`; statuses `Complete` / `Completed` / `Finished`.

Two things it proves:

1. **`Generate Payments` is logged as a user-triggered job** — corroborating
   [[finding-engine-is-button-driven]] from the other side.
2. **An hourly inbound HTTP integration is running.** `BBW Transaction Update` executes every hour on
   the half-hour, initiated by `Lx Administrator`, each with an `LxHttpMsg…` input and an
   `LxDataImportLog_…` output. **Nothing in the corpus recorded this** —
   [[q-bbw-19-hourly-integration]].

That second point makes [[finding-discount-rate-table-empty]] stranger, not easier: a tenant with live
operational traffic *and* an empty rate table is harder to explain than an idle one.

**`Job Log` and `Report Log` are the same screen** — both `JobLogEdit.jsp`. See
[[feature-administration]].

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
