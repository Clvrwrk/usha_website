# USHA Brand & Design System — Developer Reference
**United States Hydrogen Alliance · v1.0 · July 2026**
Master doc: `USHA Design System.dc.html` (+ PDF export). Assets: `/assets`. Geometry is the source of truth — never redraw dots.

---

## 1. Brand core
- **Positioning:** The one voice for American hydrogen — from statehouse to seaport.
- **Tagline:** One molecule. Every state. Zero excuses.
- **Identity idea:** America as a field of dots — each a town, plant, port, person — that only becomes the map together.

## 2. Voice & tone
Four rules: **Declarative** (verdicts, not hedges) · **American-optimistic** (places and workers by name, warmth not volume) · **Technically fearless** (real terms + plain-English payoff) · **Wit in the details** (one structural wink max; the gold period replaces the exclamation point).

Say / not: "clean, domestic, union-built" not "green, sustainable" · "hydrogen jobs on the way" not "potential employment opportunities" · "pilot to price parity" not "scaling our learnings" · "The Alliance is open." not stakeholder-speak.

## 3. Color tokens

```css
:root {
  /* Core palette */
  --usha-navy:   #0D1B2A;  /* PMS 532 C  · C90 M75 Y50 K70 · ground, text on light */
  --usha-ice:    #F8F9FA;  /*             C2 M1 Y1 K0      · air, text on dark */
  --usha-cyan:   #00D2FF;  /* PMS 306 C  · C75 M0 Y5 K0    · current, links on dark ONLY */
  --usha-gold:   #FFB703;  /* PMS 7549 C · C0 M30 Y100 K0  · action, CTAs, the period */
  --usha-purple: #3B0B59;  /* PMS 2627 C · C80 M100 Y35 K40 · gravity, accents on light */

  /* Derived tints (dots, data, states only) */
  --usha-purple-900: #2A073F; --usha-purple-600: #6C1FA0; --usha-purple-400: #9D4EDD;
  --usha-cyan-700: #0089A8;   --usha-cyan-600: #00A8CC;   --usha-cyan-200: #7CE4FF;
  --usha-gold-600: #E09E00;   --usha-gold-300: #FFC733;   --usha-gold-200: #FFD866;

  /* Functional (product UI only) */
  --usha-success: #21A66E; --usha-warning: #FFB703; --usha-error: #E5484D; --usha-info: #00A8CC;

  /* Spectrum gradient — always west→east / left→right */
  --usha-spectrum-dark:  linear-gradient(90deg, #9D4EDD, #6C1FA0, #00A8CC, #00D2FF);
  --usha-spectrum-light: linear-gradient(90deg, #3B0B59, #6C1FA0, #0089A8, #00A8CC);
}
```

Ratio per surface: **60 ground · 30 air/structure · 10 current+action**.
Hard rules: cyan and gold are **never text on light** (use `--usha-cyan-700` / `--usha-gold-600` ≥18px, or pair with navy). Gold/cyan fills always carry navy text.

## 4. Typography

| Token | Web | Print | Face · weight | Use |
|---|---|---|---|---|
| display-xl | 89px | 48pt | Unbounded 900 | hero only |
| display-l | 55px | 30pt | Unbounded 800 | section leads |
| heading-1 | 34px | 20pt | Unbounded 800 | page/card titles |
| heading-2 | 21px | 14pt | Unbounded 800 | subsections |
| label | 13px | 9pt | Space Grotesk 700, caps, +0.18em | eyebrows, buttons, tags |
| body-l | 18px | 12pt | Manrope 500 | leads |
| body | 16px | 11pt | Manrope 500 | default |
| caption | 13px | 9pt | Manrope 600 | footnotes |

```css
--usha-font-display: 'Unbounded', sans-serif;   /* 800–900; 500 marquee; tracking -0.01 to -0.02em; never <20px; never paragraphs */
--usha-font-label:   'Space Grotesk', sans-serif; /* 600–700 CAPS, +0.08 to +0.34em */
--usha-font-body:    'Manrope', sans-serif;       /* 500–800; line-height 1.6–1.7 */
```

Scale = Fibonacci (13·21·34·55·89), step ≈ φ. Minimums: 16px web body, 11pt print, 24px on 1920×1080 slides. Display headlines end with the gold period (`<span style="color:var(--usha-gold)">.</span>`).

## 5. Golden ratio, grid & spacing

```css
/* Fibonacci spacing */
--usha-sp-1: 8px;  --usha-sp-2: 13px; --usha-sp-3: 21px; --usha-sp-4: 34px;
--usha-sp-5: 55px; --usha-sp-6: 89px; --usha-sp-7: 144px;
```
- sp-1/2 inside components · sp-3/4 between elements · sp-5/6 between blocks · sp-7 between page sections.
- Two-column layouts split **62/38** (φ), not 50/50: `grid-template-columns: 1.618fr 1fr`.
- Desktop: 12 col, 1216px max, 24px gutters, 56px margins. Mobile 390: 4 col, 24px margins, **44px min hit targets**. Print: 8 col, 0.75–0.8in margins. Slides: 12 col, 96px margins.

