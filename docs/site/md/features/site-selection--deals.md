# Site Selection & Deals

Out of scope pending confirmation - no approved BRD covers the deal pipeline; ASG's BRD-11 Portfolio describes the portfolio view, not site selection. The pre-lease pipeline exists in the product: portfolios hold deals, deals become sites, sites are promoted into projects and then facilities. 'Portfolio' on the menu is one record (Program), proved by the screen routing. Confirm with the business whether any of it is used before relying on it either way.

## Who it is for

*Derived · fact · source: `docs/features/README.md`*

Real-estate and development teams working a site from prospect to signed deal.

## Promotion pipeline

*Observed · capability · source: `docs/modules/portfolio-transactions/site-pipeline.md`*

The Site-to-Project-to-Facility promotion pipeline is named by two layout fields unique to the portfolio record - the layouts used when promoting a deal site into a project, and a project into a facility. One confirmed foreign key (Project to Facility) closes half the chain.

## Deals before leases

*Derived · capability · source: `docs/modules/portfolio-transactions/README.md`*

Deals are scenarios before they are leases: a site collects deal attempts and what-if scenarios, and nothing becomes a lease until the pipeline promotes it. The pipeline is the front door of the product.

## Invisible to catalog

*Observed · fact*

The pipeline's records are invisible to the field catalogue: the Site record has 108 census fields and zero admin-catalogue rows - the starkest of the twelve records the catalogue omits entirely, plausibly because pipeline records are not layout-placeable (inferred).

## Open questions (11)

*Inferred · group*

11 things nobody has confirmed for this feature. Each one is work somebody has to do before the feature can be rebuilt with confidence; they are carried here rather than resolved by guessing. Click one for the question and the document that raised it.

### How does a

*Inferred · question · source: `docs/modules/portfolio-transactions/README.md`*

How does a PotentialProject ("Site") actually become a Project, and then a Facility? The two unique Program layout fields name the transition; no FK, workflow capture, or screen confirms the mechanism. The single biggest open question in this module — full treatment in site-pipeline.md. Nobody has confirmed this. Recorded in modules/portfolio-transactions/README.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### What are the row

*Inferred · question · source: `docs/modules/portfolio-transactions/README.md`*

**What are the row values of RE Transaction Status Code, Deal Type Code, `Scenario Type Code, and Scenario Deal Type Code`?** All four attach to this module's pipeline; none were read from the live tenant. Without them the pipeline's actual stage names are unconfirmed. Nobody has confirmed this. Recorded in modules/portfolio-transactions/README.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### Does AssigneeType s

*Inferred · question · source: `docs/modules/portfolio-transactions/README.md`*

**Does AssigneeType's REGION1/REGION2/MARKET resolve through Program.RegionID/ RootRegionID/SubRegionID, or through some other structure?** No screen or query confirms the mapping; Region's own 1-column schema entry gives no independent evidence either way. Nobody has confirmed this. Recorded in modules/portfolio-transactions/README.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### Is DevelopmentSlot

*Inferred · question · source: `docs/modules/portfolio-transactions/README.md`*

**Is DevelopmentSlot ever actually linked to the PotentialProject/RETransaction/Scenario it is meant to fill?** No FK connects them; only the generic ProjectEntityID is shared. Nobody has confirmed this. Recorded in modules/portfolio-transactions/README.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### What does the Org

*Inferred · question · source: `docs/modules/portfolio-transactions/README.md`*

What does the Org Chart screen (/en/admin/OrgChartEdit.jsp) actually render, and does a dedicated org-chart data structure exist that this schema dump simply does not surface?. Nobody has confirmed this. Recorded in modules/portfolio-transactions/README.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### Are ComparisonReport

*Inferred · question · source: `docs/modules/portfolio-transactions/README.md`*

**Are ComparisonReport/ComparisonItem used for site comparisons, scenario comparisons, or both?** Both are plausible from the fields (ScenarioName, ExpenseGroup); no screen was opened. Nobody has confirmed this. Recorded in modules/portfolio-transactions/README.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### What actually happens

*Inferred · question · source: `docs/modules/portfolio-transactions/site-pipeline.md`*

What actually happens when a Site is promoted? Does the platform create a brand-new Project row and copy matching fields across (address, region, DMA, prototype), or does it reuse the same ProjectEntityID and simply attach a new Project detail row to it, retiring the PotentialProject one — which the shared-key subtype model (project-entity.md §1.2) would make structurally possible? The two mechanisms have very different implications for how ASG Edge+ should model the transition. Nothing in this corpus decides it. Nobody has confirmed this. Recorded in modules/portfolio-transactions/site-pipeline.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### Does PotentialProject

