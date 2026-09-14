---
title: ContractAmendment
tags: [entity, contracts]
evidence: Observed
---

**`contract_amendment` · 20 fields · [[module-contracts]]**

The formal amendment that versions the whole lease. Referenced by **13** objects — which is the
interesting part: `AmendmentID` is half of the discriminator that tells a **clause** layer apart from
a **schedule** layer in the [[setup-schedule-transaction]] pattern ([[rule-CON-R-001]]).

So an amendment is not a side note on the contract; it is the versioning axis the financial clauses
hang from.

See [[Contract]] · [[Covenant]] · [[ContractTerm]]
