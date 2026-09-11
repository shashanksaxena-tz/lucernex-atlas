#!/usr/bin/env python3
"""
Assemble the single-file explorer from its parts.

  lucernex-explorer.html   the shell: styles, views, routing, notes
  map.js                   the mind-map view, inlined at __MAPJS__
  findings.json            per-module findings, inlined at __NOTES__
  mapdata.json             schema, modules, edges, curated trees
  rules.json               384 numbered rules
  questions.json           286 open questions

Output: lucernex-atlas.built.html — the same filename the published artifact
uses, so republishing keeps the existing URL.

Re-runnable. Run build_mapdata.py, build_rules.py and build_questions.py first
if their inputs have changed.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return json.load(fh)


def text(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return fh.read()


bundle = {
    "map": load("mapdata.json"),
    "feature": load("featuremap.json"),
    "rules": load("rules.json"),
    "questions": load("questions.json"),
}
payload = json.dumps(bundle, separators=(",", ":"))

# The data rides inside a <script type="application/json"> block, so the only
# sequence that can break out of it is a closing script tag.
assert "</script" not in payload.lower(), "data would break out of its script block"

html = text("lucernex-explorer.html")
html = html.replace("__MAPJS__", text("map.js"))
html = html.replace("__NOTES__", json.dumps(load("findings.json"), separators=(",", ":")))
html = html.replace("__DATA__", payload)

for marker in ("__DATA__", "__MAPJS__", "__NOTES__"):
    assert marker not in html, f"{marker} was not substituted"

out = os.path.join(HERE, "lucernex-atlas.built.html")
with open(out, "w", encoding="utf-8") as fh:
    fh.write(html)

size = os.path.getsize(out)
print(f"wrote {out}")
print(f"  {size:,} bytes ({size / 1048576:.2f} MB)")
print(f"  modules={len(bundle['map']['modules'])} "
      f"objects={len(bundle['map']['objects'])} "
      f"edges={len(bundle['map']['edges'])}")
print(f"  rules={bundle['rules']['total']} questions={bundle['questions']['total']} "
      f"curated={len(bundle['map'].get('curated', {}))}")
print(f"  feature areas={bundle['feature']['meta']['areas']} "
      f"nodes={bundle['feature']['meta']['nodes']}")
