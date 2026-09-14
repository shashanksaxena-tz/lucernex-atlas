---
title: Action buttons are placeable, securable verbs
tags: [concept, layouts, security]
evidence: Observed
---

A [[page-layout-concept|layout]] does not only hold fields. It hosts **business-action buttons**, and
they are first-class configuration: placed on a layout like a field, and secured as one of the
**70 named verbs** on the Actions tab of [[security-ladder|Manage Security]].

On a rendered contract, the Actions panel holds **eleven** buttons plus a `Deactivate` at the foot. On
the [[screen-eq-details-summary|Equipment Contract summary]]: `Edit`, `Add Equipment`, `Audit Log`,
**`Generate Payments`**, **`Approve Payments`**, `Extend Contracts`, `Extend Asset P…`,
`Save to Document`, `Link`.

**They are per-layout, not per-record.** The same contract shows 13 action buttons on its Summary and
4 on its Abstract Details — because they are different layouts.

This is what makes [[finding-engine-is-button-driven|the accounting engine user-triggered]]:
`Generate Rent` and `Calculate Schedule` are buttons on one record, not scheduled jobs. `Generate
Payments` appears in the [[screen-job-log|Job Log]] as a user-initiated job, which is the confirming
evidence from the other side.

There is also a distinct *"(Run Report Action)"* button kind, so reports are launched from layouts
too.

Source: [`features/page-layouts/`](../../docs/features/page-layouts/README.md) ·
[`admin/008-manage-page-layouts.md`](../../docs/admin/008-manage-page-layouts.md)
