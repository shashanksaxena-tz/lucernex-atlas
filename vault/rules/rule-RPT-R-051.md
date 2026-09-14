---
title: "RPT-R-051 — Dashboard tiles are secured by title string"
tags: [rule, reporting]
evidence: Observed
---

**`RPT-R-051`** · [[module-reporting]] · **Observed**

> **Not by record id. By title string.**

**Renaming a tile breaks its grants.**

The same defect shape as [[finding-rules-store-labels-not-ids]] — a display string used as an
identifier — in a second, unrelated subsystem. Which suggests it is a house style, not an oversight,
and both should be designed out.

*(Observed, plus Inferred for the breakage.)*

See [[rules-reporting]] for the full register.
