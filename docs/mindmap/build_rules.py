#!/usr/bin/env python3
"""
Extract every numbered rule from the module `rules.md` files into one JSON index.

The five modules were written by different agents and their tables do not share a
column layout, so this parser is deliberately tolerant: it finds any markdown table
row whose cells contain a rule id, keeps the remaining cells as that rule's content,
and tags it with the nearest preceding heading.

Beyond finding the rules, this splits each one into the parts a reader needs and a
rule engine could consume — trigger, inputs, condition, computation, output — and
records what the rule constrains (the record types and columns it names), the
vendor wording it rests on, the rules it cites, and where to go and check it. A
rule node that shows only an id and a name is the bug this exists to fix.

Re-runnable. Reads only; writes docs/mindmap/rules.json.
"""

import json
import os
import re

import corpus

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)

MODULES = {
    "accounting": ("ACC", "Lease Accounting & Payments"),
    "contracts": ("CON", "Contracts & Leases"),
    "workflow": ("WF", "Workflow & Approvals"),
    "layouts-and-forms": ("LAY", "Configuration, Layouts, Forms & Reporting"),
    "reporting": ("RPT", "Configuration, Layouts, Forms & Reporting"),
    "facilities-locations": ("FAC", "Facilities, Locations & Sites"),
    "platform-tenancy": ("PLT", "Platform & Tenancy"),
    "people-parties": ("PPL", "People & Parties"),
    "assets-equipment": ("AST", "Assets, Equipment & Maintenance"),
    "property-tax": ("TAX", "Property Tax"),
    "documents-folders": ("DOC", "Documents, Folders & Correspondence"),
    "portfolio-transactions": ("POR", "Portfolio & Real-Estate Transactions"),
    "projects-capital": ("PRJ", "Capital Projects & Scheduling"),
}

RULE_ID = re.compile(r"\b([A-Z]{2,4}-R-\d{2,4})\b")
CONF = re.compile(r"\b(Observed|Derived|Inferred)\b", re.I)


def clean(cell):
    """Strip markdown emphasis and links down to readable text."""
    s = cell.strip()
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def parse_headings(path, prefix):
    """Rules written as `### ACC-R-001 - Title` followed by a prose block."""
    out, seen = [], set()
    lines = open(path, encoding="utf-8").read().split("\n")
    starts = []
    for i, line in enumerate(lines):
        h = re.match(r"^#{2,4}\s+(.*)", line)
        if not h:
            continue
        m = RULE_ID.search(h.group(1))
        if m and m.group(1).startswith(prefix + "-R-"):
            starts.append((i, m.group(1), clean(h.group(1))))
    for k, (i, rid, title) in enumerate(starts):
        if rid in seen:
            continue
        seen.add(rid)
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        block = [l for l in lines[i + 1:end] if l.strip()]
        cells, body = [], []
        for l in block:
            if l.lstrip().startswith("|"):
                cs = [clean(c) for c in l.strip().strip("|").split("|")]
                cells += [c for c in cs if c and not re.fullmatch(r"-+", c)]
            else:
                body.append(clean(l))
        text = " ".join(body) or " · ".join(cells)
        cm = CONF.search(" ".join(block))
        out.append({
            "id": rid,
            "n": int(rid.rsplit("-", 1)[1]),
            "section": title.replace(rid, "").strip(" -\u2014"),
            "cells": cells[:8],
            "text": text[:1200],
            "conf": cm.group(1).lower() if cm else "derived",
        })
    return out


