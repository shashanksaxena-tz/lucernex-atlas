# CON-R-042 — 4. Escalations

*Contracts & Leases · Inferred*

**The driver is index-based: rawChange = (IndexAmount / IndexBaseFactor) − 1 — assumes IndexAmount is a level, which is unconfirmed.**

The driver is index-based: rawChange = (IndexAmount / IndexBaseFactor) − 1 — assumes IndexAmount is a level, which is unconfirmed.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | The driver is index-based |
| Stated as | `EscalationIndexID` → `EscalationIndex.IndexAmount`, `IndexBaseFactor` |
| Stated as | `rawChange = (IndexAmount / IndexBaseFactor) − 1` |
| Stated as | Raw index change |
| Stated as | Inferred — depends on whether `IndexAmount` is a level or a rate (open) |

## What it constrains

[EscalationIndex](../entities/EscalationIndex.md)

Columns named: `EscalationIndex.IndexAmount`

---

Source: `docs/modules/contracts/rules.md`
