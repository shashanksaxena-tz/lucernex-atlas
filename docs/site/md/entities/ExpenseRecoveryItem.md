# ExpenseRecoveryItem

*47 fields · module: Expense Recovery (CAM / Reconciliation) · Postgres: `expense_recovery_item`*

The line-item detail underneath ExpenseRecovery — one record per actual-vs-budget variance calculation (A-B, A-P, B-P Variance Amount/Percent), admin fee, and approved pro rata share, used during CAM reconciliation to compare what a tenant was billed against what was approved. 46 Global fields under Contract; naming convention (A=Actual, B=Budget, P=Prior, based on context) mirrors standard CAM reconciliation worksheet columns.

Source: `data-fields/expense-recovery-item.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 47 |
| Fields with a vendor definition | 46 of 47 inventoried |
| Physical tables | `expense_recovery_item` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 46 (46 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in expense_recovery_item

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 46 fields carry a vendor definition

**Observed.** 46 of this record's 47 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 4 of this record's fields required; the Data Fields catalogue marks 4; 4 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-102](../rules/CON-R-102.md) | A landlord statement is ingested: ExpenseRecoveryItemMapping maps a free-text statement line (InvoiceLineItemName, JSONConfigText) to a structured recovery item. | Inferred |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `expense_recovery_item.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `expense_recovery_item.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeApprovalStatusID` | Approval Status | Select the approval status of the recovery item from this field. | Dropdown (Approval Status Code) | Global |  | `expense_recovery_item.CodeApprovalStatusID · TEXT` | Approval Status Code |
| `CodeRecoveryItemGroupID` | Recovery Item Group | The recovery item group is the first level of categorization for recovery items. Groups are the parents of types. | Dropdown (Recovery Item Group Code) | Global |  | `expense_recovery_item.CodeRecoveryItemGroupID · TEXT` | Recovery Item Group Code |
| `CodeRecoveryItemTypeID` | Recovery Item Type | The recovery item type is the second level of categorization for recovery items. Types are the children of groups. | Dropdown (Recovery Item Type Code) | Global |  | `expense_recovery_item.CodeRecoveryItemTypeID · TEXT` | Recovery Item Type Code |
| `CodeRecoverySectionID` | Recovery Section | This field displays the recovery section to which you are adding a recovery item. An example of a recovery section is the Controllable Expenses recovery section. | Dropdown (Recovery Section Code) | Global | yes | `expense_recovery_item.CodeRecoverySectionID · TEXT` | Recovery Section Code |

### Money (22)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ABVarianceAmount` | A-B Variance Amount | This is a math field that calculates the difference between the approved and the budgeted amount for the line item. | Currency | Global |  | `expense_recovery_item.ABVarianceAmount · TEXT` |  |
| `APVarianceAmount` | A-P Variance Amount | This is a math field that calculates the difference between the approved and the prior approved amount for the line item. | Currency | Global |  | `expense_recovery_item.APVarianceAmount · TEXT` |  |
| `ApprovedAdminFeeAmtNoZeroDef` | Admin Fee Amount | Enter an admin fee amount for the recovery item in this field. You can also enter this value as a percentage in the Admin Fee Percentage field. | Currency | Global |  | `expense_recovery_item.ApprovedAdminFeeAmtNoZeroDef · TEXT` |  |
| `ApprovedAmount` | Approved Amount | Enter your approved recovery item amount in this field. | Currency | Global |  | `expense_recovery_item.ApprovedAmount · TEXT` |  |
| `ApprovedCapAmountNoZeroDef` | Cap Amount | Enter a cap for the admin fee amount for the recovery item in this field. You can also enter this value as a percentage in the Cap Percentage field. | Currency | Global |  | `expense_recovery_item.ApprovedCapAmountNoZeroDef · TEXT` |  |
| `BPVarianceAmount` | B-P Variance Amount | This is a math field that calculates the difference between the budgeted and the prior budgeted amount for the line item. | Currency | Global |  | `expense_recovery_item.BPVarianceAmount · TEXT` |  |
| `BudgetedAmount` | Budgeted Amount | Enter your budgeted recovery item amount in this field. | Currency | Global |  | `expense_recovery_item.BudgetedAmount · TEXT` |  |
| `BudgetedAmountGross` | Budgeted Amount Gross | The gross budgeted amount for the expense recovery item. | Currency | Global |  | `expense_recovery_item.BudgetedAmountGross · TEXT` |  |
| `BudgetedAmountNet` | Budgeted Amount Net | The net budgeted amount for the expense recovery item. The net budgeted amount is the gross budgeted amount multiplied by the budgeted pro rata share rate. | Currency | Global |  | `expense_recovery_item.BudgetedAmountNet · TEXT` |  |
| `ComputedApprovedAdminFeeNoZeroDef` | Computed Admin Fee | Calculates and displays the admin fee as (Admin Fee Percent multiplied by the Approved Amount) OR the Admin Fee Amount. | Currency | Global |  | `expense_recovery_item.ComputedApprovedAdminFeeNoZeroDef · TEXT` |  |
| `ComputedApprovedCapNoZeroDef` | Computed Approved Cap | Calculates and displays the admin fee cap as (Cap Percent multiplied by the Approved Amount) OR the Cap Amount. | Currency | Global |  | `expense_recovery_item.ComputedApprovedCapNoZeroDef · TEXT` |  |
| `ComputedApprovedTotalAmount` | Computed Total Approved Amount | The sum of the approved amount and the approved admin fee amount or percentage. If the approved admin fee or percentage is empty, The approved amount. | Currency | Global |  | `expense_recovery_item.ComputedApprovedTotalAmount · TEXT` |  |
| `ComputedApprovedTotalAmountGross` | Computed Total Approved Amount Gross | The sum of the approved amount and the approved admin fee amount or percentage. If the approved admin fee or percentage is empty, The approved amount. | Currency | Global |  | `expense_recovery_item.ComputedApprovedTotalAmountGross · TEXT` |  |
| `ComputedApprovedTotalAmountNet` | Computed Total Approved Amount Net | The sum of the approved amount and the approved admin fee amount or percentage. If the approved admin fee or percentage is empty, The approved amount. | Currency | Global |  | `expense_recovery_item.ComputedApprovedTotalAmountNet · TEXT` |  |
| `PriorApprovedAmountNoZeroDef` | Prior Approved Amount | This field displays the approved amount for this recovery item on the previous recovery record. | Currency | Global |  | `expense_recovery_item.PriorApprovedAmountNoZeroDef · TEXT` |  |
| `PriorBudgetedAmountNoZeroDef` | Prior Budgeted Amount | This field displays the budgeted amount for this recovery item on the previous recovery record. | Currency | Global |  | `expense_recovery_item.PriorBudgetedAmountNoZeroDef · TEXT` |  |
| `PriorReportedAmountNoZeroDef` | Prior Reported Amount | This field displays the reported amount for this recovery item on the previous recovery record. | Currency | Global |  | `expense_recovery_item.PriorReportedAmountNoZeroDef · TEXT` |  |
| `RAVarianceAmount` | R-A Variance Amount | This is a math field that calculates the difference between the reported and the approved amount for the line item. | Currency | Global |  | `expense_recovery_item.RAVarianceAmount · TEXT` |  |
| `RPVarianceAmount` | R-P Variance Amount | This is a math field that calculates the difference between the reported and the prior reported amount for the line item. | Currency | Global |  | `expense_recovery_item.RPVarianceAmount · TEXT` |  |
| `ReportedAmount` | Reported Amount | Enter your reported recovery item amount in this field. | Currency | Global |  | `expense_recovery_item.ReportedAmount · TEXT` |  |
| `ReportedAmountGross` | Reported Amount Gross | The gross reported amount for the expense recovery item. | Currency | Global |  | `expense_recovery_item.ReportedAmountGross · TEXT` |  |
| `ReportedAmountNet` | Reported Amount Net | The net reported amount for the expense recovery item. The net reported amount equals the gross reported amount multiplied by the reported pro rata share rate. | Currency | Global |  | `expense_recovery_item.ReportedAmountNet · TEXT` |  |

