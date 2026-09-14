# FAC-R-002 — A Location has no reverse pointer to any Facility

*Facilities, Locations & Sites · Observed*

**Trigger: N/A (structural). Effect: A Location's field set contains no `FacilityID`-typed column;.**

Trigger: N/A (structural). Effect: A Location's field set contains no `FacilityID`-typed column; the one-to-many is enforced only from the child side. Confidence: Observed (exhaustive field-list read, `_lucernex_objects_summary.txt`).

## Confidence

Observed (exhaustive field-list read, `_lucernex_objects_summary.txt`)

---

Source: `docs/modules/facilities-locations/rules.md`
