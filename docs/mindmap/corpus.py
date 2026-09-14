#!/usr/bin/env python3
"""
Shared reader for the documentation corpus.

Every generator in this folder used to invent its own node text. That is why the
maps rendered as labels with nothing behind them: the prose existed, in
`docs/data-fields/`, `docs/modules/`, `docs/features/` and the tenant captures,
but nothing wired it into the map data.

This module is the wire. It parses the corpus once, exposes it as plain Python
dictionaries, and the build scripts compose node text from it. Nothing here
invents a fact: every function returns text that exists in a document, plus the
path it came from so the reader can go and check.

Read-only. Imported by build_mapdata.py, build_rules.py, build_featuremap.py
and build_site.py.
"""

import csv
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)

# The product name is withheld from user-visible prose. Technical identifiers
# (LxRetail, lxID, table and column names) are code and are left alone; this
# only rewrites the branding word when it appears as running text.
#
# The lookahead protects DATA, not branding. `Lucernex Change Request` is the
# name of a workflow template in the tenant's own records — it is what a user
# reads on the Manage Work Flows screen — so rewriting it would make the map
# disagree with the product. Same reasoning as leaving `IsLucernexAdministrator`
# alone: a value a user can see is evidence, not a brand mention.
BRAND = re.compile(r"\bLucernex\b(?!\s+Change Request\b)")

# Tenant-data strings that contain the vendor name and must survive verbatim.
# Kept as a list so the next one is a one-line addition rather than a new regex.
BRAND_EXEMPT = ("Lucernex Change Request",)


def debrand(s):
    """Replace the vendor product name with `Lx` in prose, leaving data alone."""
    if not s:
        return s
    # collapse the two-word product names first, so they do not become "Lx IWMS"
    s = s.replace("Lucernex IWMS", "Lx").replace("Lucernex Atlas", "Lx Atlas")
    return BRAND.sub("Lx", s)


def _read(rel):
    p = os.path.join(DOCS, rel)
    if not os.path.exists(p):
        return ""
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def _clean(s):
    """Markdown down to readable prose, keeping identifiers legible."""
    # whitespace first: the emphasis patterns are single-line, and a bold run
    # that wraps across a newline in the source would otherwise survive
    s = re.sub(r"\s+", " ", s or "")
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", s)
    s = s.replace("`", "")
    s = s.replace("&nbsp;", " ").replace("&middot;", "·").replace("&mdash;", "—")
    return debrand(re.sub(r"\s+", " ", s).strip())


# --------------------------------------------------------------------- fields
# docs/data-fields/all-fields.csv — every one of the 6,158 catalogued Data
# Fields, with the label a user actually sees, its scope (Global = platform,
# Firm = this tenant's own) and whether the catalogue marks it required.

