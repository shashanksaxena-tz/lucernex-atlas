# CON-R-026 — 2. Contract identity and hierarchy

*Contracts & Leases · Derived*

**Any rollup is read: the rollups are denormalised and can be stale — Contract carries no recalculation flag equivalent to SLSummary's.**

Any rollup is read: the rollups are denormalised and can be stale — Contract carries no recalculation flag equivalent to SLSummary's.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Any rollup is read |
| Stated as | — |
| Stated as | The rollups are denormalised and can be stale; `SLSummary` has explicit `NeedsRecalculation`/`RecalcTriggerDate`, `Contract` has no equivalent |
| Stated as | Staleness risk |
| Stated as | Derived |

## What it constrains

[SLSummary](../entities/SLSummary.md), [Contract](../entities/Contract.md)

---

Source: `docs/modules/contracts/rules.md`
