# Responsibility

*32 fields · module: Contracts & Leases · Postgres: `responsibility`*

Defines which party (landlord/tenant) is responsible for a cost category on a lease, with cap amount/percent limits — the allocation-of-obligation record that ExpenseRecovery and FinancialAdjustment calculations reference. 33 Global fields under Contract and Wizard.

Source: `data-fields/responsibility.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 32 |
| Catalogued fields | 33 (33 global, 0 firm) |
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

### Soft references (4)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExecutionPersonID` | Repairs Contact | Contact | Global |  |  |
| `FinancialPersonID` | Replace Contact | Contact | Global |  |  |
| `MaintenancePersonID` | Maintenance Contact | Contact | Global |  |  |
| `ServicePersonID` | Service Contact | Contact | Global |  |  |

### Coded values (drop-downs) (9)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAssetCategoryID` | Maintenance Category | Dropdown (Asset Category Code) | Global |  | Asset Category Code |
| `CodeExecutionResponsibilityID` | Repairs Responsibility | Dropdown (Responsible Party) | Global |  | Responsible Party |
| `CodeFinancialResponsibilityID` | Replace Responsibility | Dropdown (Responsible Party) | Global |  | Responsible Party |
| `CodeMaintenanceResponsibilityID` | Maintenance Responsibility | Dropdown (Responsible Party) | Global |  | Responsible Party |
| `CodePassThroughTypeID` | Pass Through Type | Dropdown (Pass Through Type Code) | Global |  | Pass Through Type Code |
| `CodeResponseTimeID` | Response Time | Dropdown (Response Time Code) | Global |  | Response Time Code |
| `CodeResponsibilityGroupID` | Responsibility Group | Dropdown (Responsibility Group Code) | Global |  | Responsibility Group Code |
| `CodeResponsibilityTypeID` | Responsibility Type | Dropdown (Responsibility Type Code) | Global |  | Responsibility Type Code |
| `CodeServiceResponsibilityID` | Service Responsibility | Dropdown (Responsible Party) | Global |  | Responsible Party |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapAmount` | Cap Amount | Currency | Global |  |  |
| `ContractResponsibilityAmount` | Contract Responsibility Amount | Currency | Global |  |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CapPercent` | Cap Percent | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ResponsibilityID` | Responsibility RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IncludedInRentFlag` | Included In Rent? | Boolean | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Notes` |  | Text | Global |  |  |
| `Photos` |  | Text | Global |  |  |
| `ResponsibilePartyVal` | Responsible Party | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |
| `ServiceLevel` | Service Level | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Responsibility ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
