---
title: "PLT-R-002 — There is no Firm ID foreign-key type"
tags: [rule, platform-tenancy]
evidence: Derived
---

**`PLT-R-002`** · [[module-platform-tenancy]] · **Derived**

`FirmID` is typed **`Text`**, so **no `Firm ID` FK type exists** in the 60-type vocabulary.

**A schema-driven FK tool silently misses the relationship every row has.** See [[type-system]] ·
[[firm-tenancy]].

See [[rules-platform-tenancy]] for the full register.
