# ExpenseSchedule

*51 fields · module: Lease Accounting & Payments · Postgres: `expense_schedule`*

The recurring expense-billing schedule generated from an ExpenseSetup — per-period billed amounts, adjustment method and type (for escalating charges), and tax amount fields (Calculated Tax Amount #1-3+) for jurisdictions with multiple tax components. 51 Global fields under Contract and Summary Information.

Source: `data-fields/expense-schedule.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 51 |
| Catalogued fields | 51 (51 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 6 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 12 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

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

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetID` | Equipment | Equipment ID | Global |  | [Asset](Asset.md) |
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ContractTermID` | Contract Term | Contract Term ID | Global |  | [ContractTerm](ContractTerm.md) |
| `ExpenseSetupID` | Expense Setup | Expense Setup ID | Global | yes | [ExpenseSetup](ExpenseSetup.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Soft references (1)

Columns that name another record without a typed foreign key behind them - generic handles such as Entity ID and item ID that point at whichever table the row belongs to. These are the joins a rebuild has to make explicit.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AssetAssociatedProjectEntityID` | Equipment Associated Entity | Entity | Global |  |  |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeAdjustmentMethodID` | Adjustment Method Type | Dropdown (Adjustment Method Code) | Global |  | Adjustment Method Code |
| `CodeApprovalStatusID` | Approval Status | Dropdown (Approval Status Code) | Global |  | Approval Status Code |

### Money (18)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AnnualAmount` | Annual Amount | Currency | Global |  |  |
| `CalculatedTaxAmount1` | Calculated Tax Amount #1 | Currency | Global |  |  |
| `CalculatedTaxAmount2` | Calculated Tax Amount #2 | Currency | Global |  |  |
| `CalculatedTaxAmount3` | Calculated Tax Amount #3 | Currency | Global |  |  |
| `CalculatedTaxAmount4` | Calculated Tax Amount #4 | Currency | Global |  |  |
| `DailyRentRate` | Daily Rent Rate | Currency | Global |  |  |
| `FirstPaymentAmount` | First Payment Amount | Currency | Global |  |  |
| `LastPaymentAmount` | Last Payment Amount | Currency | Global |  |  |
| `NextAnnualAmount` | Next Annual Amount | Currency | Global |  |  |
| `NextPaymentAmount` | Next Payment Amount | Currency | Global |  |  |
| `PaymentAmount` | Payment Amount | Currency | Global |  |  |
| `PaymentRate` | Payment Rate | Currency | Global |  |  |
| `PreviousAnnualAmount` | Previous Annual Amount | Currency | Global |  |  |
| `PreviousPaymentAmount` | Previous Payment Amount | Currency | Global |  |  |
| `TaxAmount1` | Tax Amount #1 | Currency | Global |  |  |
| `TaxAmount2` | Tax Amount #2 | Currency | Global |  |  |
| `TaxAmount3` | Tax Amount #3 | Currency | Global |  |  |
| `TaxAmount4` | Tax Amount #4 | Currency | Global |  |  |

### Rates & percentages (4)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CalculatedTaxRate1` | Tax Rate #1 | Percentage | Global |  |  |
| `CalculatedTaxRate2` | Tax Rate #2 | Percentage | Global |  |  |
| `CalculatedTaxRate3` | Tax Rate #3 | Percentage | Global |  |  |
| `CalculatedTaxRate4` | Tax Rate #4 | Percentage | Global |  |  |

### Quantities (3)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AccountPeriod` | Account Period | Number | Global |  |  |
| `AccountYear` | Account Year | Number | Global |  |  |
| `ExpenseScheduleID` | Expense Schedule RecID | Number | Global |  |  |

### Dates & timestamps (4)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BeginDate` | Begin Date | Date | Global | yes |  |
| `EndDate` | End Date | Date | Global | yes |  |
| `LastApprovalChangeDate` | Last Approval Change Date | Date | Global |  |  |
| `ProcessedDate` | Processed Date | Date | Global |  |  |

### Flags (5)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `HoldFlag` | Hold? | Boolean | Global |  |  |
| `IsCPI` | Is CPI? | Boolean | Global |  |  |
| `OptionRentFlag` | Option Rent? | Boolean | Global |  |  |
| `ProcessedFlag` | Processed? | Boolean | Global |  |  |
| `ReadyForPaymentFlag` | Ready For Payment? | Boolean | Global |  |  |

### Text & notes (5)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `AdjustmentMethod` | Adjustment Method | Text | Global |  |  |
| `Description` |  | Text | Global |  |  |
| `NextExpenseScheduleID` | Next Schedule | Text | Global |  |  |
| `Notes` |  | Text | Global |  |  |
| `PreviousExpenseScheduleID` | Previous Schedule | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Expense Schedule ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |

### Other (1)

Everything that did not fall into a named group.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DateRange` | Date Range | Date Range | Global |  |  |
