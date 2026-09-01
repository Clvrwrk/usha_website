# USHA Website

Website rebuild for the United States Hydrogen Alliance (ushydrogenalliance.org), built on the USHA Brand & Design System v1.0 and the September 2026 review of the CURRENT design canvas.

## What is in this repo

| Folder | What it is |
|---|---|
| `usha-canvas/` | The design source of truth. Every v1.0 page as a desktop (1440) and mobile (390) artboard, the web design system sheet, and the generator that builds them. Published canvas: https://claude.ai/code/artifact/4a77e7e0-ae42-4bab-9c99-d4346f76f521 |
| `usha-site/` | First static HTML build of the site (July 2026, pre-review). Plain HTML/CSS/JS, no framework. To be brought in line with `usha-canvas/`. |
| `design-import/` | Brand & Design System v1.0 document (`USHA Design System.dc.html`) and the SVG masters. |
| `The New USHA/H4 Abstract Prism logo/` | Brand asset library from the Claude Design project: logo set, developer reference (`brand-guidelines.md`), component library, print and video masters. |
| `USHA Logos/` | Logo exports (PNG and SVG) in light and dark variants. |
| `docs/handoffs/` | Session handoff notes. |

## Preview the design pages

```bash
python3 -m http.server 8943 --directory usha-canvas
```

Then open http://localhost:8943/ for an index of every page. Each `.dc.html` renders on its own in a browser (the runtime is `support.js` in the same folder).

## Preview the static site

```bash
python3 -m http.server 8942 --directory usha-site
```

Both servers are also configured in `.claude/launch.json`.

## Regenerating pages

`usha-canvas/build.py` generates every page except Home (`Main.dc.html`, `HomeMobile.dc.html`) and the design system sheet, which are hand-authored:

```bash
python3 usha-canvas/build.py
```

Page copy, member tiers, testimonials, and the shared nav, join, newsletter, and footer sections all live in that file.

## Design rules that must not be broken

- Fonts: Space Grotesk (display, never below 20px), Syne (caps labels and buttons), Manrope (body, 16px minimum).
- Colors: navy `#0D1B2A`, ice `#F8F9FA`, cyan `#00D2FF`, gold `#FFB703`, purple `#3B0B59` / `#6C1FA0`. Cyan and gold are never text on light surfaces (use `#0089A8` and `#E09E00`). Gold and cyan buttons always carry navy text.
- The gold period ends display headlines. No exclamation points anywhere.
- Tagline: "Fifty states. One hydrogen economy. Built together."
- Copyright line reads 501(c)(6), never a © symbol in the entity type.
- Never redraw or rearrange the dot geometry; use the SVG masters only.

## Open items before launch

- Member logo artwork for all four tiers (names are placeholders today).
- Two LinkedIn URLs (USHA and the convention account).
- Policymaker roster names and photos, team and board photos, fellows list.
- Confirm stats, past-convention dates, and resource titles carried over from the mocks.
