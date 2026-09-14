# Program

*180 fields · module: Portfolio & Real-Estate Transactions · Postgres: `program`*

A capital/rollout program header — the container above ProjectEntity for a slate of related capital projects, carrying its own page-layout assignments (Cap Project Setup Page Layout, Cap Project Map Setup Layout) and exchange-rate-type overrides per cost category (Asset Amortization, Asset Balance, Cash Expenses) with matching '(Translation)' fields for multi-currency portfolios. 85 Global fields under Program Summary Information; the page-layout fields here are notable because they mean a Program's own metadata determines which page layout its child projects render with, tying this entity directly into the PAGE-LAYOUTS-01 configuration domain.

Source: `data-fields/program.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 180 |
| Fields with a vendor definition | 173 of 182 inventoried |
| Physical tables | `program` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in program

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 173 fields carry a vendor definition

**Observed.** 173 of this record's 182 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 6 fields marked required

**Observed.** The inventory marks 6 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | — |  | `program.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `CapProjectMapSetupLayoutID` | Cap Project Map Setup Layout | Select the page layout you want to use when you click a pin on a Google Map in the Capital Project module from this field. | item ID | Global |  | `program.CapProjectMapSetupLayoutID · TEXT` | unresolved |
| `CapProjectSetupPageLayoutID` | Cap Project Setup Page Layout | Select the page layout you want to use for step one of the Capital Project Setup Wizard from this field. | item ID | Global |  | `program.CapProjectSetupPageLayoutID · TEXT` | unresolved |
| `ComplexID` | Complex Name | This is a default field that is not used for programs. | Complex ID | — |  | `program.ComplexID · TEXT` | [Complex](Complex.md) |
| `ContractSetupPageLayoutID` | RE Contract Setup Page Layout | Select the page layout you want to use for step one of the RE Contract Setup Wizard from this field. | item ID | Global |  | `program.ContractSetupPageLayoutID · TEXT` | unresolved |
| `DemographicDMAID` | Demographic DMA | Select your demographic market area from this field. | DMA ID | — |  | `program.DemographicDMAID · TEXT` | [DMA](DMA.md) |
| `EquipmentContractSetupPageLayoutID` | Equipment Contract Setup Page Layout | Select the page layout you want to use for step one of the Equipment Contract Setup Wizard from this field. | item ID | Global |  | `program.EquipmentContractSetupPageLayoutID · TEXT` | unresolved |
| `FacilityMapSetupLayoutID` | Facility Map Setup Layout | Select the page layout you want to use when you click a pin on a Google Map in the Facility module from this field. | item ID | Global |  | `program.FacilityMapSetupLayoutID · TEXT` | unresolved |
| `FacilitySetupPageLayoutID` | Facility Setup Page Layout | Select the page layout you want to use for step one of the Facility Setup Wizard from this field. | item ID | Global |  | `program.FacilitySetupPageLayoutID · TEXT` | unresolved |
| `IStateProvinceCountryID` | State | This is a default field that is not used for programs. | Country, State, County ID | Global |  | `program.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | — |  | `program.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | This is a default field that is not used for programs. | Location ID | — |  | `program.LocationID · TEXT` | [Location](Location.md) |
| `LocationMapSetupLayoutID` | Location Map Setup Layout | Select the page layout you want to use when you click a pin on a Google Map in the Location module from this field. | item ID | Global |  | `program.LocationMapSetupLayoutID · TEXT` | unresolved |
| `LocationSetupPageLayoutID` | Location Setup Page Layout | Select the page layout you want to use for step one of the Location Setup Wizard from this field. | item ID | Global |  | `program.LocationSetupPageLayoutID · TEXT` | unresolved |
| `OpenProjectMapSetupLayoutID` | Open Project Map Setup Layout | Select the page layout you want to use when you click a pin on a Google Map in the Project module from this field. | item ID | Global |  | `program.OpenProjectMapSetupLayoutID · TEXT` | unresolved |
| `OpenProjectSetupPageLayoutID` | Open Project Setup Page Layout | Select the page layout you want to use for step one of the Opening Project Setup Wizard from this field. | item ID | Global |  | `program.OpenProjectSetupPageLayoutID · TEXT` | unresolved |
| `OrgChartProgramID` | Portfolio for Org Chart | This field determines the org chart for the program. | Portfolio ID | Global |  | `program.OrgChartProgramID · TEXT` | [Program](Program.md) |
| `ParcelMapSetupLayoutID` | Parcel Map Setup Layout | Select the page layout you want to use when you click a pin on a Google Map in the Parcel module from this field. | item ID | Global |  | `program.ParcelMapSetupLayoutID · TEXT` | unresolved |
| `ParcelSetupPageLayoutID` | Parcel Setup Page Layout | Select the page layout you want to use for step one of the Parcel Setup Wizard from this field. | item ID | Global |  | `program.ParcelSetupPageLayoutID · TEXT` | unresolved |
| `ProjectToFacilitySetupLayoutID` | Project To Facility Setup Layout | This field determines the project to facility setup layout page for this program. | item ID | Global |  | `program.ProjectToFacilitySetupLayoutID · TEXT` | unresolved |
| `PrototypeID` | Prototype | This is a default field that is not used for programs. | Prototype ID | — |  | `program.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `PrototypeSetupPageLayoutID` | Prototype Setup Page Layout | Select the page layout you want to use for step one of the Prototype Setup Wizard from this field. | item ID | Global |  | `program.PrototypeSetupPageLayoutID · TEXT` | unresolved |
| `RegionID` | Region | This is a default field that is not used for programs. | Region ID | — |  | `program.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | — |  | `program.RootRegionID · TEXT` | [Region](Region.md) |
| `ScenarioMapSetupLayoutID` | Scenario Map Setup Layout |  | item ID | Global |  | `program.ScenarioMapSetupLayoutID · TEXT` | unresolved |
| `SiteMapSetupLayoutID` | Site Map Setup Layout | Select the page layout you want to use when you click a pin on a Google Map in the Site module from this field. | item ID | Global |  | `program.SiteMapSetupLayoutID · TEXT` | unresolved |
| `SiteSetupPageLayoutID` | Site Setup Page Layout | Select the page layout you want to use for step one of the Site Setup Wizard from this field. | item ID | Global |  | `program.SiteSetupPageLayoutID · TEXT` | unresolved |
| `SiteToProjectSetupLayoutID` | Site To Project Setup Layout | This field determines the site to project setup layout page for this program. | item ID | Global |  | `program.SiteToProjectSetupLayoutID · TEXT` | unresolved |
| `SubRegionID` | Sub Region | The sub-region. | Region ID | — |  | `program.SubRegionID · TEXT` | [Region](Region.md) |

