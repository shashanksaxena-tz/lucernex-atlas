# Program

*180 fields · module: Portfolio & Real-Estate Transactions · Postgres: `program`*

A capital/rollout program header — the container above ProjectEntity for a slate of related capital projects, carrying its own page-layout assignments (Cap Project Setup Page Layout, Cap Project Map Setup Layout) and exchange-rate-type overrides per cost category (Asset Amortization, Asset Balance, Cash Expenses) with matching '(Translation)' fields for multi-currency portfolios. 85 Global fields under Program Summary Information; the page-layout fields here are notable because they mean a Program's own metadata determines which page layout its child projects render with, tying this entity directly into the PAGE-LAYOUTS-01 configuration domain.

Source: `data-fields/program.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 180 |
| Catalogued fields | 85 (85 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 12 keys from 12 record types |
| Points at | 13 other records |
| Tenancy position | subtype_root |
| Rules that name it | 20 |

## What to know before rebuilding this

### 6 tenant custom columns

**Observed.** This record carries 6 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### A ProjectEntity subtype root

**Derived.** One of the nine records that are themselves a kind of ProjectEntity rather than hanging off one. The discriminator is ProjectEntityTypeName, which is how a single table serves several apparent record types.

### Census and catalogue disagree

**Observed.** The object census declares 180 fields; the Data Fields catalogue lists 85. The 95-field gap is columns the platform holds but does not expose as configurable Data Fields — a rebuild that reads only the catalogue will miss them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-001](../rules/ACC-R-001.md) | resolve Portfolio-level rate first; if none exists, Firm-level rate. Do not read the contract-level rate | Observed |
| [ACC-R-007](../rules/ACC-R-007.md) | `< RemainingEconomicLifeThreshold` ⇒ Pass; otherwise Fail. Default threshold "usually set to 75%" | Observed |
| [ACC-R-009](../rules/ACC-R-009.md) | `InitialLiabilityBalance > ThresholdFairValueControlled` ⇒ Fail. Default threshold "usually set to 90%" | Observed |
| [ACC-R-055](../rules/ACC-R-055.md) | a hold flag is set on all recurring-expense transactions (resp. percentage-rent transactions) generated during the window | Observed |
| [ACC-R-056](../rules/ACC-R-056.md) | - `PER_PERIOD` ⇒ "distributes the amortization equally among periods"; - `PER_DAY` ⇒ "distributes the amortization according to the number of days in the period", i.e. weight each period by `SLPeriod.NumberDays` | Observed |
| [ACC-R-057](../rules/ACC-R-057.md) | when true, prorate the partial period on a 28-day multiplier; and "If you have a partial period that is greater than or equal to 28 days, it will be considered a whole period by the system and will not prorate." | Observed |
| [ACC-R-058](../rules/ACC-R-058.md) | "This field determines if the program allows for matching of fiscal/calendar year rent." | Observed |
| [ACC-R-059](../rules/ACC-R-059.md) | the `Sub` variant applies to "contracts in need of translation", the plain variant to "contracts in need of revaluation" — selected per contract by `Contract.IsTranslation` (`ACC-R-044`) | Observed |
| [LAY-R-181](../rules/LAY-R-181.md) | Setup-page assignment exists at two levels: `Firm` (11 slots, tenant default) and `Program` (18 slots — 11 setup pages + 7 map popups, per Portfolio/Capital Program). Only the Firm level was observed in the UI. | Observed |
| [LAY-R-183](../rules/LAY-R-183.md) | Map Popup Layouts are a third, minimal rendering context, distinct from Summary Page and Wizard. The seven `*MapSetupLayoutID` columns sit on `Program`, not `Firm`, implying portfolio scope. | Observed |
| [FAC-R-009](../rules/FAC-R-009.md) | Effect: `Complex`'s 45-field schema contains no FK back into `Location`/`Facility`/`Parcel`/ `Prototype`/`Program`, and no `ProjectEntityID`. It is `firm_global`, not entity-scoped. | Derived |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [POR-R-001](../rules/POR-R-001.md) | A `Contract` needs a fiscal period, discount rate, or ASC 842 threshold · `Contract.ProgramID` · Resolves to `Program`'s policy fields (`SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `FiscalYearEnd`, FX rate types | Observed |
| [POR-R-002](../rules/POR-R-002.md) | Workflow routing needs a `REGION1`/`REGION2` assignee · `Program.RegionID` / `RootRegionID` / `SubRegionID` → `Region` · Resolves an org-chart position through the region hierarchy. `MARKET` resolves through `CodeMarketAreaID` instead, a di | Inferred |
| [POR-R-003](../rules/POR-R-003.md) | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overrides the tenant-wide default from `Firm. | Observed |
| [POR-R-005](../rules/POR-R-005.md) | A `PotentialProject`, `Program`, `Scenario`, or `RETransaction` needs a deal classification · `PotentialProject.CodeDealTypeID` / `Program.CodeDealTypeID` → `Deal Type Code` (2024); `Scenario.CodeScenarioDealTypeID` / `RETransaction.Preferr | Observed |
| [POR-R-007](../rules/POR-R-007.md) | A rollout program needs capacity tracking · `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` · Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/` | Derived |
| [POR-R-009](../rules/POR-R-009.md) | Notification/routing needs to walk the org chart · `Program.OrgChartProgramID` (self-reference) + `LinkRegionManager` (member-to-region assignment) · Two independent hierarchies exist: the `Region` chain and the `Program` self-reference (a  | Inferred |
| [POR-R-012](../rules/POR-R-012.md) | A Site is promoted toward becoming an operating asset · `Program.SiteToProjectSetupLayoutID`, then `Program.ProjectToFacilitySetupLayoutID` · Names a two-step conversion pipeline (Site → Project → Facility). The second step is corroborated  | Derived |
| [PRJ-R-005](../rules/PRJ-R-005.md) | A task's dates need working-day calculation · `HolidaySchedule` → `HolidayDate`, `Program.DefaultHolidayScheduleID` (`portfolio-transactions`), `Program.DefaultWorkWeekends`, `TaskGroup.TaskEndsCodeDayOfWeekID` · The portfolio's default cal | Derived |

## Fields

### Relationships (foreign keys) (29)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` |  | Template ID | — |  | [BudgetTemplate](BudgetTemplate.md) |
| `CapProjectMapSetupLayoutID` | Cap Project Map Setup Layout | item ID | Global |  | unresolved |
| `CapProjectSetupPageLayoutID` | Cap Project Setup Page Layout | item ID | Global |  | unresolved |
| `ComplexID` |  | Complex ID | — |  | [Complex](Complex.md) |
| `ContractSetupPageLayoutID` | RE Contract Setup Page Layout | item ID | Global |  | unresolved |
| `DemographicDMAID` |  | DMA ID | — |  | [DMA](DMA.md) |
| `EquipmentContractSetupPageLayoutID` | Equipment Contract Setup Page Layout | item ID | Global |  | unresolved |
| `FacilityMapSetupLayoutID` | Facility Map Setup Layout | item ID | Global |  | unresolved |
| `FacilitySetupPageLayoutID` | Facility Setup Page Layout | item ID | Global |  | unresolved |
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` |  | County ID | — |  | [Jurisdiction](Jurisdiction.md) |
| `LocationID` |  | Location ID | — |  | [Location](Location.md) |
| `LocationMapSetupLayoutID` | Location Map Setup Layout | item ID | Global |  | unresolved |
| `LocationSetupPageLayoutID` | Location Setup Page Layout | item ID | Global |  | unresolved |
| `OpenProjectMapSetupLayoutID` | Open Project Map Setup Layout | item ID | Global |  | unresolved |
| `OpenProjectSetupPageLayoutID` | Open Project Setup Page Layout | item ID | Global |  | unresolved |
| `OrgChartProgramID` | Portfolio for Org Chart | Portfolio ID | Global |  | [Program](Program.md) |
| `ParcelMapSetupLayoutID` | Parcel Map Setup Layout | item ID | Global |  | unresolved |
| `ParcelSetupPageLayoutID` | Parcel Setup Page Layout | item ID | Global |  | unresolved |
| `ProjectToFacilitySetupLayoutID` | Project To Facility Setup Layout | item ID | Global |  | unresolved |
| `PrototypeID` |  | Prototype ID | — |  | [Prototype](Prototype.md) |
| `PrototypeSetupPageLayoutID` | Prototype Setup Page Layout | item ID | Global |  | unresolved |
| `RegionID` |  | Region ID | — |  | [Region](Region.md) |
| `RootRegionID` |  | Region ID | — |  | [Region](Region.md) |
| `ScenarioMapSetupLayoutID` | Scenario Map Setup Layout | item ID | Global |  | unresolved |
| `SiteMapSetupLayoutID` | Site Map Setup Layout | item ID | Global |  | unresolved |
| `SiteSetupPageLayoutID` | Site Setup Page Layout | item ID | Global |  | unresolved |
| `SiteToProjectSetupLayoutID` | Site To Project Setup Layout | item ID | Global |  | unresolved |
| `SubRegionID` |  | Region ID | — |  | [Region](Region.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DefaultHolidayScheduleID` | Default Holiday Schedule | Holiday Calendar | Global |  |  |
| `LinkProjectEntityContactListData` |  | Contact | — |  |  |
| `ManagerIDList` |  | Dropdown | — |  |  |

