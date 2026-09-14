---
title: "Audit Reports"
tags: [screen, administration,security,diagnostics]
evidence: Observed
---

`/en/reports/AuditReport.jsp`

![Row-and-field-level audit with Old Value and New Value columns.](../assets/screenshots/bbw-admin/47-audit-reports.jpg)
`docs/assets/screenshots/bbw-admin/47-audit-reports.jpg` · `af-admin/53-audit-reports.jpg`

The surface over `AuditMaster` / `AuditTable` / `AuditColumn` — **synchronous, in-transaction,
field-level, with old and new values. No outbox.**

**This bears on a live ASG Edge+ decision**: ADR-0020 (in-transaction audit) versus ADR-0012 (the
outbox, still only a `NoOpOutboxPublisher`). The incumbent chose in-transaction. That is not an
argument for either, but it is evidence about what the behaviour looks like in production.

See [[audit-trail]] · [[rule-PLT-R-012]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
