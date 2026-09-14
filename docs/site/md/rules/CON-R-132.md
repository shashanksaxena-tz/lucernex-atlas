# CON-R-132 — 11. Typing and integrity rules for the rebuild (Constitution §4.4)

*Contracts & Leases · Observed*

**Migrating PaymentTransaction: parse AmountInvoiced and AmountReceived to BigDecimal and reconcile them against InvoiceAmount and PaymentReceipt.ReceivedAmount.**

Migrating PaymentTransaction: parse AmountInvoiced and AmountReceived to BigDecimal and reconcile them against InvoiceAmount and PaymentReceipt.ReceivedAmount.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Migrating `PaymentTransaction` |
| Stated as | `AmountInvoiced(Text)`, `AmountReceived(Text)` |
| Stated as | Two money fields on the central ledger are declared `Text` while their siblings are `Currency` |
| Stated as | Parse to `BigDecimal`; reconcile against `InvoiceAmount` and `PaymentReceipt.ReceivedAmount` |
| Stated as | Observed |

## What it constrains

[PaymentTransaction](../entities/PaymentTransaction.md), [PaymentReceipt](../entities/PaymentReceipt.md)

Columns named: `PaymentReceipt.ReceivedAmount`

---

Source: `docs/modules/contracts/rules.md`
