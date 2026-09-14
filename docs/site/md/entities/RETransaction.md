# RETransaction

*31 fields · module: Portfolio & Real-Estate Transactions · Postgres: `r_e_transaction`*

The formal real-estate transaction record once a Scenario converts into an active deal — approved capital budget, deal schedule, and begin date. 30 Global fields under RE Transaction; sits between Scenario (evaluation) and Contract (executed lease) in the deal lifecycle.

Source: `data-fields/re-transaction.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 4 keys from 4 record types |
| Points at | 14 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 7 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActiveDealStepTaskIDList` | Active Deal Step(s) | Task/Group ID | Global |  | [TaskGroup](TaskGroup.md) |
| `AssigneeMemberID` | Transaction Manager | Member ID | Global |  | [Member](Member.md) |
| `DealSchedule` | Deal Schedule | Task/Group ID | Global |  | [TaskGroup](TaskGroup.md) |
| `FacilityID` | Facility | Facility ID | Global |  | [Facility](Facility.md) |
| `KickoffContractTermID` | Kickoff Contract Term | Contract Term ID | Global |  | [ContractTerm](ContractTerm.md) |
| `KickoffCovenantID` | Kickoff Contract Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `KickoffScenarioID` | Kickoff Scenario | Scenario ID | Global |  | [Scenario](Scenario.md) |
| `PreferredScenarioID` | Preferred Scenario | Scenario ID | Global |  | [Scenario](Scenario.md) |
| `ProgramID` | Program | Portfolio ID | Global | yes | [Program](Program.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `RelatedTransactionID` | Related Transaction | RE Transaction ID | Global |  | [RETransaction](RETransaction.md) |
| `SelectedScenarioID` | Selected Scenario | Scenario ID | Global |  | [Scenario](Scenario.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DocumentIDList` | Documents | Document List | Global |  |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeRETransactionStatusID` | Transaction Status | Dropdown (RE Transaction Status Code) | Global |  | RE Transaction Status Code |
| `PreferredScenarioCodeDealTypeID` | Preferred Scenario Deal Type | Dropdown (Scenario Deal Type Code) | Global |  | Scenario Deal Type Code |

### Money (1)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ApprovedCapitalBudget` | Approved Capital Budget | Currency | Global |  |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `NumberOfScenarios` | Number of Scenarios | Number | Global |  |  |
| `RETransactionID` | RE Transaction RecID | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global |  |  |
| `EndDate` | End Date | Date | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DealStepSchedule` | Deal Steps | Text | Global |  |  |
| `KickoffKeyDateID` | Kickoff Contract Key Date | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PreferredScenarioCovenantNotes` | Preferred Scenario Covenant Notes | Text | Global |  |  |
| `TransactionName` | Transaction Name | Text | Global | yes |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | RE Transaction ClientID | Text | Global | yes |  |
| `CreatedByID` | Created By | Member ID | Global |  | [Member](Member.md) |
| `CreatedDate` | Created Date | Time | Global |  |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
| `RevNumber` | Rev Number | Number | Global |  |  |

## What points here (4 keys)

| Record type | Via column |
|---|---|
| [LinkReTransScenContact](LinkReTransScenContact.md) | `RETransactionID` |
| [MapClientSchedule](MapClientSchedule.md) | `RETransactionID` |
| [RETransaction](RETransaction.md) | `RelatedTransactionID` |
| [Scenario](Scenario.md) | `RETransactionID` |
