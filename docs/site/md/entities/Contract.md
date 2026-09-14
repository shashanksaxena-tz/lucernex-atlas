# Contract

*570 fields, split across 4 physical tables · module: Contracts & Leases · Postgres: `contract_admin,contract_financial,contract_firm,contract_firm1`*

The lease/contract header record itself — the central entity the rest of the schema hangs off of. It mixes core lease terms (dates, base rent, discount rate, renewal options) with dozens of Boolean 'in lease?' flags (Automatic Renewal In Lease?, Bargain Renewal In Lease?) that record whether a clause exists versus whether it has been exercised, plus SUBMITBUTTON fields that are workflow triggers rather than data. At 402 fields (255 Global + 147 Firm) it is also the entity this tenant has customized the most — 147 of the 205 total Firm-scope fields attach here, confirming Contract is where ASG has extended Lx's base model with tenant-specific CAM, co-tenancy, and delivery-requirement fields.

Source: `data-fields/contract.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 570 |
| Catalogued fields | 402 (255 global, 147 firm) |
| Physical tables | 4 |
| Referenced by | 62 keys from 62 record types |
| Points at | 18 other records |
| Tenancy position | subtype_root |
| Rules that name it | 26 |

## What to know before rebuilding this

### Split across 4 physical tables

**Observed.** The logical record and the physical rows are not one to one: its columns are spread over contract_admin,contract_financial,contract_firm,contract_firm1. That is the platform working around a column-count ceiling, and any rebuild has to decide deliberately whether to reproduce the split or collapse it.

### 259 tenant custom columns

**Observed.** This record carries 258 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. A further 1 use the zFirm_ spelling instead. That is direct evidence for database-per-tenant and against a shared schema.

### A ProjectEntity subtype root

**Derived.** One of the nine records that are themselves a kind of ProjectEntity rather than hanging off one. The discriminator is ProjectEntityTypeName, which is how a single table serves several apparent record types.

### Census and catalogue disagree

**Observed.** The object census declares 570 fields; the Data Fields catalogue lists 402. The 168-field gap is columns the platform holds but does not expose as configurable Data Fields — a rebuild that reads only the catalogue will miss them.

### 147 catalogued Firm-scope fields

**Observed.** Of 402 catalogued fields on this record, 147 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

### A hub: 62 keys point here

**Observed.** 62 record types hold a foreign key into this one, so it sits at the centre of the relationship graph. Changing its key or its identity is a change to AccrualTransaction, AcctingAssumptionAdjust, Allowance, AllowanceTransaction and 58 others.

### Equipment contracts live in this table

**Observed.** There is no EquipmentContract table in any inventory. An equipment contract is a Contract row discriminated by ProjectEntityTypeName = "Equipment Contract" — with a space in the value. Any query that filters contracts has to account for that, and any rebuild has to decide whether the discriminator survives.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-001](../rules/ACC-R-001.md) | resolve Portfolio-level rate first; if none exists, Firm-level rate. Do not read the contract-level rate | Observed |
| [ACC-R-002](../rules/ACC-R-002.md) | if `Contract.DiscountRate` is populated it is the rate used; otherwise `ComputedSLDiscountRate` | Inferred |
| [ACC-R-007](../rules/ACC-R-007.md) | `< RemainingEconomicLifeThreshold` ⇒ Pass; otherwise Fail. Default threshold "usually set to 75%" | Observed |
| [ACC-R-014](../rules/ACC-R-014.md) | take the most recently locked row's `FinalResult` | Observed |
| [ACC-R-016](../rules/ACC-R-016.md) | - `TermLength = ExpireDate − CommenceDate` (the contractual term); - `LikelyTermLength` = length through the last term marked Likely on `Abstract Info > Terms`; - `LastLikelyOptionDate` = end date of the last likely term; - `TestTermLength` | Observed |
| [ACC-R-017](../rules/ACC-R-017.md) | `Topic842BeginDate = max(adoption date, PossessionBeginDate)`; `Topic842EndDate` = end of accounting including likely options | Observed |
| [ACC-R-058](../rules/ACC-R-058.md) | "This field determines if the program allows for matching of fiscal/calendar year rent." | Observed |
| [ACC-R-059](../rules/ACC-R-059.md) | the `Sub` variant applies to "contracts in need of translation", the plain variant to "contracts in need of revaluation" — selected per contract by `Contract.IsTranslation` (`ACC-R-044`) | Observed |
| [ACC-R-061](../rules/ACC-R-061.md) | the form type declares attachability as a Boolean per entity kind. For this form type, only `Portfolio` = Yes and `RE Contract` = Yes; `Capital Program`, `Prototype`, `Location`, `Parcel`, `Site`, `Project`, `Facility`, `Capital Project` an | Observed |
| [ACC-R-062](../rules/ACC-R-062.md) | all three ASC 842 steps use `Member` — a named approver, resolved at configuration time rather than by org-chart position | Observed |
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |
| [CON-R-022](../rules/CON-R-022.md) | Determining the discount rate: look up DiscountRate by accounting method + contract use + geography + a min/max-scheduled-months band, and stamp it onto Contract.DiscountRate. | Derived |
| [CON-R-023](../rules/CON-R-023.md) | Determining the fiscal calendar: the calendar is owned by Contract.ProgramID (the portfolio), not by the firm. | Observed |
| [CON-R-025](../rules/CON-R-025.md) | Computing rent rollups: 120 denormalised sTYPE_MONEY fields on Contract cross {Calendar,Fiscal}×{Base,Total}×{with,without tax}×{period buckets}. | Observed |
| [CON-R-026](../rules/CON-R-026.md) | Any rollup is read: the rollups are denormalised and can be stale — Contract carries no recalculation flag equivalent to SLSummary's. | Derived |
| [CON-R-069](../rules/CON-R-069.md) | A percentage-rent clause is flagged ExtFinalPeriodToLeaseExpDt: the final period extends to lease expiry instead of truncating at the usual period boundary. | Observed |
| [CON-R-144](../rules/CON-R-144.md) | The tenant needs a lifecycle status: Contract.Firm_LeaseStatus (a Firm-scope custom code field, with a Firm_LeaseStatusNotes companion) is ASG's own answer, sitting in the same Contract Info sub-group as the platform's status field — not to | Observed |
| [FAC-R-011](../rules/FAC-R-011.md) | Input: `Parcel.MasterParcelID` (self-reference, typed `Parcel ID`). Effect: Mirrors `Contract.MasterContractID`'s master/sub pattern exactly — a parcel of land can be split, with each resulting parcel pointing back at the original. | Observed |
| [FAC-R-012](../rules/FAC-R-012.md) | Input: `Contract.FacilityID`, `Contract.LocationID` (both present, both optional per 009). Effect: A lease can be tied to a Location without a Facility, a Facility without going through a Location lookup, or both at once — the two attachmen | Observed |
| [FAC-R-013](../rules/FAC-R-013.md) | Effect: From `Facility`'s own Related Fields sidebar, `Contract` does not appear as a related lookup at all; instead the Facility Summary layout embeds an **"ASG Contract List (One to Many List)"** child grid. | Observed |
| [PPL-R-005](../rules/PPL-R-005.md) | Both `CompanyID` and `ContactID` are independently nullable | Derived |
| [AST-R-003](../rules/AST-R-003.md) | Input: `Asset.FinancialContractID`, typed `Contract ID`. Effect: Ties the asset to the equipment-flavour `Contract` that finances it, independent of the entity it is physically scoped to. | Observed |
| [POR-R-001](../rules/POR-R-001.md) | A `Contract` needs a fiscal period, discount rate, or ASC 842 threshold · `Contract.ProgramID` · Resolves to `Program`'s policy fields (`SLDiscountRate`, `FairValueThreshold`, `RemainingEconomicLifeThreshold`, `FiscalYearEnd`, FX rate types | Observed |
| [POR-R-003](../rules/POR-R-003.md) | A user opens a `Facility`/`Location`/`Parcel`/`Prototype`/`Contract`/`CapProject`/`OpenProject`/`EquipmentContract` detail screen under a given Portfolio · `Program.<Subtype>SetupPageLayoutID` · Overrides the tenant-wide default from `Firm. | Observed |
| [POR-R-004](../rules/POR-R-004.md) | A `Scenario` reaches `Contract` · `Scenario.ContractID` · One-way, optional link. `Contract` carries no reciprocal `ScenarioID`/`RETransactionID` column — a signed lease cannot be traced back to the deal that produced it via FK. | Observed |
| [POR-R-010](../rules/POR-R-010.md) | A physical site's lifecycle needs to distinguish "building it" from "leasing it" · `Project.ProjectType` = "Opening Project or Capital Project" (`Project`, `platform-tenancy`) vs. `Contract` (`contracts-leases`) · Two independent subtype ro | Derived |

