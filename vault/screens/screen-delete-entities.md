---
title: "Delete Entities"
tags: [screen, administration,lxadmin]
evidence: Observed
---

`/en/admin/lxadmin/DeleteEntities.jsp`

> **One of only two of the 57 admin tools with no screenshot in this corpus — deliberately.**
> A vendor-only destructive tool, not opened. The other is [[screen-restful-docs]].

One of four `/lxadmin/` vendor-only tools, alongside `Modify Straight Line Status`
(`SLDemoTweaks.jsp`), `Data Conversion Cleaner` (`DataLoadTweaks.jsp`) and `Test Email Address`
(`EmailTest.jsp`).

**[[tenant-american-freight|AF]] exposes all four; [[tenant-bbw|BBW]] exposes three** — admin-tool
visibility is per-tenant or per-user-class, not fixed, which is a datapoint for the 57-versus-63 count
itself.

Worth noting for the rebuild: the incumbent's answer to "delete an entity" is **a vendor-only tool**,
not a user action — which is consistent with [[code-table|seeded values being delete-protected]] and
with ASG Edge+'s own `DeactivationPolicy` defaulting to `WARN_AND_BLOCK`.

See [[feature-administration]] · [[method-omitting-identities]]

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
