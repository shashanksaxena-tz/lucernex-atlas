# Portfolio & Real-Estate Transactions — data model

**Stated up front.** 11 objects, 513 fields, two `ProjectEntity` subtype roots (`Program`,
`PotentialProject`) and nine `entity_scoped` children. Internally the module has only **12** FK
edges — it is a shallow module, not a deep one; most of its 513 fields point *out* to other modules
(66 outbound edges) rather than to each other.

## 1. Every object

| Object | PG table | Fields | Role | One-line |
|---|---|---:|---|---|
| `Program` | `program` | 180 | `subtype_root` | The Portfolio/Capital Program — policy carrier, layout registry, rollup counters. |
| `PotentialProject` | `potential_project` | 108 | `subtype_root` | The Site — 0 inbound FKs, 0 Manage Data Fields exposure. |
| `Scenario` | `scenario` | 69 | `entity_scoped` | A deal scenario under an `RETransaction`; the one FK reaching `Contract`. |
| `RETransaction` | `r_e_transaction` | 31 | `entity_scoped` | The formal transaction header; required `ProgramID`. |
| `DevelopmentSlot` | `development_slot` | 31 | `entity_scoped` | A rollout build-out slot under `DevelopmentPlan`. |
| `LinkReTransScenContact` | `link_re_trans_scen_contact` | 33 | `entity_scoped` | Broker/attorney contact join, despite the "Link" name treated as standalone (32 admin fields). |
| `ReTransScenContact` | `re_trans_scen_contact` | 28 | `entity_scoped` | A second, non-join contact record scoped to a transaction/scenario. |
| `DevelopmentPlan` | `development_plan` | 7 | `entity_scoped` | Header over `DevelopmentSlot`. |
| `ProgramRevenueWeeks` | `program_revenue_weeks` | 13 | `entity_scoped` | Weekly filled/unfilled slot rollup for a `Program`. |
| `ComparisonReport` | `comparison_report` | 4 | `entity_scoped` | A saved comparison report, own page-layout assignment. |
| `ComparisonItem` | `comparison_item` | 9 | `entity_scoped` | One line of a comparison analysis. |

Role classification per [`project-entity.md`](../../data-model/project-entity.md) §2 — `Program` and
`PotentialProject` carry the shared `ProjectEntityID(Number)` block; the other nine carry
`ProjectEntityID(Entity ID)`, a hard FK to the spine.

## 2. Internal FK edges (12)

| Source | Column | Target | Notes |
|---|---|---|---|
| `Program` | `OrgChartProgramID` | `Program` | Self-reference — a Portfolio can roll into a parent Portfolio. |
| `PotentialProject` | `ProgramID` | `Program` | Site belongs to a Portfolio. |
| `RETransaction` | `ProgramID` | `Program` | **Required.** |
| `RETransaction` | `RelatedTransactionID` | `RETransaction` | Self-reference. |
| `RETransaction` | `KickoffScenarioID` / `PreferredScenarioID` / `SelectedScenarioID` | `Scenario` | Three independent scenario-pointer roles on the same transaction. |
| `Scenario` | `RETransactionID` | `RETransaction` | **Required.** |
| `LinkReTransScenContact` | `RETransactionID` | `RETransaction` | |
| `LinkReTransScenContact` | `ScenarioID` | `Scenario` | |
| `DevelopmentSlot` | `ProgramID` | `Program` | |
| `DevelopmentSlot` | `TaskTemplatePEID` | `TaskTemplate` | Cross-module — `projects-capital`. |

*(`DevelopmentPlan`, `ProgramRevenueWeeks`, `ComparisonReport`, `ComparisonItem`, `ReTransScenContact`
carry only `ProjectEntityID`/`ModifiedByID`-class edges, already counted in the cross-module table
below — they have no internal-module FK of their own.)*

## 3. Cross-module edges

### 3.1 Outbound (66 columns, this module → elsewhere)

