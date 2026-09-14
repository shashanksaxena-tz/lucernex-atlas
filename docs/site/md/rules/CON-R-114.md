# CON-R-114 — 9. Payment lifecycle

*Contracts & Leases · Derived*

**A landlord invoice is imported: IMPORT_INVOICE extracts VendorName/Address/TaxID and CustomerName/Address/TaxID as text, kept alongside the resolved EmployerID.**

A landlord invoice is imported: IMPORT_INVOICE extracts VendorName/Address/TaxID and CustomerName/Address/TaxID as text, kept alongside the resolved EmployerID.

## Stated for a rule engine

|  |  |
|---|---|
| Stated as | A landlord invoice is imported |
| Stated as | `IMPORT_INVOICE`, `LandlordInvoice.VendorName/Address/TaxID`, `CustomerName/Address/TaxID` |
| Stated as | Extracted values are kept as `Text` alongside the resolved `EmployerID` FK |
| Stated as | Invoice + extraction record |
| Stated as | Derived |

---

Source: `docs/modules/contracts/rules.md`
