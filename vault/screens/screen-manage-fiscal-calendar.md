---
title: "Manage Fiscal Calendar"
tags: [screen, administration,reference-data,accounting]
evidence: Observed
---

`/en/admin/ManageFiscalPeriod.jsp`

![Nine defined years, 2022–2030, twelve monthly periods each. The capability on offer is much larger than what is configured — and note the dates render DD/MM/YYYY on a US tenant.](../assets/screenshots/bbw-admin/31-manage-fiscal-calendar.jpg)
`docs/assets/screenshots/bbw-admin/31-manage-fiscal-calendar.jpg` · `af-admin/32-manage-fiscal-calendar.jpg`

**[[fiscal-period|A fiscal period is not a calendar month]].** The screen supports **4-4-5 quarters**
and **13 period slots** with per-period week counts, allowing a 53-week retail year.

**And it extrapolates.** The screen states: *"Computed calendar years will be used for date ranges not
defined below (based on last defined Fiscal Year)."* Ask for a date outside the range and you get an
answer, computed — not an error.

At [[tenant-bbw|BBW]] the nine defined years are plain calendar years with twelve monthly periods, so
the capability is configured off. **The capability being present and unused is the point**: a rebuild
that hard-codes calendar months cannot express a retail client's year.

[[Program]] carries the fiscal-year policy that resolves against this ([[rule-POR-R-001]]).

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
