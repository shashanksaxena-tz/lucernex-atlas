#!/usr/bin/env python3
"""
Generate docs/site/ — a browsable static HTML mirror of the atlas.

One real file per node, so every record type, module and rule has its own page
that opens with a double-click, works from the filesystem with no server, and
can be linked to, printed, or handed to somebody who will never open the
interactive app.

  site/index.html                 the entry point
  site/modules/<id>.html          15 module pages
  site/entities/<Name>.html       223 record-type pages, one anchor per field
  site/rules/index.html           the rule index
  site/rules/<ID>.html            384 rule pages
  site/questions.html             286 open questions
  site/atlas.html                 the interactive app, copied in

Re-runnable: wipes and rewrites site/ each time.
"""

import html
import json
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
SITE = os.path.join(DOCS, "site")


def load(n):
    with open(os.path.join(HERE, n), encoding="utf-8") as fh:
        return json.load(fh)


M = load("mapdata.json")
R = load("rules.json")
Q = load("questions.json")
F = load("findings.json")

meta, objects, modules = M["meta"], M["objects"], M["modules"]
edges = M["edges"]
group_blurb = M.get("groupBlurb", {})

edges_from, edges_to = {}, {}
for e in edges:
    edges_from.setdefault(e[0], []).append(e)
    if e[3]:
        edges_to.setdefault(e[3], []).append(e)

mod_by_id = {m["id"]: m for m in modules}
HUES = ["#4E7CA1", "#7A6BA8", "#3F8A78", "#A8743F", "#8A5470", "#5B7F45", "#9A5B4C",
        "#4C6E9E", "#7E7A46", "#6A5D95", "#3E8395", "#8C6A3F", "#5D8A5C", "#96566A", "#6E7683"]
hue = {m["id"]: HUES[i % len(HUES)] for i, m in enumerate(modules)}

e = html.escape
def fmt(n): return f"{n:,}" if isinstance(n, int) else (n or "")
def slug(s): return re.sub(r"[^A-Za-z0-9_.-]", "_", s)

CONF = {"observed": ("obs", "Observed"), "derived": ("der", "Derived"),
        "inferred": ("inf", "Inferred")}
def ctag(c):
    k, l = CONF.get(c, CONF["derived"])
    return f'<span class="tag {k}">{l}</span>'


