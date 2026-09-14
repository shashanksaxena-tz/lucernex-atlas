---
title: "Manage Company"
tags: [screen, administration,tenancy]
evidence: Observed
---

`/en/admin/FirmEdit.jsp?FirmID={id}`

![The tenant record. The "Allow X?" flags in here gate 13 of the 14 menu structures — and famously fail to gate the fourteenth.](../assets/screenshots/bbw-admin/01-manage-company.jpg)
`docs/assets/screenshots/bbw-admin/01-manage-company.jpg` · `af-admin/02-manage-company.jpg`

The [[Firm]] record — **71 fields** as rendered, 18 in the object census.

Two things it carries that matter far beyond this screen: **per-entity-type default layout
assignments**, and the **"Allow X?" entitlement flags** including `Allow Equipment Contracts?` and
`Allow AI Lease Abstraction`.

**The negative result from this screen is the useful one.** At [[tenant-american-freight|AF]],
`Allow Equipment Contracts?` reads **Yes** and the root still does not render — which eliminated the
obvious gate and eventually produced [[finding-root-renders-iff-record-exists]].

Also: there is **no `Equipment Contract Setup Page` field anywhere on this page**, so the object
catalog's description of [[Firm]] holding per-module setup-page assignments is schema-derived and not
exposed here.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
