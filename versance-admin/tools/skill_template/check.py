#!/usr/bin/env python3
"""Checks HTML / CSS files against the Versance design system.

    python3 check.py page.html styles.css

Flags colours, font sizes, border radii and font families that are not in the system. Prefer var(--token).
Exit code 1 if anything is flagged. Skips tokens.css.
"""
import re, sys
from pathlib import Path

COLOURS = __COLOURS__
ALPHAS = __ALPHAS__
SIZES = __SIZES__
RADII = __RADII__

HEX = re.compile(r"#[0-9a-fA-F]{3,8}\b")
RGB = re.compile(r"rgba?\([^)]*\)")
FONT_SIZE = re.compile(r"font-size\s*:\s*([0-9.]+)px")
RADIUS = re.compile(r"border-radius\s*:\s*([^;}]+)")
FAMILY = re.compile(r"font-family\s*:\s*([^;}]+)")


def norm(h):
    h = h.lower()
    return "#" + "".join(c * 2 for c in h[1:]) if len(h) == 4 else h


def check(path):
    out = []
    for n, line in enumerate(Path(path).read_text(errors="ignore").splitlines(), 1):
        for m in HEX.finditer(line):
            if len(m.group()) in (4, 7) and norm(m.group()) not in COLOURS:
                out.append((n, f"colour {m.group()} is not in the palette"))
        for m in RGB.finditer(line):
            v = m.group().replace(" ", "").lower()
            if v in ALPHAS or v.startswith(("rgba(0,0,0,", "rgba(255,255,255,")):
                continue
            nums = re.findall(r"[0-9.]+", v)
            if len(nums) == 3 and "#%02x%02x%02x" % tuple(int(float(x)) for x in nums) in COLOURS:
                continue
            out.append((n, f"colour {m.group()} is not in the palette"))
        for m in FONT_SIZE.finditer(line):
            if float(m.group(1)) not in SIZES:
                out.append((n, f"font-size {m.group(1)}px is not in the type scale"))
        for m in RADIUS.finditer(line):
            for v in re.findall(r"([0-9.]+)px", m.group(1)):
                if float(v) not in RADII:
                    out.append((n, f"border-radius {v}px is not a token"))
        for m in FAMILY.finditer(line):
            f = m.group(1)
            if "figtree" not in f.lower() and "var(" not in f and "monospace" not in f and "inherit" not in f and "roboto mono" not in f.lower():
                out.append((n, f"font-family {f.strip()} is not Figtree or Roboto Mono"))
    return out


def main(paths):
    total = 0
    for p in paths:
        if Path(p).name == "tokens.css":
            continue
        for n, msg in check(p):
            print(f"{p}:{n}: {msg}")
            total += 1
    print("ok: nothing flagged" if not total else f"{total} finding(s)")
    return 1 if total else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
