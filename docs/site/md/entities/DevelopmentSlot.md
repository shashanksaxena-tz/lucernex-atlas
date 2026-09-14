# DevelopmentSlot

*31 fields · module: Portfolio & Real-Estate Transactions · Postgres: `development_slot`*

A build-out slot within a development pipeline plan — assigned broker/project, current revenue weeks, and duration, feeding ProgramRevenueWeeks reporting. 30 Global fields under RE Planner.

Source: `data-fields/development-slot.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 10 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [POR-R-007](../rules/POR-R-007.md) | A rollout program needs capacity tracking · `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` · Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/` | Derived |

## Fields

### Relationships (foreign keys) (9)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BrokerMemberID` | Assigned Broker | Member ID | Global |  | [Member](Member.md) |
| `ProgramID` | Portfolio | Portfolio ID | Global | yes | [Program](Program.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |
| `ProjectPEID` | Slot Entity | Entity ID | Global |  | [ProjectEntity](ProjectEntity.md) |
| `PrototypeID` | Prototype | Prototype ID | Global |  | [Prototype](Prototype.md) |
| `RegionID` | Region | Region ID | Global | yes | [Region](Region.md) |
| `RootRegionID` | Parent Region | Region ID | Global |  | [Region](Region.md) |
| `SubRegionID` | Sub Region | Region ID | Global |  | [Region](Region.md) |
| `TaskTemplatePEID` | Task Template Project Entity ID | Template ID | Global |  | [TaskTemplate](TaskTemplate.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeMarketAreaID` | Market Area | Dropdown (Market Area Code) | Global | yes | Market Area Code |
| `CodeMarketTypeID` | Market Type | Dropdown (Market Type Code) | Global |  | Market Type Code |
| `CodeSlotTypeID` | Target Type | Dropdown (Slot Type Code) | Global |  | Slot Type Code |
| `CodeStorePhaseID` | Store Phase | Dropdown (Store Phase Code) | Global |  | Store Phase Code |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Current Revenue Weeks | Number | Global |  |  |
| `DevelopmentSlotID` | Target RecID | Number | Global |  |  |
| `Duration` |  | Number | Global |  |  |
| `SlotDuration` | Slot Duration | Number | Global |  |  |

### Dates & timestamps (6)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BaselineEndDate` | Planned Open Date | Date | Global |  |  |
| `EndDate` |  | Date | Global | yes |  |
| `OriginalEndDate` | Original Planned Open Date | Date | Global |  |  |
| `PlannedPackageDate` | Planned Package Date | Date | Global |  |  |
| `SlotEndDate` | Target End Date | Date | Global |  |  |
| `SlotStartDate` | Target Start Date | Date | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BrokerMessage` | Broker Message | Text | Global |  |  |
| `DevelopmentPlanID` | Development Plan | Text | Global | yes |  |
| `DevelopmentSlotName` | Name | Text | Global | yes |  |
| `ProjectName` | Assigned Project | Text | Global |  |  |
| `TradeArea` | Trade Area | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Target ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
