# Firm — Data Fields

The tenant-company configuration record — one row per Lucernex client firm, holding default page-layout assignments per module (Facility Setup Page, Equipment Contract Setup Page) and default folder security. 24 fields (23 Global, 1 Firm) spanning Company Items, Statics, and Summary Information; this is the master firm-level settings record, not to be confused with the 'Firm' scope of this whole catalog.

**Table Association:** `Firm` &nbsp;·&nbsp; **Total fields:** 24 (Global: 23, Firm: 1)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Capital Program Setup Page | `CapProgramSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| Capital Project Setup Page | `CapProjectSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| Default Folder Security | `CodeDefaultFolderSecurityID` | `sCODE_SECURITY_TYPE` | Global | Yes | No |  | Company Items / Summary |
| Equipment Contract Setup Page | `EquipmentContractSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| Facility Setup Page | `FacilitySetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| From Email | `FromEmailAddress` | `sTYPE_TEXT` | Global | Yes | No |  | Company Items / Summary |
| JSON Configuration | `JSONConfigText` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Summary |
| Location Setup Page | `LocationSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Company Items / Summary |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Company Items / Summary |
| Opening Project Setup Page | `OpenProjectSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| Parcel Setup Page | `ParcelSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| Portfolio Setup Page | `PortfolioSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| Prototype Setup Page | `PrototypeSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| RE Contract Setup Page | `ContractSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| Service Channel FirmID | `SvcChannelFirmID` | `sTYPE_TEXT` | Global | No | No |  | Company Items / Summary |
| Site Setup Page | `SiteSetupPageLayoutID` | `sTYPE_PAGE_LAYOUT` | Global | No | No |  | Company Items / Summary |
| DB Document Storage GB | `DBDocumentStorageGB` | `sTYPE_NUMBER_FRACTION2DIGITS` | Global | No | No |  | Statics / Hidden |
| Document Storage Used Percent | `DocumentStorageUsedPercent` | `sTYPE_PERCENTAGE_2DIGITS` | Global | No | No |  | Statics / Hidden |
| Enable Generate Rent Date (Equipment) | `EnableGenRentEquipDate` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| Enable Generate Rent Date (Real Estate) | `EnableGenRentREDate` | `sTYPE_DATE` | Global | No | No |  | Statics / Hidden |
| Max Document Storage GB | `MaxDocumentStorageGB` | `sTYPE_NUMBER_FRACTION2DIGITS` | Global | No | No |  | Statics / Hidden |
| Header Logo | `Firm_HeaderLogo` | `sTYPE_FIRM_LOGO` | Firm | No | No |  | Summary Information / General Summary Information |
| Current Date | `CurrentDate` | `sTYPE_CURRENT_DATE` | Global | No | No |  | Summary Information / Summary Dates |
