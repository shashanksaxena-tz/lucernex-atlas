# Employer

*71 fields · module: People & Parties · Postgres: `employer`*

The vendor/landlord/tenant company record — banking details (Bank Account Number, Bank Routing Number), AP vendor number, and document-access permission flags (Allow Employees Upload/Download access to Employer Documents). 71 fields (66 Global, 5 Firm) under Company Items; this is the counterparty master record referenced by Contract, PaymentTransaction, and most financial entities whenever a payee or lessor needs to be identified.

Source: `data-fields/employer.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 71 |
| Fields with a vendor definition | 63 of 71 inventoried |
| Physical tables | `employer` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in employer

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 63 fields carry a vendor definition

**Observed.** 63 of this record's 71 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 71 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 5 are marked required.

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

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IStateProvinceCountryID` | State | Select the state or province from this field. | Country, State, County ID | Global |  | `employer.IStateProvinceCountryID · TEXT` | [StateProvinceCountry](StateProvinceCountry.md) |

### Soft references (2)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccountRepPersonID` | Account Rep | Select the account representative from this field. | Contact | Global |  | `employer.AccountRepPersonID · TEXT` |  |
| `CompanyType` | Company Type | Select the company type from this field. If this employer is a company that will be paid, you MUST select Vendor from this field. | Dropdown | Global | yes | `employer.CompanyType · TEXT` |  |

### Coded values (drop-downs) (9)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAssetCategoryIDList` | Maintenance Categories | Select the maintenance categories this company belongs to from the multi-select field. | Dropdown (Asset Category Code) | Global |  | `employer.CodeAssetCategoryIDList · TEXT` | Asset Category Code |
| `CodeContactTypeIDList` | Contact Type List | Select the contact type of the company from the multi-select field. | Dropdown (Contact Type Code) | Global | yes | `employer.CodeContactTypeIDList · TEXT` | Contact Type Code |
| `CodeCoverageID` | Coverage | Select the level of coverage this company provides from this field. | Dropdown (Coverage Code) | Global |  | `employer.CodeCoverageID · TEXT` | Coverage Code |
| `CodeMasterEmployerGroupID` | Master Employer Group | If this company has a parent company, select the parent company from this field. | Dropdown (Master Employer Group Code) | Global |  | `employer.CodeMasterEmployerGroupID · TEXT` | Master Employer Group Code |
| `CodeVendorGradeID` | Vendor Grade | Select the vendor rating from this field. | Dropdown (Vendor Grade Code) | Global |  | `employer.CodeVendorGradeID · TEXT` | Vendor Grade Code |
| `EmpAvailableJobFunctionIDList` | Job Functions | This field allows you to select which job functions are allowed for employees of this employer. | Dropdown (Job Function Code) | Global |  | `employer.EmpAvailableJobFunctionIDList · TEXT` | Job Function Code |
| `EmpAvailableJobTitleIDList` | Job Titles | This field allows you to select which job titles are allowed for employees of this employer. | Dropdown (Job Title Code) | Global |  | `employer.EmpAvailableJobTitleIDList · TEXT` | Job Title Code |
| `EmpAvailableUserClassIDList` | User Classes | This field allows you to select which user classes are allowed for employees of this employer. | Dropdown (User Class) | Global |  | `employer.EmpAvailableUserClassIDList · TEXT` | User Class |
| `Firm_PaymentMethod` | Payment Method |  | Dropdown (Custom Field) | Firm |  | `employer.Firm_PaymentMethod · TEXT` | Custom Field |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AfterHoursRate` | After Hours Rate | Enter the company's after-hours rate in this field. | Currency | Global |  | `employer.AfterHoursRate · TEXT` |  |
| `HourlyRate` | Hourly Rate | Enter the company's hourly rate in this field. | Currency | Global |  | `employer.HourlyRate · TEXT` |  |
| `TravelRate` | Travel Rate | Enter the company's travel rate in this field. | Currency | Global |  | `employer.TravelRate · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `VendorEarlyPayDiscount` | Early Pay Discount |  | Percentage | Global |  | `employer.VendorEarlyPayDiscount · TEXT` |  |

