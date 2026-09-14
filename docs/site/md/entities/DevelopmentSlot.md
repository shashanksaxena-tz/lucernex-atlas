# DevelopmentSlot

*31 fields · module: Portfolio & Real-Estate Transactions · Postgres: `development_slot`*

A build-out slot within a development pipeline plan — assigned broker/project, current revenue weeks, and duration, feeding ProgramRevenueWeeks reporting. 30 Global fields under RE Planner.

Source: `data-fields/development-slot.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 31 |
| Fields with a vendor definition | 30 of 31 inventoried |
| Physical tables | `development_slot` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 30 (30 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 10 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 1 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in development_slot

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 30 fields carry a vendor definition

**Observed.** 30 of this record's 31 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 7 of this record's fields required; the Data Fields catalogue marks 7; 7 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [POR-R-007](../rules/POR-R-007.md) | A rollout program needs capacity tracking · `DevelopmentPlan` → `DevelopmentSlot` → `ProgramRevenueWeeks` · Rolls up filled/unfilled slot and week counts per `Program`. No FK connects a `DevelopmentSlot` to the specific `PotentialProject`/` | Derived |

## Fields

### Relationships (foreign keys) (9)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BrokerMemberID` | Assigned Broker | Select the real estate broker to assign to this target from this field. In order to be listed in this field, the user must have the Broker contact type. | Member ID | Global |  | `development_slot.BrokerMemberID · TEXT` | [Member](Member.md) |
| `ProgramID` | Portfolio | The portfolio that this real estate plan is associated with. | Portfolio ID | Global | yes | `development_slot.ProgramID · TEXT` | [Program](Program.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `development_slot.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `ProjectPEID` | Slot Entity | The values in this field depend on the market area. You may or may not select the assigned site or project when initially creating your target. | Entity ID | Global |  | `development_slot.ProjectPEID · TEXT` | [ProjectEntity](ProjectEntity.md) |
| `PrototypeID` | Prototype | Select the prototype that should be associated with the target from this field. Only prototypes that belong to this portfolio can be selected from this field. | Prototype ID | Global |  | `development_slot.PrototypeID · TEXT` | [Prototype](Prototype.md) |
| `RegionID` | Region | Select the region and sub-region from this field. The values that appear in this field depend on the org chart of the portfolio. | Region ID | Global | yes | `development_slot.RegionID · TEXT` | [Region](Region.md) |
| `RootRegionID` | Parent Region | This field sets some default membership at the creation of the entity. Its values are pulled from the organization chart. | Region ID | Global |  | `development_slot.RootRegionID · TEXT` | [Region](Region.md) |
| `SubRegionID` | Sub Region | The sub-region. | Region ID | Global |  | `development_slot.SubRegionID · TEXT` | [Region](Region.md) |
| `TaskTemplatePEID` | Task Template Project Entity ID | Select the appropriate schedule template from this field. If you select a schedule from this field, the Duration in Days field will become read-only. The value of the Duration in Days field will be calculated by the length of the schedule. | Template ID | Global |  | `development_slot.TaskTemplatePEID · TEXT` | [TaskTemplate](TaskTemplate.md) |

### Coded values (drop-downs) (4)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeMarketAreaID` | Market Area | This is a default field that is not used for this record type. | Dropdown (Market Area Code) | Global | yes | `development_slot.CodeMarketAreaID · TEXT` | Market Area Code |
| `CodeMarketTypeID` | Market Type | This is a generic field. It is not implemented for this record type. | Dropdown (Market Type Code) | Global |  | `development_slot.CodeMarketTypeID · TEXT` | Market Type Code |
| `CodeSlotTypeID` | Target Type | Select the target type from this field. | Dropdown (Slot Type Code) | Global |  | `development_slot.CodeSlotTypeID · TEXT` | Slot Type Code |
| `CodeStorePhaseID` | Store Phase | Select the store phase from this field. | Dropdown (Store Phase Code) | Global |  | `development_slot.CodeStorePhaseID · TEXT` | Store Phase Code |

### Quantities (4)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActualRevenueWeeks` | Current Revenue Weeks | Calculates how many actual revenue weeks this entity will exist during the fiscal year. | Number | Global |  | `development_slot.ActualRevenueWeeks · TEXT` |  |
| `DevelopmentSlotID` | Target RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `development_slot.DevelopmentSlotID · VARCHAR(64) NOT NULL` |  |
| `Duration` |  | If you selected a schedule, this field will be read-only. If you did not select a schedule, enter the duration in days for this target. | Number | Global |  | `development_slot.Duration · TEXT` |  |
| `SlotDuration` | Slot Duration | If you selected a schedule, this field will calculate the duration of the target in days. | Number | Global |  | `development_slot.SlotDuration · TEXT` |  |

### Dates & timestamps (6)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BaselineEndDate` | Planned Open Date | The baseline end date for the entity utilizing the schedules. If there is a milestone timeline the system uses the max end date from all non-operating tasks, otherwise it uses the max end date from the schedule. | Date | Global |  | `development_slot.BaselineEndDate · TEXT` |  |
| `EndDate` |  | The End Date field allows you to select an end date for the record. | Date | Global | yes | `development_slot.EndDate · TEXT` |  |
| `OriginalEndDate` | Original Planned Open Date | The baseline end date of a schedule task on the entity. | Date | Global |  | `development_slot.OriginalEndDate · TEXT` |  |
| `PlannedPackageDate` | Planned Package Date | Select the date that the real estate package will be or was presented to the committee. | Date | Global |  | `development_slot.PlannedPackageDate · TEXT` |  |
| `SlotEndDate` | Target End Date | Calculates the end date of your target. | Date | Global |  | `development_slot.SlotEndDate · TEXT` |  |
| `SlotStartDate` | Target Start Date | Calculates the start date of your target. | Date | Global |  | `development_slot.SlotStartDate · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BrokerMessage` | Broker Message | Enter a message to your broker in this field. | Text | Global |  | `development_slot.BrokerMessage · TEXT` |  |
| `DevelopmentPlanID` | Development Plan | The ID of the development plan that this development slot belongs to. | Text | Global | yes | `development_slot.DevelopmentPlanID · TEXT` |  |
| `DevelopmentSlotName` | Name | Enter the name of the target in this field. | Text | Global | yes | `development_slot.DevelopmentSlotName · TEXT` |  |
| `ProjectName` | Assigned Project | The name of the project associated with the record. | Text | Global |  | `development_slot.ProjectName · TEXT` |  |
| `TradeArea` | Trade Area | Enter the trade area in this field. | Text | Global |  | `development_slot.TradeArea · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Target ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `development_slot.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `development_slot.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `development_slot.ModifiedDate · TEXT` |  |
