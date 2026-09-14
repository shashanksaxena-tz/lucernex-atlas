# VirtualUsagePeriod

*66 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `virtual_usage_period`*

The usage-based-rent counterpart to VirtualSalesPeriod — projects breakpoint cost tiers (with 6-decimal-precision NUMBER_FRACTION6DIGITS fields for unit-cost rates) period by period for contracts billed on usage/consumption rather than sales volume. 66 Global fields under Contract.

Source: `data-fields/virtual-usage-period.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 66 |
| Fields with a vendor definition | 65 of 66 inventoried |
| Physical tables | `virtual_usage_period` |
| Replication database | `lxr_drp_bbw` |
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

### Lands in virtual_usage_period

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 65 fields carry a vendor definition

**Observed.** 65 of this record's 66 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [RPT-R-036](../rules/RPT-R-036.md) | `Virtual*` objects are computed projections exposed as tables — `VirtualSalesPeriod` (66), `VirtualUsagePeriod` (66), `VirtualPercentageRentPeriod` (38), `VirtualUseBasedRentPeriod` (23), `VirtualPRAccrualPeriod` (20), `VirtualExpenseForeca | Derived |

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global |  | `virtual_usage_period.ContractID · TEXT` | [Contract](Contract.md) |

### Coded values (drop-downs) (2)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeUsageGroupID` | Usage Group | The usage group for the period. A Usage Group will be used with one and only one Model Type. The model type of a usage group will impact how your use based rent is calculated. | Dropdown (Usage Group Code) | Global |  | `virtual_usage_period.CodeUsageGroupID · TEXT` | Usage Group Code |
| `CodeUsageUnitTypeID` | Usage Unit Type | This field can be used to create custom unit types for count-based usage groups. | Dropdown (Usage Unit Type Code) | Global |  | `virtual_usage_period.CodeUsageUnitTypeID · TEXT` | Usage Unit Type Code |

### Money (27)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BillingBucketCapAmount` | Rent Period Cap Amount | This field is a placeholder in preparation for an upcoming enhancement. | Currency | Global |  | `virtual_usage_period.BillingBucketCapAmount · TEXT` |  |
| `GrossUsagePeriodAmount` | Usage Amount | Calculates the gross usage amount during the period. | Currency | Global |  | `virtual_usage_period.GrossUsagePeriodAmount · TEXT` |  |
| `NetUsagePeriodAmount` | Net Usage Amount | Calculates the net usage amount during the period. | Currency | Global |  | `virtual_usage_period.NetUsagePeriodAmount · TEXT` |  |
| `ReportingBucketGrossUsageAmount` | Reporting Period Usage Amount | Calculates the gross usage amount during the reporting period. | Currency | Global |  | `virtual_usage_period.ReportingBucketGrossUsageAmount · TEXT` |  |
| `ReportingBucketNetUsageAmount` | Reporting Period Net Usage Amount | Calculates the net usage amount during the reporting period. | Currency | Global |  | `virtual_usage_period.ReportingBucketNetUsageAmount · TEXT` |  |
| `UBRPBreakpointCost1` | Breakpoint Cost #1 | The cost for breakpoint #1. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointCost1 · TEXT` |  |
| `UBRPBreakpointCost2` | Breakpoint Cost #2 | The cost for breakpoint #2. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointCost2 · TEXT` |  |
| `UBRPBreakpointCost3` | Breakpoint Cost #3 | The cost for breakpoint #3. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointCost3 · TEXT` |  |
| `UBRPBreakpointCost4` | Breakpoint Cost #4 | The cost for breakpoint #4. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointCost4 · TEXT` |  |
| `UBRPBreakpointCost5` | Breakpoint Cost #5 | The cost for breakpoint #5. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointCost5 · TEXT` |  |
| `UBRPBreakpointCost6` | Breakpoint Cost #6 | The cost for breakpoint #6. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointCost6 · TEXT` |  |
| `UBRPBreakpointCost7` | Breakpoint Cost #7 | The cost for breakpoint #7. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointCost7 · TEXT` |  |
| `UBRPBreakpointCost8` | Breakpoint Cost #8 | The cost for breakpoint #8. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointCost8 · TEXT` |  |
| `UBRPBreakpointRent` | Breakpoint Rent | The amount of use based rent for the period, computed using the breakpoints. This value doesn't take cap/floor amounts or prior payments into account. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRent · TEXT` |  |
| `UBRPBreakpointRentDue1` | Rent Due #1 | Calculates the rent due for usage past breakpoint #1. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRentDue1 · TEXT` |  |
| `UBRPBreakpointRentDue2` | Rent Due #2 | Calculates the rent due for usage past breakpoint #2. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRentDue2 · TEXT` |  |
| `UBRPBreakpointRentDue3` | Rent Due #3 | Calculates the rent due for usage past breakpoint #3. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRentDue3 · TEXT` |  |
| `UBRPBreakpointRentDue4` | Rent Due #4 | Calculates the rent due for usage past breakpoint #4. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRentDue4 · TEXT` |  |
| `UBRPBreakpointRentDue5` | Rent Due #5 | Calculates the rent due for usage past breakpoint #5. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRentDue5 · TEXT` |  |
| `UBRPBreakpointRentDue6` | Rent Due #6 | Calculates the rent due for usage past breakpoint #6. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRentDue6 · TEXT` |  |
| `UBRPBreakpointRentDue7` | Rent Due #7 | Calculates the rent due for usage past breakpoint #7. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRentDue7 · TEXT` |  |
| `UBRPBreakpointRentDue8` | Rent Due #8 | Calculates the rent due for usage past breakpoint #8. | Currency | Global |  | `virtual_usage_period.UBRPBreakpointRentDue8 · TEXT` |  |
| `UBRPCapFloorAdjustedRent` | Cap / Floor Adjusted Rent | The breakpoint rent with the cap/floor amounts applied. This value is used in calculating the use based rent due for the current sales period and the total used based rent up to and including the current sales period. | Currency | Global |  | `virtual_usage_period.UBRPCapFloorAdjustedRent · TEXT` |  |
| `UBRPRentDue` | Total Rent Due | Calculates the total use based rent due. | Currency | Global |  | `virtual_usage_period.UBRPRentDue · TEXT` |  |
| `UBRPTotalRent` | Total Rent | Calculates the total use based rent. | Currency | Global |  | `virtual_usage_period.UBRPTotalRent · TEXT` |  |
| `UBRPUsageAmount` | Rent Period Usage Amount | This field is a placeholder in preparation for an upcoming enhancement. | Currency | Global |  | `virtual_usage_period.UBRPUsageAmount · TEXT` |  |
| `UsagePeriodRentPaid` | Period Rent Paid | Calculates any rent paid for the period. | Currency | Global |  | `virtual_usage_period.UsagePeriodRentPaid · TEXT` |  |

