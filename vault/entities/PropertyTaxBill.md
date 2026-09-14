---
title: PropertyTaxBill
tags: [entity, property-tax, accounting]
evidence: Observed
---

**`property_tax_bill` · 32 fields · [[module-property-tax]]**

The tax bill, with early-payment discount fields. **The only object in the family reachable from the
payment engine** — the sole payable unit ([[rule-TAX-R-010]]), with [[PaymentTransaction]] and its
import twin the only two inbound cross-module edges.

`PropertyTaxDetail` beneath it is a **structured priced breakdown** (`TaxAmount`, `TaxRate`,
`CodeTaxTypeID`), not a notes field ([[rule-TAX-R-012]]) — the catalog description was wrong.

**And a won appeal never touches it** — see [[PropertyTaxAppeal]] and [[rule-TAX-R-011]].
