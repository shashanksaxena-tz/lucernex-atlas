---
title: "Manage Firm Dictionary"
tags: [screen, administration,configuration]
evidence: Observed
---

`/en/admin/Dictionary.jsp`

![The screen's own note offers it "to provide new translation or to just overwrite the field labels". That second clause is a caveat on this entire corpus.](../assets/screenshots/bbw-admin/17-manage-firm-dictionary.jpg)
`docs/assets/screenshots/bbw-admin/17-manage-firm-dictionary.jpg` · `af-admin/18-manage-firm-dictionary.jpg`

**A firm can overwrite field labels tenant-wide** by uploading a spreadsheet, with global and
firm-specific layers and per-language variants. The default download scope is
*"Firm specific phrases not translated"*.

**[[caveat-labels-are-tenant-local]]** — every screen name, navigation node name, field label and
[[code-table]] value name recorded anywhere in this corpus **may be tenant-local**. Internal names are
unaffected, which turns *"use real field and table names in `code`"* from a style preference into a
correctness requirement.

It also explains a measurement error at scale: the census reconciliation reported 18 missing tables on
UI label and **6** on physical name ([[finding-punch-list-out-of-scope]]).

**Whether either tenant has actually overridden anything is unknown.** One `Download Current
Dictionary` with *Firm specific phrases* selected would settle it, and it is worth doing.

This is the **third** subsystem on the identical global/firm two-tier pattern, after the
[[data-field-catalog|field registry]] and the layout registry — which is itself an argument for
[[hub-and-spoke]].

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
