# CON-R-022 — 2. Contract identity and hierarchy

*Contracts & Leases · Derived*

**Determining the discount rate: look up DiscountRate by accounting method + contract use + geography + a min/max-scheduled-months band, and stamp it onto Contract.DiscountRate.**

Determining the discount rate: look up DiscountRate by accounting method + contract use + geography + a min/max-scheduled-months band, and stamp it onto Contract.DiscountRate.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Determining the discount rate |
| Stated as | `CodeAccountingMethodID`, `CodeContractUseID`, geography, schedule length |
| Stated as | Look up `DiscountRate` by method + use + country/state + `MinSchedMons`..`MaxSchedMons` band; stamp onto `Contract.DiscountRate` |
| Stated as | Discount rate |
| Stated as | Derived |

## What it constrains

[DiscountRate](../entities/DiscountRate.md), [Contract](../entities/Contract.md)

Columns named: `Contract.DiscountRate`

---

Source: `docs/modules/contracts/rules.md`
