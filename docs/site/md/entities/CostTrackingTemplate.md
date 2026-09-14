# CostTrackingTemplate

*28 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `cost_tracking_template`*

A reusable cost-tracking configuration for capital projects — which budget column represents 'Approved Change Order' and how variance is calculated, applied across ProjectEntity records. 27 Global fields under Company Items.

Source: `data-fields/cost-tracking-template.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Catalogued fields | 27 (27 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 8 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApprovedCOBudgetColTypeID` | Approved CO Column | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `EstimateBudgetColumnTypeID` | Estimate Column | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `InvoiceBudgetColTypeID` | Invoice Column | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `OutstandingCOBudgetColTypeID` | Outstanding CO Column | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `POBudgetColumnTypeID` | PO Column | Budget Type ID | Global | yes | [BudgetColumnType](BudgetColumnType.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CostTrackingTemplateID` | Cost Tracking Template RecID | Number | Global |  |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsValidForCapProgram` | Cost Tracking Template Valid for Cap Program? | Boolean | Global |  |  |
| `IsValidForCapProject` | Cost Tracking Template Valid for Cap Project? | Boolean | Global |  |  |
| `IsValidForContract` | Cost Tracking Template Valid for RE Contract? | Boolean | Global |  |  |
| `IsValidForEquipContract` | Cost Tracking Template Valid for Equipment Contract? | Boolean | Global |  |  |
| `IsValidForFacility` | Cost Tracking Template Valid for Facility? | Boolean | Global |  |  |
| `IsValidForLocation` | Cost Tracking Template Valid for Location? | Boolean | Global |  |  |
| `IsValidForOpenProject` | Cost Tracking Template Valid for Open Project? | Boolean | Global |  |  |
| `IsValidForParcel` | Cost Tracking Template Valid for Parcel? | Boolean | Global |  |  |
| `IsValidForPortfolio` | Cost Tracking Template Valid for Portfolio? | Boolean | Global |  |  |
| `IsValidForPotentialProject` | Cost Tracking Template Valid for Potential Project? | Boolean | Global |  |  |
| `IsValidForPrototype` | Cost Tracking Template Valid for Prototype? | Boolean | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` | Cost Tracking Template Description | Text | Global |  |  |
| `Notes` | Cost Tracking Template Notes | Text | Global |  |  |
| `SummaryVarianceCalc` | Cost Tracking Summary Variance Calculation | Text | Global |  |  |
| `TemplateName` | Cost Tracking Template Name | Text | Global |  |  |
| `VendorBreakdownVarianceCalc` | Vendor Breakdown Variance Calculation | Text | Global |  |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |
