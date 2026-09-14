# SecurityDeposit

*25 fields · module: Contracts & Leases · Postgres: `security_deposit`*

Security/damage deposit tracking on a lease — deposit amount, account number, and Covenant linkage for deposits tied to compliance conditions. 25 fields (24 Global, 1 Firm) under Contract.

Source: `data-fields/security-deposit.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 25 |
| Fields with a vendor definition | 24 of 26 inventoried |
| Physical tables | `security_deposit` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in security_deposit

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 24 fields carry a vendor definition

**Observed.** 24 of this record's 26 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 25 comparable

**Observed.** Over the 25 fields both captures contain, they agree on 24. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-020](../rules/CON-R-020.md) | Resolving a contract's vendors: Contract has no vendor FK; the set is derived from PaymentTransaction.VendorID, ExpenseSetup.VendorID, ExpenseVendorAllocation.VendorID, ScheduledOffset.VendorID, LandlordInvoice.EmployerID and SecurityDeposi | Derived |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `security_deposit.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `security_deposit.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `security_deposit.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `PartyID` | Party | Select the legal party who is associated with the security deposit from this field. | Employer ID | Global |  | `security_deposit.PartyID · TEXT` | [Employer](Employer.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `security_deposit.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (6)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Deposit Currency | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `security_deposit.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeGuaranteeTypeID` | Guarantee Type | Select how the security deposit funds are guaranteed from this field. | Dropdown (Guarantee Type Code) | Global |  | `security_deposit.CodeGuaranteeTypeID · TEXT` | Guarantee Type Code |
| `CodePayBackCurrencyTypeID` | Return Deposit Currency | Select the currency the security deposit will be returned in from this field. | Dropdown (Currency Type Code) | Global |  | `security_deposit.CodePayBackCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeSecurityDepositGroupID` | Security Deposit Group | The security deposit group is the first level of categorization for security deposit records. Groups are the parents of types. | Dropdown (Security Deposit Group Code) | Global |  | `security_deposit.CodeSecurityDepositGroupID · TEXT` | Security Deposit Group Code |
| `CodeSecurityDepositStatusID` | Security Deposit Status | Select the status of the security deposit from this field. | Dropdown (Security Deposit Status Code) | Global |  | `security_deposit.CodeSecurityDepositStatusID · TEXT` | Security Deposit Status Code |
| `CodeSecurityDepositTypeID` | Security Deposit Type | The security deposit type is the second level of categorization for security deposit records. Types are the children of groups. | Dropdown (Security Deposit Type Code) | Global |  | `security_deposit.CodeSecurityDepositTypeID · TEXT` | Security Deposit Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DepositAmount` | Deposit Amount | Enter the deposit total in this field. | Currency | Global |  | `security_deposit.DepositAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `InterestRate` | Interest Rate | Enter the interest rate for the account that is holding the security deposit in this field. | Percentage | Global |  | `security_deposit.InterestRate · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SecurityDepositID` | Security Deposit RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `security_deposit.SecurityDepositID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `security_deposit.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `security_deposit.EndDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `InterestBearingFlag` | Interest Bearing? | Select this check box if the account where the security deposit is being held is interest-bearing. | Boolean | Global |  | `security_deposit.InterestBearingFlag · TEXT` |  |
| `RequiredFlag` | Required? | Select this check box if the security deposit was required. | Boolean | Global |  | `security_deposit.RequiredFlag · TEXT` |  |
| `SeparateAccountFlag` | Separate Account? | Select this check box if the security deposit is being held in a escrow account. | Boolean | Global |  | `security_deposit.SeparateAccountFlag · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccountNumber` | Account Number | Enter the account number of the account where the security deposit is held in this field. | Text | Global |  | `security_deposit.AccountNumber · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `security_deposit.Notes · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `security_deposit.Section · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Security Deposit ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `security_deposit.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `security_deposit.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `security_deposit.ModifiedDate · TEXT` |  |