## 6. Logo system
| Mark | File(s) | Min size | Use |
|---|---|---|---|
| Map (primary) | `usha-map-full-*`, `-spectrum-*`, `-mono-navy`, `-knockout`, `-gold-navy` | 120px / 30mm | heroes, covers, booth, video |
| H monogram | `usha-h-full-*`, `-mono-navy/-ice` | 16px | favicon, avatar, embroidery, the H in US**H**A |
| Seal | `usha-seal-navy/-ice`, `-fullcolor-*`, `-spectrum-*` | 64px / 16mm (inner H only <24px) | documents, pins, certification, avatars |
| Wordmark | Unbounded 800, tracking −2%; sub-line Manrope 600 +32% caps | — | gold sub on dark, purple on light; sits 3–5px below map's purple dot row |

Clear space: **X = largest dot diameter; 2X all sides; 3X to other logos.**
NEVER: recolor outside approved palettes · stretch/skew/rotate/outline · add/delete/rearrange dots · shadows/bevels (glow allowed on dark only) · marks on photos without scrim · cyan marks/text on light · off-center seal text · old seed palette · non-Unbounded wordmark · motion outside §8 verbs.

## 7. Dot field rules
Dots grow west→east (big civic dots left, fine network right) — keep the reading. Crop confidently; a full tiny map is wallpaper. One dot may become a graphic period/bullet. Fields sit behind/beside type — body copy needs a scrim. Data viz inherits the dot (circles, spectrum-colored low→high).

## 8. Motion
Verbs, in canonical order: **Erupt** (600–900ms, back-out) → **Assemble** (1.8–2.4s, west→east stagger) → **Pulse** (1.5–2s scale wave +35–45%) → **Settle** (final 15% at rest).
UI micro-motion 150–250ms ease-out; hover lift −8px; marquee = only linear motion. Seal ring rotates 30–36s/rev, ring text never rotates. Honor `prefers-reduced-motion` (render assembled, static).
Masters: `USHA Logo Intro.dc.html` (16:9 + 9:16, timeline-editable, exportable video).

## 9. Components (web)
```css
.usha-btn { border-radius: 999px; min-height: 44px; padding: 13px 26px;
  font: 700 13px/1 'Space Grotesk'; letter-spacing: 0.08em; text-transform: uppercase; }
.usha-btn--primary   { background: var(--usha-gold); color: var(--usha-navy); }  /* hover: cyan */
.usha-btn--secondary { background: var(--usha-cyan); color: var(--usha-navy); }  /* hover: gold */
.usha-btn--tertiary  { border: 2px solid rgba(248,249,250,.35); color: var(--usha-ice); }
:focus-visible { outline: 2px solid var(--usha-cyan); outline-offset: 2px; }
.usha-card { border-radius: 12px; border: 1px solid rgba(157,78,221,.4); /* or cyan/gold @35–40% */
  background: linear-gradient(160deg, rgba(59,11,89,.55), rgba(13,27,42,.4)); }
```
Nav: sticky, `rgba(13,27,42,.88)` + blur(12px), H-mark + USHA left, gold JOIN pill right.
Avatars: seal (brand), H-on-navy (programs). Never the map in a circle crop.

## 10. Print / swag / ads quick specs
- Ink ladder: 4CP → 2-spot (532+7549) → 1-spot (532 or reversed). Foil = 7549 substitute.
- Tees: knockout map, navy garment, ice+gold plates, ≥9in. Pins/coins: seal 0.75–1in (drop ring text <0.75in). Embroidery: mono H ≥2in, merge dots <1mm. Bottles: vertical lockup, 1-color ice. Booth: spectrum map bleed + gold marquee band.
- Ad formula: one declarative headline + one dot field + one gold CTA. 300×250/320×50: H-mark. 728×90/970×250: horizontal lockup. 300×600/stories: vertical. 1080×1080: seal or map center. 1200×628: hero recipe 62/38. OOH: ≤7 words.
- Video: open Badge or Erupt→Assemble; end on Outro end-card (QR + next videos). Lower thirds: navy bar, ice Space Grotesk caps, gold rule. Captions always, Manrope 600.

## 11. Accessibility
AAA pairs: ice/navy (16.9), cyan/navy (9.6), gold↔navy (9.2), purple/ice (14.5). FAIL: cyan or gold as text on light. Alt text: "USHA [mark], [treatment] on [background]". Never meaning by color alone.

## 12. Assets & naming
`usha-[mark]-[treatment]-[mode].svg` — lowercase, hyphenated; mode = background it sits on. SVG masters in `/assets` (17 files); export PNG @2× for raster.
**Press boilerplate:** "The United States Hydrogen Alliance (USHA) is the national coalition advancing clean, domestic, union-built hydrogen across all 50 states."

## Revision log
| Version | Date | Change | Owner |
|---|---|---|---|
| 1.0 | 2026-07 | Genesis release | — |
