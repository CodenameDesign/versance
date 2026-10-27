#!/usr/bin/env python3
"""Writes every place that carries Versance token values from the one canonical set (design-tokens/tokens.css), through design-tokens/map.json:

    browser-extension/style-v1/design-system/tokens.css   (+ its readable view-tokens.html)
    versance.html and edgar/versance.html                   (the :root blocks: light, dark media query, data-theme dark, data-theme light)

    python3 tools/build_tokens.py          write the files
    python3 tools/build_tokens.py --check  exit 1 if any file is out of step (used by audit.py)

Only the token values change: names, comments, layout and every other rule in those files are kept. Styles v2 to v13 and medicus-01.html are
separate design examples and are never read or written here.
"""
import importlib.util, json, re, shutil, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tokens_lib as T

ROOT = T.ROOT
REPO = ROOT.parent
MAP = json.loads((ROOT / "design-tokens/map.json").read_text())
VAL = T.resolved()
STYLE = REPO / "browser-extension/style-v1"

def val(canon):
    if canon not in VAL:
        raise SystemExit(f"map.json points at {canon}, which is not in tokens.css")
    return T.upper_hex(VAL[canon])

DECL = re.compile(r"^(\s*)(--[a-z0-9-]+)(\s*:\s*)([^;]+?)(\s*;.*)$")

def swap_values(block, mapping, where):
    """Replace the value of every `--name: value;` line in a block with the canonical value; every name must be mapped."""
    out = []
    for line in block.split("\n"):
        m = DECL.match(line)
        if m:
            name = m.group(2)
            if name not in mapping:
                raise SystemExit(f"{where}: {name} is not in design-tokens/map.json")
            line = f"{m.group(1)}{name}{m.group(3)}{val(mapping[name])}{m.group(5)}"
        out.append(line)
    return "\n".join(out)

def gen_style_tokens():
    src = (STYLE / "design-system/tokens.css").read_text()
    a = src.index(".vc-ext {")
    return src[:a] + swap_values(src[a:], MAP["ext"], "style-v1 tokens.css")

def gen_view_tokens(tokens_css):
    spec = importlib.util.spec_from_file_location("viewers", STYLE / "tools/viewers.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    with tempfile.TemporaryDirectory() as tmp:
        ds = Path(tmp) / "style-v1/design-system"; ds.mkdir(parents=True)
        for f in ("design-system.md", "components.css"):
            shutil.copy(STYLE / "design-system" / f, ds / f)
        (ds / "tokens.css").write_text(tokens_css)
        mod.build(str(Path(tmp) / "style-v1"))
        return (ds / "view-tokens.html").read_text()

BEGIN = "/* BEGIN generated tokens: do not edit here. Source: versance-admin/design-tokens/tokens.css via design-tokens/map.json (python3 versance-admin/tools/build_tokens.py) */"
END = "/* END generated tokens */"

def gen_app(path):
    t = (REPO / path).read_text(encoding="utf-8")
    t = re.sub(r"[ ]*" + re.escape(BEGIN) + r"\n", "", t); t = re.sub(r"\n[ ]*" + re.escape(END), "", t)   # idempotent
    a = t.index("  :root {")
    # the four token blocks run from the first :root to the end of :root[data-theme="light"] { ... }
    lt = t.index(':root[data-theme="light"] {', a)
    b = t.index("}", lt) + 1
    region = t[a:b]
    parts = re.split(r"(?m)^(?=\s*(?::root\s*\{|@media \(prefers-color-scheme: dark\)|:root\[data-theme=))", region)
    out, kind, media = [], "light", False
    for part in parts:
        head = part.lstrip()
        if head.startswith("@media (prefers-color-scheme: dark)"):
            kind, media = "dark", True              # the :root block nested inside the dark media query is dark too
        elif head.startswith(":root {"):
            kind = "dark" if media else "light"
            media = False
        elif head.startswith(':root[data-theme="dark"]'):
            kind = "dark"
        elif head.startswith(':root[data-theme="light"]'):
            kind = "light"
        out.append(swap_values(part, MAP["app"][kind], f"{path} ({kind})") if "--" in part else part)
    new = "".join(out)
    return t[:a] + "  " + BEGIN + "\n" + new + "\n  " + END + t[b:]

def generate():
    style = gen_style_tokens()
    return {
        "browser-extension/style-v1/design-system/tokens.css": style,
        "browser-extension/style-v1/design-system/view-tokens.html": gen_view_tokens(style),
        "versance.html": gen_app("versance.html"),
        "edgar/versance.html": gen_app("edgar/versance.html"),
    }

def main():
    files = generate()
    stale = [p for p, text in files.items() if (REPO / p).read_text(encoding="utf-8") != text]
    if "--check" in sys.argv:
        for p in stale:
            print("out of step with design-tokens/tokens.css:", p)
        return 1 if stale else 0
    for p in stale:
        (REPO / p).write_text(files[p], encoding="utf-8")
    print("tokens written:", ", ".join(stale) if stale else "nothing to change")
    return 0

if __name__ == "__main__":
    sys.exit(main())
