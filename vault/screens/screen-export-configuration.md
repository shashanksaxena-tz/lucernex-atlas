---
title: "Export Configuration"
tags: [screen, administration,import-export,tenancy]
evidence: Observed
---

`/en/admin/MessengerExportData.jsp`

![The clone checkbox, and its warning text. This is the publish-and-fork model, named by the product itself.](../../docs/assets/screenshots/bbw-admin/14-export-configuration.jpg)
`docs/assets/screenshots/bbw-admin/14-export-configuration.jpg` · `af-admin/15-export-configuration.jpg`

**Not a data export — a *configuration* export**, tabbed by exactly the sub-systems the layout
inventory enumerated: Summary Pages / Sub Pages / List Pages / Forms / Reports / Templates / Others.
The Summary Pages tab reads *"Displaying 1 - 15 of 15"*, matching [[tenant-bbw|BBW]]'s 15 `SEP`
layouts precisely.

Above the grid sits the sentence that settles [[finding-publish-then-fork]]:

> ☐ **Clone these layouts in this firm and environment** (new layouts/fields created when this xml is
> imported)
> *Do not check this if you are moving layouts, forms,… from one environment to another or one firm to
> another (e.g. dev to iwms)*

**Two modes, named.** Clone checked ⇒ new ids. Clone unchecked ⇒ identity preserved. ASG used the
first, which is why the two tenants share 80 layout names and zero layout ids.

**The limitation to design around:** clone-on-import leaves the copy with **no pointer back to the
original**. See [[publish-and-fork]] · [[three-publish-tiers]].

It produces **XML**, and `POST /rest/firm` consumes XML — so configuration round-trips
([[finding-no-generic-export]]).

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
