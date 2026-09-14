# KeyDate

*39 fields · module: Contracts & Leases · Postgres: `key_date`*

A tracked deadline/notice date tied to a Contract, Contract Term, or Covenant — action date/period (with a configurable period unit: days, months, etc.), earliest notice date, and coverage period bounds, used to drive renewal, termination, and compliance-notice alerts. 41 fields (31 Global, 10 Firm) under Contract; one of the entities the user specifically flagged, and its 10 Firm fields suggest ASG tracks additional tenant-specific deadline types beyond the base platform set.

Source: `data-fields/key-date.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 39 |
| Catalogued fields | 41 (31 global, 10 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### 7 tenant custom columns

**Observed.** This record carries 7 physical Firm_-prefixed columns — tenant custom fields are real columns, not rows in a value store, so adding one is a DDL change. That is direct evidence for database-per-tenant and against a shared schema.

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### 10 catalogued Firm-scope fields

**Observed.** Of 41 catalogued fields on this record, 10 are Firm scope — defined by this tenant rather than shipped by the platform. Firm-scope definitions are RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ContractTermID` | Contract Term | Contract Term ID | Global |  | [ContractTerm](ContractTerm.md) |
| `CovenantID` | Covenant | Covenant ID | Global |  | [Covenant](Covenant.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (9)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeActionPeriodUnitID` | Action Period Unit | Dropdown (Time Unit Code) | Global |  | Time Unit Code |
| `CodeFirstNoticePeriodUnitID` | Earliest Notice Period Unit | Dropdown (Time Unit Code) | Global |  | Time Unit Code |
| `CodeFrequencyID` | Frequency | Dropdown (Frequency Code) | Global |  | Frequency Code |
| `CodeKeyDateActionID` | Key Date Action | Dropdown (Key Date Action Code) | Global |  | Key Date Action Code |
| `CodeKeyDateGroupID` | Key Date Group | Dropdown (Key Date Group Code) | Global |  | Key Date Group Code |
| `CodeKeyDateTypeID` | Key Date Type | Dropdown (Key Date Type Code) | Global |  | Key Date Type Code |
| `CodeNoticePeriodUnitID` | Last Notice Period Unit | Dropdown (Time Unit Code) | Global |  | Time Unit Code |
| `Firm_Contingency` | Contingency | Dropdown (Custom Field) | Firm |  | Custom Field |
| `Firm_ContingencyTrigger` | Contingency Trigger | Dropdown (Custom Field) | Firm |  | Custom Field |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActionPeriod` | Action Period | Number | Global |  |  |
| `FirstNoticePeriod` | Earliest Notice Period | Number | Global |  |  |
| `KeyDateID` | Key Date RecID | Number | Global |  |  |
| `LengthOfTerm` | Length | Number | Global |  |  |
| `NoticePeriod` | Last Notice Period | Number | Global |  |  |

### Dates & timestamps (9)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActionDate` | Action Date | Date | Global |  |  |
| `BeginDate` | Coverage Period Begin Date | Date | Global |  |  |
| `EndDate` | Coverage Period End Date | Date | Global |  |  |
| `Firm_KeyDateEarliestTerminationDate` | Earliest Termination Date | Date | Firm |  |  |
| `Firm_KeyDateLatestTerminationDate` | Latest Termination Date | Date | Firm |  |  |
| `FirstEventBeginDate` | First Event Begin Date | Date | Global |  |  |
| `NoticeBeginDate` | Earliest Notice Date | Date | Global |  |  |
| `NoticeEndDate` | Last Notice Date | Date | Global |  |  |
| `TicklerDate` | Tickler Last Notice Date | Date | Global |  |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ActionComplete` | Is Action Complete? | Boolean | Global |  |  |
| `NoticeReceivedFlag` | Notice Received? | Boolean | Global |  |  |
| `NoticeSentFlag` | Notice Sent? | Boolean | Global |  |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `Description` |  | Text | Global |  |  |
| `Firm_KeyDateDocument` | Document | Text | Firm |  |  |
| `Firm_KeyDatePage` | Page | Text | Firm |  |  |
| `Firm_KeyDateSection` | Section | Text | Firm |  |  |
| `KeyDateEventTable` | Key Date Event Table | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Key Date ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