### Rates & percentages (10)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ABVariancePercent` | A-B Variance Percent | This is a math field that calculates the percentage difference between the approved and the budgeted amount for the line item. | Percentage | Global |  | `expense_recovery_item.ABVariancePercent · TEXT` |  |
| `APVariancePercent` | A-P Variance Percent | This is a math field that calculates the percentage difference between the approved and the prior approved amount for the line item. | Percentage | Global |  | `expense_recovery_item.APVariancePercent · TEXT` |  |
| `ApprovedAdminFeePrcntNoZeroDef` | Admin Fee Percentage | Enter an admin fee percentage for the recovery item in this field. You can also enter this value as an amount in the Admin Fee Amount field. | Percentage | Global |  | `expense_recovery_item.ApprovedAdminFeePrcntNoZeroDef · TEXT` |  |
| `ApprovedCapPercentNoZeroDef` | Cap Percentage | Enter a cap for the admin fee percentage for the recovery item in this field. You can also enter this value as an amount in the Cap Amount field. | Percentage | Global |  | `expense_recovery_item.ApprovedCapPercentNoZeroDef · TEXT` |  |
| `ApprovedProRataShareRate` | Approved Pro Rata Share Rate | The approved pro rata share rate for the expense recovery item. | Percentage | Global |  | `expense_recovery_item.ApprovedProRataShareRate · TEXT` |  |
| `BPVariancePercent` | B-P Variance Percent | This is a math field that calculates the percentage difference between the budgeted and the prior budgeted amount for the line item. | Percentage | Global |  | `expense_recovery_item.BPVariancePercent · TEXT` |  |
| `BudgetedProRataShareRate` | Budgeted Pro Rata Share Rate | The budgeted pro rata share rate for the expense recovery item. | Percentage | Global |  | `expense_recovery_item.BudgetedProRataShareRate · TEXT` |  |
| `RAVariancePercent` | R-A Variance Percent | This is a math field that calculates the percentage difference between the reported and the approved amount for the line item. | Percentage | Global |  | `expense_recovery_item.RAVariancePercent · TEXT` |  |
| `RPVariancePercent` | R-P Variance Percent | This is a math field that calculates the percentage difference between the reported and the prior reported amount for the line item. | Percentage | Global |  | `expense_recovery_item.RPVariancePercent · TEXT` |  |
| `ReportedProRataShareRate` | Reported Pro Rata Share Rate | The reported pro rata share rate for the expense recovery item. | Percentage | Global |  | `expense_recovery_item.ReportedProRataShareRate · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExpenseRecoveryItemID` | Expense Recovery Item RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `expense_recovery_item.ExpenseRecoveryItemID · VARCHAR(64) NOT NULL` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExpenseRecoveryID` | Expense Recovery | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Text | Global | yes | `expense_recovery_item.ExpenseRecoveryID · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `expense_recovery_item.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Recovery Item ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `expense_recovery_item.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `expense_recovery_item.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `expense_recovery_item.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `expense_recovery_item.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `expense_recovery_item.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `expense_recovery_item.RevNumber · TEXT` |  |
