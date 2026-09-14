# CON-R-092 — Grid structure and variances

*Contracts & Leases · Inferred*

**A measure is unset: fields suffixed NoZeroDef return null/blank rather than 0.**

A measure is unset: fields suffixed NoZeroDef return null/blank rather than 0.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A measure is unset |
| Stated as | Fields suffixed `NoZeroDef` |
| Stated as | Return null/blank rather than 0, so a genuine zero is distinguishable from unentered — preventing spurious 100% variances |
| Stated as | Nullable semantics |
| Stated as | Inferred (from the name) |

---

Source: `docs/modules/contracts/rules.md`
