# Versance admin

The same admin as CNO, 4Mativ and Equinox (left-nav shell, **Public** page list with a developer-spec page per entry, **System** design system), styled from the Versance web app and the browser-extension designs. Served at versance.futurebits.io.

**One set of tokens**, based on `versance.html` (the web app) and `browser-extension/style-v1/`. `design-tokens/tokens.css` is the only place the values are written (each value once, under one name; the source designs' own names for it are in `design-tokens/map.json`), and each token is tagged `[app]`, `[ext]`, `[both]` or `[ours]` for where it came from. Everything else that carries token values is **generated** from it: style-v1's `tokens.css` and viewer page, and the `:root` blocks of `versance.html` and `edgar/versance.html` (through `design-tokens/map.json`), plus `tokens.json`, `DESIGN-TOKENS.md`, the AI files and the skill. Styles v2 to v13 and `medicus-01.html` are design examples with their own CSS and are not part of the set.

```
design-tokens/   tokens.css (the one set), map.json (source variable names to canonical tokens), fonts.css, tokens.json + DESIGN-TOKENS.md (generated)
admin/           shell: index, system (iframe), public (generated list), spec/ (generated, one page per entry), admin.css, menu.js
system/          generated design-system site, AI files and the versance-ui skill (only system.css is hand-written)
logos/          the logo SVG sources (lock-up, icon, TTE lock-up); the build makes the white copies and /versance-logo.svg
tools/           build_system.py, build_tokens.py, build_admin.py, audit.py, tokens_lib.py, skill_template/
nginx.conf, Dockerfile, index.html (logo on white)
```

## Commands (run from `versance-admin/`)

```
python3 tools/build_system.py   # runs build_tokens.py first, then system/**, AI files, skill, tokens.json, DESIGN-TOKENS.md
python3 tools/build_tokens.py   # only the token copies: style-v1 tokens.css + viewer, versance.html, edgar/versance.html (--check to test)
python3 tools/build_admin.py    # admin/public/index.html, admin/spec/**, and the /public + /admin/source routes in nginx.conf
python3 tools/audit.py          # drift check; fix every FAIL
```

## The Public list is generated from the repo

`build_admin.py` reads `versance.html`, `edgar/versance.html`, `medicus-01.html` and every `browser-extension/style-vN/` (its `design-system/` pages and `screens/VBE-*.html`), so a new style or screen appears after re-running it. Pages are served under `/public/` without changing the URL: `browser-extension/` is mounted in place at `/public/extension/` (so each page's relative CSS keeps working), single files are served by an internal rewrite (their root URLs return 404). `/` and `/public/` show only the logo.

To add a page that is not in those folders, add a `P(...)` entry in `tools/build_admin.py` and a `COPY` line in the Dockerfile.

## Docker

Build from the **repo root**: `docker build -f versance-admin/Dockerfile -t versance-admin .`

## Notes

- Figtree and Roboto Mono load from Google Fonts, as in the source designs. To self-host, download the font files and replace the import in `design-tokens/fonts.css`.
- The System section documents the web app and style v1 (the baseline). Styles v2 to v13 and the Medicus page are design examples: each is listed in Public with its own pages, and their CSS is only for their own pages.
- To change a token value: edit `design-tokens/tokens.css`, run `python3 tools/build_system.py`, then `python3 tools/audit.py`. Do not edit the generated blocks (marked `BEGIN generated tokens`) in `versance.html` or style-v1's `tokens.css`.
- `medicus-01.html` is a saved page from another company's site, kept as a design example.
