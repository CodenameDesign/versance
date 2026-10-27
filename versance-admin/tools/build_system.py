#!/usr/bin/env python3
"""Builds the Versance Developer System (system/) and its AI files from design-tokens/tokens.css plus the data below.

    python3 tools/build_system.py

Writes system/**/index.html, system/ai/*.md, system/ai/Versance-AI-Files.zip, system/skills/versance-ui/ (+ .zip),
design-tokens/tokens.json and design-tokens/DESIGN-TOKENS.md. Nothing in system/ except system.css is hand-written. Logos: logos/*.svg are the sources; the build writes system/logos/ (black and white copies) and /versance-logo.svg.
Edit tokens.css or the data below, run the script, commit.
"""
import json, html, re, subprocess, sys, zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tokens_lib as T

ROOT = Path(__file__).resolve().parent.parent
SYS = ROOT / "system"
SITE = ""          # set to the deployed origin (no trailing slash) to make the skill's links absolute; empty = same-origin paths
VERSION = "1.0"
CSS_TOKENS = (ROOT / "design-tokens/tokens.css").read_text()
SOURCES = T.SOURCES
E = html.escape

# ---------------------------------------------------------------- data (tokens come from tokens.css)
SECTIONS = [("", "Overview"), ("typography", "Typography"), ("colour", "Colour"), ("logos", "Logos"), ("foundations", "Foundations"),
            ("components", "Components"), ("tokens", "Design tokens"), ("ai", "AI files")]

COLOUR_BLURBS = {
    "Color: text": ("Text", "Black text, muted blue-grey for labels, a fainter grey for placeholders. Same values in the web app and the extension."),
    "Color: brand (extension indigo)": ("Brand (extension indigo)", "One accent, #324EFE, for every accent role in the extension; pale tints cover hover, selected and disabled."),
    "Color: surfaces and lines": ("Surfaces and lines", "White surfaces, a #F9F9F9 pane, #F3F5F9 fills and #D9DDE5 hairlines. #0A1922 is the one near-black."),
    "Color: status": ("Status", "Severity colours come from the extension; the green family from the web app."),
    "Color: source tags": ("Source tags", "The coloured tags that say where an answer came from (filing, transcript, web)."),
    "Color: web app (versance.html)": ("Web app (versance.html)", "The web app's own values: white sidebar, light-blue active item and its green accent."),
    "Color: web app dark theme (reference only: the admin is light)": ("Web app dark theme", "Reference only. The web app ships a dark theme; the admin and the extension designs are light."),
}

# (token suffix, weight, use) in display order
TYPE_SCALE = [("title", 700, "Page title (the web app hero)"), ("lg", 700, "Help title in the extension"), ("md", 400, "Body text, table text"),
              ("nav", 600, "Sidebar items in the admin"), ("thead", 600, "Table head: uppercase, letter-spaced"), ("caption", 400, "Captions, code badges")]

FOUNDATIONS = {
    "radius": [("cite", "Citation chip"), ("tag", "Source tags"), ("sm", "Buttons, small cards"), ("box", "Inputs, tab strip, rail buttons"), ("panel", "Cards and tiles"), ("pill", "Pills, tabs, sidebar items, toggles"), ("round", "Icon buttons, send button")],
    "shadow": [("--shadow-sm", "Resting card in the web app"), ("--shadow", "Composer, menus and popovers"), ("--shadow-lg", "Dialogs and the System menu drawer (ours)")],
}

