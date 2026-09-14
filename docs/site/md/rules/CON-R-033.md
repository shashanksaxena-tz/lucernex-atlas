# CON-R-033 — 3. Recurring expense: setup and schedule

*Contracts & Leases · Observed*

**The clause is flagged IsCustomPaymentCoverage: the same ExpenseSetup record supports annual, quarterly or semi-annual coverage without a schema change, via explicit month-and-day markers per frequency.**

The clause is flagged IsCustomPaymentCoverage: the same ExpenseSetup record supports annual, quarterly or semi-annual coverage without a schema change, via explicit month-and-day markers per frequency.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | `ExpenseSetup.IsCustomPaymentCoverage = true` |
| Stated as | `CoverageBeginAnnual`, `CoverageBeginQ1..Q4`, `CoverageBeginSemiAnnual1..2`, `PaymentDueAnnual`, `PaymentDueQ1..Q4`, `PaymentDueSemiAnnual1..2` |
| Stated as | The same setup record supports annual, quarterly or semi-annual coverage without schema change; explicit month-and-day markers per frequency |
| Stated as | Coverage/due grid |
| Stated as | Observed |

---

Source: `docs/modules/contracts/rules.md`
