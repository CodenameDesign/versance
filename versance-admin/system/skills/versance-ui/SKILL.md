---
name: versance-ui
description: Build or restyle pages, components and prototypes in the Versance look (the Versance web app and the browser-extension style-v1). Use for any new Versance admin screen or mock-up, or when asked to match Versance styling. Provides the design tokens, component specs, a starter page and a checker.
---

# Versance UI

Builds pages and prototypes in the Versance look: Figtree, one indigo accent, white surfaces with hairlines, 8px buttons, pill chips and tabs.

Tokens come from the web app (`versance.html`) and `browser-extension/style-v1/`. Source of truth: `/admin/system/`.

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