### Quantities (6)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EmployerID` | Employer RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `employer.EmployerID · VARCHAR(64) NOT NULL` |  |
| `NumberOfServiceTrucks` | Number of Service Trucks | Enter the number of service trucks this company utilizes in this field. | Number | Global |  | `employer.NumberOfServiceTrucks · TEXT` |  |
| `NumberOfStates` | Number of States | Enter the number of states the company services in this field. | Number | Global |  | `employer.NumberOfStates · TEXT` |  |
| `NumberOfTechnicians` | Number of Technicians | Enter the number of technicians this company has in this field. | Number | Global |  | `employer.NumberOfTechnicians · TEXT` |  |
| `VendorEarlyPayDays` | Early Pay Days |  | Number | Global |  | `employer.VendorEarlyPayDays · TEXT` |  |
| `VendorNetPayDays` | Net Pay Days |  | Number | Global |  | `employer.VendorNetPayDays · TEXT` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DateGraded` | Date Graded | The date that the employer was assigned a vendor rating. | Date | Global |  | `employer.DateGraded · TEXT` |  |

### Flags (13)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HasAfterHoursSupport` | Has After Hours Support? | Select this check box if this company has after-hours support. | Boolean | Global |  | `employer.HasAfterHoursSupport · TEXT` |  |
| `Inactive` | Is Inactive? | If this value is true, the record is inactive. If this value is false, the record is active. | Boolean | Global | yes | `employer.Inactive · TEXT` |  |
| `IsEquipContractVendor` | Is Equip Contract Vendor? | Select this check box if this company is an equipment contract vendor. | Boolean | Global |  | `employer.IsEquipContractVendor · TEXT` |  |
| `IsFemaleOwned` | Is Female Owned? | Select this check box if this company is female owned. | Boolean | Global |  | `employer.IsFemaleOwned · TEXT` |  |
| `IsGLBTOwned` | Is GLBT Owned? | Select this check box if this company is LGBT owned. | Boolean | Global |  | `employer.IsGLBTOwned · TEXT` |  |
| `IsMinorityOwned` | Is Minority Owned? | Select this check box if this company is Minority owned. | Boolean | Global |  | `employer.IsMinorityOwned · TEXT` |  |
| `IsPreferredVendor` | Is Preferred Vendor? | Select this check box if this is a preferred vendor. | Boolean | Global |  | `employer.IsPreferredVendor · TEXT` |  |
| `IsPrimaryOwner` | Is Primary Owner? | Select this check box if this company is a primary owner. | Boolean | Global |  | `employer.IsPrimaryOwner · TEXT` |  |
| `IsREContractVendor` | Is RE Contract Vendor? | Select this check box if this company is a real estate contract vendor. | Boolean | Global |  | `employer.IsREContractVendor · TEXT` |  |
| `IsSBAProgram` | Is SBA Program? | Select this check box if this company is an SBA program. SBA stands for the US Small Business Administration. | Boolean | Global |  | `employer.IsSBAProgram · TEXT` |  |
| `IsSharedDocumentAccess` | Allow Employees Upload / Download access to Employer Documents | This field is a placeholder for an upcoming feature. | Boolean | Global |  | `employer.IsSharedDocumentAccess · TEXT` |  |
| `IsVendor` | Is Vendor? | If this value is true, the employer is a vendor. If this value is false, the employer is not a vendor. | Boolean | Global |  | `employer.IsVendor · TEXT` |  |
| `SelfPerform` | Self Perform? | Select this check box if this company performs work themselves rather than hiring third-party assistance. | Boolean | Global |  | `employer.SelfPerform · TEXT` |  |

