# CON-R-055 — 5. Percentage rent

*Contracts & Leases · Derived*

**The cap is applied: PRPNetExcludedAmount = min(gross, cap); PRPExcessExcludedAmount = gross − net — and the platform stores both numbers, which is what makes the min() reading solid rather than speculative.**

The cap is applied: PRPNetExcludedAmount = min(gross, cap); PRPExcessExcludedAmount = gross − net — and the platform stores both numbers, which is what makes the min() reading solid rather than speculative.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | The cap is applied |
| Stated as | `PRPGrossExcludedAmount`, `PRPComputedCapAmount` |
| Stated as | `PRPNetExcludedAmount = min(gross, cap)`; `PRPExcessExcludedAmount = gross − net` |
| Stated as | Allowed / disallowed exclusion |
| Stated as | Derived (both fields exist as separate stored values) |

---

Source: `docs/modules/contracts/rules.md`
