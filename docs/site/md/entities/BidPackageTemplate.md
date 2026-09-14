# BidPackageTemplate

*32 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `bid_package_template`*

A reusable bid solicitation template — pre-assigns the page layouts used at each stage of a bid (Award, Invitation) and default budget view/column types, so a new BidPackage doesn't need each layout chosen manually. 31 Global fields under Specialized Forms.

Source: `data-fields/bid-package-template.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 32 |
| Catalogued fields | 31 (31 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 1 keys from 1 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (9)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AwardApprovalLayoutID` | Award Approval Layout | item ID | Global |  | unresolved |
| `BidAwardLayoutID` | Bid Award Layout | item ID | Global |  | unresolved |
| `BidColumnTypeID` | Bid Column Type | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `BidInvitationLayoutID` | Bid Invitation Layout | item ID | Global | yes | unresolved |
| `BidPackageKickoffLayoutID` | Bid Package Kickoff Layout | item ID | Global | yes | unresolved |
| `BudgetViewID` | Bid Budget View | Budget Template View ID | Global | yes | [BudgetView](BudgetView.md) |
| `EstimateBudgetColumnTypeID` | Bid Estimate Budget Column Type | Budget Type ID | Global |  | [BudgetColumnType](BudgetColumnType.md) |
| `PostAwardLayoutID` | Post Award Layout | item ID | Global |  | unresolved |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (3)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodePreAcceptUserClassID` | Bid Pre-Accept User Class | Dropdown (User Class) | Global |  | User Class |
| `DefaultAssigneeCodeJobTitleIDList` | Default Assignee Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |
| `QnACodeJobTitleIDList` | Default Job Title List | Dropdown (Job Title Code) | Global |  | Job Title Code |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BidPackageTemplateID` | Bid Package Template RecID | Number | Global |  |  |

### Flags (11)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsValidForCapProgram` | Bid Package Template Valid for Cap Program? | Boolean | Global |  |  |
| `IsValidForCapProject` | Bid Package Template Valid for Cap Project? | Boolean | Global |  |  |
| `IsValidForContract` | Bid Package Template Valid for RE Contract? | Boolean | Global |  |  |
| `IsValidForEquipContract` | Bid Package Template Valid for Equipment Contract? | Boolean | Global |  |  |
| `IsValidForFacility` | Bid Package Template Valid for Facility? | Boolean | Global |  |  |
| `IsValidForLocation` | Bid Package Template Valid for Location? | Boolean | Global |  |  |
| `IsValidForOpenProject` | Bid Package Template Valid for Open Project? | Boolean | Global |  |  |
| `IsValidForParcel` | Bid Package Template Valid for Parcel? | Boolean | Global |  |  |
| `IsValidForPortfolio` | Bid Package Template Valid for Portfolio? | Boolean | Global |  |  |
| `IsValidForPotentialProject` | Bid Package Template Valid for Potential Project? | Boolean | Global |  |  |
| `IsValidForPrototype` | Bid Package Template Valid for Prototype? | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` | Bid Package Template Description | Text | Global |  |  |
| `Notes` | Bid Package Template Notes | Text | Global |  |  |
| `TemplateName` | Bid Package Template Name | Text | Global |  |  |

### Audit & record keeping (5)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (1 keys)

| Record type | Via column |
|---|---|
| [BidPackage](BidPackage.md) | `BidPackageTemplateID` |
