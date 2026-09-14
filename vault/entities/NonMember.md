---
title: NonMember
tags: [entity, people]
evidence: Observed
---

**`non_member` · 37 fields · [[module-people-parties]]**

An external portal or vendor identity without a platform licence. **Field-for-field identical to
[[Person]]** — 37 fields, 37 matching types, zero differences — which is the evidence that `Person` is
a supertype and these are its subtypes on a shared `PersonID` ([[rule-PPL-R-001]]).

The practical consequence: a rebuild that models "user" and "contact" as unrelated tables cannot
express what this product does, and one that merges them loses the licence distinction.

See [[Member]]
