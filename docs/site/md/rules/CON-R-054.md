# CON-R-054 — 5. Percentage rent

*Contracts & Leases · Inferred*

**A cap group is evaluated: PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent) — the effective cap, whichever binds first.**

A cap group is evaluated: PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent) — the effective cap, whichever binds first.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A cap group is evaluated |
| Stated as | `SalesExclusionCap.CapAmount`, `.CapPercent`, `.PRPGrossSalesAmount` |
| Stated as | `PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent)` |
| Stated as | Effective cap |
| Stated as | Inferred |

## What it constrains

[SalesExclusionCap](../entities/SalesExclusionCap.md)

Columns named: `SalesExclusionCap.CapAmount`

---

Source: `docs/modules/contracts/rules.md`