# Components: (id, title, blurb, specimen html, spec rows, snippet)
COMPONENTS = [
    ("shell", "Admin shell", "Dark left nav with the Versance logo and pill items, and a content area. Collapses to a top bar below 720px, where the menu opens inside the header and pushes the page down.",
     '<div class="sp-side"><img src="/admin/system/logos/versance-lock-up-white.svg" alt=""><hr><span class="on">System</span><span>Public</span></div>',
     [("Sidebar", "fill var(--color-ink), width var(--sidebar-width) (the web app's 230px), sticky and full height; logo 160px wide, padding 24px"),
      ("Item", "pill (var(--radius-pill)), 13px / 600, padding 7.5px 12px, 12px side margin, hover white at 12%, 120ms"),
      ("Active item", "white at 18% fill; no side bar"),
      ("Main", "padding var(--page-padding), white on the Public and System pages"),
      ("Mobile", "at 720px the sidebar becomes a 64px top bar; the arrow button opens the menu inside the header")],
     ".side{width:var(--sidebar-width);background:var(--color-ink);color:var(--color-surface)}\n.side nav a{margin:0 12px 4px;padding:7.5px 12px;border-radius:var(--radius-pill);font:600 var(--font-size-nav)/var(--line-height-nav) var(--font-family)}"),
    ("buttons", "Buttons", "Extension buttons: 8px radius, 14px text. One primary, an outline for secondary actions, a near-black pill.",
     '<span class="sp-btn p">Export Report</span><span class="sp-btn o">Export Conversation</span><span class="sp-btn">Cancel</span><span class="sp-btn dark">Web Search On</span><span class="sp-btn p off">Disabled</span>',
     [("Base", "padding var(--pad-btn), 1px var(--color-border) border, radius var(--radius-sm), var(--font-size-md); hover border and text var(--color-primary), 120ms"),
      ("Primary (.p)", "fill var(--color-primary), white text; hover var(--color-primary-hover); pressed var(--color-primary-dark)"),
      ("Primary disabled", "fill var(--color-primary-tint-25), white text, not-allowed"),
      ("Outline (.o)", "var(--color-primary) text, 1px var(--color-primary-tint-25) border; disabled tints lighter"),
      ("Dark pill (.dark)", "fill var(--color-ink), white text, radius var(--radius-pill): the one deliberate non-indigo control (Web Search On)"),
      ("Tile button", "var(--color-surface-alt) fill, no border, full width (Upload a document)"),
      ("Focus", "var(--focus-ring) with a 2px offset on every button, link and role=button")],
     ".btn{display:inline-flex;align-items:center;gap:6px;padding:var(--pad-btn);border:1px solid var(--color-border);border-radius:var(--radius-sm);transition:border-color var(--duration-fast),color var(--duration-fast)}\n.btn:hover{border-color:var(--color-primary);color:var(--color-primary)}\n.btn.p{background:var(--color-primary);border-color:var(--color-primary);color:#fff}\n.btn.p:hover{background:var(--color-primary-hover)}"),
    ("pills", "Pills and tabs", "Pill-shaped chips and tabs. Selected state is the pale indigo tint.",
     '<span class="sp-cpill">Web Search</span><span class="sp-cpill sel">Filings</span><span class="sp-tabs"><span class="on">Chat</span><span>History</span></span>',
     [("Pill", "padding var(--pad-pill), radius var(--radius-pill), var(--color-surface-alt) fill, var(--color-text-muted) text; hover var(--color-border) fill and black text"),
      ("Selected pill", "var(--color-primary-tint-15) fill, var(--color-primary) text, weight 600"),
      ("Tab strip", "4px padding, #E6E6E6 fill, radius var(--radius-box); tab padding 4px 12px, pill radius; active tab white with black text"),
      ("Web app pill (.cpill.on)", "var(--color-success-bg) fill and var(--color-success-text) text, 12.5px")],
     ".cpill{display:inline-flex;gap:7px;padding:var(--pad-pill);border-radius:var(--radius-pill);background:var(--color-surface-alt);color:var(--color-text-muted)}\n.cpill.is-selected{background:var(--color-primary-tint-15);color:var(--color-primary);font-weight:600}"),
    ("toggle", "Toggle and send", "The 26 x 15 toggle and the round send button.",
     '<span class="sp-tog"></span><span class="sp-tog on"></span><span class="sp-send"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" stroke="#fff" stroke-width="2" fill="none"/></svg></span><span class="sp-send off"><svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" stroke="#fff" stroke-width="2" fill="none"/></svg></span>',
     [("Toggle", "26 x 15px, radius var(--radius-pill), var(--color-border) off, var(--color-primary) on; 11px white knob, 2px inset, 180ms; the web app's on colour is var(--color-success)"),
      ("Send", "36px circle, var(--color-primary) fill, white icon; hover var(--color-primary-hover); disabled var(--color-primary-tint-25) until there is content"),
      ("Web app send", "var(--color-success-bg) fill with var(--color-success-text) icon; hover fills var(--color-success) with white")],
     ".tog{width:26px;height:15px;border-radius:var(--radius-pill);background:var(--color-border)}\n.tog.on{background:var(--color-primary)}\n.send-btn{width:36px;height:36px;border-radius:50%;background:var(--color-primary);color:#fff}"),
    ("fields", "Fields", "Text input and select: 10px radius, 1px border that turns indigo on focus (no ring).",
     '<div class="sp-field">Search filings</div><div class="sp-field on">Edgar</div>',
     [("Field", "padding 10px 14px, 1px var(--color-border) border, radius var(--radius-box), white; placeholder var(--color-text-faint) italic"),
      ("Focus", "border var(--color-primary) only: no outline, no offset"),
      ("Select", "padding 12px 14px, same border and radius; keeps the focus ring")],
     ".field{width:100%;padding:10px 14px;border:1px solid var(--color-border);border-radius:var(--radius-box)}\n.field:focus{border-color:var(--color-primary);outline:none}"),
    ("rail", "Icon rail", "The extension's vertical rail of 30px icon buttons, with a count badge.",
     '<div class="sp-rail"><span class="b">&#9679;</span><span class="b on">&#9679;<i>3</i></span><span class="b">&#9679;</span></div>',
     [("Rail", "var(--rail-width) wide, 10px gap, centred"),
      ("Button", "30px, radius var(--radius-box), white; hover var(--color-primary-tint-8); active var(--color-primary) fill with white icon"),
      ("Badge", "14px minimum, var(--color-primary) fill, white 9px / 700, top-right; on the active button it inverts (white fill, indigo text)")],
     ".rail-btn{width:30px;height:30px;border-radius:var(--radius-box)}\n.rail-btn.active{background:var(--color-primary);color:#fff}"),
    ("surfaces", "Pane, tile and card", "Surfaces in the extension: the grey tool pane, dismissible tiles and bordered cards.",
     '<div class="sp-tile">Upload a document to start<i>&times;</i></div><div class="sp-card">Primary company filings</div>',
     [("Pane", "var(--color-page-bg) (#F9F9F9)"), ("Tile", "var(--color-surface-alt) fill, radius var(--radius-panel), padding 16px 40px 16px 16px; a 20px round close button top right (indigo, hover var(--color-primary-tint-15))"),
      ("Info tile", "white with a 1px var(--color-surface-alt) border"), ("Card", "white, 1px var(--color-border) border, radius var(--radius-panel), padding 12px 14px"),
      ("Web app card", "var(--color-surface-alt) fill, radius 16px, padding 18px 20px, 13px / 600 muted heading")],
     ".card{background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-panel);padding:12px 14px}"),
    ("tags", "Source tags and severity", "Small solid tags for the source of an answer, and uppercase severity pills.",
     '<span class="sp-tg f">FILING</span><span class="sp-tg t">TRANSCRIPT</span><span class="sp-tg w">WEB</span><span class="sp-tg n">NEWS</span><span class="sp-risk h">High</span><span class="sp-risk m">Medium</span>',
     [("Source tag", "10px / 700, letter-spacing .4px, white on colour, padding 3px 8px, radius var(--radius-tag)"),
      ("Colours", "filing var(--color-primary) (the web app uses var(--color-tag-filing-app)), transcript var(--color-tag-transcript), web var(--color-text-muted), news var(--color-amber)"),
      ("Severity", "12px / 700 uppercase, letter-spacing .02em, white on colour, padding 4px 10px, pill; High var(--color-danger), Medium var(--color-warning)"),
      ("Low risk", "no style is defined: no reference design shows one")],
     ".tg{font:700 10px var(--font-family);letter-spacing:.4px;padding:3px 8px;border-radius:var(--radius-tag);color:#fff}\n.risk{font:700 12px var(--font-family);text-transform:uppercase;padding:4px 10px;border-radius:var(--radius-pill);color:#fff}"),
    ("cite", "Citation, rows and info text", "The inline citation chip, document rows and the indigo help text.",
     '<span class="sp-info">Help title</span><p class="sp-line">Revenue grew 12%<span class="sp-cite">1</span></p><div class="sp-docrow"><span>10-K 2025</span><span class="d">Mar 3, 2026</span></div>',
     [("Citation", "16px minimum, var(--color-primary-tint-15) fill, var(--color-primary) 10px / 700, radius var(--radius-cite)"),
      ("Doc row", "padding 10px 4px, 1px var(--color-surface-alt) divider; hover var(--color-primary-tint-8); date in var(--color-text-muted), tabular numbers"),
      ("Info text", "var(--color-primary); title 18px / 700 (line 1.25), sub-heads 14px / 700"),
      ("Link", "var(--color-primary), underlined; hover var(--color-primary-hover)")],
     ".cite{min-width:16px;height:16px;padding:0 4px;background:var(--color-primary-tint-15);color:var(--color-primary);border-radius:var(--radius-cite);font:700 10px var(--font-family)}"),
    ("app-nav", "Web app sidebar", "The web app's white sidebar: the New button and the pill nav items (these are the web app's own values, not the admin's).",
     '<div class="sp-app"><span class="nb new"><i>+</i>New chat</span><span class="nb on">Ask Edgar</span><span class="nb">Filings</span></div>',
     [("Sidebar", "230px wide, var(--color-surface), padding 20px, hairline var(--color-border) on the right"),
      ("New button", "pill, var(--color-surface-alt) fill, 13px / 500, a 20px black round plus icon; hover var(--color-border)"),
      ("Nav button", "pill, 14px, var(--color-text-muted); hover var(--color-surface-alt) and black; 6px gap between items"),
      ("Active", "var(--app-nav-active) (#C7E2F0) fill, black text, weight 600")],
     ".navbtn{display:flex;gap:9px;padding:7.5px 10px;border-radius:999px;color:var(--color-text-muted)}\n.navbtn.active{background:var(--app-nav-active);color:#000;font-weight:600}"),
    ("composer", "Web app composer", "The web app's message box: 20px radius, mono text, pill row below.",
     '<div class="sp-comp"><span>Ask about a company&hellip;</span><b>&#8593;</b></div>',
     [("Box", "white, 1px var(--color-border) border, radius 20px, var(--shadow), padding 16px 16px 13px"),
      ("Text", "var(--font-family-mono) 15px / 1.55, placeholder var(--color-text-faint)"),
      ("Send", "36px circle bottom right, var(--color-success-bg) fill, var(--color-success-text) icon")],
     ".composer{background:#fff;border:1px solid var(--color-border);border-radius:20px;box-shadow:var(--shadow);padding:16px 16px 13px}"),
    ("ilink", "Icon link", "The admin's quiet action: a text link with an 18px icon, no fill or border.",
     '<span class="sp-ilink"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>Open developer spec</span>',
     [("Text", "var(--font-size-md) / 600, var(--color-primary), no underline at rest"), ("Icon", "18px Material icon in currentColor, 4px from the text"),
      ("Hover", "var(--color-primary-hover) with a 2px-offset underline, 150ms"), ("Focus", "2px outline var(--color-primary)"), ("Where", "versance-admin/admin/admin.css (.ilink)")],
     ".ilink{display:inline-flex;align-items:center;gap:var(--space-1);color:var(--color-primary);font:600 var(--font-size-md)/var(--line-height-md) var(--font-family)}\n.ilink:hover{color:var(--color-primary-hover);text-decoration:underline;text-underline-offset:2px}"),
    ("table", "List table with developer row", "The Public page list: group heading rows, one row per page, a twisty that opens the route, source files and spec link.",
     '<table class="sp-table"><thead><tr><th></th><th>Page</th><th>File</th></tr></thead><tbody><tr><td>&#9656;</td><td><b>Coworker</b></td><td><code>VBE-101-Coworker.html</code></td></tr></tbody></table>',
     [("Head cell", "11px / 600 uppercase, letter-spacing .04em, 1px var(--color-surface-alt) rule"), ("Body cell", "14px / 21px, padding 8px, 51px rows"),
      ("Group row", "bold 14px heading with a 20px chevron that folds the group's rows; the count sits at the right"),
      ("Developer box", "var(--color-page-bg), 1px var(--color-border), radius var(--radius-sm), padding 16px")],
     "table{border-collapse:collapse;width:100%}\nth{font:600 var(--font-size-thead)/var(--line-height-thead) var(--font-family);text-transform:uppercase;letter-spacing:.04em}\ntd{padding:8px;font-size:var(--font-size-table);border-bottom:1px solid var(--color-surface-alt)}"),
]

