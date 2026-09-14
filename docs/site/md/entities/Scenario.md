# Scenario

*69 fields · module: Portfolio & Real-Estate Transactions · Postgres: `scenario`*

A deal/transaction scenario under RE Transaction — comparative what-if terms (Broker Commission, Capital Required, Annual Total Rent) for a prospective site or renewal being evaluated before commitment, plus site demographic fields (Average HH Income, Block) inherited from the site-selection process. 70 Global fields; Scenario sits upstream of Contract in the deal lifecycle, modeling terms under negotiation rather than terms in force.

Source: `data-fields/scenario.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 69 |
| Catalogued fields | 70 (70 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 5 keys from 3 record types |
| Points at | 10 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 7 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActiveDealStepTaskIDList` | Active Deal Step(s) | Task/Group ID | Global |  | [TaskGroup](TaskGroup.md) |
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |
| `ContractTermID` | Contract Term | Contract Term ID | Global |  | [ContractTerm](ContractTerm.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `DealSchedule` | Deal Schedule | Task/Group ID | Global |  | [TaskGroup](TaskGroup.md) |
| `ProjectEntityID` | Related Entity | Entity ID | Global | yes | [ProjectEntity](ProjectEntity.md) |
| `RETransactionID` | RE Transaction | RE Transaction ID | Global | yes | [RETransaction](RETransaction.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentIDList` | Documents | Document List | Global |  |  |

### Coded values (drop-downs) (13)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeCovenantCategoryID` | Covenant Category | Dropdown (Covenant Category Code) | Global |  | Covenant Category Code |
| `CodeCovenantGroupID` | Covenant Group | Dropdown (Covenant Group Code) | Global |  | Covenant Group Code |
| `CodeCovenantStatusID` | Covenant Status | Dropdown (Covenant Status Code) | Global |  | Covenant Status Code |
| `CodeCovenantTypeID` | Covenant Type | Dropdown (Covenant Type Code) | Global |  | Covenant Type Code |
| `CodeCurrencyTypeID` | Currency | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeDecisionStatusID` | Decision Status | Dropdown (Decision Status Code) | Global |  | Decision Status Code |
| `CodeMarketAreaID` | Market | Dropdown (Market Area Code) | Global |  | Market Area Code |
| `CodePropertyTypeID` | Property Type | Dropdown (Property Type Code) | Global |  | Property Type Code |
| `CodeScenarioDealTypeID` | Scenario Deal Type | Dropdown (Scenario Deal Type Code) | Global | yes | Scenario Deal Type Code |
| `CodeScenarioTypeID` | Scenario Type | Dropdown (Scenario Type Code) | Global |  | Scenario Type Code |
| `CodeTermStatusID` | Term Status | Dropdown (Term Status Code) | Global |  | Term Status Code |
| `CodeTermTypeID` | Term Type | Dropdown (Term Type Code) | Global |  | Term Type Code |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AnnualTotalRent` | Annual Total Rent | Currency | Global |  |  |
| `AverageHHIncome` | Average HH Income | Currency | Global |  |  |
| `CapitalRequired` | Capital Required | Currency | Global |  |  |
| `Deposit` |  | Currency | Global |  |  |
| `MedianHHIncome` | Median HH Income | Currency | Global |  |  |
| `OperatingCostsCAM` | Operating Costs CAM | Currency | Global |  |  |
| `TIAllowance` | TI Allowance | Currency | Global |  |  |
| `TiPerAreaUnit` | TI Per Area Unit | Currency | Global |  |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BrokerCommission` | Broker Commission | Percentage | Global |  |  |
| `DiscountRate` | Discount Rate | Percentage | Global |  |  |
| `Population5yrGrowth` | Population 5yr Growth | Percentage | Global |  |  |
| `ProRataShareRate` | Pro Rata Share Rate | Percentage | Global |  |  |

### Quantities (10)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdditionalTerms` | Additional Terms | Number | Global |  |  |
| `CloseDays` | Close Days | Number | Global |  |  |
| `DueDiligenceDays` | Due Diligence Days | Number | Global |  |  |
| `NewTermLength` | New Term Length | Number | Global |  |  |
| `ParkingRatio` | Parking Ratio | 5-Digit Number | Global |  |  |
| `ParkingSpaces` | Parking Spaces | Number | Global |  |  |
| `ProposedTermLength` | Proposed Term Length | Number | Global |  |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |
| `ScenarioID` | Scenario RecID | Number | Global |  |  |
| `TotalPopulation` | Total Population | Number | Global |  |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DecisionDate` | Decision Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |
| `NewTermEndDate` | New Term End Date | Date | Global |  |  |
| `NewTermStartDate` | New Term Start Date | Date | Global |  |  |
| `NoticeBeginDate` | Notice Begin Date | Date | Global |  |  |
| `NoticeEndDate` | Notice End Date | Date | Global |  |  |
| `OriginalLeaseStartDate` | Original Lease Start Date | Date | Global |  |  |
| `ProposedCommencementDate` | Proposed Commencement Date | Date | Global |  |  |

### Text & notes (11)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Block` |  | Text | Global |  |  |
| `ClientNumber` | Term Client Number | Text | Global |  |  |
| `DealStepSchedule` | Deal Steps | Text | Global |  |  |
| `HTMLAddress` | Full Address | Text | Global |  |  |
| `KeyDateID` | Contract Key Date | Text | Global |  |  |
| `Lot` |  | Text | Global |  |  |
| `MajorTenants` | Major Tenants | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `RiskClass` | Risk Class | Text | Global |  |  |
| `ScenarioName` | Scenario Name | Text | Global | yes |  |
| `TradeAreaCompetitors` | Trade Area Competitors | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Scenario ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (5 keys)

| Record type | Via column |
|---|---|
| [RETransaction](RETransaction.md) | `KickoffScenarioID`, `PreferredScenarioID`, `SelectedScenarioID` |
| [LinkReTransScenContact](LinkReTransScenContact.md) | `ScenarioID` |
| [MapClientSchedule](MapClientSchedule.md) | `ScenarioID` |
