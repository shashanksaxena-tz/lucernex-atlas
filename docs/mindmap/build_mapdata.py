#!/usr/bin/env python3
"""
Build the compact data bundle consumed by the interactive mind map artifact.

Reads the outputs of build_graph.py (objects.json, edges.json, modules.json) and
emits mapdata.json — the same facts, restructured for lazy tree expansion in the
browser and shrunk enough to embed in a single self-contained HTML page.

Re-runnable. No network, no side effects outside this directory.
"""

import json
import os
import re

import corpus

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return json.load(fh)


objects = load("objects.json")
edges = load("edges.json")
modules = load("modules.json")

# ---------------------------------------------------------------- field groups

AUDIT = {
    "CreatedByID", "CreatedDate", "ModifiedByID", "ModifiedDate",
    "RevNumber", "BOMapClientRecordID", "UUID",
}


def field_group(field):
    """Classify one field into a human-meaningful group.

    The groups are chosen so that opening a group tells a reader something about
    what the entity DOES, not merely how many columns it has.
    """
    name, typ, fam = field["name"], field["type"], field["type_family"]

    if name in AUDIT:
        return "Audit & record keeping"
    if fam == "foreign_key":
        return "Relationships (foreign keys)"
    if fam == "soft_reference":
        return "Soft references"
    if fam == "dropdown":
        return "Coded values (drop-downs)"
    if typ == "Currency":
        return "Money"
    if typ == "Percentage":
        return "Rates & percentages"
    if typ in ("Date", "Time"):
        return "Dates & timestamps"
    if typ == "Boolean":
        return "Flags"
    if typ in ("Number", "Area") or "Number" in typ:
        return "Quantities"
    if typ in ("Text", "Textarea"):
        return "Text & notes"
    return "Other"


GROUP_ORDER = [
    "Relationships (foreign keys)",
    "Soft references",
    "Coded values (drop-downs)",
    "Money",
    "Rates & percentages",
    "Quantities",
    "Dates & timestamps",
    "Flags",
    "Text & notes",
    "Audit & record keeping",
    "Other",
]

GROUP_BLURB = {
    "Relationships (foreign keys)":
        "Typed pointers to other records. Lx names each FK type after the table it "
        "points at, so the relational model is declared rather than implied.",
    "Soft references":
        "Columns that name another record without a typed foreign key behind them - generic "
        "handles such as Entity ID and item ID that point at whichever table the row belongs to. "
        "These are the joins a rebuild has to make explicit.",
    "Coded values (drop-downs)":
        "Fields bound to a master code table. Every one of these is a place where an "
        "administrator, not a developer, controls the allowed values.",
    "Money":
        "Currency amounts. Stored as TEXT in the physical database, which is why the rebuild "
        "must impose BigDecimal typing of its own.",
    "Rates & percentages": "Percentage inputs and computed rates.",
    "Quantities": "Counts, areas and other plain numeric measures.",
    "Dates & timestamps": "Dates that drive schedules, and system timestamps.",
    "Flags": "Booleans. In this product they usually gate engine behaviour rather than "
             "describe the record.",
    "Text & notes": "Free text. Notably, free text is never allowed to drive a conditional "
                    "display rule.",
    "Audit & record keeping": "Who created and changed the record, and the identifiers that "
                              "survive migration.",
    "Other": "Everything that did not fall into a named group.",
}

# ------------------------------------------------------------------ type notes

TYPE_NOTE = {
    "Text": "Free text.",
    "Currency": "A money amount.",
    "Percentage": "A percentage.",
    "Date": "A calendar date.",
    "Time": "A full timestamp, despite the name.",
    "Boolean": "True or false.",
    "Number": "A plain number.",
    "Area": "A building or land area, normally square footage.",
}

# ------------------------------------------------------------ object -> module

obj_module = {}
for mid, m in modules.items():
    for name in m.get("objects", []):
        obj_module[name] = mid

# --------------------------------------------------------- corpus-backed prose
# The maps used to label an entity "a record type in the contracts area holding
# 570 fields", which tells a reader nothing they could not see. The Data Fields
# catalogue already explains every one of these records in several sentences;
# this reads that text in and attaches it to the node.

