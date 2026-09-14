---
title: "Q-BBW-01 — What sets isReadOnlyRecord?"
tags: [open-question, configuration]
evidence: Inferred
status: open
---

**The original question — *"is [[code-table]] delete suppressed by reference count?"* — is answered:
no.** See [[finding-no-where-used-precedent]], which retracts the inference and the argument built on
it.

**What remains open: what actually sets the flag.**

`isReadOnlyRecord` is supplied per row by the server. The `FirmCode` record exposes only four fields
(Name, Description, Inactive, Available-for-Portfolios) and **no provenance or reference-count
attribute**. What sets it is **not observable from the client**.

**Best current reading (Inferred, not proven):** it marks **platform-seeded rows**, which a firm may
rename but not delete, against firm-added rows it may delete. It fits every mixed table — including
`Contact Type` (`2022`), which splits 10 protected / 4 deletable along a clean lxBOID boundary
(`9972`–`9981` versus `9982`–`9986`), and the duplicate-`Option` case in [[KeyDate|`3006`]].

Corroborating: of the **1,045** code-table values unique to one tenant (477 AF, 568 BBW), **zero** are
read-only. And on the **646** values sharing `(tableType, name)`, the flag agrees **646 of 646**.

### How to settle it

**Compare the same `LxBOID` across both tenants.** Identical flag supports provenance; a differing
flag disproves it.

### Why it still matters

The platform **does** protect seeded values from deletion, and ASG Edge+ needs that notion — it bears
on `D-07` and on `DeactivationPolicy`. It is just not a Where-Used capability.
