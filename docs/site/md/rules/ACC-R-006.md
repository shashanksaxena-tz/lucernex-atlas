# ACC-R-006 — Test 2: purchase option reasonably certain to be exercised

*Lease Accounting & Payments · Observed*

**true ⇒ Fail; false ⇒ Pass.**

A bargain purchase option = Fail = finance lease.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | classification test run |
| What it reads | `ContractFinancialTest.ContainsBargainPurchaseOption` |
| The test | true ⇒ Fail; false ⇒ Pass |
| What it writes | `Test2Result` |

## What it constrains

[ContractFinancialTest](../entities/ContractFinancialTest.md)

Columns named: `ContractFinancialTest.ContainsBargainPurchaseOption`

## Rules it cites

[ACC-R-005](ACC-R-005.md)

## Confidence

Observed / Derived as ACC-R-005

---

Source: `docs/modules/accounting/rules.md`
