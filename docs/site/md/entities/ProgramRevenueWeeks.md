# ProgramRevenueWeeks

*13 fields · module: Portfolio & Real-Estate Transactions · Postgres: `program_revenue_weeks`*

Weekly revenue-target tracking (filled/unfilled targets and weeks) for a development Program, feeding DevelopmentSlot planning.

Source: `data-fields/small-miscellaneous-entities.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 13 |
| Catalogued fields | 14 (14 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
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

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Quantities (9)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `NumberCurrentFilledSlots` | Current Filled Targets | Number | Global |  |  |
| `NumberCurrentFilledWeeks` | Current Filled Weeks | Number | Global |  |  |
| `NumberCurrentTotalSlots` | Current Targets | Number | Global |  |  |
| `NumberCurrentTotalWeeks` | Current Weeks | Number | Global |  |  |
| `NumberCurrentUnfilledSlots` | Current Unfilled Targets | Number | Global |  |  |
| `NumberCurrentUnfilledWeeks` | Current Unfilled Weeks | Number | Global |  |  |
| `NumberOfSlots` | Goal Targets | Number | Global | yes |  |
| `ProgramRevenueWeeksID` | Program Revenue Weeks RecID | Number | Global |  |  |
| `RevenueWeeks` | Goal Weeks | Number | Global | yes |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Program Revenue Weeks ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
