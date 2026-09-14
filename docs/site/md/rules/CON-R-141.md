# CON-R-141 — 12. Contract status and lifecycle

*Contracts & Leases · Derived*

**Determining a contract's lifecycle stage: the stage is derived from date fields (ActualStartDate/OpenYear, StatusEffectiveDate, PossessionBeginDate/EndDate, PaymentsBeginDate/EndDate, ExpireDate/ActualEndDate/IsDead/Inactive) rather than stored directly in any enum.**

Determining a contract's lifecycle stage: the stage is derived from date fields (ActualStartDate/OpenYear, StatusEffectiveDate, PossessionBeginDate/EndDate, PaymentsBeginDate/EndDate, ExpireDate/ActualEndDate/IsDead/Inactive) rather than stored directly in any enum.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Determining a contract's lifecycle stage |
| Stated as | `ActualStartDate`/`OpenYear` (Open), `StatusEffectiveDate` (Active), `PossessionBeginDate`/`PossessionEndDate` (Possession), `PaymentsBeginDate`/`PaymentsEndDate` (Paying Rent), `ExpireDate`/`ActualEndDate`/`IsDead`/`Inactive` (Closed) |
| Stated as | Lx derives stage from dates rather than storing it. No enum holds BRD-24's five stages |
| Stated as | Derived stage |
| Stated as | Derived |

---

Source: `docs/modules/contracts/rules.md`
