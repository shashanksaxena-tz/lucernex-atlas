# The Lucernex field-type vocabulary

**Stated up front.** The 7,421 fields use **315 distinct types**, and those types fall into exactly
five families. Two of the five carry relational meaning that a plain type name would not:
**60 foreign-key types** named after their target table (`Contract ID`, `Employer ID`, `Entity ID`)
and **229 dropdown-binding types** naming a reference code list (`Dropdown (Expense Type Code)`).
Together they are 1,671 fields — **22.5% of the whole schema is a typed reference, not a value.**
Everything else reduces to just **14 scalar types**, of which four (`Text`, `Currency`, `Number`,
`Date`) cover 4,480 fields, 60% of the product.

That the FK types are real declared schema metadata — not a naming convention this analysis
imposed — is **Observed** in [`../admin/009-related-fields-and-data-model.md`](../admin/009-related-fields-and-data-model.md),
which reads them straight off Lucernex's own `ShowObjectDetails.jsp` "Type" column.

All counts **Derived** by [`../mindmap/build_graph.py`](../mindmap/build_graph.py).

**Scope note.** This vocabulary deliberately covers **all 223 objects**, including the 27
Budget / Bid / Cost Tracking objects excluded from the rebuild on 2026-09-10. A type census that
silently omitted them would misreport how many types exist and which resolve — so the counts here
are census-wide by design. Types used *only* by out-of-scope objects (`Bid Package Template ID`,
`Budget Index Variable ID`, `Budget Template View ID`, `Budget Type ID`, and a handful of
`Dropdown (Bid …/Budget …)` code lists) are listed but not analysed.

## Families at a glance

| Family | Distinct types | Fields | Share | What it means |
|---|---:|---:|---:|---|
| `scalar` | 14 | 5,630 | 75.9% | A stored value. No relational meaning. |
| `foreign_key` | 60 | 972 | 13.1% | Type name ends in ` ID` and names its target table. A real join. |
| `dropdown` | 229 | 699 | 9.4% | `Dropdown (<Code list>)` — bound to a platform or tenant reference code list (docs/admin/007). |
| `soft_reference` | 10 | 118 | 1.6% | Names a target concept but has no ` ID` suffix — list-valued or widget-valued references. |
| `other` | 2 | 2 | 0.03% | Two one-off formatting types. |
| **Total** | **315** | **7,421** | | |

### How a type is parsed

A field is written `Name(Type)`. The type is everything between the **first** `(` and the **last**
`)`, because dropdown types embed their own parentheses (`CodeExpenseTypeID(Dropdown (Expense Type
Code))`). Classification is then purely mechanical: `Dropdown (…)` → dropdown; ends in ` ID` →
foreign_key; in the 14-name scalar set → scalar; in the 10-name soft-reference set →
soft_reference. Parsing recovers 7,421 fields against 7,421 declared — **zero discrepancy on all
223 objects**, so no field is silently dropped or double-counted.

## 1. Scalar types (14 types, 5,630 fields)

| Type | Fields | Objects using it |
|---|---:|---:|
| `Text` | 1916 | 197 |
| `Currency` | 1207 | 100 |
| `Number` | 846 | 180 |
| `Date` | 511 | 110 |
| `Boolean` | 460 | 103 |
| `Percentage` | 335 | 50 |
| `Time` | 267 | 163 |
| `5-Digit Number` | 49 | 18 |
| `2-Digit Number` | 15 | 14 |
| `Number with no digits` | 8 | 3 |
| `Acreage` | 7 | 7 |
| `Date Range` | 6 | 6 |
| `Percent or Currency` | 2 | 2 |
| `Number Format` | 1 | 1 |

Notes:

- `Currency` at 1,207 fields on 100 objects is the second-largest type in the product — a direct
  measure of how much of Lucernex is money. For ASG Edge+ this is the Constitution §4.4
  `BigDecimal`-only surface, and it is very large.
