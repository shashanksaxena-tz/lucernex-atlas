# CON-R-111 — 9. Payment lifecycle

*Contracts & Leases · Inferred*

**Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved.**

Eight-segment coding is applied: AccountNumber1..8 exists on PaymentTransaction/AccrualTransaction but not on CodeExpenseType; whether these are 8 segments of one account or 8 split-coding lines is unresolved.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Eight-segment coding is applied |
| Stated as | `AccountNumber1..8` |
| Stated as | Present on `PaymentTransaction` and `AccrualTransaction`, absent from `CodeExpenseType`; `Organization` carries `Account Number #1–8`. Whether these are 8 segments of one account or 8 split-coding lines is unresolved |
| Stated as | Account string |
| Stated as | Inferred — unresolved |

## What it constrains

[PaymentTransaction](../entities/PaymentTransaction.md), [AccrualTransaction](../entities/AccrualTransaction.md), [CodeExpenseType](../entities/CodeExpenseType.md), [Organization](../entities/Organization.md)

---

Source: `docs/modules/contracts/rules.md`
