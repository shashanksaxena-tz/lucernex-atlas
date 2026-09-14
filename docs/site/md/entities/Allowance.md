# Allowance

*23 fields · module: Contracts & Leases · Postgres: `allowance`*

A tenant-improvement or other landlord allowance on a lease — allowance type/group classification and begin date. 21 fields (17 Global, 4 Firm) under Contract; one of the entities the user specifically named, and its Firm extension (Firm_AllowCostPSF per 005's representative examples) shows ASG tracks a cost-per-square-foot calculation the base platform doesn't.

Source: `data-fields/allowance.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Catalogued fields | 21 (17 global, 4 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### 5 tenant custom columns

**Observed.** This record carries 5 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 4 catalogued Firm-scope fields

**Observed.** Of 21 catalogued fields on this record, 4 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Contract Amendment ID | Global |  | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAllowanceGroupID` | Allowance Group | Dropdown (Allowance Group Code) | Global |  | Allowance Group Code |
| `CodeAllowanceTypeID` | Allowance Type | Dropdown (Allowance Type Code) | Global |  | Allowance Type Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Dropdown (Building Area Unit Code) | Global |  | Building Area Unit Code |
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `Firm_AllowanceCategory` |  | Dropdown (Custom Field) | — |  | Custom Field |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_AllowCostPSF` | Cost PSF | Currency | Firm |  |  |
| `TotalAmount` | Total Amount | Currency | Global |  |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AllowanceID` | Allowance RecID | Number | Global |  |  |
| `RentableArea` | Rentable Area | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Firm_AllowanceDocument` | Document | Text | Firm |  |  |
| `Firm_AllowancePage` | Page | Text | Firm |  |  |
| `Firm_LandlordAllowanceContact` |  | Text | — |  |  |
| `Notes` |  | Text | Global |  |  |
| `Section` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Allowance ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [AllowanceTransaction](AllowanceTransaction.md) | `AllowanceID` |
