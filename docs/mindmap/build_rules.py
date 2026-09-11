#!/usr/bin/env python3
"""
Extract every numbered rule from the module `rules.md` files into one JSON index.

The five modules were written by different agents and their tables do not share a
column layout, so this parser is deliberately tolerant: it finds any markdown table
row whose cells contain a rule id, keeps the remaining cells as that rule's content,
and tags it with the nearest preceding heading.

Re-runnable. Reads only; writes docs/mindmap/rules.json.
"""

import json
import os
import re

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


rules, per_module = [], {}
for folder, (prefix, module_title) in MODULES.items():
    fp = os.path.join(DOCS, "modules", folder, "rules.md")
    got = parse(fp, prefix)
    if len(got) < 5 and os.path.exists(fp):          # table form found little: try headings
        got = parse_headings(fp, prefix) or got
    for r in got:
        r["module"] = folder
        r["moduleTitle"] = module_title
        r["doc"] = f"modules/{folder}/rules.md"
    got.sort(key=lambda r: r["n"])
    per_module[folder] = len(got)
    rules.extend(got)
    print(f"  {folder:20} {prefix + '-R':8} {len(got):>4} rules")

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

bundle = {
    "total": len(rules),
    "byModule": per_module,
    "rules": rules,
}
path = os.path.join(HERE, "rules.json")
with open(path, "w", encoding="utf-8") as fh:
    json.dump(bundle, fh, separators=(",", ":"))

print(f"\nwrote {path}")
print(f"  {len(rules)} rules, {enriched} enriched with tree prose, {os.path.getsize(path):,} bytes")
