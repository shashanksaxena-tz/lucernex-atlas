# VirtualUsagePeriod

*66 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_usage_period`*

The usage-based-rent counterpart to VirtualSalesPeriod — projects breakpoint cost tiers (with 6-decimal-precision NUMBER_FRACTION6DIGITS fields for unit-cost rates) period by period for contracts billed on usage/consumption rather than sales volume. 66 Global fields under Contract.

Source: `data-fields/virtual-usage-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 66 |
| Catalogued fields | 66 (66 global, 0 firm) |
| Physical tables | 1 |
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

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeUsageGroupID` | Usage Group | Dropdown (Usage Group Code) | Global |  | Usage Group Code |
| `CodeUsageUnitTypeID` | Usage Unit Type | Dropdown (Usage Unit Type Code) | Global |  | Usage Unit Type Code |

### Money (27)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillingBucketCapAmount` | Rent Period Cap Amount | Currency | Global |  |  |
| `GrossUsagePeriodAmount` | Usage Amount | Currency | Global |  |  |
| `NetUsagePeriodAmount` | Net Usage Amount | Currency | Global |  |  |
| `ReportingBucketGrossUsageAmount` | Reporting Period Usage Amount | Currency | Global |  |  |
| `ReportingBucketNetUsageAmount` | Reporting Period Net Usage Amount | Currency | Global |  |  |
| `UBRPBreakpointCost1` | Breakpoint Cost #1 | Currency | Global |  |  |
| `UBRPBreakpointCost2` | Breakpoint Cost #2 | Currency | Global |  |  |
| `UBRPBreakpointCost3` | Breakpoint Cost #3 | Currency | Global |  |  |
| `UBRPBreakpointCost4` | Breakpoint Cost #4 | Currency | Global |  |  |
| `UBRPBreakpointCost5` | Breakpoint Cost #5 | Currency | Global |  |  |
| `UBRPBreakpointCost6` | Breakpoint Cost #6 | Currency | Global |  |  |
| `UBRPBreakpointCost7` | Breakpoint Cost #7 | Currency | Global |  |  |
| `UBRPBreakpointCost8` | Breakpoint Cost #8 | Currency | Global |  |  |
| `UBRPBreakpointRent` | Breakpoint Rent | Currency | Global |  |  |
| `UBRPBreakpointRentDue1` | Rent Due #1 | Currency | Global |  |  |
| `UBRPBreakpointRentDue2` | Rent Due #2 | Currency | Global |  |  |
| `UBRPBreakpointRentDue3` | Rent Due #3 | Currency | Global |  |  |
| `UBRPBreakpointRentDue4` | Rent Due #4 | Currency | Global |  |  |
| `UBRPBreakpointRentDue5` | Rent Due #5 | Currency | Global |  |  |
| `UBRPBreakpointRentDue6` | Rent Due #6 | Currency | Global |  |  |
| `UBRPBreakpointRentDue7` | Rent Due #7 | Currency | Global |  |  |
| `UBRPBreakpointRentDue8` | Rent Due #8 | Currency | Global |  |  |
| `UBRPCapFloorAdjustedRent` | Cap / Floor Adjusted Rent | Currency | Global |  |  |
| `UBRPRentDue` | Total Rent Due | Currency | Global |  |  |
| `UBRPTotalRent` | Total Rent | Currency | Global |  |  |
| `UBRPUsageAmount` | Rent Period Usage Amount | Currency | Global |  |  |
| `UsagePeriodRentPaid` | Period Rent Paid | Currency | Global |  |  |

### Quantities (23)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossUsagePeriodCount` | Usage Count | 5-Digit Number | Global |  |  |
| `GrossUsagePeriodShare` | Usage Share | 5-Digit Number | Global |  |  |
| `NetUsagePeriodCount` | Net Usage Count | 5-Digit Number | Global |  |  |
| `NetUsagePeriodShare` | Net Usage Share | 5-Digit Number | Global |  |  |
| `UBRPBreakpointAmount1` | Breakpoint Amount #1 | 5-Digit Number | Global |  |  |
| `UBRPBreakpointAmount2` | Breakpoint Amount #2 | 5-Digit Number | Global |  |  |
| `UBRPBreakpointAmount3` | Breakpoint Amount #3 | 5-Digit Number | Global |  |  |
| `UBRPBreakpointAmount4` | Breakpoint Amount #4 | 5-Digit Number | Global |  |  |
| `UBRPBreakpointAmount5` | Breakpoint Amount #5 | 5-Digit Number | Global |  |  |
| `UBRPBreakpointAmount6` | Breakpoint Amount #6 | 5-Digit Number | Global |  |  |
| `UBRPBreakpointAmount7` | Breakpoint Amount #7 | 5-Digit Number | Global |  |  |
| `UBRPBreakpointAmount8` | Breakpoint Amount #8 | 5-Digit Number | Global |  |  |
| `UBRPUsageCount` | Rent Period Usage Count | Number with no digits | Global |  |  |
| `UBRPUsagePastBreakpoint1` | Usage Past Breakpoint #1 | 5-Digit Number | Global |  |  |
| `UBRPUsagePastBreakpoint2` | Usage Past Breakpoint #2 | 5-Digit Number | Global |  |  |
| `UBRPUsagePastBreakpoint3` | Usage Past Breakpoint #3 | 5-Digit Number | Global |  |  |
| `UBRPUsagePastBreakpoint4` | Usage Past Breakpoint #4 | 5-Digit Number | Global |  |  |
| `UBRPUsagePastBreakpoint5` | Usage Past Breakpoint #5 | 5-Digit Number | Global |  |  |
| `UBRPUsagePastBreakpoint6` | Usage Past Breakpoint #6 | 5-Digit Number | Global |  |  |
| `UBRPUsagePastBreakpoint7` | Usage Past Breakpoint #7 | 5-Digit Number | Global |  |  |
| `UBRPUsagePastBreakpoint8` | Usage Past Breakpoint #8 | 5-Digit Number | Global |  |  |
| `UBRPUsageShare` | Rent Period Usage Share | Number with no digits | Global |  |  |
| `UsageYear` | Calendar Year | Number | Global |  |  |

### Dates & timestamps (9)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BillingBucketBeginDate` | Rent Period Begin Date | Date | Global |  |  |
| `BillingBucketDueDate` | Rent Period Payment Due Date | Date | Global |  |  |
| `BillingBucketEndDate` | Rent Period End Date | Date | Global |  |  |
| `PeriodBeginDate` | Usage Period Begin Date | Date | Global |  |  |
| `PeriodEndDate` | Usage Period End Date | Date | Global |  |  |
| `ReportingBucketBeginDate` | Reporting Period Begin Date | Date | Global |  |  |
| `ReportingBucketDueDate` | Reporting Period Due Date | Date | Global |  |  |
| `ReportingBucketEndDate` | Reporting Period End Date | Date | Global |  |  |
| `UsageMonthYearSort` | Calendar Month/Year Date | Date | Global |  |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IsActual` | Is Actual? | Boolean | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `UsageMonth` | Calendar Month | Text | Global |  |  |
| `UsageMonthYearText` | Calendar Month/Year | Text | Global |  |  |
| `UsagePeriodText` | Matching Fiscal Period/Year | Text | Global |  |  |