def field_catalog():
    """{(Entity, InternalName): {label, type, scope, required, readonly, default}}"""
    out = {}
    p = os.path.join(DOCS, "data-fields", "all-fields.csv")
    if not os.path.exists(p):
        return out
    with open(p, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            out[(r["Entity"], r["InternalName"])] = {
                "label": r.get("Label", "").strip(),
                "type": r.get("FieldType", "").strip(),
                "scope": r.get("Scope", "").strip(),
                "required": (r.get("Required", "").strip().lower() == "yes"),
                "readonly": (r.get("ReadOnly", "").strip().lower() == "yes"),
                "default": r.get("Default", "").strip(),
            }
    return out


# --------------------------------------------------------- the field inventory
# docs/data-model/pg/bbw-field-inventory.csv — 7,368 rows, 222 objects, of which
# 6,091 carry a real prose Definition written by the vendor. This is the single
# best per-FIELD source in the corpus: the Data Fields catalogue says what a
# field is called, this says what it is FOR.
#
# It also carries the physical mapping (PG table, column, type) and a Key Role
# per field. Read the caveat on `PG Table Status` in object_inventory() before
# putting anything from that column on a node.

INVENTORY = "data-model/pg/bbw-field-inventory.csv"

# Key Role, shortened for the node data. The long strings are the CSV's own.
KEY_ROLE = {
    "Foreign key (ID reference)": ("fk", "a foreign key — an ID reference to another record"),
    "Primary key": ("pk", "the record's primary key"),
    "Parent key": ("parent", "the key to this record's parent"),
    "Audit": ("audit", "audit metadata — who touched the row and when"),
    "Incremental watermark": ("watermark",
                              "an incremental watermark: the column a replication loader reads "
                              "to find rows changed since its last run"),
    "Client identifier": ("client",
                          "a client identifier — the id a migrated record carried in the system "
                          "it came from, which is what makes an import an upsert rather than an "
                          "insert"),
}


def field_inventory():
    """{(Object, Field): {...}} — the vendor's own definition of nearly every field."""
    out = {}
    p = os.path.join(DOCS, INVENTORY)
    if not os.path.exists(p):
        return out
    with open(p, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            obj = (r.get("Lucernex Object") or "").strip()
            fld = (r.get("Lucernex Field Name") or "").strip()
            if not obj or not fld:
                continue
            role = KEY_ROLE.get((r.get("Key Role") or "").strip(), ("", ""))
            out[(obj, fld)] = {
                "label": (r.get("UI Label") or "").strip(),
                "type": (r.get("Lucernex Data Type") or "").strip(),
                "required": (r.get("Required") or "").strip().lower() == "required",
                "max": (r.get("Max Size") or "").strip(),
                "functional": (r.get("Functional Field") or "").strip(),
                "definition": debrand(re.sub(r"\s+", " ", (r.get("Definition") or "").strip())),
                "extracted": (r.get("Extracted to PostgreSQL") or "").strip().lower() == "yes",
                "pgdb": (r.get("PG Database") or "").strip(),
                "pgtable": (r.get("PG Table") or "").strip(),
                "pgstatus": (r.get("PG Table Status") or "").strip(),
                "pgcol": (r.get("PG Column") or "").strip(),
                "pgtype": (r.get("PG Data Type") or "").strip(),
                "role": role[0],
                "roleText": role[1],
                "notes": debrand(re.sub(r"\s+", " ", (r.get("Notes") or "").strip())),
            }
    return out


def object_inventory(by_field=None):
    """Per-object rollup of the field inventory.

    CAVEAT, and it must survive into anything written from this. `PG Table
    Status` describes the coverage of ONE replication loader targeting ONE
    database (`lxr_drp_bbw`). It is NOT a statement about the product's schema.
    The tell is `project_entity`: 107 fields, every one marked extracted, table
    never created — yet it is the universal supertype and the tenant holds 2,014
    contracts, so it cannot be empty. The loader simply does not produce it.
    Anything surfaced from this column is labelled replication coverage and
    marked Observed *of the loader*.
    """
    by_field = by_field if by_field is not None else field_inventory()
    out = {}
    for (obj, fld), r in by_field.items():
        o = out.setdefault(obj, {
            "fields": 0, "defined": 0, "required": 0, "functional": 0,
            "notExtracted": 0, "roles": {}, "tables": {}, "db": set(),
            "status": {}, "notes": {},
        })
        o["fields"] += 1
        if r["definition"]:
            o["defined"] += 1
        if r["required"]:
            o["required"] += 1
        if r["functional"] == "Yes":
            o["functional"] += 1
        if not r["extracted"]:
            o["notExtracted"] += 1
        if r["role"]:
            o["roles"][r["role"]] = o["roles"].get(r["role"], 0) + 1
        if r["pgtable"]:
            o["tables"][r["pgtable"]] = o["tables"].get(r["pgtable"], 0) + 1
        if r["pgdb"]:
            o["db"].add(r["pgdb"])
        if r["pgstatus"]:
            o["status"][r["pgstatus"]] = o["status"].get(r["pgstatus"], 0) + 1
        if r["notes"]:
            o["notes"][r["notes"]] = o["notes"].get(r["notes"], 0) + 1
    for o in out.values():
        o["db"] = sorted(o["db"])
        o["tables"] = sorted(o["tables"], key=lambda t: -o["tables"][t])
    return out


FIELD_TYPE_LEGEND_RE = re.compile(
    r"^\|\s*`(s(?:TYPE|CODE)_[A-Z0-9_]+)`\s*\|[^|]*\|[^|]*\|[^|]*\|\s*(.+?)\s*\|\s*$")


def field_type_legend():
    """{sTYPE_MONEY: 'A money amount...'} from the INDEX.md legend table."""
    out = {}
    for line in _read("data-fields/INDEX.md").split("\n"):
        m = FIELD_TYPE_LEGEND_RE.match(line)
        if m:
            out[m.group(1)] = _clean(m.group(2))
    return out


# ------------------------------------------------------------------- entities
# docs/data-fields/INDEX.md carries one row per Table Association with a
# multi-sentence explanation of what the record is and why it is shaped that
# way. That column is the single best per-entity prose in the corpus.

ENTITY_ROW_RE = re.compile(
    r"^\|\s*`([A-Za-z0-9_]+)`\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|\s*([\d,]+)\s*\|"
    r"\s*(.*?)\s*\|\s*(.+?)\s*\|\s*$")


def entity_notes():
    """{ObjectName: {blurb, total, global, firm, doc}} from the Data Fields catalogue."""
    out = {}
    for line in _read("data-fields/INDEX.md").split("\n"):
        m = ENTITY_ROW_RE.match(line)
        if not m:
            continue
        name, total, glob, firm, detail_cell, blurb = m.groups()
        link = re.search(r"\(([^)]+\.md)\)", detail_cell or "")
        out[name] = {
            "blurb": _clean(blurb),
            "total": int(total.replace(",", "")),
            "global": int(glob.replace(",", "")),
            "firm": int(firm.replace(",", "")),
            "doc": "data-fields/" + link.group(1) if link else "data-fields/INDEX.md",
        }
    return out


def entity_leads():
    """{ObjectName: (lead paragraph, source doc)} from each docs/data-fields/*.md.

    The per-entity files open with a paragraph that often says more than the
    INDEX row — notably about Virtual records and computed projections.
    """
    out = {}
    folder = os.path.join(DOCS, "data-fields")
    if not os.path.isdir(folder):
        return out
    for fn in sorted(os.listdir(folder)):
        if not fn.endswith(".md") or fn == "INDEX.md":
            continue
        raw = _read("data-fields/" + fn)
        assoc = re.search(r"\*\*Table Association:\*\*\s*`([A-Za-z0-9_]+)`", raw)
        if not assoc:
            continue
        para = []
        for line in raw.split("\n")[1:]:
            if line.startswith("**Table Association"):
                break
            if line.strip():
                para.append(line.strip())
            elif para:
                break
        if para:
            out[assoc.group(1)] = (_clean(" ".join(para)), "data-fields/" + fn)
    return out


# ------------------------------------------------------------- feature corpus
# docs/features/README.md holds a table of written feature areas: what each one
# settles, and its biggest open question. That is exactly the delivery-facing
# framing the feature map wants, already written down.

FEATURE_ROW_RE = re.compile(
    r"^\|\s*\[\*\*([a-z0-9-]+)\*\*\]\(([^)]+)\)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")


def feature_areas():
    """{slug: {settles, question, doc}} from docs/features/README.md."""
    out = {}
    for line in _read("features/README.md").split("\n"):
        m = FEATURE_ROW_RE.match(line)
        if m:
            slug, link, settles, question = m.groups()
            out[slug] = {
                "settles": _clean(settles),
                "question": _clean(question),
                "doc": "features/%s/README.md" % slug,
            }
    return out


def feature_stated_up_front(slug):
    """The 'Stated up front' paragraph a feature README opens with."""
    raw = _read("features/%s/README.md" % slug)
    m = re.search(r"\*\*Stated up front\.?\*\*(.+?)(?:\n\n|\n\|)", raw, re.S)
    return _clean(m.group(1)) if m else ""


def feature_headings(slug):
    """Second-level headings of a feature README — its table of contents."""
    raw = _read("features/%s/README.md" % slug)
    return [_clean(h) for h in re.findall(r"^##\s+(.+)$", raw, re.M)]


# ---------------------------------------------------------------- screenshots

# The walk and the slug below are deliberately the same join that
# docs/tools/build_coverage.py uses (its screenshots section), so the maps, the
# coverage scoreboard and the docs all key off ONE resolver rather than three.
# Two rules that a naive glob gets wrong, both learned the hard way:
#   * captures are .jpg AND .png — globbing *.png loses about 60% of them,
#     including every bbw-admin, af-admin and bbw-enduser capture;
#   * there are non-image files under the tree (.omc state), so any path
#     component starting with "." is skipped.
# Filenames are unstable and directory names are stable: bbw-admin was
# renumbered from 56 files to 55 when one capture was withdrawn, shifting every
# index above 52. Never key off the numeric prefix.

SHOT_EXT = (".png", ".jpg", ".jpeg")

# Captures showing a real person's name, held back from being embedded until the
# lead answers whether the images get redacted. They are still counted and named
# as evidence — a filename is not a name — but the maps do not render them, and
# a thumbnail would surface the name more prominently than the prose ever did.
# Remove an entry here once its image is cleared or redacted.
SHOT_PRIVATE_AREAS = ("bbw-enduser",)
SHOT_PRIVATE_FILES = ("bbw-admin/15-job-log.jpg",)


def _shot_slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def shot_paths():
    """Every capture, as a path relative to docs/."""
    base = os.path.join(DOCS, "assets", "screenshots")
    out = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            if fn.lower().endswith(SHOT_EXT):
                out.append(os.path.relpath(os.path.join(dirpath, fn), DOCS)
                           .replace(os.sep, "/"))
    return sorted(out)


def screenshots():
    """{area: [relative paths]} under docs/assets/screenshots/.

    Two area directories are empty (reporting, bbw); they resolve to no entry,
    which is correct rather than a bug.
    """
    out = {}
    for p in shot_paths():
        out.setdefault(p.split("/")[2], []).append(p)
    return out


def shot_index():
    """{de-numbered basename slug: [paths]} — build_coverage.py's own join."""
    out = {}
    for s in shot_paths():
        base = os.path.splitext(os.path.basename(s))[0]
        base = re.sub(r"^\d+-", "", base)     # bbw-admin/01-manage-company.jpg
        out.setdefault(_shot_slug(base), []).append(s)
    return out


def shot_for(name, index=None):
    """Resolve a surface name to the captures that show it."""
    return (index if index is not None else shot_index()).get(_shot_slug(name), [])


CITE_RE_TMPL = r"`((?:%s)/[A-Za-z0-9._-]+\.(?:jpg|jpeg|png))`"
EMBED_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+\.(?:jpg|jpeg|png))\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def shot_references(strict=True):
    """Where each capture is cited or embedded across the corpus.

    Two forms, and the first is much the larger:
      * `area/file.jpg` path citations — the convention CONVENTIONS.md mandates,
        237 of them, and the densest screenshot-to-surface mapping there is;
      * ![alt](path) embeds, 79 of them, which carry a written caption.

    Returns {path: {"cites": [(doc, heading)], "embeds": [(doc, heading, alt)]}}.

    `strict` makes an unresolvable citation fail the build. It is on by default
    because silence is how three citations to withdrawn files survived a renumber
    of bbw-admin: a resolver that skips quietly cannot tell you it skipped.
    """
    known = set(shot_paths())
    areas = sorted({p.split("/")[2] for p in known})
    if not areas:
        return {}
    cite_re = re.compile(CITE_RE_TMPL % "|".join(areas))

    out, broken = {}, []
    for dirpath, dirnames, filenames in os.walk(DOCS):
        dirnames[:] = [d for d in dirnames
                       if not d.startswith(".") and d not in ("site", "assets")]
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, DOCS).replace(os.sep, "/")
            heading = ""
            for line in open(path, encoding="utf-8"):
                h = HEADING_RE.match(line)
                if h:
                    heading = _clean(h.group(2))
                    continue
                for frag in cite_re.findall(line):
                    full = "assets/screenshots/" + frag
                    if full not in known:
                        broken.append((rel, frag))
                        continue
                    out.setdefault(full, {"cites": [], "embeds": []})
                    out[full]["cites"].append((rel, heading))
                for alt, src in EMBED_RE.findall(line):
                    full = os.path.normpath(
                        os.path.join(os.path.dirname(rel), src)).replace(os.sep, "/")
                    if full not in known:
                        broken.append((rel, src))
                        continue
                    out.setdefault(full, {"cites": [], "embeds": []})
                    out[full]["embeds"].append((rel, heading, _clean(alt)))
    if broken and strict:
        raise SystemExit(
            "screenshot references that resolve to no file (%d).\n"
            "Fix the citation or restore the capture — do not silence this:\n%s"
            % (len(broken), "\n".join("  %s -> %s" % b for b in broken)))
    return out


