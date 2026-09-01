# Project Handoff — USHA Website Rebuild
**Project:** USHA Website Rebuild (United States Hydrogen Alliance)
**Repo:** none yet — not a git repo (see CLAT-8; folder is Dropbox-synced: `Cleverwork Main/USHA/`)
**Production URL:** not yet deployed (original live site: https://www.ushydrogenalliance.org/ on Wix)
**Date:** 2026-07-30 22:55
**Agent:** Lead Orchestrator
**Reason:** User-requested (/project-handoff)

---

## Accomplished This Session

### Design system import (from Claude Design project "H4 Abstract Prism logo", id `356e778a-0027-4806-80d3-9a778a7d8a16`)

- `design-import/USHA Design System.dc.html`: full 14-section Brand & Design System v1.0 (foundation, voice, logos, color, type, golden-ratio grid, dot language, motion, digital/print/ads, press kit, a11y, governance)
- `design-import/assets/*.svg`: 7 SVG masters — dotted-H monogram, map full-light / gold-navy / knockout / spectrum-dark, seal fullcolor light + dark
- `design-import/doc-page.js`, `design-import/support.js`: render runtime for the .dc.html doc

### Site review + infrastructure

- Reviewed live ushydrogenalliance.org (Wix, red/white/blue, ~100 pages incl. ~50 member profiles) — full page inventory pulled from `pages-sitemap.xml`
- Installed Relume Library MCP (`claude mcp add --transport http relume-library https://relume-library-mcp.relume.io/mcp`, local scope) — user completed OAuth; status ✔ Connected
- `.claude/launch.json`: preview server config `usha-site` (python http.server, port 8942)

### The build — `usha-site/` (10 pages, all visually verified in browser)

- `usha-site/css/usha.css`: complete design-system stylesheet — tokens, buttons (gold⇄cyan hover swap), cards, nav, marquee, stats, logo walls, forms, footer, reveal motion w/ reduced-motion support
- `usha-site/js/usha.js`: nav toggle + IntersectionObserver reveal
- `usha-site/index.html`: homepage clone — hero (62/38, spectrum map), gold marquee, convention CTA card, Common Bond split, audience cards, about + stats (23/17/150+/74%), 4-tier logo walls, testimonial, benefits, newsletter
- `usha-site/about.html`, `membership.html`, `policymakers.html`, `industry.html`, `events.html`, `media-room.html`, `resources.html`, `common-bond.html`, `contact.html`: section-by-section clones with real copy rewritten into DS voice
- `usha-site/assets/`: 8 SVGs (7 masters + derived `usha-h-full-dark.svg` via palette-swap sed)
- `usha-site/README.md`: page → Relume component map + run instructions
- Every section annotated `data-relume="<component>"` (Navbar 2, Header 1/5, Layouts, Stats 2, Logo 4, Testimonials, Events, Blogs, CTAs, Contact 2, Footer 4)

### Linear project (CLAUDE AGENT TEAM, key CLAT)

- Project: **USHA Website Rebuild** — https://linear.app/cleverwork/project/usha-website-rebuild-4b70db424293 (High priority, In Progress, gold, eagle icon)
- Milestone: **V1 Launch — Full Site Live** (target 2026-09-01, ahead of the Sept 8–10 Atlantic City convention)
- Issues CLAT-1 … CLAT-9 (see Next Task below)

## Git State
- **Branch:** n/a — not a git repo
- **Last commit:** n/a
- **Uncommitted changes:** everything is un-versioned. Creating the repo is step 1 of CLAT-8.

| File | Status | Note |
|------|--------|------|
| `usha-site/**` | Added | this session |
| `design-import/**` | Added | this session |
| `.claude/launch.json` | Added | this session |
| `docs/handoffs/**` | Added | this session |

## Task Cut Off
None — session ended at a clean boundary. Build complete and verified; Linear backlog created.

## Next Task — Start Here

**Task:** CLAT-1 — Member profile template + generate ~50 member pages
**What to check / do:**
1. Start the preview (`python3 -m http.server 8942 --directory usha-site` from the USHA folder) and confirm all 10 pages still render
2. Extract member slugs + names from `pages-sitemap.xml` (already fetched once — refetch from https://www.ushydrogenalliance.org/pages-sitemap.xml) into `usha-site/data/members.json` with tier assignments (tiers listed on membership.html)
3. Build one member-profile template (Relume Layout 1: 62/38 split, member info left, USHA membership CTA right) and extend the page generator to emit one page per member at the original slug
4. Add `members.html` index grouped by tier

**If the Relume MCP tools are needed:** they only load in a session started fresh in this directory (this session predates the install) — CLAT-3 depends on that.

**Prompt to use:** "Read docs/handoffs/current.md. Then start CLAT-1: build the member profile template and generate all member pages from the original Wix slugs."

## Decisions Made This Session

- **Static hand-built HTML over a framework:** 10-page marketing site, no app logic; a generator script (`build_usha_site.py` pattern) handles repetition. Do not introduce React/Next unless the CMS decision (CLAT-5) demands it.
- **Relume-patterned, not Relume-exported:** the Relume MCP authenticated mid-session so its tools weren't loadable; sections were structured on the Relume taxonomy with `data-relume` annotations. CLAT-3 swaps in exact exports where they beat the hand-built markup.
- **Copy rewritten into DS voice, not copied verbatim:** declarative headlines, gold period, no exclamation points (DS §02). Mission/legal text kept verbatim. USHA sign-off gate is CLAT-9 (Urgent).
- **Scope: 10 core pages first, member profiles via template:** ~50 member pages + ~40 event/registration one-offs are generated/deferred work (CLAT-1, CLAT-5), not hand-cloned.
- **`usha-h-full-dark.svg` derived by palette swap** (navy→ice, purple→light-purple, cyan-2→cyan) per the DS dark-palette convention — the true master exists in the Claude Design project if pixel-exactness ever matters.
- **Button CSS uses doubled specificity** (`.btn.btn-primary`) so surface link colors (`.on-dark a`) can never recolor button text — this was a real bug, fixed and verified.

## Blockers Requiring Human Action

1. **USHA stakeholder sign-off (CLAT-9)** — the rebrand is a full visual overhaul; get Roxana Bekemohammadi + team in front of a staging URL before deep polish
2. **Domain/DNS access** — who controls the ushydrogenalliance.org registrar? Needed for CLAT-8 cutover
3. **Member logo assets** — originals from USHA or scraped from Wix media (CLAT-4)
4. **Newsletter list access** — which ESP does the Wix subscribe feed? Needed for CLAT-2

## Verification Commands
1. `ls "usha-site"` — should list 10 .html files + README.md + assets/ + css/ + js/
2. `python3 -m http.server 8942 --directory usha-site` then open http://localhost:8942 — homepage renders: navy hero, spectrum map, gold marquee, gold "BECOME A MEMBER" pill with **navy** text
3. `claude mcp get relume-library` — should show ✔ Connected
4. `grep -c data-relume usha-site/index.html` — should return 12+

## Full Context

### What was built across ALL sessions (complete feature list)
- Session 2026-07-30 (this one): design system imported from Claude Design; live-site review + full page inventory; Relume MCP installed + authenticated; 10-page site build (`usha-site/`) on the design system with Relume-annotated sections; preview server config; Linear project CLAT w/ milestone + 9 issues; this handoff

### Architecture decisions
- Plain static HTML/CSS/JS, generated by script where repetitive — no build step, no framework
- Pages share chrome (nav/benefits/newsletter/footer) duplicated at generation time, not runtime includes
- One stylesheet holds the whole design system as CSS custom properties; pages use utility-ish classes (`.on-dark`, `.split`, `.card`, `.btn-primary`)
- Preview via `.claude/launch.json` → `usha-site` config, port 8942

### Design system (source of truth: `design-import/USHA Design System.dc.html`)
- Palette: navy #0D1B2A / ice #F8F9FA / cyan #00D2FF / gold #FFB703 / purple #3B0B59; extended tints for dots/data; #0089A8 replaces cyan as text on light; #E09E00 replaces gold as text on light (18px+)
- Type: Space Grotesk (display only, ≥20px), Syne (caps labels/buttons +8–34% tracking), Manrope (body, 16px min)
- Fibonacci spacing (8/13/21/34/55/89/144), 62/38 splits, 1216px content max, pill buttons 44px min
- Motion verbs: Erupt/Assemble/Pulse/Settle; 150–250ms UI micro-motion; marquee = only linear motion; always honor prefers-reduced-motion
- Voice: declarative, American-optimistic, technically fearless, wit-in-details; gold period replaces "!"

### Key invariants (never violate)
- **No cyan text on light surfaces** (1.6:1 — DS §13 FAIL); use #0089A8
- **No gold text on light surfaces** below 18px; pair with navy or use #E09E00
- **Gold/cyan buttons always carry navy text**
- **Never redraw/rearrange the dot geometry** — SVG masters only (DS §03 "Ten Commandments")
- **Space Grotesk never below 20px, never for paragraphs**
- **Member slugs must match original Wix URLs** (redirect integrity, CLAT-7)

### Service / deployment map
| Service | Detail |
|---------|--------|
| Linear | Team CLAUDE AGENT TEAM (CLAT), project https://linear.app/cleverwork/project/usha-website-rebuild-4b70db424293, milestone "V1 Launch — Full Site Live" (2026-09-01), issues CLAT-1…9 |
| Relume Library MCP | https://relume-library-mcp.relume.io/mcp — local scope in USHA dir, OAuth done, ✔ Connected (fresh session required for tools) |
| Claude Design | project `356e778a-0027-4806-80d3-9a778a7d8a16` ("H4 Abstract Prism logo") — full brand asset library incl. files not yet imported (brand-guidelines.md, component library, more SVG variants) |
| Preview | `.claude/launch.json` → `usha-site`, http://localhost:8942 |
| Original site | Wix (static.wixstatic.com assets) — keep alive until DNS cutover + redirects verified |
