#!/usr/bin/env python3
"""Generates admin/public/index.html (the Public pages list, grouped) and one developer spec page per entry under admin/spec/ and the /public + /admin/source routes in nginx.conf.

    python3 tools/build_admin.py

Add a page by adding an entry to PAGES (and its file to the Dockerfile COPY if it is new), then run this, commit and deploy.
"""
from pathlib import Path
import html, re

ROOT = Path(__file__).resolve().parent.parent          # versance-admin/
REPO = ROOT.parent                                      # the versance repo (page files live here)

# Folders served in place under /public/<mount>/ (so relative CSS keeps working): (mount, folder, pretty name -> file)
MOUNTS = [("extension", "browser-extension", {})]

def mounted(url):
    return next((m for m in MOUNTS if url == "/public/" + m[0] or url.startswith("/public/" + m[0] + "/")), None)

def P(name, slug, file, desc, parts, notes, target=None, files=(), spec=(), group=""):
    """files: extra source files shown in the developer box; spec: [(label, [bullet, ...])] rows of developer spec."""
    return dict(name=name, url="/public/" + slug, file=file, target=target or "/" + file, template=None, desc=desc, parts=parts, notes=notes, files=list(files), spec=list(spec), group=group)

TYPE = ("Typography", "/admin/system/typography/")
COLOUR = ("Colour", "/admin/system/colour/")
BTN = ("Buttons", "/admin/system/components/#buttons")
PILLS = ("Pills and tabs", "/admin/system/components/#pills")
TOG = ("Toggle and send", "/admin/system/components/#toggle")
FIELDS = ("Fields", "/admin/system/components/#fields")
RAIL = ("Icon rail", "/admin/system/components/#rail")
SURF = ("Pane, tile and card", "/admin/system/components/#surfaces")
TAGS = ("Source tags and severity", "/admin/system/components/#tags")
CITE = ("Citation, rows and info text", "/admin/system/components/#cite")
APPNAV = ("Web app sidebar", "/admin/system/components/#app-nav")
COMP = ("Web app composer", "/admin/system/components/#composer")
EXT_COMPONENTS = [BTN, PILLS, TOG, FIELDS, RAIL, SURF, TAGS, CITE]

def rd(path):
    return (REPO / path).read_text(encoding="utf-8", errors="replace")

