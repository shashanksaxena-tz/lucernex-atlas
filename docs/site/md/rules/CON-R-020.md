# CON-R-020 — 2. Contract identity and hierarchy

*Contracts & Leases · Derived*

**Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposit.PartyID.**

Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposit.PartyID.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | Resolving a contract's vendors |
| Stated as | `PaymentTransaction.VendorID`, `ExpenseSetup.VendorID`, `ExpenseVendorAllocation.VendorID`, `ScheduledOffset.VendorID`, `LandlordInvoice.EmployerID`, `SecurityDeposit.PartyID` |
| Stated as | `Contract` has no vendor FK; the set is derived from children |
| Stated as | Derived vendor set |
| Stated as | Observed |

## What it constrains

[PaymentTransaction](../entities/PaymentTransaction.md), [ExpenseSetup](../entities/ExpenseSetup.md), [ExpenseVendorAllocation](../entities/ExpenseVendorAllocation.md), [ScheduledOffset](../entities/ScheduledOffset.md), [LandlordInvoice](../entities/LandlordInvoice.md), [SecurityDeposit](../entities/SecurityDeposit.md), [Contract](../entities/Contract.md)

Columns named: `PaymentTransaction.VendorID`, `ExpenseSetup.VendorID`, `ExpenseVendorAllocation.VendorID`, `ScheduledOffset.VendorID`, `LandlordInvoice.EmployerID`, `SecurityDeposit.PartyID`

---

Source: `docs/modules/contracts/rules.md`
