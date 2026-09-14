# TAX-R-006 — Every object in the family also carries a direct Parcel pointer, independent of the chain

*Property Tax · Observed*

**Input: `ParcelID` on all six objects, `Required = Yes` on each. Effect: Every level is independently queryable by Parcel without walking the roll-up chain to `PropertyTaxSummary`;.**

Input: `ParcelID` on all six objects, `Required = Yes` on each. Effect: Every level is independently queryable by Parcel without walking the roll-up chain to `PropertyTaxSummary`; nothing in the schema enforces that this direct value agrees with the `ParcelID` reachable by walking the chain. Confidence: Observed (field presence, all six Data Fields catalogs); the consistency guarantee is Inferred/unconfirmed — see `data-model.md`.

## What it constrains

[PropertyTaxSummary](../entities/PropertyTaxSummary.md)

## Confidence

Observed (field presence, all six Data Fields catalogs); the consistency guarantee is Inferred/unconfirmed — see `data-model.md`

---

Source: `docs/modules/property-tax/rules.md`
