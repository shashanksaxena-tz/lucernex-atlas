# SecurityDeposit — Data Fields

Security/damage deposit tracking on a lease — deposit amount, account number, and Covenant linkage for deposits tied to compliance conditions. 25 fields (24 Global, 1 Firm) under Contract.

**Table Association:** `SecurityDeposit` &nbsp;·&nbsp; **Total fields:** 25 (Global: 24, Firm: 1)

Field type codes (the `sTYPE_*`/`sCODE_*` values below) are decoded once, for the whole dataset, in the [field type legend](INDEX.md#field-type-legend) in INDEX.md. Full inventory: [INDEX.md](INDEX.md).

| Label | Internal Name | Field Type | Scope | Required | Read-Only | Default | Notes (Group / Subgroup) |
|---|---|---|---|---|---|---|---|
| Account Number | `AccountNumber` | `sTYPE_TEXT` | Global | No | No |  | Contract / Security Deposit |
| Amendment | `AmendmentID` | `sTYPE_CONTRACT_AMENDMENT` | Global | No | No |  | Contract / Security Deposit |
| Begin Date | `BeginDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Security Deposit |
| Burn Down Date | `Firm_SecurityBurnDownDate` | `sTYPE_DATE` | Firm | No | No |  | Contract / Security Deposit |
| Contract | `ContractID` | `sTYPE_CONTRACT` | Global | Yes | No |  | Contract / Security Deposit |
| Covenant | `CovenantID` | `sTYPE_COVENANT` | Global | No | No |  | Contract / Security Deposit |
| Deposit Amount | `DepositAmount` | `sTYPE_MONEY` | Global | No | No |  | Contract / Security Deposit |
| Deposit Currency | `CodeCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Security Deposit |
| End Date | `EndDate` | `sTYPE_DATE` | Global | No | No |  | Contract / Security Deposit |
| Guarantee Type | `CodeGuaranteeTypeID` | `sCODE_GUARANTEE_TYPE` | Global | No | No |  | Contract / Security Deposit |
| Interest Bearing? | `InterestBearingFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Security Deposit |
| Interest Rate | `InterestRate` | `sTYPE_PERCENTAGE` | Global | No | No |  | Contract / Security Deposit |
| Modified By | `ModifiedByID` | `sTYPE_MEMBER` | Global | No | No |  | Contract / Security Deposit |
| Modified Date | `ModifiedDate` | `sTYPE_TIME` | Global | No | No |  | Contract / Security Deposit |
| Notes | `Notes` | `sTYPE_TEXTAREA` | Global | No | No |  | Contract / Security Deposit |
| Party | `PartyID` | `sTYPE_EMPLOYER` | Global | No | No |  | Contract / Security Deposit |
| Required? | `RequiredFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Security Deposit |
| Return Deposit Currency | `CodePayBackCurrencyTypeID` | `sCODE_CURRENCY_TYPE` | Global | No | No |  | Contract / Security Deposit |
| Section | `Section` | `sTYPE_TEXT` | Global | No | No |  | Contract / Security Deposit |
| Security Deposit ClientID | `BOMapClientRecordID` | `sTYPE_TEXT` | Global | Yes | No |  | Contract / Security Deposit |
| Security Deposit Group | `CodeSecurityDepositGroupID` | `sCODE_SECURITY_DEPOSIT_GROUP` | Global | No | No |  | Contract / Security Deposit |
| Security Deposit RecID | `SecurityDepositID` | `sTYPE_UNFORMATTED_NUMBER` | Global | No | No |  | Contract / Security Deposit |
| Security Deposit Status | `CodeSecurityDepositStatusID` | `sCODE_SECURITY_DEPOSIT_STATUS` | Global | No | No |  | Contract / Security Deposit |
| Security Deposit Type | `CodeSecurityDepositTypeID` | `sCODE_SECURITY_DEPOSIT_TYPE` | Global | No | No |  | Contract / Security Deposit |
| Separate Account? | `SeparateAccountFlag` | `sTYPE_CHECKBOX` | Global | No | No |  | Contract / Security Deposit |
