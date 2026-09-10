# Person — Data Fields

An individual contact record (broker, attorney, property manager) distinct from Employer (the company) and Member (internal user) — billing rates, multiple email/phone slots, and job-title code linkage. 37 Global fields under Company Items.

**Table Association:** `Person` &nbsp;·&nbsp; **Total fields:** 37 (Global: 37, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Billing Rate #1 | `BillRate1` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Contacts |
| Billing Rate #2 | `BillRate2` | `sTYPE_MONEY` | Global | No | No |  | Company Items / Contacts |
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Contact Type List | `CodeContactTypeIDList` | `sTYPE_CODE_CONTACT_TYPE_LIST` | Global | Yes | No |  | Company Items / Contacts |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Company Items / Contacts |
| Description | `Description` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Contacts |
| Designations | `Designations` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Email #1 | `EMail1` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Email #2 | `EMail2` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Employer | `EmployerID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Company Items / Contacts |
| Fax | `Fax` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| First Name | `FirstName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Contacts |
| Is Inactive? | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Company Items / Contacts |
| Job Function | `CodeJobFunctionID` | `sCODE_JOB_FUNCTION` | Global | Yes | No |  | Company Items / Contacts |
| Job Title | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Contacts |
| Job Titles | `CodeJobTitleIDList` | `sCODE_JOB_TITLE` | Global | No | No |  | Company Items / Contacts |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | Company Items / Contacts |
| Last Name | `LastName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Contacts |
| Middle Name | `MiddleName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Mobile Number | `MobileNumber` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Contacts |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Contacts |
| Person ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Contacts |
| Person RecID | `PersonID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Contacts |
| Phone | `Phone` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Phone Extension | `PhoneExtension` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | Company Items / Contacts |
| State | `IStateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Company Items / Contacts |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Suffix | `Suffix` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Title | `Title` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Use Employer Address | `UseEmployerAddress` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Company Items / Contacts |
| Website | `WebSite` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
| Wireless Email | `WirelessEMail` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Contacts |
