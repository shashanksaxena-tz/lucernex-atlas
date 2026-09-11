#!/usr/bin/env python3
"""
Build featuremap.json — ONE mind map of Lucernex organised by FEATURE.

The schema map (mapdata.json) drills Product -> Module -> Entity -> Field ->
Type -> record. That answers "what exists". This map answers "what does the
product DO": every branch is a capability a user or an implementer would
recognise, and every node carries a written explanation. Numbered rules from
the docs corpus are attached under the feature area they belong to.

Re-runnable: python3 build_featuremap.py   (needs rules.json)
Output feeds build_app.py, which inlines it into the explorer at DATA.feature.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "rules.json"), encoding="utf-8") as fh:
    RULES = json.load(fh)

BY_ID = {r["id"]: r for r in RULES["rules"]}


def rule_node(rid, mod):
    r = BY_ID[rid]
    text = re.sub(r"\s+", " ", r.get("text") or "").strip()
    if len(text) > 460:
        text = text[:460].rsplit(" ", 1)[0] + " ..."
    name = r["id"] + "  " + (r.get("section") or "").strip()
    if len(name) > 90:
        name = name[:88] + "..."
    return {
        "name": name,
        "kind": "rule",
        "detail": text or "See the rule page for the full statement.",
        "conf": "derived",
        "mod": mod,
        "src": "docs/modules/%s/rules.md" % mod,
    }


def resolve(attach, mod):
    """attach: {'prefix': 'ACC'} | {'mention': 'PaymentTransaction'} | {'ids': [...]}"""
    if not attach:
        return []
    if "prefix" in attach:
        p = attach["prefix"] + "-R-"
        ids = [r["id"] for r in RULES["rules"] if r["id"].startswith(p)]
    elif "mention" in attach:
        m = attach["mention"]
        ids = [r["id"] for r in RULES["rules"]
               if m in (r.get("text") or "") or m in (r.get("section") or "")]
    else:
        ids = attach["ids"]
    return [rule_node(i, mod) for i in ids if i in BY_ID]


def node(name, kind, detail, conf="observed", mod=None, key=None, src=None,
         oos=False, children=None, attach=None):
    kids = [node(**c) if isinstance(c, dict) and "name" in c and "kind" in c else c
            for c in (children or [])]
    kids += resolve(attach, mod or key)
    n = {"name": name, "kind": kind, "detail": detail, "conf": conf}
    if mod:
        n["mod"] = mod
    if key:
        n["key"] = key
    if src:
        n["src"] = src
    if oos:
        n["oos"] = True
    if kids:
        n["children"] = kids
    return n


def area(key, title, what, children, attach=None, conf="observed"):
    """A level-1 feature area. `key` ties it to the module id for hue + links."""
    return {
        "name": title,
        "kind": "area",
        "detail": what,
        "conf": conf,
        "mod": key,
        "key": key,
        "src": "docs/modules/%s/README.md" % key,
        "children": children,
        "attach": attach,
    }


def cap(title, detail, conf="observed", src=None, children=None, attach=None, mod=None):
    return {
        "name": title, "kind": "capability", "detail": detail, "conf": conf,
        "src": src or None, "children": children, "attach": attach, "mod": mod,
    }


def fact(title, detail, conf="observed", mod=None, src=None):
    return {"name": title, "kind": "fact", "detail": detail, "conf": conf,
            "src": src, "mod": mod}


# ===========================================================================
# The feature tree. Sources: the module documentation corpus in docs/modules/,
# each claim carrying the confidence the docs corpus established for it.
# ===========================================================================

TREE = [
    area("accounting", "Lease Accounting - ASC 842 / IFRS 16 / Straight-line",
         "One accounting engine serves three lease-accounting standards. There is no "
         "separate ASC 842 module: a Summary/Period record pair (SLSummary, 134 fields; "
         "SLPeriod, 79) carries the schedule, and three mutually exclusive flags say "
         "which standard a schedule was produced under.",
         [
             cap("Classification is a separate record",
                 "ContractFinancialTest (93 fields) runs the five ASC 842 tests and holds "
                 "ASC 842 and IFRS 16 results side by side. An older ASC 840 Cap Lease Test "
                 "still sits directly on Contract. One field is literally the 90%-test as a "
                 "formula: InitLiabilityBalToThreshFairValueCtrld, initial liability balance "
                 "over threshold fair value - the 'substantially all of the fair value' "
                 "criterion, computed.",
                 src="docs/modules/accounting/asc-842.md + View Object Model"),
             cap("Classification uses three different term lengths",
                 "TermLength, TestTermLength and LikelyTermLength all live on "
                 "ContractFinancialTest. The term used for classification is not necessarily "
                 "the contractual term, because renewal options the lessee is reasonably "
                 "certain to exercise extend it. A rebuild needs all three, not one.",
                 conf="observed", src="docs/modules/contracts/cam-waterfall.md"),
             cap("Schedules are generated by a person, not a batch job",
                 "Generate Rent and Calculate Schedule are buttons on a record. The "
                 "accounting engine is user-triggered. What Generate Rent produces was "
                 "learned by reading the 11,426 transactions this tenant already has, "
                 "without writing to the shared training tenant.",
                 src="docs/screens/014-contract-record-end-user.md"),
             cap("Schedules are approved, not published",
                 "The ASC 842 Schedule Review/Approval workflow gates output: generate, "
                 "initial review, ASG approve, client approve - three steps. A rebuild needs "
                 "a schedule state machine, not just a calculator.",
                 src="docs/modules/workflow/README.md"),
             cap("Discount rate resolution is layered",
                 "Any calculation needing a discount rate resolves: contract-level override "
                 "first, then DiscountRate rows scoped by portfolio / country / state, then "
                 "the portfolio default Program.SLDiscountRate. The layered fallback is "
                 "stated as rule ACC-R-001.",
                 conf="derived", src="docs/modules/accounting/rules.md"),
             cap("Amortisation has a policy switch",
                 "GaapAmortizeMode has exactly two values: PER_DAY and PER_PERIOD. Day-based "
                 "versus period-based expense recognition is a single tenant-level choice.",
                 src="Live code-table capture"),
             cap("The engine also runs on equipment, not just leases",
                 "ContractFinancialTest, SLSummary and SLPeriod each carry a nullable foreign "
                 "key straight to Asset. The ASC 842 / IFRS 16 engine runs per equipment "
                 "asset - embedded equipment leases are first-class, not a workaround.",
                 src="docs/modules/assets-equipment/equipment-leases.md"),
             fact("This tenant runs ASC 842 only",
                  "The ASC 842 Schedule Type table holds exactly one value, '842 Rent'. The "
                  "Straight Line and IFRS 16 schedule-type tables are both empty. The "
                  "capability is present and unused - whether the rebuild needs IFRS 16 at "
                  "all is a business question, still open."),
             fact("Physical columns carry no numeric typing",
                  "In the physical Postgres export, 6,882 of 7,069 non-key columns are TEXT - "
                  "currency and percentages included. There is no numeric typing to inherit. "
                  "The rebuild's constitution already mandates BigDecimal; Lucernex shows "
                  "what happens without it."),
             fact("One field changes meaning by magnitude",
                  "SLSummary.SLRemainingAssetBalance is read as a percentage when 0-100 and "
                  "as currency at 100.01 and above. A genuine data-integrity hazard to "
                  "design out, not inherit.",
                  src="docs/modules/accounting/computed-vs-input-fields.md"),
         ],
         attach={"prefix": "ACC"}),

    area("contracts", "Expense Recovery (CAM)",
         "The CAM reconciliation is the product's computational centre of gravity: 379 of "
         "the product's 422 formula fields sit on the single ExpenseRecovery table. The "
         "vendor wrote the entire waterfall into the field UI labels, so the calculation "
         "did not have to be reverse-engineered.",
         [
             cap("The waterfall, as the vendor labels it",
                 "Sub Total #1 = Controllable + Non-Controllable - Deductions. "
                 "Pass-Through = ST1 + Admin Fee % + Admin Fee + Additions. "
                 "Sub Total #2 = Pass-Through - Recoveries. "
                 "Net Pass-Through = ST2 x Pro Rata Share Rate. "
                 "Net Amount Due = NPT - Pre-Paid. Revised = NAD + Adjustments. "
                 "Every one of those expressions is literally a field label. Observed.",
                 src="docs/modules/contracts/cam-waterfall.md"),
             cap("CAM is a reconciliation grid, not a schedule",
                 "Expense recovery has no schedule layer and does not follow the "
                 "Clause/Schedule/Transaction/Projection pattern every other money flow "
                 "uses. Treating it as an instance of that pattern would be the single most "
                 "expensive modelling mistake available here. It is a wide grid of stored, "
                 "precomputed figures.",
                 conf="derived", src="docs/modules/contracts/setup-schedule-transaction-pattern.md"),
             cap("Four measurement bases, gross and net",
                 "Every figure exists as Budgeted, Reported, Approved and Prior, each in "
                 "Gross and Net form, and five pairwise variances (Approved-Budgeted, "
                 "Approved-Prior, Budgeted-Prior, Reported-Approved, Reported-Prior) are "
                 "precomputed for every waterfall line. The table is wide because the "
                 "variance grid is fully materialised rather than computed on read. A "
                 "rebuild could store four bases and compute variances on demand - the "
                 "largest single schema simplification available in this product.",
                 src="View Object Model, ExpenseRecovery field labels"),
             cap("Occupancy gross-up applies only on the Approved basis",
                 "Approved Net Pass-Through multiplies by an Occupancy Factor "
                 "(ST2*PRS*Occ); every other basis uses only the pro-rata rate (ST2*PRR). "
                 "That is the gross-up provision - recovering as if the centre were fully "
                 "occupied - applied where the tenant's auditor would insist on it. One "
                 "formula for all bases gets approved amounts wrong on every gross-up lease.",
                 src="Vendor field labels, Observed"),
             cap("Prior periods are nullable by design (NoZeroDef)",
                 "Every Prior* field carries the suffix NoZeroDef: a prior period that does "
                 "not exist is unknown, not zero. Zero-defaulting would manufacture 100% "
                 "variances on every first-year reconciliation. Recovery measures must be "
                 "nullable, never zero-defaulted.",
                 conf="derived", src="Field-name analysis, CON-R-160"),
             fact("What is still unknown in the waterfall",
                  "Three gaps: whether Admin Fee % applies to Sub Total #1 or something "
                  "narrower; where CapAmount clamps (it has variance fields but appears in "
                  "no labelled formula); and what feeds the Occupancy Factor. All tracked "
                  "as open questions in the corpus."),
         ],
         attach={"ids": ["CON-R-153", "CON-R-154", "CON-R-155", "CON-R-156",
                         "CON-R-157", "CON-R-158", "CON-R-159", "CON-R-160",
                         "CON-R-161"]}),

    area("contracts", "Contracts & Lease Administration",
         "The Contract aggregate is the centre of the product: 570 fields across four "
         "physical tables, and 62 other record types point at it. Payment processing, "
         "percentage rent and ASC 842 accounting all sit downstream of it, which is why "
         "its schema freeze gates them.",
         [
             cap("The Clause / Schedule / Transaction / Projection pattern",
                 "Every money flow in the product is modelled as four layers: a Clause "
                 "(the negotiated term), a Schedule (the calculated run of amounts), a "
                 "Transaction (an executed payment or charge), and a Projection (future "
                 "expectation). Rent, escalations, and most financial terms follow it. "
                 "CAM is the one exception - see the Expense Recovery branch.",
                 conf="derived", src="docs/modules/contracts/setup-schedule-transaction-pattern.md"),
             cap("Lifecycle lives in tenant data, not in schema",
                 "The nine lifecycle states - Open, Future Possession, Possession, "
                 "Possession - Paying Rent, Active, Closed - Active, Closed, and two "
                 "Accounting Purposes Only variants - sit in a tenant-authored drop-down. "
                 "Anyone with drop-down rights can add a tenth. The platform's own "
                 "Contract Status Code has only three values and means something "
                 "different. Both are required on the same form.",
                 src="docs/data-model/code-table-registry.md"),
             cap("A contract can be its own parent",
                 "MasterContractID is declared as a Contract ID - a self-reference carrying "
                 "the master-lease and sublease hierarchy.",
                 src="_lucernex_objects_summary.txt"),
             cap("Relationships are asymmetric by cardinality",
                 "From Contract, Facility is reached as a single related record. From "
                 "Facility, Contract appears as an embedded child grid. The UI models the "
                 "one-to-many direction differently from the many-to-one - a rebuild "
                 "should pick one convention.",
                 src="Live screen capture, screen 014"),
             cap("Vendor is a relabelled Employer",
                 "PaymentTransaction.VendorID is declared as an Employer ID. Contract has "
                 "no direct vendor foreign key at all - the payee relationship lives one "
                 "level down, on the payment transaction, not on the lease.",
                 src="_crossmap.tsv"),
         ],
         attach={"prefix": "CON"}),

    area("contracts", "Rent, Payments & Invoices",
         "Money that actually moves: generated rent, payment transactions against a "
         "lease, and the invoice records that carry them. Everything here hangs off "
         "PaymentTransaction - the Contract itself never holds a vendor or a payment.",
         [
             cap("Generate Rent produces transactions",
                 "The Generate Rent button writes Transaction rows - this tenant holds "
                 "11,426 of them. The existing output was read instead of pressing the "
                 "button on a shared tenant. Overwrite-versus-duplicate behaviour and "
                 "batch-number storage remain open, needing a disposable contract.",
                 src="docs/modules/contracts/rent-generation.md"),
             cap("The payee is on the payment, not the lease",
                 "VendorID lives on PaymentTransaction, typed as Employer ID. Payment "
                 "history import is also a workflow step on Lease Admin Request "
                 "('Import Payment History/Sales'), so payments enter both by button and "
                 "by process.",
                 src="docs/modules/workflow/"),
             cap("Invoices are line-item records",
                 "InvoiceItem carries the only Math fields outside the recovery grid "
                 "(InvoiceAmount, TotalAmount) besides the accounting tests - invoicing "
                 "computes its totals, it does not store them pre-summed.",
                 src="View Object Model, Math field list"),
         ],
         attach={"mention": "PaymentTransaction"}),

    area("contracts", "Percentage & Variable Rent",
         "Turnover and use-based rent: 17 record types, 472 fields, documented under the "
         "contracts module because the analysis sat naturally there.",
         [
             cap("Sales feed the percentage calculation",
                 "Tenant sales are imported (the same workflow step imports payment "
                 "history or sales), and percentage-rent terms compare sales against "
                 "breakpoints. The record family covers the term, the sales periods, and "
                 "the computed overage.",
                 conf="derived", src="docs/modules/contracts/percentage-rent.md"),
             cap("One of four import channels",
                 "Lease Admin Request's step 'Import Payment History/Sales' is the single "
                 "named entry point for sales data in the observed workflows - the "
                 "product has no separate sales module.",
                 src="docs/modules/workflow/README.md"),
         ],
         attach={"mention": "Percentage"}),

    area("workflow", "Workflows & Approvals",
         "Four workflows are live in this tenant, one per form type: Lease Admin Request "
         "(8 steps), Rent Payment Review/Approval (6), ASC 842 Schedule Review/Approval "
         "(3), and User Request (2). The Form is the record; the Work Flow is its "
         "process; they share a name.",
         [
             cap("Lease Admin Request is BRD-24, already implemented",
                 "Its eight steps: Initial Review, Abstract Lease Document, ASG Review, "
                 "Client Review, Import Payment History/Sales, Finalize, Finalize "
                 "(Defaults), Complete. The BRD describes what the process should be; "
                 "this shows what it actually is.",
                 src="docs/modules/workflow/README.md"),
             cap("Each step shows a different screen",
                 "A workflow step binds its own page layout. The same request record "
                 "presents a different field surface at Submit, at Review and at Approve. "
                 "That per-step layout binding is what makes the engine expressive enough "
                 "to run a real business process.",
                 src="Live capture, Manage Work Flows"),
             cap("Routing is by position, not by person",
                 "Approval Level is Member, Job Title or Ad Hoc - and the API's "
                 "AssigneeType enum goes further: ALL, PARENT, REGION1, REGION2, MARKET, "
                 "JOB_TITLE. Notifications walk the org chart to three explicit levels. "
                 "Routing resolves through the geographic region hierarchy, not the "
                 "supervisor chain.",
                 src="docs/modules/workflow/"),
             cap("Four ways to start a workflow",
                 "KickOffMethod: STEP_ACTION, PAGE_LAYOUT, STATUS_CHANGE, TASK. This is "
                 "the trigger taxonomy any rebuilt rule engine has to reproduce.",
                 src="docs/modules/workflow/"),
             cap("Three nested state machines",
                 "The workflow module documents the template/instance split, step actions "
                 "and routing as three nested state machines - template lifecycle, "
                 "instance lifecycle, and per-step transitions.",
                 conf="derived", src="docs/modules/workflow/README.md"),
             fact("No Task step exists anywhere in this tenant",
                  "All 19 configured steps are Form steps, though 'add task step' exists in "
                  "the product. WorkFlowTemplateStep has 55 fields and the admin grid "
                  "surfaces six - most of the step model is still unseen."),
             fact("Where workflow status lives is unresolved",
                  "'Work Flow Status Code' is absent from the catalogue of 207 Firm Drop "
                  "Downs. The nearest that exist are Approval, Last Action and Decision "
                  "status codes."),
         ],
         attach={"prefix": "WF"}),

    area("layouts-and-forms", "Forms, Pages & Layouts",
         "A Page presents a record that already exists. A Form is something else entirely: "
         "a tenant-authored request type - an Issue Type in the code table - with one "
         "layout per workflow step. A Custom List is a Form without the workflow. "
         "Lucernex never built a form builder; it built one ticket record and let the "
         "tenant define its subtypes.",
         [
             cap("A Form is an Issue Type",
                 "TableType 2035 is Issue Type Code - which is why Manage Forms opens the "
                 "same editor as every Firm Drop Down. Every request-shaped feature in the "
                 "product is the same table with a different subtype value.",
                 src="docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md"),
             cap("Layouts are bound per workflow step",
                 "The Edit Layout / List Layout split serves 56% of all end-user screens "
                 "through just two JSPs: PForm.jsp (detail) and PLForm.jsp (list). The "
                 "layout is the runtime contract between the data model and the screen.",
                 src="docs/data-model/screen-routing.md"),
             cap("Everything an admin controls is one editor",
                 "All Firm Drop Downs are values of a single TableType discriminator on one "
                 "generic editor: 207 platform-fixed tables whose values you may edit but "
                 "whose catalogue you may not extend, plus tenant-authored Client Drop "
                 "Downs which support cascading lists.",
                 src="docs/data-model/code-table-registry.md"),
         ],
         attach={"prefix": "LAY"}),

    area("layouts-and-forms", "Conditional Field Rules",
         "The other rule engine in the product, and the one closest to what ASG Edge+ "
         "calls a rule engine: every field, or a whole sub-page section, can carry one "
         "rule set, read as a sentence: [Show | Show and Require | Hide] this field when "
         "[all | any] of the following rules match.",
         [
             cap("A flat engine - deliberately",
                 "No nesting, no mixed AND/OR. A rule set is one flat list evaluated "
                 "all-or-any. That keeps every rule explicable to a business user and "
                 "indexable by a machine.",
                 src="docs/modules/layouts-and-forms/conditional-fields.md"),
             cap("Operators depend on the driver's type",
                 "Dropdown drivers get is in / is not in. Number drivers get the six "
                 "comparisons. Boolean drivers get selected / not selected. All three get "
                 "is specified / is not specified. Text and Date fields can never drive a "
                 "rule at all - a deliberate constraint.",
                 src="Live capture, conditional filter editor"),
             cap("Rules cross entity boundaries",
                 "A Contract layout offers 85 candidate driver fields drawn from four "
                 "tables: Contract 65, ProjectEntity 9, Facility 7, Location 4. A Contract "
                 "field can be hidden because of a value on its Location record.",
                 src="Live capture, conditional filter editor"),
             cap("Rules are stored as an opaque JSON blob",
                 "One json.conditionalFieldsConfig per target field. Cheap to write, "
                 "impossible to query: Lucernex cannot answer 'which layouts depend on "
                 "this drop-down?'. Storing predicates as rows instead would give the "
                 "rebuild a Where-Used answer for free.",
                 conf="derived", src="docs/modules/layouts-and-forms/conditional-fields.md"),
         ]),

    area("reporting", "Reporting & BI",
         "Every field-consuming subsystem - reports, forms, exports - joins to one "
         "shared field registry, ReportGroupAvailableField. The vendor's own schema "
         "names the key to it 'Report/Form Field ID': a single type unifying report "
         "field and form field.",
         [
             cap("One field registry confirmed",
                 "The report catalogue and the field catalogue are one table, confirmed "
                 "from the schema rather than hypothesised. A rebuilt reporting layer "
                 "needs the same single registry or it will re-implement field metadata "
                 "per consumer.",
                 src="docs/modules/reporting/README.md"),
             cap("The admin tool inventory",
                 "The reporting module documents which admin tools exist, what each "
                 "exposes, and that none of them define calculation logic - computed "
                 "values are all defined at the field level, in the accounting and "
                 "recovery engines.",
                 conf="derived", src="docs/modules/reporting/"),
         ],
         attach={"prefix": "RPT"}),

    area("property-tax", "Property Tax",
         "Property tax is modelled as a roll-up: PropertyTaxSummary to Assessment, then "
         "either a Bill (with Detail lines) or an Appeal (with an Award), all under the "
         "Parcel that the tax attaches to.",
         [
             cap("The assessment roll-up",
                 "Summary -> Assessment -> {Bill -> Detail, Appeal -> Award}. The branch "
                 "splits at the assessment: the normal path produces bills, the contested "
                 "path produces appeals and awards.",
                 src="docs/modules/property-tax/README.md"),
             cap("Tax is also a recoverable expense",
                 "CodeRecoveryGroupID and CodeRecoveryTypeID tie tax records into the CAM "
                 "recovery world - property tax is modelled as a recoverable expense the "
                 "landlord can pass through, not just a bill someone pays.",
                 src="docs/modules/property-tax/appeals.md"),
             cap("A won appeal never touches an issued bill",
                 "The appeal/award workflow documents a gap: an award reducing the tax "
                 "does not flow back into an already-issued bill. The correction loop is "
                 "manual, and a rebuild must decide deliberately whether to keep it that "
                 "way.",
                 conf="derived", src="docs/modules/property-tax/appeals.md"),
         ],
         attach={"prefix": "TAX"}),

    area("portfolio-transactions", "Portfolio & Site Pipeline",
         "Program is the Portfolio - the screen routing proves the menu item labelled "
         "'Portfolio' is the Program record - and the pre-lease deal pipeline hangs "
         "beneath it: PotentialProject (shown as 'Site') to RETransaction to Scenario.",
         [
             cap("The Site -> Project -> Facility promotion pipeline",
                 "Two layout fields unique to Program name it: SiteToProjectSetupLayoutID "
                 "and ProjectToFacilitySetupLayoutID - the layouts used when promoting a "
                 "deal site into a project, and a project into a facility. One confirmed "
                 "foreign key (Project.FacilityID) closes half of the chain.",
                 src="docs/modules/portfolio-transactions/site-pipeline.md"),
             cap("Deals are scenarios before they are leases",
                 "A PotentialProject (Site) collects RETransactions (the deal attempts) "
                 "and Scenarios (the what-if variants). Nothing becomes a Contract until "
                 "the pipeline promotes it - the pipeline is the front door of the "
                 "product.",
                 conf="derived", src="docs/modules/portfolio-transactions/README.md"),
             fact("The pipeline's objects are invisible to the field catalogue",
                  "PotentialProject has 108 census fields and zero Data Fields rows - the "
                  "starkest of the twelve objects the catalogue omits entirely, plausibly "
                  "because pipeline objects are not layout-placeable (inferred)."),
         ],
         attach={"prefix": "POR"}),

    area("projects-capital", "Projects & Capital Construction",
         "Capital-project scheduling and the issue/RFI loop. The scheduling data is one "
         "of the strangest findings in the product: Task, TaskGroup and TaskItem are "
         "byte-identical tables.",
         [
             cap("Three identical tables, one hierarchy",
                 "Task, TaskGroup and TaskItem are byte-identical tables, and every "
                 "foreign key of that shape in the entire schema resolves to TaskGroup "
                 "alone. The WBS hierarchy and the CPM dependency network are two "
                 "separate graphs drawn over the same rows.",
                 src="docs/modules/projects-capital/scheduling.md"),
             cap("The issue/RFI loop",
                 "Construction issues and RFIs run through the same Issue record that "
                 "backs Forms - the request machinery is shared across the product, not "
                 "duplicated per module.",
                 conf="derived", src="docs/modules/projects-capital/README.md"),
         ],
         attach={"prefix": "PRJ"}),

    area("facilities-locations", "Facilities & Locations",
         "The central naming question of the whole product, settled: Location is the "
         "site - the 'Center' - and Facility is the building standing on it. Complex, "
         "Parcel, Prototype, Space and Tenant fill in the geography between them.",
         [
             cap("Location vs Facility vs Site",
                 "Location is the site/Center (address, market, demographics). Facility "
                 "is the physical building on that site (GLA, rentable area, floors). "
                 "Contracts attach to facilities; the CAM pro-rata share divides by "
                 "rentable area that lives on the facility, not the site.",
                 src="docs/modules/facilities-locations/location-vs-facility-vs-site.md"),
             cap("The demographics / site-selection family",
                 "Location carries the site-selection data set - demographics, trade "
                 "area, competition - which is why PotentialProject sites and Location "
                 "records share so much shape. The deal pipeline is modelled on the "
                 "site concept.",
                 conf="derived", src="docs/modules/facilities-locations/README.md"),
         ],
         attach={"prefix": "FAC"}),

    area("people-parties", "People, Parties & Org",
         "Member is the most-referenced record in the schema - 290 foreign keys point "
         "at it, more than at ProjectEntity - but 83% of those are just the universal "
         "CreatedByID / ModifiedByID audit pair. Person is a second, unnamed supertype.",
         [
             cap("Person is a second supertype",
                 "Person and NonMember are field-for-field identical (37 fields, zero "
                 "differences); Member is Person's 37 plus 44 login and authentication "
                 "fields. All three share PersonID, typed as a plain Number rather than "
                 "a declared foreign-key type. Same shared-key inheritance pattern "
                 "ProjectEntity uses, applied to people, and nothing names it.",
                 conf="derived", src="docs/modules/people-parties/member-vs-person-vs-party.md"),
             cap("The org chart used for routing is geographic",
                 "Member.SupervisorID points at Member - a supervisor chain - but "
                 "workflow's REGION1 / REGION2 / MARKET routing does not use it. It "
                 "resolves through ProjectEntity's RegionID / RootRegionID / SubRegionID "
                 "plus LinkRegionManager. Two different hierarchies; routing uses the "
                 "geographic one.",
                 src="docs/modules/people-parties/README.md"),
             cap("Region resolves to people through lists",
                 "Region carries ParentRegionID (self-referencing - regions nest), plus "
                 "ManagerIDList and MemberIDList pointing at Member: this is how a region "
                 "resolves to actual people for workflow routing.",
                 conf="observed", src="docs/data-model/reading-the-census.md"),
             cap("Identity sits on nearly every write path",
                 "161 objects carry ModifiedByID and 79 carry CreatedByID. Any write "
                 "anywhere must resolve a member - arguing for one cross-cutting "
                 "audit-stamp mechanism in the rebuild, not per-service copies.",
                 conf="derived", src="docs/modules/people-parties/README.md"),
         ],
         attach={"prefix": "PPL"}),

    area("assets-equipment", "Assets & Equipment",
         "The Asset record and the maintenance loop around it: ServiceRequest raises "
         "the problem, WorkOrder performs the work - both are Issue variants, so the "
         "same request machinery that backs Forms also backs maintenance.",
         [
             cap("Equipment leases run on the accounting engine",
                 "ContractFinancialTest, SLSummary and SLPeriod each carry a nullable FK "
                 "straight to Asset: embedded equipment leases are classified and "
                 "scheduled by the same ASC 842 / IFRS 16 engine as real estate.",
                 src="docs/modules/assets-equipment/equipment-leases.md"),
             cap("ServiceRequest -> WorkOrder",
                 "The maintenance loop is the Issue pattern again: request, triage, "
                 "work order, completion. A rebuild gets this nearly free if its request "
                 "engine is as general as Lucernex's single Issue table.",
                 conf="derived", src="docs/modules/assets-equipment/README.md"),
         ],
         attach={"prefix": "AST"}),

    area("documents-folders", "Documents & Binders",
         "Every entity root in the product shows Documents and Binders tabs. The "
         "Documents half is a real object family; the Binders half is not backed by "
         "any single object the census can name with confidence.",
         [
             cap("Universal Documents tabs",
                 "Document check-in and versioning attach to every entity root through "
                 "the ProjectEntity supertype. Four of the ten document objects are "
                 "near-empty stubs - markup content and outbound correspondence are not "
                 "recoverable from this schema.",
                 src="docs/modules/documents-folders/README.md"),
             cap("Binders: CommitteePackage is the best candidate",
                 "CommitteeDocuments/PECommPkg.jsp routes to CommitteePackage from every "
                 "entity root, and both field inventories list the object - though they "
                 "name different single fields for it, so neither shows the real table. "
                 "The earlier 'no object backs Binders' claim was withdrawn.",
                 conf="derived", src="docs/data-model/reading-the-census.md"),
         ],
         attach={"prefix": "DOC"}),

    area("platform-tenancy", "Platform & Tenancy",
         "The underpinnings every feature above stands on: Firm is the tenant, "
         "ProjectEntity is the universal entity supertype, and the two are constantly "
         "confused because both appear on nearly every record.",
         [
             cap("FirmID is the tenant key; ProjectEntityID is not",
                 "163 foreign keys point at ProjectEntity - it is the universal 'thing "
                 "you can own' supertype. But it is NOT the tenant boundary: FirmID is, "
                 "and FirmID is typed Text, not a declared foreign key. The one "
                 "relationship every row has is the one the schema declines to model, "
                 "which is exactly why tenant isolation cannot be enforced by the schema. "
                 "Decisive for database-per-tenant.",
                 src="docs/data-model/project-entity.md"),
             cap("The tenant travels in the token",
                 "The session JWT carries firmname and a cluster claim shaped host:tenant "
                 "- evidence Lucernex routes each request to a tenant-specific database "
                 "using a value inside the token, not a lookup in a shared table.",
                 src="Live JWT inspection"),
             cap("448 field-type codes hide a 10-value system",
                 "The API's FieldType enum is BOOLEAN, COMPUTED, DATE, DATETIME, FK, "
                 "FLOAT, INTEGER, MONEY, PERCENTAGE, STRING. COMPUTED and FK are "
                 "first-class types - the platform distinguishes engine-calculated values "
                 "from user input in its type system. MONEY and PERCENTAGE are distinct "
                 "from FLOAT, and BigDecimal is a declared scalar: the vendor reached the "
                 "same conclusion the rebuild's constitution mandates.",
                 src="docs/data-model/graphql-api.md"),
             cap("One code-table registry, 207 entries",
                 "All Firm Drop Downs are values of a single TableType discriminator. "
                 "Master lists - lifecycle states, schedule types, workflow statuses - "
                 "are configuration, not schema.",
                 src="docs/data-model/code-table-registry.md"),
             cap("The API is read-heavy by design",
                 "617 GraphQL queries against 3 mutations. The read surface is rich and "
                 "typed; the write surface is not. Whatever writes exist run through a "
                 "thin REST layer whose endpoint shapes never rendered, and remain "
                 "uncaptured - a standing open item.",
                 src="docs/data-model/graphql-api.md + rest-api.md"),
         ],
         attach={"prefix": "PLT"}),

    {
        "name": "Out of scope - Cost, Budgeting & Bidding",
        "kind": "area",
        "detail": "Excluded from the rebuild by decision, kept in the corpus so the "
                  "foreign-key graph stays whole. Objects like BudgetOptionTemplate (107 "
                  "census fields, zero catalog rows) live here with one-line descriptions "
                  "only. Dashed in the map, like the module view.",
        "conf": "observed",
        "oos": True,
        "children": [
            {"name": "Why excluded", "kind": "fact", "conf": "observed",
             "detail": "Cost management, budgeting and bidding are out of scope by "
                       "decision for ASG Edge+. They remain catalogued so that impact "
                       "analysis through the FK graph is never silently wrong at the "
                       "boundaries."},
        ],
    },
]


def resolve_tree(n, parent_mod):
    """Replace each node's `attach` spec with concrete rule children."""
    if isinstance(n, list):
        return [resolve_tree(c, parent_mod) for c in n]
    if not isinstance(n, dict):
        return n
    mod = n.get("mod") or n.get("key") or parent_mod
    n = dict(n)
    if "attach" in n:
        rules = resolve(n.pop("attach"), mod)
        kids = list(n.get("children") or []) + rules
        if kids:
            n["children"] = kids
    if "children" in n:
        n["children"] = resolve_tree(n["children"], mod)
    return n


