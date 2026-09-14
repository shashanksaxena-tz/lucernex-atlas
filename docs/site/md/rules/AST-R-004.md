# AST-R-004 — Asset carries its own ASC 842/IFRS 16 classification overlay, parallel to Contract's

*Assets, Equipment & Maintenance · Observed*

**Input: The 13-field block enumerated in `data-model.md` and detailed in `equipment-leases.md`. Effect: Equipment-lease classification can run per asset, using asset-supplied inputs, rather than only at the contract level.**

Input: The 13-field block enumerated in `data-model.md` and detailed in `equipment-leases.md`. Effect: Equipment-lease classification can run per asset, using asset-supplied inputs, rather than only at the contract level. Confidence: Observed (field presence); the precedence between this overlay and `ContractFinancialTest`'s equivalent fields is Inferred and unresolved — see `equipment-leases.md` open questions.

## What it constrains

[ContractFinancialTest](../entities/ContractFinancialTest.md)

## Confidence

Observed (field presence); the precedence between this overlay and `ContractFinancialTest`'s equivalent fields is Inferred and unresolved — see `equipment-leases.md` open questions

---

Source: `docs/modules/assets-equipment/rules.md`