- `Time` (267 fields on 163 objects) is a **timestamp**, not a clock time: it is what
  `CreatedDate` / `ModifiedDate` use on every audited object. Confirmed by
  [`../data-fields/INDEX.md`](../data-fields/INDEX.md) (`sTYPE_TIME` — "typically a full timestamp
  such as Created/Modified date").
- `5-Digit Number` (49) and `2-Digit Number` (15) are fixed-precision decimals, used for
  latitude/longitude and for small ratios respectively — a presentation-precision type leaking into
  the schema.
- `Acreage` (7) is the only unit-bearing scalar. Area is otherwise carried as plain `Number` with
  the unit in a companion `CodeBuildingAreaUnitID` / `CodeLandAreaUnitID` dropdown — a pattern ASG
  Edge+ should decide on deliberately rather than inherit.

## 2. Foreign-key types (60 types, 972 fields)

Each type is literally named after the table it points at. `resolution` is how this corpus mapped
the type name onto one of the 223 objects; per-edge rationale is in
[`../mindmap/edges.json`](../mindmap/edges.json).

| Type | Fields | Objects using it | Resolves to | Resolution |
|---|---:|---:|---|---|
| `Member ID` | 290 | 162 | `Member` | high |
| `Entity ID` | 163 | 161 | `ProjectEntity` | high |
| `Contract ID` | 62 | 62 | `Contract` | high |
| `item ID` | 56 | 13 | — | unresolved |
| `Employer ID` | 40 | 30 | `Employer` | high |
| `Region ID` | 34 | 12 | `Region` | high |
| `Template ID` | 31 | 19 | `EntityTemplate` | high |
| `Country, State, County ID` | 26 | 22 | `StateProvinceCountry` | medium |
| `Task/Group ID` | 18 | 12 | `TaskGroup` | high |
| `County ID` | 17 | 16 | `Jurisdiction` | medium |
| `Budget Type ID` | 16 | 8 | `BudgetColumnType` | medium |
| `Covenant ID` | 15 | 15 | `Covenant` | high |
| `Equipment ID` | 14 | 13 | `Asset` | medium |
| `Contract Amendment ID` | 13 | 13 | `ContractAmendment` | high |
| `Portfolio ID` | 12 | 12 | `Program` | high |
| `Complex ID` | 11 | 11 | `Complex` | high |
| `Prototype ID` | 11 | 11 | `Prototype` | high |
| `Expense Setup ID` | 10 | 10 | `ExpenseSetup` | high |
| `DMA ID` | 10 | 10 | `DMA` | high |
| `Document ID` | 10 | 10 | `Document` | high |
| `Location ID` | 9 | 9 | `Location` | high |
| `Organization ID` | 8 | 8 | `Organization` | high |
| `Parcel ID` | 8 | 8 | `Parcel` | high |
| `Facility ID` | 7 | 7 | `Facility` | high |
| `Folder ID` | 7 | 7 | `Folder` | high |
| `Contract Term ID` | 5 | 5 | `ContractTerm` | high |
| `Scenario ID` | 5 | 3 | `Scenario` | high |
| `Work Flow ID` | 5 | 5 | `WorkFlow` | high |
| `Step ID` | 5 | 5 | `WorkFlowStep` | medium |
| `Budget Template View ID` | 4 | 3 | `BudgetView` | medium |
| `Report/Form Field ID` | 4 | 4 | `ReportGroupAvailableField` | low |
| `Payment Transaction ID` | 4 | 4 | `PaymentTransaction` | high |
| `RE Transaction ID` | 4 | 4 | `RETransaction` | high |
| `Property Tax Bill ID` | 3 | 3 | `PropertyTaxBill` | high |
| `Purchase Order ID` | 2 | 2 | `PurchaseOrder` | high |
| `Custom Drop Down ID` | 2 | 1 | — | unresolved |
| `Alternate Rent Schedule ID` | 2 | 2 | `AlternateRentSchedule` | high |
| `Percentage Rent ID` | 2 | 2 | `PercentageRent` | high |
| `Property Tax Assessment ID` | 2 | 2 | `PropertyTaxAssessment` | high |
| `Straight-Line Schedule ID` | 2 | 2 | `SLSummary` | medium |
| `DashboardComponent ID` | 2 | 2 | — | unresolved |
| `Action ID` | 2 | 1 | `WorkFlowTemplateStepAction` | low |
| `Work Flow Step ID` | 2 | 2 | `WorkFlowStep` | high |
| `Allowance ID` | 1 | 1 | `Allowance` | high |
| `Bid Package Template ID` | 1 | 1 | `BidPackageTemplate` | high |
| `Budget Index Variable ID` | 1 | 1 | `BudgetIndex` | high |
| `Custom Field ID` | 1 | 1 | `CustomCodeField` | high |
| `Escalation Index ID` | 1 | 1 | `EscalationIndex` | high |
| `Global Property Section ID` | 1 | 1 | `GlobalProperty` | medium |
| `Vendor Site ID` | 1 | 1 | `EmployerSite` | medium |
| `Email Received Log Record ID` | 1 | 1 | `EMailReceivedLog` | high |
| `RE Transaction Contact ID` | 1 | 1 | `ReTransScenContact` | medium |
| `Payment Receipt ID` | 1 | 1 | `PaymentReceipt` | high |
| `Property Tax Appeal ID` | 1 | 1 | `PropertyTaxAppeal` | high |
| `Property Tax Summary ID` | 1 | 1 | `PropertyTaxSummary` | high |
| `Recalc Override Notes ID` | 1 | 1 | `RecalcOverrideNotes` | high |
| `Sales Exclusion Cap ID` | 1 | 1 | `SalesExclusionCap` | high |
| `Space ID` | 1 | 1 | `Space` | high |
| `Expense Accrual Schedule ID` | 1 | 1 | `ExpenseAccrualSchedule` | high |
| `Work Flow Step Approver ID` | 1 | 1 | `WorkFlowStepApprover` | high |

### Reading the FK type list

- **The distribution is extremely skewed.** `Member ID` (290) and `Entity ID` (163) alone are 47%
  of all FK columns. The next, `Contract ID`, is 62. Thirty-one of the 60 FK types appear on five
  columns or fewer, and 17 appear exactly once.
- **`Member ID` is mostly audit, not domain.** **240 of its 290 columns are just `ModifiedByID`
  (161) and `CreatedByID` (79)**; the remaining 50 spread across 44 distinct column names. In ASG
  Edge+ this is not 290 relationships — it is one auditing concern applied 240 times, plus 50 real
  ones. (Note the asymmetry: 161 objects record who last modified a row, but only 79 record who
  created it.)
- **`Entity ID` always means `ProjectEntity`.** 161 of its 163 columns are literally named
  `ProjectEntityID`; the other two are `BudgetOptionTemplate.BudgetOptionTemplateID` and
  `DevelopmentSlot.ProjectPEID`. See [`project-entity.md`](project-entity.md).
- **Four type names lie about their target**, and each is a trap for a naive rebuild:

  | Type | Actually points at | Evidence |
  |---|---|---|
  | `Portfolio ID` | `Program` | **Observed** — `Contract.ProgramID` is typed `Portfolio ID` with UI Label "Portfolio" ([009](../admin/009-related-fields-and-data-model.md)) |
  | `Employer ID` | `Employer` — but the column is often called `VendorID` | **Observed** — `PaymentTransaction.VendorID` is typed `Employer ID` ([009](../admin/009-related-fields-and-data-model.md)); "Vendor" is a relabelled Employer |
  | `Country, State, County ID` | `StateProvinceCountry` | **Inferred** — columns are named `IStateProvinceCountryID`, and it is the only geography table |
  | `County ID` | `Jurisdiction` | **Inferred** — every `County ID` column is named `JurisdictionID` |

- **Three type names resolve to nothing in the 223 and are not database FKs at all** — they point
  outside the business-object model into platform configuration:

  | Type | Fields | What the columns are named | Reading |
  |---|---:|---|---|
  | `item ID` | 56 | 54 are `*PageLayoutID` / `*LayoutID` / `*ReportGroupDataID`; 2 are `AuditColumn.GroupID` / `.SubGroupID` | A generic **configuration-item** handle. Page Layouts, Report Groups and Data-Field groups are configuration metadata (docs/admin/005–008) and have no row in this 223-object export. The lower-case `item` — every other FK type is Title Case — marks it as a different kind of pointer. **Derived**, high confidence. |
  | `Custom Drop Down ID` | 2 | `CustomCodeField.CustomCodeTableID`, `.ParentCustomCodeTableID` | Points at the Client Drop Down tables of docs/admin/007, also configuration metadata. |
  | `DashboardComponent ID` | 2 | `Security.DashboardComponentID`, `UserClassSecurity.DashboardComponentID` | Points at dashboard configuration, likewise outside the export. |

  This is a finding about **scope**, not a gap in the data: the export covers business objects, and
  Lucernex's configuration layer (page layouts, data fields, drop downs, dashboards) is a
  *separate* model that the business objects reference by id. ASG Edge+'s PAGE-LAYOUTS-01 and
  MDM-01 live on exactly that other side of the line.

- **`Template ID` (31 fields) is polymorphic**: one type serving `BudgetTemplate`, `TaskTemplate`,
  `FolderTemplate`, `WorkFlowTemplate`, `EntityTemplate`, `ProcessTimelineTemplate`,
  `BidPackageTemplate` and `CostTrackingTemplate`. The target is decided by the **column name**, not
  the type. `build_graph.py` resolves it per-column; a rebuild must not model this as one FK.

## 3. Dropdown bindings (229 types, 699 fields)

Every dropdown type has the shape `Dropdown (<Code list name>)`. The code list is the reference
data behind docs/admin/007 (Firm & Client Drop Downs) — the direct analogue of ASG Edge+'s
Masters/MDM-01 domain.

Two structural facts matter more than the list itself:

- **157 of the 229 code lists are used by exactly one field.** The long tail is enormous:
  `Tenant Use Code`, `Tax Refund Type Code`, `Slot Type Code`, `Site Rating Code` and 153 others
  each back a single column. Only 21 code lists are used by 10 or more fields.
- **The naming is regular enough to generate from.** 214 of the 229 end in `Code`, and the
  `<Entity> <Facet> Code` pattern (`Parcel Group Code`, `Parcel Type Code`, `Parcel Status Code`,
  `Parcel Category Code`, `Parcel Use Code`, `Parcel Access Type Code`, …) repeats per entity. This
  is the same **Group / Type / Status / Category / Use** facet quintet applied across the estate —
  strong evidence that Lucernex generates these lists from an entity template rather than
  hand-authoring each one. A Masters implementation for ASG Edge+ can and should exploit the same
  regularity.

<details>
<summary>All 229 dropdown code lists, most-used first (fields / objects)</summary>

| Code list | Fields | Objects |
|---|---:|---:|
| `Custom Field` | 77 | 6 |
| `Currency Type Code` | 43 | 39 |
| `Building Area Unit Code` | 23 | 23 |
| `Market Area Code` | 23 | 13 |
| `Expense Group Code` | 21 | 19 |
| `Job Title Code` | 21 | 12 |
| `Project Type Code` | 20 | 10 |
| `Expense Type Code` | 19 | 18 |
| `Frequency Code` | 18 | 13 |
| `Exchange Rate Type Code` | 15 | 2 |
| `Market Type Code` | 12 | 12 |
| `Project Phase Code` | 11 | 11 |
| `Sales Group` | 10 | 9 |
| `User Class` | 10 | 8 |
| `Construction Type Code` | 10 | 10 |
| `Deal Type Code` | 10 | 10 |
| `Distribution Center Code` | 10 | 10 |
| `Expense Category Code` | 9 | 9 |
| `Responsible Party` | 8 | 3 |
| `Asset Category Code` | 7 | 6 |
| `Contact Type Code` | 7 | 7 |
| `Approval Status Code` | 7 | 6 |
| `Condition Code` | 7 | 1 |
| `Job Function Code` | 6 | 6 |
| `ASC 842 Schedule Type` | 5 | 5 |
| `IFRS 16 Schedule Type` | 5 | 5 |
| `Accounting Method Code` | 5 | 4 |
| `Task Status Code` | 5 | 5 |
| `Usage Group Code` | 5 | 5 |
| `Usage Unit Type Code` | 5 | 5 |
| `Proration Method Code` | 4 | 4 |
| `Time Unit Code` | 4 | 2 |
| `SQL Table Code` | 4 | 4 |
| `Folder Template Action Code` | 4 | 4 |
| `Straight Line Schedule Type` | 4 | 4 |
| `Priority Code` | 4 | 4 |
| `Maintenance Remedy Code` | 3 | 1 |
| `Frequency Unit Code` | 3 | 2 |
| `Last Action Status Code` | 3 | 3 |
| `Budget Status` | 3 | 2 |
| `CSI Code` | 3 | 3 |
| `Contract Use Code` | 3 | 3 |
| `Payment Method Code` | 3 | 3 |
| `Land Area Unit Code` | 3 | 3 |
| `Area Code` | 3 | 1 |
| `Region Code` | 3 | 1 |
| `Day Of Week Code` | 3 | 3 |
| `Work Flow Status Code` | 3 | 3 |
| `Asset Group Code` | 2 | 2 |
| `Asset Type Code` | 2 | 2 |
| `CPI Index Code` | 2 | 2 |
| `Building Class Code` | 2 | 2 |
| `Term Status Code` | 2 | 2 |
| `Term Type Code` | 2 | 2 |
| `Accounting Adjustment Type Code` | 2 | 2 |
| `Covenant Category Code` | 2 | 2 |
| `Covenant Group Code` | 2 | 2 |
| `Covenant Status Code` | 2 | 2 |
| `Covenant Type Code` | 2 | 2 |
| `Accrual Type Code` | 2 | 2 |
| `Recovery Group Code` | 2 | 2 |
| `Recovery Type Code` | 2 | 2 |
| `Security Type Code` | 2 | 2 |
| `Part Order Status Code` | 2 | 2 |
| `Lock Out Reason Code` | 2 | 2 |
| `Source Entity Code` | 2 | 2 |
| `Percentage Rent Type Code` | 2 | 2 |
| `Scenario Deal Type Code` | 2 | 2 |
| `Sales Type` | 2 | 2 |
| `Security Privilege Code` | 2 | 2 |
| `Zoning Code` | 2 | 1 |
| `Use Rent Model Type Code` | 2 | 2 |
| `Allowance Group Code` | 1 | 1 |
| `Allowance Type Code` | 1 | 1 |
| `Alt Rent Math Code` | 1 | 1 |
| `Asset Department Code` | 1 | 1 |
| `Asset Operation Status Code` | 1 | 1 |
| `Asset Product Type Code` | 1 | 1 |
| `Asset Suspension Status Code` | 1 | 1 |
| `Measurement Unit Code` | 1 | 1 |
| `Weight Unit Code` | 1 | 1 |
| `Bid Grace Period Time Unit Code` | 1 | 1 |
| `Bid Package Status Code` | 1 | 1 |
| `Budget Change Reason Code` | 1 | 1 |
| `Budget Value Units Code` | 1 | 1 |
| `Co Tenancy Group Code` | 1 | 1 |
| `Co Tenancy Type Code` | 1 | 1 |
| `Responsible Party System Code` | 1 | 1 |
| `Competitor Type Code` | 1 | 1 |
| `Complex Status Code` | 1 | 1 |
| `Complex Type Code` | 1 | 1 |
| `Agreement Type Code` | 1 | 1 |
| `Asset Class Code` | 1 | 1 |
| `Contract Category Code` | 1 | 1 |
| `Contract Group Code` | 1 | 1 |
| `Contract Status Code` | 1 | 1 |
| `Contract Type Code` | 1 | 1 |
| `Holding Interest Code` | 1 | 1 |
| `Amendment Group Code` | 1 | 1 |
| `Amendment Type Code` | 1 | 1 |
| `Asset Type Test Code` | 1 | 1 |
| `Covenant Template Code` | 1 | 1 |
| `Market Demographics Code` | 1 | 1 |
| `Demographic Results Type Code` | 1 | 1 |
| `Results Status Code` | 1 | 1 |
| `Third Party Vendor Code` | 1 | 1 |
| `Distance Unit Code` | 1 | 1 |
| `Slot Type Code` | 1 | 1 |
| `Store Phase Code` | 1 | 1 |
| `Document Convert Status Code` | 1 | 1 |
| `Document Type Code` | 1 | 1 |
| `Coverage Code` | 1 | 1 |
| `Master Employer Group Code` | 1 | 1 |
| `Vendor Grade Code` | 1 | 1 |
| `Index Group Code` | 1 | 1 |
| `Index Source Code` | 1 | 1 |
| `Index Type Code` | 1 | 1 |
| `Escalation Category Code` | 1 | 1 |
| `Escalation Group Code` | 1 | 1 |
| `Escalation Type Code` | 1 | 1 |
| `Base Year Amount Type Code` | 1 | 1 |
| `Calculation Method Code` | 1 | 1 |
| `Cap Type Code` | 1 | 1 |
| `Escalation Payment Method Code` | 1 | 1 |
| `Exp Rec Based On Code` | 1 | 1 |
| `Pro Rata Share Method Code` | 1 | 1 |
| `Recovery Item Group Code` | 1 | 1 |
| `Recovery Item Type Code` | 1 | 1 |
| `Recovery Section Code` | 1 | 1 |
| `Adjustment Method Code` | 1 | 1 |
| `Expense Acct Code` | 1 | 1 |
| `Plan Forecast Based On Code` | 1 | 1 |
| `Plan Forecast Group Code` | 1 | 1 |
| `Facility Category Code` | 1 | 1 |
| `Facility Group Code` | 1 | 1 |
| `Facility Status Code` | 1 | 1 |
| `Facility Type Code` | 1 | 1 |
| `Facility Use Code` | 1 | 1 |
| `Financial Adjustment Status Code` | 1 | 1 |
| `Insurance Category Code` | 1 | 1 |
| `Insurance Group Code` | 1 | 1 |
| `Insurance Type Code` | 1 | 1 |
| `Invoice Status Code` | 1 | 1 |
| `Change Reason Code` | 1 | 1 |
| `Discipline Code` | 1 | 1 |
| `Form Type` | 1 | 1 |
| `Location Code` | 1 | 1 |
| `Method Of Contact Code` | 1 | 1 |
| `Key Date Action Code` | 1 | 1 |
| `Key Date Group Code` | 1 | 1 |
| `Key Date Type Code` | 1 | 1 |
| `Lease Status Code` | 1 | 1 |
| `Lease Type Code` | 1 | 1 |
| `Property Primary Use Code` | 1 | 1 |
| `Inspection Period Start Code` | 1 | 1 |
| `Inspection Type Code` | 1 | 1 |
| `Location Category Code` | 1 | 1 |
| `Location Group Code` | 1 | 1 |
| `Location Status Code` | 1 | 1 |
| `Location Type Code` | 1 | 1 |
| `Location Use Code` | 1 | 1 |
| `Analytics Role Code` | 1 | 1 |
| `Member Action Code` | 1 | 1 |
| `Org Category Code` | 1 | 1 |
| `Org Group Code` | 1 | 1 |
| `Org Type Code` | 1 | 1 |
| `Funding Type Code` | 1 | 1 |
| `Parcel Category Code` | 1 | 1 |
| `Parcel Group Code` | 1 | 1 |
| `Parcel Status Code` | 1 | 1 |
| `Parcel Type Code` | 1 | 1 |
| `Parcel Use Code` | 1 | 1 |
| `Parcel Access Category Code` | 1 | 1 |
| `Parcel Access Group Code` | 1 | 1 |
| `Parcel Access Type Code` | 1 | 1 |
| `Denominator Code` | 1 | 1 |
| `Parking Group Code` | 1 | 1 |
| `Parking Type Code` | 1 | 1 |
| `Party Group Code` | 1 | 1 |
| `Party Type Code` | 1 | 1 |
| `Receipt Type Code` | 1 | 1 |
| `Store Type Code` | 1 | 1 |
| `Pro Forma Budget Status Code` | 1 | 1 |
| `Tax Appeal Result Code` | 1 | 1 |
| `Tax Appeal Status Code` | 1 | 1 |
| `Tax Paid To Code` | 1 | 1 |
| `Tax Refund Type Code` | 1 | 1 |
| `Property Tax Status Code` | 1 | 1 |
| `Tax Type Code` | 1 | 1 |
| `Property Tax Type Code` | 1 | 1 |
| `RE Transaction Status Code` | 1 | 1 |
| `Pass Through Type Code` | 1 | 1 |
| `Response Time Code` | 1 | 1 |
| `Responsibility Group Code` | 1 | 1 |
| `Responsibility Type Code` | 1 | 1 |
| `Schedule Creation Reason Code` | 1 | 1 |
| `Sales Category Code` | 1 | 1 |
| `Unit Sales Type Code` | 1 | 1 |
| `Exclusion Cap Code` | 1 | 1 |
| `Decision Status Code` | 1 | 1 |
| `Property Type Code` | 1 | 1 |
| `Scenario Type Code` | 1 | 1 |
| `Guarantee Type Code` | 1 | 1 |
| `Security Deposit Group Code` | 1 | 1 |
| `Security Deposit Status Code` | 1 | 1 |
| `Security Deposit Type Code` | 1 | 1 |
| `Problem Code` | 1 | 1 |
| `SRQ Source Code` | 1 | 1 |
| `SRQ Status Code` | 1 | 1 |
| `SRQ Type Code` | 1 | 1 |
| `Location Access Code` | 1 | 1 |
| `Site Rating Code` | 1 | 1 |
| `Space Group Code` | 1 | 1 |
| `Space Status Code` | 1 | 1 |
| `Space Type Code` | 1 | 1 |
| `Space Use Code` | 1 | 1 |
| `Task Lead Lag Type Code` | 1 | 1 |
| `Tenant Category Code` | 1 | 1 |
| `Tenant Group Code` | 1 | 1 |
| `Tenant Status Code` | 1 | 1 |
| `Tenant Type Code` | 1 | 1 |
| `Tenant Use Code` | 1 | 1 |
| `Usage Category Code` | 1 | 1 |
| `Usage Type Code` | 1 | 1 |
| `Offset Group Code` | 1 | 1 |
| `Offset Type Code` | 1 | 1 |
| `Insurance Policy Type Code` | 1 | 1 |
| `Classification Code` | 1 | 1 |
| `Evaluation Rating Code` | 1 | 1 |

</details>

## 4. Soft references (10 types, 118 fields)

Reference-shaped types with **no ` ID` suffix**. They are deliberately kept out of the FK family:
several are list-valued (a widget backed by a join table, not a column FK), so promoting them to
edges would invent cardinality that is not in the data.

| Type | Fields | Objects | Reading | Confidence |
|---|---:|---:|---|---|
| `Contact` | 54 | 25 | Person/contact lookup. Columns split two ways: singular (`Complex.LandlordID`, `Document.AuthoredByPersonID`) and the list-valued `LinkProjectEntityContactListData`, which is a widget over the `LinkProjectEntityContact` join table. | Inferred |
| `Dropdown` | 21 | 20 | Bare dropdown with **no** code list named. 12 of the 21 are `ManagerIDList` — a multi-select of Members — so this is the multi-valued dropdown widget rather than a code-list binding. | Inferred |
| `Entity` | 14 | 13 | A *soft* ProjectEntity handle, distinct from the hard `Entity ID`. Columns are `AssociatedProjectEntityID`, `AssetAssociatedProjectEntityID`, `OpeningProjectPEID`, `RelatedPEID` — secondary or cross-entity pointers rather than the owning-entity key. | Derived |
| `Document List` | 8 | 8 | Multi-valued document attachment (`DocumentIDList`) on 8 objects. A join table, not a column. | Derived |
| `Custom List` | 7 | 1 | All 7 are `Firm_*` columns on `Contract` — a tenant-defined Custom List embedded in a layout (docs/admin/006). | Observed |
| `Part` | 5 | 5 | Lookup to `Part`. | Inferred |
| `Parts Package` | 3 | 3 | Lookup to `PartPackage`. | Inferred |
| `Holiday Calendar` | 3 | 3 | Lookup to `HolidaySchedule`. | Inferred |
| `Member` | 2 | 2 | Member lookup that is not audit-shaped. | Inferred |
| `Response` | 1 | 1 | Lookup to `IssueResponse`. | Inferred |

## 5. Other (2 types, 2 fields)

| Type | Field | Reading |
|---|---|---|
| `Current Date` | `Firm.CurrentDate` | A server-evaluated "today" exposed as a field — a computed value, not stored data. |
| `Date Format` | `Member.DatePattern` | A per-user date-format preference string. Its type names a *format*, not a value domain. |

Both are single-use presentation types that leaked into the schema type system. Neither should
survive into ASG Edge+ as a type.

## What this means for ASG Edge+

| Observation | Rebuild consequence |
|---|---|
| 22.5% of fields are typed references, declared in the schema | The type system *is* the relationship metadata. ASG Edge+ should model references as first-class typed attributes too, not as untyped `Long` columns — this is what makes Lucernex's Related Fields palette possible at all. |
| 1,207 `Currency` fields on 100 objects | The `BigDecimal`-only rule (Constitution §4.4) has a very wide blast radius. Budget a systematic money type, not per-field decisions. |
| 229 code lists, 157 used once, generated from a Group/Type/Status/Category/Use facet pattern | MDM-01 should support **generated** master lists per entity rather than 229 hand-registered ones. |
| `item ID` / `Custom Drop Down ID` / `DashboardComponent ID` point outside the business model | Confirms the Lucernex split between business objects and configuration metadata. ASG Edge+ already draws this line (Configuration-Service vs. the rest); the FK types are evidence the split is load-bearing, not cosmetic. |
| `Portfolio ID` → `Program`, `VendorID` → `Employer` | Internal names, UI labels and type names disagree in Lucernex. Any migration mapping must key on the **type**, never the label. |

## Open questions

1. Are the 229 dropdown code lists Global-only, or can a tenant add code lists that appear as new
   `Dropdown (…)` types? docs/admin/007 shows both Firm and Client drop-downs; whether a Client
   drop-down produces a distinct schema type was not established.
2. `Percent or Currency` (2 fields) is a union type. Which column decides the interpretation at
   runtime?
3. `Number with no digits` (8 fields, 3 objects) — integer, or a formatting instruction? The name
   suggests presentation, which would make it a fourth leaked presentation type.
4. Does the platform enforce referential integrity on FK-typed columns, or is the type purely a
   UI/lookup hint? Nothing in this export settles it, and it changes whether ASG Edge+ can trust
   migrated data.
