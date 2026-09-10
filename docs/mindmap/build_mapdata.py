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
        "Typed pointers to other records. Lucernex names each FK type after the table it "
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

# ----------------------------------------------------------------- build index

out_objects = {}
for o in objects:
    name = o["object"]
    groups = {}
    for f in o.get("fields", []):
        fam = {"foreign_key": "fk", "soft_reference": "soft"}.get(
            f["type_family"], f["type_family"]
        )
        groups.setdefault(field_group(f), []).append([f["name"], f["type"], fam])
    ordered = [
        [g, groups[g]] for g in GROUP_ORDER if g in groups
    ]
    out_objects[name] = {
        "t": o.get("pg_table") or "",
        "tc": o.get("physical_table_count", 1),
        "n": o.get("declared_field_count", 0),
        "m": obj_module.get(name, "unassigned"),
        "g": ordered,
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
        "what": m.get("what") or "",
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

curated = {}
for fname, mod in CURATED_FOR.items():
    fp = os.path.join(HERE, fname)
    if os.path.exists(fp):
        with open(fp, encoding="utf-8") as fh:
            curated[mod] = json.load(fh)
        print(f"  curated tree: {fname} -> {mod}")

bundle = {
    "curated": curated,
    "meta": {
        "product": "Lucernex IWMS",
        "vendor": "Accruent",
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
top = sorted(in_degree.items(), key=lambda x: -x[1])[:10]
print("  top in-degree:", ", ".join(f"{k}({v})" for k, v in top))
