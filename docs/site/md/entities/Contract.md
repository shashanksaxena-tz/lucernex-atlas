# Contract

*570 fields, split across 4 physical tables · module: Contracts & Leases · Postgres: `contract_admin,contract_financial,contract_firm,contract_firm1`*

The lease/contract header record itself — the central entity the rest of the schema hangs off of. It mixes core lease terms (dates, base rent, discount rate, renewal options) with dozens of Boolean 'in lease?' flags (Automatic Renewal In Lease?, Bargain Renewal In Lease?) that record whether a clause exists versus whether it has been exercised, plus SUBMITBUTTON fields that are workflow triggers rather than data. At 402 fields (255 Global + 147 Firm) it is also the entity this tenant has customized the most — 147 of the 205 total Firm-scope fields attach here, confirming Contract is where ASG has extended Lx's base model with tenant-specific CAM, co-tenancy, and delivery-requirement fields.

Source: `data-fields/contract.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 570 |
| Fields with a vendor definition | 306 of 477 inventoried |
| Physical tables | `contract_firm`, `contract_financial`, `contract_admin` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in contract_firm, contract_financial, contract_admin

**Observed.** The field inventory names the physical destination of every column: 3 tables in the database lxr_drp_bbw. A record split across several tables is the platform working around a column-count ceiling, and the split is stated here rather than inferred. Every field node carries its own table and column, so the mapping is per column, not per record.

### Two counts of its physical tables

**Observed.** The object census counts 4 physical tables for this record; the field inventory names 3 (contract_firm, contract_financial, contract_admin). These are not two witnesses — they are the SAME export read two ways (222 of 223 objects and 7,273 fields in common), so the gap is a difference of reading, not of evidence: the census reads the exported schema, the inventory reads one replication loader's configuration, and a table the loader does not write is invisible to the second count. Settle which you mean before quoting either, and do not cite them as though they corroborate each other.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 306 fields carry a vendor definition

**Observed.** 306 of this record's 477 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 5 of this record's fields required; the Data Fields catalogue marks 3; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### 1 field excluded from extraction

**Observed.** Observed of the loader. The inventory marks 1 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | — |  | `contract_admin.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | This field pulls the complex associated with the location connected to the contract. | Complex ID | — |  | `contract_admin.ComplexID · TEXT` | [Complex](Complex.md) |
| `DemographicDMAID` | Demographic DMA | The Location Demographic DMA record ID associated with the contract. | DMA ID | — |  | `contract_admin.DemographicDMAID · TEXT` | [DMA](DMA.md) |
| `FacilityID` | Facility | Select the facility that your entity will be associated with from this field. | Facility ID | Global |  | `contract_admin.FacilityID · TEXT` | [Facility](Facility.md) |
| `Firm_LeaseAnalyst` | Lease Analyst |  | Member ID | Firm |  | `contract_firm.Firm_LeaseAnalyst · TEXT` | [Member](Member.md) |
| `IStateProvinceCountryID` | State | The state or province of the associated entity. | Country, State, County ID | — |  | `contract_admin.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | The county / province associated with the associated entity's address. | County ID | — |  | `contract_admin.JurisdictionID · TEXT` | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Select the location that your entity will be associated with from this field. | Location ID | Global |  | `contract_admin.LocationID · TEXT` | [Location](Location.md) |
| `MasterContractID` | Master Contract | The Master Contract ID is the contract ID of the master lease in a master lease-sub-lease relationship. The Master Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `contract_admin.MasterContractID · TEXT` | [Contract](Contract.md) |
| `NextAvailableTermID` | Next Available Term | The next available contract term ID. Note that only contract terms that have a status of LIKELY or AVAILABLE are considered. | Contract Term ID | Global |  | `contract_admin.NextAvailableTermID · TEXT` | [ContractTerm](ContractTerm.md) |
| `OrganizationID` | Organization | Select the organization where payments should be debited from this field. | Organization ID | Global |  | `contract_admin.OrganizationID · TEXT` | [Organization](Organization.md) |
| `ProgramID` | Portfolio | The portfolio ID of the portfolio to which the contract belongs. | Portfolio ID | Global |  | `contract_admin.ProgramID · TEXT` | [Program](Program.md) |
| `PrototypeID` | Prototype | The Prototype ID associated with the contract. | Prototype ID | — |  | `contract_admin.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `RegionID` | Region | This field pulls the region from the contract's associated location record. | Region ID | — |  | `contract_admin.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | — |  | `contract_admin.RootRegionID · TEXT` | [Region](Region.md) |
| `SubRegionID` | Sub Region | This field pulls the sub-region from the contract's associated location record. | Region ID | — |  | `contract_admin.SubRegionID · TEXT` | [Region](Region.md) |

### Soft references (9)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_DefaultLog` | Default Log |  | Custom List | Firm |  | `contract_firm.Firm_DefaultLog · TEXT` |  |
| `Firm_Funds` | Funds |  | Custom List | Firm |  | `contract_firm.Firm_Funds · TEXT` |  |
| `Firm_HistoricalLeaseNotes` |  |  | Custom List | — |  |  |  |
| `Firm_LeaseContacts` |  |  | Custom List | — |  |  |  |
| `Firm_OperatingExpenses` | Operating Expenses |  | Custom List | Firm |  | `contract_firm.Firm_OperatingExpenses · TEXT` |  |
| `Firm_ReconciliationLog` | Reconciliation Log |  | Custom List | Firm |  | `contract_firm.Firm_ReconciliationLog · TEXT` |  |
| `Firm_SavingsLog` | Savings Log |  | Custom List | Firm |  | `contract_firm.Firm_SavingsLog · TEXT` |  |
| `LinkProjectEntityContactListData` | Contact List | This field returns a list of Active and Inactive entities filtered by member security. | Contact | — |  | `contract_admin.LinkProjectEntityContactListData · TEXT` |  |
| `ManagerIDList` | Project Managers | This is a generic field that you can add to a page layout. In View mode, this field returns a list of managers assigned to the entity by the org chart and managers assigned to the entity on an ad hoc basis. In Edit mode, this field allows you to add managers to your entity. | Dropdown | — |  | `contract_admin.ManagerIDList · TEXT` |  |

