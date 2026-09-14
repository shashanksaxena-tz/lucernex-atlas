# TAX-R-012 — `PropertyTaxDetail` is a structured, priced breakdown line, not a notes field

*Property Tax · Inferred*

**Input: `TaxAmount` (`sTYPE_MONEY`), `TaxRate` (`sTYPE_PERCENTAGE`), `CodeTaxTypeID`, `RateFlag` — four substantive fields, plus one genuinely free-form `Notes` field among fifteen total. Effect: A rebuild that models this object as a notes/comment record (per `../../data-fields/INDEX.md`'s inferred….**

Input: `TaxAmount` (`sTYPE_MONEY`), `TaxRate` (`sTYPE_PERCENTAGE`), `CodeTaxTypeID`, `RateFlag` — four substantive fields, plus one genuinely free-form `Notes` field among fifteen total. Effect: A rebuild that models this object as a notes/comment record (per `../../data-fields/INDEX.md`'s inferred one-liner) will lose the actual per-tax-type amount/rate breakdown a bill is composed of. Confidence: Derived, direct field-list read — see `data-model.md` for the correction in full.

## Confidence

Derived, direct field-list read — see `data-model.md` for the correction in full

---

Source: `docs/modules/property-tax/rules.md`
