# SalesExclusionCap

*23 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `sales_exclusion_cap`*

A cap limiting how much sales can be excluded from percentage-rent calculation (e.g., online/catalog sales exclusions) — cap amount/percent and begin date. 22 Global fields under Contract.

Source: `data-fields/sales-exclusion-cap.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 23 |
| Fields with a vendor definition | 22 of 23 inventoried |
| Physical tables | `sales_exclusion_cap` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 22 (22 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 3 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in sales_exclusion_cap

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 22 fields carry a vendor definition

**Observed.** 22 of this record's 23 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: 1 disagree of 22 comparable

**Observed.** Over the 22 fields both captures contain, they agree on 21. The exceptions are ContractID. Estate-wide there are 43 such fields and every one runs the same way — catalogue-required, inventory-not — and they are 34 ContractID, 8 ProjectEntityID and 1 ShortName: the owner foreign key. Parenthood is enforced by the application, not by the database.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-052](../rules/CON-R-052.md) | An exclusion applies: rawExcluded = salesOfType × SalesExclusion.ExclusionRate. | Derived |
| [CON-R-053](../rules/CON-R-053.md) | Exclusions share a cap group (ExclusionGroupCapID): PRPGrossExcludedAmount sums the raw excluded amounts within the group, before the cap. | Derived |
| [CON-R-054](../rules/CON-R-054.md) | A cap group is evaluated: PRPComputedCapAmount = min(CapAmount, PRPGrossSalesAmount × CapPercent) — the effective cap, whichever binds first. | Inferred |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `sales_exclusion_cap.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `sales_exclusion_cap.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `sales_exclusion_cap.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeExclusionCapID` | Exclusion Cap | Select the exclusion group from this field. | Dropdown (Exclusion Cap Code) | Global | yes | `sales_exclusion_cap.CodeExclusionCapID · TEXT` | Exclusion Cap Code |
| `CodeSalesGroupID` | Sales Group | The sales group is the first level of categorization for sales records. Groups are the parents of types, and grandparents of categories. | Dropdown (Sales Group) | Global |  | `sales_exclusion_cap.CodeSalesGroupID · TEXT` | Sales Group |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapAmount` | Cap Amount | Sales Exclusion Caps are groups which contain line items Sales Exclusions. A sales exclusion cap group has a cap. To determine whether the cap has been met, you must sum the sales of each of the sales exclusions which belong to the group. Enter the sales exclusion cap amount in this field. Remember, Lx applies caps on an annual, not monthly, basis. | Currency | Global |  | `sales_exclusion_cap.CapAmount · TEXT` |  |

### Rates & percentages (1)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapPercent` | Cap Percent | Sales Exclusion Caps are groups which contain line items Sales Exclusions. A sales exclusion cap group has a cap. To determine whether the cap has been met, you must sum the sales of each of the sales exclusions which belong to the group. Enter the sales exclusion cap percent in this field. The Exclusion Cap Percent is a percentage of Gross Sales. Remember, Lx applies caps on an annual, not monthly, basis. | Percentage | Global |  | `sales_exclusion_cap.CapPercent · TEXT` |  |

### Quantities (7)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PRPComputedCapAmount` | PRP Computed Cap Amount | This is a reporting field. If sales exclusion caps are configured, The cap amount computed from sales for a particular percentage rent year. | Number | Global |  | `sales_exclusion_cap.PRPComputedCapAmount · TEXT` |  |
| `PRPExcessExcludedAmount` | PRP Excess Excluded Amount | This is a reporting field. The value of this field is equal to the Gross Excluded Amount minus the Net Excluded Amount. | Number | Global |  | `sales_exclusion_cap.PRPExcessExcludedAmount · TEXT` |  |
| `PRPGrossExcludedAmount` | PRP Gross Excluded Amount | This is a reporting field. The value of this field is calculated by summing the excluded sales across sales periods. This value is also used in calculating the amount of sales exceeding the cap amount. | Number | Global |  | `sales_exclusion_cap.PRPGrossExcludedAmount · TEXT` |  |
| `PRPGrossSalesAmount` | PRP Gross Sales Amount | This is a reporting field. The value of this field is calculated by summing gross sales amounts across all applicable sales periods. The value of this field is also used in calculating the computed cap amount. | Number | Global |  | `sales_exclusion_cap.PRPGrossSalesAmount · TEXT` |  |
| `PRPNetExcludedAmount` | PRP Net Excluded Amount | This is a reporting field. The value of this field is either the Gross Excluded Amount or the Computed Cap Amount, depending on whether the Gross Excluded Amount is greater than the Cap Amount or not. This field is used to calculate the amount of sales exceeding the cap amount. | Number | Global |  | `sales_exclusion_cap.PRPNetExcludedAmount · TEXT` |  |
| `SPExcludedAmount` | SP Excluded Amount | This is a reporting field. This field sums the total amount excludes from sales. | Number | Global |  | `sales_exclusion_cap.SPExcludedAmount · TEXT` |  |
| `SalesExclusionCapID` | Exclusion Cap RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `sales_exclusion_cap.SalesExclusionCapID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `sales_exclusion_cap.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `sales_exclusion_cap.EndDate · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Notes` |  | Add any notes about the record. | Text | Global |  | `sales_exclusion_cap.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Exclusion Cap ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `sales_exclusion_cap.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `sales_exclusion_cap.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `sales_exclusion_cap.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `sales_exclusion_cap.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `sales_exclusion_cap.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `sales_exclusion_cap.RevNumber · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [SalesExclusion](SalesExclusion.md) | `ExclusionGroupCapID` |
