# AST-R-015 — The parts catalog carries no per-location stock

*Assets, Equipment & Maintenance · Derived*

**Input: `Part.QuantityOnHand`, `.QuantityOnOrder`, `.ParLevel`, `.OrderToLevel` — single counters on the catalog record, with no `FacilityID`/warehouse column anywhere in this module. Effect: A tenant with parts stocked at multiple locations has one firm-wide count per part, not one per location.**

Input: `Part.QuantityOnHand`, `.QuantityOnOrder`, `.ParLevel`, `.OrderToLevel` — single counters on the catalog record, with no `FacilityID`/warehouse column anywhere in this module. Effect: A tenant with parts stocked at multiple locations has one firm-wide count per part, not one per location. Confidence: Derived (exhaustive field-list read, `../../data-fields/part.md`).

## What it constrains

[Part](../entities/Part.md)

Columns named: `Part.QuantityOnHand`

## Confidence

Derived (exhaustive field-list read, `../../data-fields/part.md`)

---

Source: `docs/modules/assets-equipment/rules.md`
