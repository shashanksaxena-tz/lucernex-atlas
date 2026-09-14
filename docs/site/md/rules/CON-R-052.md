# CON-R-052 — Step 2 — exclusions (`` … `CON-R-056`)

*Contracts & Leases · Derived*

**An exclusion applies: rawExcluded = salesOfType × SalesExclusion.ExclusionRate.**

An exclusion applies: rawExcluded = salesOfType × SalesExclusion.ExclusionRate.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | `SalesExclusionCap` field |
| Stated as | Meaning |
| Stated as | `PRPGrossSalesAmount` |
| Stated as | Gross sales in the percentage-rent period, for the cap's percentage basis |
| Stated as | `PRPGrossExcludedAmount` |
| Stated as | Σ of raw excluded amounts in this cap group, before the cap |

## What it constrains

[SalesExclusion](../entities/SalesExclusion.md), [SalesExclusionCap](../entities/SalesExclusionCap.md)

---

Source: `docs/modules/contracts/percentage-rent.md`
