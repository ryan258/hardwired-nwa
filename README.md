# Hardwired NWA — GiveCamp prototype

A Hugo concept and review prototype for an adaptive fitness community in Northwest Arkansas. The design puts athlete access and scholarships alongside a clear starting point for prospective athletes.

The prototype is hosted live on GitHub Pages for stakeholder review:
👉 **Live Review Site**: <https://ryan258.github.io/hardwired-nwa/>

This is a review prototype. It does not process donations, transmit inquiries, reserve scholarships, or represent an officially approved production website. All pages include `noindex, nofollow`.

## Quick Start & Local Preview

From this project directory:

```sh
./scripts/preview
```

Open <http://localhost:1313/>. Hugo watches edits automatically. The cache lives inside the project (`.hugo-cache`), so no user cache directory access is required.

To generate the static prototype locally:

```sh
./scripts/build
```

The output goes to `public/`. Build output and caches are git-ignored. Tested with Hugo 0.166.0 extended; no Node package install, theme download, or backend is required.

## Verification & Link Checking

To verify local links, assets, and fragment anchors under either the local root or the GitHub Pages subpath:

```sh
# Local build verification
./scripts/build && ./scripts/check_links.py ./public /

# Production subpath build verification
./scripts/build --baseURL "https://ryan258.github.io/hardwired-nwa/" && ./scripts/check_links.py ./public /hardwired-nwa/
```

Internal links and assets are checked across all generated HTML pages for missing targets, broken fragment anchors, and escaped base paths.

## Automated Deployment (CI/CD)

The repository deploys to GitHub Pages via GitHub Actions:
- **Workflow**: `.github/workflows/deploy.yml`
- **Triggers**: Pushes to `main` and manual `workflow_dispatch`
- **Steps**: Hugo 0.166.0 extended build, `scripts/check_links.py` validation, and deployment via `actions/deploy-pages@v4`.

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

All eight routes are reachable through the header, footer, or page calls to action. Home is reached through the supplied logo. Support has its own prominent header button.

## Prototype Interactions

- Responsive navigation with a keyboard-operable mobile menu.
- Native expandable FAQ answers.
- Scholarship cost calculator for punch cards and monthly memberships.
- Donation explanation dialog with native Escape handling and focus restoration.
- Validated inquiry preview, rendered locally with no persistence or transmission.
- Interactive and accessible training pyramid and 10 general physical skills wall sketch.

Navigation, page content, FAQ, and the donation explanation anchor remain usable without JavaScript. The inquiry action stays disabled without JavaScript, preventing accidental form transmission. The calculator displays its initial cost and a no-JavaScript fallback explanation.

## Design & Visual Direction

- **Brand Palette**: Slate blue/deep teal (`#2C5D75`) and peach/apricot (`#F9B689`), supported by warm white (`#F7F4EF`), pale blue (`#DCE9EF`), and dark navy (`#193442`). See `docs/PALETTE.md`.
- **Mural & Gym Sketch Direction**: Modeled after a handwritten gym whiteboard mural (`docs/references/mural-reference.png`), featuring Patrick Hand marker lettering, sketched borders, loose arrows, a hand-drawn barbell illustration, and an accessible 5-tier training pyramid (Nutrition, Conditioning, Gymnastics, Lifting, Sport). See `docs/MURAL-DIRECTION.md`.
- **Physical Skill Motifs**: 10 vector SVG skill motifs (Cardio, Stamina, Strength, Flexibility, Power, Speed, Coordination, Agility, Balance, Accuracy) inspired by the mural, integrated into the training wall with downloadable symbols (`static/images/hardwired-icons.svg`) and interactive standalone preview at `/motifs-preview/`. See `docs/PHYSICAL-SKILL-MOTIFS.md`.
- **Typography**: Barlow Condensed, DM Sans, and Patrick Hand loaded via Google Fonts with system fallbacks.
- **Logo**: The supplied badge is retained unchanged in `assets/images/hardwired-nwa-badge-original.png`. The header and footer use `assets/images/hardwired-nwa-badge.svg`, a transparent vector trace with no embedded raster image. The downloadable SVG is at `static/downloads/hardwired-nwa-logo.svg`. Earlier circular logo assets are retained. See `docs/LOGO-EDIT.md` for provenance.
- **Favicon**: A compact blue hexagon with a white barbell follows the newer wordmark reference. SVG, 16/32px PNGs, a multi-size ICO, a 180px touch icon and a 512px site icon are included. Review and download at `/favicon-preview/`; regenerate with `python3 scripts/build_favicons.py` (ImageMagick required for export only). See `docs/FAVICON.md`.
- **Concept Imagery**: An AI-generated editorial concept illustration (`static/images/adaptive-training-concept-blue-peach.png`; prompt in `docs/ART-PROMPT.md`). Fictional concept artwork, not documentary photographs.

## Project Documentation & Roadmap

- **Handoff & Review Needs**: [`docs/HANDOFF.md`](docs/HANDOFF.md)
- **Targeted Verification Record**: [`docs/VERIFICATION.md`](docs/VERIFICATION.md)
- **Favicon Suite & Exports**: [`docs/FAVICON.md`](docs/FAVICON.md)
- **Donation Card SVG Icons**: [`docs/DONATION-ICONS.md`](docs/DONATION-ICONS.md)
- **Shared SVG Sprite Pipeline**: [`docs/SVG-SPRITE.md`](docs/SVG-SPRITE.md)
- **Physical Skill Motifs & Vector Icons**: [`docs/PHYSICAL-SKILL-MOTIFS.md`](docs/PHYSICAL-SKILL-MOTIFS.md)
- **Supporter Access Icons**: [`docs/ACCESS-ICONS.md`](docs/ACCESS-ICONS.md)
- **Our Commitments Review Set**: [`docs/COMMITMENT-ICONS.md`](docs/COMMITMENT-ICONS.md)
- **Logo Vector Trace & Transparency**: [`docs/LOGO-EDIT.md`](docs/LOGO-EDIT.md)
- **Mural Design Translation**: [`docs/MURAL-DIRECTION.md`](docs/MURAL-DIRECTION.md)
- **Palette & Contrast Specifications**: [`docs/PALETTE.md`](docs/PALETTE.md)
- **Hero Illustration Generation Record**: [`docs/ART-PROMPT.md`](docs/ART-PROMPT.md)
- **Project Roadmap & Milestones**: [`roadmap.md`](roadmap.md)

The shared SVG icon sprite contains all 24 icon symbols (`static/images/hardwired-icons.svg`). The latest additions are Donate Online and Donate by Check, with all 22 previous vectors preserved. `/icons-preview/` provides individual SVGs, visible donation, commitment, support and skills sheets, and the complete ZIP. Run `python3 scripts/build_svg_sprite.py` after changing the editable SVG sources. See `docs/SVG-SPRITE.md` for IDs and template usage.

