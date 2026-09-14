# Member

*81 fields · module: People & Parties · Postgres: `member`*

The internal user/employee account record for Lx itself (not a lease party) — login and access-control fields (Accept EULA?, Always Spell Check?, Color Scheme) alongside org fields (Code Job Function, Code Analytics Role) and billing rates. 78 Global fields under Company Items; this is user-account metadata rather than lease data, included in the catalog because Member records are referenced everywhere else (Created By, Modified By, approvers, assignees) via sTYPE_MEMBER lookup fields.

Source: `data-fields/member.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 81 |
| Catalogued fields | 78 (78 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 290 keys from 162 record types |
| Points at | 6 other records |
| Tenancy position | firm_global |
| Rules that name it | 17 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### A hub: 290 keys point here

**Observed.** 162 record types hold a foreign key into this one, so it sits at the centre of the relationship graph. Changing its key or its identity is a change to AccrualTransaction, Allowance, AllowanceTransaction, AlternateRentSchedule and 158 others.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-062](../rules/ACC-R-062.md) | all three ASC 842 steps use `Member` — a named approver, resolved at configuration time rather than by org-chart position | Observed |
| [WF-R-026](../rules/WF-R-026.md) | The step's ApproverJobTitleIDList is intersected against the roster of the entity the workflow is running on, filtered to members holding a matching job title, and the resulting flat member list is frozen onto the running step as WorkFlowSt | Derived |
| [WF-R-027](../rules/WF-R-027.md) | User Class routing resolves against Member.CodeUserClassID intersected with the entity roster; Org Chart Level routing walks Member.SupervisorID the configured number of hops from an anchor that is itself unstated (OQ-22); | Derived |
| [WF-R-028](../rules/WF-R-028.md) | Step instantiation · `WFTS.ApproverType` = Org Chart Level; `WorkFlowTemplateStepMember.OrgChartLevel`; | Derived |
| [WF-R-035](../rules/WF-R-035.md) | Both this field and Member.IsUnassignedWorkFlowApprover are documented as unimplemented placeholders. | Observed |
| [LAY-R-009](../rules/LAY-R-009.md) | A step resolves its approver by `Approval Level`: `Member`, `Job Title`, or `Ad Hoc`. | Derived |
| [PPL-R-001](../rules/PPL-R-001.md) | `Person` and `NonMember` are field-for-field identical (37/37, zero type mismatches); `Member` is that same 37-field block plus 44 login/authorization fields | Derived |
| [PPL-R-002](../rules/PPL-R-002.md) | No `Person ID` FK type exists anywhere in the 60-odd declared FK types | Inferred |
| [PPL-R-003](../rules/PPL-R-003.md) | The existing identity is promoted to carry login/authorization data; it is not deleted and recreated. The exact mechanics (same row extended vs. new row sharing `PersonID`) are open — see `member-vs-person-vs-party.md` open question 1 | Inferred |
| [PPL-R-007](../rules/PPL-R-007.md) | The identity/user record must be cheaply reachable from nearly every write path in the product for stamping alone, independent of its true business-domain reference count (50 edges) | Derived |
| [PPL-R-009](../rules/PPL-R-009.md) | A person can be selected by class, by title (global or entity-specific), or by reporting-line position, and these three do not have to agree with each other | Observed |
| [PPL-R-010](../rules/PPL-R-010.md) | Differs from `Member.CodeJobTitleID` | Inferred |
| [PPL-R-011](../rules/PPL-R-011.md) | This is a two-hop resolution (entity → region/market → manager), not a direct `Member` attribute lookup | Derived |
| [PPL-R-012](../rules/PPL-R-012.md) | The rich role-based apparatus this module documents is largely latent in ASG's actual configuration. Treat as lower priority pending the answer to `../workflow/routing-and-approvals.md` OQ-42 (deliberate policy vs. workaround for the "all-f | Observed |
| [PPL-R-013](../rules/PPL-R-013.md) | No `WorkFlowTemplateStep`/`WorkFlowTemplateStepAction` field reads these columns (exhaustive check, `../workflow/step-actions.md`/`routing-and-approvals.md`) | Derived |
| [PRJ-R-010](../rules/PRJ-R-010.md) | A task needs an assignee, but not a named individual · `LinkTaskByCodeMember.CodeJobTitleID`, `OrgChartLevel` · Assigns by job title / org-chart level rather than by `Member`, matching the `AssigneeType` = `JOB_TITLE` routing option (`graph | Derived |
| [PRJ-R-011](../rules/PRJ-R-011.md) | A task needs a named assignee · `LinkTaskMember.MemberID` · Assigns a specific `Member`, alongside `TaskGroup.Assignee_MemberID`'s own direct field — two mechanisms for the same concept exist side by side. · Observed | Observed |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EmployerID` | Employer | Employer ID | Global | yes | [Employer](Employer.md) |
| `IStateProvinceCountryID` |  | Country, State, County ID | — |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `JurisdictionID` | Jurisdiction | County ID | Global |  | [Jurisdiction](Jurisdiction.md) |
| `StateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |
| `SupervisorID` | Supervisor | Member ID | Global |  | [Member](Member.md) |

### Coded values (drop-downs) (10)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAnalyticsRoleID` | Code Analytics Role | Dropdown (Analytics Role Code) | Global |  | Analytics Role Code |
| `CodeApprovalCurrencyTypeID` | Approval Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeApprovalStatusID` | RE Contract Approval Level | Dropdown (Approval Status Code) | Global |  | Approval Status Code |
| `CodeContactTypeIDList` |  | Dropdown (Contact Type Code) | — |  | Contact Type Code |
| `CodeEquipApprovalStatusID` | Equipment Contract Approval Level | Dropdown (Approval Status Code) | Global |  | Approval Status Code |
| `CodeJobFunctionID` | Code Job Function | Dropdown (Job Function Code) | Global | yes | Job Function Code |
| `CodeJobTitleID` | Job Title | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `CodeJobTitleIDList` | Job Titles | Dropdown (Job Title Code) | Global | yes | Job Title Code |
| `CodeLockOutReasonID` | Member Login Status | Dropdown (Lock Out Reason Code) | Global | yes | Lock Out Reason Code |
| `CodeUserClassID` | User Class | Dropdown (User Class) | Global | yes | User Class |

### Money (10)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillRate1` | Bill Rate #1 | Currency | Global |  |  |
| `BillRate2` | Bill Rate #2 | Currency | Global |  |  |
| `EquipPaymentApprovalMaxAmount` | Equipment Contract Payment Approval Amount (Maximum) | Currency | Global |  |  |
| `EquipPaymentApprovalMinAmount` | Equipment Contract Payment Approval Amount (Minimum) | Currency | Global |  |  |
| `EquipRecurringApprovalMaxAmount` | Equipment Contract Recurring Approval Amount (Maximum) | Currency | Global |  |  |
| `EquipRecurringApprovalMinAmount` | Equipment Contract Recurring Approval Amount (Minimum) | Currency | Global |  |  |
| `PaymentApprovalMaxAmount` | RE Contract Payment Approval Amount (Maximum) | Currency | Global |  |  |
| `PaymentApprovalMinAmount` | RE Contract Payment Approval Amount (Minimum) | Currency | Global |  |  |
| `RecurringApprovalMaxAmount` | RE Contract Recurring Approval Amount (Maximum) | Currency | Global |  |  |
| `RecurringApprovalMinAmount` | RE Contract Recurring Approval Amount (Minimum) | Currency | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MemberID` | Member RecID | Number | Global |  |  |
| `NumberPattern` | Number Pattern | Number Format | Global |  |  |
| `PersonID` | Person RecID | Number | Global | yes |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `LastLoginDate` | Last Login Date | Time | Global |  |  |

### Flags (13)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AcceptEULA` | Accept EULA? | Boolean | Global | yes |  |
| `AlwaysSpellCheck` | Always Spell Check? | Boolean | Global | yes |  |
| `ConvertToMember` | Convert To Member | Boolean | Global |  |  |
| `EmployerInactive` | Employer Inactive? | Boolean | Global |  |  |
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |
| `IsAdministrator` | Is Administrator? | Boolean | Global |  |  |
| `IsExemptFromPWDExpiration` | Is Exempt from Password Expiration? | Boolean | Global | yes |  |
| `IsLucernexAdministrator` | Is Lx Administrator? | Boolean | Global |  |  |
| `IsMasterMember` | Is Master Member? | Boolean | Global |  |  |
| `IsMasterPerson` | Is Master Person? | Boolean | Global |  |  |
| `IsUnassignedWorkFlowApprover` | Unassigned WorkFlow Approver | Boolean | Global | yes |  |
| `IsViewPrivateIssueAllowed` | Is View Private Issue Allowed? | Boolean | Global | yes |  |
| `UseEmployerAddress` | Use Employer Address? | Boolean | Global | yes |  |

