# Responsibility

*32 fields · module: Contracts & Leases · Postgres: `responsibility`*

Defines which party (landlord/tenant) is responsible for a cost category on a lease, with cap amount/percent limits — the allocation-of-obligation record that ExpenseRecovery and FinancialAdjustment calculations reference. 33 Global fields under Contract and Wizard.

Source: `data-fields/responsibility.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 32 |
| Fields with a vendor definition | 30 of 32 inventoried |
| Physical tables | `responsibility` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 33 (33 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in responsibility

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 30 fields carry a vendor definition

**Observed.** 30 of this record's 32 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 31 comparable

**Observed.** Over the 31 fields both captures contain, they agree on 30. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AmendmentID` | Amendment | Select the amendment that the record is associated with from this field. | Contract Amendment ID | Global |  | `responsibility.AmendmentID · TEXT` | [ContractAmendment](ContractAmendment.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `responsibility.ContractID · TEXT` | [Contract](Contract.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `responsibility.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `responsibility.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (4)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExecutionPersonID` | Repairs Contact | Select the contact responsible for repairs from this field. | Contact | Global |  | `responsibility.ExecutionPersonID · TEXT` |  |
| `FinancialPersonID` | Replace Contact | Select the contact responsible for replacement from this field. | Contact | Global |  | `responsibility.FinancialPersonID · TEXT` |  |
| `MaintenancePersonID` | Maintenance Contact | Select the contact responsible for maintenance from this field. | Contact | Global |  | `responsibility.MaintenancePersonID · TEXT` |  |
| `ServicePersonID` | Service Contact | Select the individual responsible for performing the service from this field. | Contact | Global |  | `responsibility.ServicePersonID · TEXT` |  |

### Coded values (drop-downs) (9)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAssetCategoryID` | Maintenance Category | Select the maintenance category from this field. | Dropdown (Asset Category Code) | Global |  | `responsibility.CodeAssetCategoryID · TEXT` | Asset Category Code |
| `CodeExecutionResponsibilityID` | Repairs Responsibility | Select the party responsible for repairs from this field. | Dropdown (Responsible Party) | Global |  | `responsibility.CodeExecutionResponsibilityID · TEXT` | Responsible Party |
| `CodeFinancialResponsibilityID` | Replace Responsibility | Select the party responsible for replacement from this field. | Dropdown (Responsible Party) | Global |  | `responsibility.CodeFinancialResponsibilityID · TEXT` | Responsible Party |
| `CodeMaintenanceResponsibilityID` | Maintenance Responsibility | Select the party responsible for maintenance from this field. The values that you will typically use in this and the next two fields are landlord and tenant . | Dropdown (Responsible Party) | Global |  | `responsibility.CodeMaintenanceResponsibilityID · TEXT` | Responsible Party |
| `CodePassThroughTypeID` | Pass Through Type | Select how the landlord will pass the cost of the responsibility to the tenant from this field. | Dropdown (Pass Through Type Code) | Global |  | `responsibility.CodePassThroughTypeID · TEXT` | Pass Through Type Code |
| `CodeResponseTimeID` | Response Time | Select the expected response time from this field. | Dropdown (Response Time Code) | Global |  | `responsibility.CodeResponseTimeID · TEXT` | Response Time Code |
| `CodeResponsibilityGroupID` | Responsibility Group | The responsibility group is the first level of categorization for responsibility records. Groups are the parents of types. | Dropdown (Responsibility Group Code) | Global |  | `responsibility.CodeResponsibilityGroupID · TEXT` | Responsibility Group Code |
| `CodeResponsibilityTypeID` | Responsibility Type | The responsibility type is the second level of categorization for responsibility records. Types are the children of groups. | Dropdown (Responsibility Type Code) | Global |  | `responsibility.CodeResponsibilityTypeID · TEXT` | Responsibility Type Code |
| `CodeServiceResponsibilityID` | Service Responsibility | Select the responsible party from this field. | Dropdown (Responsible Party) | Global |  | `responsibility.CodeServiceResponsibilityID · TEXT` | Responsible Party |

### Money (2)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapAmount` | Cap Amount | Enter the cap amount in this field. | Currency | Global |  | `responsibility.CapAmount · TEXT` |  |
| `ContractResponsibilityAmount` | Contract Responsibility Amount | Enter the financial amount associated with this responsibility in this field. | Currency | Global |  | `responsibility.ContractResponsibilityAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapPercent` | Cap Percent | Enter the cap percentage in this field. | Percentage | Global |  | `responsibility.CapPercent · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ResponsibilityID` | Responsibility RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `responsibility.ResponsibilityID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the responsibility in the Effective Date field. | Date | Global |  | `responsibility.EffectiveDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `responsibility.EndDate · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IncludedInRentFlag` | Included In Rent? | Select this check box if the cost associated with this responsibility is included in the base rent. | Boolean | Global |  | `responsibility.IncludedInRentFlag · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `responsibility.Notes · TEXT` |  |
| `Photos` |  | This field is not used for this record type. | Text | Global |  | `responsibility.Photos · TEXT` |  |
| `ResponsibilePartyVal` | Responsible Party |  | Text | Global |  | `responsibility.ResponsibilePartyVal · TEXT` |  |
| `Section` |  | Enter the section of the covenant that pertains to this record in this field. | Text | Global |  | `responsibility.Section · TEXT` |  |
| `ServiceLevel` | Service Level | Enter the level of service the service person can offer in this field. | Text | Global |  | `responsibility.ServiceLevel · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Responsibility ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `responsibility.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `responsibility.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `responsibility.ModifiedDate · TEXT` |  |
