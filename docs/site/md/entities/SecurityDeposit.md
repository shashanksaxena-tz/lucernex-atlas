# SecurityDeposit

*25 fields · module: Contracts & Leases · Postgres: `security_deposit`*

Security/damage deposit tracking on a lease — deposit amount, account number, and Covenant linkage for deposits tied to compliance conditions. 25 fields (24 Global, 1 Firm) under Contract.

Source: `data-fields/security-deposit.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 25 |
| Catalogued fields | 25 (24 global, 1 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 1 catalogued Firm-scope fields

**Observed.** Of 25 catalogued fields on this record, 1 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `PartyID` | Party | Employer ID | Global |  | [Employer](Employer.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Deposit Currency | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeGuaranteeTypeID` | Guarantee Type | Dropdown (Guarantee Type Code) | Global |  | Guarantee Type Code |
| `CodePayBackCurrencyTypeID` | Return Deposit Currency | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeSecurityDepositGroupID` | Security Deposit Group | Dropdown (Security Deposit Group Code) | Global |  | Security Deposit Group Code |
| `CodeSecurityDepositStatusID` | Security Deposit Status | Dropdown (Security Deposit Status Code) | Global |  | Security Deposit Status Code |
| `CodeSecurityDepositTypeID` | Security Deposit Type | Dropdown (Security Deposit Type Code) | Global |  | Security Deposit Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DepositAmount` | Deposit Amount | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `InterestRate` | Interest Rate | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SecurityDepositID` | Security Deposit RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `InterestBearingFlag` | Interest Bearing? | Boolean | Global |  |  |
| `RequiredFlag` | Required? | Boolean | Global |  |  |
| `SeparateAccountFlag` | Separate Account? | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccountNumber` | Account Number | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Security Deposit ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
