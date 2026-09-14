---
title: "Company administration dashboard"
tags: [screen, administration]
evidence: Observed
---

`/en/dashboard/DashboardDispatchOld.jsp?dashboardName=admin`

![The admin landing page. Notice the route — *Old*. The end-user dashboard uses a different file entirely.](../../docs/assets/screenshots/dashboard/admin-company-administration.png)
`docs/assets/screenshots/dashboard/admin-company-administration.png`

**The administration surface is a separate world from the [[navigation-tree]]** — `Lx.ui.MenuTree`
carries only the end-user menu, which is why an `Administration` node kept appearing in layout
metadata and never in the 105-screen tree.

It lists **57 tools** at [[tenant-bbw|BBW]] and 63 at [[tenant-american-freight|AF]] — so visibility is
per-tenant or per-user-class, not fixed. The full classified inventory is [[feature-administration]].

Note the admin dashboard uses `DashboardDispatchOld.jsp` while the normal one uses
`DashboardDispatch.jsp`.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
