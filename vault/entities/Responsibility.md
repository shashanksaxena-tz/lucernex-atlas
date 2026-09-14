---
title: Responsibility
tags: [entity, contracts]
evidence: Observed
---

**`responsibility` · 32 fields · [[module-contracts]]**

Which party owes which cost category, with cap limits — the allocation table underneath the
[[cam-waterfall]].

Like [[Covenant]], it is **cloned from a [[contract-template]]** at creation: step 4 of the
[[screen-contract-wizard|wizard]] exposes exactly one control,
`Responsibility_ContractWizardTemplate`.

On [[Facility]], `Responsibilities` is the one screen served by `LeaseMaintenanceEdit.jsp` — the sole
route through that renderer in the entire 105-screen tree.
