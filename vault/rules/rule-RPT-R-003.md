---
title: "RPT-R-003 — Output format is part of the definition"
tags: [rule, reporting]
evidence: Observed
---

**`RPT-R-003`** · [[module-reporting]] · **Observed**

A report's output format is a **required property of the definition** (`OutputType`), not chosen at
run time.

So "the same report as PDF" is a second report. A rebuild offering format at run time is offering
something new — fine, but it changes the object count on migration.

See [[rules-reporting]] for the full register.
