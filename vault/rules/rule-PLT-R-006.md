---
title: "PLT-R-006 — Security is a computed shadow"
tags: [rule, platform-tenancy]
evidence: Derived
---

**`PLT-R-006`** · [[module-platform-tenancy]] · **Derived**

[[Security]] is a **read-only computed projection** of [[UserClassSecurity]]. They declare 21 fields
each, identical name for name, and **only the latter is editable**. `Security` has **no physical
table**.

See [[rules-platform-tenancy]] for the full register.
