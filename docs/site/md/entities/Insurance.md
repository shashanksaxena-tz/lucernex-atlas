# Insurance

*27 fields · module: Contracts & Leases · Postgres: `insurance`*

Required insurance coverage terms on a lease — certificate received/request dates, required flag, and whether the agent is also the named insured. 26 Global fields under Contract, anchoring VendorInsurance as the actual policy-level detail.

Source: `data-fields/insurance.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 27 |
| Catalogued fields | 26 (26 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContactID` | Contact | Contact | Global |  |  |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeInsuranceCategoryID` | Insurance Category | Dropdown (Insurance Category Code) | Global |  | Insurance Category Code |
| `CodeInsuranceGroupID` | Insurance Group | Dropdown (Insurance Group Code) | Global |  | Insurance Group Code |
| `CodeInsuranceTypeID` | Insurance Type | Dropdown (Insurance Type Code) | Global |  | Insurance Type Code |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CoverageAmount` | Coverage Amount | Currency | Global |  |  |
| `SingleOccuranceAmount` | Single Occurance Amount | Currency | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `InsuranceID` | Insurance RecID | Number | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `CertificateReceivedDate` | Certificate Received Date | Date | Global |  |  |
| `CertificateRequestDate` | Certificate Request Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AgentAlsoNamedInsuredFlag` | Agent Also Named Insured? | Boolean | Global |  |  |
| `CertificateRequiredFlag` | Certificate Required? | Boolean | Global |  |  |
| `LandlordAlsoNamedInsuredFlag` | Landlord Also Named Insured? | Boolean | Global |  |  |
| `PolicyRequiredFlag` | Policy Required? | Boolean | Global |  |  |
| `SelfInsuredFlag` | Self Insured? | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Notes` |  | Text | Global |  |  |
| `PolicyNumber` | Policy Number | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Insurance ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
