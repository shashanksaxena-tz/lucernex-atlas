# ACC-R-017 — Accounting date window

*Lease Accounting & Payments · Observed*

**`Topic842BeginDate = max(adoption date, PossessionBeginDate)`; `Topic842EndDate` = end of accounting including likely options.**

Begin date is the later of the firm's adoption date and possession; end date includes likely options.

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | classification test creation |
| What it reads | firm's ASC 842 adoption date; `Contract.PossessionBeginDate`; likely options |
| What it computes | `Topic842BeginDate = max(adoption date, PossessionBeginDate)`; `Topic842EndDate` = end of accounting including likely options |
| What it writes | `Topic842BeginDate`, `Topic842EndDate` |

## The wording it rests on

> This date is the date your organization is adopting ASC 842, or the Possession Begin Date, whichever is later.

## What it constrains

[Contract](../entities/Contract.md)

Columns named: `Contract.PossessionBeginDate`

## Confidence

Observed — "This date is the date your organization is adopting ASC 842, or the Possession Begin Date, whichever is later."

---

Source: `docs/modules/accounting/rules.md`