### Soft references (3)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DefaultHolidayScheduleID` | Default Holiday Schedule | Select the default holiday calendar you want to use from this field. | Holiday Calendar | Global |  | `program.DefaultHolidayScheduleID · TEXT` |  |
| `LinkProjectEntityContactListData` | Contact List | This field returns a list of Active and Inactive entities filtered by member security. | Contact | — |  | `program.LinkProjectEntityContactListData · TEXT` |  |
| `ManagerIDList` | Project Managers | This is a generic field that you can add to a page layout. In View mode, this field returns a list of managers assigned to the entity by the org chart and managers assigned to the entity on an ad hoc basis. In Edit mode, this field allows you to add managers to your entity. | Dropdown | — |  | `program.ManagerIDList · TEXT` |  |

### Coded values (drop-downs) (25)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAssetAmortFXTypeID` | Asset Amortization Exchange Rate Type | Select the foreign exchange rate type you want to use for your asset amortization conversions for contracts in need of revaluation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeAssetAmortFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeAssetAmortSubFXTypeID` | Asset Amortization Exchange Rate Type (Translation) | Select the foreign exchange rate type you want to use for your asset amortization conversions for contracts in need of translation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeAssetAmortSubFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeAssetBalFXTypeID` | Asset Balance Exchange Rate Type | Select the foreign exchange rate type you want to use for your asset balance conversions for contracts in need of revaluation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeAssetBalFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeAssetBalSubFXTypeID` | Asset Balance Exchange Rate Type (Translation) | Select the foreign exchange rate type you want to use for your asset balance conversions for contracts in need of translation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeAssetBalSubFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | — |  | `program.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCashExpensesFXTypeID` | Cash Expenses Exchange Rate Type | Select the foreign exchange rate type you want to use for your cash expense conversions for contracts in need of revaluation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeCashExpensesFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeCashExpensesSubFXTypeID` | Cash Expenses Exchange Rate Type (Translation) | Select the foreign exchange rate type you want to use for your cash expense conversions for contracts in need of translation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeCashExpensesSubFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeConstructionTypeID` | Construction Type | This is a default field that is not used for programs. | Dropdown (Construction Type Code) | — |  | `program.CodeConstructionTypeID · TEXT` | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `program.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDealTypeID` | Deal Type | This is a generic field. It is not implemented for portfolios or programs by default. | Dropdown (Deal Type Code) | — |  | `program.CodeDealTypeID · TEXT` | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | The description of the market. | Dropdown (Market Area Code) | — |  | `program.CodeDesc_CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | This is a generic field. It is not implemented for portfolios or programs by default. | Dropdown (Project Type Code) | — |  | `program.CodeDesc_CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | This is a default field that is not being used for programs. | Dropdown (Distribution Center Code) | — |  | `program.CodeDistributionCenterID · TEXT` | Distribution Center Code |
| `CodeInterestFXTypeID` | Interest Exchange Rate Type | Select the foreign exchange rate type you want to use for your interest conversions for contracts in need of revaluation. This field sets your default settings for your portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeInterestFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeInterestSubFXTypeID` | Interest Exchange Rate Type (Translation) | Select the foreign exchange rate type you want to use for your interest conversions for contracts in need of translation. This field sets your default settings for your portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeInterestSubFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeLiabAmortFXTypeID` | Liability Amortization Exchange Rate Type | Select the foreign exchange rate type you want to use for your liability amortization expense conversions for contracts in need of revaluation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeLiabAmortFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeLiabAmortSubFXTypeID` | Liability Amortization Exchange Rate Type (Translation) | Select the foreign exchange rate type you want to use for your liability amortization expense conversions for contracts in need of translation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeLiabAmortSubFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeLiabilityBalFXTypeID` | Liability Balances Exchange Rate Type | Select the foreign exchange rate type you want to use for your liability balance conversions for contracts in need of revaluation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeLiabilityBalFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeLiabilityBalSubFXTypeID` | Liability Balances Exchange Rate Type (Translation) | Select the foreign exchange rate type you want to use for your liability balance conversions for contracts in need of translation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeLiabilityBalSubFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeMarketAreaID` | Market Area | This is a default field that is not used for programs. | Dropdown (Market Area Code) | — |  | `program.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | This is a generic field. It is not implemented for portfolios or programs by default. | Dropdown (Market Type Code) | — |  | `program.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeProjectTypeID` | Project Type | This is a generic field. It is not implemented for portfolios or programs by default. | Dropdown (Project Type Code) | — |  | `program.CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeSingleLeaseFXTypeID` | Single Lease Exchange Rate Type | Select the foreign exchange rate type you want to use for your single lease expense conversions for contracts in need of revaluation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeSingleLeaseFXTypeID · TEXT` | Exchange Rate Type Code |
| `CodeSingleLeaseSubFXTypeID` | Single Lease Exchange Rate Type (Translation) | Select the foreign exchange rate type you want to use for your single lease expense conversions for contracts in need of translation. This field sets your default settings for a portfolio. | Dropdown (Exchange Rate Type Code) | Global |  | `program.CodeSingleLeaseSubFXTypeID · TEXT` | Exchange Rate Type Code |
| `CurrentCodeProjectPhaseID` | Project Phase | This is a default field that is not used for portfolios or programs. | Dropdown (Project Phase Code) | — |  | `program.CurrentCodeProjectPhaseID · TEXT` | Project Phase Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |
| `RevenuePerWeek` | Revenue per week | The revenue per week for the program. | Currency | Global |  | `program.RevenuePerWeek · TEXT` |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `FairValueThreshold` | Fair Value Threshold | Enter the fraction of the fair value of the underlying asset that you would like to test against to determine whether to treat this lease as a financing- / purchase-type lease or an operating lease. This value is usually set to 90%. This field is used in the ASC 842 Test. | Percentage | Global |  | `program.FairValueThreshold · TEXT` |  |
| `PercentCompleteByCount` | % Projects Complete | Calculates the percentage of capital projects in the program that have been completed. | Percentage | Global |  | `program.PercentCompleteByCount · TEXT` |  |
| `RemainingEconomicLifeThreshold` | Remaining Economic Life Threshold | Enter the fraction of the economic life of the underlying asset that amounts to a major part of the scheduled accounting period. This value is usually set to 75%. This field is used in the ASC 842 Test. | Percentage | Global |  | `program.RemainingEconomicLifeThreshold · TEXT` |  |
| `SLDiscountRate` | SL Discount Rate | Enter the default discount rate for your company here. The discount rate is also known as the Interest Rate or Internal Borrower Rate (IBR) To enter a discount rate, enter the number no % or decimal is necessary. | Percentage | Global |  | `program.SLDiscountRate · TEXT` |  |

