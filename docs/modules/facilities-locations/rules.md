# Facilities, Locations & Sites — rules

`FAC-R-001` through `FAC-R-020`. Every rule below is derived from the FK graph
([`data-model.md`](data-model.md)), the Data Fields `Required` column, or a direct screen capture;
none is derived from a business-rule-engine capture (no layout-conditional-field or workflow-step
screen exists for this module yet), so confidence here tops out at **Derived** except where a
screen is cited directly. Evidence discipline per
[`../../CONVENTIONS.md`](../../CONVENTIONS.md).

---

### FAC-R-001 — A Facility must belong to exactly one Location
**Trigger:** Facility create/save. **Input:** `Facility.LocationID`. **Effect:** Required FK;
save is blocked without a Location. **Confidence:** Observed (`Required = Yes`,
[`../../data-fields/facility.md`](../../data-fields/facility.md)).

### FAC-R-002 — A Location has no reverse pointer to any Facility
**Trigger:** N/A (structural). **Effect:** A Location's field set contains no `FacilityID`-typed
column; the one-to-many is enforced only from the child side. **Confidence:** Observed (exhaustive
field-list read, `_lucernex_objects_summary.txt`).

### FAC-R-003 — A Facility must belong to exactly one Portfolio (Program)
**Trigger:** Facility create/save. **Input:** `Facility.ProgramID`, typed `Portfolio ID`.
**Confidence:** Observed (`Required = Yes`,
[`../../data-fields/facility.md`](../../data-fields/facility.md)).

### FAC-R-004 — A Location must belong to exactly one Portfolio (Program)
**Input:** `Location.ProgramID`. **Confidence:** Observed (`Required = Yes`,
[`../../data-fields/location.md`](../../data-fields/location.md)).

### FAC-R-005 — A Parcel's mandatory containment parent is its Location, not its Facility
**Input:** `Parcel.LocationID` (Required = Yes) vs. `Parcel.FacilityID` (Required = No).
**Effect:** A Parcel can exist under a Location with no building yet on it; a Facility on that Parcel
is an optional refinement, added once construction identifies which building sits on which piece of
land. **Confidence:** Observed
([`../../data-fields/parcel.md`](../../data-fields/parcel.md)).

### FAC-R-006 — A Parcel must belong to exactly one Portfolio (Program)
**Input:** `Parcel.ProgramID`. **Confidence:** Observed
([`../../data-fields/parcel.md`](../../data-fields/parcel.md)).

### FAC-R-007 — A Prototype must belong to exactly one Portfolio (Program)
**Input:** `Prototype.ProgramID`. **Confidence:** Observed
([`../../data-fields/prototype.md`](../../data-fields/prototype.md)).

