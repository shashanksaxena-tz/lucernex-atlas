# CON-R-135 — 11. Typing and integrity rules for the rebuild (Constitution §4.4)

*Contracts & Leases · Observed*

**Any usage-based rent arithmetic: 6-decimal precision is required on unit rates; use BigDecimal with explicit scale and rounding mode, never a binary float.**

Any usage-based rent arithmetic: 6-decimal precision is required on unit rates; use BigDecimal with explicit scale and rounding mode, never a binary float.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Any usage-based rent arithmetic |
| Stated as | `sTYPE_NUMBER_FRACTION6DIGITS` unit rates × large usage counts |
| Stated as | 6-decimal precision is required; binary floating point loses money here |
| Stated as | `BigDecimal` with explicit scale and rounding mode |
| Stated as | Observed |

---

Source: `docs/modules/contracts/rules.md`
