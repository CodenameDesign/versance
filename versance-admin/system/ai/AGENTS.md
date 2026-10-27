# Versance developer system: instructions for AI agents

Applies to any UI that should look like Versance: admin tools, static prototypes and mock-ups in the Versance style (web app + browser-extension style-v1).

Read these in order:

1. `design-tokens.md`: every colour, type, radius and shadow value, and the CSS custom properties
2. `components.md`: specs and starter CSS for each component

## Always

- **Use the tokens** (`var(--color-*)`, `--font-size-*`, `--radius-*`, `--shadow*`) instead of hard-coded values.
- **Font:** Figtree (link `fonts.css`), Roboto Mono only for code and the web app composer. Set `-webkit-font-smoothing: antialiased` on body.
- **One accent:** indigo `var(--color-primary)` for links, actions, focus and selected states; pale tints (`--color-primary-tint-*`) for hover, selected and disabled. Green (`--color-success`) is for success and toggles in the web app; `--color-danger` and `--color-warning` mean severity.
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

Source of truth: the Developer System at `/admin/system/`.
