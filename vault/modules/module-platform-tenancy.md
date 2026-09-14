---
title: Platform and tenancy
tags: [module, platform-tenancy, core]
evidence: Derived
---

**21 objects · 385 fields · rules `PLT-R-001`…`PLT-R-016`**

Not a native Lx module — this corpus's own assembly of the scaffolding a multi-tenant,
entity-polymorphic product needs underneath everything else. [[Firm]] and [[ProjectEntity]] are what
make it load-bearing rather than a junk drawer.

Concepts: [[firm-tenancy]] · [[entity-spine]] · [[subtype-root]] ·
[[entity-scoped-vs-firm-global]] · [[security-ladder]] · [[audit-trail]] · [[hub-and-spoke]]

Entities: [[ProjectEntity]] · [[Firm]] · [[Project]] · [[Organization]] · [[Region]] ·
[[StateProvinceCountry]] · [[Jurisdiction]] · [[Security]] · [[UserClassSecurity]] ·
[[LinkMemberProjectEntity]]

The four facts most worth carrying:

1. **`FirmID` is the tenant key; `ProjectEntityID` is not.** Tenant isolation is **one join deep**
   and nothing in the schema enforces it ([[rule-PLT-R-001]]).
2. **No `Firm ID` FK type exists** ([[rule-PLT-R-002]]) — a schema-driven tool sees no tenancy at all.
3. **Global/Firm scope is a column**, not a schema or a partition ([[rule-PLT-R-005]]).
4. **[[Project]] and [[ProjectEntity]] are both live candidates for the spine** and are unreconciled
   ([[rule-PLT-R-016]]). Do not silently pick one.

Four thin stubs (`EntityTemplate`, `MapClientSchedule`, `Notify`, `ScratchPad`) and [[Region]] are
**joins or truncations, not one-column tables** ([[rule-PLT-R-014]]).

Rules: [[rules-platform-tenancy]] ·
[`modules/platform-tenancy/`](../../docs/modules/platform-tenancy/README.md)
