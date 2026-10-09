# Hardwired NWA — GiveCamp prototype

A local, eight-page Hugo concept for an adaptive fitness community in Northwest Arkansas. The design puts athlete access and scholarships alongside a clear starting point for prospective athletes.

This is a review prototype. It does not take donations, send inquiries, reserve scholarships, or represent an approved public website. Nothing has been deployed.

## Preview

From this project directory:

```sh
./scripts/preview
```

Open <http://localhost:1313/>. Hugo watches edits automatically. The cache lives inside the project, so no user cache directory access is required.

To generate the static prototype:

```sh
./scripts/build
```

The output goes to `public/`. Build output and caches are ignored. Tested with Hugo 0.166.0 extended; no Node package install, theme download, or backend is required.

## Pages

| Page | Route | Source |
| --- | --- | --- |
| Home | `/` | `layouts/index.html` |
| About | `/about/` | `content/about.md` |
| Our coach | `/our-coach/` | `content/our-coach.md` |
| Our gym | `/our-gym/` | `content/our-gym.md` |
| What is adaptive CrossFit? | `/adaptive-crossfit/` | `content/adaptive-crossfit.md` |
| Support & scholarships | `/support/` | `content/support.md` and `layouts/partials/support.html` |
| FAQ | `/faq/` | `content/faq.md` |
| Contact | `/contact/` | `content/contact.md` and `layouts/partials/contact.html` |

All eight routes are reachable through the header, footer, or page calls to action. Home is reached through the brand. Support has its own prominent header button.

## Prototype interactions

- Responsive navigation with a keyboard-operable mobile menu.
- Native expandable FAQ answers.
- Scholarship cost calculator for punch cards and monthly memberships.
- Donation explanation dialog with native Escape handling and focus restoration.
- Validated inquiry preview, rendered locally with no persistence or transmission.

Navigation, page content, FAQ, and the donation explanation anchor remain usable without JavaScript. The inquiry action stays disabled without JavaScript, preventing accidental form transmission. The calculator displays its initial cost and a no-JavaScript explanation.

## Design and assets

The supplied slate blue/deep teal (`#2C5D75`) and peach/apricot (`#F9B689`), with warm white and pale blue neutrals, pair with condensed display typography. Barlow Condensed and DM Sans are requested from Google Fonts with system fallbacks; the rest of the site and its illustration are local. Fonts may differ offline. See `docs/HANDOFF.md` for approval and production needs.

The concept brand mark is local SVG. The hero is AI-generated concept art of fictional people, visibly labeled on the website. It is not an approved logo, athlete photograph, coach portrait, or facility image. The illustration is in `static/images/adaptive-training-concept-blue-peach.png`; its generation prompt is in `docs/ART-PROMPT.md`.

## Editing and handoff

- Page introductions and copy: `content/`.
- Navigation and site metadata: `hugo.toml`.
- Home composition: `layouts/index.html`.
- Shared layout and functional page sections: `layouts/`.
- Colors, typography, and responsive layout: `assets/css/site.css`.
- Browser interactions: `assets/js/site.js`.

Detailed review needs and the path from this concept to a managed WordPress website are in `docs/HANDOFF.md`. Prototype pages include `noindex, nofollow`, including the 404 page.