# ---------------------------------------------------------------- tokens.css parsing
def parse_tokens():
    """tokens.css through tokens_lib: (group, name, value, note, source). Values are resolved (var() aliases replaced by the value they stand for)."""
    raw = T.read()
    res = T.resolved(raw)
    return [(g, n, res[n], note, SOURCES.get(tag, "")) for g, n, _, note, tag in raw]

TOKENS = parse_tokens()
TV = {n: v for _, n, v, _, _ in TOKENS}

def colour_groups():
    groups = {}
    for g, n, v, note, _ in TOKENS:
        if g in COLOUR_BLURBS:
            groups.setdefault(g, []).append((re.sub(r"^--(?:color|app)-", "", n).replace("-", " ").capitalize(), n, v, note))
    return [(COLOUR_BLURBS[g][0], COLOUR_BLURBS[g][1], items) for g, items in groups.items()]

COLOUR_GROUPS = colour_groups()

def tokens_md_table():
    out = ["| Token | Value | Use | Source |", "| --- | --- | --- | --- |"]
    for group, n, v, note, src in TOKENS:
        out.append(f"| `{n}` | `{v}` | {note or group} | {src} |")
    return "\n".join(out)

def write_token_json():
    colour = {re.sub(r"^--", "", n): v for _, n, v, _, _ in TOKENS if n.startswith(("--color-", "--app-"))}
    j = {"name": "versance", "version": VERSION, "source": "versance.html (web app) and browser-extension/style-v1 via design-tokens/tokens.css",
         "color": colour,
         "font": {"family": TV["--font-family"], "mono": TV["--font-family-mono"]},
         "layout": {k[2:]: v for k, v in TV.items() if k in ("--sidebar-width", "--rail-width", "--content-max-width", "--page-padding", "--card-padding")},
         "cssVariables": {n: v for _, n, v, _, _ in TOKENS}}
    (ROOT / "design-tokens/tokens.json").write_text(json.dumps(j, indent=2) + "\n")
    return j

def sync_design_tokens_md():
    head = ("<!-- Generated by tools/build_system.py from design-tokens/tokens.css and the data in that script. Do not edit by hand. -->\n\n"
            "# Versance design tokens and component specs\n\nSource of truth for building in the Versance style (web app + extension style-v1). Developer system: " + (SITE or "") + "/admin/system/\n\n")
    (ROOT / "design-tokens/DESIGN-TOKENS.md").write_text(head + md_tokens() + "\n\n" + md_components())

