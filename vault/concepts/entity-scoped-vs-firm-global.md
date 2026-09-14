---
title: Entity-scoped versus firm-global
tags: [concept, data-model, tenancy]
evidence: Derived
---

The practical half of the [[entity-spine]]: 161 objects hang off an entity, 52 sit above it.

**Entity-scoped (161 objects, 4,644 fields).** Carries `ProjectEntityID` typed `Entity ID`. These
carry **no `FirmID`** at all — tenant isolation is one join deep, through the spine. A query that
forgets the join leaks across tenants, and nothing in the schema will stop it ([[rule-PLT-R-001]]).

**Firm-global (52 objects, 1,053 fields).** Reference data, configuration and templates:
[[WorkFlowTemplate]], [[Complex]], [[UserClassSecurity]], the code tables, the layout registry. These
are the natural [[hub-and-spoke|Hub]] candidates — 47 of them after the 5 out-of-scope ones are
removed.

The split is not a schema boundary. It is a **column**: `IsGlobal` plus `FirmID`, not a second schema
or a physical partition ([[rule-PLT-R-005]]). The same two-tier pattern recurs in three unrelated
subsystems — the [[data-field-catalog|field registry]] (`RGAF.IsGlobal` + `FirmID`), the layout
registry (`Firm Layouts` / `Global Layouts`), and the [[screen-manage-firm-dictionary|firm dictionary]].
That consistency is itself an argument for the [[hub-and-spoke]] shape: the incumbent applies it to
*every* configuration surface.

Source: [`data-model/project-entity.md`](../../docs/data-model/project-entity.md) ·
[`modules/platform-tenancy/tenancy-model.md`](../../docs/modules/platform-tenancy/tenancy-model.md)
