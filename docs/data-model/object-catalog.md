# Object catalog — all 223 Lucernex objects

**Stated up front.** Every business object in the product, in one table — including the 27 marked
**out-of-scope** (Budgeting / Bid / Cost Tracking), retained here for census and FK-graph
completeness by explicit instruction but carrying a one-line purpose and no analysis. Source:
`_lucernex_objects_summary.txt`, parsed by [`../mindmap/build_graph.py`](../mindmap/build_graph.py)
(**Derived**; machine-readable form in [`../mindmap/objects.json`](../mindmap/objects.json)).

Field counts total **7,421** and the parse recovers all of them, so this table is complete — no
object is summarised away. Ten objects hold a third of the schema:

| Rank | Object | Fields | Share |
|---:|---|---:|---:|
| 1 | `Contract` | 570 | 7.7% |
| 2 | `ExpenseRecovery` | 565 | 7.6% |
| 3 | `LeaseInfo` | 219 | 3.0% |
| 4 | `Program` | 180 | 2.4% |
| 5 | `Parcel` | 154 | 2.1% |
| 6 | `Location` | 141 | 1.9% |
| 7 | `SLSummary` | 134 | 1.8% |
| 8 | `Facility` | 133 | 1.8% |
| 9 | `Asset` | 122 | 1.6% |
| 10 | `PaymentTransaction` / `PaymentTransactionFullImport` | 118 each | 3.2% |

Excluding the 27 out-of-scope objects, the **in-scope census is 196 objects and 6,875 fields**. No
object in the top ten is out of scope.

## Column meanings