## Fields

### Relationships (foreign keys) (16)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` |  | Template ID | — |  | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` |  | Complex ID | — |  | [Complex](Complex.md) |
| `DemographicDMAID` |  | DMA ID | — |  | [DMA](DMA.md) |
| `FacilityID` | Facility | Facility ID | Global |  | [Facility](Facility.md) |
| `Firm_LeaseAnalyst` | Lease Analyst | Member ID | Firm |  | [Member](Member.md) |
| `IStateProvinceCountryID` |  | Country, State, County ID | — |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` |  | County ID | — |  | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Location ID | Global |  | [Location](Location.md) |
| `MasterContractID` | Master Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `NextAvailableTermID` | Next Available Term | Contract Term ID | Global |  | [ContractTerm](ContractTerm.md) |
| `OrganizationID` | Organization | Organization ID | Global |  | [Organization](Organization.md) |
| `ProgramID` | Portfolio | Portfolio ID | Global |  | [Program](Program.md) |
| `PrototypeID` |  | Prototype ID | — |  | [Prototype](Prototype.md) |
| `RegionID` |  | Region ID | — |  | [Region](Region.md) |
| `RootRegionID` |  | Region ID | — |  | [Region](Region.md) |
| `SubRegionID` |  | Region ID | — |  | [Region](Region.md) |

### Soft references (9)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_DefaultLog` | Default Log | Custom List | Firm |  |  |
| `Firm_Funds` | Funds | Custom List | Firm |  |  |
| `Firm_HistoricalLeaseNotes` |  | Custom List | — |  |  |
| `Firm_LeaseContacts` |  | Custom List | — |  |  |
| `Firm_OperatingExpenses` | Operating Expenses | Custom List | Firm |  |  |
| `Firm_ReconciliationLog` | Reconciliation Log | Custom List | Firm |  |  |
| `Firm_SavingsLog` | Savings Log | Custom List | Firm |  |  |
| `LinkProjectEntityContactListData` |  | Contact | — |  |  |
| `ManagerIDList` |  | Dropdown | — |  |  |

### Coded values (drop-downs) (90)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAgreementTypeID` | Agreement Type | Dropdown (Agreement Type Code) | Global |  | Agreement Type Code |
| `CodeAssetClassID` | Asset Class | Dropdown (Asset Class Code) | Global |  | Asset Class Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeConstructionTypeID` |  | Dropdown (Construction Type Code) | — |  | Construction Type Code |
| `CodeContractCategoryID` | Contract Category | Dropdown (Contract Category Code) | Global |  | Contract Category Code |
| `CodeContractGroupID` | Contract Group | Dropdown (Contract Group Code) | Global |  | Contract Group Code |
| `CodeContractStatusID` | Contract Status | Dropdown (Contract Status Code) | Global |  | Contract Status Code |
| `CodeContractTypeID` | Contract Type | Dropdown (Contract Type Code) | Global |  | Contract Type Code |
| `CodeContractUseID` | Contract Use | Dropdown (Contract Use Code) | Global |  | Contract Use Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeDealTypeID` |  | Dropdown (Deal Type Code) | — |  | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeDesc_CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeDistributionCenterID` |  | Dropdown (Distribution Center Code) | — |  | Distribution Center Code |
| `CodeHoldingInterestID` | Holding Interest | Dropdown (Holding Interest Code) | Global |  | Holding Interest Code |
| `CodeMarketAreaID` |  | Dropdown (Market Area Code) | — |  | Market Area Code |
| `CodeMarketTypeID` |  | Dropdown (Market Type Code) | — |  | Market Type Code |
| `CodeProjectTypeID` |  | Dropdown (Project Type Code) | — |  | Project Type Code |
| `CodeProrationMethodID` | Proration Method | Dropdown (Proration Method Code) | Global |  | Proration Method Code |
| `CurrentCodeProjectPhaseID` |  | Dropdown (Project Phase Code) | — |  | Project Phase Code |
| `Firm_BankChargesAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_BankChargesCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_Brand` | Brand | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMAdministrativeFeeExclusionsYN` | Administrative Fee Exclusions | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMAdministrativeYN` | Administrative Fee | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMAuditRightsYN` | Audit Rights | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMContributionsYN` | Contributions | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMExclusionsYN` | Exclusions | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMFixedStatus` | Fixed CAM Status | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMFixedYN` | Is CAM Fixed? | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMLeaseTermCapExclusions` | Lease Term Cap Exclusions | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMLeaseTermCapType` | Lease Term Cap Type | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMLeaseTermCapYN` | Lease Term Cap | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMMonthofIncrease` | Month of Increase | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMNoDuplicationofCostsLanguageYN` | No Duplication of Costs Language | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMPRShareStatus` | Prorata Share Status | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMStartingCapExclusionsYN` | Starting Cap Exclusions | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMStartingCapStatus` | Starting Cap Status | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMStartingCapYN` | Starting Cap | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CAMStatementsBindingLanguageYN` | Statements Binding Language | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CostCenter` | Cost Center | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_CreditCardFeesAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CreditCardFeesCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerEnterpriseSalesAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerEnterpriseSalesCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerInStorePurchaseReturnsAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerInStorePurchaseReturnsCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerOnlinePurchaseReturnsAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerOnlinePurchaseReturnsCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerPOSSalesAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerPOSSalesCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerShiptoStoreSalesAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerShiptoStoreSalesCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerSingleSwipeSalesAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_CustomerSingleSwipeSalesCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_DRLandlordPunchlistComplete` | Landlord's Punchlist Complete | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_DRRentAbatement` | Rent Abatement | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_DeliveryChargesAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_DeliveryChargesCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_EmployeeOnlinePurchaseReturnsAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_EmployeeOnlinePurchaseReturnsCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_EmployeeSalesAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_EmployeeSalesCap` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_Guarantor` | Guarantor | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_LeaseStatus` | Lease Status | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_LeaseYear` | Lease Year | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_ONCOTClause` | Ongoing Cotenancy Clause | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_ONCOTFrequency` | Frequency | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_ONCOTRemedy` | Remedy | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_ONCOTRightToRequestRoster` | Right To Request Roster | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_ONCOTRighttoTerminate` | Right to Terminate | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_OPCOTClause` | Opening Cotenancy Clause | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_OPCOTRighttoTerminate` | Right to Terminate | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETAdministrativeFee` | Administrative Fee | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETAdministrativeFeeExclusionsYN` | Administrative Fee Exclusions | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETAuditRightsYN` | Audit Rights | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETConsultingFeeAllowedYN` | Consulting Fee Allowed | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETContributionsYN` | Contributions | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETFixedYN` | Is RET Fixed? | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETLandlordtoProvideTaxBillsYN` | Landlord to Provide Tax Bills | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETLeaseTermCapType` | Lease Term Cap Type | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETLeaseTermCapYN` | Lease Term Cap | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETPRShareStatus` | Prorata Share Status | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETStartingCapExclusionsYN` | Starting Cap Exclusions | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETStartingCapStatus` | Starting Cap Status | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETStartingCapYN` | Starting Cap | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_RETStatementsBindingYN` | Statements Binding | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_TenantLegalName` | Tenant Legal Name | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_UncollectedCreditAllowable` |  | Dropdown (Custom Field) | — |  | Custom Field |
| `Firm_UncollectedCreditCap` |  | Dropdown (Custom Field) | — |  | Custom Field |

