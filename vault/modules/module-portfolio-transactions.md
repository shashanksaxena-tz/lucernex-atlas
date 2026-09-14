---
title: Portfolio and transactions
tags: [module, portfolio, deal-pipeline]
evidence: Observed
---

**11 objects · 513 fields · rules `POR-R-001`…`POR-R-016`**

Two things bolted onto one object. [[Program]] — the menu's "Portfolio" — is both the container at
the top of the ownership hierarchy *and* the carrier of accounting policy. Beside it runs the
**pre-lease deal pipeline**, which happens before any [[Contract]] exists:

```
PotentialProject ("Site") → RETransaction → Scenario → Contract
```

Entities: [[Program]] · [[PotentialProject]] · [[RETransaction]] · [[Scenario]]

- [[Program]] is **180 fields** — larger than Scenario and PotentialProject combined — and resolves
  discount rate, thresholds, fiscal year and FX before [[Firm]] ([[rule-POR-R-001]]).
- Its two unique columns `SiteToProjectSetupLayoutID` and `ProjectToFacilitySetupLayoutID` **name the
  Site → Project → Facility promotion pipeline**, and only the second half has FK corroboration
  ([[rule-POR-R-012]]).
- **The pipeline is not reconstructible afterwards.** [[PotentialProject]] has zero inbound edges
  ([[rule-POR-R-011]]) and `Scenario.ContractID` is one-way ([[rule-POR-R-004]]).
- Four overlapping pipeline code tables, **no row values ever captured** ([[rule-POR-R-005]]).

Screens: [[screen-manage-portfolios]]

Rules: [[rules-portfolio-transactions]] ·
[`modules/portfolio-transactions/`](../../docs/modules/portfolio-transactions/README.md)