*Inferred · question · source: `docs/modules/portfolio-transactions/site-pipeline.md`*

**Does PotentialProject.LocationID get set as part of promotion, or is it set at Site-creation time to say which existing Location the Site is being evaluated at?** Both readings are consistent with the schema; only a screen capture of the Site-creation form would settle it. Nobody has confirmed this. Recorded in modules/portfolio-transactions/site-pipeline.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### What do

*Inferred · question · source: `docs/modules/portfolio-transactions/site-pipeline.md`*

What do SiteToProjectSetupLayoutID and ProjectToFacilitySetupLayoutID actually render? Opening either page layout in Manage Page Layouts would show whether it hosts a conversion button, and what fields it carries — the single most valuable next capture for this question. Nobody has confirmed this. Recorded in modules/portfolio-transactions/site-pipeline.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### Can a PotentialProject

*Inferred · question · source: `docs/modules/portfolio-transactions/site-pipeline.md`*

Can a PotentialProject be promoted directly to a Facility, skipping Project? The two-layout-field evidence implies the two-step path is the normal one; nothing rules out a direct path for simpler deployments. Nobody has confirmed this. Recorded in modules/portfolio-transactions/site-pipeline.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

### Are

*Inferred · question · source: `docs/modules/portfolio-transactions/site-pipeline.md`*

**Are LandPurchaseSummary, SiteSurvey, Ownership and DemographicResults (all facilities-locations objects, soft-attached via ProjectEntityID) actually attached to a PotentialProject in a live record**, and if so, do they transfer to the Project/Facility on promotion, or stay behind? ../facilities-locations/demographics.md flags the same open question from its side. Nobody has confirmed this. Recorded in modules/portfolio-transactions/site-pipeline.md, under the Portfolio & Real-Estate Transactions area. Until it is settled, anything built on the assumption is a guess.

## Rules (16)

*Derived · group*

Every numbered rule the docs corpus records for this feature, named by a short summary. Click one: the panel opens with its ID, the full statement, and a link to the complete rule page.

### POR-R-001 — [POR-R-001](../rules/POR-R-001.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A `Contract` needs a fiscal period, discount rate, or ASC 842 threshold · `Contract.ProgramID` · Resolves to `Program`'s policy fields (`SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `FiscalYearEnd`, FX rate types) before falling back to `Firm`. Full detail in….**

|  |  |
|---|---|
| Stated as | A `Contract` needs a fiscal period, discount rate, or ASC 842 threshold |
| Stated as | `Contract.ProgramID` |
| Stated as | Resolves to `Program`'s policy fields (`SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `FiscalYearEnd`, FX rate types) before falling back to `Firm`. Full detail in `ACC-R-056`…`059` (`../accounting/`). |
| Stated as | Observed |

### POR-R-002 — [POR-R-002](../rules/POR-R-002.md)

*Inferred · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**Workflow routing needs a `REGION1`/`REGION2` assignee · `Program.RegionID` / `RootRegionID` / `SubRegionID` → `Region` · Resolves an org-chart position through the region hierarchy. `MARKET` resolves through `CodeMarketAreaID` instead, a different code table.**

|  |  |
|---|---|
| Stated as | Workflow routing needs a `REGION1`/`REGION2` assignee |
| Stated as | `Program.RegionID` / `RootRegionID` / `SubRegionID` → `Region` |
| Stated as | Resolves an org-chart position through the region hierarchy. `MARKET` resolves through `CodeMarketAreaID` instead, a different code table. |
| Stated as | Inferred — no screen confirms the exact level mapping |

### POR-R-003 — [POR-R-003](../rules/POR-R-003.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overrides the tenant-wide default from `Firm.<Subtype>SetupPageLayoutID` for that Portfolio. Two….**

|  |  |
|---|---|
| Stated as | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio |
| Stated as | `Program.<Subtype>SetupPageLayoutID` |
| Stated as | Overrides the tenant-wide default from `Firm.<Subtype>SetupPageLayoutID` for that Portfolio. Two additional fields, `SiteToProjectSetupLayoutID` and `ProjectToFacilitySetupLayoutID`, exist only on `Program` and name a conversion between subtypes rather than one subtype's own layout — see `POR-R-012`. |
| Stated as | Observed field existence; Inferred override semantics |

### POR-R-004 — [POR-R-004](../rules/POR-R-004.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A `Scenario` reaches `Contract` · `Scenario.ContractID` · One-way, optional link. `Contract` carries no reciprocal `ScenarioID`/`RETransactionID` column — a signed lease cannot be traced back to the deal that produced it via FK.**