### Coded values (drop-downs) (90)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAgreementTypeID` | Agreement Type | You must select the agreement type of your contract from this field. If you select the sublease agreement type, you will have access to the pass-through payments functionality. | Dropdown (Agreement Type Code) | Global |  | `contract_admin.CodeAgreementTypeID · TEXT` | Agreement Type Code |
| `CodeAssetClassID` | Asset Class | This field allows you to select an asset class. | Dropdown (Asset Class Code) | Global |  | `contract_admin.CodeAssetClassID · TEXT` | Asset Class Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `contract_admin.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | This is a default field that is not used for contracts or equipment contracts. | Dropdown (Construction Type Code) | — |  | `contract_admin.CodeConstructionTypeID · TEXT` | Construction Type Code |
| `CodeContractCategoryID` | Contract Category | The contract category is the third level of categorization for contract records. Categories are the children of types and grandchildren of groups. | Dropdown (Contract Category Code) | Global |  | `contract_admin.CodeContractCategoryID · TEXT` | Contract Category Code |
| `CodeContractGroupID` | Contract Group | The contract group is the first level of categorization for contract records. Groups are the parents of types, and grandparents of categories. | Dropdown (Contract Group Code) | Global |  | `contract_admin.CodeContractGroupID · TEXT` | Contract Group Code |
| `CodeContractStatusID` | Contract Status | Select the contract status from this field. | Dropdown (Contract Status Code) | Global |  | `contract_admin.CodeContractStatusID · TEXT` | Contract Status Code |
| `CodeContractTypeID` | Contract Type | The contract type is the second level of categorization for contract records. Types are the children of groups and parents of categories. | Dropdown (Contract Type Code) | Global |  | `contract_admin.CodeContractTypeID · TEXT` | Contract Type Code |
| `CodeContractUseID` | Contract Use | Select the primary use of the space from this field. | Dropdown (Contract Use Code) | Global |  | `contract_admin.CodeContractUseID · TEXT` | Contract Use Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `contract_admin.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDealTypeID` | Deal Type | This is a generic field. It is not implemented for contracts or equipment contracts by default. | Dropdown (Deal Type Code) | — |  | `contract_admin.CodeDealTypeID · TEXT` | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | The description of the market of the location associated with the contract. | Dropdown (Market Area Code) | — |  | `contract_admin.CodeDesc_CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | This is a generic field. It is not implemented for contracts or equipment contracts by default. | Dropdown (Project Type Code) | — |  | `contract_admin.CodeDesc_CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | This is a generic field. It is not implemented for contracts or equipment contracts by default. | Dropdown (Distribution Center Code) | — |  | `contract_admin.CodeDistributionCenterID · TEXT` | Distribution Center Code |
| `CodeHoldingInterestID` | Holding Interest | Your holding interest defines who you are in terms of the lease agreement. Example holding interest categories include Lessor, Lessee, Sub-lessor, and Sub-lessee. | Dropdown (Holding Interest Code) | Global |  | `contract_admin.CodeHoldingInterestID · TEXT` | Holding Interest Code |
| `CodeMarketAreaID` | Market Area | This field pulls membership data from your portfolio's organization chart and adds default members to your contract when the contract is created. | Dropdown (Market Area Code) | — |  | `contract_admin.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | The market of the location associated with the contract. | Dropdown (Market Type Code) | — |  | `contract_admin.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeProjectTypeID` | Project Type | This is a generic field. It is not implemented for contracts or equipment contracts by default. | Dropdown (Project Type Code) | — |  | `contract_admin.CodeProjectTypeID · TEXT` | Project Type Code |
| `CodeProrationMethodID` | Proration Method | This field is related to the ExpenseSetup database table. It is not implemented at the contract- or equipment contract-level. | Dropdown (Proration Method Code) | Global |  | `contract_admin.CodeProrationMethodID · TEXT` | Proration Method Code |
| `CurrentCodeProjectPhaseID` | Project Phase | The project phase set by the milestone timeline. This value is driven by your entity schedule. | Dropdown (Project Phase Code) | — |  | `contract_admin.CurrentCodeProjectPhaseID · TEXT` | Project Phase Code |
| `Firm_BankChargesAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_BankChargesCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_Brand` | Brand |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_Brand · TEXT` | Custom Field |
| `Firm_CAMAdministrativeFeeExclusionsYN` | Administrative Fee Exclusions |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMAdministrativeFeeExclusionsYN · TEXT` | Custom Field |
| `Firm_CAMAdministrativeYN` | Administrative Fee |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMAdministrativeYN · TEXT` | Custom Field |
| `Firm_CAMAuditRightsYN` | Audit Rights |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMAuditRightsYN · TEXT` | Custom Field |
| `Firm_CAMContributionsYN` | Contributions |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMContributionsYN · TEXT` | Custom Field |
| `Firm_CAMExclusionsYN` | Exclusions |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMExclusionsYN · TEXT` | Custom Field |
| `Firm_CAMFixedStatus` | Fixed CAM Status |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMFixedStatus · TEXT` | Custom Field |
| `Firm_CAMFixedYN` | Is CAM Fixed? |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMFixedYN · TEXT` | Custom Field |
| `Firm_CAMLeaseTermCapExclusions` | Lease Term Cap Exclusions |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMLeaseTermCapExclusions · TEXT` | Custom Field |
| `Firm_CAMLeaseTermCapType` | Lease Term Cap Type |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMLeaseTermCapType · TEXT` | Custom Field |
| `Firm_CAMLeaseTermCapYN` | Lease Term Cap |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMLeaseTermCapYN · TEXT` | Custom Field |
| `Firm_CAMMonthofIncrease` | Month of Increase |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMMonthofIncrease · TEXT` | Custom Field |
| `Firm_CAMNoDuplicationofCostsLanguageYN` | No Duplication of Costs Language |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMNoDuplicationofCostsLanguageYN · TEXT` | Custom Field |
| `Firm_CAMPRShareStatus` | Prorata Share Status |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMPRShareStatus · TEXT` | Custom Field |
| `Firm_CAMStartingCapExclusionsYN` | Starting Cap Exclusions |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMStartingCapExclusionsYN · TEXT` | Custom Field |
| `Firm_CAMStartingCapStatus` | Starting Cap Status |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMStartingCapStatus · TEXT` | Custom Field |
| `Firm_CAMStartingCapYN` | Starting Cap |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMStartingCapYN · TEXT` | Custom Field |
| `Firm_CAMStatementsBindingLanguageYN` | Statements Binding Language |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CAMStatementsBindingLanguageYN · TEXT` | Custom Field |
| `Firm_CostCenter` | Cost Center |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_CostCenter · TEXT` | Custom Field |
| `Firm_CreditCardFeesAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CreditCardFeesCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerEnterpriseSalesAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerEnterpriseSalesCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerInStorePurchaseReturnsAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerInStorePurchaseReturnsCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerOnlinePurchaseReturnsAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerOnlinePurchaseReturnsCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerPOSSalesAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerPOSSalesCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerShiptoStoreSalesAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerShiptoStoreSalesCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerSingleSwipeSalesAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_CustomerSingleSwipeSalesCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_DRLandlordPunchlistComplete` | Landlord's Punchlist Complete |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_DRLandlordPunchlistComplete · TEXT` | Custom Field |
| `Firm_DRRentAbatement` | Rent Abatement |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_DRRentAbatement · TEXT` | Custom Field |
| `Firm_DeliveryChargesAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_DeliveryChargesCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_EmployeeOnlinePurchaseReturnsAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_EmployeeOnlinePurchaseReturnsCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_EmployeeSalesAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_EmployeeSalesCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_Guarantor` | Guarantor |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_Guarantor · TEXT` | Custom Field |
| `Firm_LeaseStatus` | Lease Status |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_LeaseStatus · TEXT` | Custom Field |
| `Firm_LeaseYear` | Lease Year |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_LeaseYear · TEXT` | Custom Field |
| `Firm_ONCOTClause` | Ongoing Cotenancy Clause |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_ONCOTClause · TEXT` | Custom Field |
| `Firm_ONCOTFrequency` | Frequency |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_ONCOTFrequency · TEXT` | Custom Field |
| `Firm_ONCOTRemedy` | Remedy |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_ONCOTRemedy · TEXT` | Custom Field |
| `Firm_ONCOTRightToRequestRoster` | Right To Request Roster |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_ONCOTRightToRequestRoster · TEXT` | Custom Field |
| `Firm_ONCOTRighttoTerminate` | Right to Terminate |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_ONCOTRighttoTerminate · TEXT` | Custom Field |
| `Firm_OPCOTClause` | Opening Cotenancy Clause |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_OPCOTClause · TEXT` | Custom Field |
| `Firm_OPCOTRighttoTerminate` | Right to Terminate |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_OPCOTRighttoTerminate · TEXT` | Custom Field |
| `Firm_RETAdministrativeFee` | Administrative Fee |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETAdministrativeFee · TEXT` | Custom Field |
| `Firm_RETAdministrativeFeeExclusionsYN` | Administrative Fee Exclusions |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETAdministrativeFeeExclusionsYN · TEXT` | Custom Field |
| `Firm_RETAuditRightsYN` | Audit Rights |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETAuditRightsYN · TEXT` | Custom Field |
| `Firm_RETConsultingFeeAllowedYN` | Consulting Fee Allowed |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETConsultingFeeAllowedYN · TEXT` | Custom Field |
| `Firm_RETContributionsYN` | Contributions |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETContributionsYN · TEXT` | Custom Field |
| `Firm_RETFixedYN` | Is RET Fixed? |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETFixedYN · TEXT` | Custom Field |
| `Firm_RETLandlordtoProvideTaxBillsYN` | Landlord to Provide Tax Bills |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETLandlordtoProvideTaxBillsYN · TEXT` | Custom Field |
| `Firm_RETLeaseTermCapType` | Lease Term Cap Type |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETLeaseTermCapType · TEXT` | Custom Field |
| `Firm_RETLeaseTermCapYN` | Lease Term Cap |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETLeaseTermCapYN · TEXT` | Custom Field |
| `Firm_RETPRShareStatus` | Prorata Share Status |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETPRShareStatus · TEXT` | Custom Field |
| `Firm_RETStartingCapExclusionsYN` | Starting Cap Exclusions |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETStartingCapExclusionsYN · TEXT` | Custom Field |
| `Firm_RETStartingCapStatus` | Starting Cap Status |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETStartingCapStatus · TEXT` | Custom Field |
| `Firm_RETStartingCapYN` | Starting Cap |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETStartingCapYN · TEXT` | Custom Field |
| `Firm_RETStatementsBindingYN` | Statements Binding |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_RETStatementsBindingYN · TEXT` | Custom Field |
| `Firm_TenantLegalName` | Tenant Legal Name |  | Dropdown (Custom Field) | Firm |  | `contract_firm.Firm_TenantLegalName · TEXT` | Custom Field |
| `Firm_UncollectedCreditAllowable` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |
| `Firm_UncollectedCreditCap` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |

### Money (130)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AggregateBaseRent` | Aggregate Base Rent | This is a reporting field. The total of base rent with no tax where expense category is either "Rent" or "Lease Payment" between the computed payment begin date and the likely payment end date. | Currency | Global |  | `contract_financial.AggregateBaseRent · TEXT` |  |
| `AggregateBaseRentWithTax` | Aggregate Base Rent w/ Tax | This is a reporting field. The total of base rent with tax where the expense category is either "Rent" or "Lease Payment" between the computed payment begin date and the likely payment end date. | Currency | Global |  | `contract_financial.AggregateBaseRentWithTax · TEXT` |  |
| `AggregateNNNBaseRentNPV` | Aggregate NNN Base Rent NPV | This field is included in Test 4 of the Capital Lease Test. Enter the present value of NNN rent over the analysis period the "lease term". | Currency | Global |  | `contract_financial.AggregateNNNBaseRentNPV · TEXT` |  |
| `AggregateTotalRent` | Aggregate Total Rent | This is a reporting field. The total of base rent with no tax for all expense categories between the computed payment begin date and the likely payment end date. | Currency | Global |  | `contract_financial.AggregateTotalRent · TEXT` |  |
| `AggregateTotalRentWithTax` | Aggregate Total Rent w/ Tax | This is a reporting field. The total of base rent with tax for all expense categories between the computed payment begin date and the likely payment end date. | Currency | Global |  | `contract_financial.AggregateTotalRentWithTax · TEXT` |  |
| `BaseYearOperatingExpenses` | Base Year Operating Expenses | This field is included in Test 4 of the Capital Lease Test. Enter the amount of operating expenses included in the base rent. | Currency | Global |  | `contract_financial.BaseYearOperatingExpenses · TEXT` |  |
| `BaseYearOtherExpenses` | Base Year Other Expenses | This field is included in Test 4 of the Capital Lease Test. Enter the amount of any exclusions, other than operating expenses and taxes, from base rent. | Currency | Global |  | `contract_financial.BaseYearOtherExpenses · TEXT` |  |
| `BaseYearRETax` | Base Year RE Tax | This field is included in Test 4 of the Capital Lease Test. Enter the amount of real estate taxes included in the base rent. | Currency | Global |  | `contract_financial.BaseYearRETax · TEXT` |  |
| `BeyondFifthFiscalYearBaseRent` | Beyond Fifth Fiscal Year Base Rent | This is a reporting field. This field sums the total base rent without tax where the expense category is either "Rent" or "Lease Payment" for each fiscal year past four years after the current year. | Currency | Global |  | `contract_financial.BeyondFifthFiscalYearBaseRent · TEXT` |  |
| `BeyondFifthFiscalYearBaseRentWithTax` | Beyond Fifth Fiscal Year Base Rent w/ Tax | This is a reporting field. This field sums the total base rent with tax where the expense category is either "Rent" or "Lease Payment" for each fiscal year past four years after the current year. | Currency | Global |  | `contract_financial.BeyondFifthFiscalYearBaseRentWithTax · TEXT` |  |
| `BeyondFifthFiscalYearTotalRent` | Beyond Fifth Fiscal Year Total Rent | This is a reporting field. This field sums the total base rent without tax for each fiscal year past four years after the current year. | Currency | Global |  | `contract_financial.BeyondFifthFiscalYearTotalRent · TEXT` |  |
| `BeyondFifthFiscalYearTotalRentWithTax` | Beyond Fifth Fiscal Year Total Rent w/ Tax | This is a reporting field. This field sums the total base rent with tax for each fiscal year past four years after the current year. | Currency | Global |  | `contract_financial.BeyondFifthFiscalYearTotalRentWithTax · TEXT` |  |
| `BeyondFifthYearBaseRent` | Beyond Fifth Calendar Year Base Rent | This is a reporting field. This field sums the total base rent without tax where the expense category is either "Rent" or "Lease Payment" for each calendar year past four years after the current year. | Currency | Global |  | `contract_financial.BeyondFifthYearBaseRent · TEXT` |  |
| `BeyondFifthYearBaseRentWithTax` | Beyond Fifth Calendar Year Base Rent w/ Tax | This is a reporting field. This field sums the total base rent with tax where the expense category is either "Rent" or "Lease Payment" for each calendar year past four years after the current year. | Currency | Global |  | `contract_financial.BeyondFifthYearBaseRentWithTax · TEXT` |  |
| `BeyondFifthYearTotalRent` | Beyond Fifth Calendar Year Total Rent | This is a reporting field. This field sums the total base rent without tax for each calendar year past four years after the current year. | Currency | Global |  | `contract_financial.BeyondFifthYearTotalRent · TEXT` |  |
| `BeyondFifthYearTotalRentWithTax` | Beyond Fifth Calendar Year Total Rent w/ Tax | This is a reporting field. This field sums the total base rent with tax for each calendar year past four years after the current year. | Currency | Global |  | `contract_financial.BeyondFifthYearTotalRentWithTax · TEXT` |  |
| `BeyondSixthFiscalYearBaseRent` | Beyond Sixth Fiscal Year Base Rent | This is a reporting field. This field sums the total base rent without tax where the expense category is either "Rent" or "Lease Payment" for each fiscal year past five years after the current year. | Currency | Global |  | `contract_financial.BeyondSixthFiscalYearBaseRent · TEXT` |  |
| `BeyondSixthFiscalYearBaseRentWithTax` | Beyond Sixth Fiscal Year Base Rent w/ Tax | This is a reporting field. This field sums the total base rent with tax where the expense category is either "Rent" or "Lease Payment" for each fiscal year past five years after the current year. | Currency | Global |  | `contract_financial.BeyondSixthFiscalYearBaseRentWithTax · TEXT` |  |
| `BeyondSixthFiscalYearTotalRent` | Beyond Sixth Fiscal Year Total Rent | This is a reporting field. This field sums the total base rent without tax for each fiscal year past five years after the current year. | Currency | Global |  | `contract_financial.BeyondSixthFiscalYearTotalRent · TEXT` |  |
| `BeyondSixthFiscalYearTotalRentWithTax` | Beyond Sixth Fiscal Year Total Rent w/ Tax | This is a reporting field. This field sums the total base rent with tax for each fiscal year past five years after the current year. | Currency | Global |  | `contract_financial.BeyondSixthFiscalYearTotalRentWithTax · TEXT` |  |
| `BeyondSixthYearBaseRent` | Beyond Sixth Calendar Year Base Rent | This is a reporting field. This field sums the total base rent without tax where the expense category is either "Rent" or "Lease Payment" for each calendar year past five years after the current year. | Currency | Global |  | `contract_financial.BeyondSixthYearBaseRent · TEXT` |  |
| `BeyondSixthYearBaseRentWithTax` | Beyond Sixth Calendar Year Base Rent w/ Tax | This is a reporting field. This field sums the total base rent with tax where the expense category is either "Rent" or "Lease Payment" for each calendar year past five years after the current year. | Currency | Global |  | `contract_financial.BeyondSixthYearBaseRentWithTax · TEXT` |  |
| `BeyondSixthYearTotalRent` | Beyond Sixth Calendar Year Total Rent | This is a reporting field. This field sums the total base rent without tax for each calendar year past five years after the current year. | Currency | Global |  | `contract_financial.BeyondSixthYearTotalRent · TEXT` |  |
| `BeyondSixthYearTotalRentWithTax` | Beyond Sixth Calendar Year Total Rent w/ Tax | This is a reporting field. This field sums the total base rent with tax for each calendar year past five years after the current year. | Currency | Global |  | `contract_financial.BeyondSixthYearTotalRentWithTax · TEXT` |  |
| `CurrentAnnualBaseRent` | Current Annual Calendar Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the current calendar year. | Currency | Global |  | `contract_financial.CurrentAnnualBaseRent · TEXT` |  |
| `CurrentAnnualBaseRentWithTax` | Current Annual Calendar Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the current calendar year. | Currency | Global |  | `contract_financial.CurrentAnnualBaseRentWithTax · TEXT` |  |
| `CurrentAnnualFiscalBaseRent` | Current Annual Fiscal Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the current fiscal year. | Currency | Global |  | `contract_financial.CurrentAnnualFiscalBaseRent · TEXT` |  |
| `CurrentAnnualFiscalBaseRentWithTax` | Current Annual Fiscal Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the current fiscal year. | Currency | Global |  | `contract_financial.CurrentAnnualFiscalBaseRentWithTax · TEXT` |  |
| `CurrentAnnualFiscalTotalRent` | Current Annual Fiscal Total Rent | This is a reporting field. The total base rent without tax for the current fiscal year. | Currency | Global |  | `contract_financial.CurrentAnnualFiscalTotalRent · TEXT` |  |
| `CurrentAnnualFiscalTotalRentWithTax` | Current Annual Fiscal Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the current fiscal year. | Currency | Global |  | `contract_financial.CurrentAnnualFiscalTotalRentWithTax · TEXT` |  |
| `CurrentAnnualTotalRent` | Current Annual Calendar Total Rent | This field appears on the Contract > Details > Summary page. It calculates the sum of your annual recurring expenses. | Currency | Global |  | `contract_financial.CurrentAnnualTotalRent · TEXT` |  |
| `CurrentAnnualTotalRentWithTax` | Current Annual Calendar Total Rent w/ Tax | Calculates the sum of your annual recurring expenses plus any applicable taxes. | Currency | Global |  | `contract_financial.CurrentAnnualTotalRentWithTax · TEXT` |  |
| `CurrentCalendarYearGrossSales` | Current Calendar Year Gross Sales | This is a reporting field. The total sales for the current calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearGrossSales · TEXT` |  |
| `CurrentCalendarYearQ1BaseRent` | Current Calendar Q1 Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the 1st Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ1BaseRent · TEXT` |  |
| `CurrentCalendarYearQ1BaseRentWithTax` | Current Calendar Q1 Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the 1st quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ1BaseRentWithTax · TEXT` |  |
| `CurrentCalendarYearQ1TotalRent` | Current Calendar Q1 Total Rent | This is a reporting field. The total base rent without tax for the 1st Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ1TotalRent · TEXT` |  |
| `CurrentCalendarYearQ1TotalRentWithTax` | Current Calendar Q1 Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the 1st Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ1TotalRentWithTax · TEXT` |  |
| `CurrentCalendarYearQ2BaseRent` | Current Calendar Q2 Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the 2nd Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ2BaseRent · TEXT` |  |
| `CurrentCalendarYearQ2BaseRentWithTax` | Current Calendar Q2 Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the 2nd quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ2BaseRentWithTax · TEXT` |  |
| `CurrentCalendarYearQ2TotalRent` | Current Calendar Q2 Total Rent | This is a reporting field. The total base rent without tax for the 2nd Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ2TotalRent · TEXT` |  |
| `CurrentCalendarYearQ2TotalRentWithTax` | Current Calendar Q2 Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the 2nd Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ2TotalRentWithTax · TEXT` |  |
| `CurrentCalendarYearQ3BaseRent` | Current Calendar Q3 Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the 3rd Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ3BaseRent · TEXT` |  |
| `CurrentCalendarYearQ3BaseRentWithTax` | Current Calendar Q3 Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the 3rd quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ3BaseRentWithTax · TEXT` |  |
| `CurrentCalendarYearQ3TotalRent` | Current Calendar Q3 Total Rent | This is a reporting field. The total base rent without tax for the 3rd Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ3TotalRent · TEXT` |  |
| `CurrentCalendarYearQ3TotalRentWithTax` | Current Calendar Q3 Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the 3rd Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ3TotalRentWithTax · TEXT` |  |
| `CurrentCalendarYearQ4BaseRent` | Current Calendar Q4 Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the 4th Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ4BaseRent · TEXT` |  |
| `CurrentCalendarYearQ4BaseRentWithTax` | Current Calendar Q4 Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the 4th quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ4BaseRentWithTax · TEXT` |  |
| `CurrentCalendarYearQ4TotalRent` | Current Calendar Q4 Total Rent | This is a reporting field. The total base rent without tax for the 4th Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ4TotalRent · TEXT` |  |
| `CurrentCalendarYearQ4TotalRentWithTax` | Current Calendar Q4 Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the 4th Quarter in the calendar year. | Currency | Global |  | `contract_financial.CurrentCalendarYearQ4TotalRentWithTax · TEXT` |  |
| `CurrentFiscalYearQ1BaseRent` | Current Fiscal Q1 Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the 1st Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ1BaseRent · TEXT` |  |
| `CurrentFiscalYearQ1BaseRentWithTax` | Current Fiscal Q1 Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the 1st Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ1BaseRentWithTax · TEXT` |  |
| `CurrentFiscalYearQ1TotalRent` | Current Fiscal Q1 Total Rent | This is a reporting field. The total base rent without tax for the 1st Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ1TotalRent · TEXT` |  |
| `CurrentFiscalYearQ1TotalRentWithTax` | Current Fiscal Q1 Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the 1st Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ1TotalRentWithTax · TEXT` |  |
| `CurrentFiscalYearQ2BaseRent` | Current Fiscal Q2 Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the 2nd Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ2BaseRent · TEXT` |  |
| `CurrentFiscalYearQ2BaseRentWithTax` | Current Fiscal Q2 Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the 2nd Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ2BaseRentWithTax · TEXT` |  |
| `CurrentFiscalYearQ2TotalRent` | Current Fiscal Q2 Total Rent | This is a reporting field. The total base rent without tax for the 2nd Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ2TotalRent · TEXT` |  |
| `CurrentFiscalYearQ2TotalRentWithTax` | Current Fiscal Q2 Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the 2nd Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ2TotalRentWithTax · TEXT` |  |
| `CurrentFiscalYearQ3BaseRent` | Current Fiscal Q3 Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the 3rd Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ3BaseRent · TEXT` |  |
| `CurrentFiscalYearQ3BaseRentWithTax` | Current Fiscal Q3 Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the 3rd Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ3BaseRentWithTax · TEXT` |  |
| `CurrentFiscalYearQ3TotalRent` | Current Fiscal Q3 Total Rent | This is a reporting field. The total base rent without tax for the 3rd Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ3TotalRent · TEXT` |  |
| `CurrentFiscalYearQ3TotalRentWithTax` | Current Fiscal Q3 Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the 3rd Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ3TotalRentWithTax · TEXT` |  |
| `CurrentFiscalYearQ4BaseRent` | Current Fiscal Q4 Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the 4th Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ4BaseRent · TEXT` |  |
| `CurrentFiscalYearQ4BaseRentWithTax` | Current Fiscal Q4 Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the 4th Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ4BaseRentWithTax · TEXT` |  |
| `CurrentFiscalYearQ4TotalRent` | Current Fiscal Q4 Total Rent | This is a reporting field. The total base rent without tax for the 4th Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ4TotalRent · TEXT` |  |
| `CurrentFiscalYearQ4TotalRentWithTax` | Current Fiscal Q4 Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the 4th Quarter in the fiscal year. | Currency | Global |  | `contract_financial.CurrentFiscalYearQ4TotalRentWithTax · TEXT` |  |
| `CurrentMonthlyBaseRent` | Current Monthly Base Rent | The current monthly rent without taxes. | Currency | Global |  | `contract_financial.CurrentMonthlyBaseRent · TEXT` |  |
| `CurrentMonthlyBaseRentWithTax` | Current Monthly Base Rent w/ Tax | The current monthly rent with taxes. | Currency | Global |  | `contract_financial.CurrentMonthlyBaseRentWithTax · TEXT` |  |
| `CurrentMonthlyTotalRent` | Current Monthly Total Rent | This field appears on the Contract > Details > Summary page. It calculates the sum of your monthly recurring expenses. | Currency | Global |  | `contract_financial.CurrentMonthlyTotalRent · TEXT` |  |
| `CurrentMonthlyTotalRentWithTax` | Current Monthly Total Rent w/ Tax | Calculates the sum of your monthly recurring expenses plus any applicable taxes. | Currency | Global |  | `contract_financial.CurrentMonthlyTotalRentWithTax · TEXT` |  |
| `CurrentPeriodBaseRent` | Current Period Base Rent | The base rent of the current period without taxes. If your fiscal calendar has not been configured, then the system returns the current calendar month's base rent without taxes. | Currency | Global |  | `contract_financial.CurrentPeriodBaseRent · TEXT` |  |
| `CurrentPeriodBaseRentWithTax` | Current Period Base Rent w/ Tax | The base rent of the current period with taxes. If your fiscal calendar has not been configured, then the system returns the current calendar month's base rent with taxes. | Currency | Global |  | `contract_financial.CurrentPeriodBaseRentWithTax · TEXT` |  |
| `CurrentPeriodTotalRent` | Current Period Total Rent | The total rent of the current period without taxes. If your fiscal calendar has not been configured, then the system returns the current calendar month's total rent without taxes. | Currency | Global |  | `contract_financial.CurrentPeriodTotalRent · TEXT` |  |
| `CurrentPeriodTotalRentWithTax` | Current Period Total Rent w/ Tax | The total rent of the current period with taxes. If your fiscal calendar has not been configured, then the system returns the current calendar month's total rent with taxes. | Currency | Global |  | `contract_financial.CurrentPeriodTotalRentWithTax · TEXT` |  |
| `CurrentStraightLineAssetBalance` | Current Straight Line Asset Balance | The asset balance value from the first active period. | Currency | Global |  | `contract_financial.CurrentStraightLineAssetBalance · TEXT` |  |
| `CurrentStraightLineLiabilityBalance` | Current Straight Line Liability Balance | The liability balance value from the first active period. | Currency | Global |  | `contract_financial.CurrentStraightLineLiabilityBalance · TEXT` |  |
| `FMVOfBuilding` | FMV Of Building | This field is included in Test 4 of the Capital Lease Test. Enter the price at which the property would change hands between a willing buyer and a willing seller, neither being under any compulsion to buy or to sell and both having reasonable knowledge of relevant facts. | Currency | Global |  | `contract_financial.FMVOfBuilding · TEXT` |  |
| `FMVOfLand` | FMV Of Land | This field is included in Test 4 of the Capital Lease Test. Enter the fair market value of the land. | Currency | Global |  | `contract_financial.FMVOfLand · TEXT` |  |
| `FifthFiscalYearBaseRent` | Fifth Fiscal Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the fiscal year four years after the current year. | Currency | Global |  | `contract_financial.FifthFiscalYearBaseRent · TEXT` |  |
| `FifthFiscalYearBaseRentWithTax` | Fifth Fiscal Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the fiscal year four years after the current year. | Currency | Global |  | `contract_financial.FifthFiscalYearBaseRentWithTax · TEXT` |  |
| `FifthFiscalYearTotalRent` | Fifth Fiscal Year Total Rent | This is a reporting field. The total base rent without tax for the fiscal year four years after the current year. | Currency | Global |  | `contract_financial.FifthFiscalYearTotalRent · TEXT` |  |
| `FifthFiscalYearTotalRentWithTax` | Fifth Fiscal Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the fiscal year four years after the current year. | Currency | Global |  | `contract_financial.FifthFiscalYearTotalRentWithTax · TEXT` |  |
| `FifthYearBaseRent` | Fifth Calendar Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the calendar year four years after the current year. | Currency | Global |  | `contract_financial.FifthYearBaseRent · TEXT` |  |
| `FifthYearBaseRentWithTax` | Fifth Calendar Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the calendar year four years after the current year. | Currency | Global |  | `contract_financial.FifthYearBaseRentWithTax · TEXT` |  |
| `FifthYearTotalRent` | Fifth Calendar Year Total Rent | This is a reporting field. The total base rent without tax for the calendar year four years after the current year. | Currency | Global |  | `contract_financial.FifthYearTotalRent · TEXT` |  |
| `FifthYearTotalRentWithTax` | Fifth Calendar Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the calendar year four years after the current year. | Currency | Global |  | `contract_financial.FifthYearTotalRentWithTax · TEXT` |  |
| `Firm_LastDeferredSLEntry` | Last Deferred SL Entry |  | Currency | Firm |  | `contract_firm.Firm_LastDeferredSLEntry · TEXT` |  |
| `Firm_LastDeferredSLTotal` | Last Deferred SL Total |  | Currency | Firm |  | `contract_firm.Firm_LastDeferredSLTotal · TEXT` |  |
| `Firm_PriorMonthAccrualTotal` |  |  | Currency | — |  |  |  |
| `FourthFiscalYearBaseRent` | Fourth Fiscal Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the fiscal year three years after the current year. | Currency | Global |  | `contract_financial.FourthFiscalYearBaseRent · TEXT` |  |
| `FourthFiscalYearBaseRentWithTax` | Fourth Fiscal Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the fiscal year three years after the current year. | Currency | Global |  | `contract_financial.FourthFiscalYearBaseRentWithTax · TEXT` |  |
| `FourthFiscalYearTotalRent` | Fourth Fiscal Year Total Rent | This is a reporting field. The total base rent without tax for the fiscal year three years after the current year. | Currency | Global |  | `contract_financial.FourthFiscalYearTotalRent · TEXT` |  |
| `FourthFiscalYearTotalRentWithTax` | Fourth Fiscal Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the fiscal year three years after the current year. | Currency | Global |  | `contract_financial.FourthFiscalYearTotalRentWithTax · TEXT` |  |
| `FourthYearBaseRent` | Fourth Calendar Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the calendar year three years after the current year. | Currency | Global |  | `contract_financial.FourthYearBaseRent · TEXT` |  |
| `FourthYearBaseRentWithTax` | Fourth Calendar Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the calendar year three years after the current year. | Currency | Global |  | `contract_financial.FourthYearBaseRentWithTax · TEXT` |  |
| `FourthYearTotalRent` | Fourth Calendar Year Total Rent | This is a reporting field. The total base rent without tax for the calendar year three years after the current year. | Currency | Global |  | `contract_financial.FourthYearTotalRent · TEXT` |  |
| `FourthYearTotalRentWithTax` | Fourth Calendar Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the calendar year three years after the current year. | Currency | Global |  | `contract_financial.FourthYearTotalRentWithTax · TEXT` |  |
| `NextFiscalYearBaseRent` | Next Fiscal Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the next fiscal year. | Currency | Global |  | `contract_financial.NextFiscalYearBaseRent · TEXT` |  |
| `NextFiscalYearBaseRentWithTax` | Next Fiscal Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the next fiscal year. | Currency | Global |  | `contract_financial.NextFiscalYearBaseRentWithTax · TEXT` |  |
| `NextFiscalYearTotalRent` | Next Fiscal Year Total Rent | This is a reporting field. The total base rent without tax for the next fiscal year. | Currency | Global |  | `contract_financial.NextFiscalYearTotalRent · TEXT` |  |
| `NextFiscalYearTotalRentWithTax` | Next Fiscal Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the next fiscal year. | Currency | Global |  | `contract_financial.NextFiscalYearTotalRentWithTax · TEXT` |  |
| `NextYearBaseRent` | Next Calendar Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the next calendar year. | Currency | Global |  | `contract_financial.NextYearBaseRent · TEXT` |  |
| `NextYearBaseRentWithTax` | Next Calendar Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the next calendar year. | Currency | Global |  | `contract_financial.NextYearBaseRentWithTax · TEXT` |  |
| `NextYearTotalRent` | Next Calendar Year Total Rent | This is a reporting field. The total base rent without tax for the next calendar year. | Currency | Global |  | `contract_financial.NextYearTotalRent · TEXT` |  |
| `NextYearTotalRentWithTax` | Next Calendar Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the next calendar year. | Currency | Global |  | `contract_financial.NextYearTotalRentWithTax · TEXT` |  |
| `PriorCalendarYearGrossSales` | Prior Calendar Year Gross Sales | The annual sales from the current calendar year OR the start date of the report. | Currency | Global |  | `contract_financial.PriorCalendarYearGrossSales · TEXT` |  |
| `RemainingFiscalObligationBaseRent` | Remaining Base Rent Obligation(Fiscal Year) | The remaining base rent without tax from the next period to the last period of the current fiscal year where the expense category is either "Rent" or "Lease Payment". | Currency | Global |  | `contract_financial.RemainingFiscalObligationBaseRent · TEXT` |  |
| `RemainingFiscalObligationBaseRentWithTax` | Remaining Base Rent Obligation(Fiscal Year) w/ Tax | The remaining base rent with tax from the next period to the last period of the current fiscal year where the expense category is either "Rent" or "Lease Payment". | Currency | Global |  | `contract_financial.RemainingFiscalObligationBaseRentWithTax · TEXT` |  |
| `RemainingFiscalObligationTotalRent` | Remaining Total Rent Obligation(Fiscal Year) | The remaining total rent without tax from the next period to the end period for the current fiscal year. | Currency | Global |  | `contract_financial.RemainingFiscalObligationTotalRent · TEXT` |  |
| `RemainingFiscalObligationTotalRentWithTax` | Remaining Total Rent Obligation(Fiscal Year) w/ Tax | The remaining total rent with tax from the next period to the last period of the current fiscal year. | Currency | Global |  | `contract_financial.RemainingFiscalObligationTotalRentWithTax · TEXT` |  |
| `RemainingObligationBaseRent` | Remaining Base Rent Obligation | The remaining base rent without tax from the next period to the last period of the current calendar year where the expense category is either "Rent" or "Lease Payment". | Currency | Global |  | `contract_financial.RemainingObligationBaseRent · TEXT` |  |
| `RemainingObligationBaseRentWithTax` | Remaining Base Rent Obligation w/ Tax | The remaining base rent with tax from the next period to the last period of the current calendar year where the expense category is either "Rent" or "Lease Payment". | Currency | Global |  | `contract_financial.RemainingObligationBaseRentWithTax · TEXT` |  |
| `RemainingObligationTotalRent` | Remaining Total Rent Obligation | The remaining total rent without tax from the next period to the last period of the current calendar year. | Currency | Global |  | `contract_financial.RemainingObligationTotalRent · TEXT` |  |
| `RemainingObligationTotalRentWithTax` | Remaining Total Rent Obligation w/ Tax | The remaining total rent with tax from the next period to the last period of the current calendar year. | Currency | Global |  | `contract_financial.RemainingObligationTotalRentWithTax · TEXT` |  |
| `SixthFiscalYearBaseRent` | Sixth Fiscal Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the fiscal year five years after the current year. | Currency | Global |  | `contract_financial.SixthFiscalYearBaseRent · TEXT` |  |
| `SixthFiscalYearBaseRentWithTax` | Sixth Fiscal Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the fiscal year five years after the current year. | Currency | Global |  | `contract_financial.SixthFiscalYearBaseRentWithTax · TEXT` |  |
| `SixthFiscalYearTotalRent` | Sixth Fiscal Year Total Rent | This is a reporting field. The total base rent without tax for the fiscal year five years after the current year. | Currency | Global |  | `contract_financial.SixthFiscalYearTotalRent · TEXT` |  |
| `SixthFiscalYearTotalRentWithTax` | Sixth Fiscal Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the fiscal year five years after the current year. | Currency | Global |  | `contract_financial.SixthFiscalYearTotalRentWithTax · TEXT` |  |
| `SixthYearBaseRent` | Sixth Calendar Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the calendar year five years after the current year. | Currency | Global |  | `contract_financial.SixthYearBaseRent · TEXT` |  |
| `SixthYearBaseRentWithTax` | Sixth Calendar Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the calendar year five years after the current year. | Currency | Global |  | `contract_financial.SixthYearBaseRentWithTax · TEXT` |  |
| `SixthYearTotalRent` | Sixth Calendar Year Total Rent | This is a reporting field. The total base rent without tax for the calendar year five years after the current year. | Currency | Global |  | `contract_financial.SixthYearTotalRent · TEXT` |  |
| `SixthYearTotalRentWithTax` | Sixth Calendar Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the calendar year five years after the current year. | Currency | Global |  | `contract_financial.SixthYearTotalRentWithTax · TEXT` |  |
| `ThirdFiscalYearBaseRent` | Third Fiscal Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the fiscal year two years after the current year. | Currency | Global |  | `contract_financial.ThirdFiscalYearBaseRent · TEXT` |  |
| `ThirdFiscalYearBaseRentWithTax` | Third Fiscal Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the fiscal year two years after the current year. | Currency | Global |  | `contract_financial.ThirdFiscalYearBaseRentWithTax · TEXT` |  |
| `ThirdFiscalYearTotalRent` | Third Fiscal Year Total Rent | This is a reporting field. The total base rent without tax for the fiscal year two years after the current year. | Currency | Global |  | `contract_financial.ThirdFiscalYearTotalRent · TEXT` |  |
| `ThirdFiscalYearTotalRentWithTax` | Third Fiscal Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the fiscal year two years after the current year. | Currency | Global |  | `contract_financial.ThirdFiscalYearTotalRentWithTax · TEXT` |  |
| `ThirdYearBaseRent` | Third Calendar Year Base Rent | This is a reporting field. The total base rent without tax where the expense category is either "Rent" or "Lease Payment" for the calendar year two years after the current year. | Currency | Global |  | `contract_financial.ThirdYearBaseRent · TEXT` |  |
| `ThirdYearBaseRentWithTax` | Third Calendar Year Base Rent w/ Tax | This is a reporting field. The total base rent with tax where the expense category is either "Rent" or "Lease Payment" for the calendar year two years after the current year. | Currency | Global |  | `contract_financial.ThirdYearBaseRentWithTax · TEXT` |  |
| `ThirdYearTotalRent` | Third Calendar Year Total Rent | This is a reporting field. The total base rent without tax for the calendar year two years after the current year. | Currency | Global |  | `contract_financial.ThirdYearTotalRent · TEXT` |  |
| `ThirdYearTotalRentWithTax` | Third Calendar Year Total Rent w/ Tax | This is a reporting field. The total base rent with tax for the calendar year two years after the current year. | Currency | Global |  | `contract_financial.ThirdYearTotalRentWithTax · TEXT` |  |
| `math_currPaymentRate_9` | currPaymentRate | This is a math field which calculates Contract Current Payment Rate. | Currency | Global |  | `contract_financial.math_currPaymentRate_9 · TEXT` |  |

### Rates & percentages (35)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ComputedSLDiscountRate` | Computed Discount Rate | The default discount rate. Lx will first use the discount rate at the Portfolio-level, if it exists, otherwise it will use the rate at the Firm-level. This field will not pull the discount rate from the contract-level. | Percentage | Global |  | `contract_financial.ComputedSLDiscountRate · TEXT` |  |
| `ContractTaxRate1` | Contract Tax Rate #1 | This field captures tax rate 1 from your RE contract or Equipment contract. | Percentage | Global |  | `contract_financial.ContractTaxRate1 · TEXT` |  |
| `ContractTaxRate2` | Contract Tax Rate #2 | This field captures tax rate 2 from your RE contract or Equipment contract. | Percentage | Global |  | `contract_financial.ContractTaxRate2 · TEXT` |  |
| `ContractTaxRate3` | Contract Tax Rate #3 | This field captures tax rate 3 from your RE contract or Equipment contract. | Percentage | Global |  | `contract_financial.ContractTaxRate3 · TEXT` |  |
| `ContractTaxRate4` | Contract Tax Rate #4 | This field captures tax rate 4 from your RE contract or Equipment contract. | Percentage | Global |  | `contract_financial.ContractTaxRate4 · TEXT` |  |
| `DiscountRate` | Contract Discount Rate | This field is where you enter the Discount Rate (also known as the Interest Rate or the Internal Borrower Rate [IBR]). | Percentage | Global |  | `contract_financial.DiscountRate · TEXT` |  |
| `FairValueThreshold` | Fair Value Threshold | This field computes the default fair value threshold to use for the contract. The system uses the portfolio-level value if one exists, otherwise it uses the Firm-level value. | Percentage | Global |  | `contract_financial.FairValueThreshold · TEXT` |  |
| `Firm_BankChargesCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_CAMAdministrativeFeePercent` | Administrative Fee Percent |  | Percentage | Firm |  | `contract_firm.Firm_CAMAdministrativeFeePercent · TEXT` |  |
| `Firm_CAMFixedIncreasePercent` | Fixed CAM Increase Percent |  | Percentage | Firm |  | `contract_firm.Firm_CAMFixedIncreasePercent · TEXT` |  |
| `Firm_CAMFloorPercent` | Floor Percent |  | Percentage | Firm |  | `contract_firm.Firm_CAMFloorPercent · TEXT` |  |
| `Firm_CAMLeaseTermCapPercent` | Lease Term Cap Percent |  | Percentage | Firm |  | `contract_firm.Firm_CAMLeaseTermCapPercent · TEXT` |  |
| `Firm_CreditCardFeesCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_CustomerEnterpriseSalesCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_CustomerInStorePurchaseReturnsCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_CustomerOnlinePurchaseReturnsCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_CustomerPOSSalesCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_CustomerShiptoStoreSalesCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_CustomerSingleSwipeSalesCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_DeliveryChargesCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_EmployeeSalesCapPercent` |  |  | Percentage | — |  |  |  |
| `Firm_ONCOTRequiredPercentofInlineSpace` | Required Percent of Inline Space |  | Percentage | Firm |  | `contract_firm.Firm_ONCOTRequiredPercentofInlineSpace · TEXT` |  |
| `Firm_OPCOTRequiredPercentofInlineSpace` | Required Percent of Inline Space |  | Percentage | Firm |  | `contract_firm.Firm_OPCOTRequiredPercentofInlineSpace · TEXT` |  |
| `Firm_RETAdministrativeFeePercent` | Administrative Fee Percent |  | Percentage | Firm |  | `contract_firm.Firm_RETAdministrativeFeePercent · TEXT` |  |
| `Firm_RETFloorPercent` | Floor Percent |  | Percentage | Firm |  | `contract_firm.Firm_RETFloorPercent · TEXT` |  |
| `Firm_RETLeaseTermCapPercent` | Lease Term Cap Percent |  | Percentage | Firm |  | `contract_firm.Firm_RETLeaseTermCapPercent · TEXT` |  |
| `Firm_UncollectedCreditCapPercent` |  |  | Percentage | — |  |  |  |
| `PaymentRate` | Payment Rate | This field appears on the Contract > Details > Summary page and contains the payment rate for your contract. | Percentage | Global |  | `contract_financial.PaymentRate · TEXT` |  |
| `ProRataShareRate` | Pro Rata Share Rate | Pro Rata Share refers to a proportionate share of an expense. For example, many contracts for tenants of indoor malls stipulate that each tenant pay a pre-determined percentage of common area maintenance (CAM) expenses. | Percentage | Global |  | `contract_financial.ProRataShareRate · TEXT` |  |
| `RatioLeaseAutoRenewToFMV` | Ratio Lease w/ Auto Renewal To FMV | This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test. | Percentage | Global |  | `contract_financial.RatioLeaseAutoRenewToFMV · TEXT` |  |
| `RatioLeaseBargainRenewToFMV` | Ratio Lease w/ Bargain Renewal To FMV | This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test. | Percentage | Global |  | `contract_financial.RatioLeaseBargainRenewToFMV · TEXT` |  |
| `RatioTermAutoRenewToLife` | Ratio Term w/ Auto Renewal To Life | This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test. | Percentage | Global |  | `contract_financial.RatioTermAutoRenewToLife · TEXT` |  |
| `RatioTermBargainRenewToLife` | Ratio Term w/ Bargain Renewal To Life | This is a legacy field that was used in the Capital Lease Test. It is no longer used, and does not impact the test. | Percentage | Global |  | `contract_financial.RatioTermBargainRenewToLife · TEXT` |  |
| `RemainingEconomicLifeThreshold` | Remaining Economic Life Threshold | This field computes the default value of the remaining economic life threshold field to use for this contract. The field first searches for a portfolio-level value, and if none is found, it uses the firm-level value. | Percentage | Global |  | `contract_financial.RemainingEconomicLifeThreshold · TEXT` |  |