def parse(path, prefix):
    """Yield one record per rule row found in a rules.md file."""
    if not os.path.exists(path):
        return []
    out, heading, seen = [], "", set()
    for line in open(path, encoding="utf-8"):
        h = re.match(r"^#{2,4}\s+(.*)", line)
        if h:
            heading = clean(h.group(1))
            continue
        if not line.lstrip().startswith("|"):
            continue
        cells = [clean(c) for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        # the id may live in any cell; the first one carrying it wins
        rid = None
        for i, c in enumerate(cells):
            m = RULE_ID.search(c)
            if m and m.group(1).startswith(prefix + "-R-"):
                rid, idx = m.group(1), i
                break
        if not rid or rid in seen:
            continue
        # A cell naming two ids is a range row ("LAY-R-010 … LAY-R-018 | subject |
        # owning document") — a pointer, not a rule. Taking it would give every
        # rule in the range the range's own summary and nothing else, which is
        # exactly the empty-node problem. Skip it; the real rule is elsewhere.
        if len(set(RULE_ID.findall(cells[idx]))) > 1:
            continue
        seen.add(rid)
        rest = [c for i, c in enumerate(cells) if i != idx and c and not re.fullmatch(r"-+", c)]
        body = " · ".join(rest)
        cm = CONF.search(body)
        out.append({
            "id": rid,
            "n": int(rid.rsplit("-", 1)[1]),
            "section": heading,
            "cells": rest,
            "text": body,
            "conf": cm.group(1).lower() if cm else "derived",
        })
    return out


def module_docs(folder):
    """rules.md first, then every companion document in the module folder.

    Numbered rules are not confined to rules.md — the layouts module, for one,
    states LAY-R-010…018 in conditional-fields.md and leaves only a pointer
    behind. Scanning the whole folder is how those rules arrive with a statement
    instead of a cross-reference.
    """
    d = os.path.join(DOCS, "modules", folder)
    if not os.path.isdir(d):
        return []
    first = os.path.join(d, "rules.md")
    rest = sorted(os.path.join(d, f) for f in os.listdir(d)
                  if f.endswith(".md") and f != "rules.md")
    return ([first] if os.path.exists(first) else []) + rest


def richest(candidates):
    """Of several statements of one rule, keep the one that says most."""
    return max(candidates, key=lambda r: (len(r.get("text") or ""),
                                          len(r.get("cells") or [])))


rules, per_module = [], {}
for folder, (prefix, module_title) in MODULES.items():
    found = {}
    for fp in module_docs(folder):
        got = parse(fp, prefix) + parse_headings(fp, prefix)
        for r in got:
            r["doc"] = os.path.relpath(fp, DOCS).replace(os.sep, "/")
            found.setdefault(r["id"], []).append(r)
    got = [richest(v) for v in found.values()]
    for r in got:
        r["module"] = folder
        r["moduleTitle"] = module_title
    got.sort(key=lambda r: r["n"])
    per_module[folder] = len(got)
    rules.extend(got)
    extra = sum(1 for r in got if not r["doc"].endswith("rules.md"))
    print(f"  {folder:20} {prefix + '-R':8} {len(got):>4} rules"
          + (f"  ({extra} stated outside rules.md)" if extra else ""))

# Rules also appear as nodes inside the hand-authored trees, where they carry the
# plain-language `detail` prose. Fold that in where the ids match.
enriched = 0
for fname in ("accounting-tree.json", "contracts-tree.json", "workflow-tree.json"):
    fp = os.path.join(HERE, fname)
    if not os.path.exists(fp):
        continue
    index = {r["id"]: r for r in rules}

    def walk(n):
        global enriched
        if n.get("kind") == "rule":
            m = RULE_ID.search(n.get("name", ""))
            if m and m.group(1) in index and n.get("detail"):
                tgt = index[m.group(1)]
                if not tgt.get("detail"):
                    tgt["detail"] = n["detail"]
                    enriched += 1
        for c in n.get("children") or []:
            walk(c)

    walk(json.load(open(fp, encoding="utf-8")))

# ===========================================================================
# Structure. Everything above finds the rules; this makes each one readable on
# its own, which is what a map node needs.
# ===========================================================================

# The labels the rule authors actually used, mapped onto five canonical slots so
# a reader gets the same shape whichever module wrote the rule.
SLOT = {
    "trigger": "When it fires", "when": "When it fires", "event": "When it fires",
    "input": "What it reads", "inputs": "What it reads", "reads": "What it reads",
    "condition": "The test", "test": "The test", "precondition": "The test",
    "computation": "What it computes", "calculation": "What it computes",
    "formula": "What it computes", "rule": "What it computes",
    "output": "What it writes", "outputs": "What it writes", "effect": "What it writes",
    "result": "What it writes", "writes": "What it writes",
    "confidence": "Confidence", "evidence": "Confidence", "source": "Confidence",
    "note": "Note", "notes": "Note", "caveat": "Note", "exception": "Note",
    "scope": "Scope", "applies to": "Scope",
}
SLOT_ORDER = ["When it fires", "What it reads", "The test", "What it computes",
              "What it writes", "Scope", "Note", "Confidence"]

BULLET = re.compile(r"(?:^|\s)[-•]\s+([A-Za-z][A-Za-z /]{2,22}):\s+")
IDENT = re.compile(r"`([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?)`")
QUOTED = re.compile(r"[\"“]([^\"”]{25,400})[\"”]")

OBJECTS = set()
_op = os.path.join(HERE, "objects.json")
if os.path.exists(_op):
    OBJECTS = {o["object"] for o in json.load(open(_op, encoding="utf-8"))}


def split_parts(text):
    """Break `- Trigger: … - Inputs: … - Output: …` into labelled slots."""
    marks = list(BULLET.finditer(text or ""))
    if len(marks) < 2:
        return []
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        label = SLOT.get(m.group(1).strip().lower(), m.group(1).strip().capitalize())
        body = text[m.end():end].strip(" .;·")
        # authors write an em dash when a slot does not apply; carrying that
        # through would make it the rule's headline
        if body and not re.fullmatch(r"[-—–]+|n/?a|none", body, re.I):
            out.append([label, body])
    # merge duplicate slots rather than dropping either
    merged, seen = [], {}
    for label, body in out:
        if label in seen:
            merged[seen[label]][1] += " " + body
        else:
            seen[label] = len(merged)
            merged.append([label, body])
    merged.sort(key=lambda p: SLOT_ORDER.index(p[0]) if p[0] in SLOT_ORDER else 99)
    return merged


def constrains(text, cells):
    """The record types and columns a rule names — what it actually governs."""
    objs, fields = [], []
    for raw in IDENT.findall(" ".join([text or ""] + list(cells or []))):
        if "." in raw:
            head = raw.split(".", 1)[0]
            if head in OBJECTS and raw not in fields:
                fields.append(raw)
                if head not in objs:
                    objs.append(head)
        elif raw in OBJECTS and raw not in objs:
            objs.append(raw)
    return objs[:12], fields[:16]


def statement_of(r, parts):
    """One sentence that says what the rule requires, for the node headline."""
    by = {label: body for label, body in parts}
    for slot in ("The test", "What it computes", "What it writes", "When it fires"):
        if by.get(slot):
            s = by[slot]
            return (s[:300].rsplit(" ", 1)[0] + "…") if len(s) > 300 else s
    body = (r.get("detail") or r.get("text") or "").strip()
    if not body:
        return r.get("section") or r["id"]
    cut = re.split(r"(?<=[.;])\s", body)
    s = " ".join(cut[:2]).strip()
    return (s[:300].rsplit(" ", 1)[0] + "…") if len(s) > 300 else s


def anchor_of(section):
    """GitHub-style heading anchor, so a rule links to its own paragraph."""
    a = re.sub(r"[^a-z0-9 -]", "", (section or "").lower()).strip().replace(" ", "-")
    return re.sub(r"-+", "-", a)


by_entity = {}
for r in rules:
    # debrand before splitting, so the parts a reader sees are debranded too
    r["text"] = corpus.debrand(r.get("text") or "")
    r["cells"] = [corpus.debrand(c) for c in (r.get("cells") or [])]
    joined = " ".join([r["text"]] + list(r["cells"]))
    r["parts"] = split_parts(r["text"])
    if not r["parts"] and len(r.get("cells") or []) >= 2:
        # table-form rules: the cells are already the parts, unlabelled
        r["parts"] = [["Stated as", c] for c in r["cells"][:6]]
    objs, flds = constrains(r.get("text"), r.get("cells"))
    r["objects"] = objs
    r["fields"] = flds
    r["statement"] = corpus.debrand(statement_of(r, r["parts"]))
    r["related"] = sorted({i for i in RULE_ID.findall(joined) if i != r["id"]})[:8]
    q = QUOTED.search(joined)
    r["quote"] = corpus.debrand(q.group(1).strip()) if q else ""
    # Confidence is reported once, on its own, not also as a row in the parts
    # table — the same paragraph appearing twice on a rule page reads as a bug
    by_slot = {label: body for label, body in r["parts"]}
    if by_slot.get("Confidence"):
        r["confNote"] = by_slot["Confidence"]
        r["parts"] = [p for p in r["parts"] if p[0] != "Confidence"]
    else:
        cm = re.search(r"Confidence:?\s*(.{0,260})", joined)
        r["confNote"] = corpus.debrand(cm.group(1).strip(" .·")) if cm else ""
    # the anchor addresses the heading as written in the document, so it is
    # computed before the display text is debranded
    r["anchor"] = anchor_of(r.get("section"))
    r["section"] = corpus.debrand(r.get("section") or "")
    if r.get("detail"):
        r["detail"] = corpus.debrand(r["detail"])
    for o in objs:
        by_entity.setdefault(o, []).append(r["id"])

structured = sum(1 for r in rules if r["parts"])
linked = sum(1 for r in rules if r["objects"])

bundle = {
    "total": len(rules),
    "byModule": per_module,
    "byEntity": by_entity,
    "slotOrder": SLOT_ORDER,
    "rules": rules,
}
path = os.path.join(HERE, "rules.json")
with open(path, "w", encoding="utf-8") as fh:
    json.dump(bundle, fh, separators=(",", ":"))

print(f"\nwrote {path}")
print(f"  {len(rules)} rules, {enriched} enriched with tree prose, {os.path.getsize(path):,} bytes")
print(f"  {structured} split into labelled parts, {linked} linked to named record types")
print(f"  {len(by_entity)} record types have at least one rule attached")
