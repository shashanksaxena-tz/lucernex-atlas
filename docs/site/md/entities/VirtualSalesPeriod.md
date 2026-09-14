# VirtualSalesPeriod

*66 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `none exported`*

A computed (non-stored, 'Virtual') period record projecting percentage-rent breakpoints and sales-based rent obligations forward — up to eight numbered Breakpoint Amount/Rate slots per period. 66 Global fields under Contract; 'Virtual' entities in this catalog are calculated projections generated at read-time rather than persisted transactional rows, which is why none of them appear in Firm scope (a tenant cannot customize a calculation the platform generates).

Source: `data-fields/virtual-sales-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 66 |
| Fields with a vendor definition | 65 of 66 inventoried |
| Physical tables | — |
| Replication database | — |
| Catalogued fields | 66 (66 global, 0 firm) |
| Physical tables | 0 |
| Referenced by | 0 keys from 0 record types |
| Points at | 1 other records |
| Tenancy position | firm_global |
| Rules that name it | 1 |

## What to know before rebuilding this

### A computed projection, not a table

**Observed.** Virtual records are calculated at read time rather than stored. They have no primary key to join on and never appear in Firm scope — a tenant cannot customise a projection the platform generates. Treat this as the shape of a query result, not as a table to migrate.

### Firm-global reference data

**Derived.** Owned by the firm as a whole rather than by any one business record — configuration and reference data rather than transactional rows.

### 65 fields carry a vendor definition

**Observed.** 65 of this record's 66 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### 66 fields excluded from extraction

**Observed.** Observed of the loader. The inventory marks 66 of this record's fields as not extracted to PostgreSQL, so the replication target creates no column for them. They still exist in Lx; anything reading the replica rather than the product will not see them.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | not extracted | [Contract](Contract.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeSalesGroupID` | Sales Group | The sales group. The sales group is the first level of categorization for sales records. Groups are the parents of types, and grandparents of categories. | Dropdown (Sales Group) | Global |  | not extracted | Sales Group |

