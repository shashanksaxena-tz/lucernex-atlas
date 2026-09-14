# ContractAmendment

*20 fields · module: Contracts & Leases · Postgres: `contract_amendment`*

A formal amendment/modification to an executed lease — amendment group/number/type classification and base-amount change. 19 fields (17 Global, 2 Firm) under Contract.

Source: `data-fields/contract-amendment.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Catalogued fields | 19 (17 global, 2 firm) |
| Physical tables | 1 |
| Referenced by | 13 keys from 13 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### 2 tenant custom columns

**Observed.** This record carries 2 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 2 catalogued Firm-scope fields

**Observed.** Of 19 catalogued fields on this record, 2 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentIDList` | Documents | Document List | Global |  |  |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAmendmentGroupID` | Amendment Group | Dropdown (Amendment Group Code) | Global |  | Amendment Group Code |
| `CodeAmendmentTypeID` | Amendment Type | Dropdown (Amendment Type Code) | Global |  | Amendment Type Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeContractUseID` | Contract Use | Dropdown (Contract Use Code) | Global |  | Contract Use Code |
| `CodeFrequencyID` | Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaseAmountChange` | Base Amount Change | Currency | Global |  |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractAmendmentID` | Amendment RecID | Number | Global |  |  |
| `RentableAreaChange` | Rentable Area Change | Number | Global |  |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `Firm_AmendmentEntryDate` | Entry Date | Date | Firm |  |  |
| `Firm_AmendmentExecutionDate` | Execution Date | Date | Firm |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentNumber` | Amendment Number | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Contract Amendment ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (13 keys)

| Record type | Via column |
|---|---|
| [Allowance](Allowance.md) | `AmendmentID` |
| [CoTenancy](CoTenancy.md) | `AmendmentID` |
| [ContractTerm](ContractTerm.md) | `AmendmentID` |
| [Covenant](Covenant.md) | `AmendmentID` |
| [ExpenseAccrualSetup](ExpenseAccrualSetup.md) | `AmendmentID` |
| [ExpenseRecovery](ExpenseRecovery.md) | `AmendmentID` |
| [ExpenseSetup](ExpenseSetup.md) | `AmendmentID` |
| [Insurance](Insurance.md) | `AmendmentID` |
| [PercentageRent](PercentageRent.md) | `AmendmentID` |
| [Responsibility](Responsibility.md) | `AmendmentID` |
| [Scenario](Scenario.md) | `AmendmentID` |
| [SecurityDeposit](SecurityDeposit.md) | `AmendmentID` |
| [UseBasedRent](UseBasedRent.md) | `AmendmentID` |
