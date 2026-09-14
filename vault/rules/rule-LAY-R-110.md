---
title: "LAY-R-110 — A Summary Page is composed, not authored"
tags: [rule, layouts-and-forms]
evidence: Observed
---

**`LAY-R-110`** · [[module-layouts-and-forms]] · **Observed**

A Summary Page is **composed of independently-managed Sub-page layouts**, not authored
monolithically. On the rendered screens, SUB layouts appear as **titled sections** and are **reused
across pages**.

Which is why [[layout-modes|all 32 SUB layouts carry no `ParentPageLayoutID`]] — they are composition
units, not destinations.

See [[rules-layouts-and-forms]] for the full register.