### Coded values (drop-downs) (25)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAssetAmortFXTypeID` | Asset Amortization Exchange Rate Type | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeAssetAmortSubFXTypeID` | Asset Amortization Exchange Rate Type (Translation) | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeAssetBalFXTypeID` | Asset Balance Exchange Rate Type | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeAssetBalSubFXTypeID` | Asset Balance Exchange Rate Type (Translation) | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeBuildingAreaUnitID` |  | Dropdown (Building Area Unit Code) | — |  | Building Area Unit Code |
| `CodeCashExpensesFXTypeID` | Cash Expenses Exchange Rate Type | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeCashExpensesSubFXTypeID` | Cash Expenses Exchange Rate Type (Translation) | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeConstructionTypeID` |  | Dropdown (Construction Type Code) | — |  | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeDealTypeID` |  | Dropdown (Deal Type Code) | — |  | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeDesc_CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeDistributionCenterID` |  | Dropdown (Distribution Center Code) | — |  | Distribution Center Code |
| `CodeInterestFXTypeID` | Interest Exchange Rate Type | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeInterestSubFXTypeID` | Interest Exchange Rate Type (Translation) | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeLiabAmortFXTypeID` | Liability Amortization Exchange Rate Type | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeLiabAmortSubFXTypeID` | Liability Amortization Exchange Rate Type (Translation) | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeLiabilityBalFXTypeID` | Liability Balances Exchange Rate Type | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeLiabilityBalSubFXTypeID` | Liability Balances Exchange Rate Type (Translation) | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeMarketTypeID` |  | Dropdown (Market Type Code) | — |  | Market Type Code |
| `CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeSingleLeaseFXTypeID` | Single Lease Exchange Rate Type | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CodeSingleLeaseSubFXTypeID` | Single Lease Exchange Rate Type (Translation) | Dropdown (Exchange Rate Type Code) | Global |  | Exchange Rate Type Code |
| `CurrentCodeProjectPhaseID` |  | Dropdown (Project Phase Code) | — |  | Project Phase Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  | Currency | — |  |  |
| `RevenuePerWeek` | Revenue per week | Currency | Global |  |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `FairValueThreshold` | Fair Value Threshold | Percentage | Global |  |  |
| `PercentCompleteByCount` | % Projects Complete | Percentage | Global |  |  |
| `RemainingEconomicLifeThreshold` | Remaining Economic Life Threshold | Percentage | Global |  |  |
| `SLDiscountRate` | SL Discount Rate | Percentage | Global |  |  |

### Quantities (30)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualRevenueWeeks` |  | Number | — |  |  |
| `DBFolderSizeMB` |  | 2-Digit Number | — |  |  |
| `Depth` |  | Number | — |  |  |
| `EntityId` |  | Number | — |  |  |
| `Frontage` |  | Number | — |  |  |
| `LatitudeDegrees` |  | 5-Digit Number | — |  |  |
| `LongitudeDegrees` |  | 5-Digit Number | — |  |  |
| `NumProjectsComplete` | Projects Completed | Number | Global |  |  |
| `NumProjectsNotComplete` | Projects Remaining | Number | Global |  |  |
| `NumberOfDocuments` |  | Number | — |  |  |
| `NumberOfEquipPTApprovalLevels` | Number Of Equipment Contract Approval Levels | Number | Global |  |  |
| `NumberOfPTApprovalLevels` | Number of RE Contract Approval Levels | Number | Global |  |  |
| `ProgramID` | Program RecID | Number | Global |  |  |
| `ProjectEntityID` |  | Number | — |  |  |
| `RentableArea` |  | Number | — |  |  |
| `SequenceNumber` |  | Number | — |  |  |
| `TotalActiveProjects` | Total Active Projects | Number | Global |  |  |
| `TotalCapitalProjects` | Total Capital Projects | Number | Global |  |  |
| `TotalContracts` | Total Contracts | Number | Global |  |  |
| `TotalDeadProjects` | Total Dead Projects | Number | Global |  |  |
| `TotalEquipmentContracts` | Total Equipment Contracts | Number | Global |  |  |
| `TotalFacilities` | Total Facilities | Number | Global |  |  |
| `TotalInactiveProjects` | Total Inactive Projects | Number | Global |  |  |
| `TotalLocations` | Total Locations | Number | Global |  |  |
| `TotalOpeningProjects` | Total Opening Projects | Number | Global |  |  |
| `TotalParcels` | Total Parcels | Number | Global |  |  |
| `TotalProjects` | Total Projects | Number | Global |  |  |
| `TotalREContracts` | Total RE Contracts | Number | Global |  |  |
| `TotalSites` | Total Sites | Number | Global |  |  |
| `UsableArea` |  | Number | — |  |  |

