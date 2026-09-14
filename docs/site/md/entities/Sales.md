# Sales

*28 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `sales`*

Reported retail sales figures for a location, feeding percentage-rent calculations — currency type, fiscal period/year, and a client-assigned sales ID for reconciling against a tenant's own sales report. 27 Global fields under Contract.

Source: `data-fields/sales.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Catalogued fields | 27 (27 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-051](../rules/CON-R-051.md) | Sales are reported: GrossSalesPeriodAmount sums Sales.GrossSalesAmount over the sales period; GrossSalesPeriodCount does the same for unit counts. | Observed |
| [CON-R-077](../rules/CON-R-077.md) | Usage-based rent is computed: structurally identical to the percentage-rent tiering with Sales→Usage and PRP→UBRP; the tier value is a unit cost, not a percentage rate. | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ContractID` | Contract | Contract ID | Global | yes | [Contract](Contract.md) |
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | Dropdown (Currency Type Code) | Global |  | Currency Type Code |
| `CodeSalesCategoryID` | Sales Category | Dropdown (Sales Category Code) | Global |  | Sales Category Code |
| `CodeSalesGroupID` | Sales Group | Dropdown (Sales Group) | Global |  | Sales Group |
| `CodeSalesTypeID` | Sales Type | Dropdown (Sales Type) | Global |  | Sales Type |
| `CodeUnitSalesTypeID` | Unit Sales Type | Dropdown (Unit Sales Type Code) | Global |  | Unit Sales Type Code |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `GrossSalesAmount` | Gross Sales Amount | Currency | Global |  |  |
| `NetSalesAmount` | Net Sales Amount | Currency | Global |  |  |
| `SalesAdjustment1` | Sales Adjustment #1 | Currency | Global |  |  |
| `SalesAdjustment2` | Sales Adjustment #2 | Currency | Global |  |  |
| `SalesAdjustment3` | Sales Adjustment #3 | Currency | Global |  |  |
| `SalesAdjustment4` | Sales Adjustment #4 | Currency | Global |  |  |
| `SalesAdjustment5` | Sales Adjustment #5 | Currency | Global |  |  |
| `SalesAdjustment6` | Sales Adjustment #6 | Currency | Global |  |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `MatchingCalendarYear` | Matching Calendar Year | Number | Global |  |  |
| `SalesID` | Sales RecID | Number | Global |  |  |
| `SalesPeriod` | Fiscal Period | Number | Global |  |  |
| `SalesYear` | Fiscal Year | Number | Global |  |  |
| `UnitSalesCount` | Unit Sales Count | Number | Global |  |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Date | Global |  |  |
| `PostingDate` | Posting Date | Date | Global |  |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ClientSalesID` | Client Sales ID | Text | Global |  |  |
| `MatchingCalendarMonthText` | Matching Calendar Month | Text | Global |  |  |
| `MatchingCalendarMonthYearText` | Matching Calendar Month / Year | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Sales ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
