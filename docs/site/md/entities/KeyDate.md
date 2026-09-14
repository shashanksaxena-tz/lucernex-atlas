# KeyDate

*39 fields · module: Contracts & Leases · Postgres: `key_date`*

A tracked deadline/notice date tied to a Contract, Contract Term, or Covenant — action date/period (with a configurable period unit: days, months, etc.), earliest notice date, and coverage period bounds, used to drive renewal, termination, and compliance-notice alerts. 41 fields (31 Global, 10 Firm) under Contract; one of the entities the user specifically flagged, and its 10 Firm fields suggest ASG tracks additional tenant-specific deadline types beyond the base platform set.

Source: `data-fields/key-date.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 39 |
| Fields with a vendor definition | 31 of 39 inventoried |
| Physical tables | `key_date` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in key_date

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 31 fields carry a vendor definition

**Observed.** 31 of this record's 39 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 2; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Fields

### Relationships (foreign keys) (4)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `key_date.ContractID · TEXT` | [Contract](Contract.md) |
| `ContractTermID` | Contract Term | The associated contract term record ID. | Contract Term ID | Global |  | `key_date.ContractTermID · TEXT` | [ContractTerm](ContractTerm.md) |
| `CovenantID` | Covenant | Select the covenant that the record is associated with from this field. | Covenant ID | Global |  | `key_date.CovenantID · TEXT` | [Covenant](Covenant.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `key_date.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (9)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeActionPeriodUnitID` | Action Period Unit | Select the units used for the tickler period - for example, days, weeks, months, or years. | Dropdown (Time Unit Code) | Global |  | `key_date.CodeActionPeriodUnitID · TEXT` | Time Unit Code |
| `CodeFirstNoticePeriodUnitID` | Earliest Notice Period Unit | Select the unit for the number of days, weeks, months, or years in advance that you can take action on the key date. | Dropdown (Time Unit Code) | Global |  | `key_date.CodeFirstNoticePeriodUnitID · TEXT` | Time Unit Code |
| `CodeFrequencyID` | Frequency | Select how often the key date occurs from this field. | Dropdown (Frequency Code) | Global |  | `key_date.CodeFrequencyID · TEXT` | Frequency Code |
| `CodeKeyDateActionID` | Key Date Action | Select the action you took from this field. | Dropdown (Key Date Action Code) | Global |  | `key_date.CodeKeyDateActionID · TEXT` | Key Date Action Code |
| `CodeKeyDateGroupID` | Key Date Group | The key date group is the first level of categorization for key date records. Groups are the parents of types. | Dropdown (Key Date Group Code) | Global |  | `key_date.CodeKeyDateGroupID · TEXT` | Key Date Group Code |
| `CodeKeyDateTypeID` | Key Date Type | The key date type is the second level of categorization for key date records. Types are the children of groups. If you select the Option type, this field becomes functional. | Dropdown (Key Date Type Code) | Global |  | `key_date.CodeKeyDateTypeID · TEXT` | Key Date Type Code |
| `CodeNoticePeriodUnitID` | Last Notice Period Unit | Select the units used for the notice period - for example, days, weeks, months, or years. | Dropdown (Time Unit Code) | Global |  | `key_date.CodeNoticePeriodUnitID · TEXT` | Time Unit Code |
| `Firm_Contingency` | Contingency |  | Dropdown (Custom Field) | Firm |  | `key_date.Firm_Contingency · TEXT` | Custom Field |
| `Firm_ContingencyTrigger` | Contingency Trigger |  | Dropdown (Custom Field) | Firm |  | `key_date.Firm_ContingencyTrigger · TEXT` | Custom Field |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActionPeriod` | Action Period | Enter the number of days, weeks, months, or years there are in the tickler period in this field. A Tickler is a friendly reminder that the key date is coming due. | Number | Global |  | `key_date.ActionPeriod · TEXT` |  |
| `FirstNoticePeriod` | Earliest Notice Period | Enter the number of days, weeks, months, or years in advance that you can take action on the key date. | Number | Global |  | `key_date.FirstNoticePeriod · TEXT` |  |
| `KeyDateID` | Key Date RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `key_date.KeyDateID · VARCHAR(64) NOT NULL` |  |
| `LengthOfTerm` | Length | This field is read-only and information-only. It displays the length of the term. | Number | Global |  | `key_date.LengthOfTerm · TEXT` |  |
| `NoticePeriod` | Last Notice Period | Enter the notice period value in this field. You will select the unit (days, weeks, months, or years) from the CodeNoticePeriodUnitID field. | Number | Global |  | `key_date.NoticePeriod · TEXT` |  |

