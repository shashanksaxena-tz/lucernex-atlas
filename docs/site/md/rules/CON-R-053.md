# CON-R-053 — 5. Percentage rent

*Contracts & Leases · Derived*

**Exclusions share a cap group (ExclusionGroupCapID): PRPGrossExcludedAmount sums the raw excluded amounts within the group, before the cap.**

Exclusions share a cap group (ExclusionGroupCapID): PRPGrossExcludedAmount sums the raw excluded amounts within the group, before the cap.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Exclusions share a cap group |
| Stated as | `SalesExclusion.ExclusionGroupCapID` → `SalesExclusionCap` |
| Stated as | `PRPGrossExcludedAmount = Σ rawExcluded` in the group |
| Stated as | Pre-cap total |
| Stated as | Derived |

## What it constrains

[SalesExclusion](../entities/SalesExclusion.md), [SalesExclusionCap](../entities/SalesExclusionCap.md)

Columns named: `SalesExclusion.ExclusionGroupCapID`

---

Source: `docs/modules/contracts/rules.md`
