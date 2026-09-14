---
title: "PLT-R-001 — Tenant isolation is one join deep"
tags: [rule, platform-tenancy]
evidence: Derived
---

**`PLT-R-001`** · [[module-platform-tenancy]] · **Derived**

The 161 [[entity-scoped-vs-firm-global|entity-scoped]] objects carry **no `FirmID`**. To scope a
query you must join [[ProjectEntity]] and filter there.

**Nothing in the schema enforces it.** A query that forgets the join leaks across tenants silently —
which is a large part of the argument for [[hub-and-spoke|database-per-tenant]].

See [[rules-platform-tenancy]] for the full register.
