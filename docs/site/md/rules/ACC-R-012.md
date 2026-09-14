# ACC-R-012 — Accounting method override

*Lease Accounting & Payments · Derived*

**if populated, the override supersedes the computed `CodeAccountingMethodID`.**

An 'Accounting Type Override' on the test, and a second override on the asset, can supersede the computed verdict. Precedence between the two is undocumented.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | after ACC-R-011 |
| What it reads | `ContractFinancialTest.CodeAcctMethodOverrideID` ("Accounting Type Override"); `Asset.CodeAccountingMethodOverrideID` |
| The test | if populated, the override supersedes the computed `CodeAccountingMethodID` |
| What it writes | the accounting method used by the schedule |

## The wording it rests on

> ); `Asset.CodeAccountingMethodOverrideID`. - Condition: if populated, the override supersedes the computed `CodeAccountingMethodID`. - Output: the accounting method used by the schedule. - Confidence: Derived — the field is labelled

## What it constrains

[ContractFinancialTest](../entities/ContractFinancialTest.md), [Asset](../entities/Asset.md)

Columns named: `ContractFinancialTest.CodeAcctMethodOverrideID`, `Asset.CodeAccountingMethodOverrideID`

## Rules it cites

[ACC-R-011](ACC-R-011.md)

## Confidence

Derived — the field is labelled "Override" and its definition is "Select the accounting method you want to use from this field", but the precedence is not stated

---

Source: `docs/modules/accounting/rules.md`
