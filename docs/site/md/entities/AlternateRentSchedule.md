# AlternateRentSchedule

*25 fields · module: Lease Accounting & Payments · Postgres: `alternate_rent_schedule`*

An alternate/contingency rent calculation method available on a contract — alt rent math formula selection and begin date. 24 Global fields under Contract.

Source: `data-fields/alternate-rent-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 25 |
| Fields with a vendor definition | 24 of 26 inventoried |
| Physical tables | `alternate_rent_schedule` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 24 (24 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 2 keys from 2 record types |
| Points at | 5 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 4 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in alternate_rent_schedule

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 24 fields carry a vendor definition

**Observed.** 24 of this record's 26 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 2 of this record's fields required; the Data Fields catalogue marks 3; 2 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-055](../rules/ACC-R-055.md) | a hold flag is set on all recurring-expense transactions (resp. percentage-rent transactions) generated during the window | Observed |
| [CON-R-061](../rules/CON-R-061.md) | Offsets are applied: VariableRentOffset and ScheduledOffset, applied via APPLY_OFFSETS, reduce the rent-year obligation. | Observed |
| [CON-R-062](../rules/CON-R-062.md) | Rent already paid is credited: PRPRentDue = PRPTotalRent − SalesPeriodRentPaid − offsets. | Inferred |
| [CON-R-070](../rules/CON-R-070.md) | An AlternateRentSchedule window is active: a substitute rent formula (CodeAltRentMathID, PercentRentRate) replaces the normal one for the window. | Observed |

## Fields

### Relationships (foreign keys) (3)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `alternate_rent_schedule.ContractID · TEXT` | [Contract](Contract.md) |
| `ExpenseSetupID` | Expense Setup | The ExpenseSetupID field is used to associate an alternate rent record with an expense setup record. | Expense Setup ID | Global |  | `alternate_rent_schedule.ExpenseSetupID · TEXT` | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `alternate_rent_schedule.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAltRentMathID` | Alt Rent Math | This field is for record keeping purposes only. It has no functional impact on the generated payment. Select how your alternate rent should be calculated from this field. Once you generate alternate rent, you will need to approve or reject the appropriate payments from the Approve Payments modal window. | Dropdown (Alt Rent Math Code) | Global |  | `alternate_rent_schedule.CodeAltRentMathID · TEXT` | Alt Rent Math Code |
| `CodeSalesGroupID` | Sales Group | In alternate rent scenarios, different sales figures can apply. Select the appropriate sales group from the Sales Group field. Any percentage rent schedules with this sales group will be affected if they fall within the time range of the alternate rent schedule. | Dropdown (Sales Group) | Global |  | `alternate_rent_schedule.CodeSalesGroupID · TEXT` | Sales Group |

### Money (3)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CapAmount` | Monthly Max Cap(Ceiling) | Enter the maximum, or ceiling cap for alternate rent in this field. | Currency | Global |  | `alternate_rent_schedule.CapAmount · TEXT` |  |
| `ExpenseReductionAmount` | Expense Reduction Amount | This field reduces the amount of a generated transaction by a fixed amount. Enter the fixed amount in this field. This field does not appear until the Reduce by Fixed Amount option button is selected. | Currency | Global |  | `alternate_rent_schedule.ExpenseReductionAmount · TEXT` |  |
| `FloorAmount` | Monthly Min Cap(Floor) | Enter the minimum, or floor cap for alternate rent in this field. | Currency | Global |  | `alternate_rent_schedule.FloorAmount · TEXT` |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExpenseReductionPercent` | Expense Reduction Percent | This field reduces the amount of a generated transaction by a percentage amount. Enter the percentage amount in this field. This field does not appear until the Reduce by % Amount option button is selected. | Percentage | Global |  | `alternate_rent_schedule.ExpenseReductionPercent · TEXT` |  |
| `PercentRentRate` | Percent Rent Rate | Enter the percent rent rate you would like to pay while your contract is in alternate rent and you are paying a percentage of gross sales in this field. | Percentage | Global |  | `alternate_rent_schedule.PercentRentRate · TEXT` |  |

### Quantities (1)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AlternateRentScheduleID` | Alternate Rent Schedule RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `alternate_rent_schedule.AlternateRentScheduleID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global | yes | `alternate_rent_schedule.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global |  | `alternate_rent_schedule.EndDate · TEXT` |  |

### Flags (4)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PRDeductExclusions` | Deduct Exclusions? | Select this check box if you would like to continue to deduct exclusions from your percentage rent. | Boolean | Global |  | `alternate_rent_schedule.PRDeductExclusions · TEXT` |  |
| `SetExpHoldFlag` | Set payments for Recurring Expenses on Hold | This check box sets a Hold flag on all recurring expense transactions generated while the contract is in alternate rent. | Boolean | Global |  | `alternate_rent_schedule.SetExpHoldFlag · TEXT` |  |
| `SetPRHoldFlag` | Set payments for Percent Rent on Hold | This check box sets a Hold flag on all percentage rent transactions generated while the contract is in alternate rent. | Boolean | Global |  | `alternate_rent_schedule.SetPRHoldFlag · TEXT` |  |
| `SuspendSL` | Suspend SL? | This field is no longer used. | Boolean | Global |  | `alternate_rent_schedule.SuspendSL · TEXT` |  |

### Text & notes (2)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `Description` |  | Write a description of the record. | Text | Global |  | `alternate_rent_schedule.Description · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `alternate_rent_schedule.Notes · TEXT` |  |

### Audit & record keeping (6)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Alternate Rent Schedule ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `alternate_rent_schedule.BOMapClientRecordID · TEXT` |  |
| `CreatedByID` | Created By | The Created By field is a system-populated field which captures the name of the member making changes to a record. | Member ID | Global |  | `alternate_rent_schedule.CreatedByID · TEXT` | [Member](Member.md) |
| `CreatedDate` | Created Date | The Created Date field is a system-populated field which captures the date that a record was created. | Time | Global |  | `alternate_rent_schedule.CreatedDate · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `alternate_rent_schedule.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `alternate_rent_schedule.ModifiedDate · TEXT` |  |
| `RevNumber` | Rev Number | The Rev Number field indicates how many times a record has been modified. This value of the field increases by 1 each time the record is modified. | Number | Global |  | `alternate_rent_schedule.RevNumber · TEXT` |  |

## What points here (2 keys)

| Record type | Via column |
|---|---|
| [PaymentTransaction](PaymentTransaction.md) | `AlternateRentScheduleID` |
| [PaymentTransactionFullImport](PaymentTransactionFullImport.md) | `AlternateRentScheduleID` |