### Quantities (30)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | This is a default field that is not used for programs. | Number | — |  | `program.ActualRevenueWeeks · TEXT` |  |
| `DBFolderSizeMB` | Storage Size (MB) | The folder size in megabytes for a given entity. | 2-Digit Number | — |  | `program.DBFolderSizeMB · TEXT` |  |
| `Depth` |  | The depth of the associated entity. | Number | — |  | `program.Depth · TEXT` |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | — |  | `program.EntityId · TEXT` |  |
| `Frontage` |  | This is a default field that is not used for programs. | Number | — |  | `program.Frontage · TEXT` |  |
| `LatitudeDegrees` | Latitude | This is a default field that is not used for programs. | 5-Digit Number | — |  | `program.LatitudeDegrees · TEXT` |  |
| `LongitudeDegrees` | Longitude | This is a default field that is not used for programs. | 5-Digit Number | — |  | `program.LongitudeDegrees · TEXT` |  |
| `NumProjectsComplete` | Projects Completed | The number of completed capital projects in the program. | Number | Global |  | `program.NumProjectsComplete · TEXT` |  |
| `NumProjectsNotComplete` | Projects Remaining | The number of incomplete capital projects in the program. | Number | Global |  | `program.NumProjectsNotComplete · TEXT` |  |
| `NumberOfDocuments` | Number of Documents | The total number of documents in all folders on the entity. | Number | — |  | `program.NumberOfDocuments · TEXT` |  |
| `NumberOfEquipPTApprovalLevels` | Number Of Equipment Contract Approval Levels | Enter the number of approval levels you want for equipment contracts in this field. Approval levels are configured on the Manage Members / Contacts page. | Number | Global |  | `program.NumberOfEquipPTApprovalLevels · TEXT` |  |
| `NumberOfPTApprovalLevels` | Number of RE Contract Approval Levels | Enter the number of approval levels you want for real estate contracts in this field. Approval levels are configured on the Manage Members / Contacts page. | Number | Global |  | `program.NumberOfPTApprovalLevels · TEXT` |  |
| `ProgramID` | Program RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `program.ProgramID · VARCHAR(64) NOT NULL` |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | — |  | `program.ProjectEntityID · TEXT` |  |
| `RentableArea` | Rentable Area | Enter the rentable area in this field. | Number | — |  | `program.RentableArea · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | — |  | `program.SequenceNumber · TEXT` |  |
| `TotalActiveProjects` | Total Active Projects | The total number of active projects in the portfolio. | Number | Global |  | `program.TotalActiveProjects · TEXT` |  |
| `TotalCapitalProjects` | Total Capital Projects | The total number of capital projects in the portfolio. | Number | Global |  | `program.TotalCapitalProjects · TEXT` |  |
| `TotalContracts` | Total Contracts | The total number of contracts in the portfolio. | Number | Global |  | `program.TotalContracts · TEXT` |  |
| `TotalDeadProjects` | Total Dead Projects | The total number of dead projects in the portfolio. | Number | Global |  | `program.TotalDeadProjects · TEXT` |  |
| `TotalEquipmentContracts` | Total Equipment Contracts | The total number of equipment contracts in the portfolio. | Number | Global |  | `program.TotalEquipmentContracts · TEXT` |  |
| `TotalFacilities` | Total Facilities | The total number of facilities in the portfolio. | Number | Global |  | `program.TotalFacilities · TEXT` |  |
| `TotalInactiveProjects` | Total Inactive Projects | The total number of inactive projects in the portfolio. | Number | Global |  | `program.TotalInactiveProjects · TEXT` |  |
| `TotalLocations` | Total Locations | The total number of locations in the portfolio. | Number | Global |  | `program.TotalLocations · TEXT` |  |
| `TotalOpeningProjects` | Total Opening Projects | The total number of opening projects in the portfolio. | Number | Global |  | `program.TotalOpeningProjects · TEXT` |  |
| `TotalParcels` | Total Parcels | The total number of parcels in the portfolio. | Number | Global |  | `program.TotalParcels · TEXT` |  |
| `TotalProjects` | Total Projects | The total number of projects in the portfolio. | Number | Global |  | `program.TotalProjects · TEXT` |  |
| `TotalREContracts` | Total RE Contracts | The total number of real estate contracts in the portfolio. | Number | Global |  | `program.TotalREContracts · TEXT` |  |
| `TotalSites` | Total Sites | The total number of sites in the portfolio. | Number | Global |  | `program.TotalSites · TEXT` |  |
| `UsableArea` | Usable Area | The usable area. | Number | — |  | `program.UsableArea · TEXT` |  |

### Dates & timestamps (10)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | — |  | `program.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Forecast/Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | — |  | `program.ActualStartDate · TEXT` |  |
| `BaselineEndDate` | Baseline Delivery Date | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | — |  | `program.BaselineEndDate · TEXT` |  |
| `CapProjectsEndDate` | Projects Completion Date | The latest end date for all of the program's projects. | Date | Global |  | `program.CapProjectsEndDate · TEXT` |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This field displays the last updated date. | Date | — |  | `program.ClientScheduleLastReviewedDate · TEXT` |  |
| `ExpectedEndDate` | Original Delivery Date | This is a default field that is not used for programs. | Date | — |  | `program.ExpectedEndDate · TEXT` |  |
| `FiscalYearEnd` | Fiscal year end | Select the month and day that your fiscal year ends from these fields. | Date | Global |  | `program.FiscalYearEnd · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `program.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `program.OriginalStartDate · TEXT` |  |
| `SlotEndDate` | RE Planner Open Date | This is a default field that is not used for programs. | Date | — |  | `program.SlotEndDate · TEXT` |  |