|  |  |
|---|---|
| Stated as | A `Scenario` reaches `Contract` |
| Stated as | `Scenario.ContractID` |
| Stated as | One-way, optional link. `Contract` carries no reciprocal `ScenarioID`/`RETransactionID` column — a signed lease cannot be traced back to the deal that produced it via FK. |
| Stated as | Observed |

### POR-R-005 — [POR-R-005](../rules/POR-R-005.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A `PotentialProject`, `Program`, `Scenario`, or `RETransaction` needs a deal classification · `PotentialProject.CodeDealTypeID` / `Program.CodeDealTypeID` → `Deal Type Code` (2024); `Scenario.CodeScenarioDealTypeID` / `RETransaction.PreferredScenarioCodeDealTypeID` → `Scenario Deal Type Code`….**

|  |  |
|---|---|
| Stated as | A `PotentialProject`, `Program`, `Scenario`, or `RETransaction` needs a deal classification |
| Stated as | `PotentialProject.CodeDealTypeID` / `Program.CodeDealTypeID` → `Deal Type Code` (2024); `Scenario.CodeScenarioDealTypeID` / `RETransaction.PreferredScenarioCodeDealTypeID` → `Scenario Deal Type Code` (2059); `Scenario.CodeScenarioTypeID` → `Scenario Type Code` (2060); `RETransaction.CodeRETransactionStatusID` → `RE Transaction Status Code` (2057) |
| Stated as | Four distinct code tables classify overlapping aspects of one pipeline. Row values were never captured from the live tenant. |
| Stated as | Observed table existence and attachment; unconfirmed contents |

### POR-R-006 — [POR-R-006](../rules/POR-R-006.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A `RETransaction` is opened against a site the tenant may already occupy · `RETransaction.FacilityID` · Optional direct FK to an existing `Facility` — a renewal/expansion transaction can name its Facility before any Scenario or Contract exists. · Observed.**

|  |  |
|---|---|
| Stated as | A `RETransaction` is opened against a site the tenant may already occupy |
| Stated as | `RETransaction.FacilityID` |
| Stated as | Optional direct FK to an existing `Facility` — a renewal/expansion transaction can name its Facility before any Scenario or Contract exists. |
| Stated as | Observed |

### POR-R-007 — [POR-R-007](../rules/POR-R-007.md)

*Derived · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A rollout program needs capacity tracking · `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` · Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/`RETransaction` it is meant to fill — only the generic….**

|  |  |
|---|---|
| Stated as | A rollout program needs capacity tracking |
| Stated as | `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` |
| Stated as | Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/`RETransaction` it is meant to fill — only the generic `ProjectEntityID`. |
| Stated as | Derived |

### POR-R-008 — [POR-R-008](../rules/POR-R-008.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A user compares competing sites or scenarios · `ComparisonReport` → `ComparisonItem` · `ComparisonItem.ComputedValue`/`ExpenseGroup` hold computed comparison output; `ScenarioName`/`ScenarioDate` are plain text, not FKs — a comparison item does not hard-link to the `Scenario` row it summarises.**

|  |  |
|---|---|
| Stated as | A user compares competing sites or scenarios |
| Stated as | `ComparisonReport` → `ComparisonItem` |
| Stated as | `ComparisonItem.ComputedValue`/`ExpenseGroup` hold computed comparison output; `ScenarioName`/`ScenarioDate` are plain text, not FKs — a comparison item does not hard-link to the `Scenario` row it summarises. |
| Stated as | Observed structure; Inferred usage |

### POR-R-009 — [POR-R-009](../rules/POR-R-009.md)

*Inferred · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**Notification/routing needs to walk the org chart · `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) · Two independent hierarchies exist: the `Region` chain and the `Program` self-reference (a Portfolio rolling into a parent Portfolio). Neither is the….**

|  |  |
|---|---|
| Stated as | Notification/routing needs to walk the org chart |
| Stated as | `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) |
| Stated as | Two independent hierarchies exist: the `Region` chain and the `Program` self-reference (a Portfolio rolling into a parent Portfolio). Neither is the `OrgChart` screen's data source, which was never opened. |
| Stated as | Inferred |

### POR-R-010 — [POR-R-010](../rules/POR-R-010.md)

*Derived · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A physical site's lifecycle needs to distinguish "building it" from "leasing it" · `Project.ProjectType` = "Opening Project or Capital Project" (`Project`, `platform-tenancy`) vs. `Contract` (`contracts-leases`) · Two independent subtype roots with independent financial engines (Task/schedule….**

