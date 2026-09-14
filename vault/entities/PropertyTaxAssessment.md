---
title: PropertyTaxAssessment
tags: [entity, property-tax]
evidence: Observed
---

**`property_tax_assessment` · 25 fields · [[module-property-tax]]**

The assessed land and improvement values for a [[Parcel]], at a date. Must belong to exactly one
[[PropertyTaxSummary]] ([[rule-TAX-R-001]]).

Everything downstream hangs off a *specific dated assessment*, never off the ongoing summary: a bill
is always issued against an assessed value ([[rule-TAX-R-002]]), and an appeal always contests one
specific assessment ([[rule-TAX-R-004]]).
