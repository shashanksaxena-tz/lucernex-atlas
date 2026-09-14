# CON-R-041 — 4. Escalations

*Contracts & Leases · Observed*

**The driver is fixed: new amount = f(base or current amount, FixedAmount, EscalationMethod) — but EscalationMethod is free text, so its value space is unknown.**

The driver is fixed: new amount = f(base or current amount, FixedAmount, EscalationMethod) — but EscalationMethod is free text, so its value space is unknown.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | The driver is fixed |
| Stated as | `CodeEscalationTypeID`, `EscalationMethod(Text)`, `FixedAmount`, `BaseAmount` |
| Stated as | New amount = f(base or current, `FixedAmount`, `EscalationMethod`). `EscalationMethod` is free text — its value space is unknown |
| Stated as | New amount |
| Stated as | Observed (fields); formula Inferred |

---

Source: `docs/modules/contracts/rules.md`
