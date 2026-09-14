---
title: ContractFinancialTest
tags: [entity, accounting, core]
evidence: Observed
---

**`contract_financial_test` · 93 fields · [[module-accounting]]**

Lease **classification** — the five ASC 842 / IFRS 16 tests and the present-value calculation — kept
as a separate 93-field record rather than as fields on the [[Contract]].

Two rules dominate it:

- **[[finding-classification-polarity-inverted]]** — any test *Fail* produces a **Finance** lease; all
  five *Pass* produces Operating ([[rule-ACC-R-011]]). The polarity is the opposite of the intuition,
  and getting it backwards inverts every classification in a portfolio.
- **A locked test cannot be modified or deleted.** Supersede it by creating a new row
  ([[rule-ACC-R-013]]).

Test 4 is the fair-value test: fail if `InitialLiabilityBalance > FairValueOfAsset ×
PortionControlled × FairValueThreshold` (usually 90%) — *which* liability balance is unresolved
([[rule-ACC-R-009]]).

It carries a **nullable FK straight to [[Asset]]**, which is one third of the evidence that
[[finding-accounting-runs-per-asset|the engine runs per equipment asset, not only per lease]].

Rendered as a *list* screen (`ASC 842 Test`), while the older `Capital Lease Test` is a *detail* form —
because the ASC 840 test is one record per contract and the ASC 842 test produces many rows.

See [[one-engine-three-standards]] · [[SLSummary]]
