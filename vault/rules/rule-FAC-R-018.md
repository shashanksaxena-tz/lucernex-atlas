---
title: "FAC-R-018 — Generic-attachment children fit any subtype"
tags: [rule, facilities-locations]
evidence: Derived
---

**`FAC-R-018`** · [[module-facilities-locations]] · **Derived**

`Ownership`, `SiteSurvey`, `LandPurchaseSummary` and their kin attach to **any [[ProjectEntity]]
subtype** rather than to one. The polymorphism is real and a rebuild must model it, not special-case
it per parent.

See [[rules-facilities-locations]] for the full register.