### Quantities (23)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossUsagePeriodCount` | Usage Count | Calculates the gross usage count during the period. | 5-Digit Number | Global |  | `virtual_usage_period.GrossUsagePeriodCount · TEXT` |  |
| `GrossUsagePeriodShare` | Usage Share | Calculates the gross usage percentage during the period. | 5-Digit Number | Global |  | `virtual_usage_period.GrossUsagePeriodShare · TEXT` |  |
| `NetUsagePeriodCount` | Net Usage Count | Calculates the net usage count during the period. | 5-Digit Number | Global |  | `virtual_usage_period.NetUsagePeriodCount · TEXT` |  |
| `NetUsagePeriodShare` | Net Usage Share | Calculates the net usage percentage during the period. | 5-Digit Number | Global |  | `virtual_usage_period.NetUsagePeriodShare · TEXT` |  |
| `UBRPBreakpointAmount1` | Breakpoint Amount #1 | This field contains breakpoint amount #1. This amount can either be count-based or share-based. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPBreakpointAmount1 · TEXT` |  |
| `UBRPBreakpointAmount2` | Breakpoint Amount #2 | This field contains breakpoint amount #2. This amount can either be count-based or share-based. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPBreakpointAmount2 · TEXT` |  |
| `UBRPBreakpointAmount3` | Breakpoint Amount #3 | This field contains breakpoint amount #3. This amount can either be count-based or share-based. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPBreakpointAmount3 · TEXT` |  |
| `UBRPBreakpointAmount4` | Breakpoint Amount #4 | This field contains breakpoint amount #4. This amount can either be count-based or share-based. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPBreakpointAmount4 · TEXT` |  |
| `UBRPBreakpointAmount5` | Breakpoint Amount #5 | This field contains breakpoint amount #5. This amount can either be count-based or share-based. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPBreakpointAmount5 · TEXT` |  |
| `UBRPBreakpointAmount6` | Breakpoint Amount #6 | This field contains breakpoint amount #6. This amount can either be count-based or share-based. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPBreakpointAmount6 · TEXT` |  |
| `UBRPBreakpointAmount7` | Breakpoint Amount #7 | This field contains breakpoint amount #7. This amount can either be count-based or share-based. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPBreakpointAmount7 · TEXT` |  |
| `UBRPBreakpointAmount8` | Breakpoint Amount #8 | This field contains breakpoint amount #8. This amount can either be count-based or share-based. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPBreakpointAmount8 · TEXT` |  |
| `UBRPUsageCount` | Rent Period Usage Count | The usage count. | Number with no digits | Global |  | `virtual_usage_period.UBRPUsageCount · TEXT` |  |
| `UBRPUsagePastBreakpoint1` | Usage Past Breakpoint #1 | Calculates the usage past breakpoint #1. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPUsagePastBreakpoint1 · TEXT` |  |
| `UBRPUsagePastBreakpoint2` | Usage Past Breakpoint #2 | Calculates the usage past breakpoint #2. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPUsagePastBreakpoint2 · TEXT` |  |
| `UBRPUsagePastBreakpoint3` | Usage Past Breakpoint #3 | Calculates the usage past breakpoint #3. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPUsagePastBreakpoint3 · TEXT` |  |
| `UBRPUsagePastBreakpoint4` | Usage Past Breakpoint #4 | Calculates the usage past breakpoint #4. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPUsagePastBreakpoint4 · TEXT` |  |
| `UBRPUsagePastBreakpoint5` | Usage Past Breakpoint #5 | Calculates the usage past breakpoint #5. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPUsagePastBreakpoint5 · TEXT` |  |
| `UBRPUsagePastBreakpoint6` | Usage Past Breakpoint #6 | Calculates the usage past breakpoint #6. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPUsagePastBreakpoint6 · TEXT` |  |
| `UBRPUsagePastBreakpoint7` | Usage Past Breakpoint #7 | Calculates the usage past breakpoint #7. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPUsagePastBreakpoint7 · TEXT` |  |
| `UBRPUsagePastBreakpoint8` | Usage Past Breakpoint #8 | Calculates the usage past breakpoint #8. | 5-Digit Number | Global |  | `virtual_usage_period.UBRPUsagePastBreakpoint8 · TEXT` |  |
| `UBRPUsageShare` | Rent Period Usage Share | The usage share. | Number with no digits | Global |  | `virtual_usage_period.UBRPUsageShare · TEXT` |  |
| `UsageYear` | Calendar Year | The usage year. | Number | Global |  | `virtual_usage_period.UsageYear · TEXT` |  |

