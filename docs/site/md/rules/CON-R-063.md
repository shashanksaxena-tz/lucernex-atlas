# CON-R-063 — 5. Percentage rent

*Contracts & Leases · Derived*

**Percentage rent is billed: a PaymentTransaction carrying PercentageRentID is generated for PRPRentDue.**

Percentage rent is billed: a PaymentTransaction carrying PercentageRentID is generated for PRPRentDue.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Percentage rent is billed |
| Stated as | `PRPRentDue`, `PercentageRent.CodeExpenseTypeID`/`CodeExpenseGroupID` |
| Stated as | A `PaymentTransaction` carrying `PercentageRentID` is generated |
| Stated as | L2 row |
| Stated as | Derived |

## What it constrains

[PercentageRent](../entities/PercentageRent.md), [PaymentTransaction](../entities/PaymentTransaction.md)

Columns named: `PercentageRent.CodeExpenseTypeID`

---

Source: `docs/modules/contracts/rules.md`
