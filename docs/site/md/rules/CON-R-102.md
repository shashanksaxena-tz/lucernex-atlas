# CON-R-102 — Line-item level

*Contracts & Leases · Inferred*

**A landlord statement is ingested: ExpenseRecoveryItemMapping maps a free-text statement line (InvoiceLineItemName, JSONConfigText) to a structured recovery item.**

A landlord statement is ingested: ExpenseRecoveryItemMapping maps a free-text statement line (InvoiceLineItemName, JSONConfigText) to a structured recovery item.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A landlord statement is ingested |
| Stated as | `ExpenseRecoveryItemMapping.InvoiceLineItemName`, `.DocumentID`, `.JSONConfigText` |
| Stated as | Maps a free-text statement line to a structured `ExpenseRecoveryItem` |
| Stated as | Item mapping |
| Stated as | Inferred |

## What it constrains

[ExpenseRecoveryItemMapping](../entities/ExpenseRecoveryItemMapping.md), [ExpenseRecoveryItem](../entities/ExpenseRecoveryItem.md)

Columns named: `ExpenseRecoveryItemMapping.InvoiceLineItemName`

---

Source: `docs/modules/contracts/rules.md`
