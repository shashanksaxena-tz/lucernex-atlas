# EmployerSite — Data Fields

A specific site/location belonging to an Employer (useful when a vendor has multiple branch offices) — business unit and currency type per site. 20 Global fields under Company Items.

**Table Association:** `EmployerSite` &nbsp;·&nbsp; **Total fields:** 20 (Global: 20, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Employer Site |
| Business Unit | `BusinessUnit` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| City | `City` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| Country | `CountryID` | `sTYPE_COUNTRY` | Global | No | No |  | Company Items / Employer Site |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Company Items / Employer Site |
| Employer | `EmployerID` | `sTYPE_EMPLOYER` | Global | Yes | No |  | Company Items / Employer Site |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Company Items / Employer Site |
| Is Inactive? | `Inactive` | `sTYPE_CHECKBOX` | Global | Yes | No |  | Company Items / Employer Site |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Company Items / Employer Site |
| Phone | `Phone` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| Postal Code | `PostalCode` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| State | `StateProvinceCountryID` | `sTYPE_STATE_PROVINCE` | Global | No | No |  | Company Items / Employer Site |
| Street Address #1 | `StreetAddress1` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| Street Address #2 | `StreetAddress2` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| Street Address #3 | `StreetAddress3` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| Street Address #4 | `StreetAddress4` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| Vendor Site Code | `VendorSiteCode` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| Vendor Site ID | `VendorSiteID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Employer Site |
| Vendor Site Name | `VendorSiteName` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Employer Site |
| Vendor Site RecID | `EmployerSiteID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Employer Site |
