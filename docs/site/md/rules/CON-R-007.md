# CON-R-007 — 1. The Clause / Schedule / Transaction / Projection pattern

*Contracts & Leases · Derived*

**Operator invokes GENERATE_RENT (or a sibling): generate L2 transactions from every eligible L1 row where ProcessedFlag is false; set ProcessedFlag = true, ProcessedDate = now.**

Operator invokes GENERATE_RENT (or a sibling): generate L2 transactions from every eligible L1 row where ProcessedFlag is false; set ProcessedFlag = true, ProcessedDate = now.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Operator invokes `GENERATE_RENT` (or a sibling) |
| Stated as | L1 rows where `ProcessedFlag = false` |
| Stated as | Generate L2 transactions from each eligible row; set `ProcessedFlag = true`, `ProcessedDate = now` |
| Stated as | N × L2 rows |
| Stated as | Derived |

---

Source: `docs/modules/contracts/rules.md`
