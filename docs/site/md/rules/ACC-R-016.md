# ACC-R-016 — Term-length sourcing

*Lease Accounting & Payments · Observed*

**- `TermLength = ExpireDate − CommenceDate` (the contractual term); - `LikelyTermLength` = length through the last term marked Likely on `Abstract Info > Terms`; - `LastLikelyOptionDate` = end date of the last likely term; - `TestTermLength` = length of the term selected for the test.**

Three term lengths, three different definitions.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | classification test run |
| What it reads | `Contract.CommenceDate`, `Contract.ExpireDate`, `ContractTerm` rows marked Likely |
| What it computes | - `TermLength = ExpireDate − CommenceDate` (the contractual term); - `LikelyTermLength` = length through the last term marked Likely on `Abstract Info > Terms`; - `LastLikelyOptionDate` = end date of the last likely term; - `TestTermLength` = length of the term selected for the test |
| What it writes | the three term-length fields |

## What it constrains

[Contract](../entities/Contract.md), [ContractTerm](../entities/ContractTerm.md)

Columns named: `Contract.CommenceDate`, `Contract.ExpireDate`

## Confidence

Observed for each definition; ⚠ Inferred that `TestTermLength` defaults to `LikelyTermLength` — the "Test Begin Date"/"Test End Date" fields its definition names do not exist in the schema

---

Source: `docs/modules/accounting/rules.md`
