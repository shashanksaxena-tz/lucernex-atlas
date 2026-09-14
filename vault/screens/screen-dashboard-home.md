---
title: "Dashboard home"
tags: [screen, end-user]
evidence: Observed
---

`/en/dashboard/DashboardDispatch.jsp`

![The help menu open over an empty dashboard canvas. The build string in the footer is what dated every capture in this corpus.](../../docs/assets/screenshots/dashboard/dashboard-home-help-menu.png)
`docs/assets/screenshots/dashboard/dashboard-home-help-menu.png`

[[tenant-american-freight|American Freight]], build `26.08.0.39`, captured 2026-09-02.

Rendered as an **Ext JS 7.6.0 workspace**, not a conventional document page — which is the root of
[[caveat-viewport]] and of [[method-fetch-is-not-render|why a raw fetch sees the wrong thing]].

The server delivered three default tab definitions — `Map`, `Dashboard`, `+` — and the canvas was
**empty for this user**. Key endpoints: `/servlet/Dash?formSubmit=getTreeNodes&node=root` and
`/servlet/JSONDataRequest?reqType=RMTopMenu&node=root`.

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
