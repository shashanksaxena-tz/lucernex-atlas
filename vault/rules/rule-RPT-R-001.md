---
title: "RPT-R-001 — A report is a PageLayout row"
tags: [rule, reporting]
evidence: Derived
---

**`RPT-R-001`** · [[module-reporting]] · **Derived**

> **A report is not a distinct record type. It is a [[PageLayout]] row with `IsReport = true`.**

**No `Report` table exists** in the 223-object census.

*(Derived from the absence; Observed for the column.)* And the column was only readable after
[[PageLayout]] was recovered over [[rest-business-object|REST]] — see [[q-bbw-13-census-gap]].

It also probably explains [[q-bbw-23-1647-layouts|the ~1,500 unaccounted layout rows]].

See [[rules-reporting]] for the full register.
