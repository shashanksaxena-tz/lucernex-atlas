#!/usr/bin/env python3
"""
Generate docs/site/research/ — the tenant research corpus as browsable HTML.

The atlas pages (build_site.py) are generated from the schema census. This
generator covers the material that came out of exploring the two live tenants:
the AF/BBW comparison, the feature knowledge base, the coverage tracker and the
REST API account. Those are hand-written markdown, so this renders them.

  site/research/index.html          entry point, grouped by kind
  site/research/<slug>.html         one page per source document

Markdown subset implemented deliberately: headings, GFM tables, fenced code,
blockquotes, lists, hr, and the inline set the corpus actually uses. No
dependency on a markdown package — the repo's build chain is standard-library
only and stays that way.

Re-runnable: wipes and rewrites site/research/ each time.
"""

import html
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
SITE = os.path.join(DOCS, "site")
OUT = os.path.join(SITE, "research")

e = html.escape


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# ------------------------------------------------------------------ inline
def inline(t):
    """Inline markdown -> HTML. Code spans are masked first so their
    contents are never treated as markup."""
    spans = []

    def stash(m):
        spans.append(m.group(1))
        return f"\x00{len(spans)-1}\x00"

    t = re.sub(r"`([^`]+)`", stash, t)
    t = e(t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{rewrite(m.group(2))}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"~~(.+?)~~", r"<del>\1</del>", t)
    t = t.replace("&amp;rarr;", "&rarr;").replace("&amp;mdash;", "&mdash;")
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{e(spans[int(m.group(1))])}</code>", t)


CUR = {"rel": ""}   # source path of the document being rendered, relative to docs/


def rewrite(href):
    """The generated tree mirrors docs/, so markdown links only need their
    extension swapped. Everything else (json, csv, images) still lives at the
    docs root, so resolve it there and point back out of research/."""
    if href.startswith(("http", "#", "mailto:")):
        return e(href)
    base, anchor = href.split("#")[0], href[len(href.split("#")[0]):]
    if not base:
        return e(anchor)
    if base.endswith(".md"):
        return e(base[:-3] + ".html" + anchor)
    if base.endswith("/"):
        return e(base + "index.html" + anchor)
    # non-markdown: resolve against the source doc, then climb out of research/
    srcdir = os.path.dirname(CUR["rel"])
    target = os.path.normpath(os.path.join(srcdir, base)) if srcdir else os.path.normpath(base)
    depth = CUR["rel"].count(os.sep)
    return e("../" * (depth + 2) + target.replace(os.sep, "/") + anchor)


# ------------------------------------------------------------------- block
def render(md):
    lines = md.split("\n")
    out, i, toc = [], 0, []
    while i < len(lines):
        ln = lines[i]

        # fenced code
        if ln.startswith("```"):
            lang = ln[3:].strip()
            buf, i = [], i + 1
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            cls = f' class="lang-{e(lang)}"' if lang else ""
            out.append(f"<pre{cls}><code>{e(chr(10).join(buf))}</code></pre>")
            continue

        # GFM table: header, delimiter, rows
        if ln.strip().startswith("|") and i + 1 < len(lines) and re.match(
                r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            def cells(r):
                r = r.strip()
                if r.startswith("|"): r = r[1:]
                if r.endswith("|"): r = r[:-1]
                return [c.strip() for c in r.split("|")]
            head = cells(ln)
            align = []
            for spec in cells(lines[i + 1]):
                align.append(' style="text-align:right"' if spec.endswith(":") and not spec.startswith(":")
                             else ' style="text-align:center"' if spec.startswith(":") and spec.endswith(":")
                             else "")
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(cells(lines[i])); i += 1
            h = "".join(f"<th{align[n] if n < len(align) else ''}>{inline(c)}</th>"
                        for n, c in enumerate(head))
            rows = "".join(
                "<tr>" + "".join(f"<td{align[n] if n < len(align) else ''}>{inline(c)}</td>"
                                 for n, c in enumerate(r)) + "</tr>" for r in body)
            out.append(f'<div class="wrapt"><table><thead><tr>{h}</tr></thead><tbody>{rows}</tbody></table></div>')
            continue

        # blockquote
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").lstrip()); i += 1
            out.append(f'<blockquote>{render(chr(10).join(buf))[0]}</blockquote>')
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if m:
            lvl, txt = len(m.group(1)), m.group(2).strip()
            a = slug(re.sub(r"[`*]", "", txt))[:60]
            if lvl == 2:
                toc.append((a, re.sub(r"[`*]", "", txt)))
            out.append(f'<h{lvl} id="{a}">{inline(txt)}</h{lvl}>')
            i += 1
            continue

        # hr
        if re.match(r"^\s*(-{3,}|\*{3,})\s*$", ln):
            out.append("<hr>"); i += 1; continue

        # list
        if re.match(r"^\s*([-*+]|\d+\.)\s+", ln):
            tag = "ol" if re.match(r"^\s*\d+\.", ln) else "ul"
            items, cur = [], None
            while i < len(lines) and (re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i])
                                      or (lines[i].startswith(("  ", "\t")) and lines[i].strip())):
                mm = re.match(r"^\s*(?:[-*+]|\d+\.)\s+(.*)$", lines[i])
                if mm:
                    if cur is not None: items.append(cur)
                    cur = mm.group(1)
                elif cur is not None:
                    cur += " " + lines[i].strip()
                i += 1
            if cur is not None: items.append(cur)
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue

        # paragraph — always consumes at least the current line, so the
        # cursor can never stall (a stray "|" line that is not a table used to
        # produce an empty buffer and loop forever).
        if ln.strip():
            buf = [ln]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(("#", ">", "```")) \
                    and not re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]) \
                    and not lines[i].strip().startswith("|") \
                    and not re.match(r"^\s*(-{3,}|\*{3,})\s*$", lines[i]):
                buf.append(lines[i]); i += 1
            out.append(f"<p>{inline(' '.join(buf))}</p>")
            continue
        i += 1
    return "".join(out), toc


