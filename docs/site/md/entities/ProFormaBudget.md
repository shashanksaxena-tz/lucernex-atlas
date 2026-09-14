# ProFormaBudget

*47 fields · module: Budgeting, Cost Tracking & Bidding — OUT OF SCOPE · Postgres: `pro_forma_budget`*

The financial feasibility analysis for a prospective deal or capital project — IRR, NPV, and Payback Period alongside a Finance Committee Approval flag, gating whether a deal proceeds. 46 Global fields under Summary Information, dominated by MONEY fields (36 of 46) since this is fundamentally a discounted-cash-flow worksheet.

Source: `data-fields/pro-forma-budget.md`

## At a glance

|  | Value |
|---|---|
| Fields declared | 47 |
| Catalogued fields | 46 (46 global, 0 firm) |
| Physical tables | 1 |
| Referenced by | 0 keys from 0 record types |
| Points at | 2 other records |
| Tenancy position | entity_scoped |
| Rules that name it | 0 |

## What to know before rebuilding this

### Tenant-scoped, one join deep

**Derived.** This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant isolation has to be enforced by joining to that row and filtering on its FirmID — or it is not enforced at all. 161 of the 223 record types are shaped this way.

### Out of scope by decision

**Observed.** Its module is excluded from the rebuild. It stays in the census so impact analysis through the relationship graph is never silently wrong at the boundary, but nothing here is being built.

## Fields

### Relationships (foreign keys) (1)

Typed pointers to other records. Lx names each FK type after the table it points at, so the relational model is declared rather than implied.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `ProjectEntityID` |  | Entity ID | — |  | [ProjectEntity](ProjectEntity.md) |

### Coded values (drop-downs) (1)

Fields bound to a master code table. Every one of these is a place where an administrator, not a developer, controls the allowed values.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `CodeProFormaBudgetStatusID` | Finance Committee Approval | Dropdown (Pro Forma Budget Status Code) | Global |  | Pro Forma Budget Status Code |

### Money (36)

Currency amounts. Stored as TEXT in the physical database, which is why the rebuild must impose BigDecimal typing of its own.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `NPV` |  | Currency | Global |  |  |
| `ProjectedCostCapitalBeyond` | Projected Cost Capital Beyond Fifth Year | Currency | Global |  |  |
| `ProjectedCostCapitalFifthYr` | Projected Cost Capital Fifth Year | Currency | Global |  |  |
| `ProjectedCostCapitalFourthYr` | Projected Cost Capital Fourth Year | Currency | Global |  |  |
| `ProjectedCostCapitalNextYr` | Projected Cost Capital Next Year | Currency | Global |  |  |
| `ProjectedCostCapitalPriorYear` | Projected Cost Capital PriorYear | Currency | Global |  |  |
| `ProjectedCostCapitalThirdYr` | Projected Cost Capital Third Year | Currency | Global |  |  |
| `ProjectedCostCapitalThisYr` | Projected Cost Capital This Year | Currency | Global |  |  |
| `ProjectedCostOperatingBeyond` | Projected Cost Operating Beyond Fifth Year | Currency | Global |  |  |
| `ProjectedCostOperatingFifthYr` | Projected Cost Operating Fifth Year | Currency | Global |  |  |
| `ProjectedCostOperatingFourthYr` | Projected Cost Operating Fourth Year | Currency | Global |  |  |
| `ProjectedCostOperatingNextYr` | Projected Cost Operating Next Year | Currency | Global |  |  |
| `ProjectedCostOperatingPriorYr` | Projected Cost Operating Prior Year | Currency | Global |  |  |
| `ProjectedCostOperatingThirdYr` | Projected Cost Operating Third Year | Currency | Global |  |  |
| `ProjectedCostOperatingThisYr` | Projected Cost Operating Current Year | Currency | Global |  |  |
| `ProjectedMarginBeyond` | Projected Margin Beyond Fifth Year | Currency | Global |  |  |
| `ProjectedMarginFifthYr` | Projected Margin Fifth Year | Currency | Global |  |  |
| `ProjectedMarginFourthYr` | Projected Margin Fourth Year | Currency | Global |  |  |
| `ProjectedMarginNextYr` | Projected Margin Next Year | Currency | Global |  |  |
| `ProjectedMarginPriorYear` | Projected Margin Prior Year | Currency | Global |  |  |
| `ProjectedMarginThirdYr` | Projected Margin Third Year | Currency | Global |  |  |
| `ProjectedMarginThisYr` | Projected Margin This Year | Currency | Global |  |  |
| `ProjectedPropTaxesBeyond` | Projected Property Taxes Beyond Fifth Year | Currency | Global |  |  |
| `ProjectedPropTaxesFifthYr` | Projected Property Taxes Fifth Year | Currency | Global |  |  |
| `ProjectedPropTaxesFourthYr` | Projected Property Taxes Fourth Year | Currency | Global |  |  |
| `ProjectedPropTaxesNextYr` | Projected Property Taxes Next Year | Currency | Global |  |  |
| `ProjectedPropTaxesPriorYear` | Projected Property Taxes PriorYear | Currency | Global |  |  |
| `ProjectedPropTaxesThirdYr` | Projected Property Taxes Third Year | Currency | Global |  |  |
| `ProjectedPropTaxesThisYr` | Projected Property Taxes This Year | Currency | Global |  |  |
| `ProjectedSalesBeyond` | Projected Sales Beyond Fifth Year | Currency | Global |  |  |
| `ProjectedSalesFifthYr` | Projected Sales Fifth Year | Currency | Global |  |  |
| `ProjectedSalesFourthYr` | Projected Sales Fourth Year | Currency | Global |  |  |
| `ProjectedSalesNextYr` | Projected Sales Next Year | Currency | Global |  |  |
| `ProjectedSalesPriorYr` | Projected Sales Prior Year | Currency | Global |  |  |
| `ProjectedSalesThirdYr` | Projected Sales Third Year | Currency | Global |  |  |
| `ProjectedSalesThisYr` | Projected Sales This Year | Currency | Global |  |  |

### Rates & percentages (2)

Percentage inputs and computed rates.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `IRR` |  | Percentage | Global |  |  |
| `ROI` |  | Percentage | Global |  |  |

### Quantities (2)

Counts, areas and other plain numeric measures.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `PaybackPeriod` | Payback Period | 2-Digit Number | Global |  |  |
| `ProFormaBudgetID` | Pro Forma Budget RecID | Number | Global |  |  |

### Dates & timestamps (1)

Dates that drive schedules, and system timestamps.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `DateOfFinancials` | Date Of Financials | Date | Global |  |  |

### Text & notes (1)

Free text. Notably, free text is never allowed to drive a conditional display rule.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `NotesFinancials` | Notes Financials | Text | Global |  |  |

### Audit & record keeping (3)

Who created and changed the record, and the identifiers that survive migration.

| Field | Label | Declared type | Scope | Req | Points at |
|---|---|---|---|---|---|
| `BOMapClientRecordID` | Pro Forma Budget ClientID | Text | Global | yes |  |
| `ModifiedByID` | Modified By | Member ID | Global |  | [Member](Member.md) |
| `ModifiedDate` | Modified Date | Time | Global |  |  |
