---
title: VirtualPercentageRentPeriod
tags: [entity, projection, variable-rent]
evidence: Observed
---

**`virtual_percentage_rent_period` · 38 fields** — a [[virtual-projection|computed projection]], not a
table. No primary key, no audit column, no `BOMapClientRecordID`.

It is the **projection** layer of [[setup-schedule-transaction]] for [[PercentageRent]]: the forward
period expansion nobody stores.

**And it is the primary table of two user-facing Summary Pages** —
`ASG Breakpoint Schedule` (98921) and `ASG Percent Rent Schedule` (98934), plus
`ASG Contract Payment Details - Breakpoints` (98908). See [[finding-layouts-over-projections]].

That makes it a direct constraint on the layout engine and raises
[[q-bbw-11-virtual-layout-writable]]: with no key, is such a layout structurally read-only?

The layout registry labels its primary table `Percentage Rent Period`. The physical-name match to
`VirtualPercentageRentPeriod` is what resolved the ambiguity — [[caveat-labels-are-tenant-local]].
