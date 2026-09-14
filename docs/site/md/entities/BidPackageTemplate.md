# BidPackageTemplate

*32 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `bid_package_template`*

A reusable bid solicitation template — pre-assigns the page layouts used at each stage of a bid (Award, Invitation) and default budget view/column types, so a new BidPackage doesn't need each layout chosen manually. 31 Global fields under Specialized Forms.

Source: `data-fields/bid-package-template.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 32 |
| Fields with a vendor definition | 31 of 32 inventoried |
| Physical tables | `bid_package_template` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 31 (31 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in bid_package_template

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 31 fields carry a vendor definition

**Observed.** 31 of this record's 32 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 3 of this record's fields required; the Data Fields catalogue marks 3; 3 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (9)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AwardApprovalLayoutID` | Award Approval Layout | Select the kickoff form for the work flow which should be used for your bid award approval process. | item ID | Global |  | `bid_package_template.AwardApprovalLayoutID · TEXT` | unresolved |
| `BidAwardLayoutID` | Bid Award Layout | Select the form layout you used to configure the email sent to your winning bidder. | item ID | Global |  | `bid_package_template.BidAwardLayoutID · TEXT` | unresolved |
| `BidColumnTypeID` | Bid Column Type | Select the budget column which should be used to contain your bidder's submitted bids. | Budget Type ID | Global |  | `bid_package_template.BidColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `BidInvitationLayoutID` | Bid Invitation Layout | Select the form layout you used to configure the bid invitation email. | item ID | Global | yes | `bid_package_template.BidInvitationLayoutID · TEXT` | unresolved |
| `BidPackageKickoffLayoutID` | Bid Package Kickoff Layout | Select the form layout which should be used to kick off your bid package. This form layout is used to configure the appearance of the Add Bid Package window. | item ID | Global | yes | `bid_package_template.BidPackageKickoffLayoutID · TEXT` | unresolved |
| `BudgetViewID` | Bid Budget View | Select the budget view which should be associated with this bid package template. Budget views limit the line items that your vendors can see. | Budget Template View ID | Global | yes | `bid_package_template.BudgetViewID · TEXT` | [BudgetView](BudgetView.md) |
| `EstimateBudgetColumnTypeID` | Bid Estimate Budget Column Type | Select the budget column which should be used to contain the estimated values for your budget line items. | Budget Type ID | Global |  | `bid_package_template.EstimateBudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `PostAwardLayoutID` | Post Award Layout | Select the kickoff form for the work flow which should be kicked off after the bid package has been awarded. | item ID | Global |  | `bid_package_template.PostAwardLayoutID · TEXT` | unresolved |
| `ProjectEntityID` |  |  | Entity ID | — |  | `bid_package_template.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodePreAcceptUserClassID` | Bid Pre-Accept User Class | This field is a placeholder in preparation for an upcoming enhancement. | Dropdown (User Class) | Global |  | `bid_package_template.CodePreAcceptUserClassID · TEXT` | User Class |
| `DefaultAssigneeCodeJobTitleIDList` | Default Assignee Job Title List | This field is used to set the default assignee for a bid package on a bid package template. This setting is configured by job title. | Dropdown (Job Title Code) | Global |  | `bid_package_template.DefaultAssigneeCodeJobTitleIDList · TEXT` | Job Title Code |
| `QnACodeJobTitleIDList` | Default Job Title List | Select the job titles that should be assigned questions by default for this bid package template. | Dropdown (Job Title Code) | Global |  | `bid_package_template.QnACodeJobTitleIDList · TEXT` | Job Title Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidPackageTemplateID` | Bid Package Template RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `bid_package_template.BidPackageTemplateID · VARCHAR(64) NOT NULL` |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsValidForCapProgram` | Bid Package Template Valid for Cap Program? | This check box indicates that this record type is valid for a program / capital program. | Boolean | Global |  | `bid_package_template.IsValidForCapProgram · TEXT` |  |
| `IsValidForCapProject` | Bid Package Template Valid for Cap Project? | This check box indicates that this record type is valid for a capital project. | Boolean | Global |  | `bid_package_template.IsValidForCapProject · TEXT` |  |
| `IsValidForContract` | Bid Package Template Valid for RE Contract? | This check box indicates that this record type is valid for a contract. | Boolean | Global |  | `bid_package_template.IsValidForContract · TEXT` |  |
| `IsValidForEquipContract` | Bid Package Template Valid for Equipment Contract? | This check box indicates that this record type is valid for an equipment contract. | Boolean | Global |  | `bid_package_template.IsValidForEquipContract · TEXT` |  |
| `IsValidForFacility` | Bid Package Template Valid for Facility? | This check box indicates that this record type is valid for a facility. | Boolean | Global |  | `bid_package_template.IsValidForFacility · TEXT` |  |
| `IsValidForLocation` | Bid Package Template Valid for Location? | This check box indicates that this record type is valid for a location. | Boolean | Global |  | `bid_package_template.IsValidForLocation · TEXT` |  |
| `IsValidForOpenProject` | Bid Package Template Valid for Open Project? | This check box indicates that this record type is valid for a project / opening project. | Boolean | Global |  | `bid_package_template.IsValidForOpenProject · TEXT` |  |
| `IsValidForParcel` | Bid Package Template Valid for Parcel? | This check box indicates that this record type is valid for a parcel. | Boolean | Global |  | `bid_package_template.IsValidForParcel · TEXT` |  |
| `IsValidForPortfolio` | Bid Package Template Valid for Portfolio? | This check box indicates that this record type is valid for a portfolio. | Boolean | Global |  | `bid_package_template.IsValidForPortfolio · TEXT` |  |
| `IsValidForPotentialProject` | Bid Package Template Valid for Potential Project? | This check box indicates that this record type is valid for a site / potential project. | Boolean | Global |  | `bid_package_template.IsValidForPotentialProject · TEXT` |  |
| `IsValidForPrototype` | Bid Package Template Valid for Prototype? | This check box indicates that this record type is valid for a prototype. | Boolean | Global |  | `bid_package_template.IsValidForPrototype · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` | Bid Package Template Description | Write a description of the record. | Text | Global |  | `bid_package_template.Description · TEXT` |  |
| `Notes` | Bid Package Template Notes | Add any notes about the record. | Text | Global |  | `bid_package_template.Notes · TEXT` |  |
| `TemplateName` | Bid Package Template Name | Enter the name of the bid package template in this field. | Text | Global |  | `bid_package_template.TemplateName · TEXT` |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `bid_package_template.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `bid_package_template.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `bid_package_template.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `bid_package_template.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `bid_package_template.RevNumber · TEXT` |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [BidPackage](BidPackage.md) | `BidPackageTemplateID` |
