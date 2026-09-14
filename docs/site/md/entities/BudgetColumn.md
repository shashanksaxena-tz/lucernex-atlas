# BudgetColumn

*21 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `budget_column`*

One column within a capital project budget (e.g., 'Original Budget', 'Approved Change Orders') — status, type, and an 'Allow UI Edit?' flag, the representative example walked through in 005's own documentation. 20 Global fields under Budget.

Source: `data-fields/budget-column.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 21 |
| Fields with a vendor definition | 20 of 21 inventoried |
| Physical tables | `budget_column` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 20 (20 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in budget_column

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 20 fields carry a vendor definition

**Observed.** 20 of this record's 21 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 20 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 7 are marked required.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnTypeID` | Budget Column Type | The budget type ID. | Budget Type ID | Global | yes | `budget_column.BudgetColumnTypeID · TEXT` | [BudgetColumnType](BudgetColumnType.md) |
| `BudgetTemplateID` | Budget Template | If there is a budget template associated with this entity, The foreign key of the budget template. | Template ID | Global | yes | `budget_column.BudgetTemplateID · TEXT` | [BudgetTemplate](BudgetTemplate.md) |
| `CreatedByMemberID` | Created By Member | The member ID of the person who added the budget type. | Member ID | Global | yes | `budget_column.CreatedByMemberID · TEXT` | [Member](Member.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `budget_column.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `ThirdPartyVendorID` | Third Party Vendor | This captures the vendor ID of a bidder who has submitted a bid on a bidding budget column. | Employer ID | Global |  | `budget_column.ThirdPartyVendorID · TEXT` | [Employer](Employer.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeBudgetColumnStatusID` | Budget Column Status | The status of the budget column. | Dropdown (Budget Status) | Global | yes | `budget_column.CodeBudgetColumnStatusID · TEXT` | Budget Status |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BudgetColumnID` | Budget Column RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `budget_column.BudgetColumnID · VARCHAR(64) NOT NULL` |  |
| `SealedBidNumber` | Sealed Bid Number | The ID for a sealed bid. | Number | Global |  | `budget_column.SealedBidNumber · TEXT` |  |
| `SequenceNumber` | Sequence Number | This field generates a sequence number for the record. The next record created receives the next number in the sequence. | Number | Global | yes | `budget_column.SequenceNumber · TEXT` |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AllowUIEdit` | Allow UI Edit? | This flag indicates whether the values of this budget type can be modified within the user interface. | Boolean | Global |  | `budget_column.AllowUIEdit · TEXT` |  |
| `Inactive` | Is Inactive? | If the budget column is inactive, this flag is set to TRUE. If the budget column is active, this flag is set to FALSE. | Boolean | Global | yes | `budget_column.Inactive · TEXT` |  |
| `IsLocked` | Is Locked? | If this budget column is locked, the value of this field is true. | Boolean | Global |  | `budget_column.IsLocked · TEXT` |  |
| `IsSelected` | Is Selected? | If this budget column is selected, the value of this field is true. | Boolean | Global |  | `budget_column.IsSelected · TEXT` |  |

### Text & notes (4)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BidPackageID` | Bid Package | The ID of the bid package associated with this bidder form. | Text | Global |  | `budget_column.BidPackageID · TEXT` |  |
| `BudgetColumnName` | Budget Column Name | The budget type name. | Text | Global |  | `budget_column.BudgetColumnName · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `budget_column.Description · TEXT` |  |
| `InitializedFromBudgetColumnID` | Initialized From Budget Column | If the user chooses to copy the initial values for this budget type from another budget type, the ID of the budget type they copied. | Text | Global |  | `budget_column.InitializedFromBudgetColumnID · TEXT` |  |

### Audit & record keeping (4)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Budget Column ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `budget_column.BOMapClientRecordID · TEXT` |  |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `budget_column.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `budget_column.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `budget_column.ModifiedDate · TEXT` |  |
