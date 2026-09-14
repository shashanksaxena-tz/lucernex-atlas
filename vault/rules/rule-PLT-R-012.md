---
title: "PLT-R-012 — Two unreconciled audit mechanisms coexist"
tags: [rule, platform-tenancy]
evidence: Derived
---

**`PLT-R-012`** · [[module-platform-tenancy]] · **Derived**

`AuditColumn`/`AuditTable` — the field-change trail — and the inline `CreatedBy`/`ModifiedBy` stamps
on the rows themselves. **162 of 223 objects carry an inline stamp, but only 79 carry `CreatedByID`
against 161 carrying `ModifiedByID`.**

See [[audit-trail]] · [[rule-PPL-R-008]].

See [[rules-platform-tenancy]] for the full register.
