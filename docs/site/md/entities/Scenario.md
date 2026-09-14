# Scenario

*69 fields · module: Portfolio & Real-Estate Transactions · Postgres: `scenario`*

A deal/transaction scenario under RE Transaction — comparative what-if terms (Broker Commission, Capital Required, Annual Total Rent) for a prospective site or renewal being evaluated before commitment, plus site demographic fields (Average HH Income, Block) inherited from the site-selection process. 70 Global fields; Scenario sits upstream of Contract in the deal lifecycle, modeling terms under negotiation rather than terms in force.

Source: `data-fields/scenario.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 69 |
| Fields with a vendor definition | 66 of 69 inventoried |
| Physical tables | `scenario` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 70 (70 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 5 keys from 3 record types |
| Points at | 10 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 7 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in scenario

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 66 fields carry a vendor definition

**Observed.** 66 of this record's 69 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 69 comparable

**Observed.** Over the 69 fields both captures contain, they agree on 68. The exceptions are ProjectEntityID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [POR-R-004](../rules/POR-R-004.md) | A `Scenario` reaches `Contract` · `Scenario.ContractID` · One-way, optional link. `Contract` carries no reciprocal `ScenarioID`/`RETransactionID` column — a signed lease cannot be traced back to the deal that produced it via FK. | Observed |
| [POR-R-005](../rules/POR-R-005.md) | A `PotentialProject`, `Program`, `Scenario`, or `RETransaction` needs a deal classification · `PotentialProject.CodeDealTypeID` / `Program.CodeDealTypeID` → `Deal Type Code` (2024); `Scenario.CodeScenarioDealTypeID` / `RETransaction.Preferr | Observed |
| [POR-R-008](../rules/POR-R-008.md) | A user compares competing sites or scenarios · `ComparisonReport` → `ComparisonItem` · `ComparisonItem.ComputedValue`/`ExpenseGroup` hold computed comparison output; `ScenarioName`/`ScenarioDate` are plain text, not FKs — a comparison item  | Observed |
| [POR-R-014](../rules/POR-R-014.md) | `Scenario` is created · `Scenario.RETransactionID`, `Scenario.ProjectEntityID`, `Scenario.ScenarioDealType` · All three required. `Scenario.ScenarioType` is optional. | Observed |
| [POR-R-015](../rules/POR-R-015.md) | A `Scenario`'s deal type needs comparing against its parent transaction's preference · `Scenario.CodeScenarioDealTypeID` vs. `RETransaction.PreferredScenarioCodeDealTypeID` · Both draw from the same code table (`Scenario Deal Type Code`, 20 | Derived |
| [POR-R-016](../rules/POR-R-016.md) | `Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read · `Task/Group ID` FK type · The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, | Derived |
| [PRJ-R-013](../rules/PRJ-R-013.md) | A real-estate deal step needs its own schedule · `RETransaction.DealSchedule`/`ActiveDealStepTaskIDList`, `Scenario.DealSchedule`/`ActiveDealStepTaskIDList` (`portfolio-transactions`) · Both reuse `TaskGroup` directly — the deal pipeline ha | Observed |

## Fields

### Relationships (foreign keys) (8)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActiveDealStepTaskIDList` | Active Deal Step(s) |  | Task/Group ID | Global |  | `scenario.ActiveDealStepTaskIDList · TEXT` | [TaskGroup](TaskGroup.md) |
| `AmendmentID` | Amendment | This field has not been implemented for this functionality. | Contract Amendment ID | Global |  | `scenario.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID associated with the scenario. The Contract ID is a unique identifier that belongs to a contract. | Contract ID | Global |  | `scenario.ContractID · TEXT` | [Contract](Contract.md) |
| `ContractTermID` | Contract Term | The associated contract covenant record ID. | Contract Term ID | Global |  | `scenario.ContractTermID · TEXT` | [ContractTerm](ContractTerm.md) |
| `CovenantID` | Covenant | The associated contract term record ID. | Covenant ID | Global |  | `scenario.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `DealSchedule` | Deal Schedule |  | Task/Group ID | Global |  | `scenario.DealSchedule · TEXT` | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` | Related Entity | The ProjectEntityID is the Base Entity System Identifier for associated tasks, folders, documents, forms, and other records. It is assigned automatically by the system, and is not editable. | Entity ID | Global | yes | `scenario.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `RETransactionID` | RE Transaction | The system-assigned identifier for the transaction record linked to this scenario. | RE Transaction ID | Global | yes | `scenario.RETransactionID · TEXT` | [RETransaction](RETransaction.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentIDList` | Documents | This is a generic field that allows you to add documents to the scenario from the Documents page. This field also allows you to upload new documents to the entity and attach them to the scenario. | Document List | Global |  | `scenario.DocumentIDList · TEXT` |  |

### Coded values (drop-downs) (13)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. | Dropdown (Building Area Unit Code) | Global |  | `scenario.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCovenantCategoryID` | Covenant Category | The covenant category is the third level of categorization for covenants. Categories are the children of types, and the grandchildren of groups. The category is typically used to indicate whether this is part of the original agreement or an amendment. | Dropdown (Covenant Category Code) | Global |  | `scenario.CodeCovenantCategoryID · TEXT` | Covenant Category Code |
| `CodeCovenantGroupID` | Covenant Group | The covenant group is the first level of categorization for covenants. Groups are the parents of types, and the grandparents of categories. | Dropdown (Covenant Group Code) | Global |  | `scenario.CodeCovenantGroupID · TEXT` | Covenant Group Code |
| `CodeCovenantStatusID` | Covenant Status | The status of the covenant. Example statuses include "Active" or "Expired". | Dropdown (Covenant Status Code) | Global |  | `scenario.CodeCovenantStatusID · TEXT` | Covenant Status Code |
| `CodeCovenantTypeID` | Covenant Type | The covenant type is the second level of categorization for covenants. Types are the children of groups, and the parents of categories. | Dropdown (Covenant Type Code) | Global |  | `scenario.CodeCovenantTypeID · TEXT` | Covenant Type Code |
| `CodeCurrencyTypeID` | Currency | Select the currency type to be used on the scenario record. | Dropdown (Currency Type Code) | Global |  | `scenario.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeDecisionStatusID` | Decision Status | Select the current phase of evaluation or selection for this scenario. | Dropdown (Decision Status Code) | Global |  | `scenario.CodeDecisionStatusID · TEXT` | Decision Status Code |
| `CodeMarketAreaID` | Market | The market the scenario belongs to. The values that appear in this field depend on the org chart of the portfolio you selected. | Dropdown (Market Area Code) | Global |  | `scenario.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodePropertyTypeID` | Property Type | Select the type of property from the list. | Dropdown (Property Type Code) | Global |  | `scenario.CodePropertyTypeID · TEXT` | Property Type Code |
| `CodeScenarioDealTypeID` | Scenario Deal Type | Select which kind of deal this scenario represents. | Dropdown (Scenario Deal Type Code) | Global | yes | `scenario.CodeScenarioDealTypeID · TEXT` | Scenario Deal Type Code |
| `CodeScenarioTypeID` | Scenario Type | Select which kind of scenario this scenario represents. Example scenario types include renewal, relocation, and disposition. | Dropdown (Scenario Type Code) | Global |  | `scenario.CodeScenarioTypeID · TEXT` | Scenario Type Code |
| `CodeTermStatusID` | Term Status | The status of the linked contract term. | Dropdown (Term Status Code) | Global |  | `scenario.CodeTermStatusID · TEXT` | Term Status Code |
| `CodeTermTypeID` | Term Type | The type of the linked contract term. | Dropdown (Term Type Code) | Global |  | `scenario.CodeTermTypeID · TEXT` | Term Type Code |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AnnualTotalRent` | Annual Total Rent | Enter the annual total rent for this scenario. | Currency | Global |  | `scenario.AnnualTotalRent · TEXT` |  |
| `AverageHHIncome` | Average HH Income | Enter the average household income for the market area in this field. | Currency | Global |  | `scenario.AverageHHIncome · TEXT` |  |
| `CapitalRequired` | Capital Required | On a lease, enter the cost of improvements that are not covered by the tenant improvement allowance. On a purchase, enter the deposit or equity amount contributed by the buyer, or the cash the buyer brings to closing. | Currency | Global |  | `scenario.CapitalRequired · TEXT` |  |
| `Deposit` |  | Enter the cash put down for the scenario while it is under consideration. | Currency | Global |  | `scenario.Deposit · TEXT` |  |
| `MedianHHIncome` | Median HH Income | Enter the median household income for the market area in this field. | Currency | Global |  | `scenario.MedianHHIncome · TEXT` |  |
| `OperatingCostsCAM` | Operating Costs CAM | Enter the operating costs, common area maintenance costs (CAM), or a combination of the two. | Currency | Global |  | `scenario.OperatingCostsCAM · TEXT` |  |
| `TIAllowance` | TI Allowance | Enter the amount allowed by the landlord for improvements to the leased premises. | Currency | Global |  | `scenario.TIAllowance · TEXT` |  |
| `TiPerAreaUnit` | TI Per Area Unit | Enter the tenant improvement allowance (TIA) divided by the rentable area. | Currency | Global |  | `scenario.TiPerAreaUnit · TEXT` |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BrokerCommission` | Broker Commission | Enter the commission to be paid to the broker upon completion of the scenario. | Percentage | Global |  | `scenario.BrokerCommission · TEXT` |  |
| `DiscountRate` | Discount Rate | Enter the discount rate for this scenario. | Percentage | Global |  | `scenario.DiscountRate · TEXT` |  |
| `Population5yrGrowth` | Population 5yr Growth | Enter the 5-year population growth for the market area. | Percentage | Global |  | `scenario.Population5yrGrowth · TEXT` |  |
| `ProRataShareRate` | Pro Rata Share Rate | Enter the pro rata share for the expense in this field. Pro Rata Share refers to a proportionate share of an expense. For example, many contracts for tenants of indoor malls stipulate that each tenant pay a pre-determined percentage of common area maintenance (CAM) expenses. | Percentage | Global |  | `scenario.ProRataShareRate · TEXT` |  |

### Quantities (10)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdditionalTerms` | Additional Terms | Enter the number of contract term options in addition to this scenario. | Number | Global |  | `scenario.AdditionalTerms · TEXT` |  |
| `CloseDays` | Close Days | The number of days to close on a sale. | Number | Global |  | `scenario.CloseDays · TEXT` |  |
| `DueDiligenceDays` | Due Diligence Days | The number of days you have to investigate the option to determine its viability. | Number | Global |  | `scenario.DueDiligenceDays · TEXT` |  |
| `NewTermLength` | New Term Length | This field calculates the total years, months, and days in the proposed new term. | Number | Global |  | `scenario.NewTermLength · TEXT` |  |
| `ParkingRatio` | Parking Ratio | The number of parking spaces per 1,000 area units of rentable area. | 5-Digit Number | Global |  | `scenario.ParkingRatio · TEXT` |  |
| `ParkingSpaces` | Parking Spaces | Enter the number of parking spaces in this field. | Number | Global |  | `scenario.ParkingSpaces · TEXT` |  |
| `ProposedTermLength` | Proposed Term Length | Enter the proposed term length for the new lease in months. | Number | Global |  | `scenario.ProposedTermLength · TEXT` |  |
| `RentableArea` | Rentable Area | Enter the rentable area in this field. | Number | Global |  | `scenario.RentableArea · TEXT` |  |
| `ScenarioID` | Scenario RecID | The unique system-generated identifier assigned to this scenario. | Number | Global |  | `scenario.ScenarioID · VARCHAR(64) NOT NULL` |  |
| `TotalPopulation` | Total Population | Enter the total population of the market area. | Number | Global |  | `scenario.TotalPopulation · TEXT` |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DecisionDate` | Decision Date | Enter the date that the decision status is moved to selected or not selected. | Date | Global |  | `scenario.DecisionDate · TEXT` |  |
| `EndDate` | End Date | This field has not been implemented for this functionality. | Date | Global |  | `scenario.EndDate · TEXT` |  |
| `NewTermEndDate` | New Term End Date | Enter the new term end date in this field. | Date | Global |  | `scenario.NewTermEndDate · TEXT` |  |
| `NewTermStartDate` | New Term Start Date | Enter the new term start date in this field. | Date | Global |  | `scenario.NewTermStartDate · TEXT` |  |
| `NoticeBeginDate` | Notice Begin Date | The notice begin date of the linked term or covenant. | Date | Global |  | `scenario.NoticeBeginDate · TEXT` |  |
| `NoticeEndDate` | Notice End Date | The notice end date of the linked term or covenant. The system will automatically calculate the value in the Notice End Date field using this formula: Notice End Date = Notice Begin Date - Notice Period. A Lease Notification Alert will be sent out on a nightly basis during the Notice Period until the key date is acted upon. | Date | Global |  | `scenario.NoticeEndDate · TEXT` |  |
| `OriginalLeaseStartDate` | Original Lease Start Date | Enter the start date of the original lease in this field. | Date | Global |  | `scenario.OriginalLeaseStartDate · TEXT` |  |
| `ProposedCommencementDate` | Proposed Commencement Date | Enter the proposed date for when the first term of the new lease will start. | Date | Global |  | `scenario.ProposedCommencementDate · TEXT` |  |

### Text & notes (11)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Block` |  | If the parcel has a block identifier this is commonly for parcels in urban areas enter the block identifier in this field. | Text | Global |  | `scenario.Block · TEXT` |  |
| `ClientNumber` | Term Client Number | The term number of the contract term associated with this scenario. | Text | Global |  | `scenario.ClientNumber · TEXT` |  |
| `DealStepSchedule` | Deal Steps | The deal step schedule for the transaction. | Text | Global |  | `scenario.DealStepSchedule · TEXT` |  |
| `HTMLAddress` | Full Address | The associated entity's address in HTML format. | Text | Global |  | `scenario.HTMLAddress · TEXT` |  |
| `KeyDateID` | Contract Key Date |  | Text | Global |  | `scenario.KeyDateID · TEXT` |  |
| `Lot` |  | If your parcel has a lot identifier this is commonly for parcels in urban areas enter the lot identifier in this field. | Text | Global |  | `scenario.Lot · TEXT` |  |
| `MajorTenants` | Major Tenants | Enter the anchors or competitors in the vicinity of the location. | Text | Global |  | `scenario.MajorTenants · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `scenario.Notes · TEXT` |  |
| `RiskClass` | Risk Class | Enter the risk class in this field. Risk classes are insurance tier identifiers which can be alphanumeric and differ across policies, providers, and locations. | Text | Global |  | `scenario.RiskClass · TEXT` |  |
| `ScenarioName` | Scenario Name | Enter a name for the scenario. | Text | Global | yes | `scenario.ScenarioName · TEXT` |  |
| `TradeAreaCompetitors` | Trade Area Competitors | Enter the names of the direct competitors in the market area. | Text | Global |  | `scenario.TradeAreaCompetitors · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Scenario ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `scenario.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `scenario.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `scenario.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `scenario.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `scenario.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `scenario.RevNumber · TEXT` |  |

## What points here (5 keys)

| Record type | Via column |
|---|---|
| [RETransaction](RETransaction.md) | `KickoffScenarioID`, `PreferredScenarioID`, `SelectedScenarioID` |
| [LinkReTransScenContact](LinkReTransScenContact.md) | `ScenarioID` |
| [MapClientSchedule](MapClientSchedule.md) | `ScenarioID` |
