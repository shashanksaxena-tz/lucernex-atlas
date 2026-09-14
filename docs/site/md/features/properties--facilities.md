# Properties & Facilities

The real estate itself: sites, the buildings on them, and the geography between. The central naming question of the whole product, settled: the Location is the site - the 'Center' - and the Facility is the building standing on it.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Facilities and portfolio teams — the people who own the physical estate rather than the paper about it.

## Location vs Facility

*Observed · capability · source: `docs/modules/facilities-locations/location-vs-facility-vs-site.md`*

Location is the site ('Center': address, market, demographics); Facility is the physical building on it (GLA, rentable area, floors). Leases attach to facilities; the CAM pro-rata share divides by rentable area that lives on the facility, not the site.

## Site-selection data

*Derived · capability · source: `docs/modules/facilities-locations/README.md`*

Locations carry the demographics / site-selection data set, which is why deal sites and location records share so much shape - the deal pipeline is modelled on the site concept.

## Open questions (23)

*Inferred · group*

23 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### Is Location a Hub or a

*Inferred · question · source: `docs/modules/facilities-locations/README.md`*

Is Location a Hub or a Spoke concept in ASG Edge+? This module's evidence — per-Portfolio scoping, tax rates, an Organization link — argues for Spoke, with only a thin geography/address master staying in the Hub. See asg-edgeplus-mapping.md §2 for the full argument. Not yet signed off by whoever owns the Hub/Spoke boundary. Nobody has confirmed this. Recorded in modules/facilities-locations/README.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### What does Facility

*Inferred · question · source: `docs/modules/facilities-locations/README.md`*

What does Facility.UseLocationAddress = true actually render? No Summary screen for either entity has been captured yet. Nobody has confirmed this. Recorded in modules/facilities-locations/README.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Does ASG s live tenant

*Inferred · question · source: `docs/modules/facilities-locations/README.md`*

Does ASG's live tenant have any populated Complex records at all, or is it vendor capability never exercised — the same kind of gap the accounting module found for IFRS 16?. Nobody has confirmed this. Recorded in modules/facilities-locations/README.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### How does a

*Inferred · question · source: `docs/modules/facilities-locations/README.md`*

How does a PotentialProject ("Site") get promoted into a real Location/Facility? Not captured anywhere; the single biggest open question connecting this module to portfolio-transactions. Nobody has confirmed this. Recorded in modules/facilities-locations/README.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Which specific

*Inferred · question · source: `docs/modules/facilities-locations/README.md`*

**Which specific ProjectEntity type do the soft-attached children (SiteSurvey, LandPurchaseSummary, Ownership, DemographicResults) actually point at in a live record?** The schema permits any subtype; no screen confirms which one is used in practice. Nobody has confirmed this. Recorded in modules/facilities-locations/README.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Does any approved BRD

*Inferred · question · source: `docs/modules/facilities-locations/README.md`*

Does any approved BRD require site-selection/demographics functionality in ASG Edge+ at all? Not checked in this pass — a business question, not a technical one. Nobody has confirmed this. Recorded in modules/facilities-locations/README.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### What does the Space

*Inferred · question · source: `docs/modules/facilities-locations/README.md`*

What does the Space Management screen list actually render, and is there a reporting rollup from Space/Tenant up to Complex's NumberStores/GLAExcludingAnchors fields, or are those maintained by hand?. Nobody has confirmed this. Recorded in modules/facilities-locations/README.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Is Location a Hub or

*Inferred · question · source: `docs/modules/facilities-locations/asg-edgeplus-mapping.md`*

Is Location a Hub or Spoke concept — resolved above as a recommendation, but not yet a decision anyone has signed off on. Nobody has confirmed this. Recorded in modules/facilities-locations/asg-edgeplus-mapping.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Does ASG s live tenant

*Inferred · question · source: `docs/modules/facilities-locations/asg-edgeplus-mapping.md`*

Does ASG's live tenant populate Complex at all?. Nobody has confirmed this. Recorded in modules/facilities-locations/asg-edgeplus-mapping.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### What does Facility

*Inferred · question · source: `docs/modules/facilities-locations/asg-edgeplus-mapping.md`*

What does Facility.UseLocationAddress do at render time, and does ASG Edge+ need the same address-inheritance behaviour?. Nobody has confirmed this. Recorded in modules/facilities-locations/asg-edgeplus-mapping.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Does any approved BRD

*Inferred · question · source: `docs/modules/facilities-locations/asg-edgeplus-mapping.md`*

Does any approved BRD require site-selection/demographics functionality?. Nobody has confirmed this. Recorded in modules/facilities-locations/asg-edgeplus-mapping.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### How does a