### Money (37)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BillingBucketCapAmount` | Rent Period Cap Amount | The cap amount for the rent period, depending upon the calculation model. | Currency | Global |  | not extracted |  |
| `BillingBucketFloorAmount` | Rent Period Floor Amount | The floor amount for the current rent period, prorated based on the frequency and the calculation model. | Currency | Global |  | not extracted |  |
| `ExcludedSalesPeriodAmount` | Excluded Sales Amount | The excluded amount for the sales period. | Currency | Global |  | not extracted |  |
| `GrossSalesPeriodAmount` | Gross Sales Amount | The gross sales amount for the percentage rent period. | Currency | Global |  | not extracted |  |
| `NetSalesPeriodAmount` | Net Sales Amount | The net sales amount for the percentage rent period. | Currency | Global |  | not extracted |  |
| `PRPBreakpointAmount1` | Breakpoint Amount #1 | This field gets breakpoint amount #1. | Currency | Global |  | not extracted |  |
| `PRPBreakpointAmount2` | Breakpoint Amount #2 | This field gets breakpoint amount #2. | Currency | Global |  | not extracted |  |
| `PRPBreakpointAmount3` | Breakpoint Amount #3 | This field gets breakpoint amount #3. | Currency | Global |  | not extracted |  |
| `PRPBreakpointAmount4` | Breakpoint Amount #4 | This field gets breakpoint amount #4. | Currency | Global |  | not extracted |  |
| `PRPBreakpointAmount5` | Breakpoint Amount #5 | This field gets breakpoint amount #5. | Currency | Global |  | not extracted |  |
| `PRPBreakpointAmount6` | Breakpoint Amount #6 | This field gets breakpoint amount #6. | Currency | Global |  | not extracted |  |
| `PRPBreakpointAmount7` | Breakpoint Amount #7 | This field gets breakpoint amount #7. | Currency | Global |  | not extracted |  |
| `PRPBreakpointAmount8` | Breakpoint Amount #8 | This field gets breakpoint amount #8. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRent` | Breakpoint Rent | The amount of rent for the period, computed from the breakpoints. This field does not take cap / floor amounts or prior payments into account. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRentDue1` | Rent Due #1 | Calculates the percentage rent due for sales exceeding breakpoint #1. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRentDue2` | Rent Due #2 | Calculates the percentage rent due for sales exceeding breakpoint #2. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRentDue3` | Rent Due #3 | Calculates the percentage rent due for sales exceeding breakpoint #3. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRentDue4` | Rent Due #4 | Calculates the percentage rent due for sales exceeding breakpoint #4. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRentDue5` | Rent Due #5 | Calculates the percentage rent due for sales exceeding breakpoint #5. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRentDue6` | Rent Due #6 | Calculates the percentage rent due for sales exceeding breakpoint #6. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRentDue7` | Rent Due #7 | Calculates the percentage rent due for sales exceeding breakpoint #7. | Currency | Global |  | not extracted |  |
| `PRPBreakpointRentDue8` | Rent Due #8 | Calculates the percentage rent due for sales exceeding breakpoint #8. | Currency | Global |  | not extracted |  |
| `PRPCapFloorAdjustedRent` | Cap / Floor Adjusted Rent | The breakpoint rent with the cap or floor amounts applied. This value is used in calculating the rent due for the current sales period as well as the total rent up to and including the current sales period. | Currency | Global |  | not extracted |  |
| `PRPRentDue` | Total Rent Due | Calculates the total percentage rent due. | Currency | Global |  | not extracted |  |
| `PRPSalesAmount` | Rent Period Sales Amount | The total sales for the percentage rent period. | Currency | Global |  | not extracted |  |
| `PRPSalesPastBreakpoint1` | Sales Past Breakpoint #1 | Calculates the amount of sales that exceed breakpoint #1. | Currency | Global |  | not extracted |  |
| `PRPSalesPastBreakpoint2` | Sales Past Breakpoint #2 | Calculates the amount of sales that exceed breakpoint #2. | Currency | Global |  | not extracted |  |
| `PRPSalesPastBreakpoint3` | Sales Past Breakpoint #3 | Calculates the amount of sales that exceed breakpoint #3. | Currency | Global |  | not extracted |  |
| `PRPSalesPastBreakpoint4` | Sales Past Breakpoint #4 | Calculates the amount of sales that exceed breakpoint #4. | Currency | Global |  | not extracted |  |
| `PRPSalesPastBreakpoint5` | Sales Past Breakpoint #5 | Calculates the amount of sales that exceed breakpoint #5. | Currency | Global |  | not extracted |  |
| `PRPSalesPastBreakpoint6` | Sales Past Breakpoint #6 | Calculates the amount of sales that exceed breakpoint #6. | Currency | Global |  | not extracted |  |
| `PRPSalesPastBreakpoint7` | Sales Past Breakpoint #7 | Calculates the amount of sales that exceed breakpoint #7. | Currency | Global |  | not extracted |  |
| `PRPSalesPastBreakpoint8` | Sales Past Breakpoint #8 | Calculates the amount of sales that exceed breakpoint #8. | Currency | Global |  | not extracted |  |
| `PRPTotalRent` | Total Rent | The total rent up to and including the current sales period. | Currency | Global |  | not extracted |  |
| `ReportingBucketGrossSalesAmount` | Reporting Period Gross Sales Amount | The gross sales amount for the percentage rent reporting period. | Currency | Global |  | not extracted |  |
| `ReportingBucketNetSalesAmount` | Reporting Period Net Sales Amount | The net sales amount for the percentage rent reporting period. | Currency | Global |  | not extracted |  |
| `SalesPeriodRentPaid` | Period Rent Paid | The total amount of percent rent paid for the given sales period. This value is used in calculating the total rent paid across a date range. | Currency | Global |  | not extracted |  |