### Money (130)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AggregateBaseRent` | Aggregate Base Rent | Currency | Global |  |  |
| `AggregateBaseRentWithTax` | Aggregate Base Rent w/ Tax | Currency | Global |  |  |
| `AggregateNNNBaseRentNPV` | Aggregate NNN Base Rent NPV | Currency | Global |  |  |
| `AggregateTotalRent` | Aggregate Total Rent | Currency | Global |  |  |
| `AggregateTotalRentWithTax` | Aggregate Total Rent w/ Tax | Currency | Global |  |  |
| `BaseYearOperatingExpenses` | Base Year Operating Expenses | Currency | Global |  |  |
| `BaseYearOtherExpenses` | Base Year Other Expenses | Currency | Global |  |  |
| `BaseYearRETax` | Base Year RE Tax | Currency | Global |  |  |
| `BeyondFifthFiscalYearBaseRent` | Beyond Fifth Fiscal Year Base Rent | Currency | Global |  |  |
| `BeyondFifthFiscalYearBaseRentWithTax` | Beyond Fifth Fiscal Year Base Rent w/ Tax | Currency | Global |  |  |
| `BeyondFifthFiscalYearTotalRent` | Beyond Fifth Fiscal Year Total Rent | Currency | Global |  |  |
| `BeyondFifthFiscalYearTotalRentWithTax` | Beyond Fifth Fiscal Year Total Rent w/ Tax | Currency | Global |  |  |
| `BeyondFifthYearBaseRent` | Beyond Fifth Calendar Year Base Rent | Currency | Global |  |  |
| `BeyondFifthYearBaseRentWithTax` | Beyond Fifth Calendar Year Base Rent w/ Tax | Currency | Global |  |  |
| `BeyondFifthYearTotalRent` | Beyond Fifth Calendar Year Total Rent | Currency | Global |  |  |
| `BeyondFifthYearTotalRentWithTax` | Beyond Fifth Calendar Year Total Rent w/ Tax | Currency | Global |  |  |
| `BeyondSixthFiscalYearBaseRent` | Beyond Sixth Fiscal Year Base Rent | Currency | Global |  |  |
| `BeyondSixthFiscalYearBaseRentWithTax` | Beyond Sixth Fiscal Year Base Rent w/ Tax | Currency | Global |  |  |
| `BeyondSixthFiscalYearTotalRent` | Beyond Sixth Fiscal Year Total Rent | Currency | Global |  |  |
| `BeyondSixthFiscalYearTotalRentWithTax` | Beyond Sixth Fiscal Year Total Rent w/ Tax | Currency | Global |  |  |
| `BeyondSixthYearBaseRent` | Beyond Sixth Calendar Year Base Rent | Currency | Global |  |  |
| `BeyondSixthYearBaseRentWithTax` | Beyond Sixth Calendar Year Base Rent w/ Tax | Currency | Global |  |  |
| `BeyondSixthYearTotalRent` | Beyond Sixth Calendar Year Total Rent | Currency | Global |  |  |
| `BeyondSixthYearTotalRentWithTax` | Beyond Sixth Calendar Year Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentAnnualBaseRent` | Current Annual Calendar Base Rent | Currency | Global |  |  |
| `CurrentAnnualBaseRentWithTax` | Current Annual Calendar Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentAnnualFiscalBaseRent` | Current Annual Fiscal Base Rent | Currency | Global |  |  |
| `CurrentAnnualFiscalBaseRentWithTax` | Current Annual Fiscal Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentAnnualFiscalTotalRent` | Current Annual Fiscal Total Rent | Currency | Global |  |  |
| `CurrentAnnualFiscalTotalRentWithTax` | Current Annual Fiscal Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentAnnualTotalRent` | Current Annual Calendar Total Rent | Currency | Global |  |  |
| `CurrentAnnualTotalRentWithTax` | Current Annual Calendar Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentCalendarYearGrossSales` | Current Calendar Year Gross Sales | Currency | Global |  |  |
| `CurrentCalendarYearQ1BaseRent` | Current Calendar Q1 Base Rent | Currency | Global |  |  |
| `CurrentCalendarYearQ1BaseRentWithTax` | Current Calendar Q1 Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentCalendarYearQ1TotalRent` | Current Calendar Q1 Total Rent | Currency | Global |  |  |
| `CurrentCalendarYearQ1TotalRentWithTax` | Current Calendar Q1 Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentCalendarYearQ2BaseRent` | Current Calendar Q2 Base Rent | Currency | Global |  |  |
| `CurrentCalendarYearQ2BaseRentWithTax` | Current Calendar Q2 Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentCalendarYearQ2TotalRent` | Current Calendar Q2 Total Rent | Currency | Global |  |  |
| `CurrentCalendarYearQ2TotalRentWithTax` | Current Calendar Q2 Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentCalendarYearQ3BaseRent` | Current Calendar Q3 Base Rent | Currency | Global |  |  |
| `CurrentCalendarYearQ3BaseRentWithTax` | Current Calendar Q3 Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentCalendarYearQ3TotalRent` | Current Calendar Q3 Total Rent | Currency | Global |  |  |
| `CurrentCalendarYearQ3TotalRentWithTax` | Current Calendar Q3 Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentCalendarYearQ4BaseRent` | Current Calendar Q4 Base Rent | Currency | Global |  |  |
| `CurrentCalendarYearQ4BaseRentWithTax` | Current Calendar Q4 Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentCalendarYearQ4TotalRent` | Current Calendar Q4 Total Rent | Currency | Global |  |  |
| `CurrentCalendarYearQ4TotalRentWithTax` | Current Calendar Q4 Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentFiscalYearQ1BaseRent` | Current Fiscal Q1 Base Rent | Currency | Global |  |  |
| `CurrentFiscalYearQ1BaseRentWithTax` | Current Fiscal Q1 Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentFiscalYearQ1TotalRent` | Current Fiscal Q1 Total Rent | Currency | Global |  |  |
| `CurrentFiscalYearQ1TotalRentWithTax` | Current Fiscal Q1 Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentFiscalYearQ2BaseRent` | Current Fiscal Q2 Base Rent | Currency | Global |  |  |
| `CurrentFiscalYearQ2BaseRentWithTax` | Current Fiscal Q2 Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentFiscalYearQ2TotalRent` | Current Fiscal Q2 Total Rent | Currency | Global |  |  |
| `CurrentFiscalYearQ2TotalRentWithTax` | Current Fiscal Q2 Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentFiscalYearQ3BaseRent` | Current Fiscal Q3 Base Rent | Currency | Global |  |  |
| `CurrentFiscalYearQ3BaseRentWithTax` | Current Fiscal Q3 Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentFiscalYearQ3TotalRent` | Current Fiscal Q3 Total Rent | Currency | Global |  |  |
| `CurrentFiscalYearQ3TotalRentWithTax` | Current Fiscal Q3 Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentFiscalYearQ4BaseRent` | Current Fiscal Q4 Base Rent | Currency | Global |  |  |
| `CurrentFiscalYearQ4BaseRentWithTax` | Current Fiscal Q4 Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentFiscalYearQ4TotalRent` | Current Fiscal Q4 Total Rent | Currency | Global |  |  |
| `CurrentFiscalYearQ4TotalRentWithTax` | Current Fiscal Q4 Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentMonthlyBaseRent` | Current Monthly Base Rent | Currency | Global |  |  |
| `CurrentMonthlyBaseRentWithTax` | Current Monthly Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentMonthlyTotalRent` | Current Monthly Total Rent | Currency | Global |  |  |
| `CurrentMonthlyTotalRentWithTax` | Current Monthly Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentPeriodBaseRent` | Current Period Base Rent | Currency | Global |  |  |
| `CurrentPeriodBaseRentWithTax` | Current Period Base Rent w/ Tax | Currency | Global |  |  |
| `CurrentPeriodTotalRent` | Current Period Total Rent | Currency | Global |  |  |
| `CurrentPeriodTotalRentWithTax` | Current Period Total Rent w/ Tax | Currency | Global |  |  |
| `CurrentStraightLineAssetBalance` | Current Straight Line Asset Balance | Currency | Global |  |  |
| `CurrentStraightLineLiabilityBalance` | Current Straight Line Liability Balance | Currency | Global |  |  |
| `FMVOfBuilding` | FMV Of Building | Currency | Global |  |  |
| `FMVOfLand` | FMV Of Land | Currency | Global |  |  |
| `FifthFiscalYearBaseRent` | Fifth Fiscal Year Base Rent | Currency | Global |  |  |
| `FifthFiscalYearBaseRentWithTax` | Fifth Fiscal Year Base Rent w/ Tax | Currency | Global |  |  |
| `FifthFiscalYearTotalRent` | Fifth Fiscal Year Total Rent | Currency | Global |  |  |
| `FifthFiscalYearTotalRentWithTax` | Fifth Fiscal Year Total Rent w/ Tax | Currency | Global |  |  |
| `FifthYearBaseRent` | Fifth Calendar Year Base Rent | Currency | Global |  |  |
| `FifthYearBaseRentWithTax` | Fifth Calendar Year Base Rent w/ Tax | Currency | Global |  |  |
| `FifthYearTotalRent` | Fifth Calendar Year Total Rent | Currency | Global |  |  |
| `FifthYearTotalRentWithTax` | Fifth Calendar Year Total Rent w/ Tax | Currency | Global |  |  |
| `Firm_LastDeferredSLEntry` | Last Deferred SL Entry | Currency | Firm |  |  |
| `Firm_LastDeferredSLTotal` | Last Deferred SL Total | Currency | Firm |  |  |
| `Firm_PriorMonthAccrualTotal` |  | Currency | — |  |  |
| `FourthFiscalYearBaseRent` | Fourth Fiscal Year Base Rent | Currency | Global |  |  |
| `FourthFiscalYearBaseRentWithTax` | Fourth Fiscal Year Base Rent w/ Tax | Currency | Global |  |  |
| `FourthFiscalYearTotalRent` | Fourth Fiscal Year Total Rent | Currency | Global |  |  |
| `FourthFiscalYearTotalRentWithTax` | Fourth Fiscal Year Total Rent w/ Tax | Currency | Global |  |  |
| `FourthYearBaseRent` | Fourth Calendar Year Base Rent | Currency | Global |  |  |
| `FourthYearBaseRentWithTax` | Fourth Calendar Year Base Rent w/ Tax | Currency | Global |  |  |
| `FourthYearTotalRent` | Fourth Calendar Year Total Rent | Currency | Global |  |  |
| `FourthYearTotalRentWithTax` | Fourth Calendar Year Total Rent w/ Tax | Currency | Global |  |  |
| `NextFiscalYearBaseRent` | Next Fiscal Year Base Rent | Currency | Global |  |  |
| `NextFiscalYearBaseRentWithTax` | Next Fiscal Year Base Rent w/ Tax | Currency | Global |  |  |
| `NextFiscalYearTotalRent` | Next Fiscal Year Total Rent | Currency | Global |  |  |
| `NextFiscalYearTotalRentWithTax` | Next Fiscal Year Total Rent w/ Tax | Currency | Global |  |  |
| `NextYearBaseRent` | Next Calendar Year Base Rent | Currency | Global |  |  |
| `NextYearBaseRentWithTax` | Next Calendar Year Base Rent w/ Tax | Currency | Global |  |  |
| `NextYearTotalRent` | Next Calendar Year Total Rent | Currency | Global |  |  |
| `NextYearTotalRentWithTax` | Next Calendar Year Total Rent w/ Tax | Currency | Global |  |  |
| `PriorCalendarYearGrossSales` | Prior Calendar Year Gross Sales | Currency | Global |  |  |
| `RemainingFiscalObligationBaseRent` | Remaining Base Rent Obligation(Fiscal Year) | Currency | Global |  |  |
| `RemainingFiscalObligationBaseRentWithTax` | Remaining Base Rent Obligation(Fiscal Year) w/ Tax | Currency | Global |  |  |
| `RemainingFiscalObligationTotalRent` | Remaining Total Rent Obligation(Fiscal Year) | Currency | Global |  |  |
| `RemainingFiscalObligationTotalRentWithTax` | Remaining Total Rent Obligation(Fiscal Year) w/ Tax | Currency | Global |  |  |
| `RemainingObligationBaseRent` | Remaining Base Rent Obligation | Currency | Global |  |  |
| `RemainingObligationBaseRentWithTax` | Remaining Base Rent Obligation w/ Tax | Currency | Global |  |  |
| `RemainingObligationTotalRent` | Remaining Total Rent Obligation | Currency | Global |  |  |
| `RemainingObligationTotalRentWithTax` | Remaining Total Rent Obligation w/ Tax | Currency | Global |  |  |
| `SixthFiscalYearBaseRent` | Sixth Fiscal Year Base Rent | Currency | Global |  |  |
| `SixthFiscalYearBaseRentWithTax` | Sixth Fiscal Year Base Rent w/ Tax | Currency | Global |  |  |
| `SixthFiscalYearTotalRent` | Sixth Fiscal Year Total Rent | Currency | Global |  |  |
| `SixthFiscalYearTotalRentWithTax` | Sixth Fiscal Year Total Rent w/ Tax | Currency | Global |  |  |
| `SixthYearBaseRent` | Sixth Calendar Year Base Rent | Currency | Global |  |  |
| `SixthYearBaseRentWithTax` | Sixth Calendar Year Base Rent w/ Tax | Currency | Global |  |  |
| `SixthYearTotalRent` | Sixth Calendar Year Total Rent | Currency | Global |  |  |
| `SixthYearTotalRentWithTax` | Sixth Calendar Year Total Rent w/ Tax | Currency | Global |  |  |
| `ThirdFiscalYearBaseRent` | Third Fiscal Year Base Rent | Currency | Global |  |  |
| `ThirdFiscalYearBaseRentWithTax` | Third Fiscal Year Base Rent w/ Tax | Currency | Global |  |  |
| `ThirdFiscalYearTotalRent` | Third Fiscal Year Total Rent | Currency | Global |  |  |
| `ThirdFiscalYearTotalRentWithTax` | Third Fiscal Year Total Rent w/ Tax | Currency | Global |  |  |
| `ThirdYearBaseRent` | Third Calendar Year Base Rent | Currency | Global |  |  |
| `ThirdYearBaseRentWithTax` | Third Calendar Year Base Rent w/ Tax | Currency | Global |  |  |
| `ThirdYearTotalRent` | Third Calendar Year Total Rent | Currency | Global |  |  |
| `ThirdYearTotalRentWithTax` | Third Calendar Year Total Rent w/ Tax | Currency | Global |  |  |
| `math_currPaymentRate_9` | currPaymentRate | Currency | Global |  |  |

### Rates & percentages (35)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ComputedSLDiscountRate` | Computed Discount Rate | Percentage | Global |  |  |
| `ContractTaxRate1` | Contract Tax Rate #1 | Percentage | Global |  |  |
| `ContractTaxRate2` | Contract Tax Rate #2 | Percentage | Global |  |  |
| `ContractTaxRate3` | Contract Tax Rate #3 | Percentage | Global |  |  |
| `ContractTaxRate4` | Contract Tax Rate #4 | Percentage | Global |  |  |
| `DiscountRate` | Contract Discount Rate | Percentage | Global |  |  |
| `FairValueThreshold` | Fair Value Threshold | Percentage | Global |  |  |
| `Firm_BankChargesCapPercent` |  | Percentage | — |  |  |
| `Firm_CAMAdministrativeFeePercent` | Administrative Fee Percent | Percentage | Firm |  |  |
| `Firm_CAMFixedIncreasePercent` | Fixed CAM Increase Percent | Percentage | Firm |  |  |
| `Firm_CAMFloorPercent` | Floor Percent | Percentage | Firm |  |  |
| `Firm_CAMLeaseTermCapPercent` | Lease Term Cap Percent | Percentage | Firm |  |  |
| `Firm_CreditCardFeesCapPercent` |  | Percentage | — |  |  |
| `Firm_CustomerEnterpriseSalesCapPercent` |  | Percentage | — |  |  |
| `Firm_CustomerInStorePurchaseReturnsCapPercent` |  | Percentage | — |  |  |
| `Firm_CustomerOnlinePurchaseReturnsCapPercent` |  | Percentage | — |  |  |
| `Firm_CustomerPOSSalesCapPercent` |  | Percentage | — |  |  |
| `Firm_CustomerShiptoStoreSalesCapPercent` |  | Percentage | — |  |  |
| `Firm_CustomerSingleSwipeSalesCapPercent` |  | Percentage | — |  |  |
| `Firm_DeliveryChargesCapPercent` |  | Percentage | — |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsCapPercent` |  | Percentage | — |  |  |
| `Firm_EmployeeSalesCapPercent` |  | Percentage | — |  |  |
| `Firm_ONCOTRequiredPercentofInlineSpace` | Required Percent of Inline Space | Percentage | Firm |  |  |
| `Firm_OPCOTRequiredPercentofInlineSpace` | Required Percent of Inline Space | Percentage | Firm |  |  |
| `Firm_RETAdministrativeFeePercent` | Administrative Fee Percent | Percentage | Firm |  |  |
| `Firm_RETFloorPercent` | Floor Percent | Percentage | Firm |  |  |
| `Firm_RETLeaseTermCapPercent` | Lease Term Cap Percent | Percentage | Firm |  |  |
| `Firm_UncollectedCreditCapPercent` |  | Percentage | — |  |  |
| `PaymentRate` | Payment Rate | Percentage | Global |  |  |
| `ProRataShareRate` | Pro Rata Share Rate | Percentage | Global |  |  |
| `RatioLeaseAutoRenewToFMV` | Ratio Lease w/ Auto Renewal To FMV | Percentage | Global |  |  |
| `RatioLeaseBargainRenewToFMV` | Ratio Lease w/ Bargain Renewal To FMV | Percentage | Global |  |  |
| `RatioTermAutoRenewToLife` | Ratio Term w/ Auto Renewal To Life | Percentage | Global |  |  |
| `RatioTermBargainRenewToLife` | Ratio Term w/ Bargain Renewal To Life | Percentage | Global |  |  |
| `RemainingEconomicLifeThreshold` | Remaining Economic Life Threshold | Percentage | Global |  |  |

### Quantities (39)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualRevenueWeeks` |  | Number | — |  |  |
| `BehindScheduleDays` | Schedule Behind Days | Number | Global |  |  |
| `ContractID` | Contract RecID | Number | Global |  |  |
| `ContractID` | Contract RecID | Number | Global |  |  |
| `ContractID` | Contract RecID | Number | Global |  |  |
| `CurrentYear` | Current Year | Number | Global |  |  |
| `DBFolderSizeMB` |  | 2-Digit Number | — |  |  |
| `DaysToExpiration` | Days to Expiration | Number with no digits | Global |  |  |
| `Depth` |  | Number | — |  |  |
| `EntityId` |  | Number | — |  |  |
| `Firm_BuildoutDuration` |  | Number with no digits | — |  |  |
| `Firm_CAMInitialFixedMO` | Initial Fixed CAM Monthly | Number | Firm |  |  |
| `Firm_CAMInitialFixedPSF` | Initial Fixed CAM PSF | Number | Firm |  |  |
| `Firm_CAMNumberofYearsAuditable` | Number of Years Auditable | Number | Firm |  |  |
| `Firm_CAMStartingCapAmountPSF` | Starting Cap Amount PSF | Number | Firm |  |  |
| `Firm_CAMStartingCapMonthly` | Starting Cap Amount Monthly | Number | Firm |  |  |
| `Firm_CorporateCode` | Corp | Number | Firm |  |  |
| `Firm_FixturingPeriod` | Fixturing Period | Number | Firm |  |  |
| `Firm_NSInternalID` |  | Number | — |  |  |
| `Firm_RETInitialEstimateMonthly` | Initial Estimate Monthly | Number | Firm |  |  |
| `Firm_RETInitialEstimatePSF` | Initial Estimate PSF | Number | Firm |  |  |
| `Firm_RETStartingCapAmount` | Starting Cap Amount | Number | Firm |  |  |
| `Frontage` |  | Number | — |  |  |
| `LatitudeDegrees` |  | 5-Digit Number | — |  |  |
| `LeasedLandArea` | Leased Land Area | Number | Global |  |  |
| `LongitudeDegrees` |  | 5-Digit Number | — |  |  |
| `NumberOfDocuments` |  | Number | — |  |  |
| `OpenYear` | Open Year | Number | Global |  |  |
| `OutOfDateDays` | Out Of Date Days | Number | Global |  |  |
| `ProjectEntityID` |  | Number | — |  |  |
| `ProjectLandArea` | Project Land Area | Number | Global |  |  |
| `RemainingLife` | Remaining Life | Number | Global |  |  |
| `RemainingNumberOfTerms` | Remaining Number of Terms | Number | Global |  |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |
| `SequenceNumber` |  | Number | — |  |  |
| `TermLength` | Term Length | Number | Global |  |  |
| `UsableArea` |  | Number | — |  |  |
| `YearBuilt` | Year Built | Number | Global |  |  |
| `zFirm_LeaseSquareFootage` | zLeaseSquareFootage | 2-Digit Number | Firm |  |  |

