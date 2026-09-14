# ExpenseSchedule

*51 fields · module: Lease Accounting & Payments · Postgres: `expense_schedule`*

The recurring expense-billing schedule generated from an ExpenseSetup — per-period billed amounts, adjustment method and type (for escalating charges), and tax amount fields (Calculated Tax Amount #1-3+) for jurisdictions with multiple tax components. 51 Global fields under Contract and Summary Information.

Source: `data-fields/expense-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 51 |
| Fields with a vendor definition | 50 of 51 inventoried |
| Physical tables | `expense_schedule` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 51 (51 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 12 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in expense_schedule

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 50 fields carry a vendor definition

**Observed.** 50 of this record's 51 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required-ness: the captures agree

**Observed.** Over the 50 fields both the Data Fields catalogue and the field inventory contain, the two agree on every one. 5 are marked required.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [ACC-R-021](../rules/ACC-R-021.md) | the accounting schedule associated with that expense type is dirtied | Observed |
| [ACC-R-025](../rules/ACC-R-025.md) | each period cash flow is routed to the schedule type its expense type designates for the standard being generated | Derived |
| [CON-R-008](../rules/CON-R-008.md) | Generation is requested: both ExpenseSetup.ReadyForPaymentFlag and ExpenseSchedule.ReadyForPaymentFlag must be true for the row to generate — the fields are observed, the exact gate semantics are inferred. | Observed |
| [CON-R-025](../rules/CON-R-025.md) | Computing rent rollups: 120 denormalised sTYPE_MONEY fields on Contract cross {Calendar,Fiscal}×{Base,Total}×{with,without tax}×{period buckets}. | Observed |
| [CON-R-030](../rules/CON-R-030.md) | Authoring a recurring expense through the wizard: the wizard's start date, end date, starting amount, amount type and escalation settings materialise ExpenseSetup + ExpenseEscalation + the full ExpenseSchedule in one action. | Observed |
| [CON-R-032](../rules/CON-R-032.md) | Determining billing frequency: CodeFrequencyID, NumberOfPayments and PaymentDueDay drive the number and spacing of ExpenseSchedule rows. | Derived |
| [CON-R-035](../rules/CON-R-035.md) | The clause is flagged IsDailyRent: the period amount is the daily rate multiplied by the day count in the period, rather than a fixed period amount. | Derived |
| [CON-R-036](../rules/CON-R-036.md) | A partial first or last period occurs: CodeProrationMethodID governs it, and the schedule's own FirstPaymentAmount / LastPaymentAmount carry the prorated stub amounts. | Observed |
| [CON-R-125](../rules/CON-R-125.md) | Any generation or posting: HoldFlag on ExpenseSetup, ExpenseSchedule, ExpenseAccrualSetup, PaymentTransaction or AccrualTransaction is a negative gate at every layer. | Observed |
| [CON-R-126](../rules/CON-R-126.md) | Any generation: ReadyForPaymentFlag on ExpenseSetup and ExpenseSchedule is a positive gate — both must be true. | Observed |
| [CON-R-145](../rules/CON-R-145.md) | A user invokes `Generate Rent` · `ExpenseSchedule` rows for the contract · Generation reads the Schedule layer, not the Setup layer · A contract with Expense Setups but an empty Expense Schedule generates nothing · Derived | Derived |
| [AST-R-005](../rules/AST-R-005.md) | Input: The two override fields. Effect: When populated, replace the accounting window that would otherwise be derived from the asset's `ExpenseSchedule` rows. | Derived |

## Fields

### Relationships (foreign keys) (5)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetID` | Equipment | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Equipment ID | Global |  | `expense_schedule.AssetID · TEXT` | [Asset](Asset.md) |
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `expense_schedule.ContractID · TEXT` | [Contract](Contract.md) |
| `ContractTermID` | Contract Term | The associated contract term record ID. | Contract Term ID | Global |  | `expense_schedule.ContractTermID · TEXT` | [ContractTerm](ContractTerm.md) |
| `ExpenseSetupID` | Expense Setup | The ExpenseSetupID field is used to associate an expense schedule with an expense setup record. | Expense Setup ID | Global | yes | `expense_schedule.ExpenseSetupID · TEXT` | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `expense_schedule.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | This is a reporting field that returns data about the asset associated with the entity. | Entity | Global |  | `expense_schedule.AssetAssociatedProjectEntityID · TEXT` |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeAdjustmentMethodID` | Adjustment Method Type | Adjustment method types are user-defined and information-only. Common adjustment method types include Consumer Price Indexes (CPIs), Fixed Amounts, and Percentages. This field is used for reporting. | Dropdown (Adjustment Method Code) | Global |  | `expense_schedule.CodeAdjustmentMethodID · TEXT` | Adjustment Method Code |
| `CodeApprovalStatusID` | Approval Status | This field signals the approval status of the expense schedule. Expense Schedules must be approved from the Contract > Details > Summary > Approve Payments modal window. | Dropdown (Approval Status Code) | Global |  | `expense_schedule.CodeApprovalStatusID · TEXT` | Approval Status Code |

### Money (18)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AnnualAmount` | Annual Amount | Enter the annual payment amount in the Annual Amount field. Do not enter 0 in this field. | Currency | Global |  | `expense_schedule.AnnualAmount · TEXT` |  |
| `CalculatedTaxAmount1` | Calculated Tax Amount #1 | The tax amount calculated by the system based upon the first tax rate you entered for the associated entity. | Currency | Global |  | `expense_schedule.CalculatedTaxAmount1 · TEXT` |  |
| `CalculatedTaxAmount2` | Calculated Tax Amount #2 | The tax amount calculated by the system based upon the second tax rate you entered for the associated entity. | Currency | Global |  | `expense_schedule.CalculatedTaxAmount2 · TEXT` |  |
| `CalculatedTaxAmount3` | Calculated Tax Amount #3 | The tax amount calculated by the system based upon the third tax rate you entered for the associated entity. | Currency | Global |  | `expense_schedule.CalculatedTaxAmount3 · TEXT` |  |
| `CalculatedTaxAmount4` | Calculated Tax Amount #4 | The tax amount calculated by the system based upon the fourth tax rate you entered for the associated entity. | Currency | Global |  | `expense_schedule.CalculatedTaxAmount4 · TEXT` |  |
| `DailyRentRate` | Daily Rent Rate | Enter the daily rent rate in this field. | Currency | Global |  | `expense_schedule.DailyRentRate · TEXT` |  |
| `FirstPaymentAmount` | First Payment Amount | If you need to override the value for the First Payment, enter the override value in this field. The system will calculate this value based upon the proration method you chose for your expense setup record. | Currency | Global |  | `expense_schedule.FirstPaymentAmount · TEXT` |  |
| `LastPaymentAmount` | Last Payment Amount | If you need to override the value for the Last Payment, enter the override value in this field. The system will calculate this value based upon the proration method you chose for your expense setup record. | Currency | Global |  | `expense_schedule.LastPaymentAmount · TEXT` |  |
| `NextAnnualAmount` | Next Annual Amount | The next expense schedule's annual amount. | Currency | Global |  | `expense_schedule.NextAnnualAmount · TEXT` |  |
| `NextPaymentAmount` | Next Payment Amount | The next expense schedule's period amount. | Currency | Global |  | `expense_schedule.NextPaymentAmount · TEXT` |  |
| `PaymentAmount` | Payment Amount | Enter the monthly payment amount in the Payment Amount field. Do not enter 0 in this field. | Currency | Global |  | `expense_schedule.PaymentAmount · TEXT` |  |
| `PaymentRate` | Payment Rate | Enter the rate in the Rate field, for example, $25 per square foot. Do not enter 0 in this field. | Currency | Global |  | `expense_schedule.PaymentRate · TEXT` |  |
| `PreviousAnnualAmount` | Previous Annual Amount | The previous expense schedule's annual amount. | Currency | Global |  | `expense_schedule.PreviousAnnualAmount · TEXT` |  |
| `PreviousPaymentAmount` | Previous Payment Amount | The previous expense schedule's period amount. | Currency | Global |  | `expense_schedule.PreviousPaymentAmount · TEXT` |  |
| `TaxAmount1` | Tax Amount #1 | To override the amount of taxes calculated by the system, enter the tax dollar amount in this field. Do not enter 0 in these fields. These fields are used in the scenario that a user needs to override a pre-calculated tax amount. The system automatically estimates the amount of taxes you will pay based upon the tax rate of your asset s associated entity. | Currency | Global |  | `expense_schedule.TaxAmount1 · TEXT` |  |
| `TaxAmount2` | Tax Amount #2 | To override the amount of taxes calculated by the system, enter the tax dollar amount in this field. Do not enter 0 in these fields. These fields are used in the scenario that a user needs to override a pre-calculated tax amount. The system automatically estimates the amount of taxes you will pay based upon the tax rate of your asset s associated entity. | Currency | Global |  | `expense_schedule.TaxAmount2 · TEXT` |  |
| `TaxAmount3` | Tax Amount #3 | To override the amount of taxes calculated by the system, enter the tax dollar amount in this field. Do not enter 0 in these fields. These fields are used in the scenario that a user needs to override a pre-calculated tax amount. The system automatically estimates the amount of taxes you will pay based upon the tax rate of your asset s associated entity. | Currency | Global |  | `expense_schedule.TaxAmount3 · TEXT` |  |
| `TaxAmount4` | Tax Amount #4 | To override the amount of taxes calculated by the system, enter the tax dollar amount in this field. Do not enter 0 in these fields. These fields are used in the scenario that a user needs to override a pre-calculated tax amount. The system automatically estimates the amount of taxes you will pay based upon the tax rate of your asset s associated entity. | Currency | Global |  | `expense_schedule.TaxAmount4 · TEXT` |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CalculatedTaxRate1` | Tax Rate #1 | The first tax rate you entered for the associated entity. | Percentage | Global |  | `expense_schedule.CalculatedTaxRate1 · TEXT` |  |
| `CalculatedTaxRate2` | Tax Rate #2 | The second tax rate you entered for the associated entity. | Percentage | Global |  | `expense_schedule.CalculatedTaxRate2 · TEXT` |  |
| `CalculatedTaxRate3` | Tax Rate #3 | The third tax rate you entered for the associated entity. | Percentage | Global |  | `expense_schedule.CalculatedTaxRate3 · TEXT` |  |
| `CalculatedTaxRate4` | Tax Rate #4 | The foruth tax rate you entered for the associated entity. | Percentage | Global |  | `expense_schedule.CalculatedTaxRate4 · TEXT` |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AccountPeriod` | Account Period | This field is no longer in use. | Number | Global |  | `expense_schedule.AccountPeriod · TEXT` |  |
| `AccountYear` | Account Year | This field is no longer in use. | Number | Global |  | `expense_schedule.AccountYear · TEXT` |  |
| `ExpenseScheduleID` | Expense Schedule RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `expense_schedule.ExpenseScheduleID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BeginDate` | Begin Date | The Begin Date field allows you to select a begin date for the record. | Date | Global | yes | `expense_schedule.BeginDate · TEXT` |  |
| `EndDate` | End Date | The End Date field allows you to select an end date for the record. | Date | Global | yes | `expense_schedule.EndDate · TEXT` |  |
| `LastApprovalChangeDate` | Last Approval Change Date | The date when the Approval Status field changed from Approved to Review. | Date | Global |  | `expense_schedule.LastApprovalChangeDate · TEXT` |  |
| `ProcessedDate` | Processed Date | This field is no longer in use. | Date | Global |  | `expense_schedule.ProcessedDate · TEXT` |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `HoldFlag` | Hold? | Select this check box if this recurring payment should be listed as on hold. The Hold Flag flows from the recurring payments to the transaction record to show that the payment is on hold. | Boolean | Global |  | `expense_schedule.HoldFlag · TEXT` |  |
| `IsCPI` | Is CPI? | This flag indicates that the schedule was created due to a CPI increase. | Boolean | Global |  | `expense_schedule.IsCPI · TEXT` |  |
| `OptionRentFlag` | Option Rent? | Select the Option Rent check box to identify the expense schedule record as part of an option, as opposed to an expense schedule included in the original term of the contract. | Boolean | Global |  | `expense_schedule.OptionRentFlag · TEXT` |  |
| `ProcessedFlag` | Processed? | This field is no longer in use. | Boolean | Global |  | `expense_schedule.ProcessedFlag · TEXT` |  |
| `ReadyForPaymentFlag` | Ready For Payment? | This flag indicates if the expense schedule is ready for payment. This flag is information-only, and is not used in any calculations. | Boolean | Global |  | `expense_schedule.ReadyForPaymentFlag · TEXT` |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `AdjustmentMethod` | Adjustment Method | The Adjustment Method field is information-only. This field allows you to enter why you made the adjustment. | Text | Global |  | `expense_schedule.AdjustmentMethod · TEXT` |  |
| `Description` |  | Write a description of the record. | Text | Global |  | `expense_schedule.Description · TEXT` |  |
| `NextExpenseScheduleID` | Next Schedule | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Text | Global |  | `expense_schedule.NextExpenseScheduleID · TEXT` |  |
| `Notes` |  | Add any notes about the record. | Text | Global |  | `expense_schedule.Notes · TEXT` |  |
| `PreviousExpenseScheduleID` | Previous Schedule | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Text | Global |  | `expense_schedule.PreviousExpenseScheduleID · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Schedule ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `expense_schedule.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `expense_schedule.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `expense_schedule.ModifiedDate · TEXT` |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DateRange` | Date Range | This field is no longer in use. | Date Range | Global |  | `expense_schedule.DateRange · TEXT` |  |
