---
title: A navigation root renders iff the firm holds a record of that type
tags: [finding, navigation, tenancy, core]
evidence: Inferred
---

> **A navigation root renders if and only if the firm holds at least one record of that root's
> `ProjectEntityTypeName`.** Entitlement is necessary but not sufficient.

**Four other gates were eliminated first**, all confirmed open at
[[tenant-american-freight|American Freight]] while the [[equipment-contract|Equipment Contract]] root
still refused to render:

| Gate | State at AF | Verdict |
|---|---|---|
| Build version | same `26.09.0.113` as BBW | ruled out |
| [[Firm]] entitlement (`Allow Equipment Contracts?`) | **Yes** | ruled out |
| Menu structure (id `41087`, 64 nodes) | **present** | ruled out |
| [[security-ladder\|User-class page access]] | **granted, 8 of 10 classes** | ruled out |

The discriminating measurement, run format-agnostically against both tenants:

```
GET /rest/businessObject/Contract/details?fields=ProjectEntityTypeName&$top=5000
```

| Tenant | Contracts | typed `Equipment Contract` | root |
|---|---:|---:|:--:|
| [[tenant-bbw\|BBW]] | 2,014 | **1** | **renders** |
| [[tenant-american-freight\|AF]] | 2 | **0** | does not render |

**One record is the entire difference** — 32 navigation nodes and 26 screens, switched on by a single
row.

**It explains the `Program` anomaly too, which is what makes it the answer.** AF's `Program` rows carry
`ProjectEntityTypeName = "Portfolio"`, so the structure named `Portfolio` (924) matches and renders
while the separate structure named `Program` (3851) matches **zero** and does not. Two structures, one
table, different type strings. See [[subtype-root]].

**The threshold is existence, not volume** — BBW's `Program` table holds two rows and that is enough.

### Confidence, and the falsifier

**Inferred, not Observed as a mechanism.** An 11-for-11 correlation across two tenants, not a reading
of the rendering code. **The falsifier is specific:** a tenant with the entitlement on, the type
registered, page access granted and **zero rows** that *still* renders the root.

**The circularity objection, and why it fails here.** Record existence could be a consequence rather
than a cause — nobody creates records for a module they cannot see. Equipment Contract breaks that
loop twice: AF holds the entitlement and could have created one, and the `EquipmentContract`
objectType is **registered and live at AF** (HTTP 200, zero rows) against HTTP 400 for unregistered
types. **Not-provisioned and not-populated are distinguishable, and AF is the latter** — which also
eliminates type registration, the leading alternative.

AF's zero was [[method-verify-a-zero|verified three ways]].

**For ASG Edge+:** navigation visibility in the incumbent is **data-driven, not
configuration-driven**. A tenant's menu changes shape as its first record of a type is created. That
is a behaviour to reproduce deliberately or reject deliberately — not to discover by accident.

Open question: [[q-bbw-12-equipment-contract-root]] ·
Source: [`tenants/bbw-vs-american-freight.md` §25](../../docs/tenants/bbw-vs-american-freight.md)
