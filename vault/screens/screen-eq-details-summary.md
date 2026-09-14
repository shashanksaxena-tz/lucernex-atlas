---
title: "Equipment Contract — Details : Summary"
tags: [screen, end-user,equipment]
evidence: Observed
---

`EntityInfo.jsp — not deep-linkable`

> **[[caveat-one-equipment-contract]]** — BBW holds exactly one equipment contract. This shows one
> record's population, not the module's range.

![The one equipment contract in the tenant. Contract Status reads "Active", and — the point of this capture — neither it nor Location is marked required.](../assets/screenshots/bbw-enduser/eq-01-details-summary.jpg)
`docs/assets/screenshots/bbw-enduser/eq-01-details-summary.jpg`

`ASG Equipment Contract`, lxID 507018, `Contract ID ASG1234`, commence `01/09/2026`, expire
`30/09/2031`, one asset (`Tractor`, asset group `ASG`).

**This screen closed a question.** `docs/admin/008` reported `Contract Status` and `Location` painted
red in the layout builder, when neither is schema-required on [[Contract]] — the one piece of evidence
against [[finding-no-layout-level-required]]. **Here they render, and neither is marked required.** The
builder's red text is an **editor affordance that does not reach the end user.**

The Actions panel: `Edit`, `Add Equipment`, `Audit Log`, **`Generate Payments`**,
**`Approve Payments`**, `Extend Contracts`, `Extend Asset P…`, `Save to Document`, `Link` — the
placeable, securable verbs of [[action-buttons]].

**And the route is the other finding.** [[finding-routes-are-not-addressable|None of Equipment
Contract's 32 nodes is deep-linkable]]; group nodes redirect to their first leaf.

See [[equipment-contract]] · [[Asset]]

All screens: [[map-of-screens]] · caveats: [[caveat-viewport]] · [[caveat-one-equipment-contract]]
