# ACC-R-004 — Discount rate applicability scoping

*Lease Accounting & Payments · Observed*

**a blank `CodeAccountingMethodID` matches both Finance and Operating. `MinSchedMons`/`MaxSchedMons` bound the schedule length in months for which the rate applies.**

A blank accounting method matches both; the month band bounds the schedule lengths the rate applies to.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | evaluating candidate `DiscountRate` rows |
| What it reads | `DiscountRate.CodeAccountingMethodID`, `.CodeContractUseID`, `.CountryID`/`.CountryIDList`/`.StateProvinceIDList`, `.MinSchedMons`, `.MaxSchedMons`, `.EffectiveThroughDate` |
| The test | a blank `CodeAccountingMethodID` matches both Finance and Operating. `MinSchedMons`/`MaxSchedMons` bound the schedule length in months for which the rate applies |
| What it writes | the matching rate |

## The wording it rests on

> If you leave the field blank, the discount rate will apply to both Finance and Operating.

## What it constrains

[DiscountRate](../entities/DiscountRate.md), [ContractFinancialTest](../entities/ContractFinancialTest.md)

Columns named: `DiscountRate.CodeAccountingMethodID`

## Confidence

Observed for the blank-matches-both rule ("If you leave the field blank, the discount rate will apply to both Finance and Operating."); Inferred for the precedence order when several rows match. --- ## B. ASC 842 classification (`ContractFinancialTest`)

---

Source: `docs/modules/accounting/rules.md`
