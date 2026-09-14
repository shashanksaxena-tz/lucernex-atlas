---
title: ContractTerm
tags: [entity, contracts]
evidence: Observed
---

**`contract_term` · 26 fields · [[module-contracts]]**

One renewal or extension option on a lease. Step 2 of the [[screen-contract-wizard|contract wizard]]
collects exactly this: option count, term type, term length and rentable area, in 10 fields.

`TermLength` on that wizard renders as `input[type=hidden]` — it is **computed during the wizard, not
entered**. And on a rendered contract, `Term Length` reads *"5 years 16 days"* — prose, derived, not
stored. See [[finding-computed-fields-render-as-prose]].

`ASG Lease Abstract - Contract Term` (102506) is one of the seven layouts unique to
[[tenant-bbw|BBW]] that serve the [[atlas-ai-abstraction|AI abstraction pipeline]].