CAT = corpus.entity_notes()          # 214 entities, from data-fields/INDEX.md
LEAD = corpus.entity_leads()         # 122 per-entity lead paragraphs
FIELDS = corpus.field_catalog()      # 6,158 catalogued fields with labels
LEGEND = corpus.field_type_legend()  # 448 sTYPE_/sCODE_ codes explained

# The field inventory is the primary source for what an individual field is FOR:
# 6,081 of the census's 7,421 fields carry a definition written by the vendor,
# plus a key role and the physical PostgreSQL mapping.
INV = corpus.field_inventory()
OINV = corpus.object_inventory(INV)

edges_to_obj = {}
edges_from_obj = {}
for _e in edges:
    edges_from_obj.setdefault(_e["source_object"], []).append(_e)
    if _e.get("target_object"):
        edges_to_obj.setdefault(_e["target_object"], []).append(_e)

# pe_scope is the tenancy position of a record and decides how a rebuild has to
# isolate it. Spelled out once here rather than left as a raw enum on the node.
PE_SCOPE = {
    "entity_scoped": (
        "Tenant-scoped, one join deep",
        "This record carries no FirmID of its own. It hangs off ProjectEntity, and tenant "
        "isolation has to be enforced by joining to that row and filtering on its FirmID — "
        "or it is not enforced at all. 161 of the 223 record types are shaped this way."),
    "subtype_root": (
        "A ProjectEntity subtype root",
        "One of the nine records that are themselves a kind of ProjectEntity rather than "
        "hanging off one. The discriminator is ProjectEntityTypeName, which is how a single "
        "table serves several apparent record types."),
    "firm_global": (
        "Firm-global reference data",
        "Owned by the firm as a whole rather than by any one business record — configuration "
        "and reference data rather than transactional rows."),
    "supertype": (
        "The polymorphic spine",
        "The supertype every business record hangs off. Its ProjectEntityTypeName column is "
        "the discriminator that makes one physical table present as several record types."),
}

CONF_OBS, CONF_DER, CONF_INF = "observed", "derived", "inferred"


def plural(n):
    return "" if n == 1 else "s"


def entity_prose(o, name, mod_id):
    """Compose the description a reader sees when they click this record type.

    Order of preference: the catalogue's own explanation, then the entity's own
    document, then a stated fallback that says the catalogue does not cover it
    rather than pretending otherwise.
    """
    cat = CAT.get(name)
    lead = LEAD.get(name)
    parts, src = [], []
    if cat and cat["blurb"]:
        parts.append(cat["blurb"])
        src.append(cat["doc"])
    if lead and (not parts or lead[0][:80] not in parts[0]):
        parts.append(lead[0])
        if lead[1] not in src:
            src.append(lead[1])
    if not parts:
        mod = modules.get(mod_id, {})
        oi = OINV.get(name) or {}
        parts.append(
            "Not covered by the Data Fields catalogue: this record type appears in the "
            "223-object census but has no row in the catalogue of 6,158 configurable "
            "fields, so no document describes the record as a whole. What is known is "
            "structural — %d declared fields, filed under %s, %d foreign keys pointing at it."
            % (o.get("declared_field_count", 0),
               (mod.get("title") or mod_id or "no module"),
               len(edges_to_obj.get(name, []))))
        if oi.get("defined"):
            # the field inventory reaches records the catalogue does not, so the
            # node is not empty even where no prose describes the record itself
            parts.append(
                "Its fields are documented even though the record is not: %d of its %d "
                "inventoried fields carry a definition written by the vendor. Open the "
                "field groups below and read them — that is the best account of this "
                "record available." % (oi["defined"], oi["fields"]))
            src.append(corpus.INVENTORY)
        src.append("_lucernex_objects_summary.txt")
    return " ".join(parts), src