### Dates & timestamps (9)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BillingBucketBeginDate` | Rent Period Begin Date | Calculates the billing period begin date. | Date | Global |  | `virtual_usage_period.BillingBucketBeginDate · TEXT` |  |
| `BillingBucketDueDate` | Rent Period Payment Due Date | Calculates the billing period due date. | Date | Global |  | `virtual_usage_period.BillingBucketDueDate · TEXT` |  |
| `BillingBucketEndDate` | Rent Period End Date | Calculates the billing period end date. | Date | Global |  | `virtual_usage_period.BillingBucketEndDate · TEXT` |  |
| `PeriodBeginDate` | Usage Period Begin Date | The begin date of the usage period. | Date | Global |  | `virtual_usage_period.PeriodBeginDate · TEXT` |  |
| `PeriodEndDate` | Usage Period End Date | The end date of the usage period. | Date | Global |  | `virtual_usage_period.PeriodEndDate · TEXT` |  |
| `ReportingBucketBeginDate` | Reporting Period Begin Date | Calculates the reporting period begin date. | Date | Global |  | `virtual_usage_period.ReportingBucketBeginDate · TEXT` |  |
| `ReportingBucketDueDate` | Reporting Period Due Date | Calculates the reporting period due date. | Date | Global |  | `virtual_usage_period.ReportingBucketDueDate · TEXT` |  |
| `ReportingBucketEndDate` | Reporting Period End Date | Calculates the reporting period end date. | Date | Global |  | `virtual_usage_period.ReportingBucketEndDate · TEXT` |  |
| `UsageMonthYearSort` | Calendar Month/Year Date |  | Date | Global |  | `virtual_usage_period.UsageMonthYearSort · TEXT` |  |

### Flags (1)

Booleans. In this product they usually gate engine behaviour rather than describe the record.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IsActual` | Is Actual? | Indicates if the current usage period is actual or forecasted. | Boolean | Global |  | `virtual_usage_period.IsActual · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `UsageMonth` | Calendar Month | The usage month. | Text | Global |  | `virtual_usage_period.UsageMonth · TEXT` |  |
| `UsageMonthYearText` | Calendar Month/Year | This field displays the calendar month and year as Calendar Month / Year. | Text | Global |  | `virtual_usage_period.UsageMonthYearText · TEXT` |  |
| `UsagePeriodText` | Matching Fiscal Period/Year | The periods involved for the current sales month, separated by a comma if there is more than one. | Text | Global |  | `virtual_usage_period.UsagePeriodText · TEXT` |  |