|  |  |
|---|---|
| Stated as | A physical site's lifecycle needs to distinguish "building it" from "leasing it" |
| Stated as | `Project.ProjectType` = "Opening Project or Capital Project" (`Project`, `platform-tenancy`) vs. `Contract` (`contracts-leases`) |
| Stated as | Two independent subtype roots with independent financial engines (Task/schedule budget vs. ASC 842 accounting engine); no schema-level FK forces one through the other. |
| Stated as | Derived, see `site-pipeline.md` §3 |

### POR-R-011 — [POR-R-011](../rules/POR-R-011.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**Any process needs to trace a `Facility`/`Location` back to the `PotentialProject` it originated from · (none — no such column exists) · Not possible via FK. `PotentialProject` has zero inbound edges in the 972-edge graph and zero Manage Data Fields exposure.**

|  |  |
|---|---|
| Stated as | Any process needs to trace a `Facility`/`Location` back to the `PotentialProject` it originated from |
| Stated as | (none — no such column exists) |
| Stated as | Not possible via FK. `PotentialProject` has zero inbound edges in the 972-edge graph and zero Manage Data Fields exposure. |
| Stated as | Observed (absence) |

### POR-R-012 — [POR-R-012](../rules/POR-R-012.md)

*Derived · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A Site is promoted toward becoming an operating asset · `Program.SiteToProjectSetupLayoutID`, then `Program.ProjectToFacilitySetupLayoutID` · Names a two-step conversion pipeline (Site → Project → Facility). The second step is corroborated by a real FK (`Project.FacilityID`, admin-labelled "Related….**

|  |  |
|---|---|
| Stated as | A Site is promoted toward becoming an operating asset |
| Stated as | `Program.SiteToProjectSetupLayoutID`, then `Program.ProjectToFacilitySetupLayoutID` |
| Stated as | Names a two-step conversion pipeline (Site → Project → Facility). The second step is corroborated by a real FK (`Project.FacilityID`, admin-labelled "Related Project Facility", optional); the first step has no FK corroboration at all. |
| Stated as | Derived (naming + partial FK); Inferred (full mechanism) — see `site-pipeline.md` |

### POR-R-013 — [POR-R-013](../rules/POR-R-013.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**`RETransaction` is created · `RETransaction.ProgramID` · Required — a transaction must belong to a Portfolio. · Observed.**

|  |  |
|---|---|
| Stated as | `RETransaction` is created |
| Stated as | `RETransaction.ProgramID` |
| Stated as | Required — a transaction must belong to a Portfolio. |
| Stated as | Observed |

### POR-R-014 — [POR-R-014](../rules/POR-R-014.md)

*Observed · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**`Scenario` is created · `Scenario.RETransactionID`, `Scenario.ProjectEntityID`, `Scenario.ScenarioDealType` · All three required. `Scenario.ScenarioType` is optional.**

|  |  |
|---|---|
| Stated as | `Scenario` is created |
| Stated as | `Scenario.RETransactionID`, `Scenario.ProjectEntityID`, `Scenario.ScenarioDealType` |
| Stated as | All three required. `Scenario.ScenarioType` is optional. |
| Stated as | Observed |

### POR-R-015 — [POR-R-015](../rules/POR-R-015.md)

*Derived · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**A `Scenario`'s deal type needs comparing against its parent transaction's preference · `Scenario.CodeScenarioDealTypeID` vs. `RETransaction.PreferredScenarioCodeDealTypeID` · Both draw from the same code table (`Scenario Deal Type Code`, 2059) but are independent fields — nothing in the schema….**

|  |  |
|---|---|
| Stated as | A `Scenario`'s deal type needs comparing against its parent transaction's preference |
| Stated as | `Scenario.CodeScenarioDealTypeID` vs. `RETransaction.PreferredScenarioCodeDealTypeID` |
| Stated as | Both draw from the same code table (`Scenario Deal Type Code`, 2059) but are independent fields — nothing in the schema enforces they match. |
| Stated as | Derived |

### POR-R-016 — [POR-R-016](../rules/POR-R-016.md)

*Derived · rule · source: `docs/modules/portfolio-transactions/rules.md`*

**`Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read · `Task/Group ID` FK type · The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, `TaskGroup`, and `TaskItem` are byte-identical 37-field….**

|  |  |
|---|---|
| Stated as | `Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read |
| Stated as | `Task/Group ID` FK type |
| Stated as | The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, `TaskGroup`, and `TaskItem` are byte-identical 37-field tables — treat the resolution as "one of the three," not as proof a deal step is never a plain `Task`. |
| Stated as | Derived, low confidence on the specific target |
