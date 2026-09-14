# CON-R-137 — 11. Typing and integrity rules for the rebuild (Constitution §4.4)

*Contracts & Leases · Inferred*

**Any recovery measure is unset: for the rebuild, model recovery measures as nullable BigDecimal, never zero-defaulted — a zero default silently produces spurious 100% variances.**

Any recovery measure is unset: for the rebuild, model recovery measures as nullable BigDecimal, never zero-defaulted — a zero default silently produces spurious 100% variances.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Any recovery measure is unset |
| Stated as | `NoZeroDef`-suffixed fields |
| Stated as | A zero default produces spurious 100% variances |
| Stated as | Model recovery measures as nullable `BigDecimal`, not zero-defaulted |
| Stated as | Inferred |

---

Source: `docs/modules/contracts/rules.md`
