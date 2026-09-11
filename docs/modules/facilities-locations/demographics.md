# Demographics & Site Selection

**Stated up front.** Nine objects, split cleanly into two families that never merge: a
**reusable reference layer** (`DMA`, `DemographicStudyArea`, `DemographicReport`, `DemographicFact`
— all `firm_global`, no `ProjectEntityID`) that defines *how* to measure a trade area once and reuse
it across many candidate sites, and a **per-site evaluation layer** (`Competitor`, `SiteSurvey`,
`DemographicResults`, `LandPurchaseSummary`, `LinkLandPurchaseInspection` — all `entity_scoped`,
attached generically via `ProjectEntityID`) that records what was actually found at one specific
site. This family has **no counterpart anywhere in ASG Edge+ today** — confirmed by search, no
`Location`/`Facility`/site-selection domain classes exist in either
`ASG-Edgeplus-Configuration-Service` or the legacy monorepo.

**A genuine, unresolved redundancy sits inside this family**, worth flagging up front the way
[`../workflow/README.md`](../workflow/README.md) flags its three parallel milestone mechanisms:
`SiteSurvey` bakes fixed 1/3/5-mile population/income/age bands directly into 27 of its own 79
columns, while `DemographicStudyArea` defines the *same* kind of trade area as a configurable
radius-or-drive-time record meant to be reused across sites. Two ways to say "how far out do we
measure" coexist in the schema, one hard-coded per-survey and one parameterised and reusable.
**Derived**, cross-referencing the two field lists directly.

## 1. The reference layer — reusable, firm-wide

| Object | Fields | What it defines |
|---|---:|---|
| `DMA` | 7 | A Designated Market Area — a standard US media-market geography (`DMAName`, `DMANumber`). Pure lookup data. |
| `DemographicStudyArea` | 6 | A trade-area definition: `AreaRadius` + `CodeRadiusUnitID`, or `AreaDriveTimeInMinutes` — the parameterised alternative to SiteSurvey's fixed bands. |
| `DemographicReport` | 10 | A report definition tied to a `Prototype` and a `Region`/market area — reusable across every site sharing that prototype and market, not generated fresh per site. |
| `DemographicFact` | 10 | One ordered data point (`OrderRecordName`, `Weighting`, a `ParentID`/`PreviousID` linked-list ordering) inside a `DemographicReport`. |

**Observed**, `_lucernex_objects_summary.txt` and
[`../../data-fields/demographics-market-tables.md`](../../data-fields/demographics-market-tables.md)
(an independently-built source that groups the same four tables under one file and states, without
reference to the FK graph, that they are "reusable geography... and reusable study/report
definitions... that can be run against many candidate sites rather than hard-coded to one survey's
fixed mile-radius bands" — the same conclusion reached here from the field-level evidence, a second
time, from a different angle).

