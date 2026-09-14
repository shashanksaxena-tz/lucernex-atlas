# ACC-R-010 — Test 5: specialised asset

*Lease Accounting & Payments · Observed*

**true ⇒ Fail; false ⇒ Pass.**

A specialised asset = Fail = finance lease.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | classification test run |
| What it reads | `IsAssetTooSpecializedForLessor` |
| The test | true ⇒ Fail; false ⇒ Pass |
| What it writes | `Test5Result` |

## Rules it cites

[ACC-R-005](ACC-R-005.md)

## Confidence

Observed / Derived as ACC-R-005

---

Source: `docs/modules/accounting/rules.md`