### Dates & timestamps (9)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActionDate` | Action Date | Enter the date you took action on the key date in this field. | Date | Global |  | `key_date.ActionDate · TEXT` |  |
| `BeginDate` | Coverage Period Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global |  | `key_date.BeginDate · TEXT` |  |
| `EndDate` | Coverage Period End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `key_date.EndDate · TEXT` |  |
| `Firm_KeyDateEarliestTerminationDate` | Earliest Termination Date |  | Date | Firm |  | `key_date.Firm_KeyDateEarliestTerminationDate · TEXT` |  |
| `Firm_KeyDateLatestTerminationDate` | Latest Termination Date |  | Date | Firm |  | `key_date.Firm_KeyDateLatestTerminationDate · TEXT` |  |
| `FirstEventBeginDate` | First Event Begin Date | Enter the date the first event will take place. | Date | Global |  | `key_date.FirstEventBeginDate · TEXT` |  |
| `NoticeBeginDate` | Earliest Notice Date | Enter the notice begin date in this field. | Date | Global |  | `key_date.NoticeBeginDate · TEXT` |  |
| `NoticeEndDate` | Last Notice Date | The system will automatically calculate the value in the Notice End Date field using this formula: Notice End Date = Notice Begin Date - Notice Period. A Lease Notification Alert will be sent out on a nightly basis during the Notice Period until the key date is acted upon. | Date | Global |  | `key_date.NoticeEndDate · TEXT` |  |
| `TicklerDate` | Tickler Last Notice Date | A Tickler is a friendly reminder that the key date is coming due. The system will automatically calculate the value in the Tickler Date field using this formula: Tickler Date = Notice End Date - Tickler Period | Date | Global |  | `key_date.TicklerDate · TEXT` |  |

### Flags (3)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ActionComplete` | Is Action Complete? | Select the Action Complete check box if the action has been completed. The system will continue to send email alerts and system notifications about the End Date, Notice End Date, and Tickler Date until the Action Complete check box is selected. | Boolean | Global |  | `key_date.ActionComplete · TEXT` |  |
| `NoticeReceivedFlag` | Notice Received? | Select the Notice Received check box if the notice has been received for this action. | Boolean | Global |  | `key_date.NoticeReceivedFlag · TEXT` |  |
| `NoticeSentFlag` | Notice Sent? | Select the Notice Sent check box if notice has been sent for this action. | Boolean | Global |  | `key_date.NoticeSentFlag · TEXT` |  |

### Text & notes (6)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `key_date.Description · TEXT` |  |
| `Firm_KeyDateDocument` | Document |  | Text | Firm |  | `key_date.Firm_KeyDateDocument · TEXT` |  |
| `Firm_KeyDatePage` | Page |  | Text | Firm |  | `key_date.Firm_KeyDatePage · TEXT` |  |
| `Firm_KeyDateSection` | Section |  | Text | Firm |  | `key_date.Firm_KeyDateSection · TEXT` |  |
| `KeyDateEventTable` | Key Date Event Table | This field appears on the Covenants page when you have a frequency of Annually for your key date. It displays the upcoming key dates for the covenant. | Text | Global |  | `key_date.KeyDateEventTable · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `key_date.Notes · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Key Date ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `key_date.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `key_date.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `key_date.ModifiedDate · TEXT` |  |
