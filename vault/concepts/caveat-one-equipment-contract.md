---
title: "Caveat: BBW holds exactly one Equipment Contract"
tags: [caveat, equipment, meta]
evidence: Observed
---

[[tenant-bbw|BBW]] holds **exactly one** equipment contract — `ASG Equipment Contract`, lxID 507018,
1 of 2,008 sampled contracts.

So every [[equipment-contract|Equipment Contract]] screen in this corpus shows **one record's
population, not the module's range**. An empty section may be empty *for this record* rather than
unused in the module. Four screens were captured — [[screen-eq-details-summary]],
[[screen-eq-abstract-details]], [[screen-eq-payment-details]], [[screen-eq-accounting-details]] — and
all four md5s differ, so they are four genuinely distinct screens; that is all the capture proves.

The same single row is also the entire reason the root renders at all
([[finding-root-renders-iff-record-exists]]). One record switches on 32 navigation nodes and 26
screens.

The record itself: `Contract ID ASG1234`, commence `01/09/2026`, expire `30/09/2031`, one asset
(`Tractor`, asset group `ASG`).

Also note **32 of its 32 nodes carry zero `PageLayoutField` rows** — the whole module renders from
platform defaults with no firm layout anywhere. Nothing in the tenant has been configured for it.
