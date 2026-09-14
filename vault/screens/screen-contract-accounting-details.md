---
title: "Contract — Accounting Details"
tags: [screen, end-user,contracts,accounting]
evidence: Observed
---

`PForm.jsp — Contract : Accounting Info : Accounting Details`

![The accounting assumptions on a real contract — the inputs the schedule generator reads.](../assets/screenshots/bbw-enduser/ct-27-accounting-details.jpg)
`docs/assets/screenshots/bbw-enduser/ct-27-accounting-details.jpg`

The `Accounting Info` group is the one that **survives almost intact** into
[[equipment-contract|Equipment Contract]] — 6 of 7 screens, with only `Capital Lease Test` dropped
([[q-bbw-02-capital-lease-test]]).

Changing a schedule type here sets [[SLSummary]]`.NeedsRecalculation` ([[rule-ACC-R-020]]) — the engine
**marks itself stale and waits** for someone to press a button.

Related: [[screen-contract-capital-lease-test]] · [[screen-asc842-rent-schedule]] ·
[[one-engine-three-standards]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