# ---------------------------------------------------------------- helpers
def is_hex(v): return bool(re.fullmatch(r"#[0-9a-fA-F]{6}", v))

def lum(hexv):
    n = int(hexv[1:], 16)
    c = [((n >> s) & 255) / 255 for s in (16, 8, 0)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def contrast(hexv, other="#FFFFFF"):
    a, b = sorted((lum(hexv), lum(other)), reverse=True)
    return (a + 0.05) / (b + 0.05)

def rgb(hexv):
    n = int(hexv[1:], 16)
    return f"R{(n >> 16) & 255} G{(n >> 8) & 255} B{n & 255}"

def code(text, label="Copy", scroll=False):
    return f'<pre class="code{" code--scroll" if scroll else ""}">{E(text)}</pre><button class="copy" type="button">{label}</button>'

def row(label, sub, body, id_=None):
    s = f"<small>{sub}</small>" if sub else ""
    i = f' id="{id_}"' if id_ else ""
    return f'<div class="row"{i}><div class="row__label"><b>{label}</b>{s}</div><div class="row__body">{body}</div></div>'

def rules(items):
    return '<ul class="rules">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def mono(c):
    return c if "<code>" in c else re.sub(r"(var\(--[a-z0-9-]+\))", r"<code>\1</code>", c)

def spec_table(rows, head=("Property", "Value")):
    return ('<table class="spec"><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{mono(c)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")

def tokens_html_table():
    return spec_table([(f"<code>{E(n)}</code>", f"<code>{E(v)}</code>", E(note or group), E(src)) for group, n, v, note, src in TOKENS], ("Token", "Value", "Use", "Source"))

def href(slug):
    return f"/admin/system/{slug}/" if slug else "/admin/system/"

def page(slug, title_html, intro, body, meta=""):
    n = [s for s, _ in SECTIONS].index(slug) + 1
    label = [l for s, l in SECTIONS if s == slug][0]
    nav = "".join(f'<a href="{href(s)}"{" aria-current=page" if s == slug else ""}>{l}</a>' for s, l in SECTIONS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Versance Admin | System | {E(label)}</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/design-tokens/fonts.css">
<link rel="stylesheet" href="/design-tokens/tokens.css">
<link rel="stylesheet" href="/admin/system/system.css">
<script>if(self!==top)document.documentElement.classList.add("framed");else{{var bare=/[?&]bare(&|$)/.test(location.search);try{{if(bare)sessionStorage.setItem("sysbare","1");else bare=sessionStorage.getItem("sysbare")}}catch(e){{}}if(!bare)location.replace("/admin/system#"+location.pathname.replace(/^\\/admin\\/system/,"")+location.hash)}}</script>
</head>
<body class="dsys">
<header class="bar">
  <div class="bar__title"><a href="/admin/system/"><img src="/versance-logo.svg" alt="Versance"></a><div>Versance <span>Developer System</span></div></div>
  <button class="bar__menu" type="button" aria-label="Open the menu" aria-expanded="false" aria-controls="bar-nav"><svg class="i-menu" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg></button>
  <div class="bar__scrim" aria-hidden="true"></div>
  <nav id="bar-nav" aria-label="Sections"><button class="bar__close" type="button" aria-label="Close the menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></svg></button>{nav}</nav>
</header>
<section class="pg">
  <div class="pg__head"><span>Section {n:02d} &mdash; {E(label)}</span><span></span><span class="pg__meta">{meta}</span></div>
  <div class="pg__grid">
    <div class="pg__side"><h2>{title_html}</h2><p class="lede">{intro}</p></div>
    <div class="pg__main">{body}</div>
  </div>
</section>
<script src="/admin/system/system.js"></script>
</body>
</html>
"""

def write(path, text):
    p = SYS / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)

# ---------------------------------------------------------------- pages
def p_overview():
    body = row("What this is", "", rules([
        "One reference for building Versance admin tools and prototypes in the Versance look",
        "One set of tokens, based on the web app (<code>versance.html</code>) and the browser-extension baseline <code>browser-extension/style-v1/</code>. Every token says which one it comes from; values neither defines are tagged <b>Ours</b>",
        "Use the tokens, not hard-coded values. The same data produces these pages, the CSS and JSON tokens, and the AI files",
    ]))
    body += row("One set", "How the tokens are kept", spec_table([
        ("Source of truth", "<code>design-tokens/tokens.css</code>: every value is written once, under one name; the web app's and the extension's own names for it are listed in <code>design-tokens/map.json</code>"),
        ("Based on", "the web app (<code>versance.html</code>) and the extension baseline (<code>browser-extension/style-v1/</code>); each token says which one it comes from, and values neither defines are tagged <b>Ours</b>"),
        ("Generated copies", "style-v1's <code>tokens.css</code> and viewer page, the <code>:root</code> blocks of <code>versance.html</code> and <code>edgar/versance.html</code> (through <code>design-tokens/map.json</code>), <code>tokens.json</code>, <code>DESIGN-TOKENS.md</code>, the AI files and the skill's <code>tokens.css</code>"),
        ("Change a value", "edit <code>tokens.css</code>, run <code>python3 tools/build_system.py</code>, then <code>python3 tools/audit.py</code>"),
        ("Not part of the set", "styles v2 to v13 and the Medicus page are design examples: they stay viewable in the Public list and their CSS is only for their own pages"),
    ], ("Topic", "Detail")))
    body += row("Principles", "", rules([
        "<b>One accent.</b> Indigo #324EFE for links, actions, focus and selected states; pale tints for hover and disabled",
        "<b>Light surfaces, hairlines.</b> White cards, #F9F9F9 panes, #D9DDE5 borders",
        "<b>Figtree everywhere</b>, Roboto Mono only for code and the web app composer",
        "<b>Pills and soft corners.</b> 8px buttons, 10px inputs, 12px cards, fully rounded pills and tabs",
    ]))
    body += row("Quick start", "Add the tokens", code('<link rel="stylesheet" href="/design-tokens/fonts.css">\n<link rel="stylesheet" href="/design-tokens/tokens.css">\n\n<style>\n  body{margin:0;font:var(--font-size-md)/var(--line-height-md) var(--font-family);color:var(--color-text);-webkit-font-smoothing:antialiased}\n  a{color:var(--color-primary)}\n</style>', "Copy snippet"))
    body += row("Reference", "", '<p>The <a href="/admin/public">Public</a> list shows the web app and every extension style (v1 to v13) with the files, tokens and skill a developer needs.</p>'
                '<div class="note">Figtree loads from Google Fonts, as in the source designs. To self-host it, download the font files and replace the import in <code>fonts.css</code>.</div>')
    return page("", "Developer <b>system</b>", "How the Versance interface is built: type, colour, foundations and components, in a form a developer or an AI assistant can use.", body, f"Version {VERSION}")

def p_type():
    body = row("Typeface", "Figtree", '<p><b>Figtree</b> is the typeface of the web app and the extension (weights 400 to 800). <b>Roboto Mono</b> is used for code and the web app composer. Letter spacing is normal; the web app hero title uses -0.5px.</p>'
               '<div class="note"><b>Weights.</b> 400 body, 600 pane titles, selected pills and table heads, 700 buttons, tags and titles. Set <code>-webkit-font-smoothing: antialiased</code> on body.</div>'
               + code(f"--font-family: {TV['--font-family']};\n--font-family-mono: {TV['--font-family-mono']};", "Copy"))
    rows_ = ""
    for n, w, use in TYPE_SCALE:
        sz, lh = TV[f"--font-size-{n}"], TV[f"--line-height-{n}"]
        rows_ += (f'<div class="ts"><div><b>--font-size-{n}</b><small>{sz} / {lh}, weight {w}<br>{use}</small></div>'
                  f'<div class="sample" style="font-size:{sz};line-height:{lh};font-weight:{w}">Ask Edgar about any filing</div></div>')
    body += row("Scale", "Size / line height", rows_)
    body += row("Mono", "Code and composer", '<div class="ts"><div><b>--font-family-mono</b><small>Roboto Mono 400 / 500</small></div><div class="sample" style="font-family:var(--font-family-mono);font-size:15px;line-height:23px">Summarise the latest 10-K risks.</div></div>')
    return page("typography", "Type", "One typeface, a short scale, and a hard rule: sizes come from the tokens.", body)

def p_colour():
    body = ""
    for title, blurb, items in COLOUR_GROUPS:
        tiles = ""
        for name, tk, v, use in items:
            if is_hex(v):
                fg = "#FFFFFF" if contrast(v) >= contrast(v, "#000000") else "#000000"
                spec = f'<button class="hex" data-copy-text="{v}">{v}</button>{rgb(v)}<br>{contrast(v):.1f}:1 ON WHITE<span class="tk">{tk}</span>'
            else:
                fg = "#000000"
                spec = f'<button class="hex" data-copy-text="{v}">{v}</button><span class="tk">{tk}</span>'
            tiles += f'<div class="tile" style="background:{v};color:{fg}"><div><b>{name}</b><br><span class="tk">{E(use)}</span></div><div>{spec}</div></div>'
        body += row(title, blurb, f'<div class="swatches">{tiles}</div>')
    body += row("Rules", "", rules([
        "Always use the token (<code>var(--color-primary)</code>), never the hex",
        "Indigo (<code>--color-primary</code>) is the only accent for actions, links and focus; the web app's green is for success and toggles",
        "Severity colours (<code>--color-danger</code>, <code>--color-warning</code>) mean risk, not decoration",
        f"Body text is black on white (contrast {contrast('#000000'):.1f}:1). Muted and faint text are for labels and placeholders only",
    ]))
    return page("colour", "Colour", "A small palette with fixed jobs: indigo for action, near-black frames, green and severity colours for state.", body)

LOGOS = [("versance-lock-up", "Lock-up", "Icon and VERSANCE.AI wordmark. The primary logo: the admin sidebar, page headers and the home page.", "305 x 84"),
         ("versance-icon", "Icon", "The waveform circle alone. Use where the wordmark will not fit: app icons, avatars, a collapsed rail.", "84 x 84"),
         ("versance-tte-lock-up", "TTE lock-up", "The TTE lock-up (icon with its own wordmark), supplied as a separate logo.", "269 x 84")]

def build_logos():
    out = SYS / "logos"
    out.mkdir(parents=True, exist_ok=True)
    for stem, *_ in LOGOS:
        svg = (ROOT / "logos" / f"{stem}.svg").read_text()
        (out / f"{stem}.svg").write_text(svg)
        (out / f"{stem}-white.svg").write_text(re.sub(r"<svg ", '<svg fill="#ffffff" ', svg, count=1))
    (ROOT / "versance-logo.svg").write_text((ROOT / "logos/versance-lock-up.svg").read_text())

def p_logos():
    body = row("Logos", "Black and white", rules([
        "Use the <b>lock-up</b> by default; use the <b>icon</b> only where the wordmark will not fit",
        "Black on light surfaces, white on dark (<code>var(--color-ink)</code>) or photographic backgrounds. No other colours, no gradients, no effects",
        "Never stretch, rotate, outline or re-draw a logo. Scale it proportionally, by width, and let the height follow",
        "Clear space: keep at least the height of the icon's inner bars (about a quarter of the logo height) free on every side",
        "Minimum size: lock-up 120px wide, icon 24px wide",
        "Admin sidebar: lock-up, white, 160px wide (32px high on a phone), padding 24px",
    ]))
    for stem, name, about, size in LOGOS:
        w = "width:" + ("96px" if stem == "versance-icon" else "240px")
        body += row(name, f"viewBox {size}",
                    f"<p>{about}</p>"
                    f'<div class="box"><img src="/admin/system/logos/{stem}.svg" alt="{name}, black" style="{w};height:auto"></div>'
                    f'<div class="box dark"><img src="/admin/system/logos/{stem}-white.svg" alt="{name}, white" style="{w};height:auto"></div>'
                    f'<p class="dl" style="margin-top:16px"><a href="/admin/system/logos/{stem}.svg" download>Download {stem}.svg (black)</a> &nbsp; '
                    f'<a href="/admin/system/logos/{stem}-white.svg" download>Download {stem}-white.svg (white)</a></p>', stem)
    return page("logos", "<b>Logos</b>", "The Versance logos: the lock-up, the icon and the TTE lock-up, in black and white.", body)

def p_foundations():
    sp = "".join(f'<tr><td><code>{n}</code></td><td>{v}</td><td><div class="bars"><div style="width:{v}"></div></div></td></tr>' for _, n, v, _, _ in TOKENS if n.startswith("--space-"))
    body = row("Spacing", "Scale", f'<table class="spec"><thead><tr><th>Token</th><th>Value</th><th></th></tr></thead><tbody>{sp}</tbody></table>'
               f'<p class="cap">Button padding {TV["--pad-btn"]}, pill padding {TV["--pad-pill"]}.</p>')
    body += row("Radius", "", spec_table([(f"<code>--radius-{n}</code>", TV[f"--radius-{n}"], u) for n, u in FOUNDATIONS["radius"]], ("Token", "Value", "Used for")))
    sh = "".join(f'<div style="width:150px;height:80px;background:#fff;border-radius:12px;box-shadow:{TV[n]};padding:12px;font-size:12px"><b>{n}</b><br>{u}</div>' for n, u in FOUNDATIONS["shadow"])
    body += row("Elevation", "Soft shadows", f'<div class="box grey" style="gap:32px">{sh}</div>')
    body += row("Motion", "", rules([f"Colour fades take <code>--duration-hover</code> ({TV['--duration-hover']}); button and nav hovers <code>--duration-fast</code> ({TV['--duration-fast']})",
                                    "The toggle knob moves in 180ms; the System menu drawer slides in over 250ms",
                                    f"Keyboard focus: <code>--focus-ring</code> ({TV['--focus-ring']}) with a 2px offset"]))
    body += row("Layout", "", spec_table([("Sidebar", f"{TV['--sidebar-width']} wide (the web app sidebar), near-black in the admin"), ("Icon rail", f"{TV['--rail-width']} wide (the extension)"),
                                         ("Content", f"max width {TV['--content-max-width']}, padding {TV['--page-padding']}")], ("Part", "Spec")))
    return page("foundations", "<b>Foundations</b>", "Spacing, radius, elevation, motion and layout: the values every component is built from.", body)

def p_components():
    body = ""
    for id_, title, blurb, spec, specs, snip in COMPONENTS:
        inner = f'<p>{blurb}</p><div class="box">{spec}</div>' + spec_table(specs) + f'<details class="acc"><summary>CSS</summary>{code(snip)}</details>'
        body += row(title, id_, inner, id_)
    return page("components", "<b>Components</b>", "The components of the Versance admin as live specimens with their spec and starter CSS. The specimens are built from the tokens.", body)

def p_tokens():
    body = row("Naming", "", rules(["Colours are <code>--color-&lt;name&gt;</code>", "Type is <code>--font-size-&lt;name&gt;</code>, <code>--line-height-&lt;name&gt;</code>, <code>--font-weight-&lt;name&gt;</code>",
                                   "Space, radius and shadow are <code>--space-&lt;n&gt;</code>, <code>--radius-&lt;name&gt;</code>, <code>--shadow-&lt;n&gt;</code>", "Use the token, never the raw value"]))
    body += row("Where the values are used", "Generated from tokens.css", spec_table([
        ("browser-extension/style-v1/design-system/tokens.css", "extension names (--accent, --ink, --r-btn …) mapped by design-tokens/map.json; the readable view-tokens.html is regenerated with it"),
        ("versance.html, edgar/versance.html", "the four :root blocks (light, dark media query, data-theme dark, data-theme light) in the web app's own names"),
        ("tokens.json, DESIGN-TOKENS.md, system/ai/*.md, skills/versance-ui/tokens.css", "generated by build_system.py"),
        ("Not generated", "styles v2 to v13 and medicus-01.html (design examples with their own CSS)")], ("File", "How")))
    body += row("Files", "Download", '<p class="dl"><a href="/design-tokens/tokens.css" download>tokens.css</a><a href="/design-tokens/tokens.json" download>tokens.json</a><a href="/design-tokens/fonts.css" download>fonts.css</a><a href="/design-tokens/DESIGN-TOKENS.md" download>DESIGN-TOKENS.md</a></p>')
    body += row("Reference", "Every token, generated from tokens.css", tokens_html_table())
    body += row("CSS", "All tokens as custom properties", code(CSS_TOKENS, "Copy CSS", True))
    body += row("JSON", "The same tokens as data", code((ROOT / "design-tokens/tokens.json").read_text(), "Copy JSON", True))
    return page("tokens", "Design <b>tokens</b>", "The system's values as named custom properties and as JSON, ready to use in code or a design tool.", body)

# ---------------------------------------------------------------- AI files
def md_tokens():
    out = ["# Design tokens", "", "Named values for the Versance interface, based on the web app (versance.html) and the extension style-v1. Use the token, never the raw value.", "",
           "## Colour", "", "| Colour | Token | Hex / value | RGB | Use |", "| --- | --- | --- | --- | --- |"]
    for _, _, items in COLOUR_GROUPS:
        for name, tk, v, use in items:
            out.append(f"| {name} | `{tk}` | `{v}` | {rgb(v) if is_hex(v) else ''} | {use} |")
    out += ["", "## Typography", "", f"Family `{TV['--font-family']}`; mono `{TV['--font-family-mono']}`.", "", "| Token | Size / line height | Weight | Use |", "| --- | --- | --- | --- |"]
    out += [f"| `--font-size-{n}` | {TV['--font-size-' + n]} / {TV['--line-height-' + n]} | {w} | {u} |" for n, w, u in TYPE_SCALE]
    out += ["", "## Shape and elevation", "", "| Token | Value | Use |", "| --- | --- | --- |"]
    out += [f"| `--radius-{n}` | {TV['--radius-' + n]} | {u} |" for n, u in FOUNDATIONS["radius"]]
    out += [f"| `{n}` | {TV[n]} | {u} |" for n, u in FOUNDATIONS["shadow"]]
    out += ["", "## All tokens", "", "Generated from `tokens.css`, so it is always complete.", "", tokens_md_table(), "", "## CSS", "", "```css", CSS_TOKENS.strip(), "```", ""]
    return "\n".join(out)

def md_components():
    out = ["# Components", "", "Specs for the Versance admin components. Each lists the values; build with the tokens in `design-tokens.md`.", ""]
    for id_, title, blurb, _, specs, snip in COMPONENTS:
        out += [f"## {title}", "", blurb, "", "| Property | Value |", "| --- | --- |"] + [f"| {a} | {b} |" for a, b in specs] + ["", "```css", snip, "```", ""]
    return "\n".join(out)

def md_agents():
    return f"""# Versance developer system: instructions for AI agents

Applies to any UI that should look like Versance: admin tools, static prototypes and mock-ups in the Versance style (web app + browser-extension style-v1).

Read these in order:

1. `design-tokens.md`: every colour, type, radius and shadow value, and the CSS custom properties
2. `components.md`: specs and starter CSS for each component

## Always

- **Use the tokens** (`var(--color-*)`, `--font-size-*`, `--radius-*`, `--shadow*`) instead of hard-coded values.
- **Font:** Figtree (link `fonts.css`), Roboto Mono only for code and the web app composer. Set `-webkit-font-smoothing: antialiased` on body.
- **One accent:** indigo `var(--color-primary)` for links, actions, focus and selected states; pale tints (`--color-primary-tint-*`) for hover, selected and disabled. Green (`--color-success`) is for success and toggles in the web app; `--color-danger` and `--color-warning` mean severity.
- **Logo:** use the Versance lock-up (`logos/versance-lock-up.svg`, white variant on dark); the icon alone only where the wordmark will not fit. Never recolour, stretch or re-draw it.
- **Shapes:** buttons 8px, inputs 10px, cards 12px, pills fully rounded. Body text 14px; page titles 28px / 700.
- **Surfaces:** white cards with a 1px `var(--color-border)` border, `var(--color-page-bg)` panes, `var(--color-surface-alt)` chips and hovers. The dark `var(--color-ink)` is used for the sidebar and the one dark pill.
- **Focus:** `var(--focus-ring)` with a 2px offset on buttons and links; text fields only change border colour.
- **Use made-up data** in prototypes. Never put real company, filing or user data in a repo or public page.

## Never

- Invent new colours, radii or font sizes. Pick the nearest token.
- Use a second accent hue (the extension has none), or green for actions.
- Use severity colours for decoration.

## Quick reference

| Need | Use |
| --- | --- |
| Body text | `var(--color-text)` on `var(--color-surface)` |
| Muted label | `var(--color-text-muted)` |
| Link or primary action | `var(--color-primary)`, hover `var(--color-primary-hover)` |
| Hairline | `1px solid var(--color-border)` (rows: `--color-surface-alt`) |
| Sidebar | `var(--color-ink)` with `var(--color-surface)` |
| Success | `--color-success*` (web app green) |
| High / medium severity | `--color-danger` / `--color-warning` |

## When unsure

Do not guess. Flag the question and take the safest option. Tokens tagged **Ours** in `tokens.css` are admin-tool choices, not values from the web app or the extension.

Source of truth: the Developer System at `{SITE}/admin/system/`.
"""

SKILL_SLUG = "versance-ui"
SKILL_FILES = [
    ("SKILL.md", "The workflow", "What the agent does, in order: read, plan, build, check, hand over. Start here."),
    ("rules.md", "The rules", "What to always and never do, with a quick reference of which token to use."),
    ("design-tokens.md", "Colour, type and shape values", "Every token with hex, RGB and use."),
    ("components.md", "Component specs", "Specs and starter CSS for each component."),
    ("tokens.css", "The tokens as CSS", "Custom properties to link into any page."),
    ("fonts.css", "The web fonts", "The Figtree and Roboto Mono import (Google Fonts)."),
    ("starter.html", "Starter page", "Header, page title, buttons, pills, table and footer built from the tokens."),
    ("logos/", "The logos", "The lock-up, icon and TTE lock-up as SVG, black and white."),
    ("check.py", "The checker", "Flags colours, font sizes, radii and fonts that are not in the system."),
]
TEMPLATES = Path(__file__).resolve().parent / "skill_template"

def skill_md():
    return f"""---
name: {SKILL_SLUG}
description: Build or restyle pages, components and prototypes in the Versance look (the Versance web app and the browser-extension style-v1). Use for any new Versance admin screen or mock-up, or when asked to match Versance styling. Provides the design tokens, component specs, a starter page and a checker.
---

# Versance UI

Builds pages and prototypes in the Versance look: Figtree, one indigo accent, white surfaces with hairlines, 8px buttons, pill chips and tabs.

Tokens come from the web app (`versance.html`) and `browser-extension/style-v1/`. Source of truth: `{SITE}/admin/system/`.

## Workflow

1. **Read** `rules.md` first, then `design-tokens.md`. Read `components.md` for any component you will use.
2. **Plan** the page in terms of existing components (buttons, pills and tabs, toggle, fields, rail, cards, tags, citation, table). If something is missing, pick the nearest token; do not invent values.
3. **Start from** `starter.html` or link `tokens.css` and `fonts.css` and build from `components.md`.
4. **Use tokens only.** Write `var(--color-primary)`, not `#324efe`.
5. **Use made-up data.**
6. **Check** your work: `python3 check.py <your files>`. Fix every finding, or say why one is intentional.
7. **Hand over** the files and say which components you used and anything you were unsure of.

## Notes

- Figtree loads from Google Fonts (`fonts.css`); self-host it if the page must work offline.
- The web app's green accent and the extension's indigo are both tokens; use indigo for actions.
"""

def skill_rules():
    return (md_agents().replace("# Versance developer system: instructions for AI agents", "# Rules")
            .replace("Read these in order:\n\n1. `design-tokens.md`: every colour, type, radius and shadow value, and the CSS custom properties\n2. `components.md`: specs and starter CSS for each component\n",
                     "See also `design-tokens.md` and `components.md` in this folder.\n"))

def check_py():
    colours = sorted({v.lower() for _, n, v, _, _ in TOKENS if n.startswith(("--color-", "--app-")) and is_hex(v)} | {"#fff", "#ffffff", "#000", "#000000", "#e6e6e6"})
    alphas = sorted({v.replace(" ", "").lower() for _, n, v, _, _ in TOKENS if n.startswith("--color-") and v.startswith("rgba")})
    sizes = sorted({float(v[:-2]) for _, n, v, _, _ in TOKENS if n.startswith("--font-size-") and v.endswith("px")} | {9.0, 10.0, 12.5, 13.0, 15.0, 16.0})
    radii = sorted({float(v[:-2]) for _, n, v, _, _ in TOKENS if n.startswith("--radius-") and v.endswith("px")} | {0.0, 16.0, 20.0, 999.0})
    t = (TEMPLATES / "check.py").read_text()
    for k, v in (("__COLOURS__", colours), ("__ALPHAS__", alphas), ("__SIZES__", sizes), ("__RADII__", radii)):
        t = t.replace(k, repr(v))
    return t

def build_skill():
    d = SYS / "skills" / SKILL_SLUG
    d.mkdir(parents=True, exist_ok=True)
    files = {"SKILL.md": skill_md(), "rules.md": skill_rules(), "design-tokens.md": md_tokens(), "components.md": md_components(),
             "tokens.css": CSS_TOKENS, "fonts.css": (ROOT / "design-tokens/fonts.css").read_text(),
             "starter.html": (TEMPLATES / "starter.html").read_text().replace("__SITE__", SITE), "check.py": check_py()}
    for name, text in files.items():
        (d / name).write_text(text)
    (d / "logos").mkdir(exist_ok=True)
    logos = [f"logos/{p.name}" for p in sorted((SYS / "logos").glob("*.svg"))]
    for n in logos:
        (d / n).write_text((SYS / n).read_text())
    files = {**files, **{n: None for n in logos}}
    with zipfile.ZipFile(SYS / "skills" / f"{SKILL_SLUG}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for name in files:
            z.write(d / name, f"{SKILL_SLUG}/{name}")

def p_skill_row():
    base = f"{SITE}/admin/system/skills/{SKILL_SLUG}.zip"
    install = f"curl -L <your-host>{base} -o {SKILL_SLUG}.zip && unzip -o {SKILL_SLUG}.zip -d ~/.claude/skills"
    h3 = '<h3 style="margin:28px 0 8px;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--color-primary)">'
    files = spec_table([(f if f.endswith("/") else f'<a href="/admin/system/skills/{SKILL_SLUG}/{f}" download>{f}</a>', sub, about) for f, sub, about in SKILL_FILES], ("File", "What it is", "About"))
    inner = ("<p>A skill for AI coding agents. Give it a screen to build and it uses the Versance tokens and component specs, starts from a working page, and checks the result for values that are not in the system.</p>"
             + h3 + "Install</h3><p>Download the zip below and unzip it into <code>~/.claude/skills</code>, or from a terminal (replace <code>&lt;your-host&gt;</code> with where this site is deployed):</p>"
             + code(install, "Copy command") + h3 + "Use</h3>" + code("/versance-ui build a settings page with a filter card and a table of filings, in the Versance style", "Copy example")
             + f'<p class="dl" style="margin-top:20px"><a href="/admin/system/skills/{SKILL_SLUG}.zip" download>Download the skill (.zip)</a></p>' + h3 + "What is in it</h3>" + files)
    return row("Skill", SKILL_SLUG, inner, SKILL_SLUG)

AI_FILES = [
    ("AGENTS.md", "Drop-in instructions", "Short rules for an AI agent: what to always do, what never to do, and where to look. Start here.", md_agents),
    ("design-tokens.md", "Colour, type and shape values", "Every token with hex, RGB and use, plus the ready-to-paste CSS block.", md_tokens),
    ("components.md", "Component specs", "The spec and starter CSS for each component.", md_components),
]

def p_ai():
    files = "".join(f'<li><b>{f}</b>: {sub}. {about} (<a href="/admin/system/ai/{f}" download>download</a>)</li>' for f, sub, about, _ in AI_FILES)
    root_line = "Follow the Versance developer system in docs/versance/AGENTS.md. Read the other files in that folder when it tells you to."
    chat = "I have attached the Versance developer system files (AGENTS.md, design-tokens.md and components.md). Read AGENTS.md first and follow it for everything you make for me. My request: "
    body = row("How to use", "Pick the one that matches how you work",
               f'<p>Three Markdown files tell an AI how to build in the Versance style. Give them to it once and everything it makes follows the rules. Keep all three together.</p><ul class="rules">{files}</ul>'
               f'<p class="dl" style="margin-top:16px"><a href="/admin/system/ai/Versance-AI-Files.zip" download>Download all three (.zip)</a></p>')
    body += row("A. In a code project", "Claude Code, Cursor, Codex or any coding agent",
                "<p><b>1.</b> Put the three files together in a folder, for example <code>docs/versance/</code>.</p><p><b>2.</b> Add the tokens and fonts to the project.</p>"
                "<p><b>3.</b> In the project root, add <code>AGENTS.md</code> (and <code>CLAUDE.md</code> for Claude Code) with this line:</p>" + code(root_line, "Copy line"))
    body += row("B. In a chat", "claude.ai, ChatGPT or any chat window", "<p>Attach the three files, then ask.</p>" + code(chat, "Copy prompt"))
    body += p_skill_row()
    for f, sub, about, fn in AI_FILES:
        body += row(f, sub, f'<p class="dl"><a href="/admin/system/ai/{f}" download>Download {f}</a></p>' + code(fn(), "Copy file", True), f.split(".")[0])
    return page("ai", "Files for <b>developers and AI</b>", "Markdown files that help a developer or an AI assistant apply the Versance system correctly.", body)

JS = """(function(){var bar=document.querySelector('.bar');if(!bar)return;var burger=bar.querySelector('.bar__menu'),shut=bar.querySelector('.bar__close'),scrim=bar.querySelector('.bar__scrim'),wide=matchMedia('(min-width:901px)');
function set(o,focus){bar.classList.toggle('open',o);burger.setAttribute('aria-expanded',String(o));document.body.style.overflow=o?'hidden':'';if(focus)(o?shut:burger).focus();}
burger.addEventListener('click',function(){set(true,true);});shut.addEventListener('click',function(){set(false,true);});scrim.addEventListener('click',function(){set(false,true);});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&bar.classList.contains('open'))set(false,true);});
wide.addEventListener('change',function(){if(wide.matches&&bar.classList.contains('open'))set(false,false);});})();
document.addEventListener('click',function(e){
  var b=e.target.closest('.copy,[data-copy-text]');if(!b)return;
  var t=b.dataset.copyText||b.previousElementSibling.textContent;
  var old=b.textContent;
  (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).catch(function(){
    var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(x){}a.remove();});
  if(b.classList.contains('copy')){b.textContent='Copied';setTimeout(function(){b.textContent=old},1200);}
});
"""

def main():
    subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "build_tokens.py")], check=True)   # style-v1 tokens.css, versance.html, edgar/versance.html
    build_logos()
    write_token_json()
    sync_design_tokens_md()
    write("system.js", JS)
    pages = {"": p_overview, "typography": p_type, "colour": p_colour, "logos": p_logos, "foundations": p_foundations, "components": p_components, "tokens": p_tokens, "ai": p_ai}
    for slug, fn in pages.items():
        write(f"{slug}/index.html" if slug else "index.html", fn())
    for f, _, _, fn in AI_FILES:
        write(f"ai/{f}", fn())
    build_skill()
    with zipfile.ZipFile(SYS / "ai/Versance-AI-Files.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f, *_ in AI_FILES:
            z.write(SYS / "ai" / f, f)
    print("built", len(pages), "pages and", len(AI_FILES), "AI files")

if __name__ == "__main__":
    main()
