# PPL-R-006 — The per-entity contact roster and the per-entity vendor list are separate, differently-shaped joins

*People & Parties · Observed*

**Contacts get a typed, richer roster entry; approved vendors get a bare membership list with no role classification at all.**

## Stated for a rule engine

|  |  |
|---|---|
| When it fires | Listing "who is associated with this entity." |
| What it reads | `LinkProjectEntityContact` (12 fields, classified by `CodeContactTypeID`, carries a parallel `Landlord_*` pair) vs. `LinkProjectEntityVendor` (4 fields, unclassified — just `ProjectEntityID` + `VendorID`) |
| What it writes | Contacts get a typed, richer roster entry; approved vendors get a bare membership list with no role classification at all |

## The wording it rests on

> who is associated with this entity.

## What it constrains

[LinkProjectEntityContact](../entities/LinkProjectEntityContact.md), [LinkProjectEntityVendor](../entities/LinkProjectEntityVendor.md)

## Confidence

Observed, this module's field export. ## Audit and identity load

---

Source: `docs/modules/people-parties/rules.md`
