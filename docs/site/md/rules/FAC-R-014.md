# FAC-R-014 — Property tax attaches only to the Parcel, never the Facility or the lease

*Facilities, Locations & Sites · Observed*

**Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: Observed (`../../mindmap/edges.json`).**

Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: Observed (`../../mindmap/edges.json`).

## What it constrains

[PropertyTaxAppeal](../entities/PropertyTaxAppeal.md), [PropertyTaxAppealAward](../entities/PropertyTaxAppealAward.md), [PropertyTaxAssessment](../entities/PropertyTaxAssessment.md), [PropertyTaxBill](../entities/PropertyTaxBill.md), [PropertyTaxDetail](../entities/PropertyTaxDetail.md), [PropertyTaxSummary](../entities/PropertyTaxSummary.md)

## Confidence

Observed (`../../mindmap/edges.json`)

---

Source: `docs/modules/facilities-locations/rules.md`