`DemographicReport.PrototypeID` is the one hard FK connecting this reference layer back into the
rest of the module (see [`data-model.md`](data-model.md#2-the-internal-fk-graph--23-edges)) — a
market study can be defined once per `Prototype` (the standard store design) rather than once per
physical site.

## 2. The per-site evaluation layer

| Object | Fields | Attaches via | What it captures |
|---|---:|---|---|
| `SiteSurvey` | 79 | `ProjectEntityID` only (soft) | A physical due-diligence checklist for one candidate site: building condition ratings (`CodeFacilityConditionID`, `CodeFloorConditionID`, `CodeCeilingConditionID`, `CodeParkingLotConditionID`), utility/access booleans (`FireSprinkler`, `HandicapAccessible`, `IsCLECAvail`), and — the bulk of the object — `Population`/`Households`/`MedianAge`/`PercentMale`/`PercentFemale`/`HouseholdAvgIncome` each repeated at **1 Mile / 3 Miles / 5 Miles**. |
| `Competitor` | 26 | `ComplexID` (hard, optional) + `ProjectEntityID` (soft) | A nearby competing retailer — name, type, distance, drive time, last-year sales, whether it is an anchor store. |
| `DemographicResults` | 12 | `ProjectEntityID` only (soft) | The saved output of running a demographic analysis against one entity — a name, a status, a `DocumentID` pointing at the actual result file, and `TimeInitiated`/`TimeFinished` timestamps. This is the *result record*; `DemographicReport`/`DemographicFact` above are the *definition*. |
| `LandPurchaseSummary` | 35 | `ProjectEntityID` only (soft) | A raw-land acquisition deal: `AskingPrice`/`SalePrice`, `EarnestMoney` + `EarnestMoneyHardDate`, and — distinctively — **six separate `Contact` FKs**, one each for the buyer's and seller's broker, lawyer, and signee. |
| `LinkLandPurchaseInspection` | 8 | `ProjectEntityID` (soft) + `LandPurchaseSummaryID` (untyped `Text` — see [`data-model.md`](data-model.md#4-the-one-non-typed-fk-in-the-module)) | Inspection-period terms (`CodeInspectionTypeID`, `CodeInspectionPeriodStartID`, `InspectionDays`, `WaiverDays`) attached to one land deal. |

**Observed**, `_lucernex_objects_summary.txt`.

**`LandPurchaseSummary`'s six-contact structure is a distinct sub-process from leasing.** Nowhere
else in this module — or, per the FK-graph rank list in
[`../../data-model/foreign-key-graph.md`](../../data-model/foreign-key-graph.md), in `Contract`
either — does one object carry buyer-side *and* seller-side broker/lawyer/signee roles
simultaneously. This is the schema's model of buying land outright, as opposed to leasing space in
someone else's building, and it sits in this module (not `contracts-leases`) because it is
triggered during site selection, before any lease exists. **Derived.**

## 3. Why `SiteSurvey` and `DemographicStudyArea` do not merge

Both express "how big a trade area to measure," but neither references the other, and the fixed
1/3/5-mile bands on `SiteSurvey` cannot be re-parameterised — they are separate columns
(`Population1Mile`, `Population3Miles`, `Population5Miles`, and the same pattern six more times for
`Households`, `MedianAge`, `PercentMale`, `PercentFemale`, `HouseholdAvgIncome`), not a
`DemographicStudyAreaID` foreign key plus a generic result value. **Derived**, high confidence —
the column-naming pattern is exhaustive and consistent across all seven repeated metrics.

**Rebuild consequence.** A rebuild that wants configurable trade-area radii (3 miles, 7 miles,
10-minute drive, whatever a given deployment needs) should design around `DemographicStudyArea`'s
pattern — radius/drive-time as data, not as baked-in columns — and treat `SiteSurvey`'s fixed bands
as the thing being replaced, not the thing being reproduced. Building both would mean maintaining
two mechanisms that answer the same question.

## 4. ASG Edge+ relevance

**Nothing exists yet.** No `SiteSurvey`, `DemographicReport`, `Competitor`, `DMA`, or
`LandPurchaseSummary`-equivalent class was found anywhere in
`ASG-Edgeplus-Configuration-Service` or the legacy monorepo. Whether ASG Edge+ needs this family at
all is a **business** question — ASG's own BRDs have not been checked against it in this pass — not
a technical one; the module can be built later without disturbing the Location/Facility/Parcel core
this folder's other documents describe, since every attachment here is either a soft
`ProjectEntityID` or (for `Competitor`) an optional `ComplexID`, never a required column on
`Facility`/`Location`/`Parcel` themselves.

## Open questions

1. **Which specific `ProjectEntity` type does a live `SiteSurvey`/`LandPurchaseSummary` actually
   point at** — a `PotentialProject` ("Site"), a `Location`, or a `Facility`? The soft FK cannot say,
   and no screen has been captured. This is the same open question raised in
   [`location-vs-facility-vs-site.md`](location-vs-facility-vs-site.md) §3 from the other direction.
2. **Is the fixed-band `SiteSurvey` still the one actually used by ASG**, or has the tenant moved to
   `DemographicStudyArea`-based reporting? Nothing in this corpus shows either populated with real
   data.
3. **Does any BRD require site-selection/demographics functionality in ASG Edge+ at all?** Not
   checked in this pass.
