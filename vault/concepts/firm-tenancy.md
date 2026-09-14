---
title: Firm — the tenant boundary
tags: [concept, tenancy]
evidence: Observed
---

A **firm** is the tenant. Everything in the product is scoped to one, and almost every rule turns on
what a firm may see and change versus what the platform owns.

- `FirmID` is the tenant key. [[ProjectEntity|ProjectEntityID]] is **not** — that is the intra-tenant
  partition key. Confusing the two is the single most consequential mistake available here.
- `FirmID` appears on **exactly 13** of the 223 objects: [[ProjectEntity]], the nine
  [[subtype-root|subtype roots]], `GlobalProperty`, [[ReportGroupAvailableField]] and `ReportGroupData`.
  Everywhere else, tenancy is one join deep — reach the spine, then filter. *(Derived,
  [[rule-PLT-R-001]].)*
- It is typed `Text`, not a foreign-key type, so **no `Firm ID` FK type exists** and a schema-driven
  FK tool silently misses the relationship every row has. *(Derived, [[rule-PLT-R-002]].)*
- The [[Firm]] record itself is only 18 fields, but it holds the per-entity-type default layout
  assignments and the `Allow X?` entitlement flags.

Two tenants were read: [[tenant-bbw]] (`firmID=3159`) and [[tenant-american-freight]] (`firmID=3158`).
What is identical between them is as informative as what differs — see [[finding-platform-seeded-by-id]].

For the rebuild this bears directly on [[hub-and-spoke]] and on the two contradictory ADR-004s;
[[finding-firm-fields-are-physical-columns]] is the evidence that settles it.

Source: [`modules/platform-tenancy/tenancy-model.md`](../../docs/modules/platform-tenancy/tenancy-model.md)
