---
title: "RPT-R-020 — PageLayoutFilter is not the conditional-field store"
tags: [rule, reporting]
evidence: Observed
---

**`RPT-R-020`** · [[module-reporting]] · **Observed**

Filters are [[PageLayoutFilter]] rows. **[[conditional-field|Conditional fields]] are JSON blobs per
target on [[PageLayoutField]].**

**Two different mechanisms.** Confusing them would produce a wrong rebuild of both — and note
`PageLayoutFilter` has **zero rows** in BBW while `conditionalFieldsConfig` has 50.

*(Observed, plus Inferred for the separation of concerns.)*

See [[rules-reporting]] for the full register.
