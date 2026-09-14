#!/usr/bin/env python3
"""
Render vault/ to docs/site/vault/ — the same notes, readable on the web.

The vault is an Obsidian graph: small notes joined by [[wikilinks]]. Obsidian
resolves those by note *name*, anywhere in the tree. This turns them into real
hrefs so the identical files work in Obsidian, on GitHub, and on the site,
without a second copy.

Also emits a graph index: every note, its folder, and its link degree — the
web equivalent of Obsidian's graph view, which needs a running app.

Re-runnable: wipes and rewrites site/vault/ each time.
"""

import html
import os
import re
import shutil

import gate
import sitenav
import build_research
from build_research import CSS, brand, render, slug

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
ROOT = os.path.dirname(DOCS)
VAULT = os.path.join(ROOT, "vault")
OUT = os.path.join(DOCS, "site", "vault")

e = html.escape

# note name (lowercased, no extension) -> path relative to vault/
INDEX = {}


def page(title, body, depth=0, toc=None, sub=""):
    up = "../" * depth
    nav = ""
    if toc:
        nav = ('<nav class="toc"><b>On this page</b>' +
               "".join(f'<a href="#{a}">{e(t)}</a>' for a, t in toc) + "</nav>")
    return gate.inject(brand(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} &middot; Lx Vault</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{up}../atlas.css">
<link rel="stylesheet" href="{up}../research/research.css">
<link rel="stylesheet" href="{up}vault.css">
</head><body>
<header><b>Lx Atlas</b>
{sitenav.nav_html(up + "../", "vault")}</header>
<main><p class="crumb"><a href="{up}../index.html">Atlas</a> &rsaquo;
<a href="{up}index.html">Vault</a>{sub}</p>
<p class="viewfor">{e(sitenav.purpose("vault"))}</p>{nav}{body}</main></body></html>"""))


GRAPH_BODY = r"""
<h1>Graph</h1>
<p class="lead">Every note in the vault and every link between them. Drag to pan, scroll to zoom,
drag a node to pull it. Click a node to open it; hover to isolate its neighbours. Colour is folder.</p>
<div id="gwrap">
  <div id="gbar">
    <input id="gq" placeholder="Filter notes&hellip;" autocomplete="off">
    <span id="gcount"></span>
    <label><input type="checkbox" id="glab" checked> labels</label>
    <button id="gfit">Fit</button>
  </div>
  <canvas id="gcv"></canvas>
  <div id="gtip"></div>
</div>
<style>
#gwrap{position:relative;border:1px solid var(--line,#e5e7eb);border-radius:12px;overflow:hidden;
 background:#0f172a;margin:0 0 28px}
#gcv{display:block;width:100%;height:660px;cursor:grab}
#gcv.drag{cursor:grabbing}
#gbar{position:absolute;top:12px;left:12px;right:12px;z-index:5;display:flex;gap:10px;
 align-items:center;flex-wrap:wrap}
#gbar input[type=text],#gq{padding:7px 11px;border-radius:7px;border:1px solid #334155;
 background:rgba(15,23,42,.85);color:#e2e8f0;font-size:13px;width:210px}
#gbar label,#gcount{color:#94a3b8;font-size:12px;font-family:'IBM Plex Mono',monospace}
#gbar button{padding:7px 12px;border-radius:7px;border:1px solid #334155;background:rgba(15,23,42,.85);
 color:#e2e8f0;font-size:12px;cursor:pointer}
#gtip{position:absolute;pointer-events:none;display:none;background:#fff;color:#0f172a;
 padding:7px 10px;border-radius:7px;font-size:12px;box-shadow:0 6px 20px rgba(0,0,0,.3);max-width:270px}
