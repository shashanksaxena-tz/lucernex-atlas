# ProFormaBudget

*47 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `pro_forma_budget`*

The financial feasibility analysis for a prospective deal or capital project — IRR, NPV, and Payback Period alongside a Finance Committee Approval flag, gating whether a deal proceeds. 46 Global fields under Summary Information, dominated by MONEY fields (36 of 46) since this is fundamentally a discounted-cash-flow worksheet.

Source: `data-fields/pro-forma-budget.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 47 |
| Fields with a vendor definition | 4 of 47 inventoried |
| Physical tables | `pro_forma_budget` |
| Replication database | `lxr_drp_bbw` |
| Catalogued fields | 46 (46 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Lands in pro_forma_budget

**Observed.** The field inventory names the physical destination of every column: one table in the database lxr_drp_bbw. Every field node carries its own table and column, so the mapping is per column, not per record.

### A per-tenant database name

**Derived.** The physical database is lxr_drp_bbw — the tenant's name is in the database name. That is one more piece of evidence for database-per-tenant and against a single shared schema, alongside the Firm_ columns.

### 4 fields carry a vendor definition

**Observed.** 4 of this record's 47 inventoried fields have prose written by the vendor saying what the field is for. Open any field node to read it — this is the one reading of the corpus that explains fields rather than listing them. It is a sharper reading of the same export the object census comes from, not a second source: where it agrees with the census that is one fact stated twice, not two facts.

### Required: the two captures disagree

**Observed.** The field inventory marks 1 of this record's fields required; the Data Fields catalogue marks 1; 1 appear in both. These two ARE separate captures — the catalogue is the Manage Data Fields screen, the inventory is the object export — so the disagreement is real and not a reading artefact. Estate-wide it is 606 against 637 with only 515 shared, so 213 fields are required according to exactly one of them. A rebuild that picks one capture and ignores the other silently drops obligations.

### Replication coverage: not materialised

**Observed.** Observed of the loader, not of the product. The replication target lxr_drp_bbw has never created a table for this record: Table may not exist in the database yet. No data has ever been returned for this Lx object, and the loader only issues CREATE TABLE once the first row arrives. The configuration is in place, so this table and all of its columns will be created automatically as soon as data is entered in Lx. That is a statement about one loader's coverage and says nothing about whether the record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, every one marked extracted, table never created, yet it is the universal supertype of a tenant holding 2,014 contracts, so it plainly is not empty. Do not read the 69-created / 150-not-created split as the size of the product's schema.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `ProjectEntityID` |  |  | Entity ID | — |  | `pro_forma_budget.ProjectEntityID · TEXT` | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `CodeProFormaBudgetStatusID` | Finance Committee Approval |  | Dropdown (Pro Forma Budget Status Code) | Global |  | `pro_forma_budget.CodeProFormaBudgetStatusID · TEXT` | Pro Forma Budget Status Code |

### Money (36)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `NPV` |  |  | Currency | Global |  | `pro_forma_budget.NPV · TEXT` |  |
| `ProjectedCostCapitalBeyond` | Projected Cost Capital Beyond Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostCapitalBeyond · TEXT` |  |
| `ProjectedCostCapitalFifthYr` | Projected Cost Capital Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostCapitalFifthYr · TEXT` |  |
| `ProjectedCostCapitalFourthYr` | Projected Cost Capital Fourth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostCapitalFourthYr · TEXT` |  |
| `ProjectedCostCapitalNextYr` | Projected Cost Capital Next Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostCapitalNextYr · TEXT` |  |
| `ProjectedCostCapitalPriorYear` | Projected Cost Capital PriorYear |  | Currency | Global |  | `pro_forma_budget.ProjectedCostCapitalPriorYear · TEXT` |  |
| `ProjectedCostCapitalThirdYr` | Projected Cost Capital Third Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostCapitalThirdYr · TEXT` |  |
| `ProjectedCostCapitalThisYr` | Projected Cost Capital This Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostCapitalThisYr · TEXT` |  |
| `ProjectedCostOperatingBeyond` | Projected Cost Operating Beyond Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostOperatingBeyond · TEXT` |  |
| `ProjectedCostOperatingFifthYr` | Projected Cost Operating Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostOperatingFifthYr · TEXT` |  |
| `ProjectedCostOperatingFourthYr` | Projected Cost Operating Fourth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostOperatingFourthYr · TEXT` |  |
| `ProjectedCostOperatingNextYr` | Projected Cost Operating Next Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostOperatingNextYr · TEXT` |  |
| `ProjectedCostOperatingPriorYr` | Projected Cost Operating Prior Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostOperatingPriorYr · TEXT` |  |
| `ProjectedCostOperatingThirdYr` | Projected Cost Operating Third Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostOperatingThirdYr · TEXT` |  |
| `ProjectedCostOperatingThisYr` | Projected Cost Operating Current Year |  | Currency | Global |  | `pro_forma_budget.ProjectedCostOperatingThisYr · TEXT` |  |
| `ProjectedMarginBeyond` | Projected Margin Beyond Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedMarginBeyond · TEXT` |  |
| `ProjectedMarginFifthYr` | Projected Margin Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedMarginFifthYr · TEXT` |  |
| `ProjectedMarginFourthYr` | Projected Margin Fourth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedMarginFourthYr · TEXT` |  |
| `ProjectedMarginNextYr` | Projected Margin Next Year |  | Currency | Global |  | `pro_forma_budget.ProjectedMarginNextYr · TEXT` |  |
| `ProjectedMarginPriorYear` | Projected Margin Prior Year |  | Currency | Global |  | `pro_forma_budget.ProjectedMarginPriorYear · TEXT` |  |
| `ProjectedMarginThirdYr` | Projected Margin Third Year |  | Currency | Global |  | `pro_forma_budget.ProjectedMarginThirdYr · TEXT` |  |
| `ProjectedMarginThisYr` | Projected Margin This Year |  | Currency | Global |  | `pro_forma_budget.ProjectedMarginThisYr · TEXT` |  |
| `ProjectedPropTaxesBeyond` | Projected Property Taxes Beyond Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedPropTaxesBeyond · TEXT` |  |
| `ProjectedPropTaxesFifthYr` | Projected Property Taxes Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedPropTaxesFifthYr · TEXT` |  |
| `ProjectedPropTaxesFourthYr` | Projected Property Taxes Fourth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedPropTaxesFourthYr · TEXT` |  |
| `ProjectedPropTaxesNextYr` | Projected Property Taxes Next Year |  | Currency | Global |  | `pro_forma_budget.ProjectedPropTaxesNextYr · TEXT` |  |
| `ProjectedPropTaxesPriorYear` | Projected Property Taxes PriorYear |  | Currency | Global |  | `pro_forma_budget.ProjectedPropTaxesPriorYear · TEXT` |  |
| `ProjectedPropTaxesThirdYr` | Projected Property Taxes Third Year |  | Currency | Global |  | `pro_forma_budget.ProjectedPropTaxesThirdYr · TEXT` |  |
| `ProjectedPropTaxesThisYr` | Projected Property Taxes This Year |  | Currency | Global |  | `pro_forma_budget.ProjectedPropTaxesThisYr · TEXT` |  |
| `ProjectedSalesBeyond` | Projected Sales Beyond Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedSalesBeyond · TEXT` |  |
| `ProjectedSalesFifthYr` | Projected Sales Fifth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedSalesFifthYr · TEXT` |  |
| `ProjectedSalesFourthYr` | Projected Sales Fourth Year |  | Currency | Global |  | `pro_forma_budget.ProjectedSalesFourthYr · TEXT` |  |
| `ProjectedSalesNextYr` | Projected Sales Next Year |  | Currency | Global |  | `pro_forma_budget.ProjectedSalesNextYr · TEXT` |  |
| `ProjectedSalesPriorYr` | Projected Sales Prior Year |  | Currency | Global |  | `pro_forma_budget.ProjectedSalesPriorYr · TEXT` |  |
| `ProjectedSalesThirdYr` | Projected Sales Third Year |  | Currency | Global |  | `pro_forma_budget.ProjectedSalesThirdYr · TEXT` |  |
| `ProjectedSalesThisYr` | Projected Sales This Year |  | Currency | Global |  | `pro_forma_budget.ProjectedSalesThisYr · TEXT` |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `IRR` |  |  | Percentage | Global |  | `pro_forma_budget.IRR · TEXT` |  |
| `ROI` |  |  | Percentage | Global |  | `pro_forma_budget.ROI · TEXT` |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `PaybackPeriod` | Payback Period |  | 2-Digit Number | Global |  | `pro_forma_budget.PaybackPeriod · TEXT` |  |
| `ProFormaBudgetID` | Pro Forma Budget RecID | This field contains a Base Entity System Identifier for your record. It is assigned automatically by the system, and is not editable. | Number | Global |  | `pro_forma_budget.ProFormaBudgetID · VARCHAR(64) NOT NULL` |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `DateOfFinancials` | Date Of Financials |  | Date | Global |  | `pro_forma_budget.DateOfFinancials · TEXT` |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `NotesFinancials` | Notes Financials |  | Text | Global |  | `pro_forma_budget.NotesFinancials · TEXT` |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | What it is for | Declared type | Scope | Req | Physical column | Points at |
|---|---|---|---|---|---|---|---|
| `BOMapClientRecordID` | Pro Forma Budget ClientID | The ClientID field is a free form text field that can be used when importing data to uniquely look up a record for update. This record identifier can either be system-generated or defined by the user upon the initial import of record data. The ClientID has the database name "BOMapClientRecordID". | Text | Global | yes | `pro_forma_budget.BOMapClientRecordID · TEXT` |  |
| `ModifiedByID` | Modified By | The Modified By field is a system-populated field which captures the name of the member who made a change to a record. | Member ID | Global |  | `pro_forma_budget.ModifiedByID · TEXT` | [Member](Member.md) |
| `ModifiedDate` | Modified Date | The Modified Date field is a system-populated field which captures the date that a modification is made to a record. | Time | Global |  | `pro_forma_budget.ModifiedDate · TEXT` |  |
