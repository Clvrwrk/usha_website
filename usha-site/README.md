# USHA Site — Design System Rebuild

Page-by-page clone of [ushydrogenalliance.org](https://www.ushydrogenalliance.org/) rebuilt on the **USHA Brand & Design System v1.0** (`../design-import/USHA Design System.dc.html`), with every section structured on a Relume library component (annotated in the HTML as `data-relume` attributes + comments).

## Run locally

```bash
python3 -m http.server 8942 --directory usha-site
```

Then open http://localhost:8942. (Also configured in `.claude/launch.json` as `usha-site`.)

## Pages

| Page | Clones | Relume sections used |
|---|---|---|
| `index.html` | Homepage | Navbar 2 · Header 1 · Banner 1 (marquee) · CTA 25 · Layout 1 · Layout 16 · Layout 3 + Stats 2 · Logo 4 · Testimonial 1 · Layout 238 · CTA 26 · Footer 4 |
| `about.html` | /about-us | Header 5 · Layout 239 · Layout 242 · Stats 2 · Layout 25 |
| `membership.html` | /membership | Header 5 · Layout 238 · Testimonial 4 · Logo 4 |
| `policymakers.html` | /policymakers | Header 5 · Layout 16 · Layout 396 |
| `industry.html` | /industry | Header 5 · Layout 396 |
| `events.html` | /usha-events | Header 5 + Stats 2 · Event 1 · Event 5 |
| `media-room.html` | /news-room | Header 5 · Layout 16 · Blog 33 |
| `resources.html` | /resources | Header 5 · Blog 44 |
| `common-bond.html` | /common-bond | Header 5 · Layout 242 · Layout 3 · Contact 2 |
| `contact.html` | /contact-form | Header 5 · Contact 2 |

Every page shares: Navbar 2 (sticky navy 90% + blur, gold JOIN pill), Layout 238 (six member benefits), CTA 26 (newsletter), Footer 4 (seal + gold rule).

## Design system applied

- **Color:** navy `#0D1B2A` ground · ice `#F8F9FA` air · cyan `#00D2FF` current (dark surfaces only; `#0089A8` on light) · gold `#FFB703` action · purple `#3B0B59/#6C1FA0` gravity. 60/30/10 ratio, dark-first with alternating light sections.
- **Type:** Space Grotesk (display, gold period, no exclamation points) · Syne (caps labels/buttons, +8–22% tracking) · Manrope (body 16px, 1.7 line-height).
- **Rhythm:** Fibonacci spacing tokens (8/13/21/34/55/89/144), 62/38 golden splits, 1216px content max.
- **Components:** pill buttons (44px min, gold⇄cyan hover swap, navy text), 12px-radius cards with tinted borders and 8px hover lift, 2px cyan focus rings.
- **Marks:** spectrum map (dark heroes), gold-navy duotone + knockout maps (feature splits), full-color seal (footer), dotted-H monogram (nav + favicon). `usha-h-full-dark.svg` is derived from the light master per the dark-palette convention.
- **Motion:** 200ms ease-out micro-motion, reveal-on-scroll (Assemble-lite), marquee as the only linear motion, all honoring `prefers-reduced-motion`.
- **Voice:** declarative headlines, "the gold period," no hedges — per DS §02.

## Not yet built

Member profile pages (~50 on the original — needs one Relume Layout 1 template + a data file), blog/news detail pages, job board, and the webinar/registration flows. Forms are static (`action="#"`) — wire to the real backend or a form service before launch.
