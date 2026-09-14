# ProjectEntity

*107 fields · module: Platform & Tenancy · Postgres: `project_entity`*

The generic 'project' record used for capital projects, store rollouts, and portfolio initiatives — distinct from Contract, it tracks phase-gate status (Design, Construction, Possession, Operations) via parallel status/date pairs and milestone pointers, plus SUBMITBUTTON action fields for phase transitions. It spans four top-level groups (Milestones, Schedule, Statics, Summary Information), which is unusual and reflects that a 'project' is a cross-cutting concept touched by scheduling, milestone tracking, and portfolio reporting rather than owned by a single functional group. 170 fields.

Source: `data-fields/project-entity.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 107 |
| Catalogued fields | 170 (165 global, 5 firm) |
| Physical tables | 1 |
| Referenced by | 163 keys from 161 record types |
| Points at | 12 other records |
| Tenancy position | supertype |
| Rules that name it | 11 |

## What to know before rebuilding this

### 6 tenant custom columns

**Observed.** This record carries 6 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### The polymorphic spine

**Derived.** The supertype every business record hangs off. Its ProjectEntityTypeName column is the discriminator that makes one physical table present as several record types.

### 5 catalogued Firm-scope fields

**Observed.** Of 170 catalogued fields on this record, 5 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

### A hub: 163 keys point here

**Observed.** 161 record types hold a foreign key into this one, so it sits at the centre of the relationship graph. Changing its key or its identity is a change to AccrualTransaction, AcctingAssumptionAdjust, Allowance, AllowanceTransaction and 157 others.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [WF-R-045](../rules/WF-R-045.md) | When an assignee completes the form and presses Submit, SubmitForApprovalByMemberID/Name/Date are set once for the whole step. This is the direct consequence of the approver/assignee asymmetry: assignees do the work, one stamp records that  | Derived |
| [LAY-R-015](../rules/LAY-R-015.md) | Candidate driver fields are: the layout's primary table, plus every table reachable by a many-to-one FK from it, plus `ProjectEntity`. | Derived |
| [FAC-R-018](../rules/FAC-R-018.md) | Input: `Ownership`, `SiteSurvey`, `LandPurchaseSummary`, `LinkLandPurchaseInspection`, `DemographicResults` carry `ProjectEntityID` and no hard-typed FK to `Facility`/`Location`/`Parcel`. Effect: In principle any of these can attach to any  | Derived |
| [PLT-R-001](../rules/PLT-R-001.md) | The record is one of the 161 `entity_scoped` objects (not `ProjectEntity` itself or one of its 9 subtype roots) | Derived |
| [PLT-R-008](../rules/PLT-R-008.md) | The routing rule names a region-scoped principal category (see `../workflow/routing-and-approvals.md` §2, Dimension 2) | Derived |
| [PLT-R-010](../rules/PLT-R-010.md) | Every address block in the product repeats the same `StreetAddress1..4`/`City`/ `PostalCode`/`CountryID`/`JurisdictionID` shape and resolves tax rate through `Jurisdiction`, not through the country/state master directly | Derived |
| [PLT-R-015](../rules/PLT-R-015.md) | A single audit table serves templating across modules; `EntityTemplate` (this module) is the only one of the four whose home object is filed here | Observed |
| [PLT-R-016](../rules/PLT-R-016.md) | Do not silently pick one; `../../data-model/project-entity.md` is built on `ProjectEntity` and is the authority for the spine, but `Project`'s role remains genuinely open | Derived |
| [PPL-R-011](../rules/PPL-R-011.md) | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup | Derived |
| [AST-R-001](../rules/AST-R-001.md) | Trigger: N/A (structural). Input: `Asset.ProjectEntityID`, the only entity-scoping column on `Asset`. | Observed |
| [PRJ-R-002](../rules/PRJ-R-002.md) | An entity needs milestone/phase tracking (`CurrentMilestone`/`NextMilestone`/`PreviousMilestone` on the `ProjectEntity` union block) · `ProcessTimeline` → `ProcessTimelineTemplate` · Produces a flat, non-networked milestone list — no hierar | Observed |

## Fields

### Relationships (foreign keys) (10)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetTemplateID` | Budget Template ID | Template ID | Global |  | [BudgetTemplate](BudgetTemplate.md) |
| `ComplexID` | Complex Name | Complex ID | Global |  | [Complex](Complex.md) |
| `DemographicDMAID` | Demographic DMA | DMA ID | Global |  | [DMA](DMA.md) |
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |
| `LocationID` | Location | Location ID | Global |  | [Location](Location.md) |
| `PrototypeID` | Prototype | Prototype ID | Global |  | [Prototype](Prototype.md) |
| `RegionID` | Region | Region ID | Global |  | [Region](Region.md) |
| `RootRegionID` | Parent Region | Region ID | Global |  | [Region](Region.md) |
| `SubRegionID` | Sub Region | Region ID | Global |  | [Region](Region.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LinkProjectEntityContactListData` | Contact List | Contact | Global |  |  |
| `ManagerIDList` | Project Managers | Dropdown | Global |  |  |

### Coded values (drop-downs) (11)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeConstructionTypeID` | Construction Type | Dropdown (Construction Type Code) | Global |  | Construction Type Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeDealTypeID` | Deal Type | Dropdown (Deal Type Code) | Global |  | Deal Type Code |
| `CodeDesc_CodeMarketAreaID` | Market Potential | Dropdown (Market Area Code) | Global |  | Market Area Code |
| `CodeDesc_CodeProjectTypeID` | Real Estate Type | Dropdown (Project Type Code) | Global |  | Project Type Code |
| `CodeDistributionCenterID` | Distribution Center | Dropdown (Distribution Center Code) | Global |  | Distribution Center Code |
| `CodeMarketAreaID` | Market Area | Dropdown (Market Area Code) | Global |  | Market Area Code |
| `CodeMarketTypeID` | Market Type | Dropdown (Market Type Code) | Global |  | Market Type Code |
| `CodeProjectTypeID` | Project Type | Dropdown (Project Type Code) | Global |  | Project Type Code |
| `CurrentCodeProjectPhaseID` | Project Phase | Dropdown (Project Phase Code) | Global |  | Project Phase Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_PriorMonthAccrualTotal` |  | Currency | — |  |  |

### Quantities (12)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Revenue Weeks | Number | Global |  |  |
| `DBFolderSizeMB` | Storage Size (MB) | 2-Digit Number | Global |  |  |
| `Depth` |  | Number | Global |  |  |
| `EntityId` | Entity LxID | Number | Global |  |  |
| `Frontage` |  | Number | Global |  |  |
| `LatitudeDegrees` | Latitude | 5-Digit Number | Global |  |  |
| `LongitudeDegrees` | Longitude | 5-Digit Number | Global |  |  |
| `NumberOfDocuments` | Number of Documents | Number | Global |  |  |
| `ProjectEntityID` | Entity RecID | Number | Global |  |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |
| `SequenceNumber` | Sequence Number | Number | Global |  |  |
| `UsableArea` | Usable Area | Number | Global |  |  |

### Dates & timestamps (8)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualEndDate` | Actual/Forecast Delivery Year | Date | Global |  |  |
| `ActualStartDate` | Forecast/Actual Start Date | Date | Global |  |  |
| `BaselineEndDate` | Baseline Delivery Year | Date | Global |  |  |
| `ClientScheduleLastReviewedDate` | Last Updated Date | Date | Global |  |  |
| `ExpectedEndDate` | Original Delivery Year | Date | Global |  |  |
| `OriginalEndDate` | Baseline End Date | Date | Global |  |  |
| `OriginalStartDate` | Baseline Start Date | Date | Global |  |  |
| `SlotEndDate` | RE Planner Open Year | Date | Global |  |  |

### Flags (2)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |
| `IsDead` | Is Dead? | Boolean | Global |  |  |

### Text & notes (54)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseProvider` | System of Record | Text | Global |  |  |
| `City` |  | Text | Global |  |  |
| `CityStateProvinceCountry` | City, State | Text | Global |  |  |
| `ClientEntityID` | Store Number | Text | Global |  |  |
| `ComparisonList` | Comparison List | Text | Global |  |  |
| `CompletedPhaseStatus` | Completed Phase Status | Text | Global |  |  |
| `ConstructionPhaseStatus` | Construction Phase Status | Text | Global |  |  |
| `CountryID` | Country | Text | Global |  |  |
| `CrossStreet1` | Cross Street #1 | Text | Global |  |  |
| `CrossStreet2` | Cross Street #2 | Text | Global |  |  |
| `CurrentMilestone` | Current Milestone | Text | Global |  |  |
| `CurrentPhaseStatus` | Project Status | Text | Global |  |  |
| `DesignPhaseStatus` | Design Phase Status | Text | Global |  |  |
| `EntityEmail` | Entity Email | Text | Global |  |  |
| `EntityPhoto` | Entity Photo | Text | Global |  |  |
| `FacilityName` | Facility Name | Text | Global |  |  |
| `FinancialModel` | Financial Model | Text | Global |  |  |
| `FirmID` | Firm ID | Text | Global | yes |  |
| `Firm_SalesReportLogo` | Sales Report Logo | Text | Firm |  |  |
| `Firm_SalesReportLogoMadewell` |  | Text | — |  |  |
| `Firm_SalesReportSignature` | Sales Report Signature | Text | Firm |  |  |
| `Firm_SalesReportSignatureName` | Sales Report Signature Name | Text | Firm |  |  |
| `Firm_SalesReportSignatureTitle` | Sales Report Signature Title | Text | Firm |  |  |
| `HTMLAddress` | Full Address | Text | Global |  |  |
| `IssuesAndAlerts` | Issues And Alerts | Text | Global |  |  |
| `MapClientRecordID` | Client Unique ID | Text | Global |  |  |
| `MilestoneTimeline` | Milestone Timeline | Text | Global |  |  |
| `NextMilestone` | Next Milestone | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `OperationsPhaseStatus` | Operations Phase Status | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PossessionPhaseStatus` | Possession Phase Status | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `PotentialProjectName` | Site Name | Text | Global |  |  |
| `PreviousMilestone` | Previous Milestone | Text | Global |  |  |
| `ProgramID` | Portfolio/Program RecID | Text | Global |  |  |
| `ProgramName` | Portfolio/Program Name | Text | Global |  |  |
| `ProjectDescription` | Description | Text | Global |  |  |
| `ProjectEntityName` | Name | Text | Global | yes |  |
| `ProjectEntityTypeName` | Entity Type | Text | Global |  |  |
| `ProjectName` | Project Name | Text | Global |  |  |
| `PrototypeName` | Prototype Name | Text | Global |  |  |
| `RealEstatePhaseStatus` | Real Estate Phase Status | Text | Global |  |  |
| `RelatedEntities` | Related Entities | Text | Global |  |  |
| `RelocatedFrom` |  | Text | Global |  |  |
| `RunReportAction` | Run Report Action | Text | Global |  |  |
| `StreetAddress` | Street Address | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `ThirdPartyWarehouse` | Third Party Warehouse | Text | Global |  |  |
| `TimeZone` | Time Zone | Text | Global |  |  |
| `TradeArea` | Trade Area | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
| `UUID` | Entity UUID | Text | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossArea` | Gross Area | Acreage | Global |  |  |

## What points here (163 keys)

| Record type | Via column |
|---|---|
| [BudgetOption](BudgetOption.md) | `BudgetOptionTemplateID`, `ProjectEntityID` |
| [DevelopmentSlot](DevelopmentSlot.md) | `ProjectEntityID`, `ProjectPEID` |
| [AccrualTransaction](AccrualTransaction.md) | `ProjectEntityID` |
| [AcctingAssumptionAdjust](AcctingAssumptionAdjust.md) | `ProjectEntityID` |
| [Allowance](Allowance.md) | `ProjectEntityID` |
| [AllowanceTransaction](AllowanceTransaction.md) | `ProjectEntityID` |
| [AlternateRentSchedule](AlternateRentSchedule.md) | `ProjectEntityID` |
| [Asset](Asset.md) | `ProjectEntityID` |
| [AuditColumn](AuditColumn.md) | `ProjectEntityID` |
| [AuditTable](AuditTable.md) | `ProjectEntityID` |
| [BidPackage](BidPackage.md) | `ProjectEntityID` |
| [BidPackageAlternate](BidPackageAlternate.md) | `ProjectEntityID` |
| [BidPackageAlternateValue](BidPackageAlternateValue.md) | `ProjectEntityID` |
| [BidPackageBreakout](BidPackageBreakout.md) | `ProjectEntityID` |
| [BidPackageBreakoutValue](BidPackageBreakoutValue.md) | `ProjectEntityID` |
| [BidPackageTemplate](BidPackageTemplate.md) | `ProjectEntityID` |
| [BidderIssue](BidderIssue.md) | `ProjectEntityID` |
| [BudgetColumn](BudgetColumn.md) | `ProjectEntityID` |
| [BudgetColumnItemValue](BudgetColumnItemValue.md) | `ProjectEntityID` |
| [BudgetIndexValue](BudgetIndexValue.md) | `ProjectEntityID` |
| [BudgetLineGroup](BudgetLineGroup.md) | `ProjectEntityID` |
| [BudgetLineItem](BudgetLineItem.md) | `ProjectEntityID` |
| [BudgetLineLeaf](BudgetLineLeaf.md) | `ProjectEntityID` |
| [BudgetTemplate](BudgetTemplate.md) | `ProjectEntityID` |
| [BudgetTemplateAudit](BudgetTemplateAudit.md) | `ProjectEntityID` |
| [BudgetView](BudgetView.md) | `ProjectEntityID` |
| [CLRExtensionPart](CLRExtensionPart.md) | `ProjectEntityID` |
| [CPI](CPI.md) | `ProjectEntityID` |
| [ChangeOrder](ChangeOrder.md) | `ProjectEntityID` |
| [ClientListRow](ClientListRow.md) | `ProjectEntityID` |
| [CoTenancy](CoTenancy.md) | `ProjectEntityID` |
| [CommitteePackage](CommitteePackage.md) | `ProjectEntityID` |
| [ComparisonItem](ComparisonItem.md) | `ProjectEntityID` |
| [ComparisonReport](ComparisonReport.md) | `ProjectEntityID` |
| [Competitor](Competitor.md) | `ProjectEntityID` |
| [ContractAmendment](ContractAmendment.md) | `ProjectEntityID` |
| [ContractFinancialTest](ContractFinancialTest.md) | `ProjectEntityID` |
| [ContractTerm](ContractTerm.md) | `ProjectEntityID` |
| [CostTrackingTemplate](CostTrackingTemplate.md) | `ProjectEntityID` |
| [Covenant](Covenant.md) | `ProjectEntityID` |
| [DemographicResults](DemographicResults.md) | `ProjectEntityID` |
| [DevelopmentPlan](DevelopmentPlan.md) | `ProjectEntityID` |
| [Document](Document.md) | `ProjectEntityID` |
| [DocumentMarkup](DocumentMarkup.md) | `ProjectEntityID` |
| [EMailReceivedLog](EMailReceivedLog.md) | `ProjectEntityID` |
| [EMailSentLog](EMailSentLog.md) | `ProjectEntityID` |
| [EntityTemplate](EntityTemplate.md) | `ProjectEntityID` |
| [ExpenseAccrualSchedule](ExpenseAccrualSchedule.md) | `ProjectEntityID` |
| [ExpenseAccrualSetup](ExpenseAccrualSetup.md) | `ProjectEntityID` |
| [ExpenseAllocation](ExpenseAllocation.md) | `ProjectEntityID` |
| [ExpenseEscalation](ExpenseEscalation.md) | `ProjectEntityID` |
| [ExpenseRecovery](ExpenseRecovery.md) | `ProjectEntityID` |
| [ExpenseRecoveryItem](ExpenseRecoveryItem.md) | `ProjectEntityID` |
| [ExpenseRecoveryItemMapping](ExpenseRecoveryItemMapping.md) | `ProjectEntityID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `ProjectEntityID` |
| [ExpenseSetup](ExpenseSetup.md) | `ProjectEntityID` |
| [ExpenseVendorAllocation](ExpenseVendorAllocation.md) | `ProjectEntityID` |
| [FacilityExpense](FacilityExpense.md) | `ProjectEntityID` |
| [FinancialAdjustment](FinancialAdjustment.md) | `ProjectEntityID` |
| [FiscalPeriod](FiscalPeriod.md) | `ProjectEntityID` |
| [Folder](Folder.md) | `ProjectEntityID` |
| [FolderTemplate](FolderTemplate.md) | `ProjectEntityID` |
| [FolderTemplateAudit](FolderTemplateAudit.md) | `ProjectEntityID` |
| [Insurance](Insurance.md) | `ProjectEntityID` |
| [InvoiceIssue](InvoiceIssue.md) | `ProjectEntityID` |
| [InvoiceItem](InvoiceItem.md) | `ProjectEntityID` |
| [Issue](Issue.md) | `ProjectEntityID` |
| [IssueResponse](IssueResponse.md) | `ProjectEntityID` |
| [IssueSubmittal](IssueSubmittal.md) | `ProjectEntityID` |
| [KeyDate](KeyDate.md) | `ProjectEntityID` |
| [LandPurchaseSummary](LandPurchaseSummary.md) | `ProjectEntityID` |
| [LandlordInvoice](LandlordInvoice.md) | `ProjectEntityID` |
| [LandlordInvoiceItem](LandlordInvoiceItem.md) | `ProjectEntityID` |
| [LeaseAudit](LeaseAudit.md) | `ProjectEntityID` |
| [LeaseInfo](LeaseInfo.md) | `ProjectEntityID` |
| [LinkBudgetIndexBLI](LinkBudgetIndexBLI.md) | `ProjectEntityID` |
| [LinkBudgetViewBLI](LinkBudgetViewBLI.md) | `ProjectEntityID` |
| [LinkEMailReceivedLogDocument](LinkEMailReceivedLogDocument.md) | `ProjectEntityID` |
| [LinkIssuePart](LinkIssuePart.md) | `ProjectEntityID` |
| [LinkIssuePartOrder](LinkIssuePartOrder.md) | `ProjectEntityID` |
| [LinkLandPurchaseInspection](LinkLandPurchaseInspection.md) | `ProjectEntityID` |
| [LinkLandlordInvPaymentTxn](LinkLandlordInvPaymentTxn.md) | `ProjectEntityID` |
| [LinkMemberProjectEntity](LinkMemberProjectEntity.md) | `ProjectEntityID` |
| [LinkPEMemberCodeJobTitle](LinkPEMemberCodeJobTitle.md) | `ProjectEntityID` |
| [LinkProjectEntityContact](LinkProjectEntityContact.md) | `ProjectEntityID` |
| [LinkProjectEntityVendor](LinkProjectEntityVendor.md) | `ProjectEntityID` |
| [LinkReTransScenContact](LinkReTransScenContact.md) | `ProjectEntityID` |
| [LinkReceiptTransaction](LinkReceiptTransaction.md) | `ProjectEntityID` |
| [LinkRegionManager](LinkRegionManager.md) | `ProjectEntityID` |
| [LinkSchedOffsetExpGrpType](LinkSchedOffsetExpGrpType.md) | `ProjectEntityID` |
| [LinkTaskByCodeMember](LinkTaskByCodeMember.md) | `ProjectEntityID` |
| [LinkTaskDocument](LinkTaskDocument.md) | `ProjectEntityID` |
| [LinkTaskMember](LinkTaskMember.md) | `ProjectEntityID` |
| [MapClientSchedule](MapClientSchedule.md) | `ProjectEntityID` |
| [MemberAudit](MemberAudit.md) | `ProjectEntityID` |
| [Notify](Notify.md) | `ProjectEntityID` |
| [Ownership](Ownership.md) | `ProjectEntityID` |
| [ParcelAccess](ParcelAccess.md) | `ProjectEntityID` |
| [Parking](Parking.md) | `ProjectEntityID` |
| [Party](Party.md) | `ProjectEntityID` |
| [PayApp](PayApp.md) | `ProjectEntityID` |
| [PaymentReceipt](PaymentReceipt.md) | `ProjectEntityID` |
| [PaymentTransaction](PaymentTransaction.md) | `ProjectEntityID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `ProjectEntityID` |
| [PercentageRent](PercentageRent.md) | `ProjectEntityID` |
| [PercentageRentBreakpoint](PercentageRentBreakpoint.md) | `ProjectEntityID` |
| [ProFormaBudget](ProFormaBudget.md) | `ProjectEntityID` |
| [ProcessTimeline](ProcessTimeline.md) | `ProjectEntityID` |
| [ProgramRevenueWeeks](ProgramRevenueWeeks.md) | `ProjectEntityID` |
| [PropertyTaxAppeal](PropertyTaxAppeal.md) | `ProjectEntityID` |
| [PropertyTaxAppealAward](PropertyTaxAppealAward.md) | `ProjectEntityID` |
| [PropertyTaxAssessment](PropertyTaxAssessment.md) | `ProjectEntityID` |
| [PropertyTaxBill](PropertyTaxBill.md) | `ProjectEntityID` |
| [PropertyTaxDetail](PropertyTaxDetail.md) | `ProjectEntityID` |
| [PropertyTaxSummary](PropertyTaxSummary.md) | `ProjectEntityID` |
| [PurchaseOrder](PurchaseOrder.md) | `ProjectEntityID` |
| [Question](Question.md) | `ProjectEntityID` |
| [RETransaction](RETransaction.md) | `ProjectEntityID` |
| [RecalcOverrideNotes](RecalcOverrideNotes.md) | `ProjectEntityID` |
| [Region](Region.md) | `ProjectEntityID` |
| [Responsibility](Responsibility.md) | `ProjectEntityID` |
| [SLPeriod](SLPeriod.md) | `ProjectEntityID` |
| [SLSummary](SLSummary.md) | `ProjectEntityID` |
| [Sales](Sales.md) | `ProjectEntityID` |
| [SalesExclusion](SalesExclusion.md) | `ProjectEntityID` |
| [SalesExclusionCap](SalesExclusionCap.md) | `ProjectEntityID` |
| [Scenario](Scenario.md) | `ProjectEntityID` |
| [ScheduledOffset](ScheduledOffset.md) | `ProjectEntityID` |
| [ScratchPad](ScratchPad.md) | `ProjectEntityID` |
| [SecurityDeposit](SecurityDeposit.md) | `ProjectEntityID` |
| [ServiceRequest](ServiceRequest.md) | `ProjectEntityID` |
| [SiteSurvey](SiteSurvey.md) | `ProjectEntityID` |
| [Space](Space.md) | `ProjectEntityID` |
| [Task](Task.md) | `ProjectEntityID` |
| [TaskGroup](TaskGroup.md) | `ProjectEntityID` |
| [TaskItem](TaskItem.md) | `ProjectEntityID` |
| [TaskPredecessor](TaskPredecessor.md) | `ProjectEntityID` |
| [TaskTemplate](TaskTemplate.md) | `ProjectEntityID` |
| [TaskTemplateAudit](TaskTemplateAudit.md) | `ProjectEntityID` |
| [TemplateAudit](TemplateAudit.md) | `ProjectEntityID` |
| [Tenant](Tenant.md) | `ProjectEntityID` |
| [Usage](Usage.md) | `ProjectEntityID` |
| [UseBasedRent](UseBasedRent.md) | `ProjectEntityID` |
| [UseBasedRentBreakpoint](UseBasedRentBreakpoint.md) | `ProjectEntityID` |
| [VariableRentOffset](VariableRentOffset.md) | `ProjectEntityID` |
| [VirtualPRAccrualPeriod](VirtualPRAccrualPeriod.md) | `ProjectEntityID` |
| [VirtualPRPAggregate](VirtualPRPAggregate.md) | `ProjectEntityID` |
| [VirtualPercentageRentPeriod](VirtualPercentageRentPeriod.md) | `ProjectEntityID` |
| [VirtualTemplateBudget](VirtualTemplateBudget.md) | `ProjectEntityID` |
| [VirtualTemplateBudgetOption](VirtualTemplateBudgetOption.md) | `ProjectEntityID` |
| [VirtualTemplateFolder](VirtualTemplateFolder.md) | `ProjectEntityID` |
| [VirtualTemplateSchedule](VirtualTemplateSchedule.md) | `ProjectEntityID` |
| [VirtualUBRPAggregate](VirtualUBRPAggregate.md) | `ProjectEntityID` |
| [VirtualUseBasedRentPeriod](VirtualUseBasedRentPeriod.md) | `ProjectEntityID` |
| [WFStepFullImport](WFStepFullImport.md) | `ProjectEntityID` |
| [WorkFlow](WorkFlow.md) | `ProjectEntityID` |
| [WorkFlowStep](WorkFlowStep.md) | `ProjectEntityID` |
| [WorkFlowStepApprover](WorkFlowStepApprover.md) | `ProjectEntityID` |
| [WorkFlowStepAssignee](WorkFlowStepAssignee.md) | `ProjectEntityID` |
| [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) | `ProjectEntityID` |
| [WorkOrder](WorkOrder.md) | `ProjectEntityID` |
