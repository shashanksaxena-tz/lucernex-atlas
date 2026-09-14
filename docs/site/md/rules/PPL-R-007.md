# PPL-R-007 — 83% of `Member`'s in-degree is the universal audit-stamp pair, not business routing

*People & Parties · Derived*

**The identity/user record must be cheaply reachable from nearly every write path in the product for stamping alone, independent of its true business-domain reference count (50 edges).**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any capacity-planning or service-boundary decision involving the identity service |
| What it reads | 290 FK edges target `Member`; 240 of them are `CreatedByID`/`ModifiedByID` |
| What it writes | The identity/user record must be cheaply reachable from nearly every write path in the product for stamping alone, independent of its true business-domain reference count (50 edges) |

## What it constrains

[Member](../entities/Member.md)

## Confidence

Derived — exhaustive edge-count analysis, `data-model.md`

---

Source: `docs/modules/people-parties/rules.md`
