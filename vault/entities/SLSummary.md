---
title: SLSummary
tags: [entity, accounting, core]
evidence: Observed
---

**`s_l_summary` · 134 fields · [[module-accounting]]**

The straight-line rent summary, one per contract per schedule — and **the object on which the three
accounting standards are one engine**. Three mutually exclusive flags (`IsSLSchedule`,
`IsASC842Schedule`, `IsIFRS16Schedule`) record which standard generated the schedule.
See [[one-engine-three-standards]].

- `InitialLiabilityBalance = Σ PVOfPeriodCashAmount` over every period ([[rule-ACC-R-031]]).
- **The initial *asset* balance formula is not documented anywhere.** The components exist; the
  arithmetic does not. [[rule-ACC-R-033]] says plainly: do not code it from the schema.
- It carries `NeedsRecalculation`, set by changing the schedule type on Assumptions, Covenants or
  Recurring Expenses ([[rule-ACC-R-020]]) — a staleness flag [[Contract]]'s 120 rollup fields
  conspicuously lack ([[rule-CON-R-026]]).
- Carries a nullable `AssetID` — part of [[finding-accounting-runs-per-asset]].
- Has a discount-rate override, which may be the only path by which a rate reaches the engine at all
  ([[finding-discount-rate-table-empty]]).

`ASG ASC 842 Schedule` (98859) and `ASG SL Summary` (98873) declare **the same primary table** — the
standard is a *layout* distinction here, not a data one.

Approval is irreversible ([[finding-schedules-are-approved-not-published]]).

See [[SLPeriod]] · [[ContractFinancialTest]]
