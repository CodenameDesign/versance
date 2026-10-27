# Versance admin: working rules

## Keep the design system in step with the UI (always)
When you change how the admin (or a new page) looks or behaves, update the system in the same change:
1. Add or change values in `design-tokens/tokens.css` (one token per line, trailing `[app]` / `[ext]` / `[both]` / `[ours]` comment). `tokens.json` and `DESIGN-TOKENS.md` are generated.
2. Edit the data in `tools/build_system.py` (`COMPONENTS`, type scale, foundations, the rules in `md_agents`), add specimen CSS to `system/system.css`, then run `python3 tools/build_system.py`.
3. Run `python3 tools/build_admin.py` if the Public list changed, then `python3 tools/audit.py` and fix every FAIL.
4. Commit page and system changes together. Push and deploy only when asked.

## One token set
`design-tokens/tokens.css` is the only place token values are written (each value once; other names are `var()` aliases). It is based on `versance.html` and `browser-extension/style-v1/`; mark anything neither defines as `[ours]`. The `:root` blocks of `versance.html` / `edgar/versance.html` and style-v1's `tokens.css` are generated from it (`tools/build_tokens.py`, names in `design-tokens/map.json`): never edit them by hand. A new source variable needs an entry in `map.json`. Styles v2 to v13 and `medicus-01.html` are design examples with their own CSS: do not touch them or fold them into the set.

## Data
Made-up company, filing and user data only. Never commit real data.
