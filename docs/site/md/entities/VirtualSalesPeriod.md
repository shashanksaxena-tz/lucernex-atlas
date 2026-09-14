# VirtualSalesPeriod

*66 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `none exported`*

A computed (non-stored, 'Virtual') period record projecting percentage-rent breakpoints and sales-based rent obligations forward — up to eight numbered Breakpoint Amount/Rate slots per period. 66 Global fields under Contract; 'Virtual' entities in this catalog are calculated projections generated at read-time rather than persisted transactional rows, which is why none of them appear in Firm scope (a tenant cannot customize a calculation the platform generates).

Source: `data-fields/virtual-sales-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 66 |
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

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global |  | [Contract](Contract.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |

### Money (37)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillingBucketCapAmount` | Rent Period Cap Amount | Currency | Global |  |  |
| `BillingBucketFloorAmount` | Rent Period Floor Amount | Currency | Global |  |  |
| `ExcludedSalesPeriodAmount` | Excluded Sales Amount | Currency | Global |  |  |
| `GrossSalesPeriodAmount` | Gross Sales Amount | Currency | Global |  |  |
| `NetSalesPeriodAmount` | Net Sales Amount | Currency | Global |  |  |
| `PRPBreakpointAmount1` | Breakpoint Amount #1 | Currency | Global |  |  |
| `PRPBreakpointAmount2` | Breakpoint Amount #2 | Currency | Global |  |  |
| `PRPBreakpointAmount3` | Breakpoint Amount #3 | Currency | Global |  |  |
| `PRPBreakpointAmount4` | Breakpoint Amount #4 | Currency | Global |  |  |
| `PRPBreakpointAmount5` | Breakpoint Amount #5 | Currency | Global |  |  |
| `PRPBreakpointAmount6` | Breakpoint Amount #6 | Currency | Global |  |  |
| `PRPBreakpointAmount7` | Breakpoint Amount #7 | Currency | Global |  |  |
| `PRPBreakpointAmount8` | Breakpoint Amount #8 | Currency | Global |  |  |
| `PRPBreakpointRent` | Breakpoint Rent | Currency | Global |  |  |
| `PRPBreakpointRentDue1` | Rent Due #1 | Currency | Global |  |  |
| `PRPBreakpointRentDue2` | Rent Due #2 | Currency | Global |  |  |
| `PRPBreakpointRentDue3` | Rent Due #3 | Currency | Global |  |  |
| `PRPBreakpointRentDue4` | Rent Due #4 | Currency | Global |  |  |
| `PRPBreakpointRentDue5` | Rent Due #5 | Currency | Global |  |  |
| `PRPBreakpointRentDue6` | Rent Due #6 | Currency | Global |  |  |
| `PRPBreakpointRentDue7` | Rent Due #7 | Currency | Global |  |  |
| `PRPBreakpointRentDue8` | Rent Due #8 | Currency | Global |  |  |
| `PRPCapFloorAdjustedRent` | Cap / Floor Adjusted Rent | Currency | Global |  |  |
| `PRPRentDue` | Total Rent Due | Currency | Global |  |  |
| `PRPSalesAmount` | Rent Period Sales Amount | Currency | Global |  |  |
| `PRPSalesPastBreakpoint1` | Sales Past Breakpoint #1 | Currency | Global |  |  |
| `PRPSalesPastBreakpoint2` | Sales Past Breakpoint #2 | Currency | Global |  |  |
| `PRPSalesPastBreakpoint3` | Sales Past Breakpoint #3 | Currency | Global |  |  |
| `PRPSalesPastBreakpoint4` | Sales Past Breakpoint #4 | Currency | Global |  |  |
| `PRPSalesPastBreakpoint5` | Sales Past Breakpoint #5 | Currency | Global |  |  |
| `PRPSalesPastBreakpoint6` | Sales Past Breakpoint #6 | Currency | Global |  |  |
| `PRPSalesPastBreakpoint7` | Sales Past Breakpoint #7 | Currency | Global |  |  |
| `PRPSalesPastBreakpoint8` | Sales Past Breakpoint #8 | Currency | Global |  |  |
| `PRPTotalRent` | Total Rent | Currency | Global |  |  |
| `ReportingBucketGrossSalesAmount` | Reporting Period Gross Sales Amount | Currency | Global |  |  |
| `ReportingBucketNetSalesAmount` | Reporting Period Net Sales Amount | Currency | Global |  |  |
| `SalesPeriodRentPaid` | Period Rent Paid | Currency | Global |  |  |

### Rates & percentages (8)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PRPBreakpointRate1` | Breakpoint Rate #1 | Percentage | Global |  |  |
| `PRPBreakpointRate2` | Breakpoint Rate #2 | Percentage | Global |  |  |
| `PRPBreakpointRate3` | Breakpoint Rate #3 | Percentage | Global |  |  |
| `PRPBreakpointRate4` | Breakpoint Rate #4 | Percentage | Global |  |  |
| `PRPBreakpointRate5` | Breakpoint Rate #5 | Percentage | Global |  |  |
| `PRPBreakpointRate6` | Breakpoint Rate #6 | Percentage | Global |  |  |
| `PRPBreakpointRate7` | Breakpoint Rate #7 | Percentage | Global |  |  |
| `PRPBreakpointRate8` | Breakpoint Rate #8 | Percentage | Global |  |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ExcludedSalesPeriodCount` | Excluded Sales Count | Number with no digits | Global |  |  |
| `GrossSalesPeriodCount` | Gross Sales Count | Number with no digits | Global |  |  |
| `NetSalesPeriodCount` | Net Sales Count | Number with no digits | Global |  |  |
| `PRPSalesCount` | Rent Period Sales Count | Number with no digits | Global |  |  |
| `SalesYear` | Calendar Year | Number | Global |  |  |

### Dates & timestamps (10)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillingBucketBeginDate` | Rent Period Begin Date | Date | Global |  |  |
| `BillingBucketDueDate` | Rent Period Payment Due Date | Date | Global |  |  |
| `BillingBucketEndDate` | Rent Period End Date | Date | Global |  |  |
| `PeriodBeginDate` | Sales Period Begin Date | Date | Global |  |  |
| `PeriodEndDate` | Sales Period End Date | Date | Global |  |  |
| `ReportingBucketBeginDate` | Reporting Period Begin Date | Date | Global |  |  |
| `ReportingBucketDueDate` | Reporting Period Due Date | Date | Global |  |  |
| `ReportingBucketEndDate` | Reporting Period End Date | Date | Global |  |  |
| `SalesMonthYearSort` | Calendar Month/Year Date | Date | Global |  |  |
| `SalesPeriodSort` | Fiscal Period Year | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsActual` | Is Actual? | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `SalesMonth` | Calendar Month | Text | Global |  |  |
| `SalesMonthYearText` | Calendar Month/Year | Text | Global |  |  |
| `SalesPeriodText` | Matching Fiscal Period/Year | Text | Global |  |  |
