#!/usr/bin/env python3
"""
Collect every "Open questions" list across the corpus into one JSON index.

Open questions are the corpus's most actionable output — each one is a thing
somebody has to go and find out before the rebuild can proceed — but they are
scattered across forty documents. This gathers them.

Re-runnable. Reads only; writes docs/mindmap/questions.json.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)

HEADING = re.compile(r"^#{2,4}\s+(.*open question.*)$", re.I)
ANY_HEADING = re.compile(r"^#{1,4}\s+")
ITEM = re.compile(r"^\s*(?:\d+\.|[-*])\s+(.*)")

AREA = {
    "modules/accounting": "Lease Accounting & Payments",
    "modules/contracts": "Contracts & Leases",
    "modules/workflow": "Workflow & Approvals",
    "modules/layouts-and-forms": "Configuration, Layouts & Forms",
    "modules/reporting": "Reporting",
    "data-model": "Data model & APIs",
    "admin": "Admin screens",
}


def clean(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def area_of(rel):
    for k, v in AREA.items():
        if rel.startswith(k):
            return v
    return "Other"


out = []
for root, dirs, files in os.walk(DOCS):
    dirs[:] = [d for d in dirs if d not in (".omc", "raw-captures", "data-fields", "assets")]
    for fn in sorted(files):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(root, fn)
        rel = os.path.relpath(path, DOCS)
        lines = open(path, encoding="utf-8").read().split("\n")
        i = 0
        while i < len(lines):
            if not HEADING.match(lines[i]):
                i += 1
                continue
            i += 1
            buf = []
            while i < len(lines) and not ANY_HEADING.match(lines[i]):
                m = ITEM.match(lines[i])
                if m:
                    buf.append(clean(m.group(1)))
                elif buf and lines[i].strip() and lines[i].startswith("   "):
                    buf[-1] += " " + clean(lines[i])          # continuation line
                i += 1
            for n, q in enumerate(buf, 1):
                if len(q) < 15:
                    continue
                out.append({
                    "q": q[:600],
                    "doc": rel,
                    "area": area_of(rel),
                    "rank": n,
                })

# de-duplicate on the first 90 characters; the same question is often restated
seen, uniq = set(), []
for q in out:
    k = q["q"][:90].lower()
    if k in seen:
        continue
    seen.add(k)
    uniq.append(q)

by_area = {}
for q in uniq:
    by_area[q["area"]] = by_area.get(q["area"], 0) + 1

path = os.path.join(HERE, "questions.json")
with open(path, "w", encoding="utf-8") as fh:
    json.dump({"total": len(uniq), "byArea": by_area, "questions": uniq},
              fh, separators=(",", ":"))

print(f"wrote {path}")
print(f"  {len(uniq)} open questions ({len(out)} before de-duplication)")
for a, n in sorted(by_area.items(), key=lambda x: -x[1]):
    print(f"    {n:>3}  {a}")
