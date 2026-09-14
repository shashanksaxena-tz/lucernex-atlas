# Employer

*71 fields · module: People & Parties · Postgres: `employer`*

The vendor/landlord/tenant company record — banking details (Bank Account Number, Bank Routing Number), AP vendor number, and document-access permission flags (Allow Employees Upload/Download access to Employer Documents). 71 fields (66 Global, 5 Firm) under Company Items; this is the counterparty master record referenced by Contract, PaymentTransaction, and most financial entities whenever a payee or lessor needs to be identified.

Source: `data-fields/employer.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 71 |
| Catalogued fields | 71 (66 global, 5 firm) |
| Physical tables | 1 |
| Referenced by | 40 keys from 30 record types |
| Points at | 3 other records |
| Tenancy position | firm_global |
| Rules that name it | 5 |

## What to know before rebuilding this

### 5 tenant custom columns

**Observed.** This record carries 5 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### 5 catalogued Firm-scope fields

**Observed.** Of 71 catalogued fields on this record, 5 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

### A hub: 40 keys point here

**Observed.** 30 record types hold a foreign key into this one, so it sits at the centre of the relationship graph. Changing its key or its identity is a change to Asset, BidPackage, BidderIssue, BudgetColumn and 26 others.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-021](../rules/CON-R-021.md) | Resolving a 'Vendor': VendorID's declared type is Employer ID — Vendor is a relabelled Employer, not a distinct entity. | Observed |
| [PPL-R-002](../rules/PPL-R-002.md) | No `Person ID` FK type exists anywhere in the 60-odd declared FK types | Inferred |
| [PPL-R-004](../rules/PPL-R-004.md) | No `Vendor`, `Landlord`, or `Tenant`-as-counterparty object exists in the 223-object schema | Observed |
| [PPL-R-005](../rules/PPL-R-005.md) | Both `CompanyID` and `ContactID` are independently nullable | Derived |
| [AST-R-010](../rules/AST-R-010.md) | Input: `AlternateVendorID`, `InstallerVendorID`, `ManufacturerVendorID`, `PrimaryVendorID`, `SecondaryVendorID`, `SupplierVendorID`, `WarrantyVendorID` — all typed `Employer ID`. Effect: Seven distinct roles against the same company table,  | Observed |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IStateProvinceCountryID` | State | Country, State, County ID | Global |  | [StateProvinceCountry](StateProvinceCountry.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccountRepPersonID` | Account Rep | Contact | Global |  |  |
| `CompanyType` | Company Type | Dropdown | Global | yes |  |

### Coded values (drop-downs) (9)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAssetCategoryIDList` | Maintenance Categories | Dropdown (Asset Category Code) | Global |  | Asset Category Code |
| `CodeContactTypeIDList` | Contact Type List | Dropdown (Contact Type Code) | Global | yes | Contact Type Code |
| `CodeCoverageID` | Coverage | Dropdown (Coverage Code) | Global |  | Coverage Code |
| `CodeMasterEmployerGroupID` | Master Employer Group | Dropdown (Master Employer Group Code) | Global |  | Master Employer Group Code |
| `CodeVendorGradeID` | Vendor Grade | Dropdown (Vendor Grade Code) | Global |  | Vendor Grade Code |
| `EmpAvailableJobFunctionIDList` | Job Functions | Dropdown (Job Function Code) | Global |  | Job Function Code |
| `EmpAvailableJobTitleIDList` | Job Titles | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `EmpAvailableUserClassIDList` | User Classes | Dropdown (User Class) | Global |  | User Class |
| `Firm_PaymentMethod` | Payment Method | Dropdown (Custom Field) | Firm |  | Custom Field |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AfterHoursRate` | After Hours Rate | Currency | Global |  |  |
| `HourlyRate` | Hourly Rate | Currency | Global |  |  |
| `TravelRate` | Travel Rate | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `VendorEarlyPayDiscount` | Early Pay Discount | Percentage | Global |  |  |

### Quantities (6)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EmployerID` | Employer RecID | Number | Global |  |  |
| `NumberOfServiceTrucks` | Number of Service Trucks | Number | Global |  |  |
| `NumberOfStates` | Number of States | Number | Global |  |  |
| `NumberOfTechnicians` | Number of Technicians | Number | Global |  |  |
| `VendorEarlyPayDays` | Early Pay Days | Number | Global |  |  |
| `VendorNetPayDays` | Net Pay Days | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DateGraded` | Date Graded | Date | Global |  |  |

### Flags (13)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HasAfterHoursSupport` | Has After Hours Support? | Boolean | Global |  |  |
| `Inactive` | Is Inactive? | Boolean | Global | yes |  |
| `IsEquipContractVendor` | Is Equip Contract Vendor? | Boolean | Global |  |  |
| `IsFemaleOwned` | Is Female Owned? | Boolean | Global |  |  |
| `IsGLBTOwned` | Is GLBT Owned? | Boolean | Global |  |  |
| `IsMinorityOwned` | Is Minority Owned? | Boolean | Global |  |  |
| `IsPreferredVendor` | Is Preferred Vendor? | Boolean | Global |  |  |
| `IsPrimaryOwner` | Is Primary Owner? | Boolean | Global |  |  |
| `IsREContractVendor` | Is RE Contract Vendor? | Boolean | Global |  |  |
| `IsSBAProgram` | Is SBA Program? | Boolean | Global |  |  |
| `IsSharedDocumentAccess` | Allow Employees Upload / Download access to Employer Documents | Boolean | Global |  |  |
| `IsVendor` | Is Vendor? | Boolean | Global |  |  |
| `SelfPerform` | Self Perform? | Boolean | Global |  |  |

### Text & notes (29)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `APVendorNumber` | AP Vendor Number | Text | Global |  |  |
| `AfterHoursContact` | After Hours Contact | Text | Global |  |  |
| `BankAccountNumber` | Bank Account Number | Text | Global |  |  |
| `BankRoutingNumber` | Bank Routing Number | Text | Global |  |  |
| `BusinessHours` | Business Hours | Text | Global |  |  |
| `City` |  | Text | Global |  |  |
| `CompanyInformation` | Company Information | Text | Global |  |  |
| `CountryID` | Country | Text | Global |  |  |
| `Department` |  | Text | Global |  |  |
| `EMail1` | Email #1 | Text | Global |  |  |
| `EMail2` | Email #2 | Text | Global |  |  |
| `EmployerName` | Employer Name | Text | Global | yes |  |
| `Fax` |  | Text | Global |  |  |
| `FederalTaxID` | Federal Tax ID | Text | Global |  |  |
| `Firm_AlternatePayee` | Alternate Payee | Text | Firm |  |  |
| `Firm_EmployerAttention` | Attention | Text | Firm |  |  |
| `Firm_EmployerCareof` | Care of | Text | Firm |  |  |
| `Firm_EmployerStoreNumber` | Store Number | Text | Firm |  |  |
| `MobileNumber` | Mobile Number | Text | Global |  |  |
| `NameAKA` | AKA Name | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `Phone` |  | Text | Global |  |  |
| `PortfolioIDList` | Portfolio Access | Text | Global |  |  |
| `PostalCode` | Postal Code | Text | Global |  |  |
| `StreetAddress1` | Street Address #1 | Text | Global |  |  |
| `StreetAddress2` | Street Address #2 | Text | Global |  |  |
| `StreetAddress3` | Street Address #3 | Text | Global |  |  |
| `StreetAddress4` | Street Address #4 | Text | Global |  |  |
| `WebSite` | Website | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Employer ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (40 keys)

| Record type | Via column |
|---|---|
| [Asset](Asset.md) | `AlternateVendorID`, `InstallerVendorID`, `ManufacturerVendorID`, `PrimaryVendorID`, `SecondaryVendorID`, `SupplierVendorID`, `WarrantyVendorID` |
| [WorkOrder](WorkOrder.md) | `AlternateVendorID`, `PrimaryVendorID`, `SecondaryVendorID` |
| [LinkProjectEntityContact](LinkProjectEntityContact.md) | `EmployerID`, `Landlord_EmployerID` |
| [PropertyTaxSummary](PropertyTaxSummary.md) | `TaxAuthorityID`, `VendorID` |
| [BidPackage](BidPackage.md) | `WinningBidVendorID` |
| [BidderIssue](BidderIssue.md) | `UniqueVendorID` |
| [BudgetColumn](BudgetColumn.md) | `ThirdPartyVendorID` |
| [CLRExtensionPart](CLRExtensionPart.md) | `SalesVendorID` |
| [ClientListRow](ClientListRow.md) | `SalesVendorID` |
| [EmployerSite](EmployerSite.md) | `EmployerID` |
| [ExpenseSetup](ExpenseSetup.md) | `VendorID` |
| [ExpenseVendorAllocation](ExpenseVendorAllocation.md) | `VendorID` |
| [Issue](Issue.md) | `VendorID` |
| [LandlordInvoice](LandlordInvoice.md) | `EmployerID` |
| [LinkIssuePartOrder](LinkIssuePartOrder.md) | `VendorID` |
| [LinkProjectEntityVendor](LinkProjectEntityVendor.md) | `VendorID` |
| [Member](Member.md) | `EmployerID` |
| [NonMember](NonMember.md) | `EmployerID` |
| [Part](Part.md) | `VendorID` |
| [PartPackage](PartPackage.md) | `VendorID` |
| [Party](Party.md) | `CompanyID` |
| [PaymentTransaction](PaymentTransaction.md) | `VendorID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `VendorID` |
| [Person](Person.md) | `EmployerID` |
| [PropertyTaxAppealAward](PropertyTaxAppealAward.md) | `VendorID` |
| [PropertyTaxAssessment](PropertyTaxAssessment.md) | `AppraiserID` |
| [ScheduledOffset](ScheduledOffset.md) | `VendorID` |
| [SecurityDeposit](SecurityDeposit.md) | `PartyID` |
| [Tenant](Tenant.md) | `CompanyID` |
| [VendorInsurance](VendorInsurance.md) | `VendorID` |