### Dates & timestamps (10)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` |  | Date | — |  |  |
| `ActualStartDate` |  | Date | — |  |  |
| `BaselineEndDate` |  | Date | — |  |  |
| `CapProjectsEndDate` | Projects Completion Date | Date | Global |  |  |
| `ClientScheduleLastReviewedDate` |  | Date | — |  |  |
| `ExpectedEndDate` |  | Date | — |  |  |
| `FiscalYearEnd` | Fiscal year end | Date | Global |  |  |
| `OriginalEndDate` |  | Date | — |  |  |
| `OriginalStartDate` |  | Date | — |  |  |
| `SlotEndDate` |  | Date | — |  |  |

### Flags (7)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DefaultAutoPushForecastEndDate` | Default Auto Push Forecast End Date | Boolean | Global |  |  |
| `DefaultWorkWeekends` | Default Work Weekends | Boolean | Global |  |  |
| `Inactive` |  | Boolean | — |  |  |
| `IsDead` |  | Boolean | — |  |  |
| `SLMatchYearEnds` | SL Match Year Ends? | Boolean | Global |  |  |
| `SLProrate35As28` | SL Prorate #35 As #28? | Boolean | Global |  |  |
| `UseNewSetUpRateOnRemeasure` | New SetUp Rate on Remeasurement | Boolean | Global |  |  |

