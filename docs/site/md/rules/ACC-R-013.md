# ACC-R-013 — Test locking

*Lease Accounting & Payments · Observed*

**a locked test cannot be modified and cannot be deleted. Superseding is by creating a new `ContractFinancialTest` row.**

Locked tests are immutable and undeletable.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | user sets `IsLocked = true` |
| The test | a locked test cannot be modified and cannot be deleted. Superseding is by creating a new `ContractFinancialTest` row |
| What it writes | immutable test record |

## The wording it rests on

> Locking the test ensures that the test cannot be modified. You cannot delete a classification test once it has been locked, but you can create another test as necessary.

## What it constrains

[ContractFinancialTest](../entities/ContractFinancialTest.md)

## Confidence

Observed — "Locking the test ensures that the test cannot be modified. You cannot delete a classification test once it has been locked, but you can create another test as necessary."

---

Source: `docs/modules/accounting/rules.md`
