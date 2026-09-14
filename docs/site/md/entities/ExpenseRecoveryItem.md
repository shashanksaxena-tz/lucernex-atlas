# ExpenseRecoveryItem

*47 fields · module: Expense Recovery (CAM / Reconciliation) · Postgres: `expense_recovery_item`*

The line-item detail underneath ExpenseRecovery — one record per actual-vs-budget variance calculation (A-B, A-P, B-P Variance Amount/Percent), admin fee, and approved pro rata share, used during CAM reconciliation to compare what a tenant was billed against what was approved. 46 Global fields under Contract; naming convention (A=Actual, B=Budget, P=Prior, based on context) mirrors standard CAM reconciliation worksheet columns.

Source: `data-fields/expense-recovery-item.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 47 |
| Catalogued fields | 46 (46 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 4 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-102](../rules/CON-R-102.md) | A landlord statement is ingested: ExpenseRecoveryItemMapping maps a free-text statement line (InvoiceLineItemName, JSONConfigText) to a structured recovery item. | Inferred |
| [CON-R-134](../rules/CON-R-134.md) | Migrating any parent-child edge: seven FKs are declared Text rather than typed, though the target's proper FK type exists elsewhere in the same schema; model them as real FKs with an orphan-handling policy. | Observed |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeApprovalStatusID` | Approval Status | Dropdown (Approval Status Code) | Global |  | Approval Status Code |
| `CodeRecoveryItemGroupID` | Recovery Item Group | Dropdown (Recovery Item Group Code) | Global |  | Recovery Item Group Code |
| `CodeRecoveryItemTypeID` | Recovery Item Type | Dropdown (Recovery Item Type Code) | Global |  | Recovery Item Type Code |
| `CodeRecoverySectionID` | Recovery Section | Dropdown (Recovery Section Code) | Global | yes | Recovery Section Code |

### Money (22)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ABVarianceAmount` | A-B Variance Amount | Currency | Global |  |  |
| `APVarianceAmount` | A-P Variance Amount | Currency | Global |  |  |
| `ApprovedAdminFeeAmtNoZeroDef` | Admin Fee Amount | Currency | Global |  |  |
| `ApprovedAmount` | Approved Amount | Currency | Global |  |  |
| `ApprovedCapAmountNoZeroDef` | Cap Amount | Currency | Global |  |  |
| `BPVarianceAmount` | B-P Variance Amount | Currency | Global |  |  |
| `BudgetedAmount` | Budgeted Amount | Currency | Global |  |  |
| `BudgetedAmountGross` | Budgeted Amount Gross | Currency | Global |  |  |
| `BudgetedAmountNet` | Budgeted Amount Net | Currency | Global |  |  |
| `ComputedApprovedAdminFeeNoZeroDef` | Computed Admin Fee | Currency | Global |  |  |
| `ComputedApprovedCapNoZeroDef` | Computed Approved Cap | Currency | Global |  |  |
| `ComputedApprovedTotalAmount` | Computed Total Approved Amount | Currency | Global |  |  |
| `ComputedApprovedTotalAmountGross` | Computed Total Approved Amount Gross | Currency | Global |  |  |
| `ComputedApprovedTotalAmountNet` | Computed Total Approved Amount Net | Currency | Global |  |  |
| `PriorApprovedAmountNoZeroDef` | Prior Approved Amount | Currency | Global |  |  |
| `PriorBudgetedAmountNoZeroDef` | Prior Budgeted Amount | Currency | Global |  |  |
| `PriorReportedAmountNoZeroDef` | Prior Reported Amount | Currency | Global |  |  |
| `RAVarianceAmount` | R-A Variance Amount | Currency | Global |  |  |
| `RPVarianceAmount` | R-P Variance Amount | Currency | Global |  |  |
| `ReportedAmount` | Reported Amount | Currency | Global |  |  |
| `ReportedAmountGross` | Reported Amount Gross | Currency | Global |  |  |
| `ReportedAmountNet` | Reported Amount Net | Currency | Global |  |  |

### Rates & percentages (10)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ABVariancePercent` | A-B Variance Percent | Percentage | Global |  |  |
| `APVariancePercent` | A-P Variance Percent | Percentage | Global |  |  |
| `ApprovedAdminFeePrcntNoZeroDef` | Admin Fee Percentage | Percentage | Global |  |  |
| `ApprovedCapPercentNoZeroDef` | Cap Percentage | Percentage | Global |  |  |
| `ApprovedProRataShareRate` | Approved Pro Rata Share Rate | Percentage | Global |  |  |
| `BPVariancePercent` | B-P Variance Percent | Percentage | Global |  |  |
| `BudgetedProRataShareRate` | Budgeted Pro Rata Share Rate | Percentage | Global |  |  |
| `RAVariancePercent` | R-A Variance Percent | Percentage | Global |  |  |
| `RPVariancePercent` | R-P Variance Percent | Percentage | Global |  |  |
| `ReportedProRataShareRate` | Reported Pro Rata Share Rate | Percentage | Global |  |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExpenseRecoveryItemID` | Expense Recovery Item RecID | Number | Global |  |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExpenseRecoveryID` | Expense Recovery | Text | Global | yes |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Recovery Item ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
