---
title: "ASC 842 Rent Schedule"
tags: [screen, end-user,accounting]
evidence: Observed
---

`PLForm.jsp?menuPLID=43785`

![The generated schedule, rendered as a list. Note it is a list and "Capital Lease Test" is a detail form — the ASC 840 test is one row per contract, the ASC 842 test produces many.](../assets/screenshots/end-user/asc842-rent-schedule.jpg)
`docs/assets/screenshots/end-user/asc842-rent-schedule.jpg`

Served by `PLForm.jsp` — one of the two files that
[[finding-two-files-serve-56-percent|serve 56% of the product]].

The schedule on screen is a [[SLSummary]]/[[SLPeriod]] pair flagged `IsASC842Schedule`
([[one-engine-three-standards]]).

Two things to hold in mind while looking at it:

- **It is a candidate until approved**, through a three-step workflow, and approval is irreversible
  ([[finding-schedules-are-approved-not-published]]).
- **[[finding-discount-rate-table-empty]]** — the rate table is empty in both tenants, so whether this
  output was ever computed against a real rate is [[q-bbw-18-has-any-schedule-been-calculated|open]].

`ASG ASC 842 Schedule` (98859) and `ASG SL Summary` (98873) declare **the same primary table** — see
[[finding-layouts-over-projections]].

All screens: [[map-of-screens]] · caveat: [[caveat-viewport]]
