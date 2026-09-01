# USHA site: AI Studio build brief

Paste the master prompt once when you create the project. Then build one page at a time with the per-page prompts, each of which points at a live preview URL. After each page, open the Code Editor and replace the generated stylesheet with `usha-tokens.css` (see the kit README for the exact steps).

---

## Master prompt (first message in the project)

```
You are rebuilding the website of the United States Hydrogen Alliance (USHA), a national 501(c)(6) business association advancing hydrogen policy and markets in all 50 states. Rebuild each page I give you as faithfully as possible from its preview URL. Do not invent sections, copy, images, or statistics. Use only the copy on the preview page.

Brand rules that must never be broken:
- Fonts from Google Fonts: Space Grotesk 700 for all headlines (never below 20px, never for paragraphs), Syne 600–800 in uppercase with wide letter-spacing for eyebrows, labels, buttons and nav, Manrope 500–800 for body text (16px minimum, line-height 1.7).
- Colors, exact hex only: navy #0D1B2A (page ground), ice #F8F9FA (light sections and text on dark), tint #F1F4F7 (alternating light sections), cyan #00D2FF (eyebrows and accents on dark only), gold #FFB703 (primary buttons, the period at the end of every headline, plus signs in stats), purple #6C1FA0 (pill labels on cards, eyebrows on light). On light backgrounds use #0089A8 instead of cyan and #E09E00 instead of gold for text. Body text is #45566B on light and #B9C6D6 on dark.
- Buttons are pills (border-radius 999px), 44px minimum height, Syne 700 uppercase 13px with 0.08em tracking. Primary buttons are gold with navy text and turn cyan on hover. Secondary buttons are transparent with a 2px 35% border.
- Cards are 12px radius with a 1px tinted border and lift 8px on hover. Every card follows one format: a purple pill label, a bold Space Grotesk title, Manrope body.
- Sections alternate navy, ice, tint. Content is 1216px wide max with 56px side margins on desktop, 24px on mobile. Two-column sections split 62/38, not 50/50.
- Every headline ends with a gold period. Never use an exclamation point anywhere. The tagline is "Fifty states. One hydrogen economy. Built together." The copyright line reads "© 2026 United States Hydrogen Alliance · 501(c)(6)".
- Do not generate logos or dot-map artwork. I will upload the SVG masters: use usha-h-full-dark.svg for the nav and footer mark on navy, usha-map-full-dark.svg on navy sections, usha-map-full-light.svg on light sections, usha-h-full-light.svg on light. Never redraw, recolor, or rearrange the dots.
- Shared chrome on every page: a sticky navy nav (H mark + "USHA" wordmark left; About Us, Membership, Policymakers, Industry, Events, Media Room, Resources; gold JOIN pill right), a "Join the United States Hydrogen Alliance." section with six cards, a "Stay ahead." newsletter section, and a footer with the H + USHA lockup, the tagline on one line, three link columns (Alliance / Work / Newsroom), a gold rule, and a centered copyright.
- Mobile: stack every grid to one column, buttons go full width, 48px tall, the nav collapses to the mark, a JOIN pill, and a menu button.

Build every form as a real form so it can be connected to the CRM later. Keep the site a multi-page project with these routes: /, /about, /membership, /policymakers, /industry, /events, /media-room, /resources, /hydrogen-built, /contact, /members/[slug].
```

Upload with the master prompt: every file in `kit/assets/` and `kit/usha-tokens.css`.

---

## Per-page prompts

Replace `BASE` with the preview base URL from the kit README.

### Home (route `/`)
```
Rebuild BASE/Main.dc.html as the home page. Mobile reference: BASE/HomeMobile.dc.html. Keep the kinetic eyebrow "HYDROGEN IS ENTERING A NEW ERA" at 39px, animated letter by letter, left to right, looping every 9 seconds. The gold marquee strip under the hero scrolls continuously. The About section headline alternates: line one ice with a gold period, line two gold with an ice period. Stats: first row ice numbers with gold plus signs, second row gold numbers with ice plus signs.
```

### About Us (route `/about`)
```
Rebuild BASE/About.dc.html. Mobile: BASE/AboutMobile.dc.html. Both periods in the hero headline are gold. The leadership and board sections sit on the #EEF2F6 surface. The "See the record" button scrolls to the testimonials section on the same page.
```

### Membership (route `/membership`)
```
Rebuild BASE/Membership.dc.html. Mobile: BASE/MembershipMobile.dc.html. Note the Join section on this page is different from the other pages: eyebrow "PEOPLE. POLICY. MARKETS." with the headline "Your seat is at the table." Keep the four member tiers exactly as listed; member names are text placeholders until logos are supplied.
```

### Policymakers (route `/policymakers`)
```
Rebuild BASE/Policymakers.dc.html. Mobile: BASE/PolicymakersMobile.dc.html. The "Join the Hydrogen Policy Leaders Roundtable" form on the dark section must be a working form. The eight policymaker avatars are placeholders; keep them as initials circles.
```

### Industry (route `/industry`)
```
Rebuild BASE/Industry.dc.html. Mobile: BASE/IndustryMobile.dc.html. Recreate the "Everything is connected" ring diagram with MARKET at the center and eight nodes around it, in HTML/CSS, not as an image.
```

### Events (route `/events`)
```
Rebuild BASE/Events.dc.html. Mobile: BASE/EventsMobile.dc.html.
```

### Media Room (route `/media-room`)
```
Rebuild BASE/MediaRoom.dc.html. Mobile: BASE/MediaRoomMobile.dc.html. The six coverage cards should become a CMS collection so new items can be added without editing the page.
```

### Resources (route `/resources`)
```
Rebuild BASE/Resources.dc.html. Mobile: BASE/ResourcesMobile.dc.html. The resource list should be a CMS collection with a date, title, one-line summary, category tags, and a file or link. The tag row filters the list. "Load more" paginates.
```

### Hydrogen Built (route `/hydrogen-built`)
```
Rebuild BASE/HydrogenBuilt.dc.html. Mobile: BASE/HydrogenBuiltMobile.dc.html. Use the uploaded hb-hero.jpg as the hero photo with usha-map-knockout.svg overlaid at 85% opacity. The "I stand with Hydrogen Built" card is a working form with First name, Last name, Organization (optional), Email, State (select), I am a… (select), and an updates checkbox.
```

### Contact (route `/contact`)
```
Rebuild BASE/Contact.dc.html. Mobile: BASE/ContactMobile.dc.html. One working form: First name, Last name, Work email, Organization, "I'm reaching out about" (select), Message. The only email address on the page is marketing@ushydrogenalliance.org.
```

### Member profile template (route `/members/[slug]`)
```
Rebuild BASE/MemberProfile.dc.html as a CMS template for member profiles. Mobile: BASE/MemberProfileMobile.dc.html. Fields: company name, tier, logo, one-paragraph profile, website URL, LinkedIn URL, headquarters, sector, member since, one quote and its attribution. Bracketed text on the preview marks each field.
```

---

## After each page: three follow-up prompts

```
Replace the generated stylesheet with the contents of usha-tokens.css I uploaded, keep the class names from the preview page, and remove any Tailwind or generated color that is not in that file.
```
```
Check every headline ends with a gold period, no text uses an exclamation point, and no cyan or gold text appears on a light background.
```
```
Show me the page at 390px wide and fix anything that overflows or wraps mid-word.
```
