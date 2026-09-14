---
title: "PPL-R-007 — 83% of Member's in-degree is the audit stamp"
tags: [rule, people-parties]
evidence: Derived
---

**`PPL-R-007`** · [[module-people-parties]] · **Derived**

**240 of [[Member]]'s 290 inbound FK columns** are `CreatedByID`/`ModifiedByID`.

One cross-cutting concern, not 161 relationships. The schema's biggest hub is mostly
[[audit-trail|bookkeeping]].

See [[rules-people-parties]] for the full register.
