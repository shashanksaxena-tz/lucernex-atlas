# PPL-R-004 — `Employer` is one table serving three business roles

*People & Parties · Observed*

**No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Any process that treats Vendor, Landlord, or Tenant-as-counterparty as separate entities |
| What it reads | `PaymentTransaction.VendorID` (type `Employer ID`), `LinkProjectEntityContact. Landlord_EmployerID`, `Employer.Is*Vendor` flags |
| The test | No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema |
| What it writes | All three business roles resolve to one `Employer` row. A rebuild should not create separate entities that then require manual synchronisation |

## What it constrains

[PaymentTransaction](../entities/PaymentTransaction.md), [Tenant](../entities/Tenant.md), [Employer](../entities/Employer.md)

Columns named: `PaymentTransaction.VendorID`

## Confidence

Observed — 009, this module's field export

---

Source: `docs/modules/people-parties/rules.md`
