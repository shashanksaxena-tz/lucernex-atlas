# BudgetColumnType

*31 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_column_type`*

The template defining what a Budget Column represents (multi-select allowed, one-instance-only, editable) — configuration metadata one level above the individual BudgetColumn records. 34 Global fields under Budget and Statics.

Source: `data-fields/budget-column-type.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 30 of 31 inventoried |
| Physical tables | `budget_column_type` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 34 (34 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 16 keys from 8 record types |
| Points at | 4 other records |
| Tenancy position | firm_global |
| Rules that name it | 0 |

## What to know before rebuilding this

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### Lands in budget_column_type

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 30 fields carry a vendor definition

**Observed.** 30 of this record's 31 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 20 fields marked required

**Observed.** The inventory marks 20 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetViewID` | Budget View | This is the budget view selected for the budget type. Budget views allow you to control which line items bidders can update. | Budget Template View ID | Global |  | `budget_column_type.BudgetViewID · TEXT` | [BudgetView](BudgetView.md) |
| `EditControllerID` | Use this Budget View for Edit Control |  | Budget Template View ID | Global |  | `budget_column_type.EditControllerID · TEXT` | [BudgetView](BudgetView.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeStatusDefaultID` | Default Status | This is the default status for budget columns of this type. You can configure this on the Manage Budget Types page. | Dropdown (Budget Status) | Global |  | `budget_column_type.CodeStatusDefaultID · TEXT` | Budget Status |
| `CodeStatusSelectedID` | Status | This is the selected status for budget columns of this type. You can configure this on the Manage Budget Types page. | Dropdown (Budget Status) | Global | yes | `budget_column_type.CodeStatusSelectedID · TEXT` | Budget Status |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnTypeID` | Budget Column Type RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `budget_column_type.BudgetColumnTypeID · VARCHAR(64) NOT NULL` |  |
| `ReportGroupAvailableFieldID` | Report Group Available Field | The reporting field that is associated with the object. | Number | Global |  | `budget_column_type.ReportGroupAvailableFieldID · TEXT` |  |

### Flags (17)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllowMultiSelect` | Allow Multi Select? | Select this check box to allow multiple budget versions with a status of Selected. If this check box is selected, then: If multiple budget versions have the same status, the most recently updated budget version will display on the Budget Summary page. If one budget version has the Default status and one budget version has the Selected status, the budget version with the Selected status will display on the Budget Summary page. If this check box is not selected, the budget type that has a status of Selected will appear on the Budget Summary page. | Boolean | Global | yes | `budget_column_type.AllowMultiSelect · TEXT` |  |
| `AllowOneInstance` | Allow One Instance? | Select this check box to allow only one version of this budget type per entity. This is the "indirect" method of populating your budget, used when populating your budget via a custom list in a form or a backend integration. Once you select the Allow one instance of this type per project check box and save the budget type, you cannot change this setting. If your budget will be updated via custom list, integration, or backend update, this check box must be selected. | Boolean | Global | yes | `budget_column_type.AllowOneInstance · TEXT` |  |
| `AllowUIEditForBudgetColumn` | Budget Editable? | Select this check box to allow editing of the budget from the Budget tab of the entity. This setting also allows for budget versioning. | Boolean | Global | yes | `budget_column_type.AllowUIEditForBudgetColumn · TEXT` |  |
| `IsBidTemplate` | Is Bid Template | This check box is used to link budget types that are used for bidding with budget types that are used for bid conditioning. | Boolean | Global | yes | `budget_column_type.IsBidTemplate · TEXT` |  |
| `IsForBidLeveling` | Is For Bid Leveling? | Select this check box if this budget type will be used for adjusting submitted bids through the bidding work flow. | Boolean | Global | yes | `budget_column_type.IsForBidLeveling · TEXT` |  |
| `IsForBidding` | Is For Bidding? | Select this check box if this budget type is updated from the bid process. The budget values for a bid budget type will be updated via work flow. | Boolean | Global | yes | `budget_column_type.IsForBidding · TEXT` |  |
| `IsValidForCapProgram` | Valid For Capital Program? | This check box indicates that this record type is valid for a program / capital program. | Boolean | Global | yes | `budget_column_type.IsValidForCapProgram · TEXT` |  |
| `IsValidForCapProject` | Valid For Capital Project? | This check box indicates that this record type is valid for a capital project. | Boolean | Global | yes | `budget_column_type.IsValidForCapProject · TEXT` |  |
| `IsValidForContract` | Valid For RE Contract? | This check box indicates that this record type is valid for a contract. | Boolean | Global | yes | `budget_column_type.IsValidForContract · TEXT` |  |
| `IsValidForEquipContract` | Valid For Equipment Contract? | This check box indicates that this record type is valid for an equipment contract. | Boolean | Global | yes | `budget_column_type.IsValidForEquipContract · TEXT` |  |
| `IsValidForFacility` | Valid For Facility? | This check box indicates that this record type is valid for a facility. | Boolean | Global | yes | `budget_column_type.IsValidForFacility · TEXT` |  |
| `IsValidForLocation` | Valid For Location? | This check box indicates that this record type is valid for a location. | Boolean | Global | yes | `budget_column_type.IsValidForLocation · TEXT` |  |
| `IsValidForOpenProject` | Valid For Opening Project? | This check box indicates that this record type is valid for a project / opening project. | Boolean | Global | yes | `budget_column_type.IsValidForOpenProject · TEXT` |  |
| `IsValidForParcel` | Valid For Parcel? | This check box indicates that this record type is valid for a parcel. | Boolean | Global | yes | `budget_column_type.IsValidForParcel · TEXT` |  |
| `IsValidForPortfolio` | Valid For Portfolio? | This check box indicates that this record type is valid for a portfolio. | Boolean | Global | yes | `budget_column_type.IsValidForPortfolio · TEXT` |  |
| `IsValidForPotentialProject` | Valid For Site? | This check box indicates that this record type is valid for a site / potential project. | Boolean | Global | yes | `budget_column_type.IsValidForPotentialProject · TEXT` |  |
| `IsValidForPrototype` | Valid For Prototype? | This check box indicates that this record type is valid for a prototype. | Boolean | Global | yes | `budget_column_type.IsValidForPrototype · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnTypeName` | Name | Enter the name of the budget type in this field. | Text | Global | yes | `budget_column_type.BudgetColumnTypeName · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `budget_column_type.Description · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Column Type ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `budget_column_type.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `budget_column_type.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `budget_column_type.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `budget_column_type.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `budget_column_type.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `budget_column_type.RevNumber · TEXT` |  |

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