def entity_notes_for(o, name, mod_id):
    """The caveats a rebuild has to know about this record, as [title, conf, text]."""
    out = []
    tc = o.get("physical_table_count", 1)
    if tc > 1:
        out.append([
            "Split across %d physical tables" % tc, CONF_OBS,
            "The logical record and the physical rows are not one to one: its columns are "
            "spread over %s. That is the platform working around a column-count ceiling, "
            "and any rebuild has to decide deliberately whether to reproduce the split or "
            "collapse it." % (o.get("pg_table") or "several tables")])
    if name.startswith("Virtual"):
        out.append([
            "A computed projection, not a table", CONF_OBS,
            "Virtual records are calculated at read time rather than stored. They have no "
            "primary key to join on and never appear in Firm scope — a tenant cannot "
            "customise a projection the platform generates. Treat this as the shape of a "
            "query result, not as a table to migrate."])
    firm_cols = [f["name"] for f in o.get("fields", [])
                 if f["name"].startswith("Firm_")]
    z_firm = [f["name"] for f in o.get("fields", [])
              if f["name"].lower().startswith("zfirm_")]
    if firm_cols or z_firm:
        extra = (" A further %d use the zFirm_ spelling instead." % len(z_firm)) if z_firm else ""
        out.append([
            "%d tenant custom columns" % (len(firm_cols) + len(z_firm)), CONF_OBS,
            "This record carries %d physical Firm_-prefixed columns — tenant custom fields "
            "are real columns, not rows in a value store, so adding one is a DDL change.%s "
            "That is direct evidence for database-per-tenant and against a shared schema."
            % (len(firm_cols), extra)])
    scope = PE_SCOPE.get(o.get("pe_scope") or "")
    if scope:
        out.append([scope[0], CONF_DER, scope[1]])
    cat = CAT.get(name)
    declared = o.get("declared_field_count", 0)
    if cat and declared and cat["total"] and declared - cat["total"] >= 20:
        out.append([
            "Census and catalogue disagree", CONF_OBS,
            "The object census declares %d fields; the Data Fields catalogue lists %d. The "
            "%d-field gap is columns the platform holds but does not expose as configurable "
            "Data Fields — a rebuild that reads only the catalogue will miss them."
            % (declared, cat["total"], declared - cat["total"])])
    if cat and cat["firm"]:
        out.append([
            "%d catalogued Firm-scope fields" % cat["firm"], CONF_OBS,
            "Of %d catalogued fields on this record, %d are Firm scope — defined by this "
            "tenant rather than shipped by the platform. Firm-scope definitions are "
            "RGAF rows carrying IsGlobal, FirmID and IsClientExtensionField."
            % (cat["total"], cat["firm"])])
    ind = len(edges_to_obj.get(name, []))
    outd = len([x for x in edges_from_obj.get(name, []) if x.get("target_object")])
    if ind >= 20:
        srcs = sorted({x["source_object"] for x in edges_to_obj.get(name, [])})
        out.append([
            "A hub: %d keys point here" % ind, CONF_OBS,
            "%d record types hold a foreign key into this one, so it sits at the centre of "
            "the relationship graph. Changing its key or its identity is a change to %s "
            "and %d others." % (len(srcs), ", ".join(srcs[:4]), max(0, len(srcs) - 4))])
    if ind == 0 and outd == 0:
        out.append([
            "No typed relationships either way", CONF_DER,
            "Nothing holds a typed foreign key into this record and it declares none out. "
            "Either it is joined by a soft reference the census cannot see, or it is "
            "genuinely standalone — worth settling before anything is built on it."])
    if name == "Contract":
        out.append([
            "Equipment contracts live in this table", CONF_OBS,
            "There is no EquipmentContract table in any inventory. An equipment contract is "
            "a Contract row discriminated by ProjectEntityTypeName = \"Equipment Contract\" — "
            "with a space in the value. Any query that filters contracts has to account for "
            "that, and any rebuild has to decide whether the discriminator survives."])
    if name == "DiscountRate":
        out.append([
            "Empty in both captured tenants", CONF_OBS,
            "This table holds zero rows in both American Freight and BBW while the ASC 842 "
            "engine runs and produces schedules. Where the discount rate actually comes "
            "from is unresolved, and it blocks the accounting rebuild."])
    # PageLayout / PageLayoutField carry the layout-tier and conditional-rule
    # findings, but neither is in the 223-object census — the census derives from
    # a viewer that refuses them. Those facts are carried by the feature map's
    # "Navigation & Screens" area and by corpus.CROSS_FACTS instead, so they are
    # not silently lost; do not re-add them here unless the census gains them.
    # --- from the field inventory: the physical mapping, and the loader's reach
    oi = OINV.get(name)
    if oi:
        if oi["tables"]:
            many = len(oi["tables"]) > 1
            out.append([
                "Lands in %s" % (", ".join(oi["tables"][:4])
                                 + (" and %d more" % (len(oi["tables"]) - 4)
                                    if len(oi["tables"]) > 4 else "")), CONF_OBS,
                "The field inventory names the physical destination of every column: %s "
                "in the database %s.%s Every field node carries its own table and column, "
                "so the mapping is per column, not per record."
                % (("%d tables" % len(oi["tables"])) if many else "one table",
                   ", ".join(oi["db"]) or "the replication target",
                   (" A record split across several tables is the platform working around a "
                    "column-count ceiling, and the split is stated here rather than inferred.")
                   if many else "")])
        if oi["tables"] and o.get("physical_table_count", 1) != len(oi["tables"]):
            out.append([
                "Two counts of its physical tables", CONF_OBS,
                "The object census counts %d physical tables for this record; the field "
                "inventory names %d (%s). The census reads the exported schema, the inventory "
                "reads one replication loader's configuration, so a table the loader does not "
                "write is invisible to the second count. Settle which you mean before quoting "
                "either." % (o.get("physical_table_count", 1), len(oi["tables"]),
                             ", ".join(oi["tables"]))])
        if oi["db"] == ["lxr_drp_bbw"]:
            out.append([
                "A per-tenant database name", CONF_DER,
                "The physical database is lxr_drp_bbw — the tenant's name is in the database "
                "name. That is one more piece of evidence for database-per-tenant and against "
                "a single shared schema, alongside the Firm_ columns."])
        if oi["defined"]:
            out.append([
                "%d field%s carry a vendor definition"
                % (oi["defined"], plural(oi["defined"])), CONF_OBS,
                "%d of this record's %d inventoried fields have prose written by the vendor "
                "saying what the field is for. Open any field node to read it — this is the "
                "one source in the corpus that explains fields rather than listing them."
                % (oi["defined"], oi["fields"])])
        if oi["required"]:
            out.append([
                "%d field%s marked required" % (oi["required"], plural(oi["required"])), CONF_OBS,
                "The inventory marks %d of this record's fields Required. Across the whole "
                "inventory that is 606 fields, which independently corroborates the 603 the "
                "corpus had derived from the Data Fields catalogue — two sources, arrived at "
                "separately, agreeing to within three." % oi["required"]])
        not_created = oi["status"].get("Not created yet — no data", 0)
        if not_created and not_created >= oi["fields"] * 0.5:
            loader_notes = sorted(oi["notes"], key=lambda k: -oi["notes"][k])[:2]
            out.append([
                "Replication coverage: not materialised", CONF_OBS,
                "Observed of the loader, not of the product. The replication target "
                "lxr_drp_bbw has never created a table for this record: %s That is a "
                "statement about one loader's coverage and says nothing about whether the "
                "record exists or holds data in Lx. The tell is ProjectEntity — 107 fields, "
                "every one marked extracted, table never created, yet it is the universal "
                "supertype of a tenant holding 2,014 contracts, so it plainly is not empty. "
                "Do not read the 69-created / 150-not-created split as the size of the "
                "product's schema." % (" ".join(loader_notes) if loader_notes else
                                       "no rows have ever arrived for it.")])
        if oi["notExtracted"]:
            out.append([
                "%d field%s excluded from extraction"
                % (oi["notExtracted"], plural(oi["notExtracted"])), CONF_OBS,
                "Observed of the loader. The inventory marks %d of this record's fields as "
                "not extracted to PostgreSQL, so the replication target creates no column for "
                "them. They still exist in Lx; anything reading the replica rather than the "
                "product will not see them." % oi["notExtracted"]])

    mod = modules.get(mod_id or "", {})
    if mod and not mod.get("in_scope", True):
        out.append([
            "Out of scope by decision", CONF_OBS,
            "Its module is excluded from the rebuild. It stays in the census so impact "
            "analysis through the relationship graph is never silently wrong at the "
            "boundary, but nothing here is being built."])
    return out


