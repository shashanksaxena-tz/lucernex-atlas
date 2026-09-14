# ACC-R-015 — Auto-computation marker

*Lease Accounting & Payments · Observed*

**`ContractFinancialTest.AutoComputed := true`.**

Set when the system ran the test rather than a user. The trigger is unknown.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | the system runs the test without user entry |
| What it writes | `ContractFinancialTest.AutoComputed := true` |

## The wording it rests on

> This field will have a true value if the ASC 842 test was computed automatically by the system.

## Confidence

Observed — "This field will have a true value if the ASC 842 test was computed automatically by the system." The conditions under which the system auto-runs are not documented

---

Source: `docs/modules/accounting/rules.md`
