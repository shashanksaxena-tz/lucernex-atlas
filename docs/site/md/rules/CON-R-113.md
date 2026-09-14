# CON-R-113 — 9. Payment lifecycle

*Contracts & Leases · Observed*

**AP settles a payment: CheckNumber/CheckDate/CheckAmount/CodeCheckCurrencyTypeID are written back — check currency may differ from transaction currency with no FX rate field to reconcile the two.**

AP settles a payment: CheckNumber/CheckDate/CheckAmount/CodeCheckCurrencyTypeID are written back — check currency may differ from transaction currency with no FX rate field to reconcile the two.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | AP settles a payment |
| Stated as | `CheckNumber`, `CheckDate`, `CheckAmount`, `CodeCheckCurrencyTypeID` |
| Stated as | Settlement details written back. Check currency may differ from transaction currency, with no FX rate field on the transaction |
| Stated as | Settlement |
| Stated as | Observed |

---

Source: `docs/modules/contracts/rules.md`
