# CoTenancy

*27 fields · module: Contracts & Leases · Postgres: `co_tenancy`*

A co-tenancy clause (rent reduction if an anchor tenant vacates) — anchor name, co-tenancy amount/area, and begin date, one of the seven Firm-editable Contract subgroups per 005. 26 Global fields under Contract.

Source: `data-fields/co-tenancy.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 27 |
| Fields with a vendor definition | 26 of 28 inventoried |
| Physical tables | `co_tenancy` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 26 (26 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in co_tenancy

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 26 fields carry a vendor definition

**Observed.** 26 of this record's 28 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `co_tenancy.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `co_tenancy.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `co_tenancy.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `co_tenancy.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBuildingAreaUnitID` | Building Area Unit | Select the units you are using to measure your area from this field. This field should pre-populate with the area unit you selected when creating your contract. | Dropdown (Building Area Unit Code) | Global |  | `co_tenancy.CodeBuildingAreaUnitID · TEXT` | Building Area Unit Code |
| `CodeCoTenancyGroupID` | Co Tenancy Group | The cotenancy group is the first level of categorization for cotenancy records. Groups are the parents of types. | Dropdown (Co Tenancy Group Code) | Global |  | `co_tenancy.CodeCoTenancyGroupID · TEXT` | Co Tenancy Group Code |
| `CodeCoTenancyTypeID` | Co Tenancy Type | The cotenancy type is the second level of categorization for cotenancy records. Types are the children of groups. | Dropdown (Co Tenancy Type Code) | Global |  | `co_tenancy.CodeCoTenancyTypeID · TEXT` | Co Tenancy Type Code |
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `co_tenancy.CodeCurrencyTypeID · TEXT` | Currency Type Code |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CoTenancyAmount` | Co Tenancy Amount | Enter any other financial amount that needs to be captured for co-tenancy purposes in this field. | Currency | Global |  | `co_tenancy.CoTenancyAmount · TEXT` |  |
| `RentReductionAmount` | Rent Reduction Amount | Enter the amount of rent reduction allowed if the occupancy percentage falls below the percentage specified in the cotenancy agreement in this field. | Currency | Global |  | `co_tenancy.RentReductionAmount · TEXT` |  |
| `Sales` |  | If the co-tenancy clause stipulates a minimum sales number for breaking the contract, enter the sales number in this field. For example, some contracts stipulate that if sales drop below a certain number, the lessee has the right to break the contract. | Currency | Global |  | `co_tenancy.Sales · TEXT` |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `OccupancyPercentage` | Occupancy Percentage | Enter the required occupancy percentage in this field. | Percentage | Global |  | `co_tenancy.OccupancyPercentage · TEXT` |  |
| `RentReductionPercent` | Rent Reduction Percent | Enter the percentage rent reduction allowed if the occupancy percentage falls below the percentage specified in the cotenancy agreement in this field. | Percentage | Global |  | `co_tenancy.RentReductionPercent · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CoTenancyArea` | Co Tenancy Area | Enter the rentable area in this field. This field can be used to enter the rentable area of the contract or the total rentable area of the property. | Number | Global |  | `co_tenancy.CoTenancyArea · TEXT` |  |
| `CoTenancyID` | Co Tenancy RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `co_tenancy.CoTenancyID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `co_tenancy.BeginDate · TEXT` |  |
| `EffectiveDate` | Effective Date | Enter the effective date of the cotenancy agreement in this field. | Date | Global |  | `co_tenancy.EffectiveDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `co_tenancy.EndDate · TEXT` |  |
| `RemodelDate` | Remodel Date | Enter the remodel date of your space in this field. | Date | Global |  | `co_tenancy.RemodelDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HasRightToTerminate` | Has Right To Terminate? | Select this check box if you have the right to terminate if the occupancy percentage falls below the occupancy percentage. | Boolean | Global |  | `co_tenancy.HasRightToTerminate · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CoTenancyName` | Anchor Name | Enter a name for the co-tenancy record in this field. | Text | Global |  | `co_tenancy.CoTenancyName · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `co_tenancy.Notes · TEXT` |  |
| `RentAccount` | Rent Account | In some instances, you may note and alternate account to use when a co-tenancy event triggers alternate rent. Enter the account number in this field. This field is information-only. | Text | Global |  | `co_tenancy.RentAccount · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `co_tenancy.Section · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Co Tenancy ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `co_tenancy.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `co_tenancy.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `co_tenancy.ModifiedDate · TEXT` |  |
