# CON-R-107 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**Aging is computed: AgingAmountForMonth1..3 and AgingAmountRemainder bucket from the invoice/effective date — the base date itself is inferred, not confirmed.**

Aging is computed: AgingAmountForMonth1..3 and AgingAmountRemainder bucket from the invoice/effective date — the base date itself is inferred, not confirmed.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Aging is computed |
| Stated as | `AgingAmountForMonth1..3`, `AgingAmountRemainder` |
| Stated as | Buckets 0-30 / 31-60 / 61-90 / 90+ from the invoice/effective date |
| Stated as | Aging ladder A |
| Stated as | Observed (labels); base date Inferred |

---

Source: `docs/modules/contracts/rules.md`