| Target module | Columns | What's referenced |
|---|---:|---|
| `platform-tenancy` | 26 | `Member` (audit stamps — `CreatedByID`/`ModifiedByID`, the large majority), `Region`, `StateProvinceCountry`, `Jurisdiction`, `ProjectEntity` |
| `people-parties` | 17 | `Member` (assignee/broker/contact roles beyond the audit stamps) |
| `facilities-locations` | 10 | `Location`, `Complex`, `Prototype`, `DMA`, `Facility` |
| `contracts-leases` | 6 | `Contract`, `ContractTerm`, `ContractAmendment`, `Covenant` |
| `projects-capital` | 5 | `TaskGroup` (via the ambiguous `Task/Group ID` type — see §5), `TaskTemplate` |
| `out-of-scope-cost-budget` | 2 | `BudgetTemplate` |

### 3.2 Inbound (10 columns, elsewhere → this module)

| Source module | Source.Column | Target |
|---|---|---|
| `facilities-locations` | `Facility.ProgramID`, `Location.ProgramID`, `Parcel.ProgramID`, `Prototype.ProgramID` | `Program` |
| `platform-tenancy` | `Project.ProgramID`, `MapClientSchedule.RETransactionID`, `MapClientSchedule.ScenarioID` | `Program`, `RETransaction`, `Scenario` |
| `accounting` | `DiscountRate.ProgramID`, `FiscalPeriod.ProgramID` | `Program` |
| `contracts-leases` | `Contract.ProgramID` | `Program` |

**`Program` is the single most inbound-referenced object in this module** — nine distinct source
objects across five other modules all resolve "which Portfolio is this" through it. **Nothing
outside this module references `PotentialProject`, `Scenario`, or `RETransaction`** — confirming
§1.1 of [`site-pipeline.md`](site-pipeline.md): the deal pipeline is a dead end for any object
outside this module to point into.

## 4. The Contract boundary — one way only

| From | Column | To | Required? | Reverse column on `Contract`? |
|---|---|---|---|---|
| `Scenario` | `ContractID` | `Contract` | No | **None.** |
| `Scenario` | `AmendmentID` | `ContractAmendment` | No | **None.** |
| `RETransaction` | `KickoffContractTermID` | `ContractTerm` | No | **None.** |
| `RETransaction` | `KickoffCovenantID` | `Covenant` | No | **None.** |

`Contract`'s own outbound edges include exactly one column into this module: `Contract.ProgramID` →
`Program`. There is no `Contract.ScenarioID`, no `Contract.RETransactionID`. The deal pipeline can
name a `Contract` once one exists; a `Contract` cannot name the deal that produced it. **Observed**,
`docs/mindmap/edges.json`.

## 5. A naming ambiguity worth flagging: `Task/Group ID`

