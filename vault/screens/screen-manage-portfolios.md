---
title: "Manage Portfolios / Capital Programs"
tags: [screen, administration,master-data,portfolio]
evidence: Observed
---

`/en/admin/ProgramEdit.jsp`

![The Portfolio record — 180 fields, and far more consequential than a container ought to be.](../assets/screenshots/bbw-admin/29-manage-portfolios-capital-programs.jpg)
`docs/assets/screenshots/bbw-admin/29-manage-portfolios-capital-programs.jpg` · `af-admin/30-manage-portfolios-capital-programs.jpg`

**"Portfolio" is [[Program]]** — a 180-field [[subtype-root]] that carries **accounting policy**, not
just membership.

- Discount rate, thresholds, fiscal year and FX resolve here **before** [[Firm]]
  ([[rule-POR-R-001]]).
- **14 FX rate-type selectors**, **3 independent amortisation switches** ([[rule-ACC-R-056]]), 2 ASC
  842 thresholds.
- **18 `sTYPE_PAGE_LAYOUT` columns** — more than [[Firm]]'s 11 — including the two that name the
  Site → Project → Facility pipeline ([[rule-POR-R-012]]).

**The name trap**: a separate menu structure genuinely named `Program` (id 3851) renders in neither
tenant, because its rows are typed `"Portfolio"`. See [[finding-root-renders-iff-record-exists]].

**Only the [[screen-manage-company|Firm]] layout screen has ever been opened** — this record's 18
layout columns are unexamined.

All screens: [[map-of-screens]] · caveats: [[caveat-viewport]] · [[caveat-one-equipment-contract]]
