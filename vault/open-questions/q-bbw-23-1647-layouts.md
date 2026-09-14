---
title: "Q-BBW-23 — What are the other ~1,500 PageLayout rows?"
tags: [open-question, layouts]
evidence: Observed
status: open
---

The tenant holds **1,647 [[PageLayout]] rows**.

The registries account for **135** — 93 across [[layout-modes|SEP/SUB/LIST]] plus the
[[finding-form-layouts-are-hidden|42 hidden form layouts]].

**So roughly 1,500 rows are unaccounted for.**

**Likely (Inferred):** report layouts (`IsReport = true` — [[rule-RPT-R-001]]), sub-layouts embedded
through `SubEditForm`, and per-Issue-Type step layouts.

That matters more than it sounds. If reports are `PageLayout` rows, then **most of the layout table is
reports**, and a migration that reads "135 layouts" will under-scope by an order of magnitude.

It also interacts with [[q-bbw-13-census-gap]]: `PageLayout` is one of the 25 tables the schema viewer
refuses, so the 17 columns known about it came from a serialiser that emits **only populated
columns** — a lower bound.

### How to settle it

One call: `GET /rest/businessObject/PageLayout/details?fields=…` with a group-by on the discriminating
booleans.
