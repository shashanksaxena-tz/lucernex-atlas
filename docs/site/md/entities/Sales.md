# Sales

*28 fields · module: Variable Rent (Percentage / Use-Based) & Sales · Postgres: `sales`*

Reported retail sales figures for a location, feeding percentage-rent calculations — currency type, fiscal period/year, and a client-assigned sales ID for reconciling against a tenant's own sales report. 27 Global fields under Contract.

Source: `data-fields/sales.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 28 |
| Fields with a vendor definition | 27 of 28 inventoried |
| Physical tables | `sales` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 27 (27 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 3 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 2 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in sales

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 27 fields carry a vendor definition

**Observed.** 27 of this record's 28 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one source in the corpus that explains fields rather than listing them.

### 1 field marked required

**Observed.** The inventory marks 1 of this record's fields Required. Across the whole inventory that is 606 fields, which independently corroborates the 603 the corpus had derived from the Data Fields catalogue — two sources, arrived at separately, agreeing to within three.

## Rules that govern it

| Rule | What it requires | Confidence |
|---|---|---|
| [CON-R-051](../rules/CON-R-051.md) | Sales are reported: GrossSalesPeriodAmount sums Sales.GrossSalesAmount over the sales period; GrossSalesPeriodCount does the same for unit counts. | Observed |
| [CON-R-077](../rules/CON-R-077.md) | Usage-based rent is computed: structurally identical to the percentage-rent tiering with Sales→Usage and PRP→UBRP; the tier value is a unit cost, not a percentage rate. | Derived |

## Fields

### Relationships (foreign keys) (2)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ContractID` | Contract | The Contract ID is a unique identifier that belongs to a contract. The Contract ID of a contract can only be changed from the Contract > Details > Summary page. | Contract ID | Global | yes | `sales.ContractID · TEXT` | [Contract](Contract.md) |
| `ProjectEntityID` |  |  | Entity ID | — |  | `sales.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (5)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeCurrencyTypeID` | Currency Type | The Currency Type field allows you to select a currency type to be used on a record. | Dropdown (Currency Type Code) | Global |  | `sales.CodeCurrencyTypeID · TEXT` | Currency Type Code |
| `CodeSalesCategoryID` | Sales Category | The sales category is the third level of categorization for sales records. Categories are the children of types, and grandchildren of groups. The default sales categories are Actual and Forecast. The system will not generate transactions for sales with a sales category of Forecast. | Dropdown (Sales Category Code) | Global |  | `sales.CodeSalesCategoryID · TEXT` | Sales Category Code |
| `CodeSalesGroupID` | Sales Group | The sales group is the first level of categorization for sales records. Groups are the parents of types, and grandparents of categories. | Dropdown (Sales Group) | Global |  | `sales.CodeSalesGroupID · TEXT` | Sales Group |
| `CodeSalesTypeID` | Sales Type | The sales type is the second level of categorization for sales records. Types are the children of groups, and parents of categories. | Dropdown (Sales Type) | Global |  | `sales.CodeSalesTypeID · TEXT` | Sales Type |
| `CodeUnitSalesTypeID` | Unit Sales Type | Select the unit sales type from this field. | Dropdown (Unit Sales Type Code) | Global |  | `sales.CodeUnitSalesTypeID · TEXT` | Unit Sales Type Code |

### Money (8)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `GrossSalesAmount` | Gross Sales Amount | Enter the gross sales amount in this field. | Currency | Global |  | `sales.GrossSalesAmount · TEXT` |  |
| `NetSalesAmount` | Net Sales Amount | Enter the net sales amount in this field. | Currency | Global |  | `sales.NetSalesAmount · TEXT` |  |
| `SalesAdjustment1` | Sales Adjustment #1 | Enter any sales adjustments in this field. There are six sales adjustments fields which can be used to break down your adjustments. | Currency | Global |  | `sales.SalesAdjustment1 · TEXT` |  |
| `SalesAdjustment2` | Sales Adjustment #2 | Enter any sales adjustments in this field. There are six sales adjustments fields which can be used to break down your adjustments. | Currency | Global |  | `sales.SalesAdjustment2 · TEXT` |  |
| `SalesAdjustment3` | Sales Adjustment #3 | Enter any sales adjustments in this field. There are six sales adjustments fields which can be used to break down your adjustments. | Currency | Global |  | `sales.SalesAdjustment3 · TEXT` |  |
| `SalesAdjustment4` | Sales Adjustment #4 | Enter any sales adjustments in this field. There are six sales adjustments fields which can be used to break down your adjustments. | Currency | Global |  | `sales.SalesAdjustment4 · TEXT` |  |
| `SalesAdjustment5` | Sales Adjustment #5 | Enter any sales adjustments in this field. There are six sales adjustments fields which can be used to break down your adjustments. | Currency | Global |  | `sales.SalesAdjustment5 · TEXT` |  |
| `SalesAdjustment6` | Sales Adjustment #6 | Enter any sales adjustments in this field. There are six sales adjustments fields which can be used to break down your adjustments. | Currency | Global |  | `sales.SalesAdjustment6 · TEXT` |  |

### Quantities (5)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `MatchingCalendarYear` | Matching Calendar Year | This field displays the year of the effective date of the sale. | Number | Global |  | `sales.MatchingCalendarYear · TEXT` |  |
| `SalesID` | Sales RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `sales.SalesID · VARCHAR(64) NOT NULL` |  |
| `SalesPeriod` | Fiscal Period | Select the sales period from this field. | Number | Global |  | `sales.SalesPeriod · TEXT` |  |
| `SalesYear` | Fiscal Year | Select the sales year from this field. | Number | Global |  | `sales.SalesYear · TEXT` |  |
| `UnitSalesCount` | Unit Sales Count | Enter the sales unit count in this field if applicable. | Number | Global |  | `sales.UnitSalesCount · TEXT` |  |

### Dates & timestamps (2)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `EffectiveDate` | Effective Date | Enter the effective date of the sales in this field. | Date | Global |  | `sales.EffectiveDate · TEXT` |  |
| `PostingDate` | Posting Date | Enter the posting date of your sales data in this field. | Date | Global |  | `sales.PostingDate · TEXT` |  |

### Text & notes (3)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ClientSalesID` | Client Sales ID | If you have a custom identifier for sales, enter the sales ID in this field. | Text | Global |  | `sales.ClientSalesID · TEXT` |  |
| `MatchingCalendarMonthText` | Matching Calendar Month | This field displays the month of the effective date of the sale. | Text | Global |  | `sales.MatchingCalendarMonthText · TEXT` |  |
| `MatchingCalendarMonthYearText` | Matching Calendar Month / Year | This field displays the month and year--in Month, Year format--of the effective date of the sale. | Text | Global |  | `sales.MatchingCalendarMonthYearText · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Sales ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `sales.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `sales.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `sales.ModifiedDate · TEXT` |  |