def shot_is_private(path):
    """True while a capture is held back pending the name-redaction decision."""
    return (path.split("/")[2] in SHOT_PRIVATE_AREAS
            or path.split("assets/screenshots/")[-1] in SHOT_PRIVATE_FILES)


# -------------------------------------------------------------- module README

def module_headline(mod):
    """The opening paragraph of a module README, as one-sentence context."""
    raw = _read("modules/%s/README.md" % mod)
    for para in raw.split("\n\n")[1:4]:
        t = _clean(para)
        if t and not t.startswith("|") and len(t) > 60:
            return t
    return ""


# ------------------------------------------------------------------- doc facts
# A small set of cross-cutting facts that the maps must carry and that no single
# generator owns. Each is quoted from a document and cites it, so the map never
# states one of these on its own authority.

# (short name for a node label, headline, explanation, confidence, source doc)
CROSS_FACTS = [
    ("Data gates the roots",
     "Navigation roots are gated by data, not by permission",
     "A navigation root renders if and only if the firm holds at least one record of that "
     "ProjectEntityTypeName. Four other candidate gates — user-class page security, the "
     "action-verb list, field-level security and the firm feature flags — were each tested "
     "and eliminated: all three security gates are open at American Freight and the "
     "Equipment Contract root still does not render.",
     "observed", "features/security-access/README.md"),
    ("No layout-level required",
     "Required-ness has no layout-level layer",
     "The red asterisk a user sees in the builder is the schema-required flag rendered at "
     "paint time, not a per-placement setting stored against the layout. Show and Require "
     "exists as a conditional action and is used zero times in either tenant.",
     "observed", "features/required-and-validation/README.md"),
    ("Layouts are a sequence",
     "PreviousPageLayoutID is a sequence pointer",
     "Layouts attached to one navigation node form an ordered chain through "
     "PreviousPageLayoutID, and the chains cross SEP and LIST modes. It is a sequence, not "
     "a parent link — the parent link is ParentPageLayoutID, which is a separate column.",
     "observed", "features/page-layouts/README.md"),
    ("135 layouts, not 93",
     "135 layouts, not 93",
     "Manage Page Layouts lists 93 rows, but 42 further form layouts are reachable only "
     "through Issue Types. The real layout population is 135.",
     "observed", "features/page-layouts/README.md"),
    ("Rules in opaque JSON",
     "Conditional field rules live in JSONConfigText",
     "Conditional display rules are stored as an opaque JSON blob in "
     "PageLayoutField.JSONConfigText. Eight layouts carry 50 such records. The comparison "
     "value crtVal1 stores the display label, not the underlying id — so a rule breaks "
     "silently when somebody renames a drop-down value.",
     "observed", "modules/layouts-and-forms/conditional-fields.md"),
    ("Custom fields are DDL",
     "Firm custom fields are physical columns",
     "A firm custom field is a physical Firm_-prefixed column on the table, not a row in a "
     "value store. Adding one is a DDL change. That is direct evidence for "
     "database-per-tenant and against a shared schema.",
     "observed", "features/data-fields/README.md"),
    ("Three publish tiers",
     "Configuration publishes along three tiers",
     "Configuration moves platform to firm to firm, and only the vendor's own tier is "
     "versioned. Import clones the configuration and discards its lineage, so a tenant "
     "cannot be told which version of a template it is running.",
     "derived", "tenants/bbw-vs-american-freight.md"),
    ("200 is not success",
     "HTTP 200 does not mean the write succeeded",
     "The REST surface is fully CRUD, but writes return an ImportResults envelope: the "
     "transport status is 200 while the envelope reports the failure. Any client must read "
     "the envelope, not the status code.",
     "observed", "data-model/rest-api.md"),
    ("No Equipment table",
     "EquipmentContract has no table",
     "There is no EquipmentContract table in any inventory. Equipment contracts are "
     "Contract rows discriminated by ProjectEntityTypeName = \"Equipment Contract\" — with "
     "a space in the value.",
     "observed", "features/equipment-contracts/README.md"),
    ("Discount rates empty",
     "The discount-rate table is empty in both tenants",
     "The reference table that should supply the ASC 842 discount rate holds zero rows in "
     "both captured tenants, while the accounting engine runs. Where the rate actually "
     "comes from is unresolved, and it blocks the accounting rebuild.",
     "observed", "features/reference-data/README.md"),
    ("Versions are a suffix",
     "Workflow versioning is a naming convention, not a feature",
     "The live template is the unsuffixed one. A v1 or v2 suffix marks a superseded "
     "template, not a successive version, and the fact that it was archived is recorded "
     "only as free text in the grid's Description column — \"Archived and replaced with new "
     "workflow on 10.02.25\". There is no version field, so nothing can order them. This "
     "settles which Lease Admin Request is live, and the same holds for Lucernex Change "
     "Request.",
     "observed", "features/workflows-forms/README.md"),
    ("Fields are documented",
     "6,091 fields carry the vendor's own definition",
     "The field inventory explains what nearly every field is FOR, in the vendor's words — "
     "not what it is called or how it is typed, which is all the other readings give. Six "
     "thousand of the 7,421 fields in the census now resolve to a definition, and every "
     "field node in the schema map leads with it. Read the provenance note before citing it "
     "alongside the census: it is the same export, read more sharply — not a second witness.",
     "observed", "data-model/pg/bbw-field-inventory.csv"),
    ("One export, two readings",
     "The inventory and the object census are the same source",
     "222 of 223 objects and 7,273 of roughly 7,400 fields are common to both, with the same "
     "Firm_ names present and the same CRL_ names absent. The field inventory is a sharper "
     "reading of the export the object census already came from, not an independent "
     "corroboration of it. Treating it as a second witness is how one silence becomes two "
     "confident citations — so where the two agree, that is one fact stated twice.",
     "observed", "data-model/pg/bbw-field-inventory.csv"),
    ("Required: owner FKs",
     "Required-ness disagrees on 43 fields, and they are one coherent class",
     "Joined on the 5,768 fields BOTH captures actually contain, the Data Fields catalogue "
     "and the field inventory agree on 5,725 — 99.3%. The 43 that differ all run the same "
     "way, catalogue-required and inventory-not, and they are 34 ContractID, 8 "
     "ProjectEntityID and 1 ShortName across 41 record types: the owner foreign key, the "
     "parent link the application demands and the database permits to be null. Parenthood "
     "is enforced by the application, not by the schema. Three captures made three "
     "different ways give three totals — 603 from the schema viewer, 637 from the Manage "
     "Data Fields screen, 606 from the object export — and the same structural signature "
     "every time. Never compare those three totals: they cover different populations. The "
     "signature is what is corroborated, not any one number.",
     "observed", "features/required-and-validation/README.md"),
    ("Absence is not denial",
     "A field missing from a capture is not that capture saying \"not required\"",
     "Establish that both captures contain a field before claiming they disagree about it, "
     "and state the joined denominator before stating a difference. Comparing the two "
     "required-ness sets directly rather than the fields they share manufactures 213 "
     "disagreements where there are 43: the other 170 are one capture never having heard of "
     "the field. Most of those sit on 18 record types the Data Fields catalogue does not "
     "contain at all, and the fields are plumbing — BOMapClientRecordID, FirmID, "
     "ProjectEntityName, Inactive. This is the same failure as treating one export read "
     "twice as two witnesses, in the opposite direction.",
     "derived", "features/required-and-validation/README.md"),
    ("Custom lists differ",
     "The Firm_ precedent does not extend to custom lists",
     "CRL_, OpEx and LAR_ prefixes appear zero times in all 7,368 inventory rows, and "
     "ClientListRow's 24 columns carry no prefix at all. The custom-lists analysis had "
     "argued that custom-list values are probably real columns on the strength of the Firm_ "
     "precedent. The inventory confirms that precedent at column level and shows "
     "ClientListRow demonstrably not following it, so the analogy is weaker, not stronger. "
     "Only a REST deep-serialise of one custom-list row can settle it: every offline "
     "artefact traces back to the one export that omits these fields.",
     "observed", "features/custom-lists/README.md"),
    ("Replica is not schema",
     "Replication coverage is not the product's schema",
     "The inventory's PG Table Status column splits 69 tables \"Created — holds data\" against "
     "150 \"Not created yet\". That describes the coverage of one replication loader targeting "
     "one database, lxr_drp_bbw — not the size of Lx's schema. The tell is project_entity: 107 "
     "fields, every one marked extracted, table never created, yet it is the universal "
     "supertype of a tenant holding 2,014 contracts, so it cannot be empty. The loader simply "
     "does not produce it. Read that column as loader coverage, never as a statement about the "
     "product.",
     "observed", "data-model/pg/bbw-field-inventory.csv"),
    ("Punch List is out",
     "Punch List is out of scope",
     "The four Punch List tables belong to construction management, which the approved BRDs "
     "assign to a different product. They stay in the census so impact analysis is never "
     "silently wrong at the boundary, and are documented nowhere else.",
     "observed", "data-model/object-catalog.md"),
]