### Quantities (39)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | This field is not implemented for contracts or equipment contracts. | Number | — |  | `contract_admin.ActualRevenueWeeks · TEXT` |  |
| `BehindScheduleDays` | Schedule Behind Days | This field displays the number of days behind schedule. | Number | Global |  | `contract_admin.BehindScheduleDays · TEXT` |  |
| `ContractID` | Contract RecID | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Number | Global |  | `contract_firm.ContractID · VARCHAR(64) NOT NULL` |  |
| `ContractID` | Contract RecID | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Number | Global |  | `contract_firm.ContractID · VARCHAR(64) NOT NULL` |  |
| `ContractID` | Contract RecID | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Number | Global |  | `contract_firm.ContractID · VARCHAR(64) NOT NULL` |  |
| `CurrentYear` | Current Year | The current year. | Number | Global |  | `contract_financial.CurrentYear · TEXT` |  |
| `DBFolderSizeMB` | Storage Size (MB) | The folder size in megabytes for a given entity. | 2-Digit Number | — |  | `contract_admin.DBFolderSizeMB · TEXT` |  |
| `DaysToExpiration` | Days to Expiration | The number of days until the contract expires. | Number with no digits | Global |  | `contract_admin.DaysToExpiration · TEXT` |  |
| `Depth` |  | This field is not implemented for contracts or equipment contracts. | Number | — |  | `contract_admin.Depth · TEXT` |  |
| `EntityId` | Entity LxID | The Project Entity ID. | Number | — |  | `contract_admin.EntityId · TEXT` |  |
| `Firm_BuildoutDuration` | Buildout Duration |  | Number with no digits | — |  | `contract_firm.Firm_BuildoutDuration · TEXT` |  |
| `Firm_CAMInitialFixedMO` | Initial Fixed CAM Monthly |  | Number | Firm |  | `contract_firm.Firm_CAMInitialFixedMO · TEXT` |  |
| `Firm_CAMInitialFixedPSF` | Initial Fixed CAM PSF |  | Number | Firm |  | `contract_firm.Firm_CAMInitialFixedPSF · TEXT` |  |
| `Firm_CAMNumberofYearsAuditable` | Number of Years Auditable |  | Number | Firm |  | `contract_firm.Firm_CAMNumberofYearsAuditable · TEXT` |  |
| `Firm_CAMStartingCapAmountPSF` | Starting Cap Amount PSF |  | Number | Firm |  | `contract_firm.Firm_CAMStartingCapAmountPSF · TEXT` |  |
| `Firm_CAMStartingCapMonthly` | Starting Cap Amount Monthly |  | Number | Firm |  | `contract_firm.Firm_CAMStartingCapMonthly · TEXT` |  |
| `Firm_CorporateCode` | Corp |  | Number | Firm |  | `contract_firm.Firm_CorporateCode · TEXT` |  |
| `Firm_FixturingPeriod` | Fixturing Period |  | Number | Firm |  | `contract_firm.Firm_FixturingPeriod · TEXT` |  |
| `Firm_NSInternalID` |  |  | Number | — |  |  |  |
| `Firm_RETInitialEstimateMonthly` | Initial Estimate Monthly |  | Number | Firm |  | `contract_firm.Firm_RETInitialEstimateMonthly · TEXT` |  |
| `Firm_RETInitialEstimatePSF` | Initial Estimate PSF |  | Number | Firm |  | `contract_firm.Firm_RETInitialEstimatePSF · TEXT` |  |
| `Firm_RETStartingCapAmount` | Starting Cap Amount |  | Number | Firm |  | `contract_firm.Firm_RETStartingCapAmount · TEXT` |  |
| `Frontage` |  | This field is not implemented for contracts or equipment contracts. | Number | — |  | `contract_admin.Frontage · TEXT` |  |
| `LatitudeDegrees` | Latitude | This field pulls the latitude value from the contract's associated location record. | 5-Digit Number | — |  | `contract_admin.LatitudeDegrees · TEXT` |  |
| `LeasedLandArea` | Leased Land Area | This field is included in Test 4 of the Capital Lease Test. Enter the area of any additional land that may be leased under the contract. For example, a parking lot. | Number | Global |  | `contract_admin.LeasedLandArea · TEXT` |  |
| `LongitudeDegrees` | Longitude | This field pulls the longitude value from the contract's associated location record. | 5-Digit Number | — |  | `contract_admin.LongitudeDegrees · TEXT` |  |
| `NumberOfDocuments` | Number of Documents | The total number of documents in all folders on the entity. | Number | — |  | `contract_admin.NumberOfDocuments · TEXT` |  |
| `OpenYear` | Open Year | The year the project opened. The year is computed based upon the actual end date. | Number | Global |  | `contract_financial.OpenYear · TEXT` |  |
| `OutOfDateDays` | Out Of Date Days | This field returns how many days the schedule is out of date. If the schedule hasn't been updated yet, the value of this field is 0. If the schedule has been updated, the value of the field is calculated based on the last reviewed date. | Number | Global |  | `contract_admin.OutOfDateDays · TEXT` |  |
| `ProjectEntityID` | Entity RecID | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Number | — |  | `contract_admin.ProjectEntityID · TEXT` |  |
| `ProjectLandArea` | Project Land Area | This field is included in Test 4 of the Capital Lease Test. Enter the total area of the lot that the building occupies. | Number | Global |  | `contract_admin.ProjectLandArea · TEXT` |  |
| `RemainingLife` | Remaining Life | This field appears in Test 3 of the Capital Lease Test. Enter the remaining useful life in this field. The Economic Useful Life is the estimated remaining period during which the property is expected to be of economic use by one or more users, with normal repairs and maintenance, for the purpose that it was intended at the inception of the lease. | Number | Global |  | `contract_financial.RemainingLife · TEXT` |  |
| `RemainingNumberOfTerms` | Remaining Number of Terms | The number of remaining terms for the contract. | Number | Global |  | `contract_financial.RemainingNumberOfTerms · TEXT` |  |
| `RentableArea` | Rentable Area | The Rentable Area field must be populated in order for the system to calculate your rate. The system will remember your rentable area and populate this field whenever it is present on a page. If you are not going to use rentable area, do not enter 0. Leave this field blank. | Number | Global |  | `contract_financial.RentableArea · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | — |  | `contract_admin.SequenceNumber · TEXT` |  |
| `TermLength` | Term Length | The contract term length in years. | Number | Global |  | `contract_admin.TermLength · TEXT` |  |
| `UsableArea` | Usable Area | This field is not implemented for the contract module. | Number | — |  | `contract_admin.UsableArea · TEXT` |  |
| `YearBuilt` | Year Built | This field appears in Test 3 of the Capital Lease Test. Select the year that the asset was built or the year that the asset's useful life began from the field. | Number | Global |  | `contract_financial.YearBuilt · TEXT` |  |
| `zFirm_LeaseSquareFootage` | zLeaseSquareFootage |  | 2-Digit Number | Firm |  |  |  |

### Dates & timestamps (41)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualEndDate` | Actual End Date | If there is a milestone timeline, The max end date from all non-operating tasks. Otherwise, The end date for the entity utilizing the schedule. If there are no tasks defined yet, the system will return the Original End Date / Completion Year set for the entity. | Date | Global |  | `contract_admin.ActualEndDate · TEXT` |  |
| `ActualStartDate` | Actual Start Date | The start date for the schedule associated with your entity. If there are no tasks defined in your schedule, The Original End Date / Completion Year set for the entity. | Date | Global |  | `contract_admin.ActualStartDate · TEXT` |  |
| `BaselineEndDate` | Baseline End Date | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | Global |  | `contract_admin.BaselineEndDate · TEXT` |  |
| `BaselineStartDate` | Baseline Start Date | Get the baseline start date for the entity utilizing the schedule if it exists. If there are no tasks defined yet, this field will return the original start date and year set for the entity. | Date | Global |  | `contract_admin.BaselineStartDate · TEXT` |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | This field displays the last updated date. | Date | — |  | `contract_admin.ClientScheduleLastReviewedDate · TEXT` |  |
| `CommenceDate` | Commence Date | Enter the date when the first term for the lease started in this field. The Commencement Date and the Expiration Date must be populated in order to use the term wizard when setting up a lease. | Date | Global |  | `contract_admin.CommenceDate · TEXT` |  |
| `ExecuteDate` | Execute Date | The Contract Execution date. | Date | Global |  | `contract_admin.ExecuteDate · TEXT` |  |
| `ExpectedEndDate` | Expected End Date | The original end date of the contract task schedule if the contract has one. | Date | Global |  | `contract_admin.ExpectedEndDate · TEXT` |  |
| `ExpireDate` | Expire Date | Enter the current expiration date (excluding options) in this field. The Commencement Date and the Expiration Date must be populated in order to use the term wizard when setting up a lease. | Date | Global |  | `contract_admin.ExpireDate · TEXT` |  |
| `Firm_AnticipatedDeliveryDate` |  |  | Date | — |  |  |  |
| `Firm_BankChargesBeginDate` |  |  | Date | — |  |  |  |
| `Firm_CAMDateofFirstIncrease` | Date of First Increase |  | Date | Firm |  | `contract_firm.Firm_CAMDateofFirstIncrease · TEXT` |  |
| `Firm_CreditCardFeesBeginDate` |  |  | Date | — |  |  |  |
| `Firm_CustomerEnterpriseSalesBeginDate` |  |  | Date | — |  |  |  |
| `Firm_CustomerInStorePurchaseReturnsBeginDate` |  |  | Date | — |  |  |  |
| `Firm_CustomerOnlinePurchaseReturnsBeginDate` |  |  | Date | — |  |  |  |
| `Firm_CustomerPOSSalesBeginDate` |  |  | Date | — |  |  |  |
| `Firm_CustomerShiptoStoreSalesBeginDate` |  |  | Date | — |  |  |  |
| `Firm_CustomerSingleSwipeSalesBeginDate` |  |  | Date | — |  |  |  |
| `Firm_DRAnticipatedDeliveryDate` | Anticipated Delivery Date |  | Date | Firm |  | `contract_firm.Firm_DRAnticipatedDeliveryDate · TEXT` |  |
| `Firm_DRTerminationRightDate` | Termination Right Date |  | Date | Firm |  | `contract_firm.Firm_DRTerminationRightDate · TEXT` |  |
| `Firm_DeliveryChargesBeginDate` |  |  | Date | — |  |  |  |
| `Firm_DeliveryDate` |  |  | Date | — |  |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsBeginDate` |  |  | Date | — |  |  |  |
| `Firm_EmployeeSalesBeginDate` |  |  | Date | — |  |  |  |
| `Firm_ExpansionPossessionBeginDate` |  |  | Date | — |  |  |  |
| `Firm_LastDeferredSLEntryDate` | Last Deferred SL Entry Date |  | Date | Firm |  | `contract_firm.Firm_LastDeferredSLEntryDate · TEXT` |  |
| `Firm_LatestCommencementDate` | Latest Commencement Date |  | Date | — |  | `contract_firm.Firm_LatestCommencementDate · TEXT` |  |
| `Firm_LegalReview` |  |  | Date | — |  |  |  |
| `Firm_LegalWorkflow` |  |  | Date | — |  |  |  |
| `Firm_UncollectedCreditBeginDate` |  |  | Date | — |  |  |  |
| `LastLikelyOptionDate` | Likely Term End Date | The last likely option date. The system reviews the list of likely term end dates and returns the one that is the farthest in the future. | Date | Global |  | `contract_admin.LastLikelyOptionDate · TEXT` |  |
| `ObligationDate` | Obligation Date | The obligation date is the date that you would like to report expenses to. This date is typically later than the payment end date. The obligation date is used in the Minimum Lease Obligation report. | Date | Global |  | `contract_financial.ObligationDate · TEXT` |  |
| `OriginalEndDate` | Baseline End Date | The baseline end date of a schedule task on the entity. | Date | — |  | `contract_admin.OriginalEndDate · TEXT` |  |
| `OriginalStartDate` | Baseline Start Date | The baseline start date of a schedule task on the entity. | Date | — |  | `contract_admin.OriginalStartDate · TEXT` |  |
| `PaymentsBeginDate` | Payments Begin Date | Enter the date when payments will begin for this contract. The system will not generate payments outside the payment begin / end dates. In order to have payments outside the payment begin / end date, you will have to extend your contract. | Date | Global |  | `contract_financial.PaymentsBeginDate · TEXT` |  |
| `PaymentsEndDate` | Payments End Date | Enter the date when payments will end for this contract. The system will not generate payments outside the payment begin / end dates. In order to have payments outside the payment begin / end date, you will have to extend your contract. | Date | Global |  | `contract_financial.PaymentsEndDate · TEXT` |  |
| `PossessionBeginDate` | Possession Begin Date | The date when you took possession of the asset. The system will use this date to calculate your accounting begin date. | Date | Global |  | `contract_admin.PossessionBeginDate · TEXT` |  |
| `PossessionEndDate` | Possession End Date | The date when you released possession of the asset. | Date | Global |  | `contract_admin.PossessionEndDate · TEXT` |  |
| `SlotEndDate` | RE Planner Open Date | This field is not implemented for the contract module. | Date | — |  | `contract_admin.SlotEndDate · TEXT` |  |
| `StatusEffectiveDate` | Status Effective Date | This field is an internal-only auditing field. | Date | Global |  | `contract_admin.StatusEffectiveDate · TEXT` |  |

### Flags (13)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AutomaticRenewalInLease` | Automatic Renewal In Lease? | This field is not implemented for contracts or equipment contracts. | Boolean | Global |  | `contract_admin.AutomaticRenewalInLease · TEXT` |  |
| `AutomaticRenewalOption` | Automatic Renewal Option? | This field is not implemented for contracts or equipment contracts. | Boolean | Global |  | `contract_admin.AutomaticRenewalOption · TEXT` |  |
| `BargainRenewalInLease` | Bargain Renewal In Lease? | This field is not implemented for contracts or equipment contracts. | Boolean | Global |  | `contract_financial.BargainRenewalInLease · TEXT` |  |
| `BargainRenewalOption` | Bargain Renewal Option? | This field is not implemented for contracts or equipment contracts. | Boolean | Global |  | `contract_financial.BargainRenewalOption · TEXT` |  |
| `ContainsBargainPurchaseOption` | Contains Bargain Purchase Option? | This check box appears in Test 2 of the Capital Lease Test. Select the check box if the lease contains a purchase option that the tenant is likely to exercise. | Boolean | Global |  | `contract_financial.ContainsBargainPurchaseOption · TEXT` |  |
| `DoesTitleRevertToTenant` | Does Title Revert To Tenant? | This check box appears in Test 1 of the Capital Lease Test. Select the check box if the ownership of the asset reverts to the tenant at the end of the lease term. | Boolean | Global |  | `contract_admin.DoesTitleRevertToTenant · TEXT` |  |
| `InAlternateRent` | In Alternate Rent? | This field returns true if this contract has any alternate rent records which are impacting amounts owed. | Boolean | Global |  | `contract_financial.InAlternateRent · TEXT` |  |
| `Inactive` | Is Inactive? | If selected, this check box indicates the entity is inactive. | Boolean | — | yes | `contract_admin.Inactive · TEXT` |  |
| `IsDead` | Is Dead? | If selected, this check box indicates the entity is dead. | Boolean | — |  | `contract_admin.IsDead · TEXT` |  |
| `IsLowAssetValue` | Is Low Asset Value | Select this check box if the asset is low value. | Boolean | Global |  | `contract_admin.IsLowAssetValue · TEXT` |  |
| `IsShortTerm` | Is Short Term | Select this check box if the contract is short-term. | Boolean | Global |  | `contract_admin.IsShortTerm · TEXT` |  |
| `IsTranslation` | Is Translation | Select this check box if you want to convert currency fields according to the Translation mapping specified on the Admin > Manage Company > Financial Settings page. Do not select this check box if you want to convert currency fields according to the Revaluation mapping specified on the Admin > Manage Company > Financial Settings page. | Boolean | Global |  | `contract_admin.IsTranslation · TEXT` |  |
| `MonthToMonth` | Month To Month? | Select this check box to indicate that your contract is month-to-month. You will also need to mark your expenses as month-to-month. | Boolean | Global |  | `contract_admin.MonthToMonth · TEXT` |  |

