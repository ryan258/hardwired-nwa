# Shared SVG symbol sprite

`static/images/hardwired-icons.svg` is the single web file for all 24 icon symbols. Hugo pages and the artwork previews use external `<use>` references to that file. The editable originals remain in `assets/images/physical-skills-icons.svg` and `assets/images/motifs/*.svg`. The badge logo is a separate image asset, and the homepage athlete access illustration remains a raster image.

## Symbol IDs

| Set | IDs | ViewBox |
| --- | --- | --- |
| Physical skills | `skill-cardio`, `skill-stamina`, `skill-strength`, `skill-flexibility`, `skill-power`, `skill-speed`, `skill-coordination`, `skill-agility`, `skill-balance`, `skill-accuracy` | `0 0 128 128` |
| Adaptive equipment | `adaptive-equipment` | `0 0 128 128` |
| Supporters | `access-scholarships` | `0 0 128 128` |
| Coach | `access-coach-cares` | `0 0 128 128` |
| Commitments | `commitment-safety`, `commitment-efficacy`, `commitment-efficiency` | `0 0 128 128` |
| Additional Access to Support illustrations | `support-move-your-way`, `support-scholarships-available`, `support-coach-who-cares` | `0 0 128 128` |
| Strength, Community and Opportunity | `commitment-strength`, `commitment-community`, `commitment-opportunity` | `0 0 128 128` |
| Donation options | `donation-online`, `donation-check` | `0 0 128 128` |

## Regeneration and optimization

Run after editing the source artwork, before building or previewing:

```sh
python3 scripts/build_svg_sprite.py
```

The generator uses Python's standard library. It removes comments, preview-only metadata and formatting whitespace; hoists shared stroke/fill attributes within individual symbols; and writes compact XML. It preserves path geometry, colors and viewBoxes. The sprite is 83,915 bytes, or 30,410 bytes when measured with gzip compression. The gzip figure is an asset measurement, not a claim about hosting configuration.

The previous duplicate static skills files, inline skills partial, standalone supporters/commitment web downloads, and commitment-only sprite were removed. Icon definitions are no longer repeated in every Hugo page. Home requests one shared sprite for its twelve vector icon instances.

A symbol-only sprite does not display an atlas when opened as an ordinary image. Render selected symbols with `<use>`; the commitments preview includes a visible three-icon sheet.

## Template usage

```html
<svg width="112" height="112" viewBox="0 0 128 128" aria-hidden="true" focusable="false">
  <use href="{{ "images/hardwired-icons.svg" | relURL }}#commitment-efficacy"></use>
</svg>
<span>Efficacy</span>
```

All symbols now use `viewBox="0 0 128 128"`. The physical skills use blue and peach vector outlines traced from the original illustration sheet. Keep descriptive labels in HTML. Icons without an equivalent nearby label need their own accessible name. Hugo's `relURL` preserves the GitHub Pages project subpath. Static preview pages use relative paths to the same sprite.

To add a symbol, add its editable source and update the generator's input list and expected symbol count. Do not hand-edit the generated sprite.

## Efficacy target revision

Both rings now use circular arcs with a shared center (64, 66), radii 43 and 25, and matching gaps along the arrow's approach. The peach arrow ends at that shared center. This replaces the uneven freehand rings that appeared misaligned in the supplied screenshot.

## Targeted verification — October 10, 2026

- Regeneration is byte-for-byte deterministic; all 14 symbol IDs are unique, with no embedded raster images.
- The Hugo build using the GitHub Pages project base path passed; internal links/assets resolved across eleven generated HTML pages.
- All 30 generated external `<use>` references resolve to files and existing SVG symbol IDs.
- Desktop browser inspection confirmed all ten physical skill icons on Home and the corrected efficacy target on the commitments preview. All fourteen icon types had nonzero rendered bounds across those two pages.
- Home recorded one shared sprite resource request for its eleven vector instances.
- Home and the commitments preview rendered their symbols at 320px width without horizontal overflow. The commitments preview also renders instances at 32, 64 and 112px.
- `git diff --check` passed. These are targeted asset/build/browser checks, not a full accessibility audit or deployment verification.

## Adaptive Equipment addition — October 10, 2026

Added `adaptive-equipment` from `assets/images/motifs/adaptive-equipment.svg`: a resistance handle with an adjustable strap, peach buckle and padded grip. It shares the 128 × 128 viewBox, rounded marker strokes and exact blue/peach palette. The sprite now contains 15 symbols. All 14 previous symbol definitions remain unchanged, and regeneration is deterministic.

The base-path Hugo build and eleven-page link check passed. Browser checks confirmed the new external symbol renders at 32, 64, 112px and the main preview size. The preview has no horizontal overflow at 1440px or 320px. The artwork can be reviewed at `/commitments-preview/#equipment-heading`; no donation or equipment inventory claims were added to the main site.

## Standalone SVG exports

