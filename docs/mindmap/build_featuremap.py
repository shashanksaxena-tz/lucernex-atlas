#!/usr/bin/env python3
"""
Build featuremap.json — ONE mind map of Lx organised by FEATURE.

Design rules (after user review 2026-09-11):
  * Node labels are NAMES, <=22 characters, never sentences. Truncation is a bug.
  * All prose lives in the node's `detail`, shown in the panel when clicked.
  * Feature language, not module language: the areas are written as features a
    delivery lead recognises, deliberately distinct from the schema map's
    module list. The maps stay single-purpose: features here, records there.
  * Numbered rules sit in one collapsed "Rules (N)" folder per area; each rule
    node is named with a short feature-language summary and carries its ID in
    the panel and the link to the full rule page.

Re-runnable: python3 build_featuremap.py   (needs rules.json)
Output feeds build_app.py, which inlines it into the explorer at DATA.feature.
"""

import json
import os
import re

import corpus
import sitenav

HERE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(HERE, "rules.json"), encoding="utf-8") as fh:
    RULES = json.load(fh)

with open(os.path.join(HERE, "questions.json"), encoding="utf-8") as fh:
    QUESTIONS = json.load(fh)

BY_ID = {r["id"]: r for r in RULES["rules"]}

# The feature manuals in docs/features/ are the delivery-facing account of the
# product: what each area settles and what is still open. They are read here so
# the feature map states what those documents state, rather than a paraphrase.
FEATURES = corpus.feature_areas()
SHOTS = corpus.screenshots()
# Where each capture is cited or embedded across the corpus. Strict: an
# unresolvable reference fails this build rather than being skipped quietly.
SHOT_REFS = corpus.shot_references()

# The one join that works between a named surface and a capture. Captures in
# this corpus are named after ADMIN TOOLS and never after layouts, navigation
# screens, workflows or form types — so 32 of the 36 adminTools entries in
# coverage-owners.json resolve, and all 139 entries in the other four buckets
# resolve to nothing. That is a naming convention, not missing evidence: a
# layout with no capture named for it is normal, and its image has to come from
# the citation index instead.
ADMIN_SHOTS, ADMIN_SHOT_MISSES = sitenav.admin_tool_shots(corpus.shot_index())

Q_BY_AREA = {}
for _q in QUESTIONS["questions"]:
    Q_BY_AREA.setdefault(_q["area"], []).append(_q)


def ascii_words(s):
    s = re.sub(r"[^A-Za-z0-9]+", " ", s or "")
    return [w for w in s.split() if w]


def slug(s, maxlen=20):
    out, ln = [], 0
    for w in ascii_words(s):
        if ln + len(w) + (1 if ln else 0) > maxlen:
            break
        out.append(w)
        ln += len(w) + (1 if ln else 0)
    return " ".join(out)


def rule_node(rid, mod):
    """One numbered rule, carrying the rule itself — not just its name.

    A rule node used to render as an id and a short label, which told a reader
    nothing. It now carries the statement, the labelled parts a rule engine
    would consume, what the rule constrains, the confidence the source document
    gave it, and the document to go and check.
    """
    r = BY_ID[rid]
    section = (r.get("section") or "").strip()
    statement = (r.get("statement") or "").strip()

    lines = ["Rule %s%s." % (rid, " — " + section if section else "")]
    if statement:
        lines.append(statement.rstrip(".") + ".")
    for label, body in (r.get("parts") or [])[:6]:
        if label == "Confidence":
            continue
        lines.append("%s: %s" % (label, body.rstrip(".") + "."))
    if r.get("objects"):
        lines.append("Constrains: " + ", ".join(r["objects"][:8]) + ".")
    if r.get("fields"):
        lines.append("Columns named: " + ", ".join(r["fields"][:8]) + ".")
    if r.get("quote"):
        lines.append("Vendor wording: “%s”" % r["quote"])
    if r.get("confNote"):
        lines.append("Confidence: " + r["confNote"].rstrip(".") + ".")
    if r.get("related"):
        lines.append("Cites: " + ", ".join(r["related"]) + ".")
    lines.append("Stated in %s." % r.get("doc", "the module rules"))

    return {
        "name": slug(section) or rid,
        "kind": "rule",
        "rid": rid,
        "detail": " ".join(lines),
        "statement": statement,
        "parts": r.get("parts") or [],
        "objects": r.get("objects") or [],
        "conf": r.get("conf") or "derived",
        "mod": mod,
        "src": "docs/" + r.get("doc", "modules/%s/rules.md" % mod),
    }


QMARK = re.compile(r"^\s*(?:\((?:new|updated|open|answered)\)|[⚠✅❓•*\-–—\d.)\]]+|"
                   r"(?:Q|Question)\s*\d*[:.]?)\s*", re.I)


def q_name(text):
    """A label for an open question: the question, minus the document's markers.

    Corpus questions are written with lead-in markers — "(new)", a warning
    glyph, a list number. Slugging the raw string produced labels like
    "new How does an", which is exactly the empty-label problem in another form.
    """
    s = text
    for _ in range(4):                       # markers stack: "(new) ⚠ 3."
        s2 = QMARK.sub("", s)
        if s2 == s:
            break
        s = s2
    return slug(s, 22) or slug(text, 22) or "Open question"


def question_node(q, mod):
    """One open question, as its own node — the thing somebody has to find out."""
    return {
        "name": q_name(q["q"]),
        "kind": "question",
        "detail": "%s Nobody has confirmed this. Recorded in %s, under the %s area. "
                  "Until it is settled, anything built on the assumption is a guess."
                  % (q["q"].rstrip(".") + ".", q["doc"], q["area"]),
        "conf": "inferred",
        "mod": mod,
        "src": "docs/" + q["doc"],
    }


def questions_group(areas, mod):
    """One folder per feature holding the open questions that block it."""
    qs = []
    for a in areas:
        qs.extend(Q_BY_AREA.get(a, []))
    if not qs:
        return None
    return {
        "name": "Open questions (%d)" % len(qs),
        "kind": "group",
        "detail": "%d things nobody has confirmed for this feature. Each one is work "
                  "somebody has to do before the feature can be rebuilt with confidence; "
                  "they are carried here rather than resolved by guessing. Click one for "
                  "the question and the document that raised it." % len(qs),
        "conf": "inferred",
        "mod": mod,
        "children": [question_node(q, mod) for q in qs[:60]],
    }


def shot_caption(path):
    """What a reader should notice in a capture.

    Preference order: the caption somebody wrote on an embed, then the heading
    the capture is cited under. Captions are long descriptive sentences by
    design, so they belong here and never in a node label.
    """
    ref = SHOT_REFS.get(path) or {}
    for _doc, _head, alt in ref.get("embeds", []):
        if alt:
            return alt
    for _doc, head in ref.get("cites", []):
        if head:
            return head
    return ""


def shot_cited_in(path):
    """The documents that cite or embed a capture — the screen-to-doc mapping."""
    ref = SHOT_REFS.get(path) or {}
    docs = [d for d, _h in ref.get("cites", [])] + [d for d, _h, _a in ref.get("embeds", [])]
    seen, out = set(), []
    for d in docs:
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out


