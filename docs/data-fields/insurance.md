# Insurance — Data Fields

Required insurance coverage terms on a lease — certificate received/request dates, required flag, and whether the agent is also the named insured. 26 Global fields under Contract, anchoring VendorInsurance as the actual policy-level detail.

**Table Association:** `Insurance` &nbsp;·&nbsp; **Total fields:** 26 (Global: 26, Firm: 0)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Agent Also Named Insured? | `AgentAlsoNamedInsuredFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Insurance |
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Insurance |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Insurance |
| Certificate Received Date | `CertificateReceivedDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Insurance |
| Certificate Request Date | `CertificateRequestDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Insurance |
| Certificate Required? | `CertificateRequiredFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Insurance |
| Contact | `ContactID` | `sTYPE_PERSON` | Global | No | No |  | Contract / Insurance |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Insurance |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Insurance |
| Coverage Amount | `CoverageAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Insurance |
| Currency Type | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Insurance |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Insurance |
| Insurance Category | `CodeInsuranceCategoryID` | `sCODE_INSURANCE_CATEGORY` | Global | No | No |  | Contract / Insurance |
| Insurance ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Insurance |
| Insurance Group | `CodeInsuranceGroupID` | `sCODE_INSURANCE_GROUP` | Global | No | No |  | Contract / Insurance |
| Insurance RecID | `InsuranceID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Insurance |
| Insurance Type | `CodeInsuranceTypeID` | `sCODE_INSURANCE_TYPE` | Global | No | No |  | Contract / Insurance |
| Landlord Also Named Insured? | `LandlordAlsoNamedInsuredFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Insurance |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Insurance |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Insurance |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Insurance |
| Policy Number | `PolicyNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Insurance |
| Policy Required? | `PolicyRequiredFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Insurance |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Insurance |
| Self Insured? | `SelfInsuredFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Insurance |
| Single Occurance Amount | `SingleOccuranceAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Insurance |