The same generator also produces one visible, self-contained SVG per symbol in `static/downloads/icons/`, a ZIP at `static/downloads/hardwired-nwa-icons.zip`, and a gallery at `/icons-preview/` with individual download links. Every file has a title, transparent background, explicit blue `currentColor` fallback, and vector geometry expanded directly into the SVG root. No external sprite is required to open or reuse these files. The shared sprite remains the main site's icon source.

Verification: all 15 exports parse as SVGs with viewBoxes and no external `<use>` or embedded raster image; ZIP entries match the individual files exactly and its integrity check passed. Regeneration of the sprite and ZIP is deterministic. The base-path Hugo build and twelve-page link check passed. Browser checks confirmed all 15 standalone images load at 1440px and 320px, with no horizontal overflow.

## Two-color skill icons — October 10, 2026

The ten vector skill icons previously had only inherited blue strokes. Peach accents now appear in every skill: cardio pulse, stamina bars, strength grip, flexibility arrow, power bolt fill, speed hands, coordination ring, agility route, balance fulcrum and accuracy bullseye. Source geometry and symbol IDs are preserved, except for the added barbell grip accent. The shared sprite, 15 standalone exports and ZIP were regenerated together. All ten source/export skill symbols contain both blue and peach. ZIP contents match the exported files; the base-path build and twelve-page link check passed. All 15 standalone images load in the browser, with no desktop or 320px mobile overflow.

## Hand-drawn skills redesign — October 10, 2026

The recolored 24-unit stock-style geometry was superseded by ten native vector drawings on the same 128-unit canvas as the commitments. Blue outlines use 4.6-unit strokes, peach accents use 5 units, all caps and joins are rounded, and the artwork has no filled background.

Metaphors: heart/pulse, battery/infinity, sketched barbell, bending resistance band, kettlebell/burst, stopwatch/motion, three linked points, cones/route, wobble board, target/arrow. Accuracy intentionally shares the approved target motif with Efficacy. Existing symbol IDs remain stable. The main site's viewBoxes were migrated together, and its icon display is now 64px with no colored disc behind the artwork. The download gallery shows five columns on desktop for the two skill rows.

Validation: all 15 symbols have a 128-unit viewBox and both exact palette colors. The approved commitments/supporters symbols are unchanged. ZIP files match the standalone SVGs, and regeneration is deterministic. All fifteen images load in the gallery; all ten revised symbols render on Home. Both surfaces were checked at desktop and 320px without horizontal overflow. The project-base-path Hugo build and twelve-page link check passed.

## Original illustration standard — October 10, 2026

The user confirmed that the original illustrated skill sheet should set the visual bar. The latest ten skill symbols are traced directly from that sheet, replacing the thin geometric redraw. They preserve the band handles, weight plates, cone bases, clock details, motion marks, and fuller peach accents. The colors are normalized to the site palette, small edge noise is excluded, and curves are simplified. The PNG master remains unchanged. VTracer uses color/cutout/spline mode, speckle filter 12, precision 8, layer difference 1, corner threshold 75, length threshold 8, ten iterations, splice threshold 45, and path precision 1. Filled vector contours preserve the illustration's stroke appearance; no bitmap is embedded.

All icon IDs remain stable on a 128-unit canvas. The shared sprite, standalone files, ZIP, and gallery are regenerated together. `static/downloads/hardwired-nwa-skills-sheet.svg` adds a visible, labeled five-by-two review sheet with internal symbols. Its labels use a system font. The existing commitments, supporters, and equipment vectors retain their artwork. Future icon additions should use the original illustration sheet as their style reference.

Verification of the original-derived vectors: the original PNG is byte-identical to its committed copy. Trace and export regeneration are deterministic; all 15 symbols have a 128-unit viewBox and only the exact two artwork colors. Standalone exports contain no external symbol references or embedded images. ZIP contents match all 15 exports and pass integrity checks. The visible skills sheet contains ten valid internal references. The project-base-path build and twelve-page link check passed; desktop and 320px checks confirmed the gallery images and all ten Home symbols render with no horizontal overflow.

## A Coach Who Cares addition — October 10, 2026

Added `access-coach-cares` from `assets/images/motifs/access-coach-cares.svg` for the requested coach-card icon. The native SVG shows two equal-sized people, a connecting blue curve, and a solid peach heart. It follows the set's 128-unit canvas, rounded marker outlines, exact palette, and transparent background. The retained coach PNG is now a reference; the homepage selects the new vector through the existing access-icon partial.

Targeted checks used a temporary copy of the current working tree: both root and GitHub Pages subpath builds and twelve-page link checks passed. All 15 previous symbol definitions were preserved; the set now contains 16 unique symbols. The 16 ZIP entries match their standalone SVGs and pass integrity checks, and all 20 generated outputs reproduce exactly. Browser checks at 320px confirmed the homepage coach symbol renders at 112px, remains decorative, and retains its existing `/our-coach/` link; all 16 gallery images load without horizontal overflow. These are local asset/build/browser checks, not deployment or organization acceptance.

## Three additional support illustrations — October 10, 2026