### FAC-R-008 — Complex membership is optional and available to four different entity types
**Input:** `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where
exposed) and `Competitor`. **Effect:** Any of the four subtype roots — and a tracked competitor —
may be grouped under one shared shopping-center/campus record, or none. `Complex` itself carries no
count or capacity field, so the platform does not enforce or expose how many children a Complex
actually has. **Confidence:** Observed (FK presence/optionality); "no capacity enforcement" is
Derived (absence of any such column in Complex's 45 fields).

### FAC-R-009 — Complex sits above the hierarchy and has no parent of its own
**Effect:** `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/
`Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped.
**Confidence:** Derived (exhaustive field-list read), corroborated by
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §2's independent
classification of `Complex` as one of the 52 firm-global objects.

### FAC-R-010 — A Facility may defer its address to its parent Location
**Input:** `Facility.UseLocationAddress` (Boolean, Required = Yes — the flag itself must always be
set one way or the other). **Effect:** When true, the Facility is presumed to use
`Location`'s address fields rather than its own `StreetAddress1..4`/`City`/`PostalCode`.
**Confidence:** Inferred — plausible from the field name and the required-boolean pattern, not
confirmed by any screen capture of the resulting render behaviour.

### FAC-R-011 — A Parcel may subdivide from another Parcel
**Input:** `Parcel.MasterParcelID` (self-reference, typed `Parcel ID`). **Effect:** Mirrors
`Contract.MasterContractID`'s master/sub pattern exactly — a parcel of land can be split, with each
resulting parcel pointing back at the original. **Confidence:** Observed (self-reference column
present; cross-referenced against the identical master/sub pattern on `Contract` in
[`../../data-model/foreign-key-graph.md`](../../data-model/foreign-key-graph.md) §2).

### FAC-R-012 — Contract attaches to Facility and Location directly, not only through one another
**Input:** `Contract.FacilityID`, `Contract.LocationID` (both present, both optional per
[009](../../admin/009-related-fields-and-data-model.md)). **Effect:** A lease can be tied to a
Location without a Facility, a Facility without going through a Location lookup, or both at once —
the two attachment points are independent, not a forced traversal through one to reach the other.
**Confidence:** Observed (009's schema-browser capture of `Contract.FacilityID`/`LocationID` as
separate typed columns).

### FAC-R-013 — The reverse of Contract → Facility is composed as a child grid, not a lookup
**Effect:** From `Facility`'s own Related Fields sidebar, `Contract` does not appear as a related
lookup at all; instead the Facility Summary layout embeds an **"ASG Contract List (One to Many
List)"** child grid. The relationship is asymmetric by cardinality and the UI reflects that asymmetry
correctly on both sides. **Confidence:** Observed
([009](../../admin/009-related-fields-and-data-model.md), screenshot
`facility-summary-contracts-one-to-many-list.jpg`).

### FAC-R-014 — Property tax attaches only to the Parcel, never the Facility or the lease
**Input:** All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`,
`PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a
`ParcelID` FK and no `FacilityID`/`ContractID`. **Confidence:** Observed
([`../../mindmap/edges.json`](../../mindmap/edges.json)).

### FAC-R-015 — A Space must belong to exactly one Facility
**Input:** `Space.FacilityID`, Required = Yes. **Confidence:** Observed
([`../../data-fields/space.md`](../../data-fields/space.md)).

### FAC-R-016 — A Space's lease link is optional
**Input:** `Space.ContractID`, Required = No. **Effect:** A Space can be defined on a Facility
before any lease references it — e.g., during Space Management setup ahead of leasing.
**Confidence:** Observed ([`../../data-fields/space.md`](../../data-fields/space.md)).

### FAC-R-017 — A Tenant must belong to exactly one Space
**Input:** `Tenant.SpaceID`, typed `Space ID`. **Confidence:** Derived — the FK type is declared
and every `Tenant` field (headcount, capacity, move-in/out dates) is scoped around occupying one
space; the Data Fields catalog for `Tenant` was not captured separately to confirm the `Required`
flag directly.

### FAC-R-018 — A generic-attachment child (soft `ProjectEntityID` only) is not restricted to this module's entity types
**Input:** `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`,
`DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`.
**Effect:** In principle any of these can attach to any of the eight/nine `ProjectEntity` subtype
roots across the whole product (including `PotentialProject`/"Site", `Program`, `Project`,
`Contract`), not only to a record in this module. **Confidence:** Derived — no screen capture shows
which subtype a live row actually points at (see
[`demographics.md`](demographics.md) Open Question 1).

### FAC-R-019 — `Prototype`'s Location/Complex/DMA relationships exist in the schema but are not administrator-configurable
**Input:** `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in
`_lucernex_objects_summary.txt` but do not appear anywhere in
[`../../data-fields/prototype.md`](../../data-fields/prototype.md)'s 15-row catalog. **Effect:**
Unlike the identical columns on `Facility`/`Location`/`Parcel`, these cannot be placed on a
Prototype layout by a tenant administrator through the observed mechanism. **Confidence:** Derived
(cross-referencing the two sources; see
[`data-model.md`](data-model.md#5-schema-export-vs-admin-data-fields-catalog--a-real-divergence-and-what-it-means)).
Whether this reflects a deliberate platform restriction or simply that ASG's tenant never placed
those fields is unresolved — see Open Questions there.

### FAC-R-020 — `DemographicStudyArea` and `SiteSurvey`'s fixed mile-bands are two independent, non-integrated mechanisms for the same concept
**Input:** `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the
same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as
a reusable, parameterised definition. Neither references the other. **Confidence:** Derived,
exhaustive column-name comparison — see [`demographics.md`](demographics.md) §3 for the full
argument and the rebuild consequence.