### Rates & percentages (8)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PRPBreakpointRate1` | Breakpoint Rate #1 | This field gets breakpoint rate #1. | Percentage | Global |  | not extracted |  |
| `PRPBreakpointRate2` | Breakpoint Rate #2 | This field gets breakpoint rate #2. | Percentage | Global |  | not extracted |  |
| `PRPBreakpointRate3` | Breakpoint Rate #3 | This field gets breakpoint rate #3. | Percentage | Global |  | not extracted |  |
| `PRPBreakpointRate4` | Breakpoint Rate #4 | This field gets breakpoint rate #4. | Percentage | Global |  | not extracted |  |
| `PRPBreakpointRate5` | Breakpoint Rate #5 | This field gets breakpoint rate #5. | Percentage | Global |  | not extracted |  |
| `PRPBreakpointRate6` | Breakpoint Rate #6 | This field gets breakpoint rate #6. | Percentage | Global |  | not extracted |  |
| `PRPBreakpointRate7` | Breakpoint Rate #7 | This field gets breakpoint rate #7. | Percentage | Global |  | not extracted |  |
| `PRPBreakpointRate8` | Breakpoint Rate #8 | This field gets breakpoint rate #8. | Percentage | Global |  | not extracted |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ExcludedSalesPeriodCount` | Excluded Sales Count | The number of sales excluded for the sales period. | Number with no digits | Global |  | not extracted |  |
| `GrossSalesPeriodCount` | Gross Sales Count | The gross sales count for the percentage rent period. | Number with no digits | Global |  | not extracted |  |
| `NetSalesPeriodCount` | Net Sales Count | The net sales count for the percentage rent period. | Number with no digits | Global |  | not extracted |  |
| `PRPSalesCount` | Rent Period Sales Count | The total sales count for the percentage rent period. | Number with no digits | Global |  | not extracted |  |
| `SalesYear` | Calendar Year | The year of the sales period. | Number | Global |  | not extracted |  |

### Dates & timestamps (10)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BillingBucketBeginDate` | Rent Period Begin Date | The begin date of the rent period. It is used for multiple percent rent calculations. For per period and period gross up, this date is used as the offset begin date and it is also used in calculating the prorated rent amount and count. | Date | Global |  | not extracted |  |
| `BillingBucketDueDate` | Rent Period Payment Due Date | The date that rent payment is due. This date is used to determine which fiscal period to add the percent rent floor to for expense forecasts. | Date | Global |  | not extracted |  |
| `BillingBucketEndDate` | Rent Period End Date | The end date of the current rent period. | Date | Global |  | not extracted |  |
| `PeriodBeginDate` | Sales Period Begin Date | The period begin date. | Date | Global |  | not extracted |  |
| `PeriodEndDate` | Sales Period End Date | The period end date. | Date | Global |  | not extracted |  |
| `ReportingBucketBeginDate` | Reporting Period Begin Date | The begin date of the percentage rent reporting period. | Date | Global |  | not extracted |  |
| `ReportingBucketDueDate` | Reporting Period Due Date | The due date of the percentage rent reporting period. | Date | Global |  | not extracted |  |
| `ReportingBucketEndDate` | Reporting Period End Date | The end date of the percentage rent reporting period. | Date | Global |  | not extracted |  |
| `SalesMonthYearSort` | Calendar Month/Year Date | This field displays the calendar month and year as Calendar Month / Year. | Date | Global |  | not extracted |  |
| `SalesPeriodSort` | Fiscal Period Year |  | Date | Global |  | not extracted |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsActual` | Is Actual? | If true, the sales are actual sales. If false, the sales are forecast sales. | Boolean | Global |  | not extracted |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `SalesMonth` | Calendar Month | The month of the sales period. | Text | Global |  | not extracted |  |
| `SalesMonthYearText` | Calendar Month/Year | The month and year of the sales period. | Text | Global |  | not extracted |  |
| `SalesPeriodText` | Matching Fiscal Period/Year | The periods involved for the current sales month, separated by a comma if there is more than one. | Text | Global |  | not extracted |  |
