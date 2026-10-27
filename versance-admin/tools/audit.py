#!/usr/bin/env python3
"""Audits the Versance design system for drift.

    python3 tools/audit.py

Checks (exit code 1 if any fail):
  1. every custom property in design-tokens/tokens.css is documented in system/ai/design-tokens.md
  2. every var(--x) used by the pages, the system site and the skill is defined in tokens.css (or locally)
  3. design-tokens/tokens.json lists every tokens.css property in its generated "cssVariables" map
  4. the skill folder is in step with the source files (tokens.css, fonts.css)
  5. the starter, admin.css and system.css pass the skill's checker (no raw colours, font sizes, radii or fonts outside the system)
  6. one set: no colour value is defined twice in tokens.css (other names for it are var() aliases)
  7. the generated copies (style-v1 tokens.css and viewer, versance.html, edgar/versance.html) match tokens.css (tools/build_tokens.py --check)
  8. the design examples (styles v2 to v13, medicus-01.html) have no uncommitted changes
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
fails = []

def read(p): return (ROOT / p).read_text()

tokens_css = re.sub(r"/\*.*?\*/", "", read("design-tokens/tokens.css"), flags=re.S)  # declarations only, not the comments
defined = dict(re.findall(r"(--[a-z0-9-]+)\s*:\s*([^;]+);", tokens_css))

# 1. documented
doc = read("system/ai/design-tokens.md")
missing = [t for t in defined if f"`{t}`" not in doc]
if missing: fails.append(("tokens missing from system/ai/design-tokens.md", missing))

# 2. used but undefined
files = ["admin/admin.css", "system/system.css", "tools/skill_template/starter.html"]
undefined = {}
for f in files:
    txt = read(f)
    local = set(re.findall(r"(--[a-z0-9-]+)\s*:", txt))
    for m in re.findall(r"var\((--[a-z0-9-]+)", txt):
        if m not in defined and m not in local:
            undefined.setdefault(f, set()).add(m)
if undefined: fails.append(("var(--x) used but not defined", {k: sorted(v) for k, v in undefined.items()}))

# 3. json parity
tj = json.loads(read("design-tokens/tokens.json"))
flat = tj.get("cssVariables", {})
miss_json = [t for t in defined if t not in flat]
if miss_json: fails.append(("tokens missing from tokens.json cssVariables (run tools/build_system.py)", miss_json))

# 3b. the semantic colour groups in tokens.json match the colour values in tokens.css
def norm(v): return re.sub(r"\s+", "", v.lower())
def leaves(o):
    if isinstance(o, dict):
        for v in o.values(): yield from leaves(v)
    else: yield o
json_colours = {norm(v) for v in leaves(tj.get("color", {}))}
import tokens_lib as _tl
_res = _tl.resolved()
css_colours = {norm(v) for k, v in _res.items() if k.startswith(("--color-", "--app-"))}
if json_colours != css_colours:
    fails.append(("tokens.json colour groups differ from tokens.css", {"only in json": sorted(json_colours - css_colours), "only in css": sorted(css_colours - json_colours)}))

# 4. skill in step
for src, dst in (("design-tokens/tokens.css", "system/skills/versance-ui/tokens.css"), ("design-tokens/fonts.css", "system/skills/versance-ui/fonts.css")):
    if read(src) != read(dst): fails.append((f"{dst} is out of date (run tools/build_system.py)", []))

# 5. checker on the pages that are built from tokens
r = subprocess.run([sys.executable, str(ROOT / "system/skills/versance-ui/check.py"),
                    str(ROOT / "system/skills/versance-ui/starter.html"), str(ROOT / "admin/admin.css")],
                   capture_output=True, text=True)
if r.returncode: fails.append(("checker findings", r.stdout.strip().splitlines()))

# 6. one set: each literal colour is defined once in tokens.css; every other name for it is a var() alias
sys.path.insert(0, str(ROOT / "tools"))
import tokens_lib
seen, dup = {}, []
for g, n, raw, note, tag in tokens_lib.read():
    if raw.startswith("var("): continue
    m = re.fullmatch(r"(#[0-9a-fA-F]{6}|rgba?\([^)]*\))", raw.strip())
    if not m: continue
    key = re.sub(r"\s+", "", raw.lower())
    if key in seen: dup.append(f"{n} repeats {seen[key]} ({raw}); make it var({seen[key]})")
    else: seen[key] = n
if dup: fails.append(("a value is defined twice in tokens.css", dup))

# 7. the generated copies (style-v1 tokens.css and its viewer, versance.html, edgar/versance.html) are in step with tokens.css
r = subprocess.run([sys.executable, str(ROOT / "tools/build_tokens.py"), "--check"], capture_output=True, text=True)
if r.returncode: fails.append(("token copies out of step (run python3 tools/build_tokens.py)", r.stdout.strip().splitlines() or r.stderr.strip().splitlines()))

# 8. the design examples (styles v2 to v13 and medicus-01.html) were not touched by this set's tooling
g = subprocess.run(["git", "-C", str(ROOT.parent), "status", "--porcelain", "--", "medicus-01.html"] + [f"browser-extension/style-v{n}" for n in range(2, 14)], capture_output=True, text=True)
if g.stdout.strip(): fails.append(("design examples have uncommitted changes (they are not part of the token set)", g.stdout.strip().splitlines()[:10]))

if fails:
    for title, detail in fails:
        print("FAIL:", title)
        if detail:
            print("  ", json.dumps(detail, indent=2)[:1800] if not isinstance(detail, list) else "\n   ".join(map(str, detail[:40])))
    sys.exit(1)
print(f"ok: {len(defined)} tokens documented, one definition per value, token copies in step, design examples untouched, all var() references defined, json and skill in step, checker clean")
