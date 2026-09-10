# LinkReTransScenContact — Data Fields

A join record linking a real-estate transaction Scenario to a contact (broker, attorney) with contact-type classification and email. 32 Global fields under RE Transaction — despite the Link-style name, at 32 fields it is treated as standalone rather than folded into the small Link bucket.

**Table Association:** `LinkReTransScenContact` &nbsp;·&nbsp; **Total fields:** 32 (Global: 32, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Company Contact | `PersonID` | `sTYPE_PERSON` | Global | No | No |  | RE Transaction / Contact List |
| Contact Type | `CodeContactTypeIDList` | `sCODE_CONTACT_TYPE` | Global | No | No |  | RE Transaction / Contact List |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / Contact List |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | RE Transaction / Contact List |
| E Mail #1 | `EMail1` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Employer Name | `EmployerName` | `sTYPE_TEXTAREA` | Global | No | No |  | RE Transaction / Contact List |
| First Name | `FirstName` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Job Function | `ICodeJobFunctionID` | `sCODE_JOB_FUNCTION` | Global | No | No |  | RE Transaction / Contact List |
| Job Title | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | RE Transaction / Contact List |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | RE Transaction / Contact List |
| Last Name | `LastName` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Middle Name | `MiddleName` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Mobile Number | `MobileNumber` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / Contact List |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | RE Transaction / Contact List |
| Name (First Last) | `NameFirstLast` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Name (Last First) | `NameLastFirst` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Phone | `Phone` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | RE Transaction / Contact List |
| RE Transaction | `RETransactionID` | `sTYPE_RE_TRANSACTION` | Global | No | No |  | RE Transaction / Contact List |
| RE Transaction Contact | `ReTransScenContactID` | `sTYPE_RETRAN_CONTACT` | Global | No | No |  | RE Transaction / Contact List |
| RE Transaction Scenario Contact ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | RE Transaction / Contact List |
| RE Transaction Scenario Contact RecID | `LinkReTransScenContactID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Transaction / Contact List |
| Scenario | `ScenarioID` | `sTYPE_SCENARIO` | Global | No | No |  | RE Transaction / Contact List |
| State Province Country | `StateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | RE Transaction / Contact List |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Suffix | `Suffix` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
| Title | `Title` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact List |