def title_of(path):
    m = re.search(r"<title>(.*?)</title>", rd(path), re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

def states_of(path):
    return re.findall(r'data-state="([^"]+)"', rd(path))

GROUPS = {}   # gid -> dict(title, sub, open)
PAGES = []

# ---- web app and reference pages
GROUPS["web"] = dict(title="Web App", sub="versance.html (Talk to Edgar) and its copy in edgar/", open=True)
GROUPS["medicus"] = dict(title="Medicus", sub="Design example: the saved Medicus Pharma home page", open=True)
GROUPS["ext"] = dict(title="Browser Extension v1 – v13", sub="v1 is the baseline (part of the token set); v2 to v13 are design examples", open=True)
APP_SPEC = [
    ("About this page", [
        "The Versance web app mock-up (\"Talk to Edgar\"): a white 230px sidebar with a New button and pill nav items, a main area with the hero, the composer and cards",
        "Single self-contained file: one <style> block, inline SVG logo and favicon, one script; Figtree and Roboto Mono load from Google Fonts",
        "The :root block holds the light palette (white, #D9DDE5 lines, green #5AC47E accent, amber #E2B43D); a second :root holds the dark theme"]),
    ("Tokens", [
        "Part of the Versance token set: the :root blocks of this file (light, dark media query, data-theme dark and light) are generated from design-tokens/tokens.css through design-tokens/map.json (python3 tools/build_tokens.py); edit values in tokens.css, not here",
        "Source type colours: filing #2B40C5, news #E2B43D, transcript #334EFE, web #65728E, ask/compare #5AC47E, create #E2B43D"]),
]
PAGES += [
    P("Web app: Talk to Edgar", "web-app", "versance.html", "The Versance web app mock-up: sidebar, hero, composer, answer pages and source cards.", [TYPE, COLOUR, APPNAV, COMP, PILLS, TAGS],
      ["Part of the Versance token set (with style-v1): its :root blocks are generated from design-tokens/tokens.css", "Served from the repo as is"], spec=APP_SPEC, group="web"),
    P("Web app (copy in edgar/)", "edgar-web-app", "edgar/versance.html", "Byte-identical copy of versance.html kept in the edgar/ folder.", [TYPE, COLOUR, APPNAV, COMP],
      ["Identical to versance.html (verified); listed so every file in the repo has an entry"], spec=APP_SPEC, group="web"),
    P("Medicus Pharma home page (design example)", "medicus", "medicus-01.html", "A saved copy of the Medicus Pharma home page (WordPress), kept as a design example.", [],
      ["A design example: its CSS is only for this page and is not part of the Versance token set", "Third-party scripts and assets are referenced as saved"],
      spec=[("About this page", ["A saved WordPress page (Medicus Pharma) kept as a design example", "Its fonts, colours and scripts are the site's own; it is not styled by, and not part of, the Versance token set"])], group="medicus"),
]

# ---- the extension styles
def style_no(path):
    return int(re.search(r"style-v(\d+)", path.name).group(1))

STYLES = sorted((REPO / "browser-extension").glob("style-v*"), key=style_no)
DS_PAGES = [("specimen.html", "Specimen", "The style rendered live from its real components."),
            ("view-design-system.html", "Design system document", "Readable page for design-system.md: identity, colours, type, shape, layout, behaviour rules and screens."),
            ("view-tokens.html", "Tokens (tokens.css)", "Readable page for the style's tokens.css."),
            ("view-components.html", "Components (components.css)", "Readable page for the style's components.css.")]

for sdir in STYLES:
    n = style_no(sdir); sid = f"style-v{n}"; base = f"browser-extension/{sid}"
    md = rd(f"{base}/design-system/design-system.md").splitlines()
    name = (md[0].split("style v%d:" % n)[-1].strip() if md else sid)
    summary = next((l for l in md[1:6] if l.strip()), "")
    short = summary if len(summary) <= 90 else summary[:summary.rfind(" ", 0, 90)] + "…"
    GROUPS[sid] = dict(title=f"Style v{n}: {name}" + ("" if n == 1 else " (design example)"), sub=(short if n == 1 else "Design example. " + short), open=(n == 1), parent="ext")
    docs = [(f"Style v{n} tokens", f"/public/extension/{sid}/design-system/view-tokens.html"), (f"Style v{n} components", f"/public/extension/{sid}/design-system/view-components.html"),
            (f"Style v{n} document", f"/public/extension/{sid}/design-system/view-design-system.html")]
    style_files = [f"{base}/design-system/design-system.md", f"{base}/design-system/tokens.css", f"{base}/design-system/components.css"]
    if n == 1:
        role = ["Style v1 is the baseline and part of the Versance token set: its design-system/tokens.css is generated from versance-admin/design-tokens/tokens.css (python3 versance-admin/tools/build_tokens.py); edit values there, not here"]
    else:
        role = ["A design example / alternative: its CSS (tokens.css, components.css, screens.css) is only for its own pages and is not part of the Versance token set"]
    style_spec = ("About this style", [summary, f"Tokens, components and screens for this style live in {base}/ (design-system/, screens/, tools/)"] + role)
    for fname, label, desc in DS_PAGES:
        f = f"{base}/design-system/{fname}"
        PAGES.append(P(f"Style v{n}: {label}", f"extension/{sid}/design-system/{fname}", f, desc, docs + (EXT_COMPONENTS if n == 1 else []),
                       [f"Style v{n} ({name}) of the Versance browser-extension designs" + ("" if n == 1 else " (a design example, not part of the token set)"), "Served in place from browser-extension/ so its relative links keep working"],
                       files=[x for x in style_files if x != f], spec=[("About this page", [desc]), style_spec], group=sid))
    for sf in sorted((sdir / "screens").glob("VBE-*.html")):
        f = f"{base}/screens/{sf.name}"; ttl = title_of(f); states = states_of(f)
        label = re.sub(r"^VBE-(\d+[a-z]*)-(.*)\.html$", lambda m: f"VBE-{m.group(1)} " + m.group(2).replace("-", " "), sf.name)
        PAGES.append(P(f"Style v{n}: {label}", f"extension/{sid}/screens/{sf.name}", f,
                       f"{ttl}. Holds {len(states)} screen state{'s' if len(states) != 1 else ''}.", docs + (EXT_COMPONENTS if n == 1 else []),
                       [f"Style v{n} ({name}); title: {ttl}" + ("" if n == 1 else " (a design example, not part of the token set)"), "Served in place from browser-extension/ so its relative CSS keeps working"],
                       files=[f"{base}/screens/screens.css"] + style_files[1:], spec=[
                           ("Screens on this page", [f"{ttl}"] + [f"State: {s}" for s in states]),
                           ("Styling", ["Loads screens.css (this style's overrides) on top of the style's tokens.css and components.css (scoped to .vc-ext)",
                                        ("Style v1's tokens.css is generated from the Versance token set" if n == 1 else "This style's tokens are its own and may differ from the Versance token set; see the linked tokens page")]), style_spec], group=sid))

COMMON = dict(
    tokens=[("tokens.css", "/design-tokens/tokens.css"), ("fonts.css", "/design-tokens/fonts.css"), ("tokens.json", "/design-tokens/tokens.json"), ("DESIGN-TOKENS.md", "/design-tokens/DESIGN-TOKENS.md"), ("Token reference", "/admin/system/tokens/")],
    ai=[("AGENTS.md", "/admin/system/ai/AGENTS.md"), ("components.md", "/admin/system/ai/components.md"), ("design-tokens.md", "/admin/system/ai/design-tokens.md"), ("All AI files (.zip)", "/admin/system/ai/Versance-AI-Files.zip"), ("AI files page", "/admin/system/ai/")],
    skill=[("SKILL.md", "/admin/system/skills/versance-ui/SKILL.md"), ("rules.md", "/admin/system/skills/versance-ui/rules.md"), ("check.py", "/admin/system/skills/versance-ui/check.py"), ("starter.html", "/admin/system/skills/versance-ui/starter.html"), ("Skill (.zip)", "/admin/system/skills/versance-ui.zip")],
)

OUT = '<svg class="out" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"></path></svg>'

CODE_EXT = (".css", ".json", ".md", ".py", ".html")

def links(items):
    """Text files open in the inline code block (data-code); everything else opens in a new tab."""
    out = []
    for n, u in items:
        code = u.endswith(CODE_EXT) and not u.endswith("/")
        out.append(f'<a href="{u}" target="_blank" rel="noopener"{" data-code" if code else ""}>{html.escape(n)}</a>')
    return " ".join(out)

def spec_rows(p):
    e = html.escape
    return "\n".join(f'<tr><th>{e(label)}</th><td><ul>' + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul></td></tr>" for label, bullets in p["spec"])

CODEVIEW = '''<div class="codeview" hidden><div class="cvh"><span></span><button class="cvc" type="button" aria-label="Copy code"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"></path></svg></button><button class="cvx" type="button" aria-label="Close code"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></svg></button></div><pre><code></code></pre></div>'''

def spec_url(p):
    return "/admin/spec/" + re.sub(r"\.html$", "", p["url"][len("/public/"):]) + "/"

def route_text(p):
    e = html.escape
    return f'<code>{p["url"]}</code> (' + ("served in place from <code>" + e(mounted(p["url"])[1]) + "/</code>" if mounted(p["url"]) else "served from <code>" + e(p["target"]) + "</code>, URL unchanged") + ")"

def source_links(p):
    return "".join(f'<a href="/admin/source/{f}" target="_blank" rel="noopener" data-code>{html.escape(f)}</a>' for f in [p["file"]] + p["files"])

def row(p):
    """List row: the twisty only holds the route, the source files and the link to the page's developer spec."""
    e = html.escape
    return f'''<tr class="pg"><td class="tw"><button class="twisty" type="button" aria-expanded="false" aria-label="Show details for {e(p["name"])}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m10 17 5-5-5-5z"></path></svg></button></td>
<td><button class="pgname" type="button">{e(p["name"])}</button></td><td>{e(p["desc"])}</td><td><code>{e(p["file"])}</code></td><td><a class="ext" href="{p["url"]}" target="_blank" rel="noopener" aria-label="Open {p["url"]} in a new tab">{p["url"]}{OUT}</a></td></tr>
<tr class="dev" hidden><td></td><td colspan="4"><div class="devbox"><table class="kv">
<tr><th>Route</th><td>{route_text(p)}</td></tr>
<tr><th>Source file{"s" if p["files"] else ""}</th><td class="lk">{source_links(p)}</td></tr>
<tr><th>Developer spec</th><td class="lk"><a class="ilink" href="{spec_url(p)}">Open developer spec<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"></path></svg></a></td></tr>
</table>{CODEVIEW}</div></td></tr>'''

def spec_page(p):
    """Standalone developer spec page for one entry: everything a developer needs, with a link to share."""
    e = html.escape
    tmpl = f'<tr><th>Template</th><td><code>{e(p["template"])}</code></td></tr>' if p["template"] else ""
    sections = "".join(f'<section class="spec"><h2>{e(label)}</h2><ul>' + "".join(f"<li>{e(b)}</li>" for b in bullets) + "</ul></section>" for label, bullets in p["spec"])
    notes = "".join(f"<li>{e(n)}</li>" for n in p["notes"])
    shell = HEAD[:HEAD.index("<main>")].replace("<title>Versance Admin | Public</title>", f"<title>Versance Admin | Spec | {e(p['name'])}</title>")
    script = TAIL[TAIL.index("<script>"):TAIL.index("</script>") + len("</script>")]
    return f'''{shell}<main>
<p class="back"><a class="ilink" href="/admin/public"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></svg>Back to all pages</a></p>
<p class="crumb"><a href="/admin/public">Public</a> / Developer spec</p>
<h1>{e(p["name"])}</h1>
<p class="lead">{e(p["desc"])}</p>
<p class="actions"><a class="ilink" href="{p["url"]}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"></path></svg>Open the page</a><button class="ilink" type="button" id="copy-spec" data-url="{spec_url(p)}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></svg><span>Copy link to this spec</span></button></p>
<div class="card specs">{sections}<h2 class="refs">Files and references</h2><div class="devbox"><table class="kv">
<tr><th>Route</th><td>{route_text(p)}</td></tr>
<tr><th>Source file{"s" if p["files"] else ""}</th><td class="lk">{source_links(p)}</td></tr>{tmpl}
<tr><th>Components used</th><td class="lk">{links(p["parts"])}</td></tr>
<tr><th>Design tokens</th><td class="lk">{links(COMMON["tokens"])}</td></tr>
<tr><th>AI files</th><td class="lk">{links(COMMON["ai"])}</td></tr>
<tr><th>Claude skill</th><td class="lk">{links(COMMON["skill"])}</td></tr>
<tr><th>Notes</th><td><ul>{notes}</ul></td></tr>
</table>{CODEVIEW}</div></div>
{script}
<script>document.getElementById("copy-spec").addEventListener("click",function(){{var b=this,l=b.querySelector("span"),u=location.origin+b.dataset.url,o=l.textContent;(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).catch(function(){{var x=document.createElement("textarea");x.value=u;document.body.appendChild(x);x.select();document.execCommand("copy");x.remove();}});l.textContent="Link copied";setTimeout(function(){{l.textContent=o;}},1500);}});</script>
</main>
<script src="/admin/menu.js"></script>
</body>
</html>
'''

HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Versance Admin | Public</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/design-tokens/fonts.css">
<link rel="stylesheet" href="/design-tokens/tokens.css">
<link rel="stylesheet" href="/admin/admin.css">
</head>
<body class="white">
<aside class="side">
  <a class="logo" href="/admin/"><img src="/admin/system/logo-white.svg" alt="Versance"></a>
  <button class="menubtn" type="button" aria-label="Show the admin menu" aria-expanded="false" aria-controls="admin-nav"><svg class="i-chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z"></path></svg></button>
  <hr>
  <nav id="admin-nav" aria-label="Admin">
    <div class="navrow"><a href="/admin/system">System</a><a class="navout" href="/admin/system/?bare" target="_blank" rel="noopener" aria-label="Open the design system on its own in a new tab" title="Open the design system on its own"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"></path></svg></a></div>
    <a href="/admin/public" aria-current="page">Public</a>
  </nav>
</aside>
<main>
<h1>Public</h1>
<p class="lead">The Versance web app and the browser-extension designs (styles v1 to v13). Open the twisty for a page's route and source files, or open its developer spec: one shareable page with everything a developer needs. Add a page in <code>versance-admin/tools/build_admin.py</code>.</p>
<div class="card"><table class="list"><thead><tr><th class="tw"></th><th>Page</th><th>Description</th><th>File</th><th>Link</th></tr></thead><tbody>
'''
TAIL = '''</tbody></table></div>
<script>
var COPY="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z",TICK="M9 16.17 4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z";
document.addEventListener("click",function(e){
 var gt=e.target.closest(".gtoggle");if(gt){gt.setAttribute("aria-expanded",String(gt.getAttribute("aria-expanded")!=="true"));var open={};document.querySelectorAll(".gtoggle").forEach(function(h){open[h.dataset.g]=h.getAttribute("aria-expanded")==="true";});document.querySelectorAll("tr[data-group]").forEach(function(r){var p=r.getAttribute("data-parent"),closed=!open[r.dataset.group]||(p&&!open[p]);if(closed)r.setAttribute("data-collapsed","");else r.removeAttribute("data-collapsed");});return;}
 var a=e.target.closest("a[data-code]");
 if(a){e.preventDefault();var v=a.closest(".devbox").querySelector(".codeview"),code=v.querySelector("code");v.hidden=false;v.querySelector(".cvh span").textContent=a.textContent;code.textContent="Loading...";
  fetch(a.getAttribute("href")).then(function(r){return r.text();}).then(function(t){code.textContent=t;v.querySelector("pre").scrollTop=0;}).catch(function(){code.textContent="Could not load "+a.getAttribute("href");});return;}
 var cx=e.target.closest(".cvx");if(cx){cx.closest(".codeview").hidden=true;return;}
 var cc=e.target.closest(".cvc");
 if(cc){var t=cc.closest(".codeview").querySelector("code").textContent,p=cc.querySelector("path");(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).catch(function(){var x=document.createElement("textarea");x.value=t;document.body.appendChild(x);x.select();document.execCommand("copy");x.remove();});p.setAttribute("d",TICK);setTimeout(function(){p.setAttribute("d",COPY);},1500);return;}
 var pn=e.target.closest(".pgname");if(pn){pn.closest("tr").querySelector(".twisty").click();return;}
 var b=e.target.closest(".twisty");if(!b)return;var d=b.closest("tr").nextElementSibling,o=b.getAttribute("aria-expanded")==="true";b.setAttribute("aria-expanded",String(!o));d.hidden=o;});
</script>
</main>
<script src="/admin/menu.js"></script>
</body>
</html>
'''
CHEV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m10 17 5-5-5-5z"></path></svg>'

def list_rows():
    out, cur, opened = [], None, set()
    def header(g):
        info = GROUPS[g]; par = info.get("parent")
        n = sum(1 for q in PAGES if q["group"] == g or GROUPS[q["group"]].get("parent") == g)
        cls = "grp sub" if par else "grp"
        hide = f' data-group="{par}"' + ("" if GROUPS[par]["open"] else " data-collapsed") if par else ""
        return (f'<tr class="{cls}"{hide}><th colspan="5"><button type="button" class="gtoggle" data-g="{g}" aria-expanded="{str(info["open"]).lower()}">{CHEV}'
                f'<span>{html.escape(info["title"])}</span><span class="gsub">{html.escape(info["sub"])}</span><span class="gcount">{n} page{"" if n == 1 else "s"}</span></button></th></tr>')
    for p in PAGES:
        g = p["group"]
        if g != cur:
            cur = g; par = GROUPS[g].get("parent")
            if par and par not in opened:
                out.append(header(par)); opened.add(par)
            out.append(header(g)); opened.add(g)
        par = GROUPS[g].get("parent")
        closed = (not GROUPS[g]["open"]) or (par and not GROUPS[par]["open"])
        mark = " data-collapsed" if closed else ""
        pa = f' data-parent="{par}"' if par else ""
        r = row(p)
        r = r.replace('<tr class="pg">', f'<tr class="pg" data-group="{g}"{pa}{mark}>', 1).replace('<tr class="dev" hidden>', f'<tr class="dev" hidden data-group="{g}"{pa}{mark}>', 1)
        out.append(r)
    return "\n".join(out)

(ROOT / "admin/public/index.html").write_text(HEAD + list_rows() + TAIL)
import shutil
shutil.rmtree(ROOT / "admin/spec", ignore_errors=True)
for p in PAGES:
    out = ROOT / spec_url(p).strip("/")
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(spec_page(p))
print("built admin/public/index.html and", len(PAGES), "spec pages")

# nginx: /public/<slug> redirects to the page's real path; /admin/source/<file> shows the source as plain text (only listed files)
lines = []
for mount, folder, pretty in MOUNTS:
    base = f"/public/{mount}"
    lines.append(f"  location = {base} {{ return 301 {base}/; }}")
    for name, f in pretty.items():
        lines.append(f"  location = {base}/{name} {{ rewrite ^ {base}/{f} last; }}")
    lines.append(f"  location ^~ {base}/ {{ alias /usr/share/nginx/html/{folder}/; index index.html; }}")
# single files: served at their /public/ URL (internal rewrite, no redirect) and not reachable at the root any more
lines += [f"  location = {p['url']} {{ rewrite ^ {p['target']} break; }}" for p in PAGES if not mounted(p["url"])]
lines += [f"  location = {p['target']} {{ internal; }}" for p in PAGES if not mounted(p["url"])]
lines += ["  location = /public { try_files /index.html =404; }",
          "  location = /public/ { try_files /index.html =404; }"]
routes = "\n".join(lines)
explicit = [f for f in dict.fromkeys(f for p in PAGES for f in [p["file"]] + p["files"]) if not f.startswith("browser-extension/")]
src = "|".join(["browser-extension/style-v[0-9]+/(?:screens|design-system)/[A-Za-z0-9._-]+"] + [f.replace(".", r"\.") for f in explicit])
block = f"  # BEGIN generated by tools/build_admin.py\n{routes}\n  location ~ ^/admin/source/({src})$ {{ alias /usr/share/nginx/html/$1; types {{ }} default_type \"text/plain; charset=utf-8\"; }}\n  # END generated"
ng = (ROOT / "nginx.conf").read_text()
ng = re.sub(r"  # BEGIN generated.*?# END generated", lambda m: block, ng, flags=re.S)
(ROOT / "nginx.conf").write_text(ng)
print("updated nginx.conf routes")