def evidence_node(slugs, shot_dirs, mod):
    """What this feature's claims rest on: documents and captured screens."""
    docs = [FEATURES[s]["doc"] for s in slugs if s in FEATURES]
    shots = [f for d in shot_dirs for f in SHOTS.get(d, [])]
    if not docs and not shots:
        return None
    # Captures showing a real person's name are counted but never handed
    # downstream for rendering: a thumbnail surfaces the name far more
    # prominently than the prose ever did, and the redaction decision is open.
    public = [s for s in shots if not corpus.shot_is_private(s)]
    held = len(shots) - len(public)
    bits = []
    if docs:
        bits.append("Written up in " + ", ".join(docs) + ".")
    if shots:
        bits.append("%d screen captures on disk, under %s — the screens themselves, "
                    "not a description of them."
                    % (len(shots), ", ".join("docs/assets/screenshots/" + d
                                             for d in shot_dirs if SHOTS.get(d))))
        cited = sum(1 for s in shots if SHOT_REFS.get(s))
        bits.append("%d of them are cited by name in the documentation, which is what "
                    "ties a capture to the screen it shows." % cited)
    tools = sorted(n for n, (doc, _sh) in ADMIN_SHOTS.items()
                   if any(d in doc for d in docs)) if docs else []
    if tools:
        bits.append("Admin tools documented here, each with the capture named after it: "
                    + ", ".join(tools[:8])
                    + (" and %d more" % (len(tools) - 8) if len(tools) > 8 else "") + ".")
    if held:
        bits.append("%d are held back from being shown here: they contain a named "
                    "individual, and whether those images get redacted is an open "
                    "decision. They still count as evidence — the file is on disk and "
                    "named in the docs — they are simply not thumbnailed." % held)
    return {
        "name": "Evidence", "kind": "fact", "conf": "observed", "mod": mod,
        "detail": " ".join(bits),
        "src": docs[0] if docs else "docs/assets/screenshots/",
        "shots": public[:24],
        "shotCaps": {s: shot_caption(s) for s in public[:24] if shot_caption(s)},
        "shotsHeld": held,
    }


def feature_doc_nodes(slugs, mod):
    """Turn the feature manuals into nodes: what they settle, and what they cover."""
    out = []
    for s in slugs:
        fa = FEATURES.get(s)
        if not fa:
            continue
        if fa.get("settles"):
            out.append({
                "name": slug(s.replace("-", " ").title(), 24) or "Settled",
                "kind": "fact", "conf": "observed", "mod": mod, "src": "docs/" + fa["doc"],
                "detail": "What the %s manual settles: %s%s"
                          % (s.replace("-", " "), fa["settles"].rstrip(".") + ".",
                             (" Biggest open question: " + fa["question"].rstrip(".") + ".")
                             if fa.get("question") else ""),
            })
        heads = [h for h in corpus.feature_headings(s)
                 if h.lower() not in ("open questions", "conventions", "sources")]
        if heads:
            out.append({
                "name": "Manual contents", "kind": "fact", "conf": "observed", "mod": mod,
                "src": "docs/" + fa["doc"],
                "detail": "The %s manual is organised as: %s. Read it rather than this "
                          "node when you need the detail — this is the index."
                          % (s.replace("-", " "), "; ".join(heads[:14])),
            })
    return out


def rules_group(attach, mod):
    """One collapsed folder holding the area's numbered rules."""
    if not attach:
        return None
    if "prefix" in attach:
        p = attach["prefix"] + "-R-"
        ids = [r["id"] for r in RULES["rules"] if r["id"].startswith(p)]
    elif "mention" in attach:
        m = attach["mention"]
        ids = [r["id"] for r in RULES["rules"]
               if m in (r.get("text") or "") or m in (r.get("section") or "")]
    else:
        ids = attach["ids"]
    ids = [i for i in ids if i in BY_ID]
    if not ids:
        return None
    return {
        "name": "Rules (%d)" % len(ids),
        "kind": "group",
        "detail": "Every numbered rule the docs corpus records for this feature, named "
                  "by a short summary. Click one: the panel opens with its ID, the full "
                  "statement, and a link to the complete rule page.",
        "conf": "derived",
        "mod": mod,
        "children": [rule_node(i, mod) for i in ids],
    }


def node(name, kind, detail, conf="observed", mod=None, key=None, src=None,
         oos=False, children=None, attach=None):
    kids = list(children or [])
    grp = rules_group(attach, mod or key)
    if grp:
        kids.append(grp)
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


