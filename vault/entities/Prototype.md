---
title: Prototype
tags: [entity, facilities, subtype-root]
evidence: Observed
---

**`prototype` · 113 fields · [[module-facilities-locations]]**

A standard store or facility design used for rollout programmes — *"build another one of these"*. A
[[subtype-root]], referenced by 11 other objects, and it **does not render as a navigation root** in
either tenant, consistent with [[finding-root-renders-iff-record-exists]].

Its `Location`, `Complex` and `DMA` columns exist in the schema but are **not
administrator-configurable** ([[rule-FAC-R-019]]) — a reminder that the admin catalog and the physical
schema are different populations ([[data-field-catalog]]).

See [[module-facilities-locations]] · [[DMA]]
