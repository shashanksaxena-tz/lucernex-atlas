---
title: Lease classification polarity is inverted
tags: [finding, accounting, trap]
evidence: Observed
---

> **Any test *Fail* ⇒ Finance lease. All five *Pass* ⇒ Operating lease.** ([[rule-ACC-R-011]])

The polarity is the opposite of the intuition the word "pass" invites, and **getting it backwards
inverts every lease classification in a portfolio** — which changes the balance sheet, not a report
column.

The five tests live on [[ContractFinancialTest]], a separate 93-field record rather than fields on the
[[Contract]]. Test 4 is the fair-value test: fail if
`InitialLiabilityBalance > FairValueOfAsset × PortionControlled × FairValueThreshold` (usually 90%) —
and **which liability balance is meant is unresolved** ([[rule-ACC-R-009]]).

Two related rules travel with it:

- **A locked test cannot be modified or deleted.** Supersede by creating a new row
  ([[rule-ACC-R-013]]) — so classification history is append-only.
- [[Contract]] **still carries the older ASC 840 "Cap Lease Test"** as `Test1Result`…`Test5bResult`,
  alongside the newer record. Two generations of the same idea coexist, and
  [[q-bbw-02-capital-lease-test]] asks why one of them is dropped for equipment.

See [[one-engine-three-standards]] · [[module-accounting]]