### Text & notes (34)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AnySiteLoginName` | Demographics Login | Text | Global |  |  |
| `AnySitePassword` | Demographics Password | Text | Global |  |  |
| `City` |  | Text | Global |  |  |
| `ColorScheme` | Color Scheme | Text | Global |  |  |
| `Country` |  | Text | Global |  |  |
| `CountryID` |  | Text | — |  |  |
| `Description` |  | Text | Global |  |  |
| `Designations` |  | Text | Global |  |  |
| `EMail1` | Email #1 | Text | Global |  |  |
| `EMail2` | Email #2 | Text | Global |  |  |
| `Fax` |  | Text | Global |  |  |
| `FirstName` | First Name | Text | Global | yes |  |
| `HtmlPersonAddress` | Address | Text | Global |  |  |
| `Language` |  | Text | Global |  |  |
| `LastName` | Last Name | Text | Global | yes |  |
| `LoginName` | Login Name | Text | Global | yes |  |
| `MemberNameFirstLast` | Member Name | Text | Global |  |  |
| `MemberPhoto` | Member Photo | Text | Global |  |  |
| `MiddleName` | Middle Name | Text | Global |  |  |
| `MobileNumber` | Mobile Number | Text | Global |  |  |
| `Password` |  | Text | Global | yes |  |
| `PersonNameLastFirst` | Member Name - Last, First | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PhoneExtension` | Phone Extension | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `Suffix` |  | Text | Global |  |  |
| `TimeZone` | Time Zone | Text | Global |  |  |
| `Title` |  | Text | Global |  |  |
| `WebSite` | Web Site | Text | Global |  |  |
| `WirelessEMail` | Wireless E Mail | Text | Global |  |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Member ClientID | Text | Global | yes |  |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DatePattern` | Date Pattern | Date Format | Global |  |  |

