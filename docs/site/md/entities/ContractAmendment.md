# ContractAmendment

*20 fields · module: Contracts & Leases · Postgres: `contract_amendment`*

A formal amendment/modification to an executed lease — amendment group/number/type classification and base-amount change. 19 fields (17 Global, 2 Firm) under Contract.

Source: `data-fields/contract-amendment.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 20 |
| Fields with a vendor definition | 17 of 20 inventoried |
| Physical tables | `contract_amendment` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in contract_amendment

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 17 fields carry a vendor definition

**Observed.** 17 of this record's 20 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `contract_amendment.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `contract_amendment.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentIDList` | Documents | This is a generic field that allows you to add documents a record. | Document List | Global |  | `contract_amendment.DocumentIDList · TEXT` |  |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAmendmentGroupID` | Amendment Group | The amendment group is the first level of categorization for amendments. Groups are the parents of types. | Dropdown (Amendment Group Code) | Global |  | `contract_amendment.CodeAmendmentGroupID · TEXT` | Amendment Group Code |
| `CodeAmendmentTypeID` | Amendment Type | The amendment type is the second level of categorization for amendments. Types are the children of groups. | Dropdown (Amendment Type Code) | Global |  | `contract_amendment.CodeAmendmentTypeID · TEXT` | Amendment Type Code |
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `contract_amendment.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeContractUseID` | Contract Use | Select the primary use of the space from this field. | Dropdown (Contract Use Code) | Global |  | `contract_amendment.CodeContractUseID · TEXT` | Contract Use Code |
| `CodeFrequencyID` | Frequency | Select the frequency of the payment from this field. This field is for tracking purposes only. You will need to update your recurring expenses for your transactions to be updated. | Dropdown (Frequency Code) | Global |  | `contract_amendment.CodeFrequencyID · TEXT` | Frequency Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaseAmountChange` | Base Amount Change | Enter the payment amount in this field. This field is for tracking purposes only. You will need to update your recurring expenses for your transactions to be updated. | Currency | Global |  | `contract_amendment.BaseAmountChange · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractAmendmentID` | Amendment RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `contract_amendment.ContractAmendmentID · VARCHAR(64) NOT NULL` |  |
| `RentableAreaChange` | Rentable Area Change | If there has been a change in the rentable area, enter the new rentable area in this field. This field is informational-only. You will need to change your rentable area on the Contract > Details > Summary page for your rate calculations to update. | Number | Global |  | `contract_amendment.RentableAreaChange · TEXT` |  |

### Dates & timestamps (3)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the amendment in this field. | Date | Global |  | `contract_amendment.EffectiveDate · TEXT` |  |
| `Firm_AmendmentEntryDate` | Entry Date |  | Date | Firm |  | `contract_amendment.Firm_AmendmentEntryDate · TEXT` |  |
| `Firm_AmendmentExecutionDate` | Execution Date |  | Date | Firm |  | `contract_amendment.Firm_AmendmentExecutionDate · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentNumber` | Amendment Number | Enter a unique ID for the amendment in this field. You will use this ID when selecting an amendment on the Covenants page. | Text | Global |  | `contract_amendment.AmendmentNumber · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `contract_amendment.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `contract_amendment.Notes · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Contract Amendment ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `contract_amendment.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `contract_amendment.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `contract_amendment.ModifiedDate · TEXT` |  |

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
