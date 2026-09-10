# Covenant — Data Fields

A lease covenant/compliance obligation (financial ratio tests, use restrictions, exclusivity clauses) tied to a Contract — covenant amount/area, category, and an associated document reference for the underlying clause. 45 fields (38 Global, 7 Firm) spanning Contract and Wizard groups, and one of the entities the user named as expected — the Firm extension here likely reflects tenant-specific covenant categories not in the base platform list.

**Table Association:** `Covenant` &nbsp;·&nbsp; **Total fields:** 45 (Global: 38, Firm: 7)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| ASC 842 Schedule | `CodeASC842ScheduleID` | `sCODE_ASC842_SCHEDULE` | Global | No | No |  | Contract / Covenant |
| Accounting Adjustment Type | `CodeAccountingAdjustmentTypeID` | `sCODE_ACCOUNTING_ADJUSTMENT_TYPE` | Global | No | No |  | Contract / Covenant |
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Covenant |
| Associated Document | `AssociatedDocumentID` | `sTYPE_DOCUMENT` | Global | No | No |  | Contract / Covenant |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Contract / Covenant |
| Buyout Amount | `Firm_BuyoutAmount` | `sTYPE_MONEY` | Firm | No | No |  | Contract / Covenant |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Covenant |
| Covenant Amount | `CovenantAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Covenant |
| Covenant Area | `CovenantArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Covenant |
| Covenant Category | `CodeCovenantCategoryID` | `sCODE_COVENANT_CATEGORY` | Global | No | No |  | Contract / Covenant |
| Covenant ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Covenant |
| Covenant Date | `CovenantDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Covenant |
| Covenant Group | `CodeCovenantGroupID` | `sCODE_COVENANT_GROUP` | Global | No | No |  | Contract / Covenant |
| Covenant Group/Type Name | `CovenantGroupTypeName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Covenant |
| Covenant RecID | `CovenantID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Covenant |
| Covenant Secondary Rent Schedule Allocation Percent | `SecondaryRentSchedAllocPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Covenant |
| Covenant Status | `CodeCovenantStatusID` | `sCODE_COVENANT_STATUS` | Global | No | No |  | Contract / Covenant |
| Covenant Template | `CodeCovenantTemplateID` | `sCODE_COVENANT_TEMPLATE` | Global | No | No |  | Contract / Covenant |
| Covenant Type | `CodeCovenantTypeID` | `sCODE_COVENANT_TYPE` | Global | No | No |  | Contract / Covenant |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Covenant |
| Document | `Firm_CovenantDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Covenant |
| Documents | `DocumentIDList` | `sTYPE_DOCUMENT_LIST` | Global | No | No |  | Contract / Covenant |
| Exists? | `ExistsFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Covenant |
| File Name | `BaseName` | `sTYPE_TEXT` | Global | No | No |  | Contract / Covenant |
| Folder | `FolderID` | `sTYPE_DOCUMENT` | Global | No | No |  | Contract / Covenant |
| Hold Amount in Rent Schedule Liability | `HoldAmountInSchedLiability` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Covenant |
| IFRS 16 Schedule | `CodeIFRS16ScheduleID` | `sCODE_IFRS16_SCHEDULE` | Global | No | No |  | Contract / Covenant |
| Line Number | `LineNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Covenant |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Covenant |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Covenant |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Covenant |
| Page Number | `PageNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Covenant |
| Paragraph Number | `ParagraphNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Covenant |
| Penalty | `Firm_Penalty` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Covenant |
| Portion Guaranteed By 3rd Party | `ThirdPartyRVGAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Covenant |
| Radius Amount | `Firm_RadiusAmount` | `sTYPE_NUMBER` | Firm | No | No |  | Contract / Covenant |
| Radius Unit | `Firm_RadiusUnit` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Covenant |
| Sales Threshold | `Firm_SalesThreshold` | `sTYPE_MONEY` | Firm | No | No |  | Contract / Covenant |
| Section Number | `SectionNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Covenant |
| Standard Language Version | `StandardLanguageVersion` | `sTYPE_TEXT` | Global | No | No |  | Contract / Covenant |
| Standard Language? | `StandardLanguageFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Covenant |
| Termination Right | `Firm_TerminationRight` | `sTYPE_CUSTOM_CODE_FIELD` | Firm | No | No |  | Contract / Covenant |
| Total Residual Value Guarantee | `TotalRVGAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Covenant |
| Add Covenant From Template | `AddCovenantFromTemplate` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Wizard / Contract Covenant Wizard |
| Contract Wizard Template | `ContractWizardTemplate` | `sTYPE_CONTRACT` | Global | No | No |  | Wizard / Contract Covenant Wizard |
