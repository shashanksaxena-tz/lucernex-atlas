---
title: Contract templates
tags: [concept, contracts, gap]
evidence: Observed
---

Steps 3 and 4 of the [[screen-contract-wizard|contract creation wizard]] are **not data entry**. Both
read *"Select the Contract template below to clone its covenant/Responsibility entries
automatically"*, and each exposes exactly one control — `Covenant_ContractWizardTemplate` and
`Responsibility_ContractWizardTemplate`.

**Contract templates are a first-class creation mechanism, and they are documented nowhere.** No
`ContractTemplate` object exists in the 223-object census. What backs them is
[[q-bbw-09-contract-templates]].

This matters for a rebuild because it changes what "create a contract" means: it is not filling a
form, it is selecting a precedent and cloning its [[Covenant]] and [[Responsibility]] children.

Note also the wizard uses templates for exactly these two child collections and not for
[[ContractTerm|terms]], [[KeyDate|key dates]] or [[Insurance|insurance]] — which is either a
deliberate scope or an artefact of what ASG configured.

Source: [`tenants/bbw-vs-american-freight.md` §10](../../docs/tenants/bbw-vs-american-freight.md)