# -------------------------------------------------------------------- shell
def page(title, body, toc=None, sub="", depth=0):
    up = "../" * depth
    nav = ""
    if toc:
        nav = ('<nav class="toc"><b>On this page</b>' +
               "".join(f'<a href="#{a}">{e(t)}</a>' for a, t in toc) + "</nav>")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} &middot; Lucernex Atlas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}../atlas.css">
<link rel="stylesheet" href="{up}research.css">
</head><body>
<header><b>Lucernex Atlas</b>
<nav><a href="{up}../index.html">Overview</a><a href="{up}../atlas.html#/map?set=feature">Feature map</a>
<a href="{up}../atlas.html">Interactive app</a>
<a href="{up}../entities/index.html">Record types</a><a href="{up}../rules/index.html">Rules</a>
<a href="{up}index.html" class="on">Research</a>
<a href="{up}../questions.html">Open questions</a></nav></header>
<main><p class="crumb"><a href="{up}../index.html">Atlas</a> &rsaquo;
<a href="{up}index.html">Research</a>{sub}</p>{nav}{body}</main></body></html>"""


CSS = """
.toc{display:block;margin:0 0 28px;padding:16px 18px;background:var(--card,#fff);
 border:1px solid var(--line,#e5e7eb);border-radius:10px}
.toc b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.08em;
 color:var(--muted,#6b7280);margin-bottom:8px}
.toc a{display:inline-block;margin:0 14px 6px 0;font-size:13px}
header nav a.on{color:var(--accent,#b4530a);font-weight:600}
main blockquote{margin:18px 0;padding:12px 18px;border-left:3px solid var(--accent,#b4530a);
 background:rgba(180,83,10,.05);border-radius:0 8px 8px 0}
main blockquote p{margin:0 0 8px}main blockquote p:last-child{margin:0}
main pre{background:#0f172a;color:#e2e8f0;padding:14px 16px;border-radius:8px;overflow-x:auto;
 font-size:12.5px;line-height:1.55;margin:16px 0}
main pre code{background:none;color:inherit;padding:0;font-size:inherit}
main del{color:var(--muted,#6b7280)}
.docgrid{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));margin:0 0 30px}
.doccard{display:block;padding:16px 18px;background:var(--card,#fff);border:1px solid var(--line,#e5e7eb);
 border-radius:10px;text-decoration:none;color:inherit}
.doccard:hover{border-color:var(--accent,#b4530a)}
.doccard h3{margin:0 0 6px;font-size:15px}
.doccard p{margin:0;font-size:13px;color:var(--muted,#6b7280);line-height:1.5}
.doccard .meta{margin-top:10px;font-size:11px;color:var(--muted,#6b7280);
 font-family:'IBM Plex Mono',monospace}
.shots{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}
.shots a{display:block;border:1px solid var(--line,#e5e7eb);border-radius:8px;overflow:hidden}
.shots img{width:100%;display:block}
.denselist{display:grid;gap:2px;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));margin:0 0 30px}
.denselist a{display:flex;justify-content:space-between;gap:12px;padding:7px 11px;font-size:13px;
 text-decoration:none;border-radius:6px;border:1px solid transparent}
.denselist a:hover{background:var(--card,#fff);border-color:var(--line,#e5e7eb)}
.denselist a span{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--muted,#6b7280)}
main details{margin:0 0 14px;border:1px solid var(--line,#e5e7eb);border-radius:10px;
 background:var(--card,#fff)}
main details summary{cursor:pointer;padding:12px 16px;font-weight:600;font-size:14px}
main details[open] summary{border-bottom:1px solid var(--line,#e5e7eb)}
main details .shots{padding:14px}
.shots span{display:block;padding:7px 9px;font-size:11px;
 font-family:'IBM Plex Mono',monospace;color:var(--muted,#6b7280)}
"""


# ------------------------------------------------------------------- sources
GROUPS = [
    ("The two tenants", "Read out of two live tenants — (ASG)American Freight and (ASG)BBW, "
                        "both on build 26.09.0.113. What the product does when it is actually running.",
     [("../tenants/bbw-vs-american-freight.md", "AF vs BBW — the full comparison",
       "27 sections. Every finding from exploring both tenants, including the corrections."),
      ("../tenants/CAPTURE-EXCLUSIONS.md", "Capture exclusions",
       "Routes that must never be screenshotted, and why.")]),
    ("How the product works", "Feature-by-feature accounts, written from what was observed.", None),
    ("Reference", "The API surface, and what is and is not covered.",
     [("../data-model/api/README.md", "The REST API, explained",
       "One generic CRUD controller for 227 types. 141 paths, 160 operations."),
      ("../COVERAGE.md", "Coverage tracker",
       "Every known surface, whether it is documented, and whether it is captured.")]),
]


def read(rel):
    p = os.path.normpath(os.path.join(DOCS, rel.lstrip("./").replace("../", "")))
    if not os.path.exists(p):
        p = os.path.normpath(os.path.join(HERE, rel))
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "research.css"), "w", encoding="utf-8").write(CSS)

    # Render the WHOLE markdown corpus, mirroring docs/ so cross-links resolve.
    SKIP = {"site", "mindmap", "assets"}
    srcs = []
    for root, dirs, files in os.walk(DOCS):
        dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")]
        for f in sorted(files):
            if f.endswith(".md"):
                srcs.append(os.path.relpath(os.path.join(root, f), DOCS))

    built = []
    for rel in sorted(srcs):
        md = open(os.path.join(DOCS, rel), encoding="utf-8").read()
        CUR["rel"] = rel
        body, toc = render(md)
        # The landing page of each directory is index.html, written by this
        # generator. A source doc whose name case-insensitively collides with it
        # (INDEX.md, the corpus master index) would silently overwrite it on a
        # case-insensitive filesystem and 404 on case-sensitive Pages.
        out_rel = rel[:-3] + ".html"
        if os.path.basename(out_rel).lower() == "index.html" and \
                os.path.basename(rel) != "README.md":
            out_rel = out_rel[:-len("index.html")] + "corpus-index.html"
        dest = os.path.join(OUT, out_rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        depth = rel.count(os.sep)
        m = re.search(r"^#\s+(.+)$", md, re.M)
        title = (m.group(1) if m else os.path.basename(rel)[:-3]).strip()
        title = re.sub(r"[`*]", "", title)
        open(dest, "w", encoding="utf-8").write(
            page(title, body, toc, f" &rsaquo; {e(title)}", depth))
        built.append((out_rel[:-5] + ".md", title, md.count(chr(10)) + 1))
        # links of the form "../some-folder/" expect a directory index
        if os.path.basename(rel).lower() == "readme.md":
            shutil.copyfile(dest, os.path.join(os.path.dirname(dest), "index.html"))

    # ----- index
    counts = {}
    for d in ("bbw-admin", "af-admin", "bbw-enduser"):
        p = os.path.join(DOCS, "assets", "screenshots", d)
        counts[d] = len(os.listdir(p)) if os.path.isdir(p) else 0
    tj = os.path.join(DOCS, "tenants")
    njson = len([f for f in os.listdir(tj) if f.endswith(".json")]) if os.path.isdir(tj) else 0

    def card(rel, label, desc):
        row = next((b for b in built if b[0] == rel), None)
        if not row:
            return ""
        return (f'<a class="doccard" href="{rel[:-3]}.html"><h3>{e(label)}</h3>'
                f'<p>{e(desc)}</p><div class="meta">{row[2]:,} lines</div></a>')

    b = ['<h1>Research</h1>',
         '<p class="lead">The atlas describes the schema. This describes the running product &mdash; '
         'what two live tenants actually do, where they differ, and what that means for a rebuild. '
         'Every claim is labelled Observed, Derived or Inferred, and corrections are left visible '
         'rather than tidied away.</p>',
         '<div class="stats">' + "".join(
             f'<div><b class="mono">{v}</b><span>{k}</span></div>' for k, v in
             [("Documents", len(built)), ("Screens", sum(counts.values())),
              ("Data captures", njson), ("Tenants", 2)]) + '</div>']

    b.append("<h2>Start here</h2><div class='docgrid'>")
    for rel, lab, desc in [
        ("tenants/bbw-vs-american-freight.md", "AF vs BBW — the full comparison",
         "27 sections. What one tenant has that the other does not, why a navigation root can be "
         "invisible, and how configuration is published between firms and then forks."),
        ("data-model/api/README.md", "The REST API, explained",
         "One generic CRUD controller for all 227 record types. 141 paths, 160 operations, and the "
         "envelope that makes HTTP 200 an unreliable success signal."),
        ("COVERAGE.md", "Coverage tracker",
         "Every known surface, whether it is documented, and whether it is captured."),
        ("INDEX.md", "Corpus index",
         "The master index to every document in the repository."),
    ]:
        b.append(card(rel, lab, desc))
    b.append("</div>")

    groups = [("features/", "How the product works",
               "Feature-by-feature accounts, written from what was observed in the tenants."),
              ("tenants/", "Tenant captures", "The two live tenants, and the rules for capturing them."),
              ("modules/", "Modules", "The original schema-derived module deep-dives."),
              ("data-model/", "Data model", "Objects, keys, types, APIs and the code-table registry."),
              ("admin/", "Administration screens", "Screen-by-screen admin documentation."),
              ("screens/", "End-user screens", "The product as a user meets it."),
              ("data-fields/", "Field catalogue", "Every Manage Data Fields leaf, per entity.")]
    done = set()
    for prefix, gtitle, blurb in groups:
        rows = [x for x in built if x[0].startswith(prefix) and x[0] not in done]
        if not rows:
            continue
        for r in rows:
            done.add(r[0])
        b.append(f"<h2>{e(gtitle)} &middot; {len(rows)}</h2><p>{e(blurb)}</p>")
        if len(rows) > 24:
            # Large, uniform sets (the per-entity field catalogue) read better as
            # a dense list than as 130 cards.
            b.append("<div class='denselist'>")
            for rel, title, lines in sorted(rows, key=lambda x: x[0]):
                b.append(f'<a href="{rel[:-3]}.html">{e(title[:58])}'
                         f'<span>{lines:,}</span></a>')
            b.append("</div>")
        else:
            b.append("<div class='docgrid'>")
            for rel, title, lines in sorted(rows, key=lambda x: x[1]):
                b.append(f'<a class="doccard" href="{rel[:-3]}.html"><h3>{e(title[:70])}</h3>'
                         f'<p>{e(rel)}</p><div class="meta">{lines:,} lines</div></a>')
            b.append("</div>")

    rest = [x for x in built if x[0] not in done]
    if rest:
        b.append(f"<h2>Everything else &middot; {len(rest)}</h2><div class='denselist'>")
        for rel, title, lines in sorted(rest, key=lambda x: x[0]):
            b.append(f'<a href="{rel[:-3]}.html">{e(title[:58])}<span>{lines:,}</span></a>')
        b.append("</div>")

    b.append("<h2>Screens</h2><p>Captured at each page's true width. These are ExtJS viewport "
             "apps &mdash; grids scroll internally, so a screenshot never shows more rows than the "
             "viewport held. Row counts in the data captures are authoritative; the images are not.</p>")
    for d, lab in (("bbw-enduser", "End-user screens (BBW)"),
                   ("bbw-admin", "Administration (BBW)"),
                   ("af-admin", "Administration (American Freight)")):
        p = os.path.join(DOCS, "assets", "screenshots", d)
        if not os.path.isdir(p):
            continue
        files = sorted(f for f in os.listdir(p) if f.endswith((".jpg", ".png")))
        b.append(f"<details><summary>{e(lab)} &middot; {len(files)}</summary><div class='shots'>")
        for f in files:
            src = f"../../assets/screenshots/{d}/{f}"
            b.append(f'<a href="{src}"><img loading="lazy" src="{src}" alt="{e(f)}">'
                     f'<span>{e(f)}</span></a>')
        b.append("</div></details>")

    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        page("Research", "".join(b)))
    print(f"research: {len(built)} pages, {sum(counts.values())} screens, {njson} data captures")


if __name__ == "__main__":
    main()
