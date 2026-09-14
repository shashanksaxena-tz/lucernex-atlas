# BudgetColumnType

*31 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_column_type`*

The template defining what a Budget Column represents (multi-select allowed, one-instance-only, editable) — configuration metadata one level above the individual BudgetColumn records. 34 Global fields under Budget and Statics.

Source: `data-fields/budget-column-type.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Catalogued fields | 34 (34 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 16 keys from 8 record types |
| Points at | 4 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetViewID` | Budget View | Budget Template View ID | Global |  | [BudgetView](BudgetView.md) |
| `EditControllerID` | Use this Budget View for Edit Control | Budget Template View ID | Global |  | [BudgetView](BudgetView.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeStatusDefaultID` | Default Status | Dropdown (Budget Status) | Global |  | Budget Status |
| `CodeStatusSelectedID` | Status | Dropdown (Budget Status) | Global | yes | Budget Status |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnTypeID` | Budget Column Type RecID | Number | Global |  |  |
| `ReportGroupAvailableFieldID` | Report Group Available Field | Number | Global |  |  |

### Flags (17)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AllowMultiSelect` | Allow Multi Select? | Boolean | Global | yes |  |
| `AllowOneInstance` | Allow One Instance? | Boolean | Global | yes |  |
| `AllowUIEditForBudgetColumn` | Budget Editable? | Boolean | Global | yes |  |
| `IsBidTemplate` | Is Bid Template | Boolean | Global | yes |  |
| `IsForBidLeveling` | Is For Bid Leveling? | Boolean | Global | yes |  |
| `IsForBidding` | Is For Bidding? | Boolean | Global | yes |  |
| `IsValidForCapProgram` | Valid For Capital Program? | Boolean | Global | yes |  |
| `IsValidForCapProject` | Valid For Capital Project? | Boolean | Global | yes |  |
| `IsValidForContract` | Valid For RE Contract? | Boolean | Global | yes |  |
| `IsValidForEquipContract` | Valid For Equipment Contract? | Boolean | Global | yes |  |
| `IsValidForFacility` | Valid For Facility? | Boolean | Global | yes |  |
| `IsValidForLocation` | Valid For Location? | Boolean | Global | yes |  |
| `IsValidForOpenProject` | Valid For Opening Project? | Boolean | Global | yes |  |
| `IsValidForParcel` | Valid For Parcel? | Boolean | Global | yes |  |
| `IsValidForPortfolio` | Valid For Portfolio? | Boolean | Global | yes |  |
| `IsValidForPotentialProject` | Valid For Site? | Boolean | Global | yes |  |
| `IsValidForPrototype` | Valid For Prototype? | Boolean | Global | yes |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BudgetColumnTypeName` | Name | Text | Global | yes |  |
| `Description` |  | Text | Global |  |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Column Type ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (16 keys)

| Record type | Via column |
|---|---|
| [CostTrackingTemplate](CostTrackingTemplate.md) | `ApprovedCOBudgetColTypeID`, `EstimateBudgetColumnTypeID`, `InvoiceBudgetColTypeID`, `OutstandingCOBudgetColTypeID`, `POBudgetColumnTypeID` |
| [BidPackage](BidPackage.md) | `BidBudgetColumnTypeID`, `ConditionBudgetColumnTypeID`, `EstimateBudgetColumnTypeID` |
| [BidPackageTemplate](BidPackageTemplate.md) | `BidColumnTypeID`, `EstimateBudgetColumnTypeID` |
| [Issue](Issue.md) | `Budget`, `BudgetColumnTypeID` |
| [BudgetColumn](BudgetColumn.md) | `BudgetColumnTypeID` |
| [BudgetIndexValue](BudgetIndexValue.md) | `BudgetColumnTypeID` |
| [Security](Security.md) | `BudgetColumnTypeID` |
| [UserClassSecurity](UserClassSecurity.md) | `BudgetColumnTypeID` |
