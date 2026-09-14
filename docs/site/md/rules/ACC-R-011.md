# ACC-R-011 — ⚠ Final classification (inverted polarity)

*Lease Accounting & Payments · Observed*

**any result = Fail ⇒ `Finance`; all five = Pass ⇒ `Operating`.**

Any fail means finance; all five passes means operating.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | after ACC-R-005…010 |
| What it reads | `Test1Result` … `Test5Result` |
| The test | any result = Fail ⇒ `Finance`; all five = Pass ⇒ `Operating` |
| What it writes | `ContractFinancialTest.FinalResult` (`sTYPE_TEXT`); `CodeAccountingMethodID` set to the matching Accounting Method code |

## What it constrains

[ContractFinancialTest](../entities/ContractFinancialTest.md)

Columns named: `ContractFinancialTest.FinalResult`

## Rules it cites

[ACC-R-005](ACC-R-005.md)

## Confidence

Observed, stated on all five test fields. ⚠ Note the polarity is the reverse of the intuitive reading — "passing" the tests means the lease is operating

---

Source: `docs/modules/accounting/rules.md`
