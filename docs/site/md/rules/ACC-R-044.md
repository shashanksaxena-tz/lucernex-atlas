# ACC-R-044 — Translation vs. revaluation mapping

*Lease Accounting & Payments · Observed*

**`Contract.IsTranslation = true` ⇒ use the Translation mapping on `Admin > Manage Company > Financial Settings`; false ⇒ the Revaluation mapping.**

A contract flagged 'Is Translation' uses the translation mapping; otherwise the revaluation mapping.

## Stated for a rule engine

|  |  |
|---|---|
| The test | `Contract.IsTranslation = true` ⇒ use the Translation mapping on `Admin > Manage Company > Financial Settings`; false ⇒ the Revaluation mapping |

## Confidence

Observed, stated verbatim. --- ## G. Modification, remeasurement, impairment

---

Source: `docs/modules/accounting/rules.md`
