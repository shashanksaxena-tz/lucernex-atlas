---
title: "PLT-R-005 — Global/Firm scope is a column"
tags: [rule, platform-tenancy]
evidence: Observed
---

**`PLT-R-005`** · [[module-platform-tenancy]] · **Observed**

`IsGlobal` + `FirmID` — **not a second schema and not a physical partition**.

The same two-tier pattern appears in three unrelated subsystems: the
[[data-field-catalog|field registry]], the layout registry, and the
[[screen-manage-firm-dictionary|firm dictionary]]. That consistency is itself an argument for
[[hub-and-spoke]].

See [[rules-platform-tenancy]] for the full register.