</style>
<script>
(function(){
const cv=document.getElementById('gcv'),ct=cv.getContext('2d'),tip=document.getElementById('gtip');
let N=[],E=[],W=0,H=0,tx=0,ty=0,sc=1,hover=-1,drag=null,pan=null,q='',labels=true;
const PAL=['#f97316','#38bdf8','#a78bfa','#34d399','#fbbf24','#f472b6','#60a5fa','#4ade80',
           '#fb7185','#c084fc','#2dd4bf'];
let groups=[];
function resize(){const r=cv.getBoundingClientRect();W=cv.width=r.width*devicePixelRatio;
 H=cv.height=r.height*devicePixelRatio;ct.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);draw();}
fetch('graph.json').then(r=>r.json()).then(d=>{
 N=d.nodes;E=d.edges;
 groups=[...new Set(N.map(n=>n.g))].sort();
 N.forEach(n=>{const gi=groups.indexOf(n.g);
   n.c=PAL[gi%PAL.length];n.r=3.2+Math.min(10,Math.sqrt(n.d||0)*2.0);});
 document.getElementById('gcount').textContent=N.length+' notes  ·  '+E.length+' links';
 resize();fit();draw();
});
function step(){
 const k=0.0009;
 for(const n of N){n.vx-=n.x*k;n.vy-=n.y*k;}
 for(let i=0;i<N.length;i++){const a=N[i];
  for(let j=i+1;j<N.length;j++){const b=N[j];
   let dx=b.x-a.x,dy=b.y-a.y,d2=dx*dx+dy*dy;if(d2>360000||d2===0)continue;
   const f=2600/d2;const d=Math.sqrt(d2);dx/=d;dy/=d;
   a.vx-=dx*f;a.vy-=dy*f;b.vx+=dx*f;b.vy+=dy*f;}}
 for(const [i,j] of E){const a=N[i],b=N[j];
  let dx=b.x-a.x,dy=b.y-a.y,d=Math.sqrt(dx*dx+dy*dy)||1;
  const f=(d-105)*0.0042;dx/=d;dy/=d;
  a.vx+=dx*f;a.vy+=dy*f;b.vx-=dx*f;b.vy-=dy*f;}
 for(const n of N){if(n===drag)continue;n.x+=n.vx*=0.86;n.y+=n.vy*=0.86;}
}
function fit(){if(!N.length)return;
 const xs=N.map(n=>n.x),ys=N.map(n=>n.y);
 const x0=Math.min(...xs),x1=Math.max(...xs),y0=Math.min(...ys),y1=Math.max(...ys);
 const r=cv.getBoundingClientRect();
 sc=Math.min(r.width/(x1-x0+120),r.height/(y1-y0+120),2.2);
 tx=r.width/2-(x0+x1)/2*sc;ty=r.height/2-(y0+y1)/2*sc;}
function match(n){return !q||n.t.toLowerCase().includes(q)||n.id.toLowerCase().includes(q);}
function draw(){
 const r=cv.getBoundingClientRect();ct.clearRect(0,0,r.width,r.height);
 ct.save();ct.translate(tx,ty);ct.scale(sc,sc);
 const nb=new Set();
 if(hover>=0){nb.add(hover);for(const [i,j] of E){if(i===hover)nb.add(j);if(j===hover)nb.add(i);}}
 ct.lineWidth=0.7/sc;
 for(const [i,j] of E){const a=N[i],b=N[j];
  const on=hover<0?(match(a)&&match(b)):(nb.has(i)&&nb.has(j));
  ct.strokeStyle=on?'rgba(148,163,184,.55)':'rgba(148,163,184,.09)';
  ct.beginPath();ct.moveTo(a.x,a.y);ct.lineTo(b.x,b.y);ct.stroke();}
 for(let i=0;i<N.length;i++){const n=N[i];
  const on=hover<0?match(n):nb.has(i);
  ct.globalAlpha=on?1:0.16;ct.fillStyle=n.c;
  ct.beginPath();ct.arc(n.x,n.y,n.r,0,6.284);ct.fill();
  const lab=labels&&on&&(i===hover||(hover>=0&&nb.has(i))||n.d>=30||sc>1.9);
  if(lab){
   ct.globalAlpha=on?0.95:0.2;ct.fillStyle='#e2e8f0';
   ct.font=(10/sc<5?5:10/sc)+"px 'IBM Plex Sans',sans-serif";ct.textAlign='center';
   ct.fillText(n.t,n.x,n.y-n.r-3);}}
 ct.globalAlpha=1;ct.restore();}

function at(ev){const r=cv.getBoundingClientRect();
 const x=(ev.clientX-r.left-tx)/sc,y=(ev.clientY-r.top-ty)/sc;
 let best=-1,bd=1e9;
 for(let i=0;i<N.length;i++){const n=N[i];const d=(n.x-x)**2+(n.y-y)**2;
  if(d<Math.max(90,(n.r+5)**2)&&d<bd){bd=d;best=i;}}
 return {i:best,x,y};}
cv.addEventListener('mousemove',ev=>{
 if(pan){tx=pan.tx+ev.clientX-pan.x;ty=pan.ty+ev.clientY-pan.y;draw();return;}
 if(drag){const p=at(ev);drag.x=p.x;drag.y=p.y;draw();return;}
 const h=at(ev).i;if(h!==hover){hover=h;draw();}
 if(h>=0){const n=N[h];tip.style.display='block';
  tip.style.left=(ev.clientX-cv.getBoundingClientRect().left+14)+'px';
  tip.style.top=(ev.clientY-cv.getBoundingClientRect().top+14)+'px';
  tip.innerHTML='<b>'+n.t+'</b><br>'+n.g+' · '+n.d+' links';}
 else tip.style.display='none';});
cv.addEventListener('mousedown',ev=>{const p=at(ev);
 if(p.i>=0){drag=N[p.i];}else{pan={x:ev.clientX,y:ev.clientY,tx:tx,ty:ty};cv.classList.add('drag');}});
addEventListener('mouseup',()=>{drag=null;pan=null;cv.classList.remove('drag');});
cv.addEventListener('click',ev=>{const p=at(ev);if(p.i>=0&&!pan)location.href=N[p.i].u;});
cv.addEventListener('wheel',ev=>{ev.preventDefault();
 const r=cv.getBoundingClientRect(),mx=ev.clientX-r.left,my=ev.clientY-r.top;
 const f=ev.deltaY<0?1.12:0.893,ns=Math.max(0.15,Math.min(5,sc*f));
 tx=mx-(mx-tx)*(ns/sc);ty=my-(my-ty)*(ns/sc);sc=ns;draw();},{passive:false});
document.getElementById('gq').addEventListener('input',e=>{q=e.target.value.toLowerCase();draw();});
document.getElementById('glab').addEventListener('change',e=>{labels=e.target.checked;draw();});
document.getElementById('gfit').addEventListener('click',()=>{fit();draw();});
addEventListener('resize',resize);
})();
</script>
"""


VCSS = sitenav.NAV_CSS + """
.backlinks{margin:34px 0 0;padding:16px 18px;background:var(--card,#fff);
 border:1px solid var(--line,#e5e7eb);border-radius:10px}
.backlinks b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.08em;
 color:var(--muted,#6b7280);margin-bottom:8px}
.backlinks a{display:inline-block;margin:0 12px 6px 0;font-size:13px}
.fm{margin:0 0 22px;font-size:12px;color:var(--muted,#6b7280);
 font-family:'IBM Plex Mono',monospace}
.fm span{display:inline-block;padding:2px 8px;margin-right:6px;border-radius:20px;
 background:rgba(180,83,10,.09);color:var(--accent,#b4530a)}
.fm span.ev{background:rgba(15,23,42,.07);color:#334155}
a.wl{border-bottom:1px solid rgba(180,83,10,.35);text-decoration:none}
a.wl.missing{color:#b91c1c;border-bottom-style:dotted}
"""


def build_index():
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                rel = os.path.relpath(os.path.join(root, f), VAULT)
                INDEX[f[:-3].lower()] = rel
                INDEX[slug(f[:-3])] = rel


def resolve(target, from_rel):
    """[[Note]] or [[Note|label]] -> href relative to the current page."""
    key = target.strip().lower()
    hit = INDEX.get(key) or INDEX.get(slug(target.strip()))
    if not hit:
        return None
    frm = os.path.dirname(from_rel)
    return os.path.relpath(hit[:-3] + ".html", frm or ".").replace(os.sep, "/")


WIKI = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]")


def dewiki(md, rel, missing):
    """Rewrite wikilinks to markdown links before the markdown renderer runs."""
    def sub(m):
        tgt, label = m.group(1), m.group(2)
        href = resolve(tgt, rel)
        text = label or tgt
        if href is None:
            missing.add(tgt.strip())
            return f"**{text}**"      # unresolved: show the text, do not fake a link
        return f"[{text}]({href})"
    return WIKI.sub(sub, md)


def frontmatter(md):
    if not md.startswith("---"):
        return {}, md
    end = md.find("\n---", 3)
    if end == -1:
        return {}, md
    fm = {}
    for line in md[3:end].strip().split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip("[]")
    return fm, md[end + 4:]


def main():
    if not os.path.isdir(VAULT):
        print("vault/ not present — skipping")
        return
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "vault.css"), "w", encoding="utf-8").write(CSS + VCSS)

    # This module resolves its own hrefs; stop build_research adjusting them again.
    build_research.PASSTHROUGH["on"] = True
    build_index()
    notes, missing, links = [], set(), {}

    for key, rel in sorted(set(INDEX.items()), key=lambda x: x[1]):
        pass  # INDEX holds two keys per note; iterate files instead

    seen = set()
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, f), VAULT)
            if rel in seen:
                continue
            seen.add(rel)
            md = open(os.path.join(VAULT, rel), encoding="utf-8").read()
            fm, body_md = frontmatter(md)
            outbound = {t.strip() for t, _ in
                        ((m.group(1), m.group(2)) for m in WIKI.finditer(md))}
            links[rel] = outbound
            body_md = dewiki(body_md, rel, missing)
            # Rewrite link targets for the web copy.
            #
            # A vault note lives at vault/<d>/note.md and renders to
            # site/vault/<d>/note.html. Two destinations matter:
            #
            #   corpus markdown  docs/X.md  ->  site/research/X.html
            #   everything else  docs/X     ->  docs/X      (site root is docs/)
            #
            # Compute both from the note's own depth. Using the source link's
            # "../" prefix instead is what broke this before: the prefix is
            # correct for the repo layout, and adding to it compounds two
            # rewrites into six "../" where three are right.
            depth = rel.count(os.sep)
            to_site = "../" * (depth + 1)      # site/vault/<d>/ -> site/
            to_docs = "../" * (depth + 2)      # site/vault/<d>/ -> docs/

            def _docs_link(m):
                target = m.group(2)
                if target.endswith(".md"):
                    return f"]({to_site}research/{target[:-3]}.html)"
                return f"]({to_docs}{target})"

            # vault/assets is a symlink to docs/assets so that pointing
            # Obsidian at vault/ resolves images — a path escaping the vault
            # root does not render there. On the site the real location is the
            # docs root, which is (depth + 2) levels out.
            body_md = re.sub(r"\]\(((?:\.\./)*)assets/([^)]+?)\)",
                             lambda m: f"]({to_docs}assets/{m.group(2)})", body_md)

            # Any number of leading ../ then docs/… — the prefix is discarded.
            body_md = re.sub(r"\]\(((?:\.\./)*)docs/([^)]+?)\)", _docs_link, body_md)

            # Images NOT routed through docs/ are relative to the vault itself
            # and need no rewriting beyond their own depth.
            body_md = re.sub(
                r"\]\((?!https?:|#|/)((?:\.\./)*(?!.*/docs/)[^)]+\.(?:jpg|jpeg|png|gif|svg))\)",
                lambda m: f"]({m.group(1)})", body_md)
            body, toc = render(body_md)
            chips = ""
            if fm:
                bits = []
                if fm.get("tags"):
                    bits += [f"<span>{e(t.strip())}</span>"
                             for t in fm["tags"].split(",") if t.strip()]
                if fm.get("evidence"):
                    bits.append(f'<span class="ev">{e(fm["evidence"])}</span>')
                if bits:
                    chips = '<div class="fm">' + "".join(bits) + "</div>"
            title = fm.get("title") or (re.search(r"^#\s+(.+)$", body_md, re.M).group(1)
                                        if re.search(r"^#\s+(.+)$", body_md, re.M) else f[:-3])
            dest = os.path.join(OUT, rel[:-3] + ".html")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, "w", encoding="utf-8").write(
                page(re.sub(r"[`*]", "", title), chips + body, depth, toc,
                     f" &rsaquo; {e(re.sub(r'[`*]', '', title))}"))
            notes.append((rel, re.sub(r"[`*]", "", title), fm, len(outbound)))

    # backlinks
    back = {}
    for src, outs in links.items():
        for t in outs:
            hit = INDEX.get(t.lower()) or INDEX.get(slug(t))
            if hit:
                back.setdefault(hit, set()).add(src)

    # ----- index
    folders = {}
    for rel, title, fm, deg in notes:
        folders.setdefault(os.path.dirname(rel) or ".", []).append((rel, title, deg))
    total_links = sum(d for _, _, _, d in notes)
    b = ["<h1>Vault</h1>",
         '<p><a class="btn" href="graph.html">Open the graph &rarr;</a></p>',
         "<p class='lead'>The same corpus as a <em>graph</em>: small notes, each about one thing, "
         "joined by links. Open <code>vault/</code> in Obsidian for the graph view, or read it "
         "here &mdash; these are the identical files.</p>",
         '<div class="stats">' + "".join(
             f'<div><b class="mono">{v}</b><span>{k}</span></div>' for k, v in
             [("Notes", len(notes)), ("Links", total_links),
              ("Avg links/note", f"{total_links/max(len(notes),1):.1f}"),
              ("Folders", len(folders))]) + "</div>"]
    if missing:
        b.append(f"<div class='note'><b>{len(missing)} unresolved links.</b> These point at notes "
                 "that do not exist yet; they render as plain text rather than dead links: "
                 + ", ".join(f"<code>{e(x)}</code>" for x in sorted(missing)[:14])
                 + ("&hellip;" if len(missing) > 14 else "") + "</div>")
    for fold in sorted(folders):
        rows = sorted(folders[fold], key=lambda x: x[1])
        label = fold if fold != "." else "root"
        b.append(f"<h2>{e(label)} &middot; {len(rows)}</h2><div class='denselist'>")
        for rel, title, deg in rows:
            b.append(f'<a href="{rel[:-3]}.html">{e(title[:56])}<span>{deg}</span></a>')
        b.append("</div>")
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page("Vault", "".join(b)))

    # ----- graph data + the force-directed view
    nodes, idx = [], {}
    for rel, title, fm, deg in notes:
        idx[rel] = len(nodes)
        nodes.append({"id": rel[:-3], "t": title[:52],
                      "g": os.path.dirname(rel) or "root",
                      "u": rel[:-3] + ".html"})
    edges = []
    for src, outs in links.items():
        if src not in idx:
            continue
        for t in outs:
            hit = INDEX.get(t.lower()) or INDEX.get(slug(t))
            if hit and hit in idx and hit != src:
                edges.append([idx[src], idx[hit]])
    seen_e, uniq = set(), []
    for a, bb in edges:
        k = (min(a, bb), max(a, bb))
        if k not in seen_e:
            seen_e.add(k)
            uniq.append([a, bb])
    for n in nodes:
        n["d"] = 0
    for a, bb in uniq:
        nodes[a]["d"] += 1
        nodes[bb]["d"] += 1

    # Lay the graph out HERE, not in the browser. A live simulation over 422
    # nodes was unstable — it collapsed into a band and the result depended on
    # how long the tab had been open. Deterministic coordinates with proper
    # cooling give the same picture every time and load instantly; the browser
    # is left to pan, zoom and drag.
    import math
    import random
    rnd = random.Random(7)
    gs = sorted({n["g"] for n in nodes})
    # seed each folder in its own sector so clusters start apart
    for n in nodes:
        gi = gs.index(n["g"])
        a = (gi / max(len(gs), 1)) * math.tau + rnd.uniform(-0.28, 0.28)
        r = 300 + rnd.uniform(0, 230)
        n["x"], n["y"] = math.cos(a) * r, math.sin(a) * r

    adj = [[] for _ in nodes]
    for a, bb in uniq:
        adj[a].append(bb)
        adj[bb].append(a)

    AREA = 1500.0
    k = AREA / math.sqrt(max(len(nodes), 1))          # ideal separation
    temp = AREA / 6.0
    for it in range(320):
        dx = [0.0] * len(nodes)
        dy = [0.0] * len(nodes)
        for i in range(len(nodes)):
            xi, yi = nodes[i]["x"], nodes[i]["y"]
            for j in range(i + 1, len(nodes)):
                ex, ey = xi - nodes[j]["x"], yi - nodes[j]["y"]
                d2 = ex * ex + ey * ey
                if d2 < 1e-6:
                    ex, ey, d2 = rnd.uniform(-1, 1), rnd.uniform(-1, 1), 1.0
                if d2 > 9e6:
                    continue
                d = math.sqrt(d2)
                f = (k * k) / d
                dx[i] += ex / d * f; dy[i] += ey / d * f
                dx[j] -= ex / d * f; dy[j] -= ey / d * f
        for a, bb in uniq:
            ex = nodes[a]["x"] - nodes[bb]["x"]
            ey = nodes[a]["y"] - nodes[bb]["y"]
            d = math.hypot(ex, ey) or 0.01
            f = (d * d) / k
            dx[a] -= ex / d * f; dy[a] -= ey / d * f
            dx[bb] += ex / d * f; dy[bb] += ey / d * f
        for i, n in enumerate(nodes):
            d = math.hypot(dx[i], dy[i]) or 1.0
            n["x"] += dx[i] / d * min(d, temp)
            n["y"] += dy[i] / d * min(d, temp)
            n["x"] -= n["x"] * 0.0016          # gentle centring
            n["y"] -= n["y"] * 0.0016
        temp *= 0.975
    for n in nodes:
        n["x"] = round(n["x"], 1)
        n["y"] = round(n["y"], 1)

    import json as _json
    open(os.path.join(OUT, "graph.json"), "w", encoding="utf-8").write(
        _json.dumps({"nodes": nodes, "edges": uniq}, separators=(",", ":")))
    open(os.path.join(OUT, "graph.html"), "w", encoding="utf-8").write(
        page("Graph", GRAPH_BODY, 0, None, " &rsaquo; Graph"))
    print(f"graph: {len(nodes)} nodes, {len(uniq)} edges")

    # backlink blocks appended to each page
    for rel, title, fm, deg in notes:
        srcs = sorted(back.get(rel, []))
        if not srcs:
            continue
        p = os.path.join(OUT, rel[:-3] + ".html")
        s = open(p, encoding="utf-8").read()
        frm = os.path.dirname(rel)
        items = "".join(
            f'<a href="{os.path.relpath(sp[:-3] + ".html", frm or ".")}">'
            f'{e(os.path.basename(sp)[:-3])}</a>' for sp in srcs)
        s = s.replace("</main>", f'<div class="backlinks"><b>Linked from &middot; {len(srcs)}</b>'
                                 f'{items}</div></main>')
        open(p, "w", encoding="utf-8").write(s)

    print(f"vault: {len(notes)} notes, {total_links} links, "
          f"{total_links/max(len(notes),1):.1f} avg, {len(missing)} unresolved")


if __name__ == "__main__":
    main()
