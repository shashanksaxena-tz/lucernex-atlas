# ReTransScenContact — Data Fields

Contact record specific to a real-estate transaction scenario (distinct from LinkReTransScenContact, the join-style variant) — contact type, employer name, email. 28 Global fields under RE Transaction.

**Table Association:** `ReTransScenContact` &nbsp;·&nbsp; **Total fields:** 28 (Global: 28, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Contact Type | `CodeContactTypeID` | `sCODE_CONTACT_TYPE` | Global | No | No |  | RE Transaction / Contact |
| Created By | `CreatedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / Contact |
| Created Date | `CreatedDate` | `sTYPE_TIME` | Global | No | No |  | RE Transaction / Contact |
| E Mail #1 | `EMail1` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Employer Name | `EmployerName` | `sTYPE_TEXTAREA` | Global | Yes | No |  | RE Transaction / Contact |
| First Name | `FirstName` | `sTYPE_TEXT` | Global | Yes | No |  | RE Transaction / Contact |
| Job Function | `CodeJobFunctionID` | `sCODE_JOB_FUNCTION` | Global | No | No |  | RE Transaction / Contact |
| Job Title | `CodeJobTitleID` | `sCODE_JOB_TITLE` | Global | No | No |  | RE Transaction / Contact |
| Jurisdiction | `JurisdictionID` | `sTYPE_JURISDICTION` | Global | No | No |  | RE Transaction / Contact |
| Last Name | `LastName` | `sTYPE_TEXT` | Global | Yes | No |  | RE Transaction / Contact |
| Middle Name | `MiddleName` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Mobile Number | `MobileNumber` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | RE Transaction / Contact |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | RE Transaction / Contact |
| Name (First Last) | `NameFirstLast` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Name (Last First) | `NameLastFirst` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | RE Transaction / Contact |
| Phone | `Phone` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Postal Code | `PostalCode` | `sTYPE_POSTALCODE` | Global | No | No |  | RE Transaction / Contact |
| RE Trans Scen Contact ID | `ReTransScenContactID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | RE Transaction / Contact |
| State Province Country | `StateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | RE Transaction / Contact |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Suffix | `Suffix` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
| Title | `Title` | `sTYPE_TEXT` | Global | No | No |  | RE Transaction / Contact |
