---
title: "PPL-R-002 — No hard FK references a person"
tags: [rule, people-parties]
evidence: Inferred
---

**`PPL-R-002`** · [[module-people-parties]] · **Inferred**

**Twelve columns typed [[soft-reference|`Contact`]]** are polymorphic into the identity aggregate. No
hard FK type points at [[Person]] at all — so the relationship is invisible to schema-driven tooling.

See [[rules-people-parties]] for the full register.
