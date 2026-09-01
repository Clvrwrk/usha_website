# Forms, CRM connections, and workflows

AI Studio builds every form as a front-end layout only. Each one below must be connected by opening the form in the preview, clicking **Connect**, and completing the Connect to CRM flow. Submissions then arrive in Contacts and under Sites > Forms > Submissions > External Forms. Workflows fire from the **External Tracking Event** trigger with the **Form submission** event, filtered by domain and external form name.

| Form | Page | Fields | Tag to apply | Workflow to build |
|---|---|---|---|---|
| Newsletter | every page | Work email | `newsletter` | Add to newsletter list, send welcome email |
| Contact | /contact | First name, Last name, Work email, Organization, Reaching out about (Membership / Speak at an event / Media inquiry / Policy / Other), Message | `contact-form` plus one tag per topic | Notify marketing@ushydrogenalliance.org, create an opportunity when topic = Membership |
| Hydrogen Built sign-on | /hydrogen-built | First name, Last name, Organization (optional), Email, State, I am a… (Business / Worker / Policymaker / Community member / Other), Updates opt-in | `hydrogen-built` | Add to the campaign list, send the campaign welcome, tag by "I am a" value |
| Policy Leaders Roundtable request | /policymakers | First name, Last name, Title, Work email, State, Office type (State legislator / Governor's office / Agency / Local / Federal / Staff), Message, Updates opt-in | `policymaker`, `roundtable-request` | Notify the policy team, create a task to follow up within two business days |
| Membership application | linked from Membership and Join sections | Existing application (external link or GHL form) | `membership-inquiry` | Existing membership pipeline |
| Convention registration | /events, /policymakers | Existing registration flow | `convention-2026` | Existing event workflow |

## Calendars

None of the v1.0 pages embeds a calendar. If "Speak at an event" or membership strategy calls should book directly, connect a sub-account calendar to the Contact page after the site is live.

## Custom values to set once

- Convention date and location (used on Home, Events, Policymakers): September 8–10, 2026 · Atlantic City, NJ.
- Contact email: marketing@ushydrogenalliance.org.
- LinkedIn (USHA) and LinkedIn (Convention) URLs: still to be supplied.

## Publishing checklist

1. Publish to the preview domain and click through every route on desktop and at 390px.
2. Connect the four forms and the newsletter, submit a test through each, confirm the contact and tag appear.
3. Connect ushydrogenalliance.org (DNS access still needs to be confirmed), set it as the primary published URL so other URLs 301 to it.
4. Turn on Advanced SEO Support: pre-render, social previews, sitemap. Add page titles and descriptions from `copy/`.
5. Keep the Wix site live until the DNS cutover is verified and the old member profile slugs redirect.
