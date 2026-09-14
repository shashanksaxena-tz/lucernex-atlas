# CON-R-097 — Grid structure and variances

*Contracts & Leases · Derived*

**Escrow is trued up: reconcile the current escrow payment, propose a new estimate, and spread any shortfall over CatchUpNumberOfMonths.**

Escrow is trued up: reconcile the current escrow payment, propose a new estimate, and spread any shortfall over CatchUpNumberOfMonths.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Escrow is trued up |
| Stated as | `CurrentEscrowPayment`, `EscalationPercentage`, `NewEscalationPayment`, `ProposedEscalationPayment`, `CatchUpNumberOfMonths`, `CatchUpPaymentAmount`, `ProposedCatchUpPaymentAmount`, `UPDATE_ESCROW` |
| Stated as | Reconcile, propose a new estimate, spread the shortfall over N months |
| Stated as | New escrow + catch-up |
| Stated as | Derived |

---

Source: `docs/modules/contracts/rules.md`