`RETransaction.ActiveDealStepTaskIDList`, `RETransaction.DealSchedule`, and
`Scenario.ActiveDealStepTaskIDList`/`DealSchedule` are all typed **`Task/Group ID`** — a single FK
type name that, on its face, could resolve to either `Task` or `TaskGroup`
([`projects-capital`](../projects-capital/data-model.md)). The graph-building script
(`docs/mindmap/build_graph.py`) resolved every instance to `TaskGroup` specifically. Given `Task`,
`TaskGroup`, and `TaskItem` are three **byte-identical 37-field tables**
([`../projects-capital/data-model.md`](../projects-capital/data-model.md)#2), this resolution
is best read as "one of the three schedule-row tables," not as confirmation that a deal step can
only ever be a `TaskGroup` and never a plain `Task`. **Derived**, low confidence on the specific
target.

## 6. `Program`'s 180 fields, grouped

| Group | Representative columns | Count (approx.) |
|---|---|---:|
| Identity / `ProjectEntity` union block | `EntityId`, `ProjectEntityID`, `ProjectEntityName`, `ClientEntityID`, `EntityEmail`, `EntityPhoto` | 8 |
| Accounting policy | `SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `SLAssetAmortizeMethod`/`SLCashAmortizeMethod`/`SLExpenseAmortizeMethod`, `SLProrate35As28`, `SLMatchYearEnds`, `FiscalYearEnd`, 14 FX rate-type selectors | ~23 |
| Per-subtype "Setup Page Layout" registry | 11 × `<Subtype>SetupPageLayoutID` + 6 × `<Subtype>MapSetupLayoutID` | 17 |
| Site-pipeline conversion layouts | `SiteToProjectSetupLayoutID`, `ProjectToFacilitySetupLayoutID` | 2 |
| Rollup counters | `TotalSites`, `TotalOpeningProjects`, `TotalCapitalProjects`, `TotalProjects`, `TotalFacilities`, `TotalLocations`, `TotalParcels`, `TotalContracts`, `TotalREContracts`, `TotalEquipmentContracts`, `TotalActiveProjects`, `TotalInactiveProjects`, `TotalDeadProjects` | 13 |
| Region / org-chart | `RegionID`, `RootRegionID`, `SubRegionID`, `OrgChartProgramID`, `RegionsInProgram`, `MarketsInProgram` | 6 |
| Site-selection union columns (shared with `PotentialProject`/`Project`) | `CodeDealTypeID`, `CodeMarketAreaID`, `CodeMarketTypeID`, `DemographicDMAID`, `TradeArea`, `ComplexID`, `PrototypeID` | 7 |
| Lifecycle / phase status (shared `ProjectEntity` union block) | `DesignPhaseStatus`, `ConstructionPhaseStatus`, `PossessionPhaseStatus`, `OperationsPhaseStatus`, `CurrentMilestone`/`NextMilestone`/`PreviousMilestone` | 10 |
| Address / geography (shared union block — a Portfolio can carry its own address) | `StreetAddress1..4`, `City`, `PostalCode`, `LatitudeDegrees`, `LongitudeDegrees`, `TimeZone` | ~10 |
| Everything else (identity display names, scheduling defaults, misc) | `ProgramName`, `ProgramType`, `Description`, `DefaultHolidayScheduleID`, `DefaultWorkWeekends`, `DBFolderSizeMB`, `UUID`, … | remainder |

**Derived**, from `_lucernex_objects_summary.txt`. Roughly 30 of `Program`'s 180 fields belong to
`accounting`'s domain and 19 to layout configuration — nearly a quarter of the object is
cross-cutting policy, not portfolio identity.

## 7. `PotentialProject`'s 108 fields — the same union-block shape

`PotentialProject` shares the identical `ProjectEntity`-union groups
([`project-entity.md`](../../data-model/project-entity.md) §1.3): identity block (8 columns),
lifecycle/phase status (10), site-selection fields (`CodeDealTypeID`, `CodeMarketAreaID`,
`DemographicDMAID`, `TradeArea`, `ComplexID`, `PrototypeID` — 7), address/geography (~14), plus its
own real-estate-pipeline-specific fields: `FinancialModel`, `ComparisonList`, `IssuesAndAlerts`,
`RelocatedFrom`, `RevNumber`. Required/optional flags could not be checked — see
[`site-pipeline.md`](site-pipeline.md) §1.1 — because the object carries zero rows in the Manage
Data Fields admin catalog.

## 8. `Scenario`'s 69 fields — deal terms, not lease terms

Distinct from `Contract`'s in-force terms, `Scenario` carries **proposed** terms:
`ProposedCommencementDate`, `ProposedTermLength`, `NewTermStartDate`/`NewTermEndDate`/
`NewTermLength`, `TIAllowance`, `TiPerAreaUnit`, `BrokerCommission`, `Deposit`, `CapitalRequired`,
plus site-demographic fields inherited from the evaluation process (`AverageHHIncome`,
`MedianHHIncome`, `Population5yrGrowth`, `TotalPopulation`, `ParkingRatio`, `ParkingSpaces`,
`TradeAreaCompetitors`). Two admin-required fields anchor it: `RETransactionID` and
`ProjectEntityID`. `ScenarioDealType` is required; `ScenarioType` is not.
`ContractID`/`ContractTermID`/`AmendmentID`/`CovenantID`/`KeyDateID` are all optional forward
pointers into a lease that may not exist yet. **Observed**, `docs/data-fields/scenario.md`.

## Open questions

See [`README.md`](README.md#open-questions) — this file defers the module's ranked open questions
to the overview to avoid duplication.
