# Link & Relationship Tables

These 19 tables (108 fields total, all Global) all carry the `Link*` naming prefix and exist purely to join two other entities together — a many-to-many association with at most a few descriptive columns (an amount, a date, a flag) riding along on the join. None reaches the 15-field standalone threshold individually because a join table's job is structural, not descriptive: it doesn't need to hold much data of its own once it's wired the two sides together. Grouping them here keeps the INDEX legible while still giving every one of them a real row and a real field table.

**Entities in this file:** 19 &nbsp;·&nbsp; **Total fields:** 108 (Global: 108, Firm: 0)

| Entity | Fields (G/F) | One-line role |
|---|---|---|
| `LinkLandlordInvPaymentTxn` | 13 (13/0) | Join table linking a LandlordInvoiceItem to the PaymentTransaction that paid it — allocation amount and date. |
| `LinkProjectEntityContact` | 13 (13/0) | Join table linking a ProjectEntity to a contact person with a contact-type classification. |
| `LinkReceiptTransaction` | 11 (11/0) | Join table linking a PaymentReceipt to the transaction(s) it was allocated against. |
| `LinkSchedOffsetExpGrpType` | 11 (11/0) | Join table linking a ScheduledOffset to the expense group/type it applies to. |
| `LinkLandPurchaseInspection` | 8 (8/0) | Join table linking a LandPurchaseSummary to a due-diligence inspection — type, duration, and scheduled date. |
| `LinkRegionManager` | 8 (8/0) | Join table assigning a Member as manager of a Region, with a manager flag and operating-status inheritance. |
| `LinkTaskByCodeMember` | 7 (7/0) | Join table assigning a Task to a Member by job title/org-chart level rather than by name. |
| `LinkRegionMarket` | 7 (7/0) | Join table linking a Region to a market area and its assigned market manager. |
| `LinkTaskMember` | 5 (5/0) | Join table assigning a specific Member to a specific Task on a ProjectEntity. |
| `LinkProjectEntityVendor` | 4 (4/0) | Join table linking a ProjectEntity (portfolio) to an approved Vendor. |
| `LinkBudgetViewBLI` | 4 (4/0) | Join table associating a BudgetLineItem with a BudgetView. |
| `LinkEMailReceivedLogDocument` | 4 (4/0) | Join table linking a received email log entry to a saved Document (e.g., an email attachment filed to the record). |
| `LinkSecurity` | 3 (3/0) | Join table applying a security setting to a Folder for a given user class. |
| `LinkPEMemberCodeJobTitle` | 2 (2/0) | Join table linking a ProjectEntity member assignment to a job-title code — internal ID-only fields with no exposed labels. |
| `LinkEmpAvailableJobFunction` | 2 (2/0) | Join table controlling which job functions are available/selectable for a given Employer. |
| `LinkEmpAvailableJobTitle` | 2 (2/0) | Join table controlling which job titles are available/selectable for a given Employer. |
| `LinkEmpAvailableUserClass` | 2 (2/0) | Join table controlling which security user classes are available/selectable for a given Employer. |
| `LinkBudgetIndexBLI` | 1 (1/0) | Join table associating a BudgetLineItem with a BudgetIndex escalator — a single internal RecID field only. |
| `LinkCommPkgTemplDocContent` | 1 (1/0) | Join table linking a committee-package template to its document content — a single internal RecID field only. |