CSS = """
:root{--bg:#E7EAEE;--surface:#F8F9FB;--surface2:#EEF1F5;--ink:#12161C;--ink2:#3D4650;
 --muted:#6B7480;--faint:#9AA3AF;--line:#C4CBD4;--line2:#DDE2E8;--accent:#0E6E7E;
 --accent-soft:#D3E7EA;--ok:#2F6B45;--warn:#8A5A12;--info:#2B5590;--r:3px}
@media (prefers-color-scheme:dark){:root{--bg:#0D1116;--surface:#141A21;--surface2:#1B222B;
 --ink:#E6EAEF;--ink2:#BAC3CD;--muted:#8B95A2;--faint:#67727F;--line:#2A323C;--line2:#212932;
 --accent:#48BFD2;--accent-soft:#16323A;--ok:#6FBF8C;--warn:#D6A34A;--info:#7FA9E0}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
 font-family:"IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
 font-size:14px;line-height:1.55;-webkit-font-smoothing:antialiased}
.mono{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;font-variant-numeric:tabular-nums}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
header{background:var(--surface);border-bottom:1px solid var(--line);padding:10px 22px;
 display:flex;gap:16px;align-items:baseline;flex-wrap:wrap;position:sticky;top:0;z-index:5}
header b{font-size:15px}header nav{margin-left:auto;display:flex;gap:14px;font-size:13px;flex-wrap:wrap}
main{max-width:1000px;margin:0 auto;padding:26px 22px 90px}
h1{font-size:27px;font-weight:600;letter-spacing:-.02em;margin:0 0 4px}
h1.mono{font-size:23px}
.sub{color:var(--muted);font-size:13px;margin:0 0 20px}
.crumb{font-size:11.5px;color:var(--muted);margin:0 0 12px}
h2{margin:28px 0 10px;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
 font-weight:600;border-bottom:1px solid var(--line2);padding-bottom:6px}
p{max-width:70ch;color:var(--ink2)}p.lead{font-size:15px;max-width:66ch}
.tag{display:inline-block;font-size:9.5px;letter-spacing:.07em;text-transform:uppercase;padding:2px 6px;
 border-radius:2px;border:1px solid var(--line);color:var(--muted);margin:0 4px 4px 0}
.tag.obs{color:var(--ok);border-color:currentColor}
.tag.der{color:var(--info);border-color:currentColor}
.tag.inf{color:var(--warn);border-color:currentColor}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(112px,1fr));gap:1px;background:var(--line2);
 border:1px solid var(--line2);border-radius:var(--r);overflow:hidden;margin:0 0 22px}
.stats div{background:var(--surface);padding:11px 13px}
.stats b{display:block;font-size:21px;font-weight:600;letter-spacing:-.02em}
.stats span{display:block;font-size:9.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(262px,1fr));gap:11px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:13px 15px;display:block;color:inherit}
.card:hover{border-color:var(--accent);text-decoration:none}
.card.oos{border-style:dashed;opacity:.75}
.card h3{margin:0 0 5px;font-size:14px;font-weight:600;display:flex;gap:7px;align-items:center}
.card .hue{width:3px;height:14px;border-radius:2px;flex:none}
.card p{margin:0 0 8px;font-size:12.5px;color:var(--muted);max-width:none}
.card .row{display:flex;gap:12px;font-size:10.5px;color:var(--faint)}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th,td{padding:6px 9px;text-align:left;border-bottom:1px solid var(--line2);vertical-align:top}
th{background:var(--surface2);color:var(--muted);font-weight:600;font-size:9.5px;
 letter-spacing:.07em;text-transform:uppercase;position:sticky;top:0;z-index:1}
.wrapt{max-height:none}
td.num,th.num{text-align:right;font-family:"IBM Plex Mono",monospace}
tr:target td{background:var(--accent-soft)}
.wrapt{border:1px solid var(--line2);border-radius:var(--r);overflow:auto;margin:0 0 8px}
dl{display:grid;grid-template-columns:auto 1fr;gap:5px 16px;font-size:13px;margin:0 0 18px}
dt{color:var(--muted);white-space:nowrap}dd{margin:0}
.find{background:var(--surface);border:1px solid var(--line);border-left:3px solid var(--accent);
 border-radius:var(--r);padding:11px 14px;margin:0 0 9px}
.find h4{margin:0 0 4px;font-size:13.5px}.find p{margin:0;font-size:12.5px;max-width:none}
.item{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:10px 13px;margin:0 0 7px}
.item .m{font-size:10.5px;color:var(--faint);margin-top:5px}
.grp{margin:0 0 16px}
.grp h3{margin:0 0 4px;font-size:14px;font-weight:600}
.grp .gb{font-size:12.5px;color:var(--muted);margin:0 0 7px;max-width:70ch}
.note{background:var(--surface2);border:1px solid var(--line2);border-radius:var(--r);
 padding:10px 13px;font-size:12.5px;color:var(--ink2);margin:0 0 18px}
"""


