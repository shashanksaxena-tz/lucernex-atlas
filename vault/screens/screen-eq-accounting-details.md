---
title: "Equipment Contract — Accounting Details"
tags: [screen, end-user,equipment,accounting]
evidence: Observed
---

`EntityInfo.jsp — not deep-linkable`

> **[[caveat-one-equipment-contract]]**

![The accounting layer on an equipment lease — and this is the group that survives almost untouched. The entire ASC 842 / IFRS 16 / straight-line engine is here.](../assets/screenshots/bbw-enduser/eq-04-accounting-details.jpg)
`docs/assets/screenshots/bbw-enduser/eq-04-accounting-details.jpg`

**The most important screen in the [[equipment-contract]] module, because of what it does *not* drop.**

`Straight-Line Rent`, `Accounting Assumptions`, `ASC 842 Test`, `ASC 842 Rent Schedule`,
`IFRS 16 Rent Schedule` — all present. 6 of [[Contract]]'s 7 screens, with only
[[screen-contract-capital-lease-test|Capital Lease Test]] removed
([[q-bbw-02-capital-lease-test]]).

**This is [[finding-accounting-runs-per-asset]] rendered.** The schema-side evidence was three nullable
foreign keys to [[Asset]]; here the product exposes the same fact as a first-class navigation root with
its own 26 screens.

For ASG Edge+ that is a scoping constraint: an engine built as *"schedules hang off contracts"* cannot
take equipment leases, and the incumbent's own product line expects them.

See [[one-engine-three-standards]] · [[SLSummary]]

All screens: [[map-of-screens]] · caveats: [[caveat-viewport]] · [[caveat-one-equipment-contract]]
