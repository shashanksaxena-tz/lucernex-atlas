# Location vs. Facility vs. Complex vs. Parcel vs. Prototype vs. "Site"

**Stated up front.** These are six different concepts, not near-synonyms, and the FK graph gives a
clean answer for five of the six. **Location is the retail site/"Center"** — the operating unit
with an address, tax rates, and a link to the operating `Organization`. **Facility is the building
or premises inside it** — one Location can hold more than one Facility, never the reverse.
**Complex is an optional physical container above both** — a shopping-mall/campus record that a
Location, Facility, Parcel or Prototype may belong to, with no upward pointer of its own.
**Parcel is the legal land record** — its mandatory parent is the Location (not the Facility), and
it is the sole attachment point for the entire property-tax subsystem. **Prototype is a reusable
design template**, not a place at all — it seeds defaults for Facilities built to a standard plan.
**"Site" is not one of this module's objects.** It is `PotentialProject`, which lives in the
`portfolio-transactions` module — the pre-development pipeline record *before* a Location or
Facility exists, not a sixth member of this hierarchy. A rebuild that treats "Site" as part of the
Facility/Location family will build a concept that does not exist in this schema.

## 1. The evidence, entity by entity

| Entity | Required parent(s) | Optional parent(s) | Screens (003) | One-line role |
|---|---|---|---|---|
| `Complex` | *(none)* | *(none — is itself the optional parent)* | Location → "Complex/Center Details" | The shopping-center/campus container. `firm_global`, no `ProjectEntityID`. |
| `Location` | `Program` (Portfolio) | `Complex`, `Prototype`, `Organization` | 12, own root | The site/"Center" — address, GLA, tax rates, an operating `Organization`. |
| `Facility` | `Location`, `Program` | `Complex`, `Prototype` | 16, own root | The building/premises inside a Location. |
| `Parcel` | `Location`, `Program` | `Facility`, `Contract`, `Complex`, `Prototype`, `Organization`, `MasterParcelID` (self) | *(no own nav root — reached via Related Fields/child grids)* | The legal land record; anchors `PropertyTax*`. |
| `Prototype` | `Program` | *(schema has `Location`/`Complex`/`DMA` but not exposed in Data Fields — see [`data-model.md`](data-model.md#5-schema-export-vs-admin-data-fields-catalog--a-real-divergence-and-what-it-means))* | *(no own nav root)* | A reusable store/building design template. |
| `PotentialProject` ("Site") | *(not this module — see §3)* | | *(not this module)* | The pre-development pipeline entity. |

Required/optional is read directly from each entity's Data Fields `Required` column
([`../../data-fields/facility.md`](../../data-fields/facility.md),
[`location.md`](../../data-fields/location.md), [`parcel.md`](../../data-fields/parcel.md),
[`prototype.md`](../../data-fields/prototype.md)) — **Observed**.

## 2. Location is the "Center"; Facility is the building in it

Three independent pieces of evidence converge on this reading, none of them a naming assumption:

1. **The FK direction is asymmetric and one-way.** `Facility.LocationID` is a **required** FK to
   `Location`. `Location` has **no `FacilityID` column anywhere in its 141-field schema**. A Location
   can contain many Facilities; a Facility belongs to exactly one Location. **Observed.**
2. **The field vocabulary splits cleanly along "building" vs. "site/operator" lines**, even though
   both objects share the same `ProjectEntity` base block (which is why both carry a `FacilityName`
   column — see [`../../data-model/project-entity.md`](../../data-model/project-entity.md) §1.3, not
   because Location secretly is a Facility):

   | Facility-specific | Location-specific |
   |---|---|
   | `CodeFacilityCategoryID/GroupID/StatusID/TypeID/UseID` | `CodeLocationCategoryID/GroupID/StatusID/TypeID/UseID` |
   | `ConstructionDate`, `RemodelDate`, `OpenDate`, `CloseDate`, `DaysUntilOpen` | `OrganizationID` (the operating company) |
   | `DistributionCenterArea`, `ThirdPartyWarehouse` | `TaxRate1..4`, `EquipContractTaxRate1..4` |
   | `Firm_SpaceNumber`, `Firm_SellingSQFT` | `GrossLeaseArea`, `LocationParcelArea`, `AccountingNumber` |
   | `OperatingStatus` | `Firm_CenterName`, `Firm_County`, `Firm_Developer`, `Firm_GrandOpeningDate` |
   | `UseLocationAddress` (boolean — see below) | `CodeSubArea1-3ID`, `CodeSubRegion1-3ID`, `EDGE_ASGCenterID` |

   Facility carries the physical-asset lifecycle (built, remodeled, opened, closed) and retail
   space metrics. Location carries the tax/accounting and market-geography surface of the site as a
   whole, plus the link to the `Organization` that operates it. **Derived.**
3. **`Facility.UseLocationAddress` is a checkbox, required, with no default shown.** Its plain
   reading: a Facility may either carry its own street address or defer to its parent Location's.
   That only makes sense if Location is the "real" address of record and Facility is a building
   that normally sits at it. **Inferred** — no screen was captured showing the field's runtime
   effect.
4. **`Firm_CenterName` and `EDGE_ASGCenterID`, both on `Location`**, are the strongest naming
   evidence in the schema. `EDGE_ASGCenterID` in particular — the `EDGE_` prefix is called out
   independently in [`../../data-fields/INDEX.md`](../../data-fields/INDEX.md) as "a strong signal
   it was pushed into Lucernex from an external ASG Edge+ era integration" — says explicitly that
   ASG's own prior tooling already called this record a **Center**, not a Location. That is
   corroborated a second, independent way: [003](../../screens/003-main-navigation.md) shows
   Location's own second detail screen is literally labelled **"Complex/Center Details"**. Two
   unrelated sources — a field-naming convention and a live menu label — agree that "Center" is
   what ASG's own people call this record. **Derived**, and it is the single most load-bearing fact
   in this document for anyone naming the ASG Edge+ equivalent.
5. **An independent, separately-authored source agrees without having seen this reasoning.** The
   Data Fields catalog's own one-line summary of `Location`, written from a different admin screen
   ([005](../../admin/005-manage-data-fields.md)) by a different exploration pass, calls it *"a
   lighter-weight alternative to Facility for sites tracked before or without a full facility
   record."* That is the same conclusion — Location is the site, Facility is the (optional, later)
   building on it — arrived at from field labels alone, with no access to the FK graph.

## 3. "Site" is not part of this module — it is `PotentialProject`

The walkHierarchy aggregate-root list ([009](../../admin/009-related-fields-and-data-model.md))
names eleven types including `Site`. `Site` does **not** correspond to any object in this module.
[`../../data-model/project-entity.md`](../../data-model/project-entity.md) §2 already worked out
that the eleven walkHierarchy names map onto only nine real objects, with `Site` ↔ `PotentialProject`
— and `PotentialProject` belongs to the **`portfolio-transactions`** module
([`../../mindmap/modules.json`](../../mindmap/modules.json)), confirmed here independently: this
module's own object list has no `PotentialProject`, `Project`, or `Program`.

**Why this matters for the rebuild.** `PotentialProject` carries `LocationID`, `ComplexID`, and
`PrototypeID` (it is a `ProjectEntity` subtype root and shares that block — see
[`data-model.md`](data-model.md#31-inbound-34-columns-but-only-7-distinct-source-objects)), which
means a "Site" *can* reference a Location, Complex or Prototype from this module while it is being
evaluated — but the Site itself, its demographic pipeline, and its promotion into a real Facility
are a different module's story. `SiteSurvey` and `LandPurchaseSummary` in *this* module attach only
by the generic `ProjectEntityID`, never by a hard-typed FK — consistent with them being usable
against a `PotentialProject` just as easily as against a `Facility` or `Location`, but this corpus
never observed which one they were actually pointed at in a live record. See
[`demographics.md`](demographics.md) open questions.

## 4. Where a record has two parents, and where it has none

| Object | Two-or-more simultaneous optional parents? | None? |
|---|---|---|
| `Parcel` | **Yes — up to five at once**: `Location` (required), plus optional `Facility`, `Contract`, `Complex`, `Prototype`, `Organization`, and a self-reference `MasterParcelID`. Nothing else in this module carries as many live FKs on one record. | |
| `Facility` | Yes: `Location` (required) + optional `Complex` + optional `Prototype`, simultaneously — a Facility can sit in a Location, inside a Complex, built from a Prototype, all at once, and none of the three conflicts with another because they encode different axes (physical nesting, physical grouping, design template). | |
| `Location` | Yes: `Program` (required) + optional `Complex` + optional `Prototype` + optional `Organization`. | |
| `Complex` | | **Yes.** No upward FK anywhere in its 45-field schema. It is the top of the physical-containment axis in this module. |
| `Prototype` | | Effectively yes in the admin-visible schema — only `Program` is exposed as a relationship field (§5 of `data-model.md`). |
| `PotentialProject` ("Site") | | Not analysed here — out of module. |

## 5. Confidence summary

| Claim | Label |
|---|---|
| Facility belongs to exactly one Location; Location has no reverse pointer | **Observed** — required FK column present on Facility, absent on Location |
| Location = "Center", Facility = building within it | **Derived**, corroborated by two independent sources (`EDGE_ASGCenterID`/`Firm_CenterName` naming, and a separately-written Data Fields summary) |
| Complex is the top of the physical hierarchy in this module | **Derived** — zero outbound FKs of its own, referenced by all four subtypes |
| Parcel's true containment parent is Location, not Facility | **Observed** — `LocationID` required, `FacilityID` optional, on Parcel |
| "Site" = `PotentialProject`, a different module | **Derived**, from `../../data-model/project-entity.md` §2, confirmed here by absence from this module's object list |
| `UseLocationAddress` means Facility can inherit its address from Location | **Inferred** — plausible reading of the field name, not observed in a screen |

## Open questions

1. **What does `Facility.UseLocationAddress = true` actually do at render time?** No `Summary`
   screen for either entity has been captured yet ([003](../../screens/003-main-navigation.md)'s own
   open question #1).
2. **Does ASG's live tenant have any populated `Complex` records?** Nothing in this corpus confirms
   whether the shopping-center grouping is actually used, or is a vendor capability ASG has never
   exercised — the same kind of gap [`../accounting/README.md`](../accounting/README.md) found for
   IFRS 16.
3. **How does a `PotentialProject` ("Site") get promoted into a real `Location`/`Facility`?** Not
   captured anywhere. This is the single biggest open question connecting this module to
   `portfolio-transactions`.
