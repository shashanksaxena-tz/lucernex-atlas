# CON-R-133 — 11. Typing and integrity rules for the rebuild (Constitution §4.4)

*Contracts & Leases · Observed*

**Migrating LandlordInvoiceItem: money, date and boolean are all stored as text on this reconciliation grid; replace the seven PayTrans* mirror fields with a join.**

Migrating LandlordInvoiceItem: money, date and boolean are all stored as text on this reconciliation grid; replace the seven PayTrans* mirror fields with a join.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Migrating `LandlordInvoiceItem` |
| Stated as | `PayTransTotalAmount(Text)`, `LinkAmountAllocated(Text)`, `PayTransEffectiveDate(Text)`, `PayTransIsReceivable(Text)` |
| Stated as | Money, date and boolean all stored as text on a reconciliation grid |
| Stated as | Replace the seven `PayTrans*` mirror fields with a join |
| Stated as | Observed |

## What it constrains

[LandlordInvoiceItem](../entities/LandlordInvoiceItem.md)

---

Source: `docs/modules/contracts/rules.md`
