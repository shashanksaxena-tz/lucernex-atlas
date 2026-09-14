# ACC-R-042 — Which short-term liability is reported

*Lease Accounting & Payments · Observed*

**`Liability Amortization Based` ⇒ use `Forward12MonthLiabilityAmortBased`; `PV Based` ⇒ use `Forward12MonthLiabilityPVBased`.**

A firm-level setting selects the amortisation-based or PV-based figure.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | reporting the short-term liability |
| What it reads | firm setting Short-Term/Long-Term Liability Calculation Method (`Admin > Manage Company > Financial Settings`) |
| The test | `Liability Amortization Based` ⇒ use `Forward12MonthLiabilityAmortBased`; `PV Based` ⇒ use `Forward12MonthLiabilityPVBased` |

## Confidence

Observed for the switch; the PV-based formula itself is not available offline

---

Source: `docs/modules/accounting/rules.md`