### Flags (7)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DefaultAutoPushForecastEndDate` | Default Auto Push Forecast End Date | Select this check box if you want to increment schedule tasks by one day each day that a task is late. This setting only applies to the forecast / actual date. | Boolean | Global |  | `program.DefaultAutoPushForecastEndDate · TEXT` |  |
| `DefaultWorkWeekends` | Default Work Weekends | Select the Yes option if you want new schedules to include weekends as working days by default. Select No if you do not want new schedules to include weekends as working days by default. | Boolean | Global |  | `program.DefaultWorkWeekends · TEXT` |  |
| `Inactive` | Is Inactive? | If selected, this check box indicates the entity is inactive. | Boolean | — | yes | `program.Inactive · TEXT` |  |
| `IsDead` | Is Dead? | If selected, this check box indicates the entity is dead. | Boolean | — |  | `program.IsDead · TEXT` |  |
| `SLMatchYearEnds` | SL Match Year Ends? | This field determines if the program allows for matching of fiscal/calendar year rent. | Boolean | Global |  | `program.SLMatchYearEnds · TEXT` |  |
| `SLProrate35As28` | SL Prorate #35 As #28? | Select the Yes option if you would like to prorate partial first and last periods based on a 28-day multiplier. This setting only impacts values calculated per period. If you have a partial period that is greater than or equal to 28 days, it will be considered a whole period by the system and will not prorate. | Boolean | Global |  | `program.SLProrate35As28 · TEXT` |  |
| `UseNewSetUpRateOnRemeasure` | New SetUp Rate on Remeasurement | There are two options for this portfolio-level setting: Commencement, where the rate equals the Cash (spot) rate that is closest to but not before lease commencement, and Schedule Begin, where the rate equals the Cash (spot) rate that is closest to but not before the Schedule Begin Date. | Boolean | Global |  | `program.UseNewSetUpRateOnRemeasure · TEXT` |  |

