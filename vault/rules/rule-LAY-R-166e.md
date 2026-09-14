---
title: "LAY-R-166e — No mechanism passes values between steps"
tags: [rule, layouts-and-forms]
evidence: Derived
---

**`LAY-R-166e`** · [[module-layouts-and-forms]] · **Derived**

> **The workflow engine has no general mechanism for passing field values between steps.**

**Derived by exhaustive scan** — which is the only way to prove an absence.

Combined with [[rule-WF-R-055]] (the engine writes exactly one field), this bounds what a
[[workflow-template|Lx workflow]] can do very tightly. **ASG Edge+ must design it**, not migrate it.

See [[rules-layouts-and-forms]] for the full register.