### Text & notes (29)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `APVendorNumber` | AP Vendor Number | Enter the company's AP Vendor number in this field. The AP Vendor number is referenced when you send payments to your accounts payable system. | Text | Global |  | `employer.APVendorNumber · TEXT` |  |
| `AfterHoursContact` | After Hours Contact | Enter the contact information of the company's after-hours contact in this field. | Text | Global |  | `employer.AfterHoursContact · TEXT` |  |
| `BankAccountNumber` | Bank Account Number | Enter the company's bank account number in this field. | Text | Global |  | `employer.BankAccountNumber · TEXT` |  |
| `BankRoutingNumber` | Bank Routing Number | Enter the company's bank routing number in this field. | Text | Global |  | `employer.BankRoutingNumber · TEXT` |  |
| `BusinessHours` | Business Hours | Enter the business hours of the company in this field. | Text | Global |  | `employer.BusinessHours · TEXT` |  |
| `City` |  | The city associated with this record. | Text | Global |  | `employer.City · TEXT` |  |
| `CompanyInformation` | Company Information | Enter any additional information about the company in this field. | Text | Global |  | `employer.CompanyInformation · TEXT` |  |
| `CountryID` | Country | Select the country where this company is located from this field. | Text | Global |  | `employer.CountryID · TEXT` |  |
| `Department` |  | Enter the company department in this field. | Text | Global |  | `employer.Department · TEXT` |  |
| `EMail1` | Email #1 | Enter the company's primary email address in this field. | Text | Global |  | `employer.EMail1 · TEXT` |  |
| `EMail2` | Email #2 | Enter the company's secondary email address in this field. | Text | Global |  | `employer.EMail2 · TEXT` |  |
| `EmployerName` | Employer Name | Enter the company's name in this field. | Text | Global | yes | `employer.EmployerName · TEXT` |  |
| `Fax` |  | Enter the company's fax number in this field. | Text | Global |  | `employer.Fax · TEXT` |  |
| `FederalTaxID` | Federal Tax ID | Enter the company's federal tax ID number in this field. | Text | Global |  | `employer.FederalTaxID · TEXT` |  |
| `Firm_AlternatePayee` | Alternate Payee |  | Text | Firm |  | `employer.Firm_AlternatePayee · TEXT` |  |
| `Firm_EmployerAttention` | Attention |  | Text | Firm |  | `employer.Firm_EmployerAttention · TEXT` |  |
| `Firm_EmployerCareof` | Care of |  | Text | Firm |  | `employer.Firm_EmployerCareof · TEXT` |  |
| `Firm_EmployerStoreNumber` | Store Number |  | Text | Firm |  | `employer.Firm_EmployerStoreNumber · TEXT` |  |
| `MobileNumber` | Mobile Number | Enter the mobile phone number in this field. | Text | Global |  | `employer.MobileNumber · TEXT` |  |
| `NameAKA` | AKA Name | If the company has another name, enter the name in this field. | Text | Global |  | `employer.NameAKA · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `employer.Notes · TEXT` |  |
| `Phone` |  | Enter the company's phone number in this field. | Text | Global |  | `employer.Phone · TEXT` |  |
| `PortfolioIDList` | Portfolio Access | This field contains a list of the portfolios that are associated with a given employer. It is used to filter vendor records based on the current porfolio. | Text | Global |  | `employer.PortfolioIDList · TEXT` |  |
| `PostalCode` | Postal Code | Enter the company's postal code in this field. | Text | Global |  | `employer.PostalCode · TEXT` |  |
| `StreetAddress1` | Street Address #1 | The first line of the street address. | Text | Global |  | `employer.StreetAddress1 · TEXT` |  |
| `StreetAddress2` | Street Address #2 | The second line of the street address. | Text | Global |  | `employer.StreetAddress2 · TEXT` |  |
| `StreetAddress3` | Street Address #3 | The third line of the street address. | Text | Global |  | `employer.StreetAddress3 · TEXT` |  |
| `StreetAddress4` | Street Address #4 | The fourth line of the street address. | Text | Global |  | `employer.StreetAddress4 · TEXT` |  |
| `WebSite` | Website | Enter the company's website in this field. | Text | Global |  | `employer.WebSite · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Employer ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `employer.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `employer.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `employer.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `employer.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `employer.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `employer.RevNumber · TEXT` |  |

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
