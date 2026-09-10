#!/usr/bin/env python3
"""
build_graph.py — parse the Lucernex object-model export into structured graph data.

Input  : ../../_lucernex_objects_summary.txt   (TSV: LUCERNEX OBJECT / PG TABLE / FIELD COUNT / FIELDS)
Output : objects.json, edges.json, modules.json  (written next to this script)

The FIELDS cell is a " | "-separated list of `Name(Type)` pairs. Types may themselves contain
parentheses (`Dropdown (Currency Type Code)`), so the type is taken as everything between the
FIRST "(" and the LAST ")".

Evidence for the FK reading of `<Entity> ID` types: docs/admin/009-related-fields-and-data-model.md
(Observed, from Lucernex's own View Object Model / ShowObjectDetails.jsp).

Re-runnable and side-effect free apart from the three JSON outputs.
Usage: python3 docs/mindmap/build_graph.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SRC = REPO / "_lucernex_objects_summary.txt"

# ---------------------------------------------------------------------------
# 1. Type-family classification
# ---------------------------------------------------------------------------

# Plain scalar types — no relational meaning.
SCALAR_TYPES = {
    "Text", "Number", "Currency", "Date", "Time", "Boolean", "Percentage",
    "Area", "Acreage", "Date Range", "Number Format", "Percent or Currency",
    "5-Digit Number", "2-Digit Number", "Number with no digits",
}

# Reference-shaped types that do NOT end in " ID" — they name a target concept
# but carry no explicit `<Entity> ID` suffix. Kept in their own family so they
# are never silently promoted to hard FKs.
SOFT_REFERENCE_TYPES = {
    "Contact": "LinkProjectEntityContact",   # e.g. ProjectEntity.LinkProjectEntityContactListData
    "Entity": None,                          # untyped entity handle
    "Member": "Member",
    "Part": "Part",
    "Parts Package": "PartPackage",
    "Document List": "Document",
    "Custom List": "ClientListRow",
    "Holiday Calendar": "HolidaySchedule",
    "Response": "IssueResponse",
    "Dropdown": None,                        # bare dropdown, no bound code list named
}

DROPDOWN_RE = re.compile(r"^Dropdown \((?P<code>.+)\)$")
FK_RE = re.compile(r"^(?P<target>.+?) ID$")


def type_family(t: str) -> str:
    if t in SCALAR_TYPES:
        return "scalar"
    if DROPDOWN_RE.match(t):
        return "dropdown"
    if FK_RE.match(t):
        return "foreign_key"
    if t in SOFT_REFERENCE_TYPES:
        return "soft_reference"
    return "other"


# ---------------------------------------------------------------------------
# 2. FK target resolution
# ---------------------------------------------------------------------------

def normalise(name: str) -> str:
    """'Payment Transaction' -> 'PAYMENTTRANSACTION'; 'Task/Group' -> 'TASKGROUP'."""
    return re.sub(r"[^A-Za-z0-9]", "", name).upper()


# Curated aliases. Each entry is (target_object, confidence, rationale).
# `high`   = corroborated by an independent source (doc 009, a PK-type check, or the
#            data-fields legend in docs/data-fields/INDEX.md).
# `medium` = strong single-source naming/domain inference.
# `low`    = best guess, explicitly flagged for follow-up.
ALIASES: dict[str, tuple[str | None, str, str]] = {
    # --- high confidence -----------------------------------------------------
    "Entity": (
        "ProjectEntity", "high",
        "ProjectEntity's own PK column ProjectEntityID is typed `Number`, while every other "
        "object carries ProjectEntityID typed `Entity ID`. `Entity ID` is therefore the FK type "
        "pointing at ProjectEntity. Corroborated by docs/data-fields/INDEX.md "
        "(`sTYPE_PROJECT_ENTITY`, `sTYPE_PORTFOLIO` = 'portfolio-level ProjectEntity record').",
    ),
    "Portfolio": (
        "Program", "high",
        "doc 009 (Observed, View Object Model): Contract.ProgramID has Type `Portfolio ID`, "
        "UI Label 'Portfolio' — a naming-legacy mismatch, Portfolio == Program table.",
    ),
    "Employer": (
        "Employer", "high",
        "Exact match. doc 009 also proves PaymentTransaction.VendorID is typed `Employer ID`, "
        "i.e. Lucernex 'Vendor' is a relabelled Employer.",
    ),
    # --- medium confidence ---------------------------------------------------
    "item": (
        None, "unresolved",
        "No `Item` object exists in the 223. Lower-case `item` (all other FK types are Title "
        "Case) marks it as a distinct, polymorphic handle. All 56 occurrences are on budgeting / "
        "bid-package / part objects, so it most likely addresses a generic line-item row "
        "(BudgetLineItem / BudgetLineLeaf / PartPackageItem) resolved at runtime by the owning "
        "object rather than by the column's type. Rebuild consideration, not a resolvable edge.",
    ),
    "Country, State, County": (
        "StateProvinceCountry", "medium",
        "No object of that literal name; StateProvinceCountry is the only geography reference "
        "table in the export and column names are IStateProvinceCountryID.",
    ),
    "County": (
        "Jurisdiction", "medium",
        "Every `County ID` column is named JurisdictionID; Jurisdiction is the taxing-authority "
        "reference table.",
    ),
    "Template": (
        None, "unresolved",
        "Ambiguous. Columns are BudgetTemplateID, TaskTemplateID, FolderTemplateID, "
        "WorkFlowTemplateID etc. — one shared `Template ID` type serving several distinct "
        "template tables (BudgetTemplate, TaskTemplate, FolderTemplate, WorkFlowTemplate, "
        "EntityTemplate, ProcessTimelineTemplate, BidPackageTemplate). The target is determined "
        "by the column name, not the type. Resolved per-column below where the name is explicit.",
    ),
    "Budget Type": (
        "BudgetColumnType", "medium",
        "No `BudgetType` object. BudgetColumnType is the only budget-typing table, and "
        "docs/data-fields/INDEX.md documents `sTYPE_BUDGET_COLUMN_TYPE` as the budget-type lookup.",
    ),
    "Equipment": (
        "Asset", "medium",
        "No `Equipment` object. walkHierarchy.jsp exposes 'Equipment Contract' as an aggregate "
        "root and Asset is the only equipment-shaped table (122 fields, CodeAssetCategory). "
        "Equipment is most likely a Contract/Asset flavour rather than its own table.",
    ),
    "Step": (
        "WorkFlowStep", "medium",
        "Columns are WorkFlowStepID / StepID on workflow objects.",
    ),
    "Straight-Line Schedule": (
        "SLSummary", "medium",
        "The straight-line schedule header table. SLPeriod holds its periods; CodeSLSchedule is "
        "the code list, not the schedule instance.",
    ),
    "Budget Template View": (
        "BudgetView", "medium",
        "Only budget-view table in the export.",
    ),
    "Vendor Site": (
        "EmployerSite", "medium",
        "'Vendor' == Employer (doc 009), so a Vendor Site is an EmployerSite row.",
    ),
    "RE Transaction Contact": (
        "ReTransScenContact", "medium",
        "The only RE-transaction contact table.",
    ),
    "Global Property Section": (
        "GlobalProperty", "medium",
        "Only global-property table in the export.",
    ),
    "Work Flow Step Approver": ("WorkFlowStepApprover", "high", "Exact match after normalisation."),
    # --- low confidence / unresolved ----------------------------------------
    "Report/Form Field": (
        "ReportGroupAvailableField", "low",
        "No ReportFormField object. ReportGroupAvailableField is the closest report-field "
        "metadata table, but the report/form designer's own metadata is largely absent from this "
        "business-object export.",
    ),
    "DashboardComponent": (
        None, "unresolved",
        "No dashboard object in the export. Dashboard configuration is platform metadata living "
        "outside the 223 business objects.",
    ),
    "Custom Drop Down": (
        None, "unresolved",
        "No object. Drop-down definitions are configuration metadata (see docs/admin/007), not "
        "business objects — same class of gap as page layouts and data fields.",
    ),
    "Action": (
        "WorkFlowTemplateStepAction", "low",
        "Both `Action ID` columns sit on workflow objects; the only Action table is "
        "WorkFlowTemplateStepAction.",
    ),
    "Folder Template Action": (
        "FolderTemplate", "low",
        "Dropdown-adjacent; no dedicated action table for folders.",
    ),
    "Budget Index Variable": (
        "BudgetIndex", "high",
        "Sole occurrence is BudgetIndexValue.BudgetIndexID — the child-to-parent FK.",
    ),
    "Custom Field": (
        "CustomCodeField", "high",
        "Sole occurrence is CustomCodeField.ParentCustomCodeFieldID — a self-referencing "
        "parent pointer for nested custom lists.",
    ),
    "Email Received Log Record": (
        "EMailReceivedLog", "high",
        "Sole occurrence is LinkEMailReceivedLogDocument.EMailReceivedLogID.",
    ),
}

# Column-name overrides for the polymorphic `Template ID` type, where the column name
# names its own target unambiguously.
TEMPLATE_COLUMN_TARGETS = {
    "BudgetTemplateID": "BudgetTemplate",
    "TaskTemplateID": "TaskTemplate",
    "FolderTemplateID": "FolderTemplate",
    "WorkFlowTemplateID": "WorkFlowTemplate",
    "EntityTemplateID": "EntityTemplate",
    "ProcessTimelineTemplateID": "ProcessTimelineTemplate",
    "BidPackageTemplateID": "BidPackageTemplate",
    "CostTrackingTemplateID": "CostTrackingTemplate",
    "BudgetEntityTemplateID": "EntityTemplate",
    "FolderEntityTemplateID": "EntityTemplate",
    "TaskEntityTemplateID": "EntityTemplate",
    "TaskTemplatePEID": "TaskTemplate",
}


def resolve_fk(target_phrase: str, column: str, by_norm: dict[str, str]):
    """Return (target_object|None, confidence, rationale)."""
    # 1. polymorphic Template ID, disambiguated by column name
    if target_phrase == "Template" and column in TEMPLATE_COLUMN_TARGETS:
        tgt = TEMPLATE_COLUMN_TARGETS[column]
        if tgt in by_norm.values():
            return tgt, "high", f"`Template ID` disambiguated by column name `{column}`."
    # 2. curated alias
    if target_phrase in ALIASES:
        tgt, conf, why = ALIASES[target_phrase]
        if tgt is None:
            return None, conf, why
        return tgt, conf, why
    # 3. exact normalised match against an object name
    hit = by_norm.get(normalise(target_phrase))
    if hit:
        return hit, "high", "Type name matches an object name exactly after normalisation."
    return None, "unresolved", "No object matches this type name and no alias is defined."


# ---------------------------------------------------------------------------
# 3. Module taxonomy
# ---------------------------------------------------------------------------
# Primary module assignment. Exactly one primary module per object; every object below.
# Grounded in (a) the System Administrator Dashboard's own section headings (Observed,
# docs/admin/004), (b) walkHierarchy.jsp's aggregate roots (Observed, docs/admin/009),
# (c) the per-entity explanations in docs/data-fields/INDEX.md.

MODULES: dict[str, dict] = {
    "platform-tenancy": {
        "title": "Platform & Tenancy",
        "what": "The tenant/partition spine and cross-cutting platform plumbing: the Firm (tenant), "
                "the polymorphic ProjectEntity node every business record hangs off, geography and "
                "currency reference data, security, and audit scaffolding.",
        "dashboard_heading": "Company Administration / Data-PS Tools",
        "objects": [
            "Firm", "ProjectEntity", "Project", "Organization", "Region", "GlobalProperty",
            "Security", "UserClassSecurity", "AuditTable", "AuditColumn", "TemplateAudit",
            "EntityTemplate", "ScratchPad", "StateProvinceCountry", "Jurisdiction",
            "ExchangeRate", "MapClientSchedule", "Notify", "LinkRegionManager",
            "LinkMemberProjectEntity", "LinkPEMemberCodeJobTitle",
        ],
    },
    "people-parties": {
        "title": "People & Parties",
        "what": "Everyone the system knows about: internal Members (users), external Persons and "
                "Parties, and Employer records — the single table behind landlords, tenants and "
                "vendors alike (doc 009).",
        "dashboard_heading": "Member Administration",
        "objects": [
            "Member", "MemberAudit", "NonMember", "Person", "Party", "Employer", "EmployerSite",
            "VendorInsurance", "LinkProjectEntityContact", "LinkProjectEntityVendor",
        ],
    },
    "portfolio-transactions": {
        "title": "Portfolio & Real-Estate Transactions",
        "what": "The portfolio/capital-program container above projects, plus deal pipeline: "
                "potential projects, RE transactions, scenarios and comparison reporting.",
        "dashboard_heading": "Portfolio/Capital Program Administration; Portfolio Administration",
        "objects": [
            "Program", "PotentialProject", "RETransaction", "ReTransScenContact",
            "LinkReTransScenContact", "Scenario", "ComparisonReport", "ComparisonItem",
            "DevelopmentPlan", "DevelopmentSlot", "ProgramRevenueWeeks",
        ],
    },
    "facilities-locations": {
        "title": "Facilities, Locations & Sites",
        "what": "The physical estate and the site-selection data around it: Facility, Location, "
                "Complex, Parcel, Space, Parking, plus prototypes, demographics and site surveys.",
        "dashboard_heading": "Portfolio Administration",
        "objects": [
            "Facility", "Location", "Complex", "Parcel", "ParcelAccess", "Space", "Parking",
            "Tenant", "Competitor", "Prototype", "SiteSurvey", "Ownership",
            "LandPurchaseSummary", "LinkLandPurchaseInspection", "DMA", "DemographicFact",
            "DemographicReport", "DemographicResults", "DemographicStudyArea", "FacilityExpense",
        ],
    },
    "contracts-leases": {
        "title": "Contracts & Leases",
        "what": "The Contract aggregate root (570 fields across four physical tables) and the "
                "lease terms hanging off it: amendments, terms, key dates, covenants, co-tenancy, "
                "insurance, security deposits, responsibilities and allowances.",
        "dashboard_heading": "Portfolio Administration",
        "objects": [
            "Contract", "ContractAmendment", "ContractTerm", "ContractFinancialTest", "LeaseInfo",
            "LeaseAudit", "Covenant", "CoTenancy", "Insurance", "SecurityDeposit", "Responsibility",
            "KeyDate", "Allowance", "AllowanceTransaction", "Ownership_placeholder_unused",
        ],
    },
    "accounting": {
        "title": "Lease Accounting & Payments",
        "what": "ASC 842 / IFRS 16 / straight-line schedules, expense setups and their generated "
                "schedules, accruals, escalation indices, and the payment/invoice ledger.",
        "dashboard_heading": "Cost Management",
        "objects": [
            "AccrualTransaction", "AcctingAssumptionAdjust", "AlternateRentSchedule", "SLPeriod",
            "SLSummary", "CodeASC842Schedule", "CodeIFRS16Schedule", "CodeSLSchedule",
            "DiscountRate", "FinancialAdjustment", "RecalcOverrideNotes", "ExpenseSetup",
            "ExpenseSchedule", "ExpenseEscalation", "ExpenseAccrualSetup",
            "ExpenseAccrualSchedule", "ExpenseAllocation", "ExpenseVendorAllocation",
            "CodeExpenseType", "EscalationIndex", "CPI", "FiscalPeriod", "PaymentTransaction",
            "PaymentTransactionFullImport", "PaymentReceipt", "LinkReceiptTransaction",
            "LandlordInvoice", "LandlordInvoiceItem", "LinkLandlordInvPaymentTxn", "InvoiceItem",
            "InvoiceIssue", "PurchaseOrder", "PayApp", "VariableRentOffset", "ScheduledOffset",
            "LinkSchedOffsetExpGrpType", "VirtualExpAccrualForecastPeriod",
            "VirtualExpenseForecastPeriod",
        ],
    },
    "variable-rent": {
        "title": "Variable Rent (Percentage / Use-Based) & Sales",
        "what": "Retail turnover rent: reported sales and usage, breakpoints, exclusions and caps, "
                "and the virtual period projections that price them.",
        "dashboard_heading": "Cost Management",
        "objects": [
            "PercentageRent", "PercentageRentBreakpoint", "UseBasedRent", "UseBasedRentBreakpoint",
            "Sales", "SalesExclusion", "SalesExclusionCap", "Usage", "CodeSalesGroup",
            "CodeSalesType", "VirtualPercentageRentPeriod", "VirtualPRAccrualPeriod",
            "VirtualPRPAggregate", "VirtualSalesPeriod", "VirtualUsagePeriod",
            "VirtualUseBasedRentPeriod", "VirtualUBRPAggregate",
        ],
    },
    "expense-recovery": {
        "title": "Expense Recovery (CAM / Reconciliation)",
        "what": "Landlord operating-expense recovery and CAM reconciliation. Physically remarkable: "
                "ExpenseRecovery is 565 fields split across four PG tables.",
        "dashboard_heading": "Cost Management",
        "objects": ["ExpenseRecovery", "ExpenseRecoveryItem", "ExpenseRecoveryItemMapping"],
    },
    "property-tax": {
        "title": "Property Tax",
        "what": "Assessment, bill, appeal and award tracking for real-property tax.",
        "dashboard_heading": "Cost Management",
        "objects": [
            "PropertyTaxSummary", "PropertyTaxAssessment", "PropertyTaxBill", "PropertyTaxDetail",
            "PropertyTaxAppeal", "PropertyTaxAppealAward",
        ],
    },
    "projects-capital": {
        "title": "Capital Projects & Scheduling",
        "what": "Project delivery: task/schedule networks with predecessors and holiday calendars, "
                "process timelines, change orders, and the issue/RFI loop.",
        "dashboard_heading": "Portfolio/Capital Program Administration",
        "objects": [
            "Task", "TaskGroup", "TaskItem", "TaskPredecessor", "TaskTemplate",
            "TaskTemplateAudit", "LinkTaskDocument", "LinkTaskMember", "LinkTaskByCodeMember",
            "ProcessTimeline", "ProcessTimelineTemplate", "HolidaySchedule", "HolidayDate",
            "ChangeOrder", "Issue", "IssueResponse", "IssueSubmittal",
            "LinkIssuePart", "LinkIssuePartOrder", "CodeIssueType", "CodeProblem",
            "CodeResponsibleParty", "VirtualTemplateSchedule",
        ],
    },
    "assets-equipment": {
        "title": "Assets, Equipment & Maintenance",
        "what": "The asset register and the reactive-maintenance loop: service requests, work "
                "orders and the parts catalogue that feeds them.",
        "dashboard_heading": "Portfolio Administration",
        "objects": [
            "Asset", "AssetHistory", "CodeAssetCategory", "ServiceRequest", "WorkOrder",
            "Part", "PartPackage", "PartPackageItem",
        ],
    },
    # ---- DELIBERATELY OUT OF SCOPE -----------------------------------------
    # User decision, 2026-09-10, relayed via the team lead: Cost Management and
    # Budgeting are out of scope for the ASG Edge+ rebuild. These objects stay in
    # the census and in the FK graph so the edge inventory remains whole, but they
    # get no module analysis, no hub write-up and no mind-map depth.
    "out-of-scope-cost-budget": {
        "title": "Budgeting, Cost Tracking & Bidding — OUT OF SCOPE",
        "what": "Deliberately excluded by user decision (2026-09-10). The budget model, "
                "bid packages and cost-tracking templates. Retained in objects.json / edges.json "
                "and object-catalog.md for census and FK-graph completeness only.",
        "dashboard_heading": "Cost Management (excluded)",
        "in_scope": False,
        "objects": [
            "BudgetColumn", "BudgetColumnItemValue", "BudgetColumnType", "CodeBudgetColumnStatus",
            "BudgetIndex", "BudgetIndexValue", "BudgetLineGroup", "BudgetLineItem",
            "BudgetLineLeaf", "BudgetOption", "BudgetOptionTemplate", "BudgetTemplate",
            "BudgetTemplateAudit", "BudgetView", "LinkBudgetIndexBLI", "LinkBudgetViewBLI",
            "ProFormaBudget", "CostTrackingTemplate", "VirtualTemplateBudget",
            "VirtualTemplateBudgetOption", "BidPackage", "BidPackageAlternate",
            "BidPackageAlternateValue", "BidPackageBreakout", "BidPackageBreakoutValue",
            "BidPackageTemplate", "BidderIssue",
        ],
    },
    "workflow": {
        "title": "Workflow & Approvals",
        "what": "Template-driven approval routing: workflow templates and their steps/actions, "
                "instantiated workflows, and per-step approvers and assignees.",
        "dashboard_heading": "Company Administration",
        "objects": [
            "WorkFlow", "WorkFlowStep", "WorkFlowStepApprover", "WorkFlowStepAssignee",
            "WorkFlowTemplate", "WorkFlowTemplateStep", "WorkFlowTemplateStepAction",
            "WFStepFullImport", "CommitteePackage",
        ],
    },
    "documents-folders": {
        "title": "Documents, Folders & Correspondence",
        "what": "Document storage with a templated folder tree and per-folder security, plus the "
                "inbound/outbound e-mail log.",
        "dashboard_heading": "Folder Administration",
        "objects": [
            "Document", "DocumentMarkup", "Folder", "FolderSecurity", "FolderTemplate",
            "FolderTemplateAudit", "VirtualTemplateFolder", "EMailReceivedLog", "EMailSentLog",
            "LinkEMailReceivedLogDocument",
        ],
    },
    "layouts-forms-reporting": {
        "title": "Configuration, Layouts, Forms & Reporting",
        "what": "The tenant-configurable presentation layer that has a business-object footprint: "
                "custom lists and their extension parts, custom code fields, questions, and report "
                "group metadata. Most of this module's surface (page layouts, data fields, drop "
                "downs) lives OUTSIDE these 223 business objects — see docs/admin/005-008.",
        "dashboard_heading": "Company Administration / Data-PS Tools",
        "objects": [
            "ClientListRow", "CLRExtensionPart", "CustomCodeField", "Question",
            "ReportGroupAvailableField", "ReportGroupData",
        ],
    },
}

# Objects listed above that are placeholders and must be dropped.
MODULES["contracts-leases"]["objects"].remove("Ownership_placeholder_unused")

# Secondary (cross-cutting) module memberships.
SECONDARY: dict[str, list[str]] = {
    "Contract": ["accounting", "variable-rent", "expense-recovery", "property-tax"],
    "ProjectEntity": [m for m in MODULES
                      if m not in ("platform-tenancy", "out-of-scope-cost-budget")],
    "Member": ["platform-tenancy", "workflow", "projects-capital"],
    "Employer": ["accounting", "assets-equipment"],
    "Facility": ["contracts-leases", "assets-equipment", "property-tax"],
    "Location": ["contracts-leases", "portfolio-transactions", "facilities-locations"],
    "Document": ["contracts-leases", "projects-capital", "workflow"],
    "WorkFlow": ["contracts-leases", "projects-capital"],
    "ExpenseSetup": ["contracts-leases", "expense-recovery"],
    "Covenant": ["accounting", "variable-rent"],
    "Asset": ["accounting"],
    "Program": ["platform-tenancy", "projects-capital"],
    "Task": ["workflow", "projects-capital"],
    "Sales": ["accounting"],
    "PaymentTransaction": ["contracts-leases", "expense-recovery", "property-tax"],
}


# ---------------------------------------------------------------------------
# 4. Parse
# ---------------------------------------------------------------------------

def parse_fields(cell: str):
    """Split a FIELDS cell into [(name, type)]. Type = between first '(' and last ')'."""
    out = []
    for raw in cell.split(" | "):
        raw = raw.strip()
        if not raw:
            continue
        i = raw.find("(")
        if i == -1 or not raw.endswith(")"):
            out.append({"name": raw, "type": None, "type_family": "unparsed"})
            continue
        name, typ = raw[:i], raw[i + 1:-1]
        out.append({"name": name, "type": typ, "type_family": type_family(typ)})
    return out


def main() -> int:
    if not SRC.exists():
        print(f"missing source: {SRC}", file=sys.stderr)
        return 1

    rows = SRC.read_text(encoding="utf-8").splitlines()
    header = rows[0].split("\t")
    assert header[:4] == ["LUCERNEX OBJECT", "PG TABLE", "FIELD COUNT", "FIELDS"], header

    objects, by_norm = [], {}
    for line in rows[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        name, table, count = parts[0].strip(), parts[1].strip(), int(parts[2])
        fields = parse_fields(parts[3] if len(parts) > 3 else "")
        tables = [t for t in table.split(",") if t]
        objects.append({
            "object": name,
            "pg_table": table or None,
            "pg_tables": tables,
            "physical_table_count": len(tables),
            "declared_field_count": count,
            "parsed_field_count": len(fields),
            "fields": fields,
        })
        by_norm[normalise(name)] = name

    # --- module assignment ---------------------------------------------------
    primary = {}
    for mod, spec in MODULES.items():
        for obj in spec["objects"]:
            if obj in primary:
                raise SystemExit(f"{obj} assigned to both {primary[obj]} and {mod}")
            primary[obj] = mod

    known = {o["object"] for o in objects}
    missing = sorted(known - set(primary))
    bogus = sorted(set(primary) - known)
    if bogus:
        raise SystemExit(f"module taxonomy names non-existent objects: {bogus}")
    if missing:
        raise SystemExit(f"objects with no primary module: {missing}")

    for o in objects:
        o["primary_module"] = primary[o["object"]]
        o["secondary_modules"] = SECONDARY.get(o["object"], [])

    # --- ProjectEntity scope classification ---------------------------------
    # Three observable signatures in the export:
    #  * ProjectEntity itself                                   -> "supertype"
    #  * carries the inherited supertype column block with
    #    ProjectEntityID typed `Number` (not `Entity ID`)       -> "subtype_root"
    #  * carries ProjectEntityID (or another column) typed
    #    `Entity ID`                                            -> "entity_scoped"
    #  * neither                                                -> "firm_global"
    SUPERTYPE_BLOCK = {"EntityId", "ProjectEntityID", "ProjectEntityName",
                       "ProjectEntityTypeName", "ClientEntityID"}
    for o in objects:
        names = {f["name"]: f for f in o["fields"]}
        has_fk = any(f["type"] == "Entity ID" for f in o["fields"])
        inherited = (SUPERTYPE_BLOCK <= set(names)
                     and names["ProjectEntityID"]["type"] == "Number")
        if o["object"] == "ProjectEntity":
            o["pe_scope"] = "supertype"
        elif inherited:
            o["pe_scope"] = "subtype_root"
        elif has_fk:
            o["pe_scope"] = "entity_scoped"
        else:
            o["pe_scope"] = "firm_global"

    # --- edges ---------------------------------------------------------------
    edges = []
    for o in objects:
        src = o["object"]
        for f in o["fields"]:
            if f["type_family"] != "foreign_key":
                continue
            phrase = FK_RE.match(f["type"]).group("target")
            tgt, conf, why = resolve_fk(phrase, f["name"], by_norm)
            # A column that is its own object's PK is not an edge.
            self_pk = (tgt == src and f["name"] == f"{src}ID")
            if tgt:
                kind = "object"
            elif phrase == "item":
                kind = "external_configuration"
            elif phrase in ("Custom Drop Down", "DashboardComponent"):
                kind = "external_configuration"
            elif phrase == "Template":
                kind = "polymorphic"
            else:
                kind = "unknown"
            edges.append({
                "source_object": src,
                "source_column": f["name"],
                "declared_type": f["type"],
                "target_phrase": phrase,
                "target_object": tgt,
                "target_kind": kind,
                "resolution": conf,
                "rationale": why,
                "self_reference": bool(tgt == src and not self_pk),
                "is_self_pk": self_pk,
                "source_module": o["primary_module"],
                "target_module": primary.get(tgt) if tgt else None,
            })

    # --- degrees -------------------------------------------------------------
    real = [e for e in edges if e["target_object"] and not e["is_self_pk"]]
    in_deg_cols = Counter(e["target_object"] for e in real)
    in_deg_objs = Counter()
    seen = set()
    for e in real:
        k = (e["source_object"], e["target_object"])
        if k not in seen and e["source_object"] != e["target_object"]:
            seen.add(k)
            in_deg_objs[e["target_object"]] += 1
    out_deg_cols = Counter(e["source_object"] for e in real)

    for o in objects:
        n = o["object"]
        o["in_degree_columns"] = in_deg_cols.get(n, 0)
        o["in_degree_objects"] = in_deg_objs.get(n, 0)
        o["out_degree_columns"] = out_deg_cols.get(n, 0)

    # --- module rollup -------------------------------------------------------
    mods_out = {}
    for mod, spec in MODULES.items():
        objs = [o for o in objects if o["primary_module"] == mod]
        names = {o["object"] for o in objs}
        out_e = [e for e in real if e["source_module"] == mod and e["target_module"] != mod]
        in_e = [e for e in real if e["target_module"] == mod and e["source_module"] != mod]
        dep_out = Counter(e["target_module"] for e in out_e if e["target_module"])
        dep_in = Counter(e["source_module"] for e in in_e)
        mods_out[mod] = {
            "module": mod,
            "in_scope": spec.get("in_scope", True),
            "title": spec["title"],
            "what": spec["what"],
            "dashboard_heading": spec["dashboard_heading"],
            "object_count": len(objs),
            "field_count": sum(o["declared_field_count"] for o in objs),
            "objects": sorted(names),
            "internal_edges": len([e for e in real if e["source_module"] == mod
                                   and e["target_module"] == mod]),
            "edges_out": len(out_e),
            "edges_in": len(in_e),
            "depends_on": dict(dep_out.most_common()),
            "depended_on_by": dict(dep_in.most_common()),
        }

    # --- write ---------------------------------------------------------------
    (HERE / "objects.json").write_text(json.dumps(objects, indent=1), encoding="utf-8")
    (HERE / "edges.json").write_text(json.dumps(edges, indent=1), encoding="utf-8")
    (HERE / "modules.json").write_text(json.dumps(mods_out, indent=1), encoding="utf-8")

    # --- report --------------------------------------------------------------
    fams = Counter(f["type_family"] for o in objects for f in o["fields"])
    types = Counter(f["type"] for o in objects for f in o["fields"])
    print(f"objects                     {len(objects)}")
    print(f"declared field total        {sum(o['declared_field_count'] for o in objects)}")
    print(f"parsed field total          {sum(o['parsed_field_count'] for o in objects)}")
    print(f"count mismatches            "
          f"{[o['object'] for o in objects if o['declared_field_count'] != o['parsed_field_count']]}")
    print(f"distinct types              {len(types)}")
    print(f"type families               {dict(fams.most_common())}")
    print(f"objects with empty pg_table {[o['object'] for o in objects if not o['pg_table']]}")
    print(f"objects with >1 pg table    "
          f"{[(o['object'], o['physical_table_count']) for o in objects if o['physical_table_count'] > 1]}")
    print(f"FK-typed columns            {len(edges)}")
    print(f"  self-PK (not edges)       {len([e for e in edges if e['is_self_pk']])}")
    print(f"  resolved edges            {len(real)}")
    print(f"  unresolved                {len([e for e in edges if not e['target_object']])}")
    print(f"  self-referencing edges    {len([e for e in real if e['self_reference']])}")
    print(f"resolution mix              "
          f"{dict(Counter(e['resolution'] for e in edges).most_common())}")
    print(f"unresolved phrases          "
          f"{dict(Counter(e['target_phrase'] for e in edges if not e['target_object']).most_common())}")
    print("\ntop 15 in-degree (distinct source objects):")
    for n, c in in_deg_objs.most_common(15):
        print(f"  {n:<28} {c:>4} objects  {in_deg_cols[n]:>4} columns")
    zero = sorted(o["object"] for o in objects if o["in_degree_objects"] == 0)
    print(f"\nin-degree 0 ({len(zero)}): {zero}")
    print("\npe_scope:", dict(Counter(o["pe_scope"] for o in objects).most_common()))
    print("  subtype_root:", sorted(o["object"] for o in objects if o["pe_scope"] == "subtype_root"))
    print("  firm_global :", sorted(o["object"] for o in objects if o["pe_scope"] == "firm_global"))
    print("\nmodules:")
    for m in sorted(mods_out.values(), key=lambda x: -x["field_count"]):
        print(f"  {m['module']:<26} {m['object_count']:>3} obj  {m['field_count']:>5} fields  "
              f"int={m['internal_edges']:>3} out={m['edges_out']:>4} in={m['edges_in']:>4}"
              f"{'   [OUT OF SCOPE]' if not m['in_scope'] else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