### Dates & timestamps (41)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` | Actual End Date | Date | Global |  |  |
| `ActualStartDate` | Actual Start Date | Date | Global |  |  |
| `BaselineEndDate` | Baseline End Date | Date | Global |  |  |
| `BaselineStartDate` | Baseline Start Date | Date | Global |  |  |
| `ClientScheduleLastReviewedDate` |  | Date | — |  |  |
| `CommenceDate` | Commence Date | Date | Global |  |  |
| `ExecuteDate` | Execute Date | Date | Global |  |  |
| `ExpectedEndDate` | Expected End Date | Date | Global |  |  |
| `ExpireDate` | Expire Date | Date | Global |  |  |
| `Firm_AnticipatedDeliveryDate` |  | Date | — |  |  |
| `Firm_BankChargesBeginDate` |  | Date | — |  |  |
| `Firm_CAMDateofFirstIncrease` | Date of First Increase | Date | Firm |  |  |
| `Firm_CreditCardFeesBeginDate` |  | Date | — |  |  |
| `Firm_CustomerEnterpriseSalesBeginDate` |  | Date | — |  |  |
| `Firm_CustomerInStorePurchaseReturnsBeginDate` |  | Date | — |  |  |
| `Firm_CustomerOnlinePurchaseReturnsBeginDate` |  | Date | — |  |  |
| `Firm_CustomerPOSSalesBeginDate` |  | Date | — |  |  |
| `Firm_CustomerShiptoStoreSalesBeginDate` |  | Date | — |  |  |
| `Firm_CustomerSingleSwipeSalesBeginDate` |  | Date | — |  |  |
| `Firm_DRAnticipatedDeliveryDate` | Anticipated Delivery Date | Date | Firm |  |  |
| `Firm_DRTerminationRightDate` | Termination Right Date | Date | Firm |  |  |
| `Firm_DeliveryChargesBeginDate` |  | Date | — |  |  |
| `Firm_DeliveryDate` |  | Date | — |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsBeginDate` |  | Date | — |  |  |
| `Firm_EmployeeSalesBeginDate` |  | Date | — |  |  |
| `Firm_ExpansionPossessionBeginDate` |  | Date | — |  |  |
| `Firm_LastDeferredSLEntryDate` | Last Deferred SL Entry Date | Date | Firm |  |  |
| `Firm_LatestCommencementDate` |  | Date | — |  |  |
| `Firm_LegalReview` |  | Date | — |  |  |
| `Firm_LegalWorkflow` |  | Date | — |  |  |
| `Firm_UncollectedCreditBeginDate` |  | Date | — |  |  |
| `LastLikelyOptionDate` | Likely Term End Date | Date | Global |  |  |
| `ObligationDate` | Obligation Date | Date | Global |  |  |
| `OriginalEndDate` |  | Date | — |  |  |
| `OriginalStartDate` |  | Date | — |  |  |
| `PaymentsBeginDate` | Payments Begin Date | Date | Global |  |  |
| `PaymentsEndDate` | Payments End Date | Date | Global |  |  |
| `PossessionBeginDate` | Possession Begin Date | Date | Global |  |  |
| `PossessionEndDate` | Possession End Date | Date | Global |  |  |
| `SlotEndDate` |  | Date | — |  |  |
| `StatusEffectiveDate` | Status Effective Date | Date | Global |  |  |

### Flags (13)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AutomaticRenewalInLease` | Automatic Renewal In Lease? | Boolean | Global |  |  |
| `AutomaticRenewalOption` | Automatic Renewal Option? | Boolean | Global |  |  |
| `BargainRenewalInLease` | Bargain Renewal In Lease? | Boolean | Global |  |  |
| `BargainRenewalOption` | Bargain Renewal Option? | Boolean | Global |  |  |
| `ContainsBargainPurchaseOption` | Contains Bargain Purchase Option? | Boolean | Global |  |  |
| `DoesTitleRevertToTenant` | Does Title Revert To Tenant? | Boolean | Global |  |  |
| `InAlternateRent` | In Alternate Rent? | Boolean | Global |  |  |
| `Inactive` |  | Boolean | — |  |  |
| `IsDead` |  | Boolean | — |  |  |
| `IsLowAssetValue` | Is Low Asset Value | Boolean | Global |  |  |
| `IsShortTerm` | Is Short Term | Boolean | Global |  |  |
| `IsTranslation` | Is Translation | Boolean | Global |  |  |
| `MonthToMonth` | Month To Month? | Boolean | Global |  |  |