Field type codes are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Entity | Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|---|
| LinkLandlordInvPaymentTxn | Allocation Amount | `AllocationAmount` | `sTYPE_MONEY` | Global | Yes | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Allocation Date | `AllocationDate` | `sTYPE_DATE` | Global | Yes | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Landlord Invoice Item | `LandlordInvoiceItemID` | `sTYPE_LANDLORD_INVOICE_ITEM` | Global | Yes | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Notes | `Notes` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Payment Transaction | `PaymentTransactionID` | `sTYPE_PAYMENT_TRANSACTION` | Global | Yes | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Project Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Reconciliation Status | `ReconciliationStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Variance Amount | `VarianceAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Landlord Invoice Association |
| LinkLandlordInvPaymentTxn | Variance Reason | `VarianceReason` | `sTYPE_TEXT` | Global | No | No |  | Contract / Landlord Invoice Association |
| LinkProjectEntityContact | Link Project Entity Contact RecID | `LinkProjectEntityContactID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| LinkProjectEntityContact | Contact Type | `CodeContactTypeID` | `sCODE_CONTACT_TYPE` | Global | Yes | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Employer | `EmployerID` | `sTYPE_EMPLOYER` | Global | No | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Inactive | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Is Primary? | `IsPrimary` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Landlord (Employer) | `Landlord_EmployerID` | `sTYPE_EMPLOYER` | Global | No | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Landlord (Person) | `Landlord_PersonID` | `sTYPE_PERSON` | Global | No | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Person | `PersonID` | `sTYPE_PERSON` | Global | No | No |  | Summary Information / Contacts |
| LinkProjectEntityContact | Rating | `Rating` | `sTYPE_NUMBER` | Global | No | No |  | Summary Information / Contacts |
| LinkReceiptTransaction | Allocation Amount | `AllocationAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Link Receipt Transaction ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Link Receipt Transaction RecID | `LinkReceiptTransactionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Payment Receipt | `PaymentReceiptID` | `sTYPE_PAYMENT_RECEIPT` | Global | Yes | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Payment Transaction | `PaymentTransactionID` | `sTYPE_PAYMENT_TRANSACTION` | Global | Yes | No |  | Contract / Receipt Transaction Association |
| LinkReceiptTransaction | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Receipt Transaction Association |
| LinkSchedOffsetExpGrpType | Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Expense Group | `CodeExpenseGroupID` | `sCODE_EXPENSE_GROUP` | Global | No | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Expense Type | `CodeExpenseTypeID` | `sCODE_EXPENSE_TYPE` | Global | No | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Scheduled Offset | `ScheduledOffsetID` | `sTYPE_SCHEDULED_OFFSET` | Global | Yes | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Scheduled Offset Expense Type ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Scheduled Offset Expense Types |
| LinkSchedOffsetExpGrpType | Scheduled Offset Expense Type RecID | `LinkSchedOffsetExpGrpTypeID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Scheduled Offset Expense Types |
| LinkLandPurchaseInspection | Comments | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Purchase Management / Inspections |
| LinkLandPurchaseInspection | Inspection Duration | `InspectionDays` | `sTYPE_NUMBER` | Global | Yes | No |  | Purchase Management / Inspections |
| LinkLandPurchaseInspection | Inspection To Begin | `CodeInspectionPeriodStartID` | `sCODE_INSPECTION_PERIOD_START` | Global | Yes | No |  | Purchase Management / Inspections |
| LinkLandPurchaseInspection | Inspection Type | `CodeInspectionTypeID` | `sCODE_INSPECTION_TYPE` | Global | Yes | No |  | Purchase Management / Inspections |
| LinkLandPurchaseInspection | Land Purchase Summary | `LandPurchaseSummaryID` | `sTYPE_LAND_PURCHASE_SUMMARY` | Global | Yes | No |  | Purchase Management / Inspections |
| LinkLandPurchaseInspection | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Purchase Management / Inspections |
| LinkLandPurchaseInspection | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Purchase Management / Inspections |
| LinkLandPurchaseInspection | Link Land Purchase Inspection RecID | `LinkLandPurchaseInspectionID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| LinkRegionManager | Link Region Manager ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| LinkRegionManager | Link Region Manager Is Manager? | `IsManager` | `sTYPE_BOOLEAN` | Global | Yes | No |  | Statics / Hidden |
| LinkRegionManager | Link Region Manager Member | `MemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Statics / Hidden |
| LinkRegionManager | Link Region Manager Operating Status | `OperatingStatus` | `sTYPE_OPERATING_STATUS` | Global | Yes | No |  | Statics / Hidden |
| LinkRegionManager | Link Region Manager Portfolio or Capital Program | `ProgramID` | `sTYPE_PROGRAM` | Global | Yes | No |  | Statics / Hidden |
| LinkRegionManager | Link Region Manager RecID | `LinkRegionManagerID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| LinkRegionManager | Link Region Manager Region | `RegionID` | `sTYPE_REGION` | Global | No | No |  | Statics / Hidden |
| LinkRegionManager | Link Region Market RecID | `LinkRegionMarketID` | `sTYPE_LINK_REGION_MARKET` | Global | No | No |  | Statics / Hidden |
| LinkTaskByCodeMember | Job Title | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | Schedule / Template Auto-Assignment |
| LinkTaskByCodeMember | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Schedule / Template Auto-Assignment |
| LinkTaskByCodeMember | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Schedule / Template Auto-Assignment |
| LinkTaskByCodeMember | Org Chart Level | `OrgChartLevel` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Schedule / Template Auto-Assignment |
| LinkTaskByCodeMember | Task | `TaskID` | `sTYPE_TASK` | Global | Yes | No |  | Schedule / Template Auto-Assignment |
| LinkTaskByCodeMember | Template Auto-Assignmen ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Schedule / Template Auto-Assignment |
| LinkTaskByCodeMember | Template Auto-Assignment RecID | `LinkTaskByCodeMemberID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Schedule / Template Auto-Assignment |
| LinkRegionMarket | Market Area | `CodeMarketAreaID` | `sCODE_MARKET_AREA` | Global | Yes | No |  | Statics / Hidden |
| LinkRegionMarket | Market Manager Names | `ManagerIDList` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| LinkRegionMarket | Market Member Names | `MemberIDList` | `sTYPE_MEMBER` | Global | No | No |  | Statics / Hidden |
| LinkRegionMarket | OrgChart Operating Status | `OperatingStatus` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| LinkRegionMarket | Portfolio Project Entity ID | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Statics / Hidden |
| LinkRegionMarket | Previous Region Market | `PreviousLinkRegionMarketID` | `sTYPE_LINK_REGION_MARKET` | Global | No | No |  | Statics / Hidden |
| LinkRegionMarket | Related Region | `RegionID` | `sTYPE_REGION` | Global | Yes | No |  | Statics / Hidden |
| LinkTaskMember | Member | `MemberID` | `sTYPE_MEMBER` | Global | Yes | No |  | Schedule / Task Member |
| LinkTaskMember | Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Schedule / Task Member |
| LinkTaskMember | Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Schedule / Task Member |
| LinkTaskMember | Project Entity | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Schedule / Task Member |
| LinkTaskMember | Task | `TaskID` | `sTYPE_TASK` | Global | Yes | No |  | Schedule / Task Member |
| LinkProjectEntityVendor | Link Portfolio Vendor ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Employer Portfolio |
| LinkProjectEntityVendor | Link Portfolio Vendor RecID | `LinkProjectEntityVendorID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Employer Portfolio |
| LinkProjectEntityVendor | Porfolio | `ProjectEntityID` | `sTYPE_PROJECT_ENTITY` | Global | Yes | No |  | Company Items / Employer Portfolio |
| LinkProjectEntityVendor | Vendor | `VendorID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Company Items / Employer Portfolio |
| LinkBudgetViewBLI | Budget Line Item | `BudgetLineItemID` | `sTYPE_BUDGET_LINE_ITEM` | Global | No | No |  | Statics / Hidden |
| LinkBudgetViewBLI | Budget View | `BudgetViewID` | `sTYPE_BUDGET_VIEW` | Global | Yes | No |  | Statics / Hidden |
| LinkBudgetViewBLI | Link Budget View BLI ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Statics / Hidden |
| LinkBudgetViewBLI | Link Budget View BLI RecID | `LinkBudgetViewBLIID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| LinkEMailReceivedLogDocument | Document | `DocumentID` | `sTYPE_DOCUMENT` | Global | No | No |  | Summary Information / In-bound Email |
| LinkEMailReceivedLogDocument | E Mail Rcvd Log | `EMailReceivedLogID` | `sTYPE_EMAIL_RECEIVED_LOG` | Global | Yes | No |  | Summary Information / In-bound Email |
| LinkEMailReceivedLogDocument | E-Mail Rcvd Doc ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Summary Information / In-bound Email |
| LinkEMailReceivedLogDocument | E-Mail Rcvd Doc RecID | `LinkEMailReceivedLogDocumentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Summary Information / In-bound Email |
| LinkSecurity | Folder | `FolderID` | `sTYPE_FOLDER` | Global | No | No |  | Documents / Folder Security |
| LinkSecurity | Security Setting | `CodeFolderSecurityTypeID` | `sCODE_SECURITY_TYPE` | Global | No | No |  | Documents / Folder Security |
| LinkSecurity | User Class | `CodeUserClassID` | `sCODE_USER_CLASS` | Global | Yes | No |  | Documents / Folder Security |
| LinkPEMemberCodeJobTitle | CodeJobTitleID | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | Yes | No |  | Statics / Hidden |
| LinkPEMemberCodeJobTitle | LinkMemberPEID | `LinkMemberPEID` | `sTYPE_PE_MEMBER` | Global | Yes | No |  | Statics / Hidden |
| LinkEmpAvailableJobFunction | EmpAvailableCodeJobFunctionID | `CodeJobFunctionID` | `sCODE_JOB_FUNCTION` | Global | Yes | No |  | Statics / Hidden |
| LinkEmpAvailableJobFunction | JobFunctionEmployerID | `EmployerID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Statics / Hidden |
| LinkEmpAvailableJobTitle | EmpAvailableCodeJobTitleID | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | Yes | No |  | Statics / Hidden |
| LinkEmpAvailableJobTitle | JobTitleEmployerID | `EmployerID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Statics / Hidden |
| LinkEmpAvailableUserClass | EmpAvailableCodeUserClassID | `CodeUserClassID` | `sCODE_USER_CLASS` | Global | Yes | No |  | Statics / Hidden |
| LinkEmpAvailableUserClass | UserClassEmployerID | `EmployerID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Statics / Hidden |
| LinkBudgetIndexBLI | Link Budget Index BLI RecID | `LinkBudgetIndexBLIID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
| LinkCommPkgTemplDocContent | Link Comm Pkg Templ Doc Content RecID | `LinkCommPkgTemplDocContentID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Statics / Hidden |
