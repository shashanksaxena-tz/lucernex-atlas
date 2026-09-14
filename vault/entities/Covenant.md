---
title: Covenant
tags: [entity, contracts]
evidence: Observed
---

**`covenant` · 44 fields · [[module-contracts]]**

A lease covenant or compliance obligation, with a document reference. Referenced by **15** objects —
seventh in the schema's in-degree ranking, which is high for something that reads like a child record.

- Carries 7 [[firm-custom-field|`Firm_` columns]].
- Cloned wholesale at contract creation: step 3 of the [[screen-contract-wizard|wizard]] does nothing
  but pick a [[contract-template]] to copy covenant entries from.
- One of only **two non-form layouts** carrying a [[conditional-field]] rule
  (`ASG Contract Covenants` 98864 and `ASG Lease Abstract - Covenants` 102250), both driven by
  `Covenant.CodeCovenantTypeID`.
- `Covenant Status Code` (`2157`) is one of the four tables where `AI Abstracted` became
  delete-protected in build `26.09` — see [[atlas-ai-abstraction]].

[[SecurityDeposit]] links to it, which is not where you would look for it.
