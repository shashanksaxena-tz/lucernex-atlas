"""
The access gate injected into every published page.

READ THIS BEFORE RELYING ON IT.

This is a **client-side gate, not security.** The site is static files on
GitHub Pages; there is no server to check a password against. Anyone can read
the credential in the page source, disable JavaScript, or fetch the HTML
directly with curl and see everything. It stops a casual visitor who lands on
the URL. It stops nothing else.

If the corpus genuinely must not be public, the answer is to make the
repository private and publish somewhere with real authentication — not to
strengthen this.

Kept in one place so the gate is identical on every page and can be removed in
one edit.
"""

USER = "admin"
PASS = "admin"

GATE = """<style id="lxg">body{visibility:hidden}
#lxgate{visibility:visible;position:fixed;inset:0;z-index:9999;display:flex;
align-items:center;justify-content:center;background:#0f172a;
font-family:'IBM Plex Sans',system-ui,sans-serif}
#lxgate form{background:#fff;padding:30px 32px;border-radius:12px;width:310px;
box-shadow:0 20px 60px rgba(0,0,0,.35)}
#lxgate h2{margin:0 0 4px;font-size:19px;color:#0f172a}
#lxgate p{margin:0 0 18px;font-size:12.5px;color:#64748b;line-height:1.5}
#lxgate label{display:block;font-size:11px;text-transform:uppercase;
letter-spacing:.07em;color:#64748b;margin:0 0 5px}
#lxgate input{width:100%;box-sizing:border-box;padding:9px 11px;margin:0 0 14px;
border:1px solid #cbd5e1;border-radius:7px;font-size:14px}
#lxgate button{width:100%;padding:10px;border:0;border-radius:7px;
background:#b4530a;color:#fff;font-size:14px;font-weight:600;cursor:pointer}
#lxgate .err{color:#b91c1c;font-size:12px;margin:0 0 10px;display:none}</style>
<div id="lxgate"><form onsubmit="return lxg(event)">
<h2>Lx Atlas</h2>
<p>Internal documentation. Not a security boundary &mdash; see
<code>gate.py</code>.</p>
<p class="err" id="lxge">Incorrect.</p>
<label for="lxgu">User</label><input id="lxgu" autocomplete="username" autofocus>
<label for="lxgp">Password</label><input id="lxgp" type="password"
autocomplete="current-password">
<button type="submit">Enter</button></form></div>
<script>
function lxgOpen(){var g=document.getElementById('lxgate');if(g)g.remove();
var s=document.getElementById('lxg');if(s)s.remove();
document.body.style.visibility='visible';}
function lxg(ev){ev.preventDefault();
if(document.getElementById('lxgu').value==='__USER__'&&
   document.getElementById('lxgp').value==='__PASS__'){
 try{sessionStorage.setItem('lxg','1');}catch(e){}
 lxgOpen();return false;}
document.getElementById('lxge').style.display='block';return false;}
try{if(sessionStorage.getItem('lxg')==='1')
 document.addEventListener('DOMContentLoaded',lxgOpen);}catch(e){}
</script>""".replace("__USER__", USER).replace("__PASS__", PASS)


def inject(html):
    """Insert the gate as early in the document as possible.

    Not every shell in this repo writes an explicit <body> — the interactive
    app does not — so fall back to after </head>, then to the top of the
    document. The CSS targets `body`, which the browser implies either way.
    """
    if 'id="lxgate"' in html:
        return html
    for anchor in ("<body>", "</head>"):
        i = html.find(anchor)
        if i != -1:
            i += len(anchor)
            return html[:i] + GATE + html[i:]
    m = html.find(">", html.find("<html"))
    if m != -1:
        return html[:m + 1] + GATE + html[m + 1:]
    return GATE + html
