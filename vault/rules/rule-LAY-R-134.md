---
title: "LAY-R-134 — Lx cannot answer 'which layouts use this field'"
tags: [rule, layouts-and-forms]
evidence: Derived
---

**`LAY-R-134`** · [[module-layouts-and-forms]] · **Derived**

Because [[rule-LAY-R-130|rules are an opaque blob]], **Lx cannot answer "which layouts depend on this
field"**. Where-Used needs normalised rows.

This compounds [[finding-rules-store-labels-not-ids]]: renaming a drop-down value silently breaks
rules, **and the breakage is not discoverable by query.**

Directly relevant to ASG Edge+'s `D-07` / `MST-015` — and note it is a *different* argument from the
retracted one in [[finding-no-where-used-precedent]].

See [[rules-layouts-and-forms]] for the full register.