*Inferred · question · source: `docs/modules/facilities-locations/asg-edgeplus-mapping.md`*

How does a PotentialProject ("Site") get promoted into a Location/Facility, and does ASG Edge+ need to model that pipeline at all, or only the post-promotion state?. Nobody has confirmed this. Recorded in modules/facilities-locations/asg-edgeplus-mapping.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### What actually

*Inferred · question · source: `docs/modules/facilities-locations/data-model.md`*

What actually populates Prototype.LocationID/ComplexID/DemographicDMAID if the admin Data Fields catalog never exposes them for placement? (§5). Nobody has confirmed this. Recorded in modules/facilities-locations/data-model.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Is

*Inferred · question · source: `docs/modules/facilities-locations/data-model.md`*

Is LinkLandPurchaseInspection.LandPurchaseSummaryID truly untyped in the live schema, or is that a parsing artefact of the offline export? (§4). Nobody has confirmed this. Recorded in modules/facilities-locations/data-model.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Does Complex carry any

*Inferred · question · source: `docs/modules/facilities-locations/data-model.md`*

Does Complex carry any tenant-scoping column at all, or is it genuinely one flat list shared across every Portfolio in the Firm? Nothing in this module's field list answers it. Nobody has confirmed this. Recorded in modules/facilities-locations/data-model.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Which specific

*Inferred · question · source: `docs/modules/facilities-locations/demographics.md`*

**Which specific ProjectEntity type does a live SiteSurvey/LandPurchaseSummary actually point at** — a PotentialProject ("Site"), a Location, or a Facility? The soft FK cannot say, and no screen has been captured. This is the same open question raised in location-vs-facility-vs-site.md §3 from the other direction. Nobody has confirmed this. Recorded in modules/facilities-locations/demographics.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Is the fixed band

*Inferred · question · source: `docs/modules/facilities-locations/demographics.md`*

Is the fixed-band SiteSurvey still the one actually used by ASG, or has the tenant moved to DemographicStudyArea-based reporting? Nothing in this corpus shows either populated with real data. Nobody has confirmed this. Recorded in modules/facilities-locations/demographics.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Does any BRD require

*Inferred · question · source: `docs/modules/facilities-locations/demographics.md`*

Does any BRD require site-selection/demographics functionality in ASG Edge+ at all? Not checked in this pass. Nobody has confirmed this. Recorded in modules/facilities-locations/demographics.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### What does Facility

*Inferred · question · source: `docs/modules/facilities-locations/location-vs-facility-vs-site.md`*