## What points here (290 keys)

| Record type | Via column |
|---|---|
| [WorkFlowTemplateStep](WorkFlowTemplateStep.md) | `ApproverMemberIDList`, `AssigneeMemberIDList`, `CreatedByID`, `ModifiedByID`, `NotifieeMemberIDList`, `RunAtCompleteApprover1ID`, `RunAtCompleteApprover2ID`, `RunAtStartApprover1ID`, `RunAtStartApprover2ID`, `UnassignedApproverID` |
| [WFStepFullImport](WFStepFullImport.md) | `ApproverMemberIDList`, `AssigneeMemberIDList`, `CurrentStepMemberIDList`, `ModifiedByID`, `NotifieeMemberIDList`, `PriorSubmitByMemberID`, `SubmitForApprovalByMemberID` |
| [WorkFlowStep](WorkFlowStep.md) | `ApproverMemberIDList`, `AssigneeMemberIDList`, `CurrentStepMemberIDList`, `ModifiedByID`, `NotifieeMemberIDList`, `PriorSubmitByMemberID`, `SubmitForApprovalByMemberID` |
| [Issue](Issue.md) | `AssignedToMemberIDs`, `AttentionEmailTo`, `CheckedOutByMemberID`, `InitiatedByMemberID`, `ManagerMemberIDs`, `ModifiedByID` |
| [BidPackage](BidPackage.md) | `BidAwardByID`, `BidCancelledByID`, `CreatedByID`, `ModifiedByID`, `WinningBidMemberIDList` |
| [SLSummary](SLSummary.md) | `CreatedByID`, `ModifiedByID`, `NeedsRecalcModifiedByLastMember`, `NeedsRecalcModifiedByMemberIDList` |
| [BidderIssue](BidderIssue.md) | `CreatedByID`, `MemberIDList`, `ModifiedByID` |
| [Contract](Contract.md) | `CreatedByID`, `Firm_LeaseAnalyst`, `ModifiedByID` |
| [MemberAudit](MemberAudit.md) | `ImpersonatingMemberID`, `MemberID`, `ModifiedByID` |
| [RETransaction](RETransaction.md) | `AssigneeMemberID`, `CreatedByID`, `ModifiedByID` |
| [WorkOrder](WorkOrder.md) | `ApproverMemberID`, `CreatedByID`, `ModifiedByID` |
| [AccrualTransaction](AccrualTransaction.md) | `CreatedByID`, `ModifiedByID` |
| [AlternateRentSchedule](AlternateRentSchedule.md) | `CreatedByID`, `ModifiedByID` |
| [Asset](Asset.md) | `CreatedByID`, `ModifiedByID` |
| [AssetHistory](AssetHistory.md) | `CreatedByID`, `ModifiedByID` |
| [BidPackageTemplate](BidPackageTemplate.md) | `CreatedByID`, `ModifiedByID` |
| [BudgetColumn](BudgetColumn.md) | `CreatedByMemberID`, `ModifiedByID` |
| [BudgetColumnType](BudgetColumnType.md) | `CreatedByID`, `ModifiedByID` |
| [BudgetOption](BudgetOption.md) | `CreatedByMemberID`, `ModifiedByID` |
| [BudgetOptionTemplate](BudgetOptionTemplate.md) | `CreatedByID`, `ModifiedByID` |
| [BudgetTemplateAudit](BudgetTemplateAudit.md) | `CreatedByID`, `ModifiedByID` |
| [BudgetView](BudgetView.md) | `CreatedByID`, `ModifiedByID` |
| [ChangeOrder](ChangeOrder.md) | `CreatedByID`, `ModifiedByID` |
| [ContractFinancialTest](ContractFinancialTest.md) | `CreatedByID`, `ModifiedByID` |
| [CostTrackingTemplate](CostTrackingTemplate.md) | `CreatedByID`, `ModifiedByID` |
| [CustomCodeField](CustomCodeField.md) | `CreatedByID`, `ModifiedByID` |
| [DevelopmentSlot](DevelopmentSlot.md) | `BrokerMemberID`, `ModifiedByID` |
| [DiscountRate](DiscountRate.md) | `CreatedByID`, `ModifiedByID` |
| [Document](Document.md) | `CheckedOutByMemberID`, `ModifiedByID` |
| [EMailReceivedLog](EMailReceivedLog.md) | `CreatedByID`, `ModifiedByID` |
| [Employer](Employer.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseAccrualSchedule](ExpenseAccrualSchedule.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseAccrualSetup](ExpenseAccrualSetup.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseRecovery](ExpenseRecovery.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseRecoveryItem](ExpenseRecoveryItem.md) | `CreatedByID`, `ModifiedByID` |
| [ExpenseVendorAllocation](ExpenseVendorAllocation.md) | `CreatedByID`, `ModifiedByID` |
| [Facility](Facility.md) | `CreatedByID`, `ModifiedByID` |
| [FacilityExpense](FacilityExpense.md) | `CreatedByID`, `ModifiedByID` |
| [FinancialAdjustment](FinancialAdjustment.md) | `CreatedByID`, `ModifiedByID` |
| [FolderTemplateAudit](FolderTemplateAudit.md) | `CreatedByID`, `ModifiedByID` |
| [HolidayDate](HolidayDate.md) | `CreatedByID`, `ModifiedByID` |
| [HolidaySchedule](HolidaySchedule.md) | `CreatedByID`, `ModifiedByID` |
| [InvoiceIssue](InvoiceIssue.md) | `CreatedByID`, `ModifiedByID` |
| [InvoiceItem](InvoiceItem.md) | `CreatedByID`, `ModifiedByID` |
| [IssueResponse](IssueResponse.md) | `CreatedByID`, `ModifiedByID` |
| [LandlordInvoice](LandlordInvoice.md) | `CreatedByID`, `ModifiedByID` |
| [LandlordInvoiceItem](LandlordInvoiceItem.md) | `CreatedByID`, `ModifiedByID` |
| [LinkLandlordInvPaymentTxn](LinkLandlordInvPaymentTxn.md) | `CreatedByID`, `ModifiedByID` |
| [LinkMemberProjectEntity](LinkMemberProjectEntity.md) | `MemberID`, `ModifiedByID` |
| [LinkReTransScenContact](LinkReTransScenContact.md) | `CreatedByID`, `ModifiedByID` |
| [LinkReceiptTransaction](LinkReceiptTransaction.md) | `CreatedByID`, `ModifiedByID` |
| [LinkSchedOffsetExpGrpType](LinkSchedOffsetExpGrpType.md) | `CreatedByID`, `ModifiedByID` |
| [LinkTaskMember](LinkTaskMember.md) | `MemberID`, `ModifiedByID` |
| [Location](Location.md) | `CreatedByID`, `ModifiedByID` |
| [Member](Member.md) | `ModifiedByID`, `SupervisorID` |
| [Parcel](Parcel.md) | `CreatedByID`, `ModifiedByID` |
| [Parking](Parking.md) | `CreatedByID`, `ModifiedByID` |
| [PayApp](PayApp.md) | `CreatedByID`, `ModifiedByID` |
| [PercentageRentBreakpoint](PercentageRentBreakpoint.md) | `CreatedByID`, `ModifiedByID` |
| [PotentialProject](PotentialProject.md) | `CreatedByID`, `ModifiedByID` |
| [ProcessTimeline](ProcessTimeline.md) | `Assignee_MemberID`, `ModifiedByID` |
| [Program](Program.md) | `CreatedByID`, `ModifiedByID` |
| [Project](Project.md) | `CreatedByID`, `ModifiedByID` |
| [ProjectEntity](ProjectEntity.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxAppeal](PropertyTaxAppeal.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxAppealAward](PropertyTaxAppealAward.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxAssessment](PropertyTaxAssessment.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxBill](PropertyTaxBill.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxDetail](PropertyTaxDetail.md) | `CreatedByID`, `ModifiedByID` |
| [PropertyTaxSummary](PropertyTaxSummary.md) | `CreatedByID`, `ModifiedByID` |
| [Prototype](Prototype.md) | `CreatedByID`, `ModifiedByID` |
| [PurchaseOrder](PurchaseOrder.md) | `CreatedByID`, `ModifiedByID` |
| [Question](Question.md) | `CreatedByID`, `ModifiedByID` |
| [ReTransScenContact](ReTransScenContact.md) | `CreatedByID`, `ModifiedByID` |
| [RecalcOverrideNotes](RecalcOverrideNotes.md) | `CreatedByID`, `ModifiedByID` |
| [SLPeriod](SLPeriod.md) | `CreatedByID`, `ModifiedByID` |
| [SalesExclusion](SalesExclusion.md) | `CreatedByID`, `ModifiedByID` |
| [SalesExclusionCap](SalesExclusionCap.md) | `CreatedByID`, `ModifiedByID` |
| [Scenario](Scenario.md) | `CreatedByID`, `ModifiedByID` |
| [ScheduledOffset](ScheduledOffset.md) | `CreatedByID`, `ModifiedByID` |
| [ServiceRequest](ServiceRequest.md) | `CreatedByID`, `ModifiedByID` |
| [Space](Space.md) | `CreatedByID`, `ModifiedByID` |
| [Task](Task.md) | `Assignee_MemberID`, `ModifiedByID` |
| [TaskGroup](TaskGroup.md) | `Assignee_MemberID`, `ModifiedByID` |
| [TaskItem](TaskItem.md) | `Assignee_MemberID`, `ModifiedByID` |
| [TaskPredecessor](TaskPredecessor.md) | `CreatedByID`, `ModifiedByID` |
| [TaskTemplateAudit](TaskTemplateAudit.md) | `CreatedByID`, `ModifiedByID` |
| [TemplateAudit](TemplateAudit.md) | `CreatedByID`, `ModifiedByID` |
| [Tenant](Tenant.md) | `CreatedByID`, `ModifiedByID` |
| [UseBasedRentBreakpoint](UseBasedRentBreakpoint.md) | `CreatedByID`, `ModifiedByID` |
| [VendorInsurance](VendorInsurance.md) | `CreatedByID`, `ModifiedByID` |
| [WorkFlow](WorkFlow.md) | `InitiatedByMemberID`, `ModifiedByID` |
| [WorkFlowStepApprover](WorkFlowStepApprover.md) | `MemberID`, `ModifiedByID` |
| [WorkFlowStepAssignee](WorkFlowStepAssignee.md) | `MemberID`, `ModifiedByID` |
| [WorkFlowTemplate](WorkFlowTemplate.md) | `CreatedByID`, `ModifiedByID` |
| [WorkFlowTemplateStepAction](WorkFlowTemplateStepAction.md) | `CreatedByID`, `ModifiedByID` |
| [Allowance](Allowance.md) | `ModifiedByID` |
| [AllowanceTransaction](AllowanceTransaction.md) | `ModifiedByID` |
| [AuditColumn](AuditColumn.md) | `CreatedByID` |
| [BudgetColumnItemValue](BudgetColumnItemValue.md) | `ModifiedByID` |
| [BudgetIndex](BudgetIndex.md) | `ModifiedByID` |
| [BudgetIndexValue](BudgetIndexValue.md) | `ModifiedByID` |
| [BudgetLineGroup](BudgetLineGroup.md) | `ModifiedByID` |
| [BudgetLineItem](BudgetLineItem.md) | `ModifiedByID` |
| [BudgetLineLeaf](BudgetLineLeaf.md) | `ModifiedByID` |
| [CLRExtensionPart](CLRExtensionPart.md) | `ModifiedByID` |
| [CPI](CPI.md) | `ModifiedByID` |
| [ClientListRow](ClientListRow.md) | `ModifiedByID` |
| [CoTenancy](CoTenancy.md) | `ModifiedByID` |
| [CodeExpenseType](CodeExpenseType.md) | `ModifiedByID` |
| [Competitor](Competitor.md) | `ModifiedByID` |
| [Complex](Complex.md) | `ModifiedByID` |
| [ContractAmendment](ContractAmendment.md) | `ModifiedByID` |
| [ContractTerm](ContractTerm.md) | `ModifiedByID` |
| [Covenant](Covenant.md) | `ModifiedByID` |
| [DMA](DMA.md) | `ModifiedByID` |
| [DemographicReport](DemographicReport.md) | `ModifiedByID` |
| [DevelopmentPlan](DevelopmentPlan.md) | `ModifiedByID` |
| [EscalationIndex](EscalationIndex.md) | `ModifiedByID` |
| [ExpenseAllocation](ExpenseAllocation.md) | `ModifiedByID` |
| [ExpenseEscalation](ExpenseEscalation.md) | `ModifiedByID` |
| [ExpenseSchedule](ExpenseSchedule.md) | `ModifiedByID` |
| [ExpenseSetup](ExpenseSetup.md) | `ModifiedByID` |
| [Firm](Firm.md) | `ModifiedByID` |
| [FiscalPeriod](FiscalPeriod.md) | `ModifiedByID` |
| [Folder](Folder.md) | `ModifiedByID` |
| [Insurance](Insurance.md) | `ModifiedByID` |
| [Jurisdiction](Jurisdiction.md) | `ModifiedByID` |
| [KeyDate](KeyDate.md) | `ModifiedByID` |
| [LandPurchaseSummary](LandPurchaseSummary.md) | `ModifiedByID` |
| [LeaseInfo](LeaseInfo.md) | `ModifiedByID` |
| [LinkIssuePart](LinkIssuePart.md) | `ModifiedByID` |
| [LinkIssuePartOrder](LinkIssuePartOrder.md) | `ModifiedByID` |
| [LinkLandPurchaseInspection](LinkLandPurchaseInspection.md) | `ModifiedByID` |
| [LinkProjectEntityContact](LinkProjectEntityContact.md) | `ModifiedByID` |
| [LinkTaskByCodeMember](LinkTaskByCodeMember.md) | `ModifiedByID` |
| [NonMember](NonMember.md) | `ModifiedByID` |
| [Organization](Organization.md) | `ModifiedByID` |
| [Ownership](Ownership.md) | `ModifiedByID` |
| [ParcelAccess](ParcelAccess.md) | `ModifiedByID` |
| [Part](Part.md) | `ModifiedByID` |
| [PartPackage](PartPackage.md) | `ModifiedByID` |
| [PartPackageItem](PartPackageItem.md) | `ModifiedByID` |
| [Party](Party.md) | `ModifiedByID` |
| [PaymentReceipt](PaymentReceipt.md) | `ModifiedByID` |
| [PaymentTransaction](PaymentTransaction.md) | `ModifiedByID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `ModifiedByID` |
| [PercentageRent](PercentageRent.md) | `ModifiedByID` |
| [Person](Person.md) | `ModifiedByID` |
| [ProFormaBudget](ProFormaBudget.md) | `ModifiedByID` |
| [ProcessTimelineTemplate](ProcessTimelineTemplate.md) | `ModifiedByID` |
| [ProgramRevenueWeeks](ProgramRevenueWeeks.md) | `ModifiedByID` |
| [Responsibility](Responsibility.md) | `ModifiedByID` |
| [Sales](Sales.md) | `ModifiedByID` |
| [Security](Security.md) | `ModifiedByID` |
| [SecurityDeposit](SecurityDeposit.md) | `ModifiedByID` |
| [SiteSurvey](SiteSurvey.md) | `ModifiedByID` |
| [StateProvinceCountry](StateProvinceCountry.md) | `ModifiedByID` |
| [Usage](Usage.md) | `ModifiedByID` |
| [UseBasedRent](UseBasedRent.md) | `ModifiedByID` |
| [UserClassSecurity](UserClassSecurity.md) | `ModifiedByID` |
| [VariableRentOffset](VariableRentOffset.md) | `ModifiedByID` |
