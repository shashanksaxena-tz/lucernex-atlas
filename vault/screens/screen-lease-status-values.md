---
title: "Lease Status values"
tags: [screen, administration,contracts,reference-data]
evidence: Observed
---

`/en/admin/CustomCodeTableEdit.jsp — CustomCodeTableID 7727`

![The seven Lease Status values. Notice the order they render in: alphabetical. `SortOrder` is null on every row, so the real lifecycle sequence exists nowhere in the data.](../../docs/assets/screenshots/drop-downs/client-lease-status-values.jpg)
`docs/assets/screenshots/drop-downs/client-lease-status-values.jpg`

`Open` · `Possession` · `Possession - Paying Rent` · `Closed` · `Closed - Active` ·
`Future Possession` · `Accounting Purposes Only`

**This screen answers a question that was open for most of this corpus's life.** The platform's
`Contract Status Code` has three values and never matched BRD-24 — it does not have to, because
[[contract-lifecycle|ASG tracks the lifecycle in a field it defined itself]].

And it opens a new one: **[[finding-lifecycle-has-no-ordering]]**. A rebuild that models an ordered
state machine is making a decision, not migrating one — [[q-bbw-20-lease-status]].

Note the name collision: a *platform* `Lease Status Code` (`2043`) also exists, with exactly one value
(`Expired`). Different thing, same name. See [[client-drop-down]].

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
