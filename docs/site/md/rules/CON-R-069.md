# CON-R-069 — 5. Percentage rent

*Contracts & Leases · Observed*

**A percentage-rent clause is flagged ExtFinalPeriodToLeaseExpDt: the final period extends to lease expiry instead of truncating at the usual period boundary.**

A percentage-rent clause is flagged ExtFinalPeriodToLeaseExpDt: the final period extends to lease expiry instead of truncating at the usual period boundary.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | `ExtFinalPeriodToLeaseExpDt = true` |
| Stated as | `Contract.ExpireDate` |
| Stated as | The final percentage-rent period extends to lease expiry rather than truncating at the period boundary |
| Stated as | Final period end |
| Stated as | Observed (label) |

## What it constrains

[Contract](../entities/Contract.md)

Columns named: `Contract.ExpireDate`

---

Source: `docs/modules/contracts/rules.md`
