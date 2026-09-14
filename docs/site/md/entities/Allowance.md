# Allowance

*23 fields · module: Contracts & Leases · Postgres: `allowance`*

A tenant-improvement or other landlord allowance on a lease — allowance type/group classification and begin date. 21 fields (17 Global, 4 Firm) under Contract; one of the entities the user specifically named, and its Firm extension (Firm_AllowCostPSF per 005's representative examples) shows ASG tracks a cost-per-square-foot calculation the base platform doesn't.

Source: `data-fields/allowance.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Fields with a vendor definition | 17 of 23 inventoried |
| Physical tables | `allowance` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in allowance

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 17 fields carry a vendor definition

**Observed.** 17 of this record's 23 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `allowance.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `allowance.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `allowance.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `allowance.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAllowanceGroupID` | Allowance Group | The allowance group is the first level of categorization for allowance records. Groups are the parents of types. | Dropdown (Allowance Group Code) | Global |  | `allowance.CodeAllowanceGroupID · TEXT` | Allowance Group Code |
| `CodeAllowanceTypeID` | Allowance Type | The allowance type is the second level of categorization for allowance records. Types are the children of groups. | Dropdown (Allowance Type Code) | Global |  | `allowance.CodeAllowanceTypeID · TEXT` | Allowance Type Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `allowance.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `allowance.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `Firm_AllowanceCategory` |  |  | Dropdown (Custom Field) | — |  |  | Custom Field |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_AllowCostPSF` | Cost PSF |  | Currency | Firm |  | `allowance.Firm_AllowCostPSF · TEXT` |  |
| `TotalAmount` | Total Amount | Enter the total amount of the allowance in this field. | Currency | Global |  | `allowance.TotalAmount · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllowanceID` | Allowance RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `allowance.AllowanceID · VARCHAR(64) NOT NULL` |  |
| `RentableArea` | Rentable Area | The rentable area entered for the contract. Your rentable area and area unit should pre-populate if you have them entered at the contract level. | Number | Global |  | `allowance.RentableArea · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `allowance.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `allowance.EndDate · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Firm_AllowanceDocument` | Document |  | Text | Firm |  | `allowance.Firm_AllowanceDocument · TEXT` |  |
| `Firm_AllowancePage` | Page |  | Text | Firm |  | `allowance.Firm_AllowancePage · TEXT` |  |
| `Firm_LandlordAllowanceContact` |  |  | Text | — |  |  |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `allowance.Notes · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `allowance.Section · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Allowance ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `allowance.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `allowance.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `allowance.ModifiedDate · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [AllowanceTransaction](AllowanceTransaction.md) | `AllowanceID` |
