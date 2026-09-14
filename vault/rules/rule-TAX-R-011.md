---
title: "TAX-R-011 — A won appeal is reconciled nowhere"
tags: [rule, property-tax]
evidence: Derived
---

**`TAX-R-011`** · [[module-property-tax]] · **Derived**

> **No FK connects [[PropertyTaxAppeal]] or its award back to [[PropertyTaxBill]] or
> `PropertyTaxDetail`.**

If a bill has been issued and the appeal then succeeds, the product has **no modelled path** from the
reduction to the bill. A real gap, and one ASG Edge+ would have to close deliberately.

See [[rules-property-tax]] for the full register.
