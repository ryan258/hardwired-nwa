# Access-to-support icons

## Additional SVG set — October 10, 2026

The current collection contains 24 vectors. The Access to Support expansion added three illustrations while preserving the original 16; later additions supplied commitment and donation icons without changing this trio. Editable support sources are `assets/images/motifs/support-move-your-way.svg`, `support-scholarships-available.svg`, and `support-coach-who-cares.svg`. Each has a matching shared symbol and standalone file under `static/downloads/icons/`. The gallery at `/icons-preview/#support-heading` provides individual downloads, a complete ZIP, and a visible sheet at `/downloads/hardwired-nwa-support-sheet.svg`.

The additions are native SVG contours traced from the three original generated PNGs listed below; no bitmap is embedded. `scripts/trace_support_artwork.py` records the authoring method and optional tracing dependencies. They preserve the original barbell/arrow, hand/access-card and coaching-partnership metaphors while cleaning edge noise and using the exact blue/peach palette. The PNG masters are unchanged. New `support-*` IDs keep the previous supporters and coach vectors intact. This asset expansion does not change homepage card selections, copy or destinations. All 16 prior definitions and standalone bytes passed a preservation comparison; the updated 19-entry ZIP, deterministic generation, base-path build and responsive gallery checks passed. See `docs/SVG-SPRITE.md` for details.

## Original access artwork and previous revisions

The user requested icons for the three cards in the supplied reference: Move Your Way, Scholarships Available, and A Coach Who Cares. Three new hand-drawn marker illustrations were generated in the site's blue-and-peach palette, with transparent backgrounds. They are used by the corresponding athlete, scholarship, and coach cards on Home. Each icon is decorative because its adjacent heading and text communicate the card's purpose.

## Assets

- `assets/images/motifs/access-move-your-way.png`: Move Your Way — dumbbell with an adaptable movement arrow. Copied unchanged from the built-in image tool's output.
- `assets/images/motifs/access-scholarships.svg`: current 02 / For Supporters icon — an open hand supporting a peach heart, drawn directly as vector paths.
- `assets/images/motifs/access-scholarships.png`: previous scholarship icon — an open hand supporting a gym access card. Retained unchanged from the built-in image tool's output.
- `assets/images/motifs/access-coach-cares.svg`: current A Coach Who Cares icon — two equal-sized people joined by a gently curved line, with a peach heart above them. Native vector artwork on a transparent 128 × 128 canvas.
- `assets/images/motifs/access-coach-cares.png`: previous coach icon, retained unchanged from the built-in image tool's output as a reference.

The `layouts/partials/access-icon.html` partial renders the supporters and coach symbols from `static/images/hardwired-icons.svg`; the athlete illustration remains a 224px WebP export from its PNG source. CSS displays each icon at 112px. Icons are decorative (`aria-hidden="true"`); raster images also have empty alt text. The adjacent heading and copy communicate each card's purpose. Full PNG sources are retained for reuse.

## Coach SVG expansion — October 10, 2026

The “A Coach Who Cares” reference requested a new icon for Elisabeth's coaching card. The new `access-coach-cares` symbol uses the set's blue `#2C5D75`, peach `#F9B689`, 4.6-unit rounded marker outlines, and 128 × 128 viewBox. Equal-sized head-and-shoulder figures and a connecting curve communicate partnership; the solid peach heart supplies the warm accent. The drawing does not portray Elisabeth or any specific athlete.

The homepage coach card selects this vector automatically through the existing access-icon partial. Its current copy and `/our-coach/` destination remain as implemented; the screenshot's separate link annotation was not part of the icon request. The standard generator exports the standalone icon at `/downloads/icons/access-coach-cares.svg` and includes it in the gallery and complete 16-icon ZIP.

## Supporters SVG remake — October 10, 2026

The user requested a remake of the 02 / For Supporters icon as an SVG. The redesigned symbol simplifies the previous hand/access-card concept to a blue cupped hand supporting a peach heart, with slight asymmetry and rounded marker strokes. It was authored directly as five SVG paths in a 128 × 128 viewBox, with exact site colors `#2C5D75` and `#F9B689`. There is no embedded raster image or background fill. The editable file is 993 bytes. Its web symbol is `access-scholarships` in the shared sprite; the former separate downloadable copy was removed during consolidation.

Validation: the Hugo build with the GitHub Pages base path passed, and internal links/assets resolved across ten generated HTML pages. Browser inspection and screenshots confirmed the supporters card uses the new SVG at 112px on 1440px desktop and 320px mobile layouts, with no horizontal overflow. The card still links to `/support/`. The neighboring athlete/coach cards retain their existing WebP icons. These are targeted build/render checks; the previous PNG remains available as an alternate.

## Generation record