# ----------------------------------------------------------------- build index

FLAG_FIRM, FLAG_REQ, FLAG_RO = 1, 2, 4
FLAG_INV_REQ, FLAG_FUNC, FLAG_NOPG = 8, 16, 32

out_objects = {}
for o in objects:
    name = o["object"]
    mod_id = obj_module.get(name, "unassigned")
    groups = {}
    for f in o.get("fields", []):
        fam = {"foreign_key": "fk", "soft_reference": "soft"}.get(
            f["type_family"], f["type_family"]
        )
        cat = FIELDS.get((name, f["name"]))
        inv = INV.get((name, f["name"]))
        # Field entries stay positional to keep the bundle small:
        # [column, declared type, family, label, flags, catalogue type code,
        #  vendor definition, key role, physical mapping]
        flags = 0
        label = ""
        code = ""
        if cat:
            if cat["scope"] == "Firm":
                flags |= FLAG_FIRM
            if cat["required"]:
                flags |= FLAG_REQ
            if cat["readonly"]:
                flags |= FLAG_RO
            code = cat["type"]
            label = cat["label"]
        if inv:
            if inv["required"]:
                flags |= FLAG_INV_REQ
            if inv["functional"] == "Yes":
                flags |= FLAG_FUNC
            if not inv["extracted"]:
                flags |= FLAG_NOPG
            label = label or inv["label"]
        if label == f["name"]:
            label = ""
        pg = ""
        if inv and inv["pgcol"]:
            pg = "%s.%s" % (inv["pgtable"], inv["pgcol"])
            if inv["pgtype"]:
                pg += ":" + inv["pgtype"]
        row = [f["name"], f["type"], fam, label, flags, code,
               (inv or {}).get("definition", ""), (inv or {}).get("role", ""), pg]
        while len(row) > 3 and not row[-1]:      # trailing blanks cost bytes
            row.pop()
        groups.setdefault(field_group(f), []).append(row)
    ordered = [
        [g, groups[g]] for g in GROUP_ORDER if g in groups
    ]
    prose, prose_src = entity_prose(o, name, mod_id)
    out_objects[name] = {
        "t": o.get("pg_table") or "",
        "tc": o.get("physical_table_count", 1),
        "n": o.get("declared_field_count", 0),
        "m": mod_id,
        "g": ordered,
        "d": prose,
        "ds": prose_src,
        "notes": entity_notes_for(o, name, mod_id),
        "pe": o.get("pe_scope") or "",
        "sm": o.get("secondary_modules") or [],
        "cat": ([CAT[name]["total"], CAT[name]["global"], CAT[name]["firm"]]
                if name in CAT else None),
        # [fields inventoried, with a definition, marked required, not extracted]
        "inv": ([OINV[name]["fields"], OINV[name]["defined"], OINV[name]["required"],
                 OINV[name]["notExtracted"]] if name in OINV else None),
        "pgt": (OINV[name]["tables"] if name in OINV else []),
        "pgdb": (", ".join(OINV[name]["db"]) if name in OINV else ""),
    }

