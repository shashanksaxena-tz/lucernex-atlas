# CON-R-072 — 6. Alternate rent and offsets

*Contracts & Leases · Observed*

**A payment is generated under alternate rent: PreAltRentInvoiceAmount records what would have been invoiced without the concession.**

A payment is generated under alternate rent: PreAltRentInvoiceAmount records what would have been invoiced without the concession.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A payment is generated under alternate rent |
| Stated as | `PaymentTransaction.InAlternateRent`, `.AlternateRentScheduleID`, `.PreAltRentInvoiceAmount` |
| Stated as | Records what would have been invoiced without the concession |
| Stated as | Concession audit trail |
| Stated as | Observed |

## What it constrains

[PaymentTransaction](../entities/PaymentTransaction.md)

Columns named: `PaymentTransaction.InAlternateRent`

---

Source: `docs/modules/contracts/rules.md`