### Text & notes (187)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseProvider` |  | Text | — |  |  |
| `City` |  | Text | — |  |  |
| `CityStateProvinceCountry` |  | Text | — |  |  |
| `ClientEntityID` | Contract ID | Text | Global |  |  |
| `ComparisonList` |  | Text | — |  |  |
| `CompletedPhaseStatus` |  | Text | — |  |  |
| `ConstructionPhaseStatus` |  | Text | — |  |  |
| `ContractClass` | Contract Class | Text | Global |  |  |
| `ContractName` | Contract Name | Text | Global | yes |  |
| `CountryID` |  | Text | — |  |  |
| `CrossStreet1` |  | Text | — |  |  |
| `CrossStreet2` |  | Text | — |  |  |
| `CurrentMilestone` |  | Text | — |  |  |
| `CurrentMonthYear` | Current Month/Year | Text | Global |  |  |
| `CurrentPhaseStatus` |  | Text | — |  |  |
| `DesignPhaseStatus` |  | Text | — |  |  |
| `EntityEmail` |  | Text | — |  |  |
| `EntityPhoto` |  | Text | — |  |  |
| `ExpAccrualForecastTable` | Expense Accrual Forecast Table | Text | Global |  |  |
| `ExpenseForecastTable` | Expense Forecast Table | Text | Global |  |  |
| `FMVSource` | FMV Source | Text | Global |  |  |
| `FacilityName` |  | Text | — |  |  |
| `FinalResult` | Final Result | Text | Global |  |  |
| `FinancialModel` |  | Text | — |  |  |
| `FirmID` |  | Text | — |  |  |
| `Firm_BankChargesDocument` |  | Text | — |  |  |
| `Firm_BankChargesNotes` |  | Text | — |  |  |
| `Firm_BankChargesPage` |  | Text | — |  |  |
| `Firm_BankChargesSection` |  | Text | — |  |  |
| `Firm_CAMAdministrativeFeeDefinition` | Administrative Fee Definition | Text | Firm |  |  |
| `Firm_CAMAuditRightsReference` | Audit Rights Reference | Text | Firm |  |  |
| `Firm_CAMComment` | Comment | Text | Firm |  |  |
| `Firm_CAMContributionsReference` | Contributions Reference | Text | Firm |  |  |
| `Firm_CAMDocument` | Document | Text | Firm |  |  |
| `Firm_CAMExclusionsReference` | Exclusions Reference | Text | Firm |  |  |
| `Firm_CAMFixedComment` | Fixed CAM Increase Comment | Text | Firm |  |  |
| `Firm_CAMFixedText` | Fixed CAM Text | Text | Firm |  |  |
| `Firm_CAMLeaseTermCapComment` | Lease Term Cap Comment | Text | Firm |  |  |
| `Firm_CAMLeaseTermCapTextReference` | Lease Term Cap Text Reference | Text | Firm |  |  |
| `Firm_CAMNoDuplicationofCostsReference` | No Duplication of Costs Reference | Text | Firm |  |  |
| `Firm_CAMNotes` | Notes | Text | Firm |  |  |
| `Firm_CAMPRShare` | PR Share | Text | Firm |  |  |
| `Firm_CAMPage` | Page | Text | Firm |  |  |
| `Firm_CAMSection` | Section | Text | Firm |  |  |
| `Firm_CAMStartingCapComment` | Starting Cap Comment | Text | Firm |  |  |
| `Firm_CAMStartingCapTextReference` | Starting Cap Text Reference | Text | Firm |  |  |
| `Firm_CAMStatementsBindingLanguageReference` | Statements Binding Language Reference | Text | Firm |  |  |
| `Firm_CAMStatementsDue` | Statements Due | Text | Firm |  |  |
| `Firm_CAMStatementsDueReference` | Statements Due Reference | Text | Firm |  |  |
| `Firm_CreditCardFeesDocument` |  | Text | — |  |  |
| `Firm_CreditCardFeesNotes` |  | Text | — |  |  |
| `Firm_CreditCardFeesPage` |  | Text | — |  |  |
| `Firm_CreditCardFeesSection` |  | Text | — |  |  |
| `Firm_CustomerEnterpriseSalesDocument` |  | Text | — |  |  |
| `Firm_CustomerEnterpriseSalesNotes` |  | Text | — |  |  |
| `Firm_CustomerEnterpriseSalesPage` |  | Text | — |  |  |
| `Firm_CustomerEnterpriseSalesSection` |  | Text | — |  |  |
| `Firm_CustomerInStorePurchaseReturnsDocument` |  | Text | — |  |  |
| `Firm_CustomerInStorePurchaseReturnsNotes` |  | Text | — |  |  |
| `Firm_CustomerInStorePurchaseReturnsPage` |  | Text | — |  |  |
| `Firm_CustomerInStorePurchaseReturnsSection` |  | Text | — |  |  |
| `Firm_CustomerOnlinePurchaseReturnsDocument` |  | Text | — |  |  |
| `Firm_CustomerOnlinePurchaseReturnsNotes` |  | Text | — |  |  |
| `Firm_CustomerOnlinePurchaseReturnsPage` |  | Text | — |  |  |
| `Firm_CustomerOnlinePurchaseReturnsSection` |  | Text | — |  |  |
| `Firm_CustomerPOSSalesDocument` |  | Text | — |  |  |
| `Firm_CustomerPOSSalesNotes` |  | Text | — |  |  |
| `Firm_CustomerPOSSalesPage` |  | Text | — |  |  |
| `Firm_CustomerPOSSalesSection` |  | Text | — |  |  |
| `Firm_CustomerShiptoStoreSalesDocument` |  | Text | — |  |  |
| `Firm_CustomerShiptoStoreSalesNotes` |  | Text | — |  |  |
| `Firm_CustomerShiptoStoreSalesPage` |  | Text | — |  |  |
| `Firm_CustomerShiptoStoreSalesSection` |  | Text | — |  |  |
| `Firm_CustomerSingleSwipeSalesDocument` |  | Text | — |  |  |
| `Firm_CustomerSingleSwipeSalesNotes` |  | Text | — |  |  |
| `Firm_CustomerSingleSwipeSalesPage` |  | Text | — |  |  |
| `Firm_CustomerSingleSwipeSalesSection` |  | Text | — |  |  |
| `Firm_DRDocument` | Document | Text | Firm |  |  |
| `Firm_DRNotes` | Notes | Text | Firm |  |  |
| `Firm_DRPage` | Page | Text | Firm |  |  |
| `Firm_DRSection` | Section | Text | Firm |  |  |
| `Firm_DeliveryChargesDocument` |  | Text | — |  |  |
| `Firm_DeliveryChargesNotes` |  | Text | — |  |  |
| `Firm_DeliveryChargesPage` |  | Text | — |  |  |
| `Firm_DeliveryChargesSection` |  | Text | — |  |  |
| `Firm_DeveloperLeaseID` | Developer Lease ID | Text | Firm |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsDocument` |  | Text | — |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsNotes` |  | Text | — |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsPage` |  | Text | — |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsSection` |  | Text | — |  |  |
| `Firm_EmployeeSalesDocument` |  | Text | — |  |  |
| `Firm_EmployeeSalesNotes` |  | Text | — |  |  |
| `Firm_EmployeeSalesPage` |  | Text | — |  |  |
| `Firm_EmployeeSalesSection` |  | Text | — |  |  |
| `Firm_GISLink` | GIS Link | Text | Firm |  |  |
| `Firm_GISWebsite` | GIS Website | Text | Firm |  |  |
| `Firm_LandlordLegalName` | Landlord Legal Name | Text | Firm |  |  |
| `Firm_LeaseExpirationReference` | Lease Expiration Reference | Text | Firm |  |  |
| `Firm_LeaseStatusNotes` | Lease Status Notes | Text | Firm |  |  |
| `Firm_LeaseYearReference` | Lease Year Reference | Text | Firm |  |  |
| `Firm_LegalNotes` |  | Text | — |  |  |
| `Firm_ONCOTAlternativeRentTerms` | Alternative Rent Terms | Text | Firm |  |  |
| `Firm_ONCOTDocument` | Document | Text | Firm |  |  |
| `Firm_ONCOTLimitPerYear` | Limit Per Year | Text | Firm |  |  |
| `Firm_ONCOTNotes` | Notes | Text | Firm |  |  |
| `Firm_ONCOTPage` | Page | Text | Firm |  |  |
| `Firm_ONCOTRequiredNumberofAnchors` | Required Number of Anchors | Text | Firm |  |  |
| `Firm_ONCOTSection` | Section | Text | Firm |  |  |
| `Firm_OPCOTAlternativeRentTerms` | Alternative Rent Terms | Text | Firm |  |  |
| `Firm_OPCOTDocument` | Document | Text | Firm |  |  |
| `Firm_OPCOTNotes` | Notes | Text | Firm |  |  |
| `Firm_OPCOTPage` | Page | Text | Firm |  |  |
| `Firm_OPCOTRequiredNumberofAnchors` | Required Number of Anchors | Text | Firm |  |  |
| `Firm_OPCOTSection` | Section | Text | Firm |  |  |
| `Firm_PCRNumber` |  | Text | — |  |  |
| `Firm_RETAdministrativeFeeReference` | Administrative Fee Reference | Text | Firm |  |  |
| `Firm_RETAuditRightsReference` | Audit Rights Reference | Text | Firm |  |  |
| `Firm_RETComment` | Comment | Text | Firm |  |  |
| `Firm_RETConsultingFeeReference` | Consulting Fee Reference | Text | Firm |  |  |
| `Firm_RETContributionsReferences` | Contributions Reference | Text | Firm |  |  |
| `Firm_RETDocument` | Document | Text | Firm |  |  |
| `Firm_RETInitialEstimateReference` | Initial Estimate Reference | Text | Firm |  |  |
| `Firm_RETLeaseTermCapComment` | Lease Term Cap Comment | Text | Firm |  |  |
| `Firm_RETLeaseTermCapTextReference` | Lease Term Cap Text Reference | Text | Firm |  |  |
| `Firm_RETNotes` | Notes | Text | Firm |  |  |
| `Firm_RETPRShare` | PR Share | Text | Firm |  |  |
| `Firm_RETPage` | Page | Text | Firm |  |  |
| `Firm_RETSection` | Section | Text | Firm |  |  |
| `Firm_RETStartingCapTextReference` | Starting Cap Text Reference | Text | Firm |  |  |
| `Firm_RETStatementsBindingReference` | Statements Binding Reference | Text | Firm |  |  |
| `Firm_RETStatementsDue` | Statements Due | Text | Firm |  |  |
| `Firm_RETStatementsDueReference` | Statements Due Reference | Text | Firm |  |  |
| `Firm_RETTaxesFor` | Taxes For? | Text | Firm |  |  |
| `Firm_RentCommencementNotes` | Rent Commencement Notes | Text | Firm |  |  |
| `Firm_SalesReportLogo` |  | Text | — |  |  |
| `Firm_SalesReportLogoMadewell` |  | Text | — |  |  |
| `Firm_SalesReportSignature` |  | Text | — |  |  |
| `Firm_SalesReportSignatureName` |  | Text | — |  |  |
| `Firm_SalesReportSignatureTitle` |  | Text | — |  |  |
| `Firm_TaxLink1` | Tax Link 1 | Text | Firm |  |  |
| `Firm_TaxLink2` | Tax Link 2 | Text | Firm |  |  |
| `Firm_TaxWebsite1` | Tax Website 1 | Text | Firm |  |  |
| `Firm_TaxWebsite2` | Tax Website 2 | Text | Firm |  |  |
| `Firm_UncollectedCreditDocument` |  | Text | — |  |  |
| `Firm_UncollectedCreditNotes` |  | Text | — |  |  |
| `Firm_UncollectedCreditPage` |  | Text | — |  |  |
| `Firm_UncollectedCreditSection` |  | Text | — |  |  |
| `HTMLAddress` |  | Text | — |  |  |
| `IssuesAndAlerts` |  | Text | — |  |  |
| `LatestFinancialTestFinalResult` | Latest Financial Test Result | Text | Global |  |  |
| `MapClientRecordID` |  | Text | — |  |  |
| `MilestoneTimeline` |  | Text | — |  |  |
| `NextAvailableTermKeyDateID` | Next Available Term Key Date Info | Text | Global |  |  |
| `NextMilestone` |  | Text | — |  |  |
| `Notes` |  | Text | Global |  |  |
| `OperationsPhaseStatus` |  | Text | — |  |  |
| `OptionDescription` | Option Description | Text | Global |  |  |
| `Phone` |  | Text | — |  |  |
| `PossessionPhaseStatus` |  | Text | — |  |  |
| `PostalCode` |  | Text | — |  |  |
| `PotentialProjectName` |  | Text | — |  |  |
| `PreviousMilestone` |  | Text | — |  |  |
| `ProgramName` |  | Text | — |  |  |
| `ProjectDescription` | Description | Text | Global |  |  |
| `ProjectEntityName` |  | Text | — |  |  |
| `ProjectEntityTypeName` |  | Text | — |  |  |
| `ProjectName` |  | Text | — |  |  |
| `PrototypeName` |  | Text | — |  |  |
| `RealEstatePhaseStatus` |  | Text | — |  |  |
| `RelatedEntities` |  | Text | — |  |  |
| `RelocatedFrom` |  | Text | — |  |  |
| `RunReportAction` |  | Text | — |  |  |
| `ScLocationID` | Service Channel Location ID | Text | Global |  |  |
| `StreetAddress` |  | Text | — |  |  |
| `StreetAddress1` |  | Text | — |  |  |
| `StreetAddress2` |  | Text | — |  |  |
| `StreetAddress3` |  | Text | — |  |  |
| `StreetAddress4` |  | Text | — |  |  |
| `Test1Result` | Test #1 Result | Text | Global |  |  |
| `Test2Result` | Test #2 Result | Text | Global |  |  |
| `Test3Result` | Test #3 Result | Text | Global |  |  |
| `Test4Result` | Test #4 Result | Text | Global |  |  |
| `Test5aResult` | Test #5a Result | Text | Global |  |  |
| `Test5bResult` | Test #5b Result | Text | Global |  |  |
| `ThirdPartyWarehouse` |  | Text | — |  |  |
| `TimeZone` | Time Zone | Text | Global |  |  |
| `TradeArea` |  | Text | — |  |  |

