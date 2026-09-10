# ContractTerm — Data Fields

One renewal/extension term option on a lease — average rent per area unit and area-unit basis, linked to Amendment and Covenant, appearing under both Contract and Wizard (the guided lease-entry flow). 29 fields (26 Global, 3 Firm).

**Table Association:** `ContractTerm` &nbsp;·&nbsp; **Total fields:** 29 (Global: 26, Firm: 3)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Contract Term |
| Average Rent Per Area Unit | `AvgRentPerAreaUnit` | `sTYPE_MONEY` | Global | No | No |  | Contract / Contract Term |
| Building Area Unit | `CodeBuildingAreaUnitID` | `sCODE_BUILDING_AREA_UNIT` | Global | No | No |  | Contract / Contract Term |
| Client Number | `ClientNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Term |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Contract Term |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Contract Term |
| Coverage Period Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Term |
| Coverage Period End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Term |
| Description | `Description` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Term |
| Document | `Firm_TermDocument` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Contract Term |
| Include Term For Accruals? | `IncludeTermForAccruals` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Contract Term |
| Length | `LengthOfTerm` | `sTYPE_DATE_MATH_OPERATION` | Global | No | No |  | Contract / Contract Term |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Contract Term |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Contract Term |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Contract Term |
| Option Rent PSF | `Firm_OptionRentPSF` | `sTYPE_NUMBER_FRACTION2DIGITS` | Firm | No | No |  | Contract / Contract Term |
| Page | `Firm_TermPage` | `sTYPE_TEXT` | Firm | No | No |  | Contract / Contract Term |
| Payment Begin Date | `PaymentBeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Term |
| Payment End Date | `PaymentEndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Contract Term |
| Rentable Area | `RentableArea` | `sTYPE_AREA` | Global | No | No |  | Contract / Contract Term |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Contract Term |
| Term ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Contract Term |
| Term RecID | `ContractTermID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Contract Term |
| Term Status | `CodeTermStatusID` | `sCODE_TERM_STATUS` | Global | No | No |  | Contract / Contract Term |
| Term Type | `CodeTermTypeID` | `sCODE_TERM_TYPE` | Global | No | No |  | Contract / Contract Term |
| Generate Contract Terms | `GenerateContractTerms` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Wizard / Contract Terms Wizard |
| Length of the term (years) | `ContractTermWizard_TermLength` | `sTYPE_NUMBER` | Global | No | No |  | Wizard / Contract Terms Wizard |
| New Term Coverage Period Begin Date | `ContractTermWizard_TermCoverageBeginDate` | `sTYPE_DATE` | Global | No | No |  | Wizard / Contract Terms Wizard |
| Number of Options | `ContractTermWizard_OptionNumber` | `sTYPE_NUMBER` | Global | No | No |  | Wizard / Contract Terms Wizard |
