# CON-R-136 — 11. Typing and integrity rules for the rebuild (Constitution §4.4)

*Contracts & Leases · Observed*

**Any percentage arithmetic: sTYPE_PERCENTAGE fields multiply money in the pro-rata, breakpoint and CPI paths; store as BigDecimal and fix the scale and rounding policy at every multiplication step.**

Any percentage arithmetic: sTYPE_PERCENTAGE fields multiply money in the pro-rata, breakpoint and CPI paths; store as BigDecimal and fix the scale and rounding policy at every multiplication step.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Any percentage arithmetic |
| Stated as | `sTYPE_PERCENTAGE` fields (188 catalog-wide) used as multipliers in `CON-R-059`, `CON-R-084`, `CON-R-042` |
| Stated as | Rates multiply money in the pro-rata share, breakpoint and CPI paths |
| Stated as | Store as `BigDecimal`; fix scale and rounding at each step; never `double` |
| Stated as | Observed hazard, Judgement on remedy |

## Rules it cites

[CON-R-042](CON-R-042.md), [CON-R-059](CON-R-059.md), [CON-R-084](CON-R-084.md)

---

Source: `docs/modules/contracts/rules.md`
