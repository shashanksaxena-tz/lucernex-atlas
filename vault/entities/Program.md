---
title: Program
tags: [entity, portfolio, subtype-root]
evidence: Observed
---

**`program` · 180 fields · [[module-portfolio-transactions]]**

The Portfolio / capital-program container at the top of the ownership hierarchy — and **the navigation
root labelled `Portfolio` is this object**. Larger than [[Scenario]] (69) and [[PotentialProject]]
(108) combined.

It is where accounting *policy* lives, which is why it matters far beyond the portfolio screen:

- `Contract.ProgramID` resolves discount rate, thresholds, fiscal year and FX **before** falling back
  to [[Firm]] ([[rule-POR-R-001]]).
- **14 FX rate-type selectors**, **3 independent per-day/per-period amortisation switches** (asset,
  cash, expense — not one switch, [[rule-ACC-R-056]]), and 2 ASC 842 thresholds.
- **11 `<Subtype>SetupPageLayoutID` columns** overriding the tenant-wide [[Firm]] defaults per
  portfolio, plus 18 `sTYPE_PAGE_LAYOUT` columns in total — more than `Firm`'s 11.
- Two columns fit no subtype: **`SiteToProjectSetupLayoutID`** and **`ProjectToFacilitySetupLayoutID`**
  — the only fields in the entire 7,421-field schema containing `ToProject` or `ToFacility`. They name
  the Site → Project → Facility promotion pipeline ([[rule-POR-R-012]]).
- `OrgChartProgramID` is a self-reference — portfolios nest.

**The `Program` name trap.** A separate menu structure genuinely named `Program` (id `3851`) renders
in neither tenant, because its rows are typed `ProjectEntityTypeName = "Portfolio"`. See
[[subtype-root]] and [[finding-root-renders-iff-record-exists]].

Screens: [[screen-manage-portfolios]]