def area(key, title, what, children, attach=None, conf="observed", oos=False):
    """A level-1 feature. `key` ties it to the module id for hue + deep links."""
    n = {
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
    if oos:
        n["oos"] = True
    return n


# --------------------------------------------------------------- delivery view
# What turns a schema-shaped area into a delivery-shaped one: who it is for,
# which screens it is used through, which feature manual documents it, which
# screenshot folder evidences it, and which open questions block it. Held as a
# table keyed by area title so the tree above stays readable, and applied in one
# pass after the tree is built.

AREA_SPEC = {
    "ASC 842 Accounting": dict(
        who="Lease accountants and the controller's office. They do not configure anything: "
            "they press Generate Rent or Calculate Schedule on a contract, review what comes "
            "out, and route it for approval. The output is what the auditors see.",
        screens="The contract record's accounting tabs, the schedule review screens, and the "
                "approval steps of the accounting workflow. The engine has no screen of its "
                "own — it is a button on a record.",
        shots=["accounting"],
        qareas=["Lease Accounting & Payments"]),
    "CAM & Expense Recovery": dict(
        who="Lease administrators auditing a landlord's reconciliation, and the analysts who "
            "have to defend the number back to the landlord.",
        screens="The expense-recovery grid on the contract. It is a reconciliation grid, not "
                "a schedule, and it has no schedule layer behind it.",
        qareas=["Contracts & Leases"]),
    "Leases & Contracts": dict(
        who="Lease administrators and abstractors — the people who read an executed lease and "
            "turn it into data. Everything else in the product reads what they enter.",
        screens="The contract record: 15 SEP page layouts and the sub-page sections beneath "
                "them, reached from the Contracts navigation root.",
        shots=["end-user", "bbw-enduser"],
        qareas=["Contracts & Leases"]),
    "Rent & Payments": dict(
        who="Accounts payable and the lease administrators who reconcile what was billed "
            "against what the lease says.",
        screens="Payment Info on the contract, and the invoice list layouts.",
        qareas=[]),
    "Approvals & Workflows": dict(
        who="Everyone who submits a request and everyone who approves one. Routing is by "
            "position — a member, a job title, or ad hoc — not by named person.",
        screens="A different page layout per workflow step, so the same request presents a "
                "different screen to the submitter and to each approver.",
        shots=["workflow", "forms"],
        feat=["workflows-forms"],
        qareas=["Workflow & Approvals", "Approvals & Workflows"]),
    "Forms & Page Layouts": dict(
        who="Configuration administrators. This is the surface on which the product is "
            "assembled, and the one a rebuild has to reproduce most faithfully.",
        screens="Manage Page Layouts and Manage Forms, plus the two JSP renderers that serve "
                "56% of all end-user screens from what those editors produce.",
        shots=["page-layouts", "forms", "bbw-admin", "af-admin"],
        feat=["page-layouts"],
        qareas=["Configuration, Layouts & Forms", "Forms & Page Layouts"]),
    "Smart Field Rules": dict(
        who="Configuration administrators, working inside the layout editor. No developer is "
            "involved, which is the point of the feature and the risk in it.",
        screens="The conditional-rule editor inside a page layout's field properties.",
        shots=["conditional-fields"],
        qareas=[]),
    "Reports & Exports": dict(
        who="Anyone who has to get data out — analysts, auditors, and the integrations that "
            "read the product rather than the database.",
        screens="The report builder, the export tools, and the REST surface.",
        shots=["reporting", "data-model"],
        feat=["import-export", "search-filtering"],
        qareas=["Reporting", "Data model & APIs", "Import & Export", "Search & Filtering"]),
    "Property Tax": dict(
        who="The property-tax team and the outside consultants who file appeals.",
        qareas=["Property Tax"]),
    "Site Selection & Deals": dict(
        who="Real-estate and development teams working a site from prospect to signed deal.",
        qareas=["Portfolio & Real-Estate Transactions"]),
    "Projects & Construction": dict(
        who="Project managers running a build-out against a schedule and a budget.",
        qareas=["Capital Projects & Scheduling"]),
    "Properties & Facilities": dict(
        who="Facilities and portfolio teams — the people who own the physical estate rather "
            "than the paper about it.",
        qareas=["Facilities, Locations & Sites"]),
    "People & Organisation": dict(
        who="Administrators managing who exists in the system and what they may see. Security "
            "is per user class, not per person.",
        shots=["bbw-admin", "af-admin"],
        feat=["security-access"],
        qareas=["People & Parties", "Security & Access"]),
    "Equipment on Contracts": dict(
        who="The teams leasing equipment rather than space — and the accountants, because the "
            "same ASC 842 engine runs over both.",
        screens="BBW's fifth navigation root, 32 nodes. It renders only because BBW holds "
                "equipment-contract records; American Freight's identical configuration does "
                "not render, because it holds none.",
        feat=["equipment-contracts"],
        qareas=["Equipment on Contracts"]),
    "Documents & Files": dict(
        who="Everyone. Documents hang off records, and the folder tree is how they are found.",
        qareas=["Documents, Folders & Correspondence"]),
    "Admin & Tenancy": dict(
        who="Platform and firm administrators. 57 admin tools, and the boundary between what "
            "the vendor owns and what a firm may change runs through all of them.",
        screens="Company Administration and the Data-PS tools.",
        shots=["bbw-admin", "af-admin", "dashboard", "navigation"],
        feat=["administration", "data-fields", "drop-downs-code-tables", "custom-lists",
              "reference-data"],
        qareas=["Platform & Tenancy", "Admin & Tenancy", "Data Fields",
                "Drop Downs & Code Tables", "Custom Lists", "Reference Data",
                "Tenant comparison"]),
    "Required & Validation": dict(
        who="Configuration administrators deciding what a user must fill in, and the "
            "developers who will have to reproduce that decision.",
        screens="The red asterisk in the record renderer, and the required flags in Manage "
                "Data Fields.",
        shots=["data-fields"],
        feat=["required-and-validation"],
        qareas=["Required & Validation"]),
    "Navigation & Screens": dict(
        who="Every user. The navigation tree is the product's front door and it is "
            "platform-seeded, not tenant-authored.",
        screens="141 navigation nodes at BBW, 109 at American Freight, from one seeded tree.",
        shots=["navigation", "dashboard", "end-user"],
        qareas=["Screens & navigation"]),
}


def enrich_areas(tree):
    """Attach the delivery view to each area, from AREA_SPEC and the corpus."""
    touched = 0
    for a in tree:
        spec = AREA_SPEC.get(a["name"])
        if not spec:
            continue
        key = a.get("key") or a.get("mod") or ""
        kids = a.setdefault("children", [])
        head = []
        if spec.get("who"):
            head.append({"name": "Who it is for", "kind": "fact", "conf": "derived",
                         "mod": key, "detail": spec["who"],
                         "src": "docs/features/README.md"})
        if spec.get("screens"):
            head.append({"name": "Where it is used", "kind": "fact", "conf": "observed",
                         "mod": key, "detail": spec["screens"],
                         "src": "docs/data-model/screen-routing.md"})
        kids[:0] = head
        kids.extend(feature_doc_nodes(spec.get("feat", []), key))
        ev = evidence_node(spec.get("feat", []), spec.get("shots", []), key)
        if ev:
            kids.append(ev)
        qg = questions_group(spec.get("qareas", []), key)
        if qg:
            kids.append(qg)
        touched += 1
    return touched


def cap(title, detail, conf="observed", src=None, children=None, attach=None, mod=None,
        oos=False):
    n = {
        "name": title, "kind": "capability", "detail": detail, "conf": conf,
        "src": src or None, "children": children, "attach": attach, "mod": mod,
    }
    if oos:
        n["oos"] = True
    return n


def fact(title, detail, conf="observed", mod=None, src=None):
    return {"name": title, "kind": "fact", "detail": detail, "conf": conf,
            "src": src, "mod": mod}


# ===========================================================================
# The feature tree. Sources: the module documentation corpus in docs/modules/,
# each claim carrying the confidence the docs corpus established for it.
# ===========================================================================

TREE = [
    area("accounting", "ASC 842 Accounting",
         "Lease accounting and compliance. One engine serves three standards - ASC 842, "
         "IFRS 16 and legacy straight-line. There is no separate ASC 842 module: a "
         "Summary/Period record pair (SLSummary, 134 fields; SLPeriod, 79) carries the "
         "schedule, and three mutually exclusive flags say which standard a schedule was "
         "produced under.",
         [
             cap("Classification record",
                 "A separate 93-field record (ContractFinancialTest) runs the five ASC 842 "
                 "classification tests and holds ASC 842 and IFRS 16 results side by side. "
                 "An older ASC 840 Cap Lease Test still sits directly on the lease. One "
                 "field is literally the 90%-test as a formula: initial liability balance "
                 "over threshold fair value - the 'substantially all of the fair value' "
                 "criterion, computed.",
                 src="docs/modules/accounting/asc-842.md + View Object Model"),
             cap("Three term lengths",
                 "Classification uses three different term lengths - contractual, test and "
                 "'likely'. The term used for classification is not necessarily the "
                 "contractual term, because renewal options the lessee is reasonably "
                 "certain to exercise extend it. A rebuild needs all three, not one.",
                 conf="observed", src="docs/modules/contracts/cam-waterfall.md"),
             cap("User-triggered runs",
                 "Schedules are generated by a person pressing a button on the record - "
                 "Generate Rent, Calculate Schedule - not by a batch job. The accounting "
                 "engine is user-triggered. What Generate Rent produces was learned by "
                 "reading the 11,426 transactions this tenant already has, without writing "
                 "to the shared training tenant.",
                 src="docs/screens/014-contract-record-end-user.md"),
             cap("Approved, not published",
                 "Schedule output passes through an approval workflow before anyone relies "
                 "on it: generate, initial review, ASG approve, client approve - three "
                 "steps. A rebuild needs a schedule state machine, not just a calculator.",
                 src="docs/modules/workflow/README.md"),
             cap("Layered discount rate",
                 "Any calculation needing a discount rate resolves in layers: contract "
                 "override first, then rate tables scoped by portfolio / country / state, "
                 "then the portfolio default. The layered fallback is stated as rule "
                 "ACC-R-001.",
                 conf="derived", src="docs/modules/accounting/rules.md"),
             cap("Amortisation switch",
                 "Amortisation has exactly one policy switch with two values: per day or "
                 "per period (GaapAmortizeMode). Day-based versus period-based expense "
                 "recognition is a single tenant-level choice.",
                 src="Live code-table capture"),
             cap("Equipment leases too",
                 "The engine runs on equipment, not just real estate: the classification, "
                 "summary and period records each carry a nullable foreign key to Asset. "
                 "Embedded equipment leases are first-class, not a workaround.",
                 src="docs/modules/assets-equipment/equipment-leases.md"),
             fact("Runs ASC 842 only",
                  "This tenant runs ASC 842 only: the ASC 842 schedule-type table holds "
                  "exactly one value, '842 Rent', and the straight-line and IFRS 16 type "
                  "tables are both empty. The capability is present and unused - whether "
                  "the rebuild needs IFRS 16 at all is a business question, still open."),
             fact("No numeric typing",
                  "In the physical database export, 6,882 of 7,069 non-key columns are "
                  "TEXT - currency and percentages included. There is no numeric typing to "
                  "inherit. The rebuild's constitution already mandates BigDecimal; "
                  "Lx shows what happens without it."),
             fact("Magnitude-typed field",
                  "One accounting field changes meaning by magnitude: it is read as a "
                  "percentage from 0-100 and as currency at 100.01 and above. A genuine "
                  "data-integrity hazard to design out, not inherit.",
                  src="docs/modules/accounting/computed-vs-input-fields.md"),
         ],
         attach={"prefix": "ACC"}),

    area("contracts", "CAM & Expense Recovery",
         "Expense recovery - the CAM reconciliation tenants audit and landlords issue. "
         "This is the product's computational centre of gravity: 379 of the product's 422 "
         "formula fields sit on the single ExpenseRecovery record. The vendor wrote the "
         "entire waterfall into the field labels, so the calculation did not have to be "
         "reverse-engineered.",
         [
             cap("The CAM waterfall",
                 "Sub Total #1 = Controllable + Non-Controllable - Deductions. "
                 "Pass-Through = ST1 + Admin Fee % + Admin Fee + Additions. "
                 "Sub Total #2 = Pass-Through - Recoveries. "
                 "Net Pass-Through = ST2 x Pro Rata Share Rate. "
                 "Net Amount Due = NPT - Pre-Paid. Revised = NAD + Adjustments. "
                 "Every one of those expressions is literally a field label. Observed.",
                 src="docs/modules/contracts/cam-waterfall.md"),
             cap("Grid, not a schedule",
                 "CAM is a reconciliation grid, not a schedule: it has no schedule layer "
                 "and does not follow the four-layer pattern every other money flow uses. "
                 "Treating it as an instance of that pattern would be the single most "
                 "expensive modelling mistake available here. It is a wide grid of stored, "
                 "precomputed figures.",
                 conf="derived", src="docs/modules/contracts/setup-schedule-transaction-pattern.md"),
             cap("Four bases, gross/net",
                 "Every figure exists as Budgeted, Reported, Approved and Prior, each in "
                 "Gross and Net form, and five pairwise variances (Approved-Budgeted, "
                 "Approved-Prior, Budgeted-Prior, Reported-Approved, Reported-Prior) are "
                 "precomputed for every waterfall line. The table is wide because the "
                 "variance grid is fully materialised rather than computed on read. A "
                 "rebuild could store four bases and compute variances on demand - the "
                 "largest single schema simplification available in this product.",
                 src="View Object Model, ExpenseRecovery field labels"),
             cap("Occupancy gross-up",
                 "The gross-up provision - recovering as if the centre were fully occupied "
                 "- applies only on the Approved basis: approved net pass-through "
                 "multiplies by an Occupancy Factor, every other basis uses only the "
                 "pro-rata rate. One formula for all bases gets approved amounts wrong on "
                 "every gross-up lease.",
                 src="Vendor field labels, Observed"),
             cap("NoZeroDef: nullable",
                 "Prior periods are nullable by design: every prior-period field carries "
                 "the suffix NoZeroDef - a prior period that does not exist is unknown, "
                 "not zero. Zero-defaulting would manufacture 100% variances on every "
                 "first-year reconciliation. Recovery measures must be nullable, never "
                 "zero-defaulted.",
                 conf="derived", src="Field-name analysis, CON-R-160"),
             fact("Waterfall gaps",
                  "Three gaps remain: whether Admin Fee % applies to Sub Total #1 or "
                  "something narrower; where the Cap clamps (it has variance fields but "
                  "appears in no labelled formula); and what feeds the Occupancy Factor. "
                  "All tracked as open questions in the corpus."),
         ],
         attach={"ids": ["CON-R-153", "CON-R-154", "CON-R-155", "CON-R-156",
                         "CON-R-157", "CON-R-158", "CON-R-159", "CON-R-160",
                         "CON-R-161"]}),

    area("contracts", "Leases & Contracts",
         "The lease record is the centre of the product: 570 fields across four physical "
         "tables, and 62 other record types point at it. Payment processing, percentage "
         "rent and ASC 842 accounting all sit downstream of it, which is why its schema "
         "freeze gates them.",
         [
             cap("Co-tenancy clauses",
                 "A retail clause family with its own 26-field record: anchor name, "
                 "co-tenancy group and type, occupancy percentage, rent reduction amount "
                 "and percent, and a right-to-terminate flag, linked to the lease and to "
                 "a covenant record, with two code tables governing clause kinds. The "
                 "record is fully tabulated in the corpus; how Lx evaluates the "
                 "clause - what triggers the occupancy test, how the reduction applies, "
                 "what termination unlocks - is documented only in outline and stands as "
                 "an open analysis item. ASG Edge+ BRD-29.",
                 src="data-fields/co-tenancy.md, modules/contracts/percentage-rent.md"),
             cap("The 4-layer pattern",
                 "Every money flow is modelled as four layers: Clause (the negotiated "
                 "term), Schedule (the calculated run of amounts), Transaction (an "
                 "executed payment or charge) and Projection (future expectation). Rent, "
                 "escalations and most financial terms follow it. CAM is the one "
                 "exception - see its own feature.",
                 conf="derived", src="docs/modules/contracts/setup-schedule-transaction-pattern.md"),
             cap("Lifecycle in data",
                 "The lease lifecycle lives in tenant-editable data, not schema: nine "
                 "states - Open, Future Possession, Possession, Paying Rent, Active, two "
                 "Closed variants and two Accounting Purposes Only variants - sit in a "
                 "tenant-authored list. Anyone with drop-down rights can add a tenth. The "
                 "platform's own three-value status field means something different, and "
                 "both are required on the same form.",
                 src="docs/data-model/code-table-registry.md"),
             cap("Self-parenting leases",
                 "A lease can be its own parent: the master-contract field points back at "
                 "leases, carrying the master-lease and sublease hierarchy.",
                 src="_lucernex_objects_summary.txt"),
             cap("Asymmetric relations",
                 "Relationships read differently from each side: from a lease, the "
                 "building is a single related record; from the building, leases appear "
                 "as an embedded child list. The product models the one-to-many direction "
                 "differently from the many-to-one - a rebuild should pick one "
                 "convention.",
                 src="Live screen capture, screen 014"),
             cap("Vendor = Employer",
                 "The payee ('Vendor') is a relabelled Employer: the payment's vendor "
                 "field is declared as an Employer ID. The lease itself has no vendor "
                 "foreign key at all - the payee relationship lives on the payment, not "
                 "the lease.",
                 src="_crossmap.tsv"),
         ],
         attach={"prefix": "CON"}),

    area("contracts", "Rent & Payments",
         "Money that actually moves: generated rent, payment transactions against a "
         "lease, and the invoice records that carry them. Everything here hangs off the "
         "payment record - the lease itself never holds a vendor or a payment.",
         [
             cap("Generate Rent output",
                 "Generate Rent writes payment/charge transactions - this tenant holds "
                 "11,426 of them. The existing output was read instead of pressing the "
                 "button on a shared tenant. Overwrite-versus-duplicate behaviour and "
                 "batch-number storage remain open, needing a disposable lease.",
                 src="docs/modules/contracts/rent-generation.md"),
             cap("Payee on the payment",
                 "The payee lives on the payment, typed as Employer. Payment history also "
                 "enters through a workflow step ('Import Payment History/Sales'), so "
                 "payments arrive both by button and by process.",
                 src="docs/modules/workflow/"),
             cap("Line-item invoices",
                 "Invoices are line-item records, and their totals are the only formulas "
                 "outside the recovery grid and the accounting tests - invoicing computes "
                 "its totals, it does not store them pre-summed.",
                 src="View Object Model, Math field list"),
             cap("Allowances & offsets",
                 "Tenant improvement and other allowances, offset against rent: the "
                 "Allowance, Scheduled Offset and Variable Rent Offset records are "
                 "tabulated field-by-field in the corpus. The posting and offsetting "
                 "behavior - when an offset fires, what it nets against - is not yet "
                 "written up as analysis. ASG Edge+ BRD-22.",
                 conf="derived",
                 src="data-fields/allowance.md, scheduled-offset.md, variable-rent-offset.md"),
             cap("Accrual management",
                 "Expense accruals: Accrual Transaction, Expense Accrual Setup and the "
                 "virtual PR accrual period records are tabulated. Accrual runs, "
                 "reversals and period-close behavior are not yet analyzed. ASG Edge+ "
                 "BRD-23.",
                 conf="derived",
                 src="data-fields/accrual-transaction.md, expense-accrual-setup.md"),
         ],
         attach={"mention": "PaymentTransaction"}),

    area("contracts", "Percentage & Sales Rent",
         "Turnover and use-based rent: 17 record types, 472 fields, documented under the "
         "contracts module because the analysis sat naturally there.",
         [
             cap("Sales feed overage",
                 "Tenant sales are imported, and percentage-rent terms compare sales "
                 "against breakpoints. The record family covers the term, the sales "
                 "periods, and the computed overage.",
                 conf="derived", src="docs/modules/contracts/percentage-rent.md"),
             cap("Sales import step",
                 "The single named entry point for sales data in the observed workflows "
                 "is Lease Admin Request's 'Import Payment History/Sales' step - the "
                 "product has no separate sales module.",
                 src="docs/modules/workflow/README.md"),
         ],
         attach={"mention": "Percentage"}),

    area("workflow", "Approvals & Workflows",
         "The approval machinery. Four workflows are live in this tenant, one per form "
         "type: Lease Admin Request (8 steps), Rent Payment Review/Approval (6), ASC 842 "
         "Schedule Review/Approval (3), and User Request (2). The request is the record; "
         "the workflow is its process; they share a name.",
         [
             cap("BRD-24, already live",
                 "Lease Admin Request is BRD-24, already implemented: Initial Review, "
                 "Abstract Lease Document, ASG Review, Client Review, Import Payment "
                 "History/Sales, Finalize, Finalize (Defaults), Complete. The BRD "
                 "describes what the process should be; this shows what it actually is.",
                 src="docs/modules/workflow/README.md"),
             cap("Per-step layouts",
                 "Each step shows a different screen: a workflow step binds its own page "
                 "layout, so the same request presents a different field surface at "
                 "Submit, at Review and at Approve. That per-step binding is what makes "
                 "the engine expressive enough to run a real business process.",
                 src="Live capture, Manage Work Flows"),
             cap("Position-based routing",
                 "Routing is by position, not by person: approval level is a member, a "
                 "job title, or ad hoc - and the API's assignee enum goes further (all, "
                 "parent, region 1, region 2, market, job title). Notifications walk the "
                 "org chart to three explicit levels, and routing resolves through the "
                 "geographic region hierarchy, not the supervisor chain.",
                 src="docs/modules/workflow/"),
             cap("Four kick-off triggers",
                 "A workflow can start four ways: from a step action, from a page layout, "
                 "on a status change, or from a task. This is the trigger taxonomy any "
                 "rebuilt rule engine has to reproduce.",
                 src="docs/modules/workflow/"),
             cap("Nested state machines",
                 "The module documents three nested state machines: template lifecycle, "
                 "instance lifecycle, and per-step transitions, split cleanly into "
                 "template versus instance.",
                 conf="derived", src="docs/modules/workflow/README.md"),
             fact("No Task steps exist",
                  "No task step exists anywhere in this tenant: all 19 configured steps "
                  "are form steps, though 'add task step' exists in the product. The step "
                  "record has 55 fields and the admin grid surfaces six - most of the "
                  "step model is still unseen."),
             fact("Status home unknown",
                  "Where workflow status lives is unresolved: 'Work Flow Status Code' is "
                  "absent from the catalogue of 207 firm-wide value lists. The nearest "
                  "that exist are approval, last-action and decision status codes."),
         ],
         attach={"prefix": "WF"}),

    area("layouts-and-forms", "Forms & Page Layouts",
         "Configuration of what users see. A page presents a record that already exists. "
         "A form is something else entirely: a tenant-authored request type with one "
         "layout per workflow step. A custom list is a form without the workflow. "
         "Lx never built a form builder; it built one ticket record and let the "
         "tenant define its subtypes.",
         [
             cap("Form = Issue Type",
                 "A form is literally a value in the tenant's request-type list - which "
                 "is why Manage Forms opens the same editor as every admin-controlled "
                 "value list. Every request-shaped feature in the product is the same "
                 "table with a different subtype value.",
                 src="docs/modules/layouts-and-forms/forms-vs-pages-vs-layouts.md"),
             cap("Layouts bound to steps",
                 "Two renderer screens serve 56% of all end-user screens between them - "
                 "the detail and list renderers. The layout is the runtime contract "
                 "between the data model and the screen.",
                 src="docs/data-model/screen-routing.md"),
             cap("One value-list editor",
                 "Everything an admin controls is one editor: 207 platform-fixed value "
                 "lists whose values you may edit but whose catalogue you may not extend, "
                 "plus tenant-authored lists which support cascading values.",
                 src="docs/data-model/code-table-registry.md"),
         ],
         attach={"prefix": "LAY"}),

    area("layouts-and-forms", "Smart Field Rules",
         "The conditional display engine - fields and whole sections that appear, hide "
         "or become required based on rules. The rule engine closest to what ASG Edge+ "
         "calls a rule engine: every field can carry one rule set, read as a sentence: "
         "[Show | Show and Require | Hide] this field when [all | any] of these rules "
         "match.",
         [
             cap("Flat, deliberately",
                 "A flat engine, deliberately: no nesting, no mixed AND/OR. A rule set is "
                 "one flat list evaluated all-or-any. That keeps every rule explicable to "
                 "a business user and indexable by a machine.",
                 src="docs/modules/layouts-and-forms/conditional-fields.md"),
             cap("Typed operators",
                 "Operators depend on the driver's type: list fields get is-in / "
                 "is-not-in; numbers get the six comparisons; checkboxes get selected / "
                 "not selected; all get is-specified / is-not-specified. Text and date "
                 "fields can never drive a rule at all - a deliberate constraint.",
                 src="Live capture, conditional filter editor"),
             cap("Cross-entity drivers",
                 "Rules cross record boundaries: a lease layout offers 85 candidate "
                 "driver fields drawn from four records - lease 65, entity 9, building 7, "
                 "site 4. A lease field can be hidden because of a value on its site "
                 "record.",
                 src="Live capture, conditional filter editor"),
             cap("Opaque JSON storage",
                 "Rules are stored as an opaque JSON blob, one per target field. Cheap to "
                 "write, impossible to query: the product cannot answer 'which layouts "
                 "depend on this drop-down?'. Storing predicates as rows instead would "
                 "give the rebuild a Where-Used answer for free.",
                 conf="derived", src="docs/modules/layouts-and-forms/conditional-fields.md"),
         ]),

    area("reporting", "Reports & Exports",
         "Reporting and data export. Every field-consuming subsystem - reports, forms, "
         "exports - joins to one shared field registry. The vendor's own schema names "
         "the key to it 'Report/Form Field ID': a single type unifying report field and "
         "form field.",
         [
             cap("One field registry",
                 "The report catalogue and the field catalogue are one table, confirmed "
                 "from the schema rather than hypothesised. A rebuilt reporting layer "
                 "needs the same single registry or it will re-implement field metadata "
                 "per consumer.",
                 src="docs/modules/reporting/README.md"),
             cap("Admin tool inventory",
                 "The admin reporting tools are inventoried in the docs: what each "
                 "exposes, and that none of them define calculation logic - computed "
                 "values are all defined at the field level, in the accounting and "
                 "recovery engines.",
                 conf="derived", src="docs/modules/reporting/"),
         ],
         attach={"prefix": "RPT"}),

    area("property-tax", "Property Tax",
         "Out of scope - no approved BRD covers property tax, and ASG does not use this "
         "Lx module. Kept in the corpus so the relationship graph stays whole. "
         "The product models tax as a roll-up: a summary per parcel, assessments under "
         "it, then either a bill (with detail lines) or an appeal (with an award).",
         [
             cap("Assessment roll-up",
                 "Summary, then Assessment, then the branch: the normal path produces "
                 "bills with detail lines; the contested path produces appeals and "
                 "awards. All under the parcel the tax attaches to.",
                 src="docs/modules/property-tax/README.md"),
             cap("Recoverable expense",
                 "Tax is also a recoverable expense: recovery-group and recovery-type "
                 "references tie tax records into the CAM recovery world - property tax "
                 "is modelled as something the landlord can pass through, not just a bill "
                 "someone pays.",
                 src="docs/modules/property-tax/appeals.md"),
             cap("Appeals miss bills",
                 "A won appeal never touches an issued bill: the appeal/award workflow "
                 "documents a gap where an award reducing the tax does not flow back into "
                 "an already-issued bill. The correction loop is manual, and a rebuild "
                 "must decide deliberately whether to keep it that way.",
                 conf="derived", src="docs/modules/property-tax/appeals.md"),
         ],
         attach={"prefix": "TAX"},
         oos=True),

    area("portfolio-transactions", "Site Selection & Deals",
         "Out of scope pending confirmation - no approved BRD covers the deal pipeline; "
         "ASG's BRD-11 Portfolio describes the portfolio view, not site selection. The "
         "pre-lease pipeline exists in the product: portfolios hold deals, deals become "
         "sites, sites are promoted into projects and then facilities. 'Portfolio' on "
         "the menu is one record (Program), proved by the screen routing. Confirm with "
         "the business whether any of it is used before relying on it either way.",
         [
             cap("Promotion pipeline",
                 "The Site-to-Project-to-Facility promotion pipeline is named by two "
                 "layout fields unique to the portfolio record - the layouts used when "
                 "promoting a deal site into a project, and a project into a facility. "
                 "One confirmed foreign key (Project to Facility) closes half the chain.",
                 src="docs/modules/portfolio-transactions/site-pipeline.md"),
             cap("Deals before leases",
                 "Deals are scenarios before they are leases: a site collects deal "
                 "attempts and what-if scenarios, and nothing becomes a lease until the "
                 "pipeline promotes it. The pipeline is the front door of the product.",
                 conf="derived", src="docs/modules/portfolio-transactions/README.md"),
             fact("Invisible to catalog",
                  "The pipeline's records are invisible to the field catalogue: the Site "
                  "record has 108 census fields and zero admin-catalogue rows - the "
                  "starkest of the twelve records the catalogue omits entirely, "
                  "plausibly because pipeline records are not layout-placeable "
                  "(inferred)."),
         ],
         attach={"prefix": "POR"},
         oos=True),

    area("projects-capital", "Projects & Construction",
         "Out of scope - no approved BRD covers capital projects or construction. "
         "Kept in the corpus for graph completeness. The scheduling data is one of the "
         "strangest findings in the product - three byte-identical tables.",
         [
             cap("Identical tables",
                 "Task, TaskGroup and TaskItem are byte-identical tables, and every "
                 "foreign key of that shape in the entire schema resolves to TaskGroup "
                 "alone. The work-breakdown hierarchy and the dependency network are two "
                 "separate graphs drawn over the same rows.",
                 src="docs/modules/projects-capital/scheduling.md"),
             cap("Issue / RFI loop",
                 "Construction issues and RFIs run through the same request record that "
                 "backs forms - the request machinery is shared across the product, not "
                 "duplicated per module.",
                 conf="derived", src="docs/modules/projects-capital/README.md"),
         ],
         attach={"prefix": "PRJ"},
         oos=True),

    area("facilities-locations", "Properties & Facilities",
         "The real estate itself: sites, the buildings on them, and the geography "
         "between. The central naming question of the whole product, settled: the "
         "Location is the site - the 'Center' - and the Facility is the building "
         "standing on it.",
         [
             cap("Location vs Facility",
                 "Location is the site ('Center': address, market, demographics); "
                 "Facility is the physical building on it (GLA, rentable area, floors). "
                 "Leases attach to facilities; the CAM pro-rata share divides by "
                 "rentable area that lives on the facility, not the site.",
                 src="docs/modules/facilities-locations/location-vs-facility-vs-site.md"),
             cap("Site-selection data",
                 "Locations carry the demographics / site-selection data set, which is "
                 "why deal sites and location records share so much shape - the deal "
                 "pipeline is modelled on the site concept.",
                 conf="derived", src="docs/modules/facilities-locations/README.md"),
         ],
         attach={"prefix": "FAC"}),

    area("people-parties", "People & Organisation",
         "People, parties and the org chart. The user record is the most-referenced "
         "record in the schema - 290 foreign keys point at it, more than at the entity "
         "supertype - but 83% of those are just the universal created-by / modified-by "
         "audit pair. Person is a second, unnamed supertype.",
         [
             cap("Person supertype",
                 "There is a second supertype hiding in the schema: Person and NonMember "
                 "are field-for-field identical (37 fields, zero differences); Member is "
                 "Person's 37 plus 44 login and authentication fields. All three share "
                 "PersonID, typed as a plain number rather than a declared foreign-key "
                 "type. Same shared-key inheritance pattern the entity supertype uses, "
                 "applied to people, and nothing names it.",
                 conf="derived", src="docs/modules/people-parties/member-vs-person-vs-party.md"),
             cap("Geographic routing",
                 "The org chart used for routing is geographic: a supervisor chain exists "
                 "on the user record, but the workflow's region-1 / region-2 / market "
                 "routing does not use it - it resolves through the entity's region "
                 "fields plus the region-manager link table. Two different hierarchies; "
                 "routing uses the geographic one.",
                 src="docs/modules/people-parties/README.md"),
             cap("Region people lists",
                 "Regions resolve to people through lists: a region carries a "
                 "self-reference (regions nest), plus manager and member lists pointing "
                 "at users - this is how a region resolves to actual people for workflow "
                 "routing.",
                 conf="observed", src="docs/data-model/reading-the-census.md"),
             cap("Stamps on every write",
                 "Identity sits on nearly every write path: 161 records carry "
                 "modified-by and 79 carry created-by. Any write anywhere must resolve a "
                 "user - arguing for one cross-cutting audit-stamp mechanism in the "
                 "rebuild, not per-service copies.",
                 conf="derived", src="docs/modules/people-parties/README.md"),
         ],
         attach={"prefix": "PPL"}),

    area("assets-equipment", "Equipment on Contracts",
         "Equipment as a leased asset on a contract - in scope via ASG Edge+ BRD-13 "
         "(Equipment Contracts) and BRD-16 (Contract Equipment Accounting). The "
         "maintenance side of the module (service requests and work orders) has no BRD "
         "and is out of scope.",
         [
             cap("Equipment on 842",
                 "Equipment leases run on the accounting engine: the classification, "
                 "summary and period records each carry a nullable foreign key to Asset, "
                 "so embedded equipment leases are classified and scheduled by the same "
                 "engine as real estate.",
                 src="docs/modules/assets-equipment/equipment-leases.md"),
             cap("Request to WorkOrder",
                 "Out of scope - no BRD covers maintenance: the loop is request, triage, "
                 "work order, completion, all variants of the same request record that "
                 "backs forms. Kept here because it shares the module.",
                 conf="derived", oos=True,
                 src="docs/modules/assets-equipment/README.md"),
         ],
         attach={"prefix": "AST"}),

    area("documents-folders", "Documents & Files",
         "Documents and binders: every record root in the product shows Documents and "
         "Binders tabs. The documents half is a real record family; the binders half is "
         "not backed by any single record the census can name with confidence.",
         [
             cap("Documents everywhere",
                 "Document check-in and versioning attach to every record root through "
                 "the entity supertype. Four of the ten document records are near-empty "
                 "stubs - markup content and outbound correspondence are not recoverable "
                 "from this schema.",
                 src="docs/modules/documents-folders/README.md"),
             cap("Binders = CommitteePkg",
                 "Binders: the committee-package record is the best candidate - a "
                 "dedicated screen routes to it from every record root, and both field "
                 "inventories list the record, though they name different single fields "
                 "for it, so neither shows the real table. The earlier 'no record backs "
                 "binders' claim was withdrawn.",
                 conf="derived", src="docs/data-model/reading-the-census.md"),
         ],
         attach={"prefix": "DOC"}),

    area("platform-tenancy", "Admin & Tenancy",
         "The platform underpinnings every feature above stands on: firms (tenants), the "
         "universal entity supertype, value lists, and the API. The two keys are "
         "constantly confused because both appear on nearly every record.",
         [
             cap("FirmID = tenant key",
                 "The firm is the tenant, and its ID is the tenant key - NOT the universal "
                 "entity ID, even though 163 foreign keys point at the entity supertype. "
                 "The tenant key is typed as plain text, not a declared foreign key: the "
                 "one relationship every row has is the one the schema declines to model, "
                 "which is exactly why tenant isolation cannot be enforced by the schema. "
                 "Decisive for database-per-tenant.",
                 src="docs/data-model/project-entity.md"),
             cap("Tenant in the token",
                 "The tenant travels in the login token: the session JWT carries the firm "
                 "name and a cluster claim shaped host:tenant - evidence the platform "
                 "routes each request to a tenant-specific database using a value inside "
                 "the token, not a lookup in a shared table.",
                 src="Live JWT inspection"),
             cap("448 codes, 10 types",
                 "448 field-type codes hide a 10-value system: the API's type enum is "
                 "boolean, computed, date, datetime, foreign key, float, integer, money, "
                 "percentage, string. Computed and foreign-key are first-class types - "
                 "the platform distinguishes engine-calculated values from user input in "
                 "its type system. Money and percentage are distinct from float, and "
                 "BigDecimal is a declared scalar: the vendor reached the same conclusion "
                 "the rebuild's constitution mandates.",
                 src="docs/data-model/graphql-api.md"),
             cap("207 code tables",
                 "One value-list registry, 207 entries: all admin-controlled lists are "
                 "values of a single type discriminator. Master lists - lifecycle states, "
                 "schedule types, workflow statuses - are configuration, not schema.",
                 src="docs/data-model/code-table-registry.md"),
             cap("Read-heavy API",
                 "The API is read-heavy by design: 617 GraphQL queries against 3 "
                 "mutations. The read surface is rich and typed; the write surface is "
                 "not. Whatever writes exist run through a thin REST layer whose endpoint "
                 "shapes never rendered, and remain uncaptured - a standing open item.",
                 src="docs/data-model/graphql-api.md + rest-api.md"),
         ],
         attach={"prefix": "PLT"}),

    area("layouts-and-forms", "Required & Validation",
         "Where the obligation to fill a field in comes from — and the finding that it "
         "does not come from the layout. There is no layout-level required-ness layer: "
         "the red asterisk a user sees in the builder is the schema-required flag "
         "rendered at paint time, not a per-placement setting. Two further obligations "
         "live in the column flag and the catalogue flag, and they disagree on 44 "
         "fields in both directions, so collapsing them into one loses 44 obligations.",
         [
             cap("No layout-level layer",
                 "The asterisk is not stored against the placement. It is the "
                 "schema-required flag, rendered when the field is painted. A rebuild "
                 "that models required-ness as a layout property is modelling something "
                 "that does not exist in the source system.",
                 src="docs/features/required-and-validation/README.md"),
             cap("Two flags, not one",
                 "The column flag and the catalogue flag are two separate obligations. "
                 "They disagree on 44 fields, in both directions. Collapsing them loses "
                 "44 real obligations, so a rebuild has to carry both and decide which "
                 "wins, field by field.",
                 src="docs/features/required-and-validation/README.md"),
             cap("Show and Require, unused",
                 "SHOW_AND_REQUIRE is one of the three conditional actions, and it is "
                 "used zero times across both captured tenants. It exists; nobody has "
                 "chosen it. Worth confirming before it is built.",
                 conf="observed",
                 src="docs/features/required-and-validation/README.md"),
         ]),

    area("platform-tenancy", "Navigation & Screens",
         "The front door. The navigation tree is platform-seeded and identical across "
         "tenants — 109 of 109 nodes at American Freight share their PageLayoutID with "
         "BBW's — and what a firm sees is decided by its data, not by its configuration.",
         [
             cap("Data decides the roots",
                 "A navigation root renders if and only if the firm holds at least one "
                 "record of that ProjectEntityTypeName. Four other candidate gates were "
                 "tested and eliminated: user-class page security, the action-verb list, "
                 "field-level security and the firm feature flags are all open at "
                 "American Freight and the Equipment Contract root still does not render. "
                 "This is the single most consequential navigation fact in the corpus, "
                 "because it means an empty tenant looks like a differently-configured one.",
                 src="docs/features/security-access/README.md"),
             cap("Layouts form a sequence",
                 "PreviousPageLayoutID is a sequence pointer, not a parent link. Layouts "
                 "attached to one navigation node form an ordered chain, and the chains "
                 "cross SEP and LIST modes. The parent link is a different column, "
                 "ParentPageLayoutID.",
                 src="docs/features/page-layouts/README.md"),
             cap("135 layouts, not 93",
                 "Manage Page Layouts shows 93 rows. A further 42 form layouts are "
                 "reachable only through Issue Types and never appear in that list. The "
                 "real population is 135, and an inventory that stops at the admin screen "
                 "is short by a third.",
                 src="docs/features/page-layouts/README.md"),
             fact("Two tiers, one column",
                  "Navigation nodes and firm layouts share the PageLayoutID column and "
                  "never collide: the navigation tier sits in a low, byte-identical band "
                  "across tenants, the firm tier in a high tenant-specific block. A firm "
                  "layout does not replace a navigation screen, it hangs off one — and "
                  "several may hang off the same one.",
                  src="docs/features/page-layouts/README.md"),
         ]),

    # Facts that belong to no single feature and would be lost if filed under
    # one. Generated from corpus.CROSS_FACTS so the map and the documents cannot
    # drift apart: each node quotes a document and names it.
    {
        "name": "What bites a rebuild",
        "kind": "area",
        "key": "cross-cutting",
        "mod": "platform-tenancy",
        "conf": "observed",
        "src": "docs/features/ and docs/tenants/",
        "detail": "The findings that cut across every feature, and that a delivery plan "
                  "gets wrong if it reads only the schema. Each one was established in a "
                  "named document and is repeated here because filing it under a single "
                  "feature would hide it from the features it also governs.",
        "children": [
            {"name": n, "kind": "fact", "conf": c, "mod": "platform-tenancy",
             "src": "docs/" + s, "detail": corpus.debrand(t.rstrip(".") + ". " + d)}
            for n, t, d, c, s in corpus.CROSS_FACTS
        ],
    },

    {
        "name": "Cost & Bidding (out)",
        "kind": "area",
        "detail": "Out of scope by decision: cost management, budgeting and bidding are "
                  "excluded from the rebuild. Kept in the corpus so the relationship "
                  "graph stays whole - records like the budget-option template (107 "
                  "census fields, zero catalogue rows) live here with one-line "
                  "descriptions only. Drawn dashed, like the schema map's excluded "
                  "modules.",
        "conf": "observed",
        "oos": True,
        "children": [
            {"name": "Why excluded", "kind": "fact", "conf": "observed",
             "detail": "Cost management, budgeting and bidding are out of scope by "
                       "decision for ASG Edge+. They remain catalogued so that impact "
                       "analysis through the relationship graph is never silently wrong "
                       "at the boundaries."},
        ],
    },
]


def strip(n):
    """Drop None-valued keys so the JSON carries only what is set."""
    if isinstance(n, dict):
        return {k: strip(v) for k, v in n.items() if v is not None}
    if isinstance(n, list):
        return [strip(c) for c in n]
    return n


def count(n):
    return 1 + sum(count(c) for c in n.get("children") or [])


def apply_attach(n, parent_mod=None):
    """Walk the built tree; any node carrying an `attach` spec gets its numbered
    rules folded into one Rules folder as its last child."""
    mod = n.get("mod") or parent_mod
    for c in n.get("children") or []:
        apply_attach(c, mod)
    at = n.pop("attach", None)
    if at:
        grp = rules_group(at, mod)
        if grp:
            n.setdefault("children", []).append(grp)


enriched_areas = enrich_areas(TREE)

for _a in TREE:
    apply_attach(_a)

root_children = [strip(a) for a in TREE]
total = count({"children": root_children})

# Guard the design rule: labels are names, not sentences.
LONG = [(n["name"], len(n["name"])) for n in []
        if False]


def walk_labels(n, out):
    out.append((n["kind"], n["name"]))
    for c in n.get("children") or []:
        walk_labels(c, out)


labels = []
for _a in root_children:
    walk_labels(_a, labels)
bad = [(k, nm, len(nm)) for k, nm in labels
       if k not in ("rule", "question") and len(nm) > 24]
if bad:
    raise SystemExit("labels over 24 chars: %s" % bad)
rule_long = [(nm, len(nm)) for k, nm in labels
             if k in ("rule", "question") and len(nm) > 24]
if rule_long:
    raise SystemExit("rule labels over 22 chars: %s" % rule_long[:5])

out = {
    "meta": {
        "name": "Lx - the product by feature",
        "detail": "One map organised by what the product DOES, not by database table. "
                  "Node names are short on purpose: click any node and the panel on the "
                  "right opens with the full explanation, the evidence label, and links "
                  "to the underlying documentation. Rule nodes sit in each feature's "
                  "Rules folder and open the full numbered rule. Areas ASG does not use "
                  "- no approved BRD covers them - are drawn dashed, like the excluded "
                  "cost and budgeting feature.",
        "conf": "observed",
        "src": "docs/modules/ corpus, captured from the live tenant 2026-09-10/11",
        "areas": len(root_children),
        "nodes": total,
        "rules": RULES["total"],
    },
    "root": {"name": "Lx", "kind": "product", "children": root_children},
}

with open(os.path.join(HERE, "featuremap.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, separators=(",", ":"), sort_keys=False)

print("wrote featuremap.json: %d areas, %d nodes total, %d rules attached"
      % (len(root_children), total, RULES["total"]))
print("label check passed: every label <=24 chars")
print("delivery view attached to %d of %d areas" % (enriched_areas, len(root_children)))
