# Responsibility — Data Fields

Defines which party (landlord/tenant) is responsible for a cost category on a lease, with cap amount/percent limits — the allocation-of-obligation record that ExpenseRecovery and FinancialAdjustment calculations reference. 33 Global fields under Contract and Wizard.

**Table Association:** `Responsibility` &nbsp;·&nbsp; **Total fields:** 33 (Global: 33, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Responsibility |
| Cap Amount | `CapAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Responsibility |
| Cap Percent | `CapPercent` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Responsibility |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Responsibility |
| Contract Responsibility Amount | `ContractResponsibilityAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Responsibility |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Responsibility |
| Effective Date | `EffectiveDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Responsibility |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Responsibility |
| Included In Rent? | `IncludedInRentFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Responsibility |
| Maintenance Category | `CodeAssetCategoryID` | `sCODE_ASSET_CATEGORY` | Global | No | No |  | Contract / Responsibility |
| Maintenance Contact | `MaintenancePersonID` | `sTYPE_PERSON` | Global | No | No |  | Contract / Responsibility |
| Maintenance Responsibility | `CodeMaintenanceResponsibilityID` | `sCODE_RESPONSIBLE_PARTY` | Global | No | No |  | Contract / Responsibility |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Responsibility |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Responsibility |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Responsibility |
| Pass Through Type | `CodePassThroughTypeID` | `sCODE_PASS_THROUGH_TYPE` | Global | No | No |  | Contract / Responsibility |
| Photos | `Photos` | `sTYPE_PHOTO` | Global | No | No |  | Contract / Responsibility |
| Repairs Contact | `ExecutionPersonID` | `sTYPE_PERSON` | Global | No | No |  | Contract / Responsibility |
| Repairs Responsibility | `CodeExecutionResponsibilityID` | `sCODE_RESPONSIBLE_PARTY` | Global | No | No |  | Contract / Responsibility |
| Replace Contact | `FinancialPersonID` | `sTYPE_PERSON` | Global | No | No |  | Contract / Responsibility |
| Replace Responsibility | `CodeFinancialResponsibilityID` | `sCODE_RESPONSIBLE_PARTY` | Global | No | No |  | Contract / Responsibility |
| Response Time | `CodeResponseTimeID` | `sCODE_RESPONSE_TIME` | Global | No | No |  | Contract / Responsibility |
| Responsibility ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Responsibility |
| Responsibility Group | `CodeResponsibilityGroupID` | `sCODE_RESPONSIBILITY_GROUP` | Global | No | No |  | Contract / Responsibility |
| Responsibility RecID | `ResponsibilityID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Responsibility |
| Responsibility Type | `CodeResponsibilityTypeID` | `sCODE_RESPONSIBILITY_TYPE` | Global | No | No |  | Contract / Responsibility |
| Responsible Party | `ResponsibilePartyVal` | `sTYPE_TEXT` | Global | No | No |  | Contract / Responsibility |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Responsibility |
| Service Contact | `ServicePersonID` | `sTYPE_PERSON` | Global | No | No |  | Contract / Responsibility |
| Service Level | `ServiceLevel` | `sTYPE_TEXT` | Global | No | No |  | Contract / Responsibility |
| Service Responsibility | `CodeServiceResponsibilityID` | `sCODE_RESPONSIBLE_PARTY` | Global | No | No |  | Contract / Responsibility |
| Add Responsibility From Template | `AddResponsibilityFromTemplate` | `sTYPE_SUBMITBUTTON` | Global | No | No |  | Wizard / Contract Responsibility Wizard |
| Contract Wizard Template | `ContractWizardTemplate` | `sTYPE_CONTRACT` | Global | No | No |  | Wizard / Contract Responsibility Wizard |