if __name__ == "__main__":  # a smoke test, not a build step
    en = entity_notes()
    le = entity_leads()
    fc = field_catalog()
    fa = feature_areas()
    fi = field_inventory()
    oi = object_inventory(fi)
    sh = screenshots()
    print("entity_notes   %d" % len(en))
    print("entity_leads   %d" % len(le))
    print("field_catalog  %d" % len(fc))
    print("feature_areas  %d  %s" % (len(fa), ", ".join(sorted(fa))))
    print("screenshots    %d areas, %d files"
          % (len(sh), sum(len(v) for v in sh.values())))
    print("legend         %d types" % len(field_type_legend()))
    print("field_inventory %d rows, %d with a definition"
          % (len(fi), sum(1 for v in fi.values() if v["definition"])))
    print("object_inventory %d objects" % len(oi))
    refs = shot_references()
    print("shot_paths      %d captures in %d areas" % (len(shot_paths()), len(sh)))
    print("shot_index      %d de-numbered slugs" % len(shot_index()))
    print("shot_references %d captures referenced; %d citations, %d embeds"
          % (len(refs), sum(len(v["cites"]) for v in refs.values()),
             sum(len(v["embeds"]) for v in refs.values())))
    print("held back       %d captures pending the name-redaction decision"
          % sum(1 for p in shot_paths() if shot_is_private(p)))
    print()
    print("Contract:", (en.get("Contract") or {}).get("blurb", "")[:200])
