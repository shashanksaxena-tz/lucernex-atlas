---
title: "Q-BBW-02 — Why is Capital Lease Test dropped from Equipment Contract?"
tags: [open-question, accounting, equipment]
evidence: Observed
status: open
---

[[equipment-contract|Equipment Contract]] keeps `ASC 842 Test` and **drops `Capital Lease Test`**.

Everything else dropped from the root is retail-property-specific — [[CoTenancy|co-tenancy]],
recoveries, [[PercentageRent|percentage rent]], [[Sales|sales]], the whole Accrual Info group. **This
one is not**, so the generic-versus-retail reading does not explain it.

### The likely answer

`Capital Lease Test` is the legacy **ASC 840** test — [[Contract]] still carries it as
`Test1Result`…`Test5bResult` — and equipment leases were plausibly only ever onboarded post-842. If so,
**ASG Edge+ can omit it for equipment too**, which is a real scope reduction.

*(Inferred. The two generations coexisting on [[Contract]] is Observed; the onboarding history is
not.)*

### How to settle it

Open both `Accounting Info` groups and compare, or ask whoever onboarded the equipment portfolio.

See [[finding-classification-polarity-inverted]] · [[ContractFinancialTest]]
