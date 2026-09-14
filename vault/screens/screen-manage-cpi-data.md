---
title: "Manage CPI Data"
tags: [screen, administration,reference-data,accounting]
evidence: Observed
---

`/en/admin/ManageCPIData.jsp`

![3,683 rows of one index series, ending in 2019. Notice the Published Date column: every row reads 12/06/2019.](../assets/screenshots/bbw-admin/26-manage-cpi-data.jpg)
`docs/assets/screenshots/bbw-admin/26-manage-cpi-data.jpg` · `af-admin/27-manage-cpi-data.jpg`

**The only populated reference-data table of the five.** One index, `BLS_CWUR0000SA0`, years **1932 to
2019**.

**The grid is identical in both tenants to five decimal places** — same series, same 3,683 rows — so
it is **platform-seeded [[hub-and-spoke|Hub]] data**, not tenant data. *(Derived.)*

**The series stops in 2019.** Any [[ExpenseEscalation|escalation clause]] indexed past then has nothing
to read.

One unexplained detail: 2019 rows show months `3`, `2`, `1` **and `0`**. *(Inferred: an annual or
average row.)*

See [[EscalationIndex]] · [[feature-reference-data]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
