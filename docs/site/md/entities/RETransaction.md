# RETransaction

*31 fields · module: Portfolio & Real-Estate Transactions · Postgres: `r_e_transaction`*

The formal real-estate transaction record once a Scenario converts into an active deal — approved capital budget, deal schedule, and begin date. 30 Global fields under RE Transaction; sits between Scenario (evaluation) and Contract (executed lease) in the deal lifecycle.

Source: `data-fields/re-transaction.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 24 of 31 inventoried |
| Physical tables | `r_e_transaction` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 4 keys from 4 record types |
| Points at | 14 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 7 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in r_e_transaction

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 24 fields carry a vendor definition

**Observed.** 24 of this record's 31 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 3 fields marked required

**Observed.** The inventory marks 3 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [POR-R-005](../rules/POR-R-005.md) | A `PotentialProject`, `Program`, `Scenario`, or `RETransaction` needs a deal classification · `PotentialProject.CodeDealTypeID` / `Program.CodeDealTypeID` → `Deal Type Code` (2024); `Scenario.CodeScenarioDealTypeID` / `RETransaction.Preferr | Observed |
| [POR-R-006](../rules/POR-R-006.md) | A `RETransaction` is opened against a site the tenant may already occupy · `RETransaction.FacilityID` · Optional direct FK to an existing `Facility` — a renewal/expansion transaction can name its Facility before any Scenario or Contract exi | Observed |
| [POR-R-007](../rules/POR-R-007.md) | A rollout program needs capacity tracking · `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` · Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/` | Derived |
| [POR-R-013](../rules/POR-R-013.md) | `RETransaction` is created · `RETransaction.ProgramID` · Required — a transaction must belong to a Portfolio. · Observed | Observed |
| [POR-R-015](../rules/POR-R-015.md) | A `Scenario`'s deal type needs comparing against its parent transaction's preference · `Scenario.CodeScenarioDealTypeID` vs. `RETransaction.PreferredScenarioCodeDealTypeID` · Both draw from the same code table (`Scenario Deal Type Code`, 20 | Derived |
| [POR-R-016](../rules/POR-R-016.md) | `Task`/`TaskGroup`-typed columns on `RETransaction`/`Scenario` (`ActiveDealStepTaskIDList`, `DealSchedule`) are read · `Task/Group ID` FK type · The graph-building script resolves this ambiguous type to `TaskGroup` specifically, but `Task`, | Derived |
| [PRJ-R-013](../rules/PRJ-R-013.md) | A real-estate deal step needs its own schedule · `RETransaction.DealSchedule`/`ActiveDealStepTaskIDList`, `Scenario.DealSchedule`/`ActiveDealStepTaskIDList` (`portfolio-transactions`) · Both reuse `TaskGroup` directly — the deal pipeline ha | Observed |

## Fields

### Relationships (foreign keys) (12)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActiveDealStepTaskIDList` | Active Deal Step(s) |  | Task/Group ID | Global |  | `r_e_transaction.ActiveDealStepTaskIDList · TEXT` | [TaskGroup](TaskGroup.md) |
| `AssigneeMemberID` | Transaction Manager | Select the name of the transaction manager or whoever owns the transaction. | Member ID | Global |  | `r_e_transaction.AssigneeMemberID · TEXT` | [Member](Member.md) |
| `DealSchedule` | Deal Schedule |  | Task/Group ID | Global |  | `r_e_transaction.DealSchedule · TEXT` | [TaskGroup](TaskGroup.md) |
| `FacilityID` | Facility | The facility that the transaction is associated with. | Facility ID | Global |  | `r_e_transaction.FacilityID · TEXT` | [Facility](Facility.md) |
| `KickoffContractTermID` | Kickoff Contract Term |  | Contract Term ID | Global |  | `r_e_transaction.KickoffContractTermID · TEXT` | [ContractTerm](ContractTerm.md) |
| `KickoffCovenantID` | Kickoff Contract Covenant |  | Covenant ID | Global |  | `r_e_transaction.KickoffCovenantID · TEXT` | [Covenant](Covenant.md) |
| `KickoffScenarioID` | Kickoff Scenario |  | Scenario ID | Global |  | `r_e_transaction.KickoffScenarioID · TEXT` | [Scenario](Scenario.md) |
| `PreferredScenarioID` | Preferred Scenario | This field has not been implemented for this functionality. | Scenario ID | Global |  | `r_e_transaction.PreferredScenarioID · TEXT` | [Scenario](Scenario.md) |
| `ProgramID` | Program | The portfolio that the transaction belongs to. | Portfolio ID | Global | yes | `r_e_transaction.ProgramID · TEXT` | [Program](Program.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `r_e_transaction.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `RelatedTransactionID` | Related Transaction | Select any transaction that is related or similar to this transaction record. | RE Transaction ID | Global |  | `r_e_transaction.RelatedTransactionID · TEXT` | [RETransaction](RETransaction.md) |
| `SelectedScenarioID` | Selected Scenario | Select the scenario which has been selected to go forward for this transaction. | Scenario ID | Global |  | `r_e_transaction.SelectedScenarioID · TEXT` | [Scenario](Scenario.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DocumentIDList` | Documents | This is a generic field that allows you to add documents to the transaction from the Documents page. This field also allows you to upload new documents to the entity and attach them to the transaction. | Document List | Global |  | `r_e_transaction.DocumentIDList · TEXT` |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeRETransactionStatusID` | Transaction Status | Select the current phase of the transaction. | Dropdown (RE Transaction Status Code) | Global |  | `r_e_transaction.CodeRETransactionStatusID · TEXT` | RE Transaction Status Code |
| `PreferredScenarioCodeDealTypeID` | Preferred Scenario Deal Type | This field has not been implemented for this functionality. | Dropdown (Scenario Deal Type Code) | Global |  | `r_e_transaction.PreferredScenarioCodeDealTypeID · TEXT` | Scenario Deal Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ApprovedCapitalBudget` | Approved Capital Budget | On a lease, enter the cost of improvements that are not covered by the tenant improvement allowance. On a purchase, enter the deposit or equity amount contributed by the buyer, or the cash the buyer brings to closing. | Currency | Global |  | `r_e_transaction.ApprovedCapitalBudget · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `NumberOfScenarios` | Number of Scenarios | The total number of scenarios linked to this transaction record. | Number | Global |  | `r_e_transaction.NumberOfScenarios · TEXT` |  |
| `RETransactionID` | RE Transaction RecID | The RETransactionID field is a system-assigned identifier for an individual transaction record. | Number | Global |  | `r_e_transaction.RETransactionID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | This field has not been implemented for this functionality. | Date | Global |  | `r_e_transaction.BeginDate · TEXT` |  |
| `EndDate` | End Date | This field has not been implemented for this functionality. | Date | Global |  | `r_e_transaction.EndDate · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DealStepSchedule` | Deal Steps | The deal step schedule for the transaction. | Text | Global |  | `r_e_transaction.DealStepSchedule · TEXT` |  |
| `KickoffKeyDateID` | Kickoff Contract Key Date |  | Text | Global |  | `r_e_transaction.KickoffKeyDateID · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `r_e_transaction.Notes · TEXT` |  |
| `PreferredScenarioCovenantNotes` | Preferred Scenario Covenant Notes | This field has not been implemented for this functionality. | Text | Global |  | `r_e_transaction.PreferredScenarioCovenantNotes · TEXT` |  |
| `TransactionName` | Transaction Name | Enter a name for the transaction. | Text | Global | yes | `r_e_transaction.TransactionName · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | RE Transaction ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `r_e_transaction.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `r_e_transaction.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `r_e_transaction.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `r_e_transaction.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `r_e_transaction.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `r_e_transaction.RevNumber · TEXT` |  |

## What points here (4 keys)

| Record type | Via column |
|---|---|
| [LinkReTransScenContact](LinkReTransScenContact.md) | `RETransactionID` |
| [MapClientSchedule](MapClientSchedule.md) | `RETransactionID` |
| [RETransaction](RETransaction.md) | `RelatedTransactionID` |
| [Scenario](Scenario.md) | `RETransactionID` |