The user requested three additions while preserving all 16 existing vectors. The new `support-*` sources trace the original blue-and-peach access PNG illustrations using `scripts/trace_support_artwork.py` (optional Pillow 12.3 and VTracer 0.6.15 authoring dependencies). The normal sprite/export build still uses only Python's standard library. Colors are normalized to `#2C5D75` and `#F9B689`, low-alpha edge noise is excluded, and spline contours preserve the fuller illustrated strokes. All three are centered on a transparent 128-unit canvas with artwork occupying 100 units along its longest dimension.

- `support-move-your-way`: a barbell with a rising arrow, peach grip marks and a motion burst.
- `support-scholarships-available`: a hand supporting an access card with a peach heart and three visit marks.
- `support-coach-who-cares`: two equal-sized people joined beneath a peach outline heart.

These are additional assets with distinct IDs. Existing `access-scholarships`, `access-coach-cares`, skill, commitment and equipment symbols retain their exact definitions. The homepage card selections, copy and destinations are unchanged. The reference's link annotations were not part of the icon addition request.

The generator now exports 19 standalone files and a 19-icon ZIP. `/icons-preview/` shows the additions together before the original collection. `/downloads/hardwired-nwa-support-sheet.svg` is a visible, self-contained three-icon review sheet with internal symbols and system-font labels.

Targeted verification: all 16 original symbol definitions, standalone file bytes, editable vector sources, PNG masters and the existing skills sheet are unchanged. All three new standalone SVGs contain both exact palette colors, valid titles and viewBoxes, and no embedded raster images, external references or background rectangles. All 19 ZIP entries match their standalone files and pass integrity checks. Tracing and export regeneration reproduce identical outputs. The GitHub Pages subpath Hugo build and twelve-page link/asset check passed. All 19 gallery images load in the browser with no horizontal overflow on the desktop preview or at 320 CSS pixels. The Git index is preserved. These checks cover local assets and rendering.

## Strength, Community and Opportunity — October 10, 2026

The latest reference requests three more icons for Our Commitments. The additions are authored directly as editable SVG paths in `assets/images/motifs/commitment-strength.svg`, `commitment-community.svg` and `commitment-opportunity.svg`. Rounded marker strokes, slight curve variation, blue `#2C5D75` outlines and peach `#F9B689` accents carry forward the established illustration style. Each drawing is centered on the 128-unit canvas, with a longest geometry extent of 100 units before stroke thickness.

- Strength: a tilted loaded barbell, peach grip marks and a star for personal goals.
- Community: three people connected by a shared curve and a peach heart.
- Opportunity: an open doorway, an unobstructed peach path and light marks.

The new IDs are `commitment-strength`, `commitment-community` and `commitment-opportunity`. All 19 earlier vectors, their standalone files and the skills/support review sheets remain unchanged. The new drawings are included in the shared sprite and 22-icon ZIP; `/icons-preview/#values-heading` shows them first. `/downloads/hardwired-nwa-commitments-sheet.svg` is the visible, self-contained review sheet. The site copy and homepage icon selections are unchanged by this asset addition.

Targeted checks: all prior source/file hashes and symbol definitions match the starting state. All three additions have valid titles, 128-unit viewBoxes, both exact palette colors and no embedded raster image, external reference or background rectangle. All 22 ZIP entries match their standalone SVGs and pass integrity checks. Export regeneration is deterministic. The GitHub Pages subpath Hugo build and twelve-page link/asset check passed. Browser inspection confirmed the new sheet's three symbols have visible bounds, and all 22 gallery images load at 1440 and 320 CSS pixels without horizontal overflow. The existing Git index is preserved. These checks cover local assets and rendering.

## Donate Online and Donate by Check — October 10, 2026

The latest reference adds two donation-card icons. `donation-online` shows a rounded browser window with a peach heart, header dots and a blue cursor. The frame has a deliberate gap beside the cursor to keep their outlines distinct. `donation-check` shows a paper check, peach signature, small heart and pen. Both are authored directly as editable native SVG paths, with blue `#2C5D75` and peach `#F9B689`, rounded marker strokes, transparent backgrounds and centered 100-unit artwork extents on 128-unit canvases.

Editable sources are `assets/images/motifs/donation-online.svg` and `donation-check.svg`. Their standalone exports appear under `static/downloads/icons/`; the shared sprite and complete ZIP now contain 24 icons. The two additions appear first at `/icons-preview/#donation-heading`. `/downloads/hardwired-nwa-donations-sheet.svg` is a visible, self-contained 480 × 240 review sheet. The sheet helper now supports any group length, while the three existing review sheets reproduce exactly.

Verification: all 22 prior source vectors, symbol definitions, standalone files and review sheets remain unchanged. The favicon assets and existing Git index are also preserved. The new exports have valid titles and 128-unit viewBoxes, use both exact palette colors, and contain no embedded images, external references or background shapes. All 24 ZIP entries match their standalone files and pass integrity checks. Regeneration is deterministic. The GitHub Pages subpath Hugo build and thirteen-page link/asset check passed; all 24 gallery images load at 1440 and 320 CSS pixels without horizontal overflow. These are local asset/build/render checks. The supplied card text is reference context for the artwork; this addition does not configure a payment destination or mailing address.