What does Facility.UseLocationAddress = true actually do at render time? No Summary screen for either entity has been captured yet (003's own open question #1). Nobody has confirmed this. Recorded in modules/facilities-locations/location-vs-facility-vs-site.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Does ASG s live tenant

*Inferred · question · source: `docs/modules/facilities-locations/location-vs-facility-vs-site.md`*

Does ASG's live tenant have any populated Complex records? Nothing in this corpus confirms whether the shopping-center grouping is actually used, or is a vendor capability ASG has never exercised — the same kind of gap ../accounting/README.md found for IFRS 16. Nobody has confirmed this. Recorded in modules/facilities-locations/location-vs-facility-vs-site.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### What does the Space

*Inferred · question · source: `docs/modules/facilities-locations/space-management.md`*

What does the Space Management screen list actually render? Not captured; Facility's own group in 003 names it but no screen inside it was opened. Nobody has confirmed this. Recorded in modules/facilities-locations/space-management.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### What do the four

*Inferred · question · source: `docs/modules/facilities-locations/space-management.md`*

What do the four HeadCount/Capacity slots on Tenant represent? (§2). Nobody has confirmed this. Recorded in modules/facilities-locations/space-management.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

### Is there a reporting

*Inferred · question · source: `docs/modules/facilities-locations/space-management.md`*

**Is there a reporting rollup from Space/Tenant up to Complex's NumberStores and GLAExcludingAnchors fields**, or are those Complex fields maintained by hand?. Nobody has confirmed this. Recorded in modules/facilities-locations/space-management.md, under the Facilities, Locations & Sites area. Until it is settled, anything built on the assumption is a guess.

## Rules (20)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### A Facility must — [FAC-R-001](../rules/FAC-R-001.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Trigger: Facility create/save. Input: `Facility.LocationID`.**

### A Location has no — [FAC-R-002](../rules/FAC-R-002.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Trigger: N/A (structural). Effect: A Location's field set contains no `FacilityID`-typed column;.**

### A Facility must — [FAC-R-003](../rules/FAC-R-003.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Trigger: Facility create/save. Input: `Facility.ProgramID`, typed `Portfolio ID`.**

### A Location must — [FAC-R-004](../rules/FAC-R-004.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Location.ProgramID`. Confidence: Observed (`Required = Yes`, `../../data-fields/location.md`).**

### A Parcel s mandatory — [FAC-R-005](../rules/FAC-R-005.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Parcel.LocationID` (Required = Yes) vs. `Parcel.FacilityID` (Required = No).**

### A Parcel must belong — [FAC-R-006](../rules/FAC-R-006.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Parcel.ProgramID`. Confidence: Observed (`../../data-fields/parcel.md`).**

### A Prototype must — [FAC-R-007](../rules/FAC-R-007.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Prototype.ProgramID`. Confidence: Observed (`../../data-fields/prototype.md`).**

### Complex membership — [FAC-R-008](../rules/FAC-R-008.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `ComplexID` on `Facility`, `Location`, `Parcel`, `Prototype` (all `Required = No` where exposed) and `Competitor`. Effect: Any of the four subtype roots — and a tracked competitor — may be grouped under one shared shopping-center/campus record, or none.**

### Complex sits above — [FAC-R-009](../rules/FAC-R-009.md)

*Derived · rule · source: `docs/modules/facilities-locations/rules.md`*

**Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped.**

### A Facility may defer — [FAC-R-010](../rules/FAC-R-010.md)

*Inferred · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Facility.UseLocationAddress` (Boolean, Required = Yes — the flag itself must always be set one way or the other). Effect: When true, the Facility is presumed to use `Location`'s address fields rather than its own `StreetAddress1..4`/`City`/`PostalCode`.**

### A Parcel may — [FAC-R-011](../rules/FAC-R-011.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Parcel.MasterParcelID` (self-reference, typed `Parcel ID`). Effect: Mirrors `Contract.MasterContractID`'s master/sub pattern exactly — a parcel of land can be split, with each resulting parcel pointing back at the original.**

### Contract attaches to — [FAC-R-012](../rules/FAC-R-012.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Contract.FacilityID`, `Contract.LocationID` (both present, both optional per 009). Effect: A lease can be tied to a Location without a Facility, a Facility without going through a Location lookup, or both at once — the two attachment points are independent, not a forced traversal through….**

### The reverse of — [FAC-R-013](../rules/FAC-R-013.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Effect: From `Facility`'s own Related Fields sidebar, `Contract` does not appear as a related lookup at all; instead the Facility Summary layout embeds an **"ASG Contract List (One to Many List)"** child grid.**

### Property tax — [FAC-R-014](../rules/FAC-R-014.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: All six `PropertyTax*` objects (`PropertyTaxAppeal`, `PropertyTaxAppealAward`, `PropertyTaxAssessment`, `PropertyTaxBill`, `PropertyTaxDetail`, `PropertyTaxSummary`) carry a `ParcelID` FK and no `FacilityID`/`ContractID`. Confidence: Observed (`../../mindmap/edges.json`).**

### A Space must belong — [FAC-R-015](../rules/FAC-R-015.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Space.FacilityID`, Required = Yes. Confidence: Observed (`../../data-fields/space.md`).**

### A Space s lease link — [FAC-R-016](../rules/FAC-R-016.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Space.ContractID`, Required = No. Effect: A Space can be defined on a Facility before any lease references it — e.g., during Space Management setup ahead of leasing.**

### A Tenant must belong — [FAC-R-017](../rules/FAC-R-017.md)

*Derived · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Tenant.SpaceID`, typed `Space ID`. Confidence: Derived — the FK type is declared and every `Tenant` field (headcount, capacity, move-in/out dates) is scoped around occupying one space;.**

### A generic attachment — [FAC-R-018](../rules/FAC-R-018.md)

*Derived · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any of the eight/nine `ProjectEntity` subtype roots across the….**

### Prototype s Location — [FAC-R-019](../rules/FAC-R-019.md)

*Observed · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `Prototype.LocationID`, `.ComplexID`, `.DemographicDMAID` are declared columns in `_lucernex_objects_summary.txt` but do not appear anywhere in `../../data-fields/prototype.md`'s 15-row catalog. Effect: Unlike the identical columns on `Facility`/`Location`/`Parcel`, these cannot be placed on….**

### DemographicStudyArea — [FAC-R-020](../rules/FAC-R-020.md)

*Derived · rule · source: `docs/modules/facilities-locations/rules.md`*

**Input: `SiteSurvey` carries `Population1Mile/3Miles/5Miles` (and six more metrics repeated the same way) as fixed columns; `DemographicStudyArea` carries `AreaRadius`/`AreaDriveTimeInMinutes` as a reusable, parameterised definition.**
