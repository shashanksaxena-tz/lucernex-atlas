---
title: One layout set, copied per tenant, then forked
tags: [finding, tenancy, layouts, core]
evidence: Derived
---

**[[tenant-american-freight|AF]] has 88 page layouts, [[tenant-bbw|BBW]] 93. Joined on
`(mode, PageLayoutID)`, not one pair is shared.**

Taken alone that misleads. Joined instead on `(mode, name)`:

| Join | Result |
|---|---:|
| Shared `(mode, PageLayoutID)` | **0** |
| Shared `(mode, name)` | **80** |
| …of those 80, `primaryTable` mismatches | **0** |
| Only at AF | 7 (four are scratch: `TABLE`, `test` ×3) |
| Only at BBW | 12 |

> **80 of ~87 layouts are the same layout, under the same name, over the same primary table, at a
> different id.**

And the ids are not random: `BBW_id − AF_id` clusters in a narrow band around **+2626 … +2677** on 58
of the 80 — the signature of a contiguous block reassigned when a set is copied into a new tenant.
Even a **duplicate row** (`LIST / ASG Contract Payment Details - Security Deposit`, present twice in
both tenants) was carried across by the copy.

**This replaces a wrong earlier reading.** An earlier revision took "zero shared ids" to mean layouts
are independently firm-authored and filed them under Spoke as unrelated per-firm work. They are not
unrelated. **ASG maintains one standard layout set and deploys a copy into each client tenant, where
it is re-keyed and then drifts.**

The [[screen-export-configuration|Export Configuration]] screen then **named the mechanism in the
vendor's own words** — see [[publish-and-fork]].

### Why it matters

This is the incumbent already running a **template-set-published-per-tenant-then-forked** model — the
same shape as the [[hub-and-spoke]] publish mechanism ASG Edge+ proposes and has not specified. It is
evidence that the mechanism is needed, **and evidence of its failure mode**: with nothing tracking
versions, the two tenants diverged silently, and the only way to tell they came from one source is to
join on name and notice the offset.

**A rebuild needs the layout's provenance — template id, version, fork point — as first-class data.
Lx carries none of it.** See [[three-publish-tiers]].

The drift itself is legible and points one way: [[finding-tenants-differ-by-one-feature]].
