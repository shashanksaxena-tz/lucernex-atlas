---
title: Allowance
tags: [entity, contracts]
evidence: Observed
---

**`allowance` · 23 fields · [[module-contracts]]**

A tenant-improvement or landlord allowance. Its child `AllowanceTransaction` carries 6
[[firm-custom-field|`Firm_` columns]].

It is the worked example behind [[required-ness]]'s central point: *"you must pick a parent Contract
when creating an Allowance"* is an obligation the [[data-field-catalog|catalog]] expresses and
`NOT NULL` cannot. `ContractID` is catalog-required and schema-nullable on **34 tables**, of which
this is one.

Survives into [[equipment-contract|Equipment Contract]].