| Column | Meaning |
|---|---|
| **Table(s)** | The `PG TABLE` cell. `_(none)_` means the export named no physical table — see [`foreign-key-graph.md`](foreign-key-graph.md#6-objects-with-no-physical-table). Two objects name four tables each. |
| **Fields** | Declared field count, which the parse independently confirms for all 223. |
| **Module** | Primary module from the taxonomy ([`../mindmap/taxonomy.md`](../mindmap/taxonomy.md)) — 14 in-scope modules plus `out-of-scope-cost-budget`. Every object has exactly one. **out-of-scope** marks the 27 Budget/Bid/Cost objects excluded by user decision on 2026-09-10. |
| **Spine** | Role relative to `ProjectEntity` ([`project-entity.md`](project-entity.md)): `supertype` (1), `subtype_root` (9, inherit the supertype column block on a shared key), `entity_scoped` (161, carry a `ProjectEntityID` FK), `firm_global` (52, outside the spine). |
| **In/Out** | In-degree = how many distinct objects hold a typed FK to this one. Out-degree = how many FK columns this object holds. |
| **Purpose** | One line. Unmarked lines are **Derived** — the leading sentence of that entity's explanation in [`../data-fields/INDEX.md`](../data-fields/INDEX.md), which is itself domain-inferred from field labels. Lines marked _(Inferred)_ are written here because the entity has no `INDEX.md` entry. |

## The catalog

| Object | Table(s) | Fields | Module | Spine | In/Out | Purpose |
|---|---|---:|---|---|---:|---|
| `AccrualTransaction` | `accrual_transaction` | 55 | accounting | entity_scoped | 0 / 5 | An individual expense-accrual posting tied to a contract, carrying up to eight parallel Account Number fields for GL split coding, matching the same allocation pattern seen in PaymentTransaction. |
| `AcctingAssumptionAdjust` | `accting_assumption_adjust` | 19 | accounting | entity_scoped | 0 / 3 | A manual adjustment to lease-accounting assumptions used in ASC 842/IFRS 16 calculations — adjustment percent and annual amount, letting an accountant override a calculated assumption. |
| `Allowance` | `allowance` | 23 | contracts-leases | entity_scoped | 1 / 5 | A tenant-improvement or other landlord allowance on a lease — allowance type/group classification and begin date. |
| `AllowanceTransaction` | `allowance_transaction` | 20 | contracts-leases | entity_scoped | 0 / 4 | An individual draw/payment transaction against an Allowance — due date and linkage back to the Allowance and Contract. |
| `AlternateRentSchedule` | `alternate_rent_schedule` | 25 | accounting | entity_scoped | 2 / 5 | An alternate/contingency rent calculation method available on a contract — alt rent math formula selection and begin date. |
| `Asset` | `asset` | 122 | assets-equipment | entity_scoped | 13 / 11 | The fixed-asset/ROU-asset record tied to a lease or equipment contract — accounting begin/end dates, discount rate overrides, depreciation dates, sale price, and current payment amounts. |
| `AssetHistory` | `asset_history` | 13 | assets-equipment | firm_global | 0 / 3 | A point-in-time snapshot of an Asset's financial state, letting the platform show what an asset's values were before a later recalculation. |
| `AuditColumn` | _(none)_ | 14 | platform-tenancy | entity_scoped | 0 / 2 | Metadata defining which columns on a table are tracked for audit history — accessor name and audit action per tracked field. |
| `AuditTable` | `audit_table` | 1 | platform-tenancy | entity_scoped | 0 / 1 | Header row of the audit log — names the table/entity a batch of `AuditColumn` change records belongs to. _(Inferred)_ |
| `BidPackage` | `bid_package` | 48 | **out-of-scope** | entity_scoped | 0 / 12 | The competitive-bid solicitation record for a capital project — ranked bidder results (1st Place Bidder Name/Amount, and by pattern 2nd/3rd)... |
| `BidPackageAlternate` | `bid_package_alternate` | 5 | **out-of-scope** | entity_scoped | 0 / 1 | An alternate (optional add/deduct) bid line offered within a BidPackage, with an accepted flag. |
| `BidPackageAlternateValue` | `bid_package_alternate_value` | 4 | **out-of-scope** | entity_scoped | 0 / 1 | The dollar value a bidder submitted for one BidPackageAlternate line. |
| `BidPackageBreakout` | _(none)_ | 4 | **out-of-scope** | entity_scoped | 0 / 1 | A cost breakout line item within a BidPackage tied to a specific budget line. |
| `BidPackageBreakoutValue` | `bid_package_breakout_value` | 6 | **out-of-scope** | entity_scoped | 0 / 1 | The dollar value a bidder submitted for one BidPackageBreakout line item. |
| `BidPackageTemplate` | `bid_package_template` | 32 | **out-of-scope** | entity_scoped | 1 / 6 | A reusable bid solicitation template — pre-assigns the page layouts used at each stage of a bid (Award, Invitation) and default budget view/... |
| `BidderIssue` | `bidder_issue` | 21 | **out-of-scope** | entity_scoped | 0 / 5 | One bidder's response to a BidPackage — conditioned bid amount and allow-conditioning flag, letting a bidder submit a qualified rather than ... |
| `BudgetColumn` | `budget_column` | 21 | **out-of-scope** | entity_scoped | 0 / 6 | One column within a capital project budget (e.g., 'Original Budget', 'Approved Change Orders') — status, type, and an 'Allow UI Edit?' flag,... |
| `BudgetColumnItemValue` | _(none)_ | 19 | **out-of-scope** | entity_scoped | 0 / 2 | The actual dollar value at the intersection of a BudgetLineItem and a BudgetColumn — the individual cell in the budget grid. |
| `BudgetColumnType` | `budget_column_type` | 31 | **out-of-scope** | firm_global | 8 / 4 | The template defining what a Budget Column represents (multi-select allowed, one-instance-only, editable) — configuration metadata one level... |
| `BudgetIndex` | `budget_index` | 6 | **out-of-scope** | firm_global | 1 / 1 | A named escalation index (e.g., a cost inflation index) applied to capital budgets, the header record for BudgetIndexValue. |
| `BudgetIndexValue` | `budget_index_value` | 8 | **out-of-scope** | entity_scoped | 0 / 4 | One escalation percentage within a BudgetIndex series, tied to a budget column type. |
| `BudgetLineGroup` | `budget_line_group` | 26 | **out-of-scope** | entity_scoped | 0 / 3 | Grouping level in the budget tree, above `BudgetLineItem`. _(Inferred)_ |
| `BudgetLineItem` | `budget_line_item` | 26 | **out-of-scope** | entity_scoped | 0 / 3 | One line item within a budget template — alert threshold, category code, and template linkage; the line-item layer beneath BudgetColumn/Budg... |
| `BudgetLineLeaf` | `budget_line_leaf` | 26 | **out-of-scope** | entity_scoped | 0 / 3 | Leaf-level budget row beneath `BudgetLineItem` — the finest cost-breakdown level. _(Inferred)_ |
| `BudgetOption` | `budget_option` | 13 | **out-of-scope** | entity_scoped | 0 / 4 | A selectable alternative version of a budget-column entity type. |
| `BudgetOptionTemplate` | _(none)_ | 107 | **out-of-scope** | subtype_root | 0 / 12 | Denormalised `ProjectEntity` x `BudgetTemplate` projection: carries ProjectEntity's whole inherited column block plus `BudgetTemplateID`. No physical table. _(Inferred)_ |
| `BudgetTemplate` | `budget_template` | 1 | **out-of-scope** | entity_scoped | 14 / 1 | Reusable budget structure applied to an entity; only `TemplateID` is exposed here, the body surfaces through `VirtualTemplateBudget`. _(Inferred)_ |
| `BudgetTemplateAudit` | `budget_template_audit` | 18 | **out-of-scope** | entity_scoped | 0 / 7 | Change history for budget-template application; shares the `BudgetEntityTemplateID`/`FolderEntityTemplateID`/`TaskEntityTemplateID` trio with the other `*TemplateAudit` tables. _(Inferred)_ |
| `BudgetView` | `budget_view` | 10 | **out-of-scope** | entity_scoped | 3 / 3 | A named saved view/filter over the budget grid. |
| `CLRExtensionPart` | `c_l_r_extension_part` | 24 | layouts-forms-reporting | entity_scoped | 0 / 5 | Extension part of a Custom List row (`ClientListRow`) holding the tenant-defined columns (docs/admin/006). _(Inferred)_ |
| `CPI` | `c_p_i` | 10 | accounting | entity_scoped | 0 / 3 | A recorded Consumer Price Index value at a point in time, tied to a Contract, feeding CPI-indexed rent escalation. |
| `ChangeOrder` | `change_order` | 16 | projects-capital | entity_scoped | 0 / 4 | A cost change against an active capital project — approved amount, sequence number, and cost-tracking-variance linkage back to CostTrackingTemplate. |
| `ClientListRow` | `client_list_row` | 24 | layouts-forms-reporting | entity_scoped | 0 / 5 | One row of a tenant-defined Custom List (docs/admin/006). _(Inferred)_ |
| `CoTenancy` | `co_tenancy` | 27 | contracts-leases | entity_scoped | 0 / 5 | A co-tenancy clause (rent reduction if an anchor tenant vacates) — anchor name, co-tenancy amount/area, and begin date, one of the seven Firm-editable Contract subgroups per 005. |
| `CodeASC842Schedule` | `code_a_s_c842_schedule` | 24 | accounting | firm_global | 0 / 0 | A reusable amortization-schedule template for ASC 842 reporting — 'Don't Amortize Asset Value' flag plus a large block of numbered GL Export Account slots for mapping schedule output to different ledger accounts. |
| `CodeAssetCategory` | `code_asset_category` | 6 | assets-equipment | firm_global | 0 / 0 | Master asset-category reference record — GL number and sub-account mapping for a category of equipment/assets. |
| `CodeBudgetColumnStatus` | `code_budget_column_status` | 3 | **out-of-scope** | firm_global | 0 / 0 | Master reference record for budget-column status values, including a locked flag. |
| `CodeExpenseType` | `code_expense_type` | 31 | accounting | firm_global | 0 / 1 | Master expense-category configuration — AP export account/tax numbers for up to several slots, defining how each expense type maps to the general ledger on export. |
| `CodeIFRS16Schedule` | `code_i_f_r_s16_schedule` | 24 | accounting | firm_global | 0 / 0 | The IFRS 16 counterpart to CodeASC842Schedule, structurally identical (same export-account slot pattern) but for the international standard. |
| `CodeIssueType` | `code_issue_type` | 19 | projects-capital | firm_global | 0 / 0 | Reference code list classifying issues/RFIs. _(Inferred)_ |
| `CodeProblem` | `code_problem` | 4 | projects-capital | firm_global | 0 / 0 | Master maintenance-problem-type reference record with a remedy note, linked to an asset category. |
| `CodeResponsibleParty` | `code_responsible_party` | 4 | projects-capital | firm_global | 0 / 0 | A single-field master value for the responsible-party code list used on Responsibility records. |
| `CodeSLSchedule` | `code_s_l_schedule` | 24 | accounting | firm_global | 0 / 0 | The pre-ASC-842/pre-IFRS-16 straight-line schedule template, structurally identical to the two standard-specific schedules — Lucernex evidently kept the legacy SL schedule type alongside both new-standard schedule types rather than replacing it. |
| `CodeSalesGroup` | `code_sales_group` | 3 | variable-rent | firm_global | 0 / 0 | A single-field master value letting one sales group alias to another for reporting rollups. |
| `CodeSalesType` | `code_sales_type` | 3 | variable-rent | firm_global | 0 / 0 | Master reference record for sales-type classification, with a flag to omit a type from sales-group totals. |
| `CommitteePackage` | `committee_package` | 1 | workflow | entity_scoped | 0 / 1 | A single-field stub representing a committee-review package record (see LinkCommPkgTemplDocContent). |
| `ComparisonItem` | `comparison_item` | 9 | portfolio-transactions | entity_scoped | 0 / 1 | One line in a competitive/market comparison analysis, with a computed value and expense-group total. |
| `ComparisonReport` | `comparison_report` | 4 | portfolio-transactions | entity_scoped | 0 / 1 | A saved competitive-comparison report with its own assigned page layout. |
| `Competitor` | `competitor` | 26 | facilities-locations | entity_scoped | 0 / 4 | A competing retailer/property tracked for market analysis — name, type, and building area unit, used in site-selection and demographic comparison work. |
| `Complex` | `complex` | 45 | facilities-locations | firm_global | 11 / 3 | A multi-building property complex/campus record sitting above Facility in the property hierarchy — complex-level classification and status fields plus a linked Person (likely site or leasing contact). |
| `Contract` | `contract_admin`, `contract_financial`, `contract_firm`, `contract_firm1` | 570 | contracts-leases | subtype_root | 61 / 18 | The lease/contract header record itself — the central entity the rest of the schema hangs off of. |
| `ContractAmendment` | `contract_amendment` | 20 | contracts-leases | entity_scoped | 13 / 3 | A formal amendment/modification to an executed lease — amendment group/number/type classification and base-amount change. |
| `ContractFinancialTest` | `contract_financial_test` | 93 | contracts-leases | entity_scoped | 0 / 7 | The ASC 842 / IFRS 16 lease-classification and present-value calculation record for a contract — initial asset and liability balances, PV of financial terms before and after adjustments, and the aggregate lease value under each standard. |
| `ContractTerm` | `contract_term` | 26 | contracts-leases | entity_scoped | 5 / 5 | One renewal/extension term option on a lease — average rent per area unit and area-unit basis, linked to Amendment and Covenant, appearing under both Contract and Wizard (the guided lease-entry flow). |
| `CostTrackingTemplate` | `cost_tracking_template` | 28 | **out-of-scope** | entity_scoped | 0 / 8 | A reusable cost-tracking configuration for capital projects — which budget column represents 'Approved Change Order' and how variance is cal... |
| `Covenant` | `covenant` | 44 | contracts-leases | entity_scoped | 15 / 6 | A lease covenant/compliance obligation (financial ratio tests, use restrictions, exclusivity clauses) tied to a Contract — covenant amount/area, category, and an associated document reference for the underlying clause. |
| `CustomCodeField` | `custom_code_field` | 13 | layouts-forms-reporting | firm_global | 0 / 3 | Meta-definition of a tenant-created custom code/dropdown field — the schema record behind Manage Custom Lists (see 006). |
| `DMA` | `d_m_a` | 7 | facilities-locations | firm_global | 10 / 1 | A Designated Market Area (a standard US media-market geography) reference record, used for site-selection demographic comparison. |
| `DemographicFact` | `demographic_fact` | 10 | facilities-locations | firm_global | 0 / 0 | One data point within a demographic report, with an ordering sequence for display. |
| `DemographicReport` | `demographic_report` | 10 | facilities-locations | firm_global | 0 / 3 | A demographic report definition tied to a market area, the report-level wrapper around DemographicResults/DemographicFact data. |
| `DemographicResults` | `demographic_results` | 12 | facilities-locations | entity_scoped | 0 / 2 | A saved demographic analysis output for a site — name, description, and an attached results document. |
| `DemographicStudyArea` | `demographic_study_area` | 6 | facilities-locations | firm_global | 0 / 0 | The trade-area definition used for a demographic study — radius in miles or drive time in minutes, an alternative to SiteSurvey's fixed 1/3/5-mile bands. |
| `DevelopmentPlan` | `development_plan` | 7 | portfolio-transactions | entity_scoped | 0 / 2 | A named development pipeline plan under RE Planner, the header record above DevelopmentSlot. |
| `DevelopmentSlot` | `development_slot` | 31 | portfolio-transactions | entity_scoped | 0 / 10 | A build-out slot within a development pipeline plan — assigned broker/project, current revenue weeks, and duration, feeding ProgramRevenueWeeks reporting. |
| `DiscountRate` | `discount_rate` | 16 | accounting | firm_global | 0 / 6 | A named discount-rate configuration (by country and accounting method) used in NPV/present-value calculations across ContractFinancialTest and ProFormaBudget. |
| `Document` | `document` | 23 | documents-folders | entity_scoped | 10 / 3 | The document/file metadata record used across the platform — author, checkout status (Checked Out By Member, Checked Out Date) for document locking during edits. |
| `DocumentMarkup` | `document_markup` | 1 | documents-folders | entity_scoped | 0 / 1 | Annotation/markup overlay stored against a `Document`. _(Inferred)_ |
| `EMailReceivedLog` | `e_mail_received_log` | 15 | documents-folders | entity_scoped | 1 / 3 | A logged inbound email tied to a record — arrival date and body, the source EMailReceivedLog rows LinkEMailReceivedLogDocument attaches Documents to. |
| `EMailSentLog` | `e_mail_sent_log` | 1 | documents-folders | entity_scoped | 0 / 1 | Outbound e-mail audit record. _(Inferred)_ |
| `Employer` | `employer` | 71 | people-parties | firm_global | 30 / 3 | The vendor/landlord/tenant company record — banking details (Bank Account Number, Bank Routing Number), AP vendor number, and document-access permission flags (Allow Employees Upload/Download access to Employer Documents). |
| `EmployerSite` | `employer_site` | 20 | people-parties | firm_global | 1 / 2 | A specific site/location belonging to an Employer (useful when a vendor has multiple branch offices) — business unit and currency type per site. |
| `EntityTemplate` | `entity_template` | 1 | platform-tenancy | entity_scoped | 4 / 1 | A single-field stub representing a reusable entity-setup template, referenced by TemplateAudit. |
| `EscalationIndex` | `escalation_index` | 12 | accounting | firm_global | 1 / 1 | A named index value series (e.g., a specific published CPI series) used to drive ExpenseEscalation calculations. |
| `ExchangeRate` | `exchange_rate` | 8 | platform-tenancy | firm_global | 0 / 1 | A currency exchange rate captured at a point in time for a Contract, supporting multi-currency financial calculations. |
| `ExpenseAccrualSchedule` | `expense_accrual_schedule` | 31 | accounting | entity_scoped | 1 / 4 | The generated period-by-period accrual schedule from an ExpenseAccrualSetup — accrual rate and annual amount per begin period/year. |
| `ExpenseAccrualSetup` | `expense_accrual_setup` | 31 | accounting | entity_scoped | 0 / 7 | The configuration for accruing an expense ahead of its billing (common for property tax and insurance accrued monthly against an annual bill) — accrual message, area-unit basis, and begin period. |
| `ExpenseAllocation` | `expense_allocation` | 15 | accounting | entity_scoped | 0 / 6 | Splits one recoverable expense across multiple contracts/entities by percentage — the allocation record for shared-building expenses. |
| `ExpenseEscalation` | `expense_escalation` | 28 | accounting | entity_scoped | 0 / 5 | An automatic escalation clause on a recoverable expense — base amount/year, cap amount/percentage, and begin date, distinct from CPI-indexed escalation (see the small CPI entity). |
| `ExpenseRecovery` | `expense_recovery_part1`, `expense_recovery_part2`, `expense_recovery_part3`, `expense_recovery_part4` | 565 | expense-recovery | entity_scoped | 0 / 6 | The CAM/OpEx recovery engine for a lease — one record per recoverable expense category (CAM, taxes, insurance, HVAC, etc.) per contract per year, carrying the base year, cap formula (percent or dollar, per-period or cumulative), pro rata share method, gross-up... |
| `ExpenseRecoveryItem` | `expense_recovery_item` | 47 | expense-recovery | entity_scoped | 0 / 4 | The line-item detail underneath ExpenseRecovery — one record per actual-vs-budget variance calculation (A-B, A-P, B-P Variance Amount/Percent), admin fee, and approved pro rata share, used during CAM reconciliation to compare what a tenant was billed against w... |
| `ExpenseRecoveryItemMapping` | `expense_recovery_item_mapping` | 6 | expense-recovery | entity_scoped | 0 / 3 | Maps an ExpenseRecoveryItem to an external invoice line item name and a JSON configuration blob, likely supporting invoice-import matching. |
| `ExpenseSchedule` | `expense_schedule` | 51 | accounting | entity_scoped | 0 / 6 | The recurring expense-billing schedule generated from an ExpenseSetup — per-period billed amounts, adjustment method and type (for escalating charges), and tax amount fields (Calculated Tax Amount #1-3+) for jurisdictions with multiple tax components. |
| `ExpenseSetup` | `expense_setup` | 96 | accounting | entity_scoped | 10 / 6 | The recurring-expense billing configuration for a contract (insurance, taxes, CAM billed directly rather than through recovery) — coverage period begin markers for every possible billing frequency (Annual, Q1-Q4, both Semi-Annual halves) so the same setup reco... |
| `ExpenseVendorAllocation` | `expense_vendor_allocation` | 16 | accounting | entity_scoped | 0 / 6 | Allocation of a recoverable expense to a specific paying vendor — AP vendor number and begin/end date. |
| `Facility` | `facility` | 133 | facilities-locations | subtype_root | 7 / 13 | The physical property/building record — address fields (Street Address #1-3, City, State, Postal Code, Jurisdiction) plus facility-level dates and area figures. |
| `FacilityExpense` | `facility_expense` | 22 | facilities-locations | entity_scoped | 0 / 6 | A non-recovered operating expense tracked directly against a Facility rather than through a Contract's ExpenseRecovery — actual vs. |
| `FinancialAdjustment` | `financial_adjustment` | 19 | accounting | entity_scoped | 0 / 6 | A manual dollar adjustment to an Asset's or Contract's financial position — accounting adjustment type and amount. |
| `Firm` | `firm` | 18 | platform-tenancy | firm_global | 0 / 1 | The tenant-company configuration record — one row per Lucernex client firm, holding default page-layout assignments per module (Facility Setup Page, Equipment Contract Setup Page) and default folder security. |
| `FiscalPeriod` | `fiscal_period` | 17 | accounting | entity_scoped | 0 / 3 | The fiscal calendar definition — begin/end date and days-in-period per named fiscal period, the calendar backbone that SLPeriod, ExpenseSchedule, and Sales fiscal-period fields reference. |
| `Folder` | `folder` | 16 | documents-folders | entity_scoped | 7 / 2 | A document-management folder — downloadable flag and folder-template linkage, the container Document records live in. |
| `FolderSecurity` | `folder_security` | 3 | documents-folders | firm_global | 0 / 0 | Per-folder access-control entry. _(Inferred)_ |
| `FolderTemplate` | `folder_template` | 1 | documents-folders | entity_scoped | 0 / 1 | Reusable folder-tree structure applied to an entity; body surfaces through `VirtualTemplateFolder`. _(Inferred)_ |
| `FolderTemplateAudit` | `folder_template_audit` | 18 | documents-folders | entity_scoped | 0 / 7 | Change history for folder-template application. _(Inferred)_ |
| `GlobalProperty` | `global_property` | 4 | platform-tenancy | firm_global | 0 / 1 | A generic firm-scoped key/value configuration setting, organized by property section — a low-level settings-store table. |
| `HolidayDate` | `holiday_date` | 12 | projects-capital | firm_global | 0 / 2 | One calendar date within a HolidaySchedule. |
| `HolidaySchedule` | `holiday_schedule` | 8 | projects-capital | firm_global | 0 / 2 | A named calendar of holidays (the header record for HolidayDate), used in schedule/task date calculations. |
| `Insurance` | `insurance` | 27 | contracts-leases | entity_scoped | 0 / 5 | Required insurance coverage terms on a lease — certificate received/request dates, required flag, and whether the agent is also the named insured. |
| `InvoiceIssue` | `invoice_issue` | 23 | accounting | entity_scoped | 0 / 3 | An invoice batch header for accounts-payable processing — batch date/number and currency type, anchoring InvoiceItem as line-level detail. |
| `InvoiceItem` | `invoice_item` | 18 | accounting | entity_scoped | 0 / 3 | Line-item detail under an InvoiceIssue batch — GL number and invoice amount per line. |
| `Issue` | `issue` | 56 | projects-capital | entity_scoped | 0 / 14 | A bid-package issue/question thread header — date range and type, the object Question and IssueResponse attach to. |
| `IssueResponse` | `issue_response` | 11 | projects-capital | entity_scoped | 0 / 3 | A reply/answer posted against a bidder Issue (Q&A) during a bid process. |
| `IssueSubmittal` | `issue_submittal` | 1 | projects-capital | entity_scoped | 0 / 1 | Submittal record attached to an `Issue`. _(Inferred)_ |
| `Jurisdiction` | `jurisdiction` | 11 | platform-tenancy | firm_global | 16 / 3 | A tax/legal jurisdiction reference record, referenced by Facility, Parcel, and Location address blocks. |
| `KeyDate` | `key_date` | 39 | contracts-leases | entity_scoped | 0 / 5 | A tracked deadline/notice date tied to a Contract, Contract Term, or Covenant — action date/period (with a configurable period unit: days, months, etc.), earliest notice date, and coverage period bounds, used to drive renewal, termination, and compliance-notic... |
| `LandPurchaseSummary` | `land_purchase_summary` | 35 | facilities-locations | entity_scoped | 0 / 2 | The land-acquisition deal record for ground purchases — asking price, acreage, and commencement date, anchoring the Purchase Management group alongside Ownership and DevelopmentPlan. |
| `LandlordInvoice` | `landlord_invoice` | 31 | accounting | entity_scoped | 0 / 7 | An invoice received from a landlord for billing outside the standard recovery/rent cycle — coverage period and allocation-status amounts, anchoring LandlordInvoiceItem as its line-item detail. |
| `LandlordInvoiceItem` | `landlord_invoice_item` | 28 | accounting | entity_scoped | 0 / 4 | Line-item detail under a LandlordInvoice — allocated vs. |
| `LeaseAudit` | `lease_audit` | 1 | contracts-leases | entity_scoped | 0 / 1 | A single-field audit-trail stub for lease-level changes; likely a placeholder or minimally-used table relative to the richer Contract audit trail. |
| `LeaseInfo` | `lease_info` | 219 | contracts-leases | entity_scoped | 0 / 2 | A negotiation-history snapshot living under the Pro Forma Lease group — it captures the same handful of deal terms (abatement, rent, TI allowance) at multiple negotiation checkpoints (Broker Recommended, Landlord Asking, Final Terms), each as its own field tri... |
| `LinkBudgetIndexBLI` | `link_budget_index_b_l_i` | 1 | **out-of-scope** | entity_scoped | 0 / 1 | Join table associating a BudgetLineItem with a BudgetIndex escalator — a single internal RecID field only. |
| `LinkBudgetViewBLI` | `link_budget_view_b_l_i` | 1 | **out-of-scope** | entity_scoped | 0 / 1 | Join table associating a BudgetLineItem with a BudgetView. |
| `LinkEMailReceivedLogDocument` | `link_e_mail_received_log_document` | 5 | documents-folders | entity_scoped | 0 / 3 | Join table linking a received email log entry to a saved Document (e.g., an email attachment filed to the record). |
| `LinkIssuePart` | `link_issue_part` | 13 | projects-capital | entity_scoped | 0 / 3 | Join between an `Issue` and a `Part`. _(Inferred)_ |
| `LinkIssuePartOrder` | `link_issue_part_order` | 16 | projects-capital | entity_scoped | 0 / 3 | Join between an issue's part requirement and its ordering/procurement record. _(Inferred)_ |
| `LinkLandPurchaseInspection` | `link_land_purchase_inspection` | 8 | facilities-locations | entity_scoped | 0 / 2 | Join table linking a LandPurchaseSummary to a due-diligence inspection — type, duration, and scheduled date. |
| `LinkLandlordInvPaymentTxn` | `link_landlord_inv_payment_txn` | 13 | accounting | entity_scoped | 0 / 4 | Join table linking a LandlordInvoiceItem to the PaymentTransaction that paid it — allocation amount and date. |
| `LinkMemberProjectEntity` | `link_member_project_entity` | 7 | platform-tenancy | entity_scoped | 0 / 3 | A join record linking an internal Member to a ProjectEntity in an org-chart role — manager name/title and job function, despite the Link-style name it carries enough project-team detail (24 fields) to warrant standalone treatment. |
| `LinkPEMemberCodeJobTitle` | `link_p_e_member_code_job_title` | 1 | platform-tenancy | entity_scoped | 0 / 1 | Join table linking a ProjectEntity member assignment to a job-title code — internal ID-only fields with no exposed labels. |
| `LinkProjectEntityContact` | `link_project_entity_contact` | 12 | people-parties | entity_scoped | 0 / 4 | Join table linking a ProjectEntity to a contact person with a contact-type classification. |
| `LinkProjectEntityVendor` | `link_project_entity_vendor` | 4 | people-parties | entity_scoped | 0 / 2 | Join table linking a ProjectEntity (portfolio) to an approved Vendor. |
| `LinkReTransScenContact` | `link_re_trans_scen_contact` | 33 | portfolio-transactions | entity_scoped | 0 / 8 | A join record linking a real-estate transaction Scenario to a contact (broker, attorney) with contact-type classification and email. |
| `LinkReceiptTransaction` | `link_receipt_transaction` | 12 | accounting | entity_scoped | 0 / 5 | Join table linking a PaymentReceipt to the transaction(s) it was allocated against. |
| `LinkRegionManager` | `link_region_manager` | 1 | platform-tenancy | entity_scoped | 0 / 1 | Join table assigning a Member as manager of a Region, with a manager flag and operating-status inheritance. |
| `LinkSchedOffsetExpGrpType` | `link_sched_offset_exp_grp_type` | 12 | accounting | entity_scoped | 0 / 4 | Join table linking a ScheduledOffset to the expense group/type it applies to. |
| `LinkTaskByCodeMember` | `link_task_by_code_member` | 8 | projects-capital | entity_scoped | 0 / 3 | Join table assigning a Task to a Member by job title/org-chart level rather than by name. |
| `LinkTaskDocument` | `link_task_document` | 1 | projects-capital | entity_scoped | 0 / 1 | Join attaching a `Document` to a `Task`. _(Inferred)_ |
| `LinkTaskMember` | `link_task_member` | 5 | projects-capital | entity_scoped | 0 / 4 | Join table assigning a specific Member to a specific Task on a ProjectEntity. |
| `Location` | `location` | 141 | facilities-locations | subtype_root | 9 / 13 | A general site/location record — address and geocoding fields (Latitude, Longitude) plus percentage-based site metrics — used as a lighter-weight alternative to Facility for sites that are tracked before or without a full facility record. |
| `MapClientSchedule` | `map_client_schedule` | 10 | platform-tenancy | entity_scoped | 0 / 3 | Links a RETransaction/schedule to auto-push forecast behavior and percent-complete tracking. |
| `Member` | `member` | 81 | people-parties | firm_global | 161 / 6 | The internal user/employee account record for Lucernex itself (not a lease party) — login and access-control fields (Accept EULA?, Always Spell Check?, Color Scheme) alongside org fields (Code Job Function, Code Analytics Role) and billing rates. |
| `MemberAudit` | `member_audit` | 12 | people-parties | entity_scoped | 0 / 4 | Login/session audit trail for internal Members — action name, audit date, and impersonation tracking for support access. |
| `NonMember` | `non_member` | 37 | people-parties | firm_global | 0 / 4 | External, non-licensed user record — a portal/vendor login that is not a `Member`. _(Inferred)_ |
| `Notify` | `notify` | 1 | platform-tenancy | entity_scoped | 0 / 1 | A single-field stub representing an individual fired notification instance. |
| `Organization` | `organization` | 17 | platform-tenancy | firm_global | 8 / 1 | A broader organizational entity (parent company, franchise group) above Employer — up to several numbered Account Number slots mirroring the financial entities' split-coding pattern. |
| `Ownership` | `ownership` | 9 | facilities-locations | entity_scoped | 0 / 2 | Records a funding/ownership percentage and type for an entity in a land purchase, supporting multi-party purchases. |
| `Parcel` | `parcel` | 154 | facilities-locations | subtype_root | 7 / 18 | The land-parcel record, distinct from Facility (building) and Location (site) — address fields plus parcel-specific attributes like Demographic DMA linkage, used primarily for ground-lease and land-purchase scenarios and as the anchor for the large PropertyTax... |
| `ParcelAccess` | `parcel_access` | 20 | facilities-locations | entity_scoped | 0 / 5 | An access easement or right-of-way record on a Parcel — effective/expire date and associated document. |
| `Parking` | `parking` | 19 | facilities-locations | entity_scoped | 0 / 4 | Parking-facility detail under a Facility record — currency type and description for parking-related costs/revenue. |
| `Part` | `part` | 16 | assets-equipment | firm_global | 0 / 2 | An equipment/maintenance parts-catalog record — cost, manufacturer, and model number, supporting the Equipment/Assets maintenance workflow. |
| `PartPackage` | `part_package` | 6 | assets-equipment | firm_global | 0 / 2 | A named kit/bundle of parts, the header record above PartPackageItem. |
| `PartPackageItem` | `part_package_item` | 7 | assets-equipment | firm_global | 0 / 1 | One part within a PartPackage kit. |
| `Party` | `party` | 12 | people-parties | entity_scoped | 0 / 4 | A generic company/contact reference tied to a Contract, used where the role doesn't fit Employer or Person specifically. |
| `PayApp` | `pay_app` | 15 | accounting | entity_scoped | 0 / 4 | An AIA-style payment application against a construction contract — invoice retainage and cost-tracking variance. |
| `PaymentReceipt` | `payment_receipt` | 21 | accounting | entity_scoped | 1 / 3 | Money received from a tenant/payer (the inverse of PaymentTransaction) — allocated/unallocated amount and bank account/routing number for the depositing account. |
| `PaymentTransaction` | `payment_transaction` | 118 | accounting | entity_scoped | 3 / 13 | Individual rent/expense payment or receipt records against a contract — up to eight parallel 'Account Number #N' fields for split GL coding, allocation amounts, and payment dates. |
| `PaymentTransactionFullImport` | _(none)_ | 118 | accounting | entity_scoped | 0 / 13 | Import/integration projection of `PaymentTransaction` (identical 118-field shape, no physical table). _(Inferred)_ |
| `PercentageRent` | `percentage_rent` | 45 | variable-rent | entity_scoped | 2 / 5 | The percentage/sales-based rent clause on a retail lease — cap amount/frequency, audit-right flag, and billing frequency, linked to Covenant for cross-referencing compliance obligations tied to the same clause. |
| `PercentageRentBreakpoint` | `percentage_rent_breakpoint` | 40 | variable-rent | entity_scoped | 0 / 4 | The natural-breakpoint configuration for a percentage-rent clause — up to eight numbered Breakpoint Amount/Count slots defining the sales tiers at which the percentage rate changes. |
| `Person` | `person` | 37 | people-parties | firm_global | 0 / 4 | An individual contact record (broker, attorney, property manager) distinct from Employer (the company) and Member (internal user) — billing rates, multiple email/phone slots, and job-title code linkage. |
| `PotentialProject` | `potential_project` | 108 | portfolio-transactions | subtype_root | 0 / 13 | A candidate site or deal before it becomes a project — a ProjectEntity subtype root. _(Inferred)_ |
| `ProFormaBudget` | `pro_forma_budget` | 47 | **out-of-scope** | entity_scoped | 0 / 2 | The financial feasibility analysis for a prospective deal or capital project — IRR, NPV, and Payback Period alongside a Finance Committee Ap... |
| `ProcessTimeline` | `process_timeline` | 31 | projects-capital | entity_scoped | 0 / 3 | A generic milestone/phase timeline attached to a Location or ProjectEntity — actual vs. |
| `ProcessTimelineTemplate` | `process_timeline_template` | 10 | projects-capital | firm_global | 0 / 1 | A reusable milestone/phase template that ProcessTimeline instances are created from, with default phase-status labels. |
| `Program` | `program` | 180 | portfolio-transactions | subtype_root | 11 / 13 | A capital/rollout program header — the container above ProjectEntity for a slate of related capital projects, carrying its own page-layout assignments (Cap Project Setup Page Layout, Cap Project Map Setup Layout) and exchange-rate-type overrides per cost categ... |
| `ProgramRevenueWeeks` | `program_revenue_weeks` | 13 | portfolio-transactions | entity_scoped | 0 / 2 | Weekly revenue-target tracking (filled/unfilled targets and weeks) for a development Program, feeding DevelopmentSlot planning. |
| `Project` | `project` | 111 | platform-tenancy | subtype_root | 0 / 14 | A lightweight project identity record (ID, RecID, UUID) distinct from the richer ProjectEntity, likely used for cross-system reference linking. |
| `ProjectEntity` | `project_entity` | 107 | platform-tenancy | supertype | 161 / 12 | The generic 'project' record used for capital projects, store rollouts, and portfolio initiatives — distinct from Contract, it tracks phase-gate status (Design, Construction, Possession, Operations) via parallel status/date pairs and milestone pointers, plus `... |
| `PropertyTaxAppeal` | `property_tax_appeal` | 41 | property-tax | entity_scoped | 1 / 5 | A property-tax assessment appeal filed against a Parcel — filing date, appraisal fee, attorney fee, and the resulting assessment reduction, anchoring a sub-family (PropertyTaxAppealAward) for tracking the appeal's financial outcome. |
| `PropertyTaxAppealAward` | `property_tax_appeal_award` | 18 | property-tax | entity_scoped | 0 / 6 | The financial outcome of a PropertyTaxAppeal — actual/estimated award date and award/award-fee amount. |
| `PropertyTaxAssessment` | `property_tax_assessment` | 25 | property-tax | entity_scoped | 2 / 6 | The underlying assessed value detail for a Parcel — land, improvements, and adjustment components of the total assessment, feeding PropertyTaxBill and PropertyTaxSummary. |
| `PropertyTaxBill` | `property_tax_bill` | 32 | property-tax | entity_scoped | 3 / 5 | A property tax bill issued against a Parcel — discount amount/date/rate for early-payment discounts, feeding into PropertyTaxSummary. |
| `PropertyTaxDetail` | `property_tax_detail` | 15 | property-tax | entity_scoped | 0 / 5 | Free-form notes detail attached to a Parcel's property tax record. |
| `PropertyTaxSummary` | `property_tax_summary` | 32 | property-tax | entity_scoped | 1 / 6 | The rollup of assessment amount/percent and billing frequency for a Parcel's property tax obligation across bills and appeals. |
| `Prototype` | `prototype` | 113 | facilities-locations | subtype_root | 11 / 12 | A standardized store/facility design template used for rollout programs — approved flag, average project cost/duration, and default construction type/distribution center. |
| `PurchaseOrder` | `purchase_order` | 20 | accounting | entity_scoped | 2 / 3 | A capital-project purchase order — approved change order amount and estimate amount, tied into the ChangeOrder/CostTrackingTemplate variance-tracking chain. |
| `Question` | `question` | 14 | layouts-forms-reporting | entity_scoped | 0 / 3 | A question posted during a bid Q&A process, with published/private visibility flags — the counterpart IssueResponse replies to. |
| `RETransaction` | `r_e_transaction` | 31 | portfolio-transactions | entity_scoped | 3 / 14 | The formal real-estate transaction record once a Scenario converts into an active deal — approved capital budget, deal schedule, and begin date. |
| `ReTransScenContact` | `re_trans_scen_contact` | 28 | portfolio-transactions | firm_global | 1 / 4 | Contact record specific to a real-estate transaction scenario (distinct from LinkReTransScenContact, the join-style variant) — contact type, employer name, email. |
| `RecalcOverrideNotes` | `recalc_override_notes` | 7 | accounting | entity_scoped | 1 / 4 | A free-text note explaining why a financial recalculation was manually overridden — an audit-style justification field. |
| `Region` | `region` | 1 | platform-tenancy | entity_scoped | 12 / 1 | A geographic region in the portfolio hierarchy — parent/previous region linkage and operating status, referenced by LinkRegionManager and LinkRegionMarket. |
| `ReportGroupAvailableField` | `report_group_available_field` | 27 | layouts-forms-reporting | firm_global | 4 / 0 | Metadata about the Data Fields catalog itself — API table name, dropdown table name, field type and definition — meaning this entity is Lucernex describing its own field-metadata system, the same system this documentation set is built from. |
| `ReportGroupData` | `report_group_data` | 5 | layouts-forms-reporting | firm_global | 0 / 0 | Platform metadata for a top-level or subgroup node in this very Data Fields hierarchy — parent group name and firm scoping. |
| `Responsibility` | `responsibility` | 32 | contracts-leases | entity_scoped | 0 / 5 | Defines which party (landlord/tenant) is responsible for a cost category on a lease, with cap amount/percent limits — the allocation-of-obligation record that ExpenseRecovery and FinancialAdjustment calculations reference. |
| `SLPeriod` | `s_l_period` | 79 | accounting | entity_scoped | 0 / 6 | Period-level straight-line rent detail underlying SLSummary — one record per accounting period per contract carrying asset/liability balance, amortization expense, and both the current-currency and '- Translated' value pair for every monetary field, plus 12-Mo... |
| `SLSummary` | `s_l_summary` | 134 | accounting | entity_scoped | 2 / 8 | Straight-line rent summary — one record per contract holding forward-looking cash and interest expense projected out fiscal-year by fiscal-year (Current, Beyond Fifth, Beyond Sixth) and quarter by quarter within the current year, used for ASC 842/IFRS 16 discl... |
| `Sales` | `sales` | 28 | variable-rent | entity_scoped | 0 / 3 | Reported retail sales figures for a location, feeding percentage-rent calculations — currency type, fiscal period/year, and a client-assigned sales ID for reconciling against a tenant's own sales report. |
| `SalesExclusion` | `sales_exclusion` | 19 | variable-rent | entity_scoped | 0 / 5 | An individual excluded sales category feeding into a SalesExclusionCap total. |
| `SalesExclusionCap` | `sales_exclusion_cap` | 23 | variable-rent | entity_scoped | 1 / 4 | A cap limiting how much sales can be excluded from percentage-rent calculation (e.g., online/catalog sales exclusions) — cap amount/percent and begin date. |
| `Scenario` | `scenario` | 69 | portfolio-transactions | entity_scoped | 3 / 10 | A deal/transaction scenario under RE Transaction — comparative what-if terms (Broker Commission, Capital Required, Annual Total Rent) for a prospective site or renewal being evaluated before commitment, plus site demographic fields (Average HH Income, Block) i... |
| `ScheduledOffset` | `scheduled_offset` | 19 | accounting | entity_scoped | 0 / 5 | A pre-scheduled (as opposed to variable) rent offset — cap amount per month/percent and allocation tracking. |
| `ScratchPad` | `scratch_pad` | 1 | platform-tenancy | entity_scoped | 0 / 1 | Free-form scratch-note store. _(Inferred)_ |
| `Security` | _(none)_ | 21 | platform-tenancy | firm_global | 0 / 3 | Computed effective-permission projection over user class, page layout, report group and dashboard component. No physical table. _(Inferred)_ |
| `SecurityDeposit` | `security_deposit` | 25 | contracts-leases | entity_scoped | 0 / 6 | Security/damage deposit tracking on a lease — deposit amount, account number, and Covenant linkage for deposits tied to compliance conditions. |
| `ServiceRequest` | `service_request` | 30 | assets-equipment | entity_scoped | 0 / 4 | A facilities service/maintenance ticket tied to an Asset or Contract — approval date/party, asset group/type, anchoring WorkOrder as the dispatched work resulting from the request. |
| `SiteSurvey` | `site_survey` | 79 | facilities-locations | entity_scoped | 0 / 2 | Site-selection/demographic evaluation data for a candidate location — household income and count at 1/3/5-mile radii, median age, and condition-code ratings, used during real estate site selection before a lease is signed. |
| `Space` | `space` | 27 | facilities-locations | entity_scoped | 1 / 5 | A leasable space/suite record within a Facility — area unit and Contract linkage, more granular than Facility itself for multi-tenant buildings. |
| `StateProvinceCountry` | `state_province_country` | 11 | platform-tenancy | firm_global | 22 / 1 | Master geography reference with ISO Alpha-2/3 country codes, backing every address field across Facility, Location, and Parcel. |
| `Task` | `task` | 37 | projects-capital | entity_scoped | 0 / 5 | A schedule/project task record — baseline vs. |
| `TaskGroup` | `task_group` | 37 | projects-capital | entity_scoped | 11 / 5 | Grouping node in the task/schedule tree, above `TaskItem`. _(Inferred)_ |
| `TaskItem` | `task_item` | 37 | projects-capital | entity_scoped | 0 / 5 | Leaf task row within a `TaskGroup`. _(Inferred)_ |
| `TaskPredecessor` | `task_predecessor` | 15 | projects-capital | entity_scoped | 0 / 5 | Defines a dependency between two Task records, with actual lead/lag days — the scheduling-network edge beneath Task. |
| `TaskTemplate` | `task_template` | 1 | projects-capital | entity_scoped | 1 / 1 | Reusable schedule structure applied to an entity; body surfaces through `VirtualTemplateSchedule`. _(Inferred)_ |
| `TaskTemplateAudit` | `task_template_audit` | 18 | projects-capital | entity_scoped | 0 / 7 | Change history for task/schedule-template application. _(Inferred)_ |
| `TemplateAudit` | `template_audit` | 18 | platform-tenancy | entity_scoped | 0 / 7 | An audit trail of when a BudgetTemplate/EntityTemplate/FolderTemplate was applied to a new project — applied date and whether folder structure was copied. |
| `Tenant` | `tenant` | 42 | facilities-locations | entity_scoped | 0 / 8 | The sub-tenant/occupant record under a Facility (for landlords or sub-lease scenarios) — headcount capacity fields (Capacity #1-4, calcTotalHeadcount) and a Contract linkage. |
| `Usage` | `usage` | 14 | variable-rent | entity_scoped | 0 / 3 | A recorded consumption/usage reading against a contract on a given posting date, feeding usage-based rent calculations. |
| `UseBasedRent` | `use_based_rent` | 23 | variable-rent | entity_scoped | 0 / 5 | The usage-based rent clause header (e.g., per-unit, per-transaction rent) — billing frequency and currency type, the clause-level record UseBasedRentBreakpoint and VirtualUseBasedRentPeriod project from. |
| `UseBasedRentBreakpoint` | `use_based_rent_breakpoint` | 31 | variable-rent | entity_scoped | 0 / 4 | The tiered-cost-per-unit configuration for usage-based rent, mirroring PercentageRentBreakpoint's structure but keyed to consumption cost rather than sales. |
| `UserClassSecurity` | `user_class_security` | 21 | platform-tenancy | firm_global | 0 / 3 | A named security role/permission class — dashboard component visibility and group hierarchy, referenced by WorkFlowTemplateStep's 'Assignee User Class List' fields. |
| `VariableRentOffset` | `variable_rent_offset` | 20 | accounting | entity_scoped | 0 / 3 | A rent offset tied to a variable expense group/type (rent that adjusts based on a specific expense category rather than CPI or sales). |
| `VendorInsurance` | `vendor_insurance` | 15 | people-parties | firm_global | 0 / 3 | The actual insurance policy detail for a vendor/employer (as opposed to Insurance, which is the lease's required-coverage terms) — aggregate occurrence amount and policy type/dates. |
| `VirtualExpAccrualForecastPeriod` | `virtual_exp_accrual_forecast_period` | 13 | accounting | firm_global | 0 / 2 | A computed forward forecast of an expense accrual by period, referencing the ExpenseAccrualSchedule/Setup it projects from. |
| `VirtualExpenseForecastPeriod` | `virtual_expense_forecast_period` | 20 | accounting | firm_global | 0 / 2 | A forward-looking forecast of recoverable expense by calendar month/year and expense category, computed rather than stored. |
| `VirtualPRAccrualPeriod` | `virtual_pr_accrual_period` | 20 | variable-rent | entity_scoped | 0 / 2 | The computed period projection of percentage-rent accrual, showing this-period, prior-periods, and total accrual amounts. |
| `VirtualPRPAggregate` | `virtual_p_r_p_aggregate` | 16 | variable-rent | entity_scoped | 0 / 2 | An aggregated percentage-rent obligation projection across a contract's full term — current offset amount and current percentage rent obligation/paid. |
| `VirtualPercentageRentPeriod` | `virtual_percentage_rent_period` | 38 | variable-rent | entity_scoped | 0 / 2 | The computed period-by-period projection of PercentageRentBreakpoint tiers, following the same Virtual-entity pattern as VirtualSalesPeriod. |
| `VirtualSalesPeriod` | _(none)_ | 66 | variable-rent | firm_global | 0 / 1 | A computed (non-stored, 'Virtual') period record projecting percentage-rent breakpoints and sales-based rent obligations forward — up to eight numbered Breakpoint Amount/Rate slots per period. |
| `VirtualTemplateBudget` | `virtual_template_budget` | 17 | **out-of-scope** | entity_scoped | 0 / 1 | Near-identical structure to VirtualTemplateBudgetOption; the two likely back two different UI pickers (a single-select field vs. |
| `VirtualTemplateBudgetOption` | `virtual_template_budget_option` | 17 | **out-of-scope** | entity_scoped | 0 / 1 | Read-only projection of a budget template's metadata (name, description, notes, and Cap Program/Cap Project applicability flags) surfaced fo... |
| `VirtualTemplateFolder` | `virtual_template_folder` | 16 | documents-folders | entity_scoped | 0 / 1 | Read-only projection of FolderTemplate metadata (name, description, Cap Program/Cap Project applicability), the folder-template counterpart to VirtualTemplateBudget. |
| `VirtualTemplateSchedule` | `virtual_template_schedule` | 16 | projects-capital | entity_scoped | 0 / 1 | Read-only projection of a schedule-template's metadata, completing the Virtual*Template trio alongside VirtualTemplateBudget and VirtualTemplateFolder. |
| `VirtualUBRPAggregate` | `virtual_u_b_r_p_aggregate` | 14 | variable-rent | entity_scoped | 0 / 2 | An aggregated projection of use-based-rent obligation across a contract term, the use-based-rent counterpart to VirtualPRPAggregate. |
| `VirtualUsagePeriod` | `virtual_usage_period` | 66 | variable-rent | firm_global | 0 / 1 | The usage-based-rent counterpart to VirtualSalesPeriod — projects breakpoint cost tiers (with 6-decimal-precision `NUMBER_FRACTION6DIGITS` fields for unit-cost rates) period by period for contracts billed on usage/consumption rather than sales volume. |
| `VirtualUseBasedRentPeriod` | `virtual_use_based_rent_period` | 23 | variable-rent | entity_scoped | 0 / 2 | The computed period projection of UseBasedRentBreakpoint tiers, following the same Virtual-entity calculation pattern. |
| `WFStepFullImport` | `w_f_step_full_import` | 47 | workflow | entity_scoped | 0 / 11 | Import/integration projection of `WorkFlowStep` (identical 47-field shape). _(Inferred)_ |
| `WorkFlow` | `work_flow` | 19 | workflow | entity_scoped | 4 / 6 | The active workflow instance running against a real trigger object (Trigger CodeSQLTable, Trigger Object) — the runtime record one level above WorkFlowStep. |
| `WorkFlowStep` | `work_flow_step` | 47 | workflow | entity_scoped | 4 / 11 | The runtime instance of one workflow step executing against a real record — computed alert/warn/due dates for approvers and assignees, checkout tracking (CheckedOutByMemberID), and a pointer back to the WorkFlowTemplateStep it was instantiated from. |
| `WorkFlowStepApprover` | `work_flow_step_approver` | 20 | workflow | entity_scoped | 1 / 7 | One named approver's action on a running WorkFlowStep — action comment, action taken, and has-approved flag, the audit trail of an individual approval decision. |
| `WorkFlowStepAssignee` | `work_flow_step_assignee` | 11 | workflow | entity_scoped | 0 / 5 | One assignee's notification/acknowledgment status on a running WorkFlowStep, parallel to WorkFlowStepApprover for the assignee (rather than approver) role. |
| `WorkFlowTemplate` | `work_flow_template` | 25 | workflow | firm_global | 0 / 2 | The top-level workflow definition (the container for WorkFlowTemplateStep records) — active layout, associated task, and auto-assignment rules for the initiator. |
| `WorkFlowTemplateStep` | `work_flow_template_step` | 55 | workflow | firm_global | 0 / 11 | One approval step within a reusable workflow template — approver/assignee configuration exposed as four parallel list-type fields per role (Approver Job Title List, Approver Member List, Approver Type, Approver User Class List) so a single step can route to a ... |
| `WorkFlowTemplateStepAction` | `work_flow_template_step_action` | 37 | workflow | entity_scoped | 1 / 5 | The button/action definition available at a workflow template step (Approve, Reject, Send Back) — Boolean flags controlling what the action does to the workflow (Should Close Work Flow?, Should Move to Next Step, Should Restart the Step?) plus finance-specific... |
| `WorkOrder` | `work_order` | 30 | assets-equipment | entity_scoped | 0 / 7 | The dispatched maintenance work order resulting from a ServiceRequest — actual completion date, cost, labor hours, and vendor assignment. |
## Objects worth a second look

| Object | Why |
|---|---|
| `Contract` | 570 fields across `contract_admin`, `contract_financial`, `contract_firm`, `contract_firm1`. **258 of the 570 are `Firm_`-prefixed tenant-custom columns** — 45% of the largest object in the product is one tenant's customisation, physically merged into the core table. |
| `ExpenseRecovery` | 565 fields across `expense_recovery_part1..part4`, with `ExpenseRecoveryID` and `ModifiedDate` repeated **once per part**. Purely mechanical column-overflow partitioning, no semantics in the split. |
| `LeaseInfo` | 219 fields, in-degree 0, and only **two** FK columns out. A wide, almost edgeless read-model of the lease — a reporting projection rather than a transactional table. |
| `PaymentTransactionFullImport` / `WFStepFullImport` | Field-for-field the same size as `PaymentTransaction` (118) and `WorkFlowStep` (47). Import/integration projections of their base object. `PaymentTransactionFullImport` names no physical table. |
| `BudgetOptionTemplate` | Out of scope, but structurally relevant: 107 fields, no physical table, and it carries `ProjectEntity`'s entire inherited column block. Classified `subtype_root` by column signature — a false positive of that test, which matters for [`project-entity.md`](project-entity.md) §2. |
| The 13 `Virtual*` objects | None has a primary key. None has a single audit column. See [`foreign-key-graph.md`](foreign-key-graph.md#5-the-virtual-family--computed-projections-not-tables). |
| `Region` | **1 field declared**, yet 12 distinct objects point at it across 34 columns (`RegionID`, `RootRegionID`, `SubRegionID` on the same rows) — one of the most-referenced objects in the product, from a table the export barely describes. |
| `AuditTable`, `BudgetTemplate`, `CommitteePackage`, `DocumentMarkup`, `EMailSentLog`, `EntityTemplate`, `FolderTemplate`, `IssueSubmittal`, `LeaseAudit`, `LinkBudgetIndexBLI`, `LinkBudgetViewBLI`, `LinkPEMemberCodeJobTitle`, `LinkRegionManager`, `LinkTaskDocument`, `Notify`, `Region`, `ScratchPad`, `TaskTemplate` | Declared with **1 field**. Either the export truncates them, or they are pure key-only join/marker tables. Unresolved — see Open questions. |

## Tables in the platform picker but not in this catalogue

**Derived, 2026-09-13.** This catalogue derives from `ShowObjectDetails.jsp`, so **every table that
viewer refuses is absent from it by construction, not by oversight.** The `ShowObjectDetails` picker
offers **227** tables; joining on **physical name** (never on UI label — see the warning below),
**31** are absent here, and the composition matters far more than the count:

| Group | Count | Status |
|---|---:|---|
| Refused by the viewer (*"Data for that table not supported"*) | **25** | **Recoverable over REST** — `GET /rest/businessObject/{type}/lxid/{id}?deep=true`. The `Page Layout` trio was obtained this way; see [`../features/page-layouts/`](../features/page-layouts/) |
| `Punch List` family | 4 | **Out of scope** — census entries below only |
| Genuine in-scope omissions | **2** | `ChangeManage`, `VirtualTemplateMember` — one field each |

**So the in-scope catalogue gap is two single-field tables.** The business-object census is
essentially complete for in-scope work.

> **Warning: never join this catalogue on UI label.** The UI systematically renames objects,
> especially computed views. A label-based diff reports **18** apparent absences where a
> physical-name diff reports **6** — the twelve differences include `General Entity Info`
> (`ProjectEntity`), `Development Target` (`DevelopmentSlot`), `Schedule Template`
> (`VirtualTemplateSchedule`) and eight further `Virtual*` period projections presented under
> business names. `ProjectEntity` is the one that matters most, being the universal entity supertype.

### `Punch List` — out of scope, census entries only

**Observed.** Four tables, 33 fields between them, fully captured in
[`../tenants/bbw-platform-tables.json`](../tenants/bbw-platform-tables.json).

| sqlTableID | Object | Physical | Fields | Purpose |
|---:|---|---|---:|---|
| `3197` | Punch List | `PunchList` | 10 | A snagging list against a project or facility |
| `3198` | Punch List Assignee | `PunchListAssignee` | 5 | Who a punch list is assigned to |
| `3199` | Punch List Task | `PunchListTask` | 13 | One defect item on a punch list |
| `3200` | Punch List Task Assignee | `PunchListTaskAssignee` | 5 | Who a defect item is assigned to |

**Why out of scope.** A search of all 38 approved BRDs returns **zero** files for `punch` /
`punch list`, `snag`, `defect list` or `site survey`, verified against a control term. More
decisively than the absence: two BRDs describe the existing ASG Edge system — *"the deal-making and
**construction management** platform"* — as a **separate product** that ASG Edge+ integrates with and
migrates away from. Punch List is snagging, i.e. construction management, so the BRDs actively place
it in another system rather than merely omitting it. Treated here as the 27 Budgeting / Bid /
Cost-Tracking objects are: census and FK-graph completeness only, no analysis.

### The two genuine in-scope omissions

| sqlTableID | Object | Physical | Fields |
|---:|---|---|---:|
| `2460` | Change Manage | `ChangeManage` | 1 |
| `3004` | Member Template | `VirtualTemplateMember` | 1 |

**Derived.** Both are single-field objects, and `VirtualTemplateMember` fits the `VirtualTemplate*`
pattern already noted in open question 1 — a projection whose stored column is the only one exported.
Neither is likely to carry weight, but both should be confirmed rather than assumed.

## Open questions

1. **The 18 one-field objects.** `BudgetTemplate`, `TaskTemplate` and `FolderTemplate` each declare
   one field, yet their content is clearly visible through the corresponding `VirtualTemplate*`
   projection (16–17 fields including 12 `IsValidFor*` flags). That pattern suggests the export
   lists only the *stored* column and surfaces the rest through a view — but `Region` (1 field,
   in-degree 12) and `Notify` (1 field) do not fit that reading. Needs a `ShowObjectDetails.jsp`
   pass on each.
2. **`Project` vs `ProjectEntity`.** `Project` has 111 fields and is a `subtype_root`;
   `ProjectEntity` has 107. `INDEX.md` calls `Project` "a lightweight project identity record …
   distinct from the richer ProjectEntity" but reports only 6 Data-Fields leaves for it against 170
   for `ProjectEntity`. The two sources disagree about which is the lightweight one.
3. **28 objects have no Manage Data Fields entry at all** (no `LeafTable` match in `_crossmap.tsv`),
   including `Security`, `TaskGroup`, `TaskItem`, `NonMember` and both `*FullImport` objects. Are
   they simply not user-configurable, or is the Data Fields capture incomplete for them?
4. **What are `ChangeManage` and `VirtualTemplateMember`?** One field each, and the only two in-scope
   tables the picker exposes that this catalogue lacks.
5. `AuditColumn` and `AuditTable` describe a separate audit-log model, yet **162 of 223 objects
   also carry inline `CreatedByID`/`ModifiedByID` columns** (161 have `ModifiedByID`, only 79 have
   `CreatedByID` — so most objects record who last touched a row but not who made it). Which is
   authoritative? This is the same choice ASG Edge+'s open ADR-0020 question poses (in-transaction
   audit vs. the ADR-0012 outbox), and Lucernex appears to run both.
