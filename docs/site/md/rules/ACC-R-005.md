# ACC-R-005 — Test 1: title transfer

*Lease Accounting & Payments · Observed*

**`DoesTitleRevertToTenant = true` ⇒ Fail; false ⇒ Pass.**

Title reverts to the tenant = Fail = finance lease.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | classification test run |
| What it reads | `ContractFinancialTest.DoesTitleRevertToTenant` (`sTYPE_CHECKBOX`) |
| The test | `DoesTitleRevertToTenant = true` ⇒ Fail; false ⇒ Pass |
| What it writes | `Test1Result` (`sTYPE_PASS_FAIL`) |

## The wording it rests on

> If you 'fail' at least one of the five tests, the lease will be classified as a Finance lease.

## What it constrains

[ContractFinancialTest](../entities/ContractFinancialTest.md)

Columns named: `ContractFinancialTest.DoesTitleRevertToTenant`

## Confidence

Observed that this checkbox is Test 1; Derived for the polarity, from the global rule "If you 'fail' at least one of the five tests, the lease will be classified as a Finance lease."

---

Source: `docs/modules/accounting/rules.md`