### Audit & record keeping (9)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Contract ClientID | Text | Global | yes |  |
| `CreatedByID` |  | Member ID | — |  | [Member](Member.md) |
| `CreatedDate` |  | Time | — |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` |  | Number | — |  |  |
| `UUID` | Contract UUID | Text | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossArea` |  | Acreage | — |  |  |

## What points here (62 keys)

| Record type | Via column |
|---|---|
| [AccrualTransaction](AccrualTransaction.md) | `ContractID` |
| [AcctingAssumptionAdjust](AcctingAssumptionAdjust.md) | `ContractID` |
| [Allowance](Allowance.md) | `ContractID` |
| [AllowanceTransaction](AllowanceTransaction.md) | `ContractID` |
| [AlternateRentSchedule](AlternateRentSchedule.md) | `ContractID` |
| [Asset](Asset.md) | `FinancialContractID` |
| [CPI](CPI.md) | `ContractID` |
| [CoTenancy](CoTenancy.md) | `ContractID` |
| [Contract](Contract.md) | `MasterContractID` |
| [ContractAmendment](ContractAmendment.md) | `ContractID` |
| [ContractFinancialTest](ContractFinancialTest.md) | `ContractID` |
| [ContractTerm](ContractTerm.md) | `ContractID` |
| [Covenant](Covenant.md) | `ContractID` |
| [ExchangeRate](ExchangeRate.md) | `ContractID` |
| [ExpenseAccrualSchedule](ExpenseAccrualSchedule.md) | `ContractID` |
| [ExpenseAccrualSetup](ExpenseAccrualSetup.md) | `ContractID` |
| [ExpenseAllocation](ExpenseAllocation.md) | `ContractID` |
| [ExpenseEscalation](ExpenseEscalation.md) | `ContractID` |
| [ExpenseRecovery](ExpenseRecovery.md) | `ContractID` |
| [ExpenseRecoveryItem](ExpenseRecoveryItem.md) | `ContractID` |
| [ExpenseRecoveryItemMapping](ExpenseRecoveryItemMapping.md) | `ContractID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `ContractID` |
| [ExpenseSetup](ExpenseSetup.md) | `ContractID` |
| [ExpenseVendorAllocation](ExpenseVendorAllocation.md) | `ContractID` |
| [FinancialAdjustment](FinancialAdjustment.md) | `ContractID` |
| [Insurance](Insurance.md) | `ContractID` |
| [KeyDate](KeyDate.md) | `ContractID` |
| [LandlordInvoice](LandlordInvoice.md) | `ContractID` |
| [LandlordInvoiceItem](LandlordInvoiceItem.md) | `ContractID` |
| [LinkSchedOffsetExpGrpType](LinkSchedOffsetExpGrpType.md) | `ContractID` |
| [Parcel](Parcel.md) | `ContractID` |
| [Party](Party.md) | `ContractID` |
| [PaymentReceipt](PaymentReceipt.md) | `ContractID` |
| [PaymentTransaction](PaymentTransaction.md) | `ContractID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `ContractID` |
| [PercentageRent](PercentageRent.md) | `ContractID` |
| [PercentageRentBreakpoint](PercentageRentBreakpoint.md) | `ContractID` |
| [Responsibility](Responsibility.md) | `ContractID` |
| [SLPeriod](SLPeriod.md) | `ContractID` |
| [SLSummary](SLSummary.md) | `ContractID` |
| [Sales](Sales.md) | `ContractID` |
| [SalesExclusion](SalesExclusion.md) | `ContractID` |
| [SalesExclusionCap](SalesExclusionCap.md) | `ContractID` |
| [Scenario](Scenario.md) | `ContractID` |
| [ScheduledOffset](ScheduledOffset.md) | `ContractID` |
| [SecurityDeposit](SecurityDeposit.md) | `ContractID` |
| [ServiceRequest](ServiceRequest.md) | `ContractID` |
| [Space](Space.md) | `ContractID` |
| [Tenant](Tenant.md) | `ContractID` |
| [Usage](Usage.md) | `ContractID` |
| [UseBasedRent](UseBasedRent.md) | `ContractID` |
| [UseBasedRentBreakpoint](UseBasedRentBreakpoint.md) | `ContractID` |
| [VariableRentOffset](VariableRentOffset.md) | `ContractID` |
| [VirtualExpAccrualForecastPeriod](VirtualExpAccrualForecastPeriod.md) | `ContractID` |
| [VirtualExpenseForecastPeriod](VirtualExpenseForecastPeriod.md) | `ContractID` |
| [VirtualPRAccrualPeriod](VirtualPRAccrualPeriod.md) | `ContractID` |
| [VirtualPRPAggregate](VirtualPRPAggregate.md) | `ContractID` |
| [VirtualPercentageRentPeriod](VirtualPercentageRentPeriod.md) | `ContractID` |
| [VirtualSalesPeriod](VirtualSalesPeriod.md) | `ContractID` |
| [VirtualUBRPAggregate](VirtualUBRPAggregate.md) | `ContractID` |
| [VirtualUsagePeriod](VirtualUsagePeriod.md) | `ContractID` |
| [VirtualUseBasedRentPeriod](VirtualUseBasedRentPeriod.md) | `ContractID` |
