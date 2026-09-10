# Employer — Data Fields

The vendor/landlord/tenant company record — banking details (Bank Account Number, Bank Routing Number), AP vendor number, and document-access permission flags (Allow Employees Upload/Download access to Employer Documents). 71 fields (66 Global, 5 Firm) under Company Items; this is the counterparty master record referenced by Contract, PaymentTransaction, and most financial entities whenever a payee or lessor needs to be identified.

**Table Association:** `Employer` &nbsp;·&nbsp; **Total fields:** 71 (Global: 66, Firm: 5)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| AKA Name | `NameAKA` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| AP Vendor Number | `APVendorNumber` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Account Rep | `AccountRepPersonID` | `sTYPE_PERSON` | Global | No | No |  | Company Items / Employers |
| After Hours Contact | `AfterHoursContact` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Employers |
| After Hours Rate | `AfterHoursRate` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Employers |
| Allow Employees Upload / Download access to Employer Documents | `IsSharedDocumentAccess` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Alternate Payee | `Firm_AlternatePayee` | `sTYPE_TEXT` | Firm | No | No |  | Company Items / Employers |
| Attention | `Firm_EmployerAttention` | `sTYPE_TEXT` | Firm | No | No |  | Company Items / Employers |
| Bank Account Number | `BankAccountNumber` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Bank Routing Number | `BankRoutingNumber` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Business Hours | `BusinessHours` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Employers |
| Care of | `Firm_EmployerCareof` | `sTYPE_TEXT` | Firm | No | No |  | Company Items / Employers |
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Company Information | `CompanyInformation` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Employers |
| Company Type | `CompanyType` | `sTYPE_COMPANY_TYPE` | Global | Yes | No |  | Company Items / Employers |
| Contact Type List | `CodeContactTypeIDList` | `sTYPE_CODE_CONTACT_TYPE_LIST` | Global | Yes | No |  | Company Items / Employers |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Company Items / Employers |
| Coverage | `CodeCoverageID` | `sCODE_COVERAGE` | Global | No | No |  | Company Items / Employers |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Employers |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Employers |
| Date Graded | `DateGraded` | `sTYPE_DATE` | Global | No | No |  | Company Items / Employers |
| Department | `Department` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Early Pay Days | `VendorEarlyPayDays` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Employers |
| Early Pay Discount | `VendorEarlyPayDiscount` | `sTYPE_PERCENTAGE` | Global | No | No |  | Company Items / Employers |
| Email #1 | `EMail1` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Email #2 | `EMail2` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Employer ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Employers |
| Employer Name | `EmployerName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Employers |
| Employer RecID | `EmployerID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Employers |
| Fax | `Fax` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Federal Tax ID | `FederalTaxID` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Has After Hours Support? | `HasAfterHoursSupport` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Hourly Rate | `HourlyRate` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Employers |
| Is Equip Contract Vendor? | `IsEquipContractVendor` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Is Female Owned? | `IsFemaleOwned` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Is GLBT Owned? | `IsGLBTOwned` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Is Inactive? | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Company Items / Employers |
| Is Minority Owned? | `IsMinorityOwned` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Is Preferred Vendor? | `IsPreferredVendor` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Is Primary Owner? | `IsPrimaryOwner` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Is RE Contract Vendor? | `IsREContractVendor` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Is SBA Program? | `IsSBAProgram` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Is Vendor? | `IsVendor` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| Job Functions | `EmpAvailableJobFunctionIDList` | `sTYPE_EMP_JOB_FUNCTION_LIST` | Global | No | No |  | Company Items / Employers |
| Job Titles | `EmpAvailableJobTitleIDList` | `sTYPE_EMP_JOB_TITLE_LIST` | Global | No | No |  | Company Items / Employers |
| Maintenance Categories | `CodeAssetCategoryIDList` | `sTYPE_CODE_ASSET_CATEGORY_LIST` | Global | No | No |  | Company Items / Employers |
| Master Employer Group | `CodeMasterEmployerGroupID` | `sCODE_MASTER_EMPLOYER_GROUP` | Global | No | No |  | Company Items / Employers |
| Mobile Number | `MobileNumber` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Employers |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Employers |
| Net Pay Days | `VendorNetPayDays` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Employers |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Employers |
| Number of Service Trucks | `NumberOfServiceTrucks` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Employers |
| Number of States | `NumberOfStates` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Employers |
| Number of Technicians | `NumberOfTechnicians` | `sTYPE_NUMBER` | Global | No | No |  | Company Items / Employers |
| Payment Method | `Firm_PaymentMethod` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Company Items / Employers |
| Phone | `Phone` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Portfolio Access | `PortfolioIDList` | `sTYPE_PORTFOLIO_LIST` | Global | No | No |  | Company Items / Employers |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Company Items / Employers |
| Rev Number | `RevNumber` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Employers |
| Self Perform? | `SelfPerform` | `sTYPE_CHECKBOX` | Global | No | No |  | Company Items / Employers |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Company Items / Employers |
| Store Number | `Firm_EmployerStoreNumber` | `sTYPE_TEXT` | Firm | No | No |  | Company Items / Employers |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
| Travel Rate | `TravelRate` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Employers |
| User Classes | `EmpAvailableUserClassIDList` | `sTYPE_EMP_USER_CLASS_LIST` | Global | No | No |  | Company Items / Employers |
| Vendor Grade | `CodeVendorGradeID` | `sCODE_VENDOR_GRADE` | Global | No | No |  | Company Items / Employers |
| Website | `WebSite` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employers |
