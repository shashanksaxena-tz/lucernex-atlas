---
title: Jurisdiction
tags: [entity, platform-tenancy, reference-data, property-tax]
evidence: Observed
---

**`jurisdiction` · 11 fields · [[module-platform-tenancy]]**

The tax or legal jurisdiction. Sixth in in-degree — **16 objects, 17 columns**.

**Its FK type is named `County ID`.** That is one of the four misleading type names in the system, and
it matters here more than elsewhere: a rebuild reading the type name would model a county and get a
jurisdiction. See [[type-system]] and [[StateProvinceCountry]].

Naturally central to [[module-property-tax]], where the assessment and bill both resolve against it.
