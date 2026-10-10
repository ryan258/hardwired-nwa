# GiveCamp review and handoff

## What exists

An eight-page responsive Hugo prototype, hosted live on GitHub Pages for stakeholder review:
👉 **Live Review Site**: <https://ryan258.github.io/hardwired-nwa/>  
👉 **Source Repository**: <https://github.com/ryan258/hardwired-nwa>

The prototype features a proposed visual identity and draft copy derived from the user-supplied project charter, combined with the confirmed brand palette (slate blue and peach) and a handwritten gym whiteboard mural aesthetic. It implements the requested mockup change from WordPress to Hugo, while preserving a clean migration path to WordPress or managed static hosting if desired.

The prototype centers two primary visitor journeys: an athlete can explore adaptive training, review the gym whiteboard pyramid, and preview an inquiry message; a supporter can explore scholarship costs and view the proposed ARCF donation handoff.

## Review the experience

1. **Live Deployment**: Open <https://ryan258.github.io/hardwired-nwa/>.
2. **Athlete Journey**: Follow “Find your starting point” to Contact (`/contact/`). Enter sample information and choose “Preview your inquiry.” Nothing is sent or stored.
3. **Training Wall**: Explore the mural-inspired training wall sketch on Home and Adaptive CrossFit (`/adaptive-crossfit/`). Review the 5-layer pyramid (Sport, Lifting, Gymnastics, Conditioning, Nutrition) and the 10 general physical skills vector cards (Cardio through Accuracy), and jump to the `#what-scaling-means` anchor.
4. **Supporter Journey**: Follow “Sponsor an athlete” to Support (`/support/`). Choose monthly membership and 6 months; the calculator displays $810. Choose punch cards and 6 cards; the calculator displays $450 and 60 visits.
5. **Donation Modal**: Click “Explore monthly support” or “Explore this gift” to trigger the donation dialog. Dismiss using the close button or keyboard `Escape`.
6. **FAQ**: Expand questions on FAQ (`/faq/`) with keyboard `Enter` or pointer.
7. **Mobile Drawer**: Resize to a mobile viewport (<820px), open the hamburger menu, navigate, and close using `Escape` or outer click.

## Organization confirmation before public use

| Topic | Supplied evidence | Needed confirmation |
| --- | --- | --- |
| Mission and program | User-supplied charter | Approved organization wording and scope |
| Elisabeth | Founder/head coach; eight years; L1/L2 and adaptive certificate | Full approved name/bio, dates, current credentials, portrait consent |
| Gym | Adaptive equipment and community training space | Address, parking, entrance, restrooms, exact equipment and access details |
| Classes | Inclusive/adaptive group training concept | Current schedule, introductory visit, enrollment process, safety procedures |
| Prices | $75 ten-visit card; $135 unlimited month | Current prices, inclusions, expiration, billing, extra terms, and gear funding language |
| Scholarships | Proposed individual/corporate athlete sponsorship | Eligibility, matching, privacy/consent, designation restrictions, ongoing administration |
| Donations | Proposed ARCF portal | Exact approved organization/fund URL, available gift types, recurring support and designation rules |
| Contact | Inquiry form requested | Destination inbox, approved contact details, privacy notice, spam handling and delivery verification |
| Assets | Logo supplied and selected for the prototype; mural reference supplied | Production logo master if available, rights-cleared athlete/facility photos and video, captions, alt text, consent |

The stray `1`, `2`, and similar numbers in the pasted charter were not accompanied by source references. They have not been treated as verified citations. The prototype uses the charter as draft input and does not claim independent verification.

Six punch cards totaling $450 is a cost example, not a verified usage statistic. No testimonials, named athletes, partner endorsements, impact totals, or donation receipts have been invented. Walmart is not displayed as an established partner.

## Content and imagery

Page-specific pending details are visible within the draft content:
- The home scene shows fictional people and an imagined gym; the coach page makes clear that it is not a portrait. Replace the illustration only with approved media and matching alt text.
- The latest supplied Hardwired NWA badge is preserved unchanged in `assets/images/hardwired-nwa-badge-original.png`. The website uses its transparent vector trace, `assets/images/hardwired-nwa-badge.svg`, in the header and footer. All white areas are transparent, including the badge interior and letter counters. A downloadable copy is at `static/downloads/hardwired-nwa-logo.svg`. Earlier circular logo assets are retained. This trace is derived from the supplied PNG; obtain the original vector master if available for production.
- The training wall sketch (`layouts/partials/training-wall.html`) reflects the handwritten gym whiteboard mural (`docs/references/mural-reference.png`, `docs/MURAL-DIRECTION.md`). It features both the five visible layers (Sport, Lifting, Gymnastics, Conditioning, Nutrition) and the ten general physical skills (Cardio, Stamina, Strength, Flexibility, Power, Speed, Coordination, Agility, Balance, Accuracy) rendered using scalable SVG symbols (`assets/images/physical-skills-icons.svg`). The shared downloadable sprite is at `static/images/hardwired-icons.svg` (all 14 icon symbols; regenerate with `python3 scripts/build_svg_sprite.py`, see `docs/SVG-SPRITE.md`) and a standalone sprite preview is at `/motifs-preview/` (`static/motifs-preview/index.html`).

## Accessibility status

Implemented: semantic landmarks, one main heading per page, a skip link, labeled form controls, visible focus indicators, native FAQ and dialog behavior, touch-sized actions, responsive layout, and reduced-motion support. The calculator uses an `aria-live="polite"` status region and the form preview uses text content rather than rendering user input as HTML. The training pyramid and physical skills grid use accessible HTML list items (`<ol class="training-pyramid">` and `<ol class="skills-grid">`), while decorative SVG icons and geometry are marked `aria-hidden="true"`.

Automated tests check all routes and assets under both root and subpath baseURLs via `scripts/check_links.py`. These are implementation checks, not a full WCAG conformance determination. Human keyboard, screen-reader, real-device, content, and facility-access review remain separate acceptance work.

## Production work after mockup approval

1. **CMS & Hosting Selection**: Decide whether the production website remains WordPress as in the charter or uses static hosting (e.g., custom domain on GitHub Pages, Cloudflare Pages, or Netlify). This prototype does not provide a WordPress admin interface.
2. **WordPress Transition (if selected)**: Transfer the approved layout, CSS design tokens, and copy into an editable theme or block system. Keep shared colors and type consistent. Hosting, domain registration, DreamHost program eligibility, TLS, administrator access, backups, and maintenance ownership require separate implementation.
3. **Donation Gateway**: Connect the approved donation destination as an ordinary external link to the ARCF portal. Define what the organization can promise regarding sponsorship selection and recurring payments.
4. **Inquiry Delivery**: Connect contact submissions to an approved inbox, add spam mitigation, and verify message receipt. Confirm privacy disclosures with the organization.
5. **Real Assets & Public Launch**: Replace concept athlete imagery with cleared photography, and obtain a production logo master if available, update schedules, complete final assistive technology audits, and remove prototype disclaimers and `noindex` headers.
