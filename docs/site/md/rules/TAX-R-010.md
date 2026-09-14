# TAX-R-010 — Only PropertyTaxBill, not Summary/Assessment/Appeal/Award, is reachable from the cash-payment engine

*Property Tax · Observed*

**Input: `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID` — the family's only cross-module inbound edges. Effect: The bill is the sole payable, actionable unit in this family.**

Input: `PaymentTransaction.PropertyTaxBillID` / `PaymentTransactionFullImport.PropertyTaxBillID` — the family's only cross-module inbound edges. Effect: The bill is the sole payable, actionable unit in this family. Confidence: Observed, exhaustive (`../../mindmap/edges.json`).

## What it constrains

[PaymentTransaction](../entities/PaymentTransaction.md), [PaymentTransactionFullImport](../entities/PaymentTransactionFullImport.md)

Columns named: `PaymentTransaction.PropertyTaxBillID`, `PaymentTransactionFullImport.PropertyTaxBillID`

## Confidence

Observed, exhaustive (`../../mindmap/edges.json`)

---

Source: `docs/modules/property-tax/rules.md`