### Text & notes (62)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseProvider` |  | Text | — |  |  |
| `CapProjectsInProgram` | Projects Summary | Text | Global |  |  |
| `City` |  | Text | Global |  |  |
| `CityStateProvinceCountry` |  | Text | — |  |  |
| `ClientEntityID` |  | Text | — |  |  |
| `ComparisonList` |  | Text | — |  |  |
| `CompletedPhaseStatus` |  | Text | — |  |  |
| `ConstructionPhaseStatus` |  | Text | — |  |  |
| `CountryID` |  | Text | — |  |  |
| `CrossStreet1` |  | Text | — |  |  |
| `CrossStreet2` |  | Text | — |  |  |
| `CurrentMilestone` |  | Text | — |  |  |
| `CurrentPhaseStatus` |  | Text | — |  |  |
| `Description` |  | Text | Global |  |  |
| `DesignPhaseStatus` |  | Text | — |  |  |
| `EntityEmail` |  | Text | — |  |  |
| `EntityPhoto` |  | Text | — |  |  |
| `FacilityName` |  | Text | — |  |  |
| `FinancialModel` |  | Text | — |  |  |
| `FirmID` |  | Text | — |  |  |
| `Firm_SalesReportLogo` |  | Text | — |  |  |
| `Firm_SalesReportLogoMadewell` |  | Text | — |  |  |
| `Firm_SalesReportSignature` |  | Text | — |  |  |
| `Firm_SalesReportSignatureName` |  | Text | — |  |  |
| `Firm_SalesReportSignatureTitle` |  | Text | — |  |  |
| `HTMLAddress` |  | Text | — |  |  |
| `IssuesAndAlerts` |  | Text | — |  |  |
| `MapClientRecordID` |  | Text | — |  |  |
| `MarketsInProgram` | Markets Summary | Text | Global |  |  |
| `MilestoneTimeline` |  | Text | — |  |  |
| `NextMilestone` |  | Text | — |  |  |
| `Notes` |  | Text | — |  |  |
| `OperationsPhaseStatus` |  | Text | — |  |  |
| `Phone` |  | Text | — |  |  |
| `PossessionPhaseStatus` |  | Text | — |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `PotentialProjectName` |  | Text | — |  |  |
| `PreviousMilestone` |  | Text | — |  |  |
| `ProgramName` | Name | Text | Global | yes |  |
| `ProgramType` | Program or Portfolio | Text | Global | yes |  |
| `ProjectDescription` |  | Text | — |  |  |
| `ProjectEntityName` |  | Text | — |  |  |
| `ProjectEntityTypeName` |  | Text | — |  |  |
| `ProjectName` |  | Text | — |  |  |
| `PrototypeName` |  | Text | — |  |  |
| `PrototypesInProgram` | Prototypes Summary | Text | Global |  |  |
| `RealEstatePhaseStatus` |  | Text | — |  |  |
| `RegionsInProgram` | Regions Summary | Text | Global |  |  |
| `RelatedEntities` |  | Text | — |  |  |
| `RelocatedFrom` |  | Text | — |  |  |
| `RunReportAction` |  | Text | — |  |  |
| `SLAssetAmortizeMethod` | SL Asset Amortize Method | Text | Global |  |  |
| `SLCashAmortizeMethod` | SL Cash Amortize Method | Text | Global |  |  |
| `SLExpenseAmortizeMethod` | SL Expense Amortize Method | Text | Global |  |  |
| `StreetAddress` |  | Text | — |  |  |
| `StreetAddress1` | Street address #1 | Text | Global |  |  |
| `StreetAddress2` | Street address #2 | Text | Global |  |  |
| `StreetAddress3` | Street address #3 | Text | Global |  |  |
| `StreetAddress4` | Street address #4 | Text | Global |  |  |
| `ThirdPartyWarehouse` |  | Text | — |  |  |
| `TimeZone` |  | Text | — |  |  |
| `TradeArea` |  | Text | — |  |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Program ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` |  | Time | — |  |  |
| `ModifiedByID` |  | Member ID | — |  | [Member](Member.md) |
| `ModifiedDate` |  | Time | — |  |  |
| `RevNumber` |  | Number | — |  |  |
| `UUID` |  | Text | — |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossArea` |  | Acreage | — |  |  |

## What points here (12 keys)

| Record type | Via column |
|---|---|
| [Contract](Contract.md) | `ProgramID` |
| [DevelopmentSlot](DevelopmentSlot.md) | `ProgramID` |
| [DiscountRate](DiscountRate.md) | `ProgramID` |
| [Facility](Facility.md) | `ProgramID` |
| [FiscalPeriod](FiscalPeriod.md) | `ProgramID` |
| [Location](Location.md) | `ProgramID` |
| [Parcel](Parcel.md) | `ProgramID` |
| [PotentialProject](PotentialProject.md) | `ProgramID` |
| [Program](Program.md) | `OrgChartProgramID` |
| [Project](Project.md) | `ProgramID` |
| [Prototype](Prototype.md) | `ProgramID` |
| [RETransaction](RETransaction.md) | `ProgramID` |
