# GoHighLevel AI Studio import kit

Everything needed to rebuild the USHA site inside GoHighLevel AI Studio, page by page, without losing the design system.

## Contents

| File | Use |
|---|---|
| `ai-studio-brief.md` | The master prompt for the project, one prompt per page, and the three follow-up prompts to run after every page. |
| `usha-tokens.css` | Color, type, spacing, and component styles as one responsive stylesheet. Paste it over the generated CSS in the Code Editor. |
| `copy/` | Every page's copy in reading order, with section, eyebrow, headline, button, and form-field markers. Use it to check nothing was rewritten and to fill SEO titles and descriptions. |
| `assets/` | The SVG logo masters and the Hydrogen Built hero photo. Upload all of them with the master prompt. |
| `forms-and-workflows.md` | Which forms exist, how each connects to the CRM, the tags and workflows to build, and the publishing checklist. |

## Preview URLs

AI Studio's "turn a URL into a page" needs each page on a public URL. The preview base is:

`BASE = https://clvrwrk.github.io/usha_website_preview/`

Page → desktop URL → mobile URL:

| Page | Desktop | Mobile |
|---|---|---|
| Home | `Main.dc.html` | `HomeMobile.dc.html` |
| About Us | `About.dc.html` | `AboutMobile.dc.html` |
| Membership | `Membership.dc.html` | `MembershipMobile.dc.html` |
| Policymakers | `Policymakers.dc.html` | `PolicymakersMobile.dc.html` |
| Industry | `Industry.dc.html` | `IndustryMobile.dc.html` |
| Events | `Events.dc.html` | `EventsMobile.dc.html` |
| Media Room | `MediaRoom.dc.html` | `MediaRoomMobile.dc.html` |
| Resources | `Resources.dc.html` | `ResourcesMobile.dc.html` |
| Hydrogen Built | `HydrogenBuilt.dc.html` | `HydrogenBuiltMobile.dc.html` |
| Contact | `Contact.dc.html` | `ContactMobile.dc.html` |
| Member profile template | `MemberProfile.dc.html` | `MemberProfileMobile.dc.html` |
| Design system sheet | `DesignSystem.dc.html` | |

The preview repository is a throwaway mirror of `usha-canvas/`; delete it once the site is live.

## Procedure

1. In the sub-account, enable AI Studio under Labs if it is not already on, then open AI Studio and create a new project.
2. Send the master prompt from `ai-studio-brief.md`. Attach every file in `assets/` and `usha-tokens.css`.
3. Send the Home page prompt. Wait for the build, then run the three follow-up prompts.
4. Open the Code Editor, find the project's global stylesheet, replace its contents with `usha-tokens.css`, save, and confirm the preview still matches.
5. Repeat step 3 for each remaining page in the order listed in the brief. Check each against its `copy/` file.
6. Connect forms and calendars per `forms-and-workflows.md`.
7. Publish to the preview domain, review every route on desktop and mobile, then connect the custom domain, set it primary, and enable Advanced SEO Support.

## Costs and limits to expect

HighLevel prices AI Studio by usage per session. Their own examples run about $0.60 to $1.30 per page, with generated images the biggest driver; this kit avoids image generation by supplying the artwork. Advanced SEO covers up to 150 routes. AI Studio projects cannot be exported or moved into the classic Sites builder.
