# Portfolio & Real-Estate Transactions

*In scope for the rebuild*

The portfolio/capital-program container above projects, plus deal pipeline: potential projects, RE transactions, scenarios and comparison reporting.

Stated up front. This module is two things bolted together on one shared object, Program — the record the menu calls Portfolio: (1) the portfolio container that sits at the top of the ownership hierarchy and carries the tenant's accounting policy, fiscal calendar, and org-chart region tree, and (2) the pre-lease deal pipeline — PotentialProject ("Site") → RETransaction → Scenario — that runs before a Contract exists. 11 objects, 513 fields. PotentialProject is the site-selection record itself (../facilities-locations/location-vs-facility-vs-site.md already established it does not belong to the facilities module); this module owns it and everything that evaluates it. The central finding: two page-layout fields exist on Program and nowhere else in the 223-object schema — SiteToProjectSetupLayoutID and ProjectToFacilitySetupLayoutID — naming a two-step promotion pipeline, Site → Project → Facility, that no other evidence in the corpus confirms end-to-end. Full argument in site-pipeline.md.

|  | Count |
|---|---|
| Record types | 11 |
| Fields | 513 |
| Keys in | 10 |
| Keys out | 66 |
| Rules | 16 |

## Record types

| Record type | Postgres table | Fields | Referenced by |
|---|---|---|---|
| [Program](../entities/Program.md) | `program` | 180 | 12 |
| [PotentialProject](../entities/PotentialProject.md) | `potential_project` | 108 | 0 |
| [Scenario](../entities/Scenario.md) | `scenario` | 69 | 5 |
| [LinkReTransScenContact](../entities/LinkReTransScenContact.md) | `link_re_trans_scen_contact` | 33 | 0 |
| [DevelopmentSlot](../entities/DevelopmentSlot.md) | `development_slot` | 31 | 0 |
| [RETransaction](../entities/RETransaction.md) | `r_e_transaction` | 31 | 4 |
| [ReTransScenContact](../entities/ReTransScenContact.md) | `re_trans_scen_contact` | 28 | 1 |
| [ProgramRevenueWeeks](../entities/ProgramRevenueWeeks.md) | `program_revenue_weeks` | 13 | 0 |
| [ComparisonItem](../entities/ComparisonItem.md) | `comparison_item` | 9 | 0 |
| [DevelopmentPlan](../entities/DevelopmentPlan.md) | `development_plan` | 7 | 0 |
| [ComparisonReport](../entities/ComparisonReport.md) | `comparison_report` | 4 | 0 |

## Rules

| Rule | Subject | What it requires | Confidence |
|---|---|---|---|
| [POR-R-001](../rules/POR-R-001.md) |  | A `Contract` needs a fiscal period, discount rate, or ASC 842 threshold · `Contract.ProgramID` · Resolves to `Program`'s policy fields (`SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeTh | Observed |
| [POR-R-002](../rules/POR-R-002.md) |  | Workflow routing needs a `REGION1`/`REGION2` assignee · `Program.RegionID` / `RootRegionID` / `SubRegionID` → `Region` · Resolves an org-chart position through the region hierarchy. `MARKET` resolves  | Inferred |
| [POR-R-003](../rules/POR-R-003.md) |  | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overr | Observed |
| [POR-R-004](../rules/POR-R-004.md) |  | A `Scenario` reaches `Contract` · `Scenario.ContractID` · One-way, optional link. `Contract` carries no reciprocal `ScenarioID`/`RETransactionID` column — a signed lease cannot be traced back to the d | Observed |
| [POR-R-005](../rules/POR-R-005.md) |  | A `PotentialProject`, `Program`, `Scenario`, or `RETransaction` needs a deal classification · `PotentialProject.CodeDealTypeID` / `Program.CodeDealTypeID` → `Deal Type Code` (2024); `Scenario.CodeScen | Observed |
| [POR-R-006](../rules/POR-R-006.md) |  | A `RETransaction` is opened against a site the tenant may already occupy · `RETransaction.FacilityID` · Optional direct FK to an existing `Facility` — a renewal/expansion transaction can name its Faci | Observed |
| [POR-R-007](../rules/POR-R-007.md) |  | A rollout program needs capacity tracking · `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` · Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSl | Derived |
| [POR-R-008](../rules/POR-R-008.md) |  | A user compares competing sites or scenarios · `ComparisonReport` → `ComparisonItem` · `ComparisonItem.ComputedValue`/`ExpenseGroup` hold computed comparison output; `ScenarioName`/`ScenarioDate` are  | Observed |
| [POR-R-009](../rules/POR-R-009.md) |  | Notification/routing needs to walk the org chart · `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) · Two independent hierarchies exist: the `Region` ch | Inferred |
| [POR-R-010](../rules/POR-R-010.md) |  | A physical site's lifecycle needs to distinguish "building it" from "leasing it" · `Project.ProjectType` = "Opening Project or Capital Project" (`Project`, `platform-tenancy`) vs. `Contract` (`contrac | Derived |
| [POR-R-011](../rules/POR-R-011.md) |  | Any process needs to trace a `Facility`/`Location` back to the `PotentialProject` it originated from · (none — no such column exists) · Not possible via FK. `PotentialProject` has zero inbound edges i | Observed |
| [POR-R-012](../rules/POR-R-012.md) |  | A Site is promoted toward becoming an operating asset · `Program.SiteToProjectSetupLayoutID`, then `Program.ProjectToFacilitySetupLayoutID` · Names a two-step conversion pipeline (Site → Project → Fac | Derived |
| [POR-R-013](../rules/POR-R-013.md) |  | `RETransaction` is created · `RETransaction.ProgramID` · Required — a transaction must belong to a Portfolio. · Observed | Observed |
| [POR-R-014](../rules/POR-R-014.md) |  | `Scenario` is created · `Scenario.RETransactionID`, `Scenario.ProjectEntityID`, `Scenario.ScenarioDealType` · All three required. `Scenario.ScenarioType` is optional. | Observed |
| [POR-R-015](../rules/POR-R-015.md) |  | A `Scenario`'s deal type needs comparing against its parent transaction's preference · `Scenario.CodeScenarioDealTypeID` vs. `RETransaction.PreferredScenarioCodeDealTypeID` · Both draw from the same c | Derived |
| [POR-R-016](../rules/POR-R-016.md) |  | `Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read · `Task/Group ID` FK type · The graph-building script resolves this ambiguous type  | Derived |
