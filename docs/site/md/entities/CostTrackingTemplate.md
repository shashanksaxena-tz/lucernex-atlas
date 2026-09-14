# CostTrackingTemplate

*28 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `cost_tracking_template`*

A reusable cost-tracking configuration for capital projects — which budget column represents 'Approved Change Order' and how variance is calculated, applied across ProjectEntity records. 27 Global fields under Company Items.

Source: `data-fields/cost-tracking-template.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Fields with a vendor definition | 0 of 28 inventoried |
| Physical tables | `cost_tracking_template` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 27 (27 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 8 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in cost_tracking_template

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 1 field marked required

**Observed.** The inventory marks 1 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (6)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApprovedCOBudgetColTypeID` | Approved CO Column |  | Budget Type ID | Global |  | `cost_tracking_template.ApprovedCOBudgetColTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `EstimateBudgetColumnTypeID` | Estimate Column |  | Budget Type ID | Global |  | `cost_tracking_template.EstimateBudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `InvoiceBudgetColTypeID` | Invoice Column |  | Budget Type ID | Global |  | `cost_tracking_template.InvoiceBudgetColTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `OutstandingCOBudgetColTypeID` | Outstanding CO Column |  | Budget Type ID | Global |  | `cost_tracking_template.OutstandingCOBudgetColTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `POBudgetColumnTypeID` | PO Column |  | Budget Type ID | Global | yes | `cost_tracking_template.POBudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `cost_tracking_template.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CostTrackingTemplateID` | Cost Tracking Template RecID |  | Number | Global |  | `cost_tracking_template.CostTrackingTemplateID · VARCHAR(64) NOT NULL` |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsValidForCapProgram` | Cost Tracking Template Valid for Cap Program? |  | Boolean | Global |  | `cost_tracking_template.IsValidForCapProgram · TEXT` |  |
| `IsValidForCapProject` | Cost Tracking Template Valid for Cap Project? |  | Boolean | Global |  | `cost_tracking_template.IsValidForCapProject · TEXT` |  |
| `IsValidForContract` | Cost Tracking Template Valid for RE Contract? |  | Boolean | Global |  | `cost_tracking_template.IsValidForContract · TEXT` |  |
| `IsValidForEquipContract` | Cost Tracking Template Valid for Equipment Contract? |  | Boolean | Global |  | `cost_tracking_template.IsValidForEquipContract · TEXT` |  |
| `IsValidForFacility` | Cost Tracking Template Valid for Facility? |  | Boolean | Global |  | `cost_tracking_template.IsValidForFacility · TEXT` |  |
| `IsValidForLocation` | Cost Tracking Template Valid for Location? |  | Boolean | Global |  | `cost_tracking_template.IsValidForLocation · TEXT` |  |
| `IsValidForOpenProject` | Cost Tracking Template Valid for Open Project? |  | Boolean | Global |  | `cost_tracking_template.IsValidForOpenProject · TEXT` |  |
| `IsValidForParcel` | Cost Tracking Template Valid for Parcel? |  | Boolean | Global |  | `cost_tracking_template.IsValidForParcel · TEXT` |  |
| `IsValidForPortfolio` | Cost Tracking Template Valid for Portfolio? |  | Boolean | Global |  | `cost_tracking_template.IsValidForPortfolio · TEXT` |  |
| `IsValidForPotentialProject` | Cost Tracking Template Valid for Potential Project? |  | Boolean | Global |  | `cost_tracking_template.IsValidForPotentialProject · TEXT` |  |
| `IsValidForPrototype` | Cost Tracking Template Valid for Prototype? |  | Boolean | Global |  | `cost_tracking_template.IsValidForPrototype · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` | Cost Tracking Template Description |  | Text | Global |  | `cost_tracking_template.Description · TEXT` |  |
| `Notes` | Cost Tracking Template Notes |  | Text | Global |  | `cost_tracking_template.Notes · TEXT` |  |
| `SummaryVarianceCalc` | Cost Tracking Summary Variance Calculation |  | Text | Global |  | `cost_tracking_template.SummaryVarianceCalc · TEXT` |  |
| `TemplateName` | Cost Tracking Template Name |  | Text | Global |  | `cost_tracking_template.TemplateName · TEXT` |  |
| `VendorBreakdownVarianceCalc` | Vendor Breakdown Variance Calculation |  | Text | Global |  | `cost_tracking_template.VendorBreakdownVarianceCalc · TEXT` |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By |  | Member ID | Global |  | `cost_tracking_template.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date |  | Time | Global |  | `cost_tracking_template.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By |  | Member ID | Global |  | `cost_tracking_template.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date |  | Time | Global |  | `cost_tracking_template.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number |  | Number | Global |  | `cost_tracking_template.RevNumber · TEXT` |  |
