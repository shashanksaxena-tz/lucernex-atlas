---
title: "PLT-R-014 — Single-field objects are joins or truncations"
tags: [rule, platform-tenancy]
evidence: Derived
---

**`PLT-R-014`** · [[module-platform-tenancy]] · **Derived**

`EntityTemplate`, `MapClientSchedule`, `Notify`, `AuditTable`, `FolderTemplate`, [[Region]] and their
kin declare one field each.

> **Do not model them as one-column tables.** They are joins, or the export truncated them.

18 objects in the census declare exactly one field.

See [[rules-platform-tenancy]] for the full register.