# ------------------------------------------------------------------- edge maps

out_edges = []
for e in edges:
    out_edges.append([
        e["source_object"],
        e["source_column"],
        e["declared_type"],
        e.get("target_object") or "",
        e.get("target_kind") or "",
        e.get("resolution") or "",
    ])

in_degree = {}
for e in edges:
    t = e.get("target_object")
    if t:
        in_degree[t] = in_degree.get(t, 0) + 1

out_modules = []
for mid, m in modules.items():
    out_modules.append({
        "id": mid,
        "title": m.get("title") or mid,
        "what": corpus.debrand(m.get("what") or ""),
        "lead": corpus.module_headline(mid),
        "scope": bool(m.get("in_scope", True)),
        "oc": m.get("object_count", 0),
        "fc": m.get("field_count", 0),
        "ei": m.get("edges_in", 0),
        "eo": m.get("edges_out", 0),
        "dep": m.get("depends_on", []),
        "objects": sorted(
            m.get("objects", []),
            key=lambda n: -out_objects.get(n, {}).get("n", 0),
        ),
    })
out_modules.sort(key=lambda x: (not x["scope"], -x["fc"]))

# ------------------------------------------------------- curated module trees
# Hand-authored, semantically-organised trees produced per module. They carry the
# capabilities, rules and constraints that no schema dump can express, and they sit
# alongside the structural tree generated from the schema.