Validation: all three source PNGs are 1254 × 1254 RGBA images, with alpha from 0 to 255 and transparent corners. All three generated 224px WebP versions retain alpha and range from 4640 to 8674 bytes. The Hugo build with the GitHub Pages base path passed, and internal links/assets resolved across ten generated HTML pages. Desktop Home was visually inspected at 1440px: all icons load in the corresponding cards at 112px, retain decorative semantics, and the original card destinations resolve. At 320px mobile width, all three icons load and the page has no horizontal overflow. These are targeted icon/render checks.

Built-in image generation mode was used, with transparent background enabled. Three independent calls produced one icon each. No CLI/API fallback was used. The final prompts follow.

### Move Your Way — dumbbell with an adaptable movement arrow

Create ONE finished transparent-background icon for the Hardwired NWA adaptive fitness website. Square canvas, one centered motif with generous transparent padding, artwork occupies about 70% of canvas. Hand-drawn felt-tip marker doodle inspired by a coach's gym whiteboard mural: confident slightly imperfect strokes, uneven curves, simple readable outline forms, gentle hand-drawn variation. Main strokes slate blue #2C5D75; one or two warm peach #F9B689 accents. Consistent medium thick rounded marker strokes, restrained two-color drawing, no heavy filled silhouettes. Friendly, energetic, respectful. Clean sharp edges, no shadows, no gradients, no paper texture, no background tile, NO white fills; genuine transparent alpha outside colored strokes AND inside open shapes. No words, lettering, numbers, labels, watermarks or logo. Readable at 80px. No border or enclosing badge. Match a set of simple blue-and-peach gym doodle icons: heart with pulse, barbell with peach grip, stopwatch with motion marks.
ICON: MOVE YOUR WAY. A simple hand-sketched horizontal dumbbell with two weight plates at either end, blue outline strokes, small peach marks on the center grip. A broad curving blue arrow arcs freely above the dumbbell from lower left toward upper right, representing an adaptable personal path of movement. One small peach spark near the arrow tip. Exactly one dumbbell and one curved arrow. Inclusive fitness symbol without assuming walking, running or standing. Compact uncluttered composition.

### Scholarships Available — an open hand supporting a gym access card

Create ONE finished transparent-background icon for the Hardwired NWA adaptive fitness website. Square canvas, one centered motif with generous transparent padding, artwork occupies about 70% of canvas. Hand-drawn felt-tip marker doodle inspired by a coach's gym whiteboard mural: confident slightly imperfect strokes, uneven curves, simple readable outline forms, gentle hand-drawn variation. Main strokes slate blue #2C5D75; one or two warm peach #F9B689 accents. Consistent medium thick rounded marker strokes, restrained two-color drawing, no heavy filled silhouettes. Friendly, energetic, respectful. Clean sharp edges, no shadows, no gradients, no paper texture, no background tile, NO white fills; genuine transparent alpha outside colored strokes AND inside open shapes. No words, lettering, numbers, labels, watermarks or logo. Readable at 80px. No border or enclosing badge. Match a set of simple blue-and-peach gym doodle icons: heart with pulse, barbell with peach grip, stopwatch with motion marks.
ICON: SCHOLARSHIPS AVAILABLE. One simple blue-outline open hand, palm up, gently supporting a small rounded rectangular gym access punch card. The card tilts slightly and has a single peach outlined heart in its center and exactly three small blue punch circles along its bottom edge. Card contains no text or monetary signs. The hand and card together communicate a gift that opens access to training. Friendly respectful support, no graduation cap, no coins, no cash, no charity stereotypes. Compact uncluttered composition.

### A Coach Who Cares — two equal-sized people connected by a heart

Create ONE finished transparent-background icon for the Hardwired NWA adaptive fitness website. Square canvas, one centered motif with generous transparent padding, artwork occupies about 70% of canvas. Hand-drawn felt-tip marker doodle inspired by a coach's gym whiteboard mural: confident slightly imperfect strokes, uneven curves, simple readable outline forms, gentle hand-drawn variation. Main strokes slate blue #2C5D75; one or two warm peach #F9B689 accents. Consistent medium thick rounded marker strokes, restrained two-color drawing, no heavy filled silhouettes. Friendly, energetic, respectful. Clean sharp edges, no shadows, no gradients, no paper texture, no background tile, NO white fills; genuine transparent alpha outside colored strokes AND inside open shapes. No words, lettering, numbers, labels, watermarks or logo. Readable at 80px. No border or enclosing badge. Match a set of simple blue-and-peach gym doodle icons: heart with pulse, barbell with peach grip, stopwatch with motion marks.
ICON: A COACH WHO CARES. Two equal-sized simple blue-outline human busts side by side, drawn as circular heads over gentle shoulder curves, with a small peach outlined heart floating between and slightly above their shoulders. A short gently curved blue connection line links the two shoulder outlines underneath the heart, showing listening and a caring partnership. Only heads and shoulders, no legs, no wheelchair, no gender markers, no facial detail. Do not depict one figure as larger, dominant, or standing over the other. Exactly two people and one heart. Compact uncluttered composition.

