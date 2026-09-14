---
title: "FAC-R-002 — Location has no reverse pointer"
tags: [rule, facilities-locations]
evidence: Observed
---

**`FAC-R-002`** · [[module-facilities-locations]] · **Observed**

A [[Location]] carries **no `FacilityID`**. The one-to-many is enforced **only from the child side**
([[rule-FAC-R-001]]) — so one Location holds many Facilities, and you can only see that by looking up.

See [[rules-facilities-locations]] for the full register.