def page(title, body, depth=0, crumb=""):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} &middot; Lucernex Atlas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}atlas.css">
</head><body>
<header><b>Lucernex Atlas</b>
<nav><a href="{up}index.html">Overview</a><a href="{up}atlas.html">Interactive app</a>
<a href="{up}entities/index.html">Record types</a><a href="{up}rules/index.html">Rules</a>
<a href="{up}questions.html">Open questions</a></nav></header>
<main>{crumb}{body}</main></body></html>"""


# --------------------------------------------------------------------- rebuild
if os.path.isdir(SITE):
    shutil.rmtree(SITE)
for d in ("", "modules", "entities", "rules"):
    os.makedirs(os.path.join(SITE, d), exist_ok=True)

with open(os.path.join(SITE, "atlas.css"), "w", encoding="utf-8") as fh:
    fh.write(CSS)

built = os.path.join(HERE, "lucernex-atlas.built.html")
if os.path.exists(built):
    shutil.copyfile(built, os.path.join(SITE, "atlas.html"))

NOTE = ('<div class="note">These pages are generated from the same data as the interactive app. '
        'Notes and the mind map live in <a href="atlas.html">the app</a> &mdash; these files are for '
        'reading, linking and printing.</div>')


def mod_card(m, up=""):
    return (f'<a class="card {"" if m["scope"] else "oos"}" href="{up}modules/{slug(m["id"])}.html">'
            f'<h3><span class="hue" style="background:{hue[m["id"]]}"></span>{e(m["title"])}</h3>'
            f'<p>{e(m["what"][:190])}</p><div class="row"><span>{m["oc"]} records</span>'
            f'<span>{fmt(m["fc"])} fields</span><span>{m["ei"]} in</span><span>{m["eo"]} out</span>'
            f'</div></a>')


# ------------------------------------------------------------------- index
stats = [("Modules", meta["modules"]), ("Record types", meta["objects"]),
         ("Fields", fmt(meta["fields"])), ("Foreign keys", meta["edges"]),
         ("Rules", fmt(R["total"])), ("Open questions", fmt(Q["total"])),
         ("Data Fields", fmt(meta["datafields"])), ("API types", meta["gqlTypes"])]
body = [f'<h1>Lucernex, as it actually runs</h1>',
        f'<p class="sub">{e(meta["vendor"])} &middot; {e(meta["tenant"])} &middot; build {e(meta["build"])} &middot; captured {e(meta["captured"])}</p>',
        NOTE.replace('href="atlas.html"', 'href="atlas.html"'),
        '<p class="lead">Everything here was read out of the live application and its own schema tools. '
        'Every claim carries an evidence label &mdash; <b>Observed</b> means somebody saw it, '
        '<b>Inferred</b> means nobody has yet.</p>',
        '<div class="stats">' + "".join(
            f'<div><b class="mono">{v}</b><span>{k}</span></div>' for k, v in stats) + '</div>',
        '<h2>Modules</h2><div class="cards">' +
        "".join(mod_card(m) for m in modules if m["scope"]) + '</div>',
        '<h2>Excluded by decision</h2><div class="cards">' +
        "".join(mod_card(m) for m in modules if not m["scope"]) + '</div>']
open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(
    page("Overview", "".join(body)))

# ----------------------------------------------------------------- modules
for m in modules:
    rules = [r for r in R["rules"] if r["module"] == m["id"] or r["moduleTitle"] == m["title"]]
    finds = F.get(m["id"], [])
    b = [f'<p class="crumb"><a href="../index.html">Atlas</a> &rsaquo; {e(m["title"])}</p>',
         f'<h1>{e(m["title"])}</h1>',
         f'<p class="sub">{"In scope for the rebuild" if m["scope"] else "Out of scope by decision"}</p>',
         f'<p class="lead">{e(m["what"])}</p>',
         '<div class="stats">' + "".join(
             f'<div><b class="mono">{v}</b><span>{k}</span></div>' for k, v in
             [("Record types", m["oc"]), ("Fields", fmt(m["fc"])), ("Keys in", m["ei"]),
              ("Keys out", m["eo"]), ("Rules", len(rules))]) + '</div>']
    if finds:
        b.append('<h2>What was found here</h2>')
        b += [f'<div class="find"><h4>{e(t)} {ctag(c)}</h4><p>{e(d)}</p></div>' for t, c, d in finds]
    if m.get("dep"):
        b.append('<h2>Depends on</h2><div class="cards">' + "".join(
            mod_card(mod_by_id[d], "../") for d in m["dep"] if d in mod_by_id) + '</div>')
    b.append(f'<h2>Record types &middot; {m["oc"]}</h2><div class="wrapt"><table>'
             '<thead><tr><th>Record type</th><th>Postgres table</th><th class="num">Fields</th>'
             '<th class="num">Referenced by</th></tr></thead><tbody>')
    for n in m["objects"]:
        o = objects.get(n)
        if not o:
            continue
        b.append(f'<tr><td><a class="mono" href="../entities/{slug(n)}.html">{e(n)}</a></td>'
                 f'<td class="mono" style="color:var(--muted)">{e(o["t"] or "—")}</td>'
                 f'<td class="num">{fmt(o["n"])}</td>'
                 f'<td class="num">{fmt(len(edges_to.get(n, [])))}</td></tr>')
    b.append('</tbody></table></div>')
    if rules:
        b.append(f'<h2>Rules &middot; {len(rules)}</h2><div class="wrapt"><table>'
                 '<thead><tr><th>Rule</th><th>Subject</th><th>Confidence</th></tr></thead><tbody>')
        for r in rules:
            b.append(f'<tr><td><a class="mono" href="../rules/{slug(r["id"])}.html">{e(r["id"])}</a></td>'
                     f'<td>{e((r.get("section") or r["text"])[:140])}</td><td>{ctag(r["conf"])}</td></tr>')
        b.append('</tbody></table></div>')
    open(os.path.join(SITE, "modules", slug(m["id"]) + ".html"), "w", encoding="utf-8").write(
        page(m["title"], "".join(b), depth=1))

# ---------------------------------------------------------------- entities
names = sorted(objects, key=lambda n: -objects[n]["n"])
rows = []
for n in names:
    o = objects[n]
    mm = mod_by_id.get(o["m"])
    rows.append(f'<tr><td><a class="mono" href="{slug(n)}.html">{e(n)}</a></td>'
                f'<td style="font-size:11.5px"><a href="../modules/{slug(o["m"])}.html">'
                f'{e(mm["title"] if mm else o["m"])}</a></td>'
                f'<td class="mono" style="color:var(--muted)">{e(o["t"] or "—")}</td>'
                f'<td class="num">{fmt(o["n"])}</td>'
                f'<td class="num">{fmt(len(edges_to.get(n, [])))}</td></tr>')
open(os.path.join(SITE, "entities", "index.html"), "w", encoding="utf-8").write(page(
    "All record types",
    f'<h1>All record types</h1><p class="sub">{len(names)}, largest first</p>'
    '<div class="wrapt"><table><thead><tr><th>Record type</th><th>Module</th>'
    '<th>Postgres table</th><th class="num">Fields</th><th class="num">Ref by</th></tr></thead>'
    '<tbody>' + "".join(rows) + '</tbody></table></div>', depth=1))

for n in names:
    o = objects[n]
    mm = mod_by_id.get(o["m"])
    ins = edges_to.get(n, [])
    outs = [x for x in edges_from.get(n, []) if x[3]]
    by_src = {}
    for x in ins:
        by_src.setdefault(x[0], []).append(x[1])
    b = [f'<p class="crumb"><a href="../index.html">Atlas</a> &rsaquo; '
         f'<a href="../modules/{slug(o["m"])}.html">{e(mm["title"] if mm else o["m"])}</a> &rsaquo; {e(n)}</p>',
         f'<h1 class="mono">{e(n)}</h1>',
         f'<p class="sub">{fmt(o["n"])} fields'
         + (f' &middot; split across {o["tc"]} physical tables' if o["tc"] > 1 else '') + '</p>',
         '<dl>'
         f'<dt>Postgres table</dt><dd class="mono">{e(o["t"] or "none exported")}</dd>'
         f'<dt>Module</dt><dd><a href="../modules/{slug(o["m"])}.html">{e(mm["title"] if mm else o["m"])}</a></dd>'
         f'<dt>Referenced by</dt><dd>{fmt(len(ins))} keys from {len(by_src)} record types</dd>'
         f'<dt>Points at</dt><dd>{fmt(len(outs))} other records</dd></dl>']
    if o["tc"] > 1:
        b.append(f'<div class="find"><h4>Column-split table {ctag("observed")}</h4><p>This record&rsquo;s '
                 f'columns are spread across {o["tc"]} physical tables &mdash; the platform working around a '
                 'column-count ceiling. The logical record and the physical rows are not one to one.</p></div>')
    b.append('<h2>Fields</h2>')
    for g, fields in o["g"]:
        b.append(f'<div class="grp"><h3>{e(g)} <span class="tag">{len(fields)}</span></h3>')
        if group_blurb.get(g):
            b.append(f'<p class="gb">{e(group_blurb[g])}</p>')
        b.append('<div class="wrapt"><table><thead><tr><th>Field</th><th>Declared type</th>'
                 '<th>Points at</th></tr></thead><tbody>')
        for fn, ft, fam in fields:
            tgt = ""
            if fam == "fk":
                ed = next((x for x in edges_from.get(n, []) if x[1] == fn), None)
                if ed and ed[3] and ed[3] in objects:
                    tgt = f'<a class="mono" href="{slug(ed[3])}.html">{e(ed[3])}</a>'
                else:
                    tgt = '<span style="color:var(--faint)">unresolved</span>'
            elif fam == "dropdown":
                cm = re.search(r"\(([^)]+)\)", ft)
                tgt = f'<span style="color:var(--muted)">{e(cm.group(1) if cm else "code table")}</span>'
            b.append(f'<tr id="f-{slug(fn)}"><td class="mono">{e(fn)}</td>'
                     f'<td style="color:var(--muted)">{e(ft)}</td><td>{tgt}</td></tr>')
        b.append('</tbody></table></div></div>')
    if by_src:
        b.append(f'<h2>What points here &middot; {fmt(len(ins))} keys</h2><div class="wrapt"><table>'
                 '<thead><tr><th>Record type</th><th>Via column</th></tr></thead><tbody>')
        for s, cols in sorted(by_src.items(), key=lambda x: -len(x[1])):
            b.append(f'<tr><td><a class="mono" href="{slug(s)}.html">{e(s)}</a></td>'
                     f'<td class="mono" style="font-size:11.5px;color:var(--muted)">{e(", ".join(cols))}</td></tr>')
        b.append('</tbody></table></div>')
    open(os.path.join(SITE, "entities", slug(n) + ".html"), "w", encoding="utf-8").write(
        page(n, "".join(b), depth=1))

# ------------------------------------------------------------------- rules
by_mod = {}
for r in R["rules"]:
    by_mod.setdefault(r["moduleTitle"], []).append(r)
b = [f'<h1>Rules</h1><p class="sub">{fmt(R["total"])} numbered rules</p>',
     '<p class="lead">Each is stated so a rule engine could consume it. The confidence label is the one '
     'the source document gave it &mdash; an <b>Inferred</b> rule is a hypothesis somebody still has to '
     'confirm.</p>']
for mt, rs in sorted(by_mod.items(), key=lambda x: -len(x[1])):
    b.append(f'<h2>{e(mt)} &middot; {len(rs)}</h2><div class="wrapt"><table>'
             '<thead><tr><th>Rule</th><th>Subject</th><th>Confidence</th></tr></thead><tbody>')
    for r in rs:
        b.append(f'<tr><td><a class="mono" href="{slug(r["id"])}.html">{e(r["id"])}</a></td>'
                 f'<td>{e((r.get("section") or r["text"])[:150])}</td><td>{ctag(r["conf"])}</td></tr>')
    b.append('</tbody></table></div>')
open(os.path.join(SITE, "rules", "index.html"), "w", encoding="utf-8").write(
    page("Rules", "".join(b), depth=1))

for r in R["rules"]:
    b = [f'<p class="crumb"><a href="../index.html">Atlas</a> &rsaquo; '
         f'<a href="index.html">Rules</a> &rsaquo; {e(r["id"])}</p>',
         f'<h1 class="mono">{e(r["id"])}</h1>',
         f'<p class="sub">{e(r["moduleTitle"])} &middot; {e(r.get("section") or "")}</p>',
         ctag(r["conf"])]
    if r.get("detail"):
        b.append(f'<p class="lead">{e(r["detail"])}</p>')
    if r.get("cells"):
        b.append('<div class="wrapt"><table><tbody>' +
                 "".join(f'<tr><td>{e(c)}</td></tr>' for c in r["cells"]) + '</tbody></table></div>')
    else:
        b.append(f'<p>{e(r["text"])}</p>')
    b.append(f'<p style="font-size:11.5px;color:var(--faint);margin-top:18px">Source: {e(r["doc"])}</p>')
    open(os.path.join(SITE, "rules", slug(r["id"]) + ".html"), "w", encoding="utf-8").write(
        page(r["id"], "".join(b), depth=1))

# --------------------------------------------------------------- questions
by_area = {}
for q in Q["questions"]:
    by_area.setdefault(q["area"], []).append(q)
b = [f'<h1>Open questions</h1><p class="sub">{fmt(Q["total"])} things nobody has confirmed yet</p>',
     '<p class="lead">Every one of these is a thing somebody has to go and find out. They are the '
     'corpus&rsquo;s most actionable output.</p>']
for area, qs in sorted(by_area.items(), key=lambda x: -len(x[1])):
    b.append(f'<h2>{e(area)} &middot; {len(qs)}</h2>')
    b += [f'<div class="item">{e(q["q"])}<div class="m">{e(q["doc"])}</div></div>' for q in qs]
open(os.path.join(SITE, "questions.html"), "w", encoding="utf-8").write(
    page("Open questions", "".join(b)))

# ------------------------------------------------------------------ report
count = sum(len(f) for _, _, f in os.walk(SITE))
size = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(SITE) for f in fs)
print(f"wrote {SITE}")
print(f"  {count} files, {size / 1048576:.1f} MB")
print(f"  {len(modules)} modules, {len(names)} record types, {R['total']} rules, {Q['total']} questions")
