# PLT-R-011 — Exchange rates are point-in-time captures, not a live feed

*Platform & Tenancy · Derived*

**The rate used for a calculation is whatever was captured effective as of a given date, not a re-derived live lookup — supports historical reporting without recomputation.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | A multi-currency Contract calculation |
| What it reads | `ExchangeRate.ContractID`, `ConversionRate`, `EffectiveDate` |
| What it writes | The rate used for a calculation is whatever was captured effective as of a given date, not a re-derived live lookup — supports historical reporting without recomputation |

## What it constrains

[ExchangeRate](../entities/ExchangeRate.md)

Columns named: `ExchangeRate.ContractID`

## Confidence

Derived — field shape only, no live capture. ## Audit

---

Source: `docs/modules/platform-tenancy/rules.md`
