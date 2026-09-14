# CON-R-123 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**Percentage-rent accrual is reconciled: VirtualPRAccrualPeriod's computed AccrualAmount{ThisPeriod,PriorPeriods,Total} is displayed next to the PostedAccrualAmount{...} that was actually posted, with IsPosted as the flag.**

Percentage-rent accrual is reconciled: VirtualPRAccrualPeriod's computed AccrualAmount{ThisPeriod,PriorPeriods,Total} is displayed next to the PostedAccrualAmount{...} that was actually posted, with IsPosted as the flag.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Percentage-rent accrual is reconciled |
| Stated as | `VirtualPRAccrualPeriod.AccrualAmount{ThisPeriod,PriorPeriods,Total}` vs `PostedAccrualAmount{…}`, `IsPosted` |
| Stated as | Recomputed accrual is displayed against what was actually posted |
| Stated as | Reconciliation pair |
| Stated as | Observed |

---

Source: `docs/modules/contracts/rules.md`