### Text & notes (187)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseProvider` | System of Record | This field is used to fetch a record value from another Accruent software. | Text | — |  | `contract_admin.BaseProvider · TEXT` |  |
| `City` |  | This field pulls the city from the contract's associated location record. | Text | — |  | `contract_admin.City · TEXT` |  |
| `CityStateProvinceCountry` | City, State | The city and state / province. If there is no state / province, the field returns only the city. If there is no city, this field returns only the state / province. | Text | — |  | `contract_admin.CityStateProvinceCountry · TEXT` |  |
| `ClientEntityID` | Contract ID | Enter a unique ID for the entity in this field. Remember: when uploading information to a contract using Lx's import spreadsheet functionality, the entity ID and entity name must be replicated exactly in the spreadsheet. | Text | Global |  | `contract_admin.ClientEntityID · TEXT` |  |
| `ComparisonList` | Comparison List | When added to a page layout, this field allows for a comparison of entities from a page or subpage. | Text | — |  | `contract_admin.ComparisonList · TEXT` |  |
| `CompletedPhaseStatus` | Completed Phase Status | The milestone timeline status of the entity. This status is updated when a milestone is completed. | Text | — |  | `contract_admin.CompletedPhaseStatus · TEXT` |  |
| `ConstructionPhaseStatus` | Construction Phase Status | This field is not implemented for contracts or equipment contracts. | Text | — |  | `contract_admin.ConstructionPhaseStatus · TEXT` |  |
| `ContractClass` | Contract Class | This field is used internally to indicate if an entity is a RE Contract, Equipment Contract, Portfolio, or other entity type. | Text | Global |  | `contract_admin.ContractClass · TEXT` |  |
| `ContractName` | Contract Name | This is the name for your contract. Do not enter apostrophes in the Contract Name field. When importing data for a contract, you will need to enter the contract name exactly, including any spaces and punctuation. | Text | Global | yes | `contract_admin.ContractName · TEXT` |  |
| `CountryID` | Country | This field pulls the country code from the contract's associated location record. | Text | — |  | `contract_admin.CountryID · TEXT` |  |
| `CrossStreet1` | Cross Street #1 | This is a generic field. It is not implemented for contracts or equipment contracts by default. | Text | — |  | `contract_admin.CrossStreet1 · TEXT` |  |
| `CrossStreet2` | Cross Street #2 | This is a generic field. It is not implemented for contracts or equipment contracts by default. | Text | — |  | `contract_admin.CrossStreet2 · TEXT` |  |
| `CurrentMilestone` | Current Milestone | The current milestone task of your entity schedule. | Text | — |  | `contract_admin.CurrentMilestone · TEXT` |  |
| `CurrentMonthYear` | Current Month/Year | The current month. | Text | Global |  | `contract_financial.CurrentMonthYear · TEXT` |  |
| `CurrentPhaseStatus` | Project Status | This field is not implemented for contracts or equipment contracts. | Text | — |  | `contract_admin.CurrentPhaseStatus · TEXT` |  |
| `DesignPhaseStatus` | Design Phase Status | This field is not implemented for contracts or equipment contracts. | Text | — |  | `contract_admin.DesignPhaseStatus · TEXT` |  |
| `EntityEmail` | Entity Email | The entity's email address that is created when the Email into Lx functionality is enabled. | Text | — |  | `contract_admin.EntityEmail · TEXT` |  |
| `EntityPhoto` | Entity Photo | This is a generic field. When you add this field to a page layout, you can use it to add a photo to the layout. | Text | — |  | `contract_admin.EntityPhoto · TEXT` |  |
| `ExpAccrualForecastTable` | Expense Accrual Forecast Table | This field displays the Accrual Forecast Grid. | Text | Global |  | `contract_financial.ExpAccrualForecastTable · TEXT` |  |
| `ExpenseForecastTable` | Expense Forecast Table | This field displays the Expense Forecast Grid. | Text | Global |  | `contract_financial.ExpenseForecastTable · TEXT` |  |
| `FMVSource` | FMV Source | This field is included in Test 4 of the Capital Lease Test. Enter the name of the person who assessed the fair value of the asset. | Text | Global |  | `contract_financial.FMVSource · TEXT` |  |
| `FacilityName` | Facility Name | The name of the facility associated with this entity. | Text | — |  | `contract_admin.FacilityName · TEXT` |  |
| `FinalResult` | Final Result | The final result of the ASC 842 test. | Text | Global |  | `contract_financial.FinalResult · TEXT` |  |
| `FinancialModel` | Financial Model | When added to a page layout, this field appears as a button that generates an Excel Financial Model spreadsheet. If you have questions about this functionality, contact your Accruent representative. | Text | — |  | `contract_admin.FinancialModel · TEXT` |  |
| `FirmID` | Firm ID | The record's Firm ID. | Text | — | yes | `contract_admin.FirmID · TEXT` |  |
| `Firm_BankChargesDocument` |  |  | Text | — |  |  |  |
| `Firm_BankChargesNotes` |  |  | Text | — |  |  |  |
| `Firm_BankChargesPage` |  |  | Text | — |  |  |  |
| `Firm_BankChargesSection` |  |  | Text | — |  |  |  |
| `Firm_CAMAdministrativeFeeDefinition` | Administrative Fee Definition |  | Text | Firm |  | `contract_firm.Firm_CAMAdministrativeFeeDefinition · TEXT` |  |
| `Firm_CAMAuditRightsReference` | Audit Rights Reference |  | Text | Firm |  | `contract_firm.Firm_CAMAuditRightsReference · TEXT` |  |
| `Firm_CAMComment` | Comment |  | Text | Firm |  | `contract_firm.Firm_CAMComment · TEXT` |  |
| `Firm_CAMContributionsReference` | Contributions Reference |  | Text | Firm |  | `contract_firm.Firm_CAMContributionsReference · TEXT` |  |
| `Firm_CAMDocument` | Document |  | Text | Firm |  | `contract_firm.Firm_CAMDocument · TEXT` |  |
| `Firm_CAMExclusionsReference` | Exclusions Reference |  | Text | Firm |  | `contract_firm.Firm_CAMExclusionsReference · TEXT` |  |
| `Firm_CAMFixedComment` | Fixed CAM Increase Comment |  | Text | Firm |  | `contract_firm.Firm_CAMFixedComment · TEXT` |  |
| `Firm_CAMFixedText` | Fixed CAM Text |  | Text | Firm |  | `contract_firm.Firm_CAMFixedText · TEXT` |  |
| `Firm_CAMLeaseTermCapComment` | Lease Term Cap Comment |  | Text | Firm |  | `contract_firm.Firm_CAMLeaseTermCapComment · TEXT` |  |
| `Firm_CAMLeaseTermCapTextReference` | Lease Term Cap Text Reference |  | Text | Firm |  | `contract_firm.Firm_CAMLeaseTermCapTextReference · TEXT` |  |
| `Firm_CAMNoDuplicationofCostsReference` | No Duplication of Costs Reference |  | Text | Firm |  | `contract_firm.Firm_CAMNoDuplicationofCostsReference · TEXT` |  |
| `Firm_CAMNotes` | Notes |  | Text | Firm |  | `contract_firm.Firm_CAMNotes · TEXT` |  |
| `Firm_CAMPRShare` | PR Share |  | Text | Firm |  | `contract_firm.Firm_CAMPRShare · TEXT` |  |
| `Firm_CAMPage` | Page |  | Text | Firm |  | `contract_firm.Firm_CAMPage · TEXT` |  |
| `Firm_CAMSection` | Section |  | Text | Firm |  | `contract_firm.Firm_CAMSection · TEXT` |  |
| `Firm_CAMStartingCapComment` | Starting Cap Comment |  | Text | Firm |  | `contract_firm.Firm_CAMStartingCapComment · TEXT` |  |
| `Firm_CAMStartingCapTextReference` | Starting Cap Text Reference |  | Text | Firm |  | `contract_firm.Firm_CAMStartingCapTextReference · TEXT` |  |
| `Firm_CAMStatementsBindingLanguageReference` | Statements Binding Language Reference |  | Text | Firm |  | `contract_firm.Firm_CAMStatementsBindingLanguageReference · TEXT` |  |
| `Firm_CAMStatementsDue` | Statements Due |  | Text | Firm |  | `contract_firm.Firm_CAMStatementsDue · TEXT` |  |
| `Firm_CAMStatementsDueReference` | Statements Due Reference |  | Text | Firm |  | `contract_firm.Firm_CAMStatementsDueReference · TEXT` |  |
| `Firm_CreditCardFeesDocument` |  |  | Text | — |  |  |  |
| `Firm_CreditCardFeesNotes` |  |  | Text | — |  |  |  |
| `Firm_CreditCardFeesPage` |  |  | Text | — |  |  |  |
| `Firm_CreditCardFeesSection` |  |  | Text | — |  |  |  |
| `Firm_CustomerEnterpriseSalesDocument` |  |  | Text | — |  |  |  |
| `Firm_CustomerEnterpriseSalesNotes` |  |  | Text | — |  |  |  |
| `Firm_CustomerEnterpriseSalesPage` |  |  | Text | — |  |  |  |
| `Firm_CustomerEnterpriseSalesSection` |  |  | Text | — |  |  |  |
| `Firm_CustomerInStorePurchaseReturnsDocument` |  |  | Text | — |  |  |  |
| `Firm_CustomerInStorePurchaseReturnsNotes` |  |  | Text | — |  |  |  |
| `Firm_CustomerInStorePurchaseReturnsPage` |  |  | Text | — |  |  |  |
| `Firm_CustomerInStorePurchaseReturnsSection` |  |  | Text | — |  |  |  |
| `Firm_CustomerOnlinePurchaseReturnsDocument` |  |  | Text | — |  |  |  |
| `Firm_CustomerOnlinePurchaseReturnsNotes` |  |  | Text | — |  |  |  |
| `Firm_CustomerOnlinePurchaseReturnsPage` |  |  | Text | — |  |  |  |
| `Firm_CustomerOnlinePurchaseReturnsSection` |  |  | Text | — |  |  |  |
| `Firm_CustomerPOSSalesDocument` |  |  | Text | — |  |  |  |
| `Firm_CustomerPOSSalesNotes` |  |  | Text | — |  |  |  |
| `Firm_CustomerPOSSalesPage` |  |  | Text | — |  |  |  |
| `Firm_CustomerPOSSalesSection` |  |  | Text | — |  |  |  |
| `Firm_CustomerShiptoStoreSalesDocument` |  |  | Text | — |  |  |  |
| `Firm_CustomerShiptoStoreSalesNotes` |  |  | Text | — |  |  |  |
| `Firm_CustomerShiptoStoreSalesPage` |  |  | Text | — |  |  |  |
| `Firm_CustomerShiptoStoreSalesSection` |  |  | Text | — |  |  |  |
| `Firm_CustomerSingleSwipeSalesDocument` |  |  | Text | — |  |  |  |
| `Firm_CustomerSingleSwipeSalesNotes` |  |  | Text | — |  |  |  |
| `Firm_CustomerSingleSwipeSalesPage` |  |  | Text | — |  |  |  |
| `Firm_CustomerSingleSwipeSalesSection` |  |  | Text | — |  |  |  |
| `Firm_DRDocument` | Document |  | Text | Firm |  | `contract_firm.Firm_DRDocument · TEXT` |  |
| `Firm_DRNotes` | Notes |  | Text | Firm |  | `contract_firm.Firm_DRNotes · TEXT` |  |
| `Firm_DRPage` | Page |  | Text | Firm |  | `contract_firm.Firm_DRPage · TEXT` |  |
| `Firm_DRSection` | Section |  | Text | Firm |  | `contract_firm.Firm_DRSection · TEXT` |  |
| `Firm_DeliveryChargesDocument` |  |  | Text | — |  |  |  |
| `Firm_DeliveryChargesNotes` |  |  | Text | — |  |  |  |
| `Firm_DeliveryChargesPage` |  |  | Text | — |  |  |  |
| `Firm_DeliveryChargesSection` |  |  | Text | — |  |  |  |
| `Firm_DeveloperLeaseID` | Developer Lease ID |  | Text | Firm |  | `contract_firm.Firm_DeveloperLeaseID · TEXT` |  |
| `Firm_EmployeeOnlinePurchaseReturnsDocument` |  |  | Text | — |  |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsNotes` |  |  | Text | — |  |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsPage` |  |  | Text | — |  |  |  |
| `Firm_EmployeeOnlinePurchaseReturnsSection` |  |  | Text | — |  |  |  |
| `Firm_EmployeeSalesDocument` |  |  | Text | — |  |  |  |
| `Firm_EmployeeSalesNotes` |  |  | Text | — |  |  |  |
| `Firm_EmployeeSalesPage` |  |  | Text | — |  |  |  |
| `Firm_EmployeeSalesSection` |  |  | Text | — |  |  |  |
| `Firm_GISLink` | GIS Link |  | Text | Firm |  | `contract_firm.Firm_GISLink · TEXT` |  |
| `Firm_GISWebsite` | GIS Website |  | Text | Firm |  | `contract_firm.Firm_GISWebsite · TEXT` |  |
| `Firm_LandlordLegalName` | Landlord Legal Name |  | Text | Firm |  | `contract_firm.Firm_LandlordLegalName · TEXT` |  |
| `Firm_LeaseExpirationReference` | Lease Expiration Reference |  | Text | Firm |  | `contract_firm.Firm_LeaseExpirationReference · TEXT` |  |
| `Firm_LeaseStatusNotes` | Lease Status Notes |  | Text | Firm |  | `contract_firm.Firm_LeaseStatusNotes · TEXT` |  |
| `Firm_LeaseYearReference` | Lease Year Reference |  | Text | Firm |  | `contract_firm.Firm_LeaseYearReference · TEXT` |  |
| `Firm_LegalNotes` |  |  | Text | — |  |  |  |
| `Firm_ONCOTAlternativeRentTerms` | Alternative Rent Terms |  | Text | Firm |  | `contract_firm.Firm_ONCOTAlternativeRentTerms · TEXT` |  |
| `Firm_ONCOTDocument` | Document |  | Text | Firm |  | `contract_firm.Firm_ONCOTDocument · TEXT` |  |
| `Firm_ONCOTLimitPerYear` | Limit Per Year |  | Text | Firm |  | `contract_firm.Firm_ONCOTLimitPerYear · TEXT` |  |
| `Firm_ONCOTNotes` | Notes |  | Text | Firm |  | `contract_firm.Firm_ONCOTNotes · TEXT` |  |
| `Firm_ONCOTPage` | Page |  | Text | Firm |  | `contract_firm.Firm_ONCOTPage · TEXT` |  |
| `Firm_ONCOTRequiredNumberofAnchors` | Required Number of Anchors |  | Text | Firm |  | `contract_firm.Firm_ONCOTRequiredNumberofAnchors · TEXT` |  |
| `Firm_ONCOTSection` | Section |  | Text | Firm |  | `contract_firm.Firm_ONCOTSection · TEXT` |  |
| `Firm_OPCOTAlternativeRentTerms` | Alternative Rent Terms |  | Text | Firm |  | `contract_firm.Firm_OPCOTAlternativeRentTerms · TEXT` |  |
| `Firm_OPCOTDocument` | Document |  | Text | Firm |  | `contract_firm.Firm_OPCOTDocument · TEXT` |  |
| `Firm_OPCOTNotes` | Notes |  | Text | Firm |  | `contract_firm.Firm_OPCOTNotes · TEXT` |  |
| `Firm_OPCOTPage` | Page |  | Text | Firm |  | `contract_firm.Firm_OPCOTPage · TEXT` |  |
| `Firm_OPCOTRequiredNumberofAnchors` | Required Number of Anchors |  | Text | Firm |  | `contract_firm.Firm_OPCOTRequiredNumberofAnchors · TEXT` |  |
| `Firm_OPCOTSection` | Section |  | Text | Firm |  | `contract_firm.Firm_OPCOTSection · TEXT` |  |
| `Firm_PCRNumber` | PCR Number |  | Text | — |  | `contract_firm.Firm_PCRNumber · TEXT` |  |
| `Firm_RETAdministrativeFeeReference` | Administrative Fee Reference |  | Text | Firm |  | `contract_firm.Firm_RETAdministrativeFeeReference · TEXT` |  |
| `Firm_RETAuditRightsReference` | Audit Rights Reference |  | Text | Firm |  | `contract_firm.Firm_RETAuditRightsReference · TEXT` |  |
| `Firm_RETComment` | Comment |  | Text | Firm |  | `contract_firm.Firm_RETComment · TEXT` |  |
| `Firm_RETConsultingFeeReference` | Consulting Fee Reference |  | Text | Firm |  | `contract_firm.Firm_RETConsultingFeeReference · TEXT` |  |
| `Firm_RETContributionsReferences` | Contributions Reference |  | Text | Firm |  | `contract_firm.Firm_RETContributionsReferences · TEXT` |  |
| `Firm_RETDocument` | Document |  | Text | Firm |  | `contract_firm.Firm_RETDocument · TEXT` |  |
| `Firm_RETInitialEstimateReference` | Initial Estimate Reference |  | Text | Firm |  | `contract_firm.Firm_RETInitialEstimateReference · TEXT` |  |
| `Firm_RETLeaseTermCapComment` | Lease Term Cap Comment |  | Text | Firm |  | `contract_firm.Firm_RETLeaseTermCapComment · TEXT` |  |
| `Firm_RETLeaseTermCapTextReference` | Lease Term Cap Text Reference |  | Text | Firm |  | `contract_firm.Firm_RETLeaseTermCapTextReference · TEXT` |  |
| `Firm_RETNotes` | Notes |  | Text | Firm |  | `contract_firm.Firm_RETNotes · TEXT` |  |
| `Firm_RETPRShare` | PR Share |  | Text | Firm |  | `contract_firm.Firm_RETPRShare · TEXT` |  |
| `Firm_RETPage` | Page |  | Text | Firm |  | `contract_firm.Firm_RETPage · TEXT` |  |
| `Firm_RETSection` | Section |  | Text | Firm |  | `contract_firm.Firm_RETSection · TEXT` |  |
| `Firm_RETStartingCapTextReference` | Starting Cap Text Reference |  | Text | Firm |  | `contract_firm.Firm_RETStartingCapTextReference · TEXT` |  |
| `Firm_RETStatementsBindingReference` | Statements Binding Reference |  | Text | Firm |  | `contract_firm.Firm_RETStatementsBindingReference · TEXT` |  |
| `Firm_RETStatementsDue` | Statements Due |  | Text | Firm |  | `contract_firm.Firm_RETStatementsDue · TEXT` |  |
| `Firm_RETStatementsDueReference` | Statements Due Reference |  | Text | Firm |  | `contract_firm.Firm_RETStatementsDueReference · TEXT` |  |
| `Firm_RETTaxesFor` | Taxes For? |  | Text | Firm |  | `contract_firm.Firm_RETTaxesFor · TEXT` |  |
| `Firm_RentCommencementNotes` | Rent Commencement Notes |  | Text | Firm |  | `contract_firm.Firm_RentCommencementNotes · TEXT` |  |
| `Firm_SalesReportLogo` | Sales Report Logo |  | Text | — |  | `contract_firm.Firm_SalesReportLogo · TEXT` |  |
| `Firm_SalesReportLogoMadewell` |  |  | Text | — |  |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature |  | Text | — |  | `contract_firm.Firm_SalesReportSignature · TEXT` |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name |  | Text | — |  | `contract_firm.Firm_SalesReportSignatureName · TEXT` |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title |  | Text | — |  | `contract_firm.Firm_SalesReportSignatureTitle · TEXT` |  |
| `Firm_TaxLink1` | Tax Link 1 |  | Text | Firm |  | `contract_firm.Firm_TaxLink1 · TEXT` |  |
| `Firm_TaxLink2` | Tax Link 2 |  | Text | Firm |  | `contract_firm.Firm_TaxLink2 · TEXT` |  |
| `Firm_TaxWebsite1` | Tax Website 1 |  | Text | Firm |  | `contract_firm.Firm_TaxWebsite1 · TEXT` |  |
| `Firm_TaxWebsite2` | Tax Website 2 |  | Text | Firm |  | `contract_firm.Firm_TaxWebsite2 · TEXT` |  |
| `Firm_UncollectedCreditDocument` |  |  | Text | — |  |  |  |
| `Firm_UncollectedCreditNotes` |  |  | Text | — |  |  |  |
| `Firm_UncollectedCreditPage` |  |  | Text | — |  |  |  |
| `Firm_UncollectedCreditSection` |  |  | Text | — |  |  |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | — |  | `contract_admin.HTMLAddress · TEXT` |  |
| `IssuesAndAlerts` | Issues And Alerts | This field can be added to page layouts. In View mode, this field will display a table with form and workflow data, such as the work flow / form type, critical issue count, non-critical issue count, escalated count, and past due notification count. | Text | — |  | `contract_admin.IssuesAndAlerts · TEXT` |  |
| `LatestFinancialTestFinalResult` | Latest Financial Test Result | The final result of the most recently locked ASC 842 test. | Text | Global |  | `contract_financial.LatestFinancialTestFinalResult · TEXT` |  |
| `MapClientRecordID` | Client Unique ID | The entity Map Client Record ID. | Text | — |  | `contract_admin.MapClientRecordID · TEXT` |  |
| `MilestoneTimeline` | Milestone Timeline | This field generates a list of all milestones, but hides those with no values. | Text | — |  | `contract_admin.MilestoneTimeline · TEXT` |  |
| `NextAvailableTermKeyDateID` | Next Available Term Key Date Info | The next available term's key date record ID for a given contract. The system will only return contract terms where the term status is LIKELY or AVAILABLE, the notice end date has been set, and the notice end date is greater than or equal to today's date. | Text | Global |  | `contract_admin.NextAvailableTermKeyDateID · TEXT` |  |
| `NextMilestone` | Next Milestone | The upcoming milestone in the milestone timeline. | Text | — |  | `contract_admin.NextMilestone · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `contract_admin.Notes · TEXT` |  |
| `OperationsPhaseStatus` | Operations Phase Status | This field is not implemented for the contract module. | Text | — |  | `contract_admin.OperationsPhaseStatus · TEXT` |  |
| `OptionDescription` | Option Description | Write a description of the record. | Text | Global |  | `contract_admin.OptionDescription · TEXT` |  |
| `Phone` |  | If there is a facility, The facility's phone number. Otherwise, The location's phone number. | Text | — |  | `contract_admin.Phone · TEXT` |  |
| `PossessionPhaseStatus` | Possession Phase Status | This field is not implemented for the contract module. | Text | — |  | `contract_admin.PossessionPhaseStatus · TEXT` |  |
| `PostalCode` | Postal Code | This field pulls the postal code from the contract's associated location record. | Text | — |  | `contract_admin.PostalCode · TEXT` |  |
| `PotentialProjectName` | Site Name | This field is not implemented for the contract module. | Text | — |  | `contract_admin.PotentialProjectName · TEXT` |  |
| `PreviousMilestone` | Previous Milestone | The previous milestone task. | Text | — |  | `contract_admin.PreviousMilestone · TEXT` |  |
| `ProgramName` | Portfolio/Program Name | The name of the portfolio associated with this entity. | Text | — |  | `contract_admin.ProgramName · TEXT` |  |
| `ProjectDescription` | Description | Write a description of the record. | Text | Global |  | `contract_admin.ProjectDescription · TEXT` |  |
| `ProjectEntityName` | Name | The entity name. | Text | — | yes | `contract_admin.ProjectEntityName · TEXT` |  |
| `ProjectEntityTypeName` | Entity Type | There are two values for this field: "RE Contract" or "Equipment Contract". | Text | — |  | `contract_admin.ProjectEntityTypeName · TEXT` |  |
| `ProjectName` | Project Name | The name of the project associated with the record. | Text | — |  | `contract_admin.ProjectName · TEXT` |  |
| `PrototypeName` | Prototype Name | The name of the prototype associated with this entity. | Text | — |  | `contract_admin.PrototypeName · TEXT` |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | This field is not implemented for the contract module. | Text | — |  | `contract_admin.RealEstatePhaseStatus · TEXT` |  |
| `RelatedEntities` | Related Entities | The facility name associated with the contract. | Text | — |  | `contract_admin.RelatedEntities · TEXT` |  |
| `RelocatedFrom` |  | This field is not implemented for the contract module. | Text | — |  | `contract_admin.RelocatedFrom · TEXT` |  |
| `RunReportAction` | Run Report Action | This is a generic field. When you add this field to a page layout, it will run a report. See the Run Report Action Buttons article in the Online Help to learn more. | Text | — |  | `contract_admin.RunReportAction · TEXT` |  |
| `ScLocationID` | Service Channel Location ID |  | Text | Global |  | `contract_admin.ScLocationID · TEXT` |  |
| `StreetAddress` | Street Address | This field pulls the street address from the contract's associated location record. | Text | — |  | `contract_admin.StreetAddress · TEXT` |  |
| `StreetAddress1` | Street Address #1 | This field pulls the first line of the street address from the contract's associated location record. | Text | — |  | `contract_admin.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | This field pulls the second line of the street address from the contract's associated location record. | Text | — |  | `contract_admin.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | This field pulls the third line of the street address from the contract's associated location record. | Text | — |  | `contract_admin.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | This field pulls the fourth line of the street address from the contract's associated location record. | Text | — |  | `contract_admin.StreetAddress4 · TEXT` |  |
| `Test1Result` | Test #1 Result | This field contains result 1 of the Capital Lease test for the contract. | Text | Global |  | `contract_financial.Test1Result · TEXT` |  |
| `Test2Result` | Test #2 Result | This field contains result 2 of the Capital Lease test for the contract. | Text | Global |  | `contract_financial.Test2Result · TEXT` |  |
| `Test3Result` | Test #3 Result | This field contains result 3 of the Capital Lease test for the contract. | Text | Global |  | `contract_financial.Test3Result · TEXT` |  |
| `Test4Result` | Test #4 Result | This field contains result 4 of the Capital Lease test for the contract. | Text | Global |  | `contract_financial.Test4Result · TEXT` |  |
| `Test5aResult` | Test #5a Result | This field contains result 5 of the Capital Lease test for the contract. | Text | Global |  | `contract_financial.Test5aResult · TEXT` |  |
| `Test5bResult` | Test #5b Result | This field contains result 6 of the Capital Lease test for the contract. | Text | Global |  | `contract_financial.Test5bResult · TEXT` |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | This is a default field that is not used for contracts or equipment contracts. | Text | — |  | `contract_admin.ThirdPartyWarehouse · TEXT` |  |
| `TimeZone` | Time Zone | Select the appropriate time zone from this field. | Text | Global |  | `contract_admin.TimeZone · TEXT` |  |
| `TradeArea` | Trade Area | The trade area from the contract's location. | Text | — |  | `contract_admin.TradeArea · TEXT` |  |

### Audit & record keeping (9)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Contract ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `contract_admin.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | — |  | `contract_admin.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | — |  | `contract_admin.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `contract_admin.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `contract_firm.ModifiedDate · TEXT` |  |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `contract_firm.ModifiedDate · TEXT` |  |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `contract_firm.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | — |  | `contract_admin.RevNumber · TEXT` |  |
| `UUID` | Contract UUID | This field captures a unique identifier associated with your record. This identifier is used if you are using an integration with other Accruent products. | Text | Global |  | `contract_admin.UUID · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossArea` | Gross Acreage | This is a default field that is not used for contracts or equipment contracts. | Acreage | — |  | `contract_admin.GrossArea · TEXT` |  |

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
