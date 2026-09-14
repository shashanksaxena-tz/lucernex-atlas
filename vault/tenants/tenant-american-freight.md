---
title: "Tenant: (ASG)American Freight"
tags: [tenant]
evidence: Observed
---

| Property | Value |
|---|---|
| Tenant | `(ASG)American Freight`, `firmID=3158` |
| Build at first capture | `26.08.0.46` (later `26.08.0.39` on the dashboard capture) |
| Build at re-read | **`26.09.0.113`** — the same as [[tenant-bbw\|BBW]] |
| Captured | 2026-09-02 and 2026-09-10, re-read 2026-09-13 |

The **first** tenant, and the source of most of this corpus. Almost every document in `docs/` was
written from it, which is exactly why reading a second one mattered.

**The build upgrade is load-bearing.** When AF moved from `26.08.0.46` to `26.09.0.113`, an AF/BBW
asymmetry that a published inference rested on **disappeared** — see
[[finding-no-where-used-precedent]]. Comparisons made before and after the upgrade are not
comparable, and several in the corpus had to be re-run.

**Four navigation roots, 109 nodes.** It holds **2** contracts, **zero** of them typed
`Equipment Contract`, and **does not render** the [[equipment-contract|Equipment Contract]] root even
though its entitlement flag is on, its menu structure is present and 8 of 10 user classes are granted
page access — which is the whole of [[finding-root-renders-iff-record-exists]].

It is also the only tenant with a **vendor schema export**, `_lucernex_objects_summary.txt` — 223
objects, 7,421 fields. Every field-level and table-level claim in this corpus rests on that file.

**AF exposes six more admin tools than BBW**, including `/lxadmin/` vendor-only entries — so admin-tool
visibility is per-tenant or per-user-class, not fixed.

See [[tenant-comparison]] for what the two settle between them.

What it retains that BBW has replaced: older co-tenancy layout variants and `ASG Client Request Log`,
plus four scratch rows (`TABLE`, `test` ×3). See [[finding-tenants-differ-by-one-feature]].
