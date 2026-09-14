---
title: "PLT-R-003 — ProjectEntityID must survive database-per-tenant"
tags: [rule, platform-tenancy]
evidence: Derived
---

**`PLT-R-003`** · [[module-platform-tenancy]] · **Derived**

Only `FirmID`'s job is subsumed by the database boundary. **[[ProjectEntity|`ProjectEntityID`]] is the
intra-tenant partition key and must survive.**

Confusing the two is the most consequential mistake available in this data model.

See [[rules-platform-tenancy]] for the full register.