def strip(n):
    """Drop None-valued keys so the JSON carries only what is set."""
    if isinstance(n, dict):
        return {k: strip(v) for k, v in n.items() if v is not None}
    if isinstance(n, list):
        return [strip(c) for c in n]
    return n


def count(n):
    return 1 + sum(count(c) for c in n.get("children") or [])


root_children = [strip(n) for n in resolve_tree(TREE, None)]
total = count({"children": root_children})

out = {
    "meta": {
        "name": "Lucernex - the product by feature",
        "detail": "One map organised by what the product DOES, not by database table. "
                  "Every node carries a written explanation; rule nodes carry the "
                  "numbered rules from the docs corpus and link to their full text. "
                  "Follow a branch top-down: feature area, the capabilities inside it, "
                  "the facts and constraints observed in the live tenant, then every "
                  "numbered rule that belongs to the area.",
        "conf": "observed",
        "src": "docs/modules/ corpus, captured from the live tenant 2026-09-10/11",
        "areas": len(root_children),
        "nodes": total,
        "rules": RULES["total"],
    },
    "root": {"name": "Lucernex IWMS", "kind": "product", "children": root_children},
}

with open(os.path.join(HERE, "featuremap.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, separators=(",", ":"), sort_keys=False)

print("wrote featuremap.json: %d areas, %d nodes total, %d rules attached"
      % (len(root_children), total, RULES["total"]))