CURATED_FOR = {"accounting-tree.json": "accounting",
               "contracts-tree.json": "contracts-leases",
               "workflow-tree.json": "workflow"}

def debrand_tree(n):
    """The curated trees are generated input, so the product name is rewritten
    here at build time rather than by editing their JSON."""
    if isinstance(n, dict):
        return {k: (corpus.debrand(v) if isinstance(v, str) else debrand_tree(v))
                for k, v in n.items()}
    if isinstance(n, list):
        return [debrand_tree(c) for c in n]
    return corpus.debrand(n) if isinstance(n, str) else n


curated = {}
for fname, mod in CURATED_FOR.items():
    fp = os.path.join(HERE, fname)
    if os.path.exists(fp):
        with open(fp, encoding="utf-8") as fh:
            curated[mod] = debrand_tree(json.load(fh))
        print(f"  curated tree: {fname} -> {mod}")

bundle = {
    "curated": curated,
    "meta": {
        "product": "Lx",
        "vendor": "Vendor-hosted IWMS",
        "tenant": "(ASG) American Freight",
        "build": "26.08.0.46 (2026/08/26 16:15)",
        "captured": "2026-09-10",
        "objects": len(objects),
        "fields": sum(o.get("declared_field_count", 0) for o in objects),
        "edges": len(edges),
        "modules": len(out_modules),
        "datafields": 6158,
        "fieldtypes": 448,
        "gqlTypes": 490,
        "gqlQueries": 617,
        "gqlMutations": 3,
    },
    "groupBlurb": GROUP_BLURB,
    "typeNote": TYPE_NOTE,
    # 448 sTYPE_/sCODE_ codes explained once, so a field node can say what its
    # catalogued type means instead of just naming it.
    "typeLegend": LEGEND,
    # what a field's Key Role means, explained once
    "roleNote": {v[0]: v[1] for v in corpus.KEY_ROLE.values()},
    # Cross-cutting facts the whole map has to carry, each quoting a document.
    "facts": [{"n": n, "t": t, "conf": c, "d": d, "src": s}
              for n, t, d, c, s in corpus.CROSS_FACTS],
    "modules": out_modules,
    "objects": out_objects,
    "edges": out_edges,
    "inDegree": in_degree,
}

path = os.path.join(HERE, "mapdata.json")
with open(path, "w", encoding="utf-8") as fh:
    json.dump(bundle, fh, separators=(",", ":"))

print(f"wrote {path}")
print(f"  {os.path.getsize(path):,} bytes")
print(f"  modules={len(out_modules)} objects={len(out_objects)} edges={len(out_edges)}")
print(f"  fields={bundle['meta']['fields']:,}")
_defined = sum(1 for gs in out_objects.values() for _g, fs in gs["g"]
               for f in fs if len(f) > 6 and f[6])
_mapped = sum(1 for gs in out_objects.values() for _g, fs in gs["g"]
              for f in fs if len(f) > 8 and f[8])
print(f"  field definitions from the inventory: {_defined:,}")
print(f"  fields with a physical PostgreSQL mapping: {_mapped:,}")
top = sorted(in_degree.items(), key=lambda x: -x[1])[:10]
print("  top in-degree:", ", ".join(f"{k}({v})" for k, v in top))
