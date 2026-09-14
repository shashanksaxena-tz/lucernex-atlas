---
title: "A contract, as a user sees it"
tags: [screen, end-user,contracts,layouts]
evidence: Observed
---

`PForm.jsp?menuPLID=3494&requestedProjectEntityType=Contract`

![The rendered contract summary. Two status fields side by side, a layout picker at the top, eleven action buttons in the right-hand rail — and "Term Length" written out as prose.](../assets/screenshots/end-user/contract-summary-rendered.jpg)
`docs/assets/screenshots/end-user/contract-summary-rendered.jpg`

Contract `86383`, layout `ASG Contract Summary` (`PageLayoutID=96289`). **One of the first captures of
the product as a user actually meets it**, and it changed several things.

- **`Contract Status = Active` and `Lease Status = Active` render side by side**, two different
  vocabularies — and **the record's breadcrumb header ends with the `Lease Status`**. See
  [[contract-lifecycle]].
- **A layout picker offers `ASG Contract Summary` and `ASG Lease Logs`** — so the
  [[layout-chain|ordered chain]] renders as a dropdown, and layout choice is a **runtime user
  decision**.
- **Eleven [[action-buttons|action buttons]]** plus a `Deactivate` at the foot. `Generate Rent` and
  `Calculate Schedule` are among them — [[finding-engine-is-button-driven]].
- **`Term Length` reads "5 years 16 days"** — prose, computed at paint time, not stored
  ([[finding-computed-fields-render-as-prose]]).
- SUB layouts render as **titled sections** and are reused across pages ([[rule-LAY-R-110]]).

Related: [[screen-contract-abstract-details]] · [[screen-asc842-rent-schedule]] · [[Contract]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