### Text & notes (62)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | — |  | `program.BaseProvider · TEXT` |  |
| `CapProjectsInProgram` | Projects Summary | This field generates a list of all capital projects in the program. | Text | Global |  | `program.CapProjectsInProgram · TEXT` |  |
| `City` |  | The city associated with this record. | Text | Global |  | `program.City · TEXT` |  |
| `CityStateProvinceCountry` | City, State | The city and state / province. If there is no state / province, the field returns only the city. If there is no city, this field returns only the state / province. | Text | — |  | `program.CityStateProvinceCountry · TEXT` |  |
| `ClientEntityID` | Store Number | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | — |  | `program.ClientEntityID · TEXT` |  |
| `ComparisonList` | Comparison List | When added to a page layout, this field allows for a comparison of entities from a page or subpage. | Text | — |  | `program.ComparisonList · TEXT` |  |
| `CompletedPhaseStatus` | Completed Phase Status | The milestone timeline status of the entity. This status is updated when a milestone is completed. | Text | — |  | `program.CompletedPhaseStatus · TEXT` |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This is a default field that is not used for programs. | Text | — |  | `program.ConstructionPhaseStatus · TEXT` |  |
| `CountryID` | Country | This is a default field that is not used for programs. | Text | — |  | `program.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | Enter the first cross street in this field. | Text | — |  | `program.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | Enter the second cross street in this field. | Text | — |  | `program.CrossStreet2 · TEXT` |  |
| `CurrentMilestone` | Current Milestone | The current milestone task of your entity schedule. | Text | — |  | `program.CurrentMilestone · TEXT` |  |
| `CurrentPhaseStatus` | Project Status | This is a default field that is not used for portfolios or programs. | Text | — |  | `program.CurrentPhaseStatus · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `program.Description · TEXT` |  |
| `DesignPhaseStatus` | Design Phase Status | This is a default field that is not used for programs. | Text | — |  | `program.DesignPhaseStatus · TEXT` |  |
| `EntityEmail` | Entity Email | The entity's email address that is created when the Email into Lx functionality is enabled. | Text | — |  | `program.EntityEmail · TEXT` |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | — |  | `program.EntityPhoto · TEXT` |  |
| `FacilityName` | Facility Name | The name of the facility associated with this entity. | Text | — |  | `program.FacilityName · TEXT` |  |
| `FinancialModel` | Financial Model | When added to a page layout, this field appears as a button that generates an Excel Financial Model spreadsheet. If you have questions about this functionality, contact your Accruent representative. | Text | — |  | `program.FinancialModel · TEXT` |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | — | yes | `program.FirmID · TEXT` |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | — |  | `program.Firm_SalesReportLogo · TEXT` |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | — |  | `program.Firm_SalesReportSignature · TEXT` |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | — |  | `program.Firm_SalesReportSignatureName · TEXT` |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | — |  | `program.Firm_SalesReportSignatureTitle · TEXT` |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | — |  | `program.HTMLAddress · TEXT` |  |
| `IssuesAndAlerts` | Issues And Alerts | This field can be added to page layouts. In View mode, this field will display a table with form and workflow data, such as the work flow / form type, critical issue count, non-critical issue count, escalated count, and past due notification count. | Text | — |  | `program.IssuesAndAlerts · TEXT` |  |
| `MapClientRecordID` | Client Unique ID | The entity Map Client Record ID. | Text | — |  | `program.MapClientRecordID · TEXT` |  |
| `MarketsInProgram` | Markets Summary | This field generates a list of all markets in the portfolio. | Text | Global |  | `program.MarketsInProgram · TEXT` |  |
| `MilestoneTimeline` | Milestone Timeline | This field generates a list of all milestones, but hides those with no values. | Text | — |  | `program.MilestoneTimeline · TEXT` |  |
| `NextMilestone` | Next Milestone | The upcoming milestone in the milestone timeline. | Text | — |  | `program.NextMilestone · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | — |  | `program.Notes · TEXT` |  |
| `OperationsPhaseStatus` | Operations Phase Status | This is a default field that is not used for programs. | Text | — |  | `program.OperationsPhaseStatus · TEXT` |  |
| `Phone` |  | This field can be used to store a phone number. | Text | — |  | `program.Phone · TEXT` |  |
| `PossessionPhaseStatus` | Possession Phase Status | This is a default field that is not used for programs. | Text | — |  | `program.PossessionPhaseStatus · TEXT` |  |
| `PostalCode` | Postal Code | This is a default field that is not used for programs. | Text | Global |  | `program.PostalCode · TEXT` |  |
| `PotentialProjectName` | Site Name | This is a default field that is not used for programs. | Text | — |  | `program.PotentialProjectName · TEXT` |  |
| `PreviousMilestone` | Previous Milestone | The previous milestone task. | Text | — |  | `program.PreviousMilestone · TEXT` |  |
| `ProgramName` | Name | Enter the name of the portfolio in this field. | Text | Global | yes | `program.ProgramName · TEXT` |  |
| `ProgramType` | Program or Portfolio | This field has one of two values: program or portfolio. | Text | Global | yes | `program.ProgramType · TEXT` |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | — |  | `program.ProjectDescription · TEXT` |  |
| `ProjectEntityName` | Name | The entity name. | Text | — | yes | `program.ProjectEntityName · TEXT` |  |
| `ProjectEntityTypeName` | Entity Type | The entity type. | Text | — |  | `program.ProjectEntityTypeName · TEXT` |  |
| `ProjectName` | Project Name | The name of the project associated with the record. | Text | — |  | `program.ProjectName · TEXT` |  |
| `PrototypeName` | Prototype Name | This is a default field that is not used for programs. | Text | — |  | `program.PrototypeName · TEXT` |  |
| `PrototypesInProgram` | Prototypes Summary | This field generates a list of all prototypes in the portfolio. | Text | Global |  | `program.PrototypesInProgram · TEXT` |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This is a default field that is not used for programs. | Text | — |  | `program.RealEstatePhaseStatus · TEXT` |  |
| `RegionsInProgram` | Regions Summary | This field generates a list of all regions in the portfolio. | Text | Global |  | `program.RegionsInProgram · TEXT` |  |
| `RelatedEntities` | Related Entities | The name of entities associated with this entity. | Text | — |  | `program.RelatedEntities · TEXT` |  |
| `RelocatedFrom` |  | This field is not implemented for programs. | Text | — |  | `program.RelocatedFrom · TEXT` |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | — |  | `program.RunReportAction · TEXT` |  |
| `SLAssetAmortizeMethod` | SL Asset Amortize Method | Select the appropriate option for how you want the system to calculate the amortization of Assets in Straight Line schedules. There are two options: Per Day, and Per Period. By Period distributes the amortization equally among periods, and Per Day distributes the amortization according to the number of days in the period. This setting impacts only ASC 842 Finance leases. | Text | Global |  | `program.SLAssetAmortizeMethod · TEXT` |  |
| `SLCashAmortizeMethod` | SL Cash Amortize Method | Select the appropriate option for how you would like the system to calculate the amortization of Cash Rent in Straight Line schedules. | Text | Global |  | `program.SLCashAmortizeMethod · TEXT` |  |
| `SLExpenseAmortizeMethod` | SL Expense Amortize Method | Select the appropriate option for how you would like the system to calculate the amortization of Rent Expense in Straight Line schedules. | Text | Global |  | `program.SLExpenseAmortizeMethod · TEXT` |  |
| `StreetAddress` | Street Address | The street address. | Text | — |  | `program.StreetAddress · TEXT` |  |
| `StreetAddress1` | Street address #1 | The first line of the street address. | Text | Global |  | `program.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street address #2 | The second line of the street address. | Text | Global |  | `program.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street address #3 | The third line of the street address. | Text | Global |  | `program.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street address #4 | The fourth line of the street address. | Text | Global |  | `program.StreetAddress4 · TEXT` |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | This is a default field that is not used for programs. | Text | — |  | `program.ThirdPartyWarehouse · TEXT` |  |
| `TimeZone` | Time Zone | This is a default field that is not used for programs. | Text | — |  | `program.TimeZone · TEXT` |  |
| `TradeArea` | Trade Area | The trade area. | Text | — |  | `program.TradeArea · TEXT` |  |

### Audit & record keeping (7)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Program ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `program.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `program.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `program.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | — |  | `program.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | — |  | `program.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | `program.RevNumber · TEXT` |  |
| `UUID` | Entity UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | — |  | `program.UUID · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossArea` | Gross Acreage | This is a default field that is not used for programs. | Acreage | — |  | `program.GrossArea · TEXT` |  |

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
