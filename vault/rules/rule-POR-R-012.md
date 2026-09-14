---
title: "POR-R-012 — Program names a two-step conversion"
tags: [rule, portfolio-transactions]
evidence: Derived
---

**`POR-R-012`** · [[module-portfolio-transactions]] · **Derived**

`SiteToProjectSetupLayoutID` and `ProjectToFacilitySetupLayoutID` are **the only fields in the entire
7,421-field schema containing `ToProject` or `ToFacility`**. They name a Site → Project → Facility
pipeline.

**Only the second step has FK corroboration** (`Project.FacilityID`). *(Derived, plus Inferred.)*

See [[rules-portfolio-transactions]] for the full register.
