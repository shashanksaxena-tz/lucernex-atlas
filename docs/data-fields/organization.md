# Organization — Data Fields

A broader organizational entity (parent company, franchise group) above Employer — up to several numbered Account Number slots mirroring the financial entities' split-coding pattern. 17 Global fields under Company Items.

**Table Association:** `Organization` &nbsp;·&nbsp; **Total fields:** 17 (Global: 17, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Account Number #1 | `AccountNumber1` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Organization |
| Account Number #2 | `AccountNumber2` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Organization |
| Account Number #3 | `AccountNumber3` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Organization |
| Account Number #4 | `AccountNumber4` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Organization |
| Account Number #5 | `AccountNumber5` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Organization |
| Account Number #6 | `AccountNumber6` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Organization |
| Account Number #7 | `AccountNumber7` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Organization |
| Account Number #8 | `AccountNumber8` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Organization |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Organization |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Organization |
| Organization Category | `CodeOrganizationCategoryID` | `sCODE_ORG_CATEGORY` | Global | No | No |  | Company Items / Organization |
| Organization ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Organization |
| Organization Group | `CodeOrganizationGroupID` | `sCODE_ORG_GROUP` | Global | No | No |  | Company Items / Organization |
| Organization Name | `OrganizationName` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Organization |
| Organization RecID | `OrganizationID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Company Items / Organization |
| Organization Type | `CodeOrganizationTypeID` | `sCODE_ORG_TYPE` | Global | No | No |  | Company Items / Organization |
| Portfolio Access | `PortfolioIDList` | `sTYPE_PORTFOLIO_LIST` | Global | No | No |  | Company Items / Organization |
