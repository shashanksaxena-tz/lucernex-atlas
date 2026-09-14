# CON-R-115 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**An invoice line is matched to a payment: LinkLandlordInvPaymentTxn allocates AllocationAmount/AllocationDate between LandlordInvoiceItemID and PaymentTransactionID.**

An invoice line is matched to a payment: LinkLandlordInvPaymentTxn allocates AllocationAmount/AllocationDate between LandlordInvoiceItemID and PaymentTransactionID.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | An invoice line is matched to a payment |
| Stated as | `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`, `.PaymentTransactionID`, `.AllocationAmount`, `.AllocationDate` |
| Stated as | Many-to-many allocation |
| Stated as | Match |
| Stated as | Observed |

## What it constrains

[LinkLandlordInvPaymentTxn](../entities/LinkLandlordInvPaymentTxn.md)

Columns named: `LinkLandlordInvPaymentTxn.LandlordInvoiceItemID`

---

Source: `docs/modules/contracts/rules.md`
