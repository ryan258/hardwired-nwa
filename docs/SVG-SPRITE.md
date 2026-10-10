# Shared SVG symbol sprite

`static/images/hardwired-icons.svg` is the single web file for all 14 icon symbols. Hugo pages and the artwork previews use external `<use>` references to that file. The editable originals remain in `assets/images/physical-skills-icons.svg` and `assets/images/motifs/*.svg`. The badge logo is a separate image asset, and the athlete/coach illustrations remain raster images.

## Symbol IDs

| Set | IDs | ViewBox |
| --- | --- | --- |
| Physical skills | `skill-cardio`, `skill-stamina`, `skill-strength`, `skill-flexibility`, `skill-power`, `skill-speed`, `skill-coordination`, `skill-agility`, `skill-balance`, `skill-accuracy` | `0 0 24 24` |
| Supporters | `access-scholarships` | `0 0 128 128` |
| Commitments | `commitment-safety`, `commitment-efficacy`, `commitment-efficiency` | `0 0 128 128` |

## Regeneration and optimization

Run after editing the source artwork, before building or previewing:

```sh
python3 scripts/build_svg_sprite.py
```

The generator uses Python's standard library. It removes comments, preview-only metadata and formatting whitespace; hoists shared stroke/fill attributes within individual symbols; and writes compact XML. It preserves path geometry, colors and viewBoxes. The sprite is 5,492 bytes, or 1,404 bytes when measured with gzip compression. The gzip figure is an asset measurement, not a claim about hosting configuration.

The previous duplicate static skills files, inline skills partial, standalone supporters/commitment web downloads, and commitment-only sprite were removed. Icon definitions are no longer repeated in every Hugo page. Home requests one shared sprite for its eleven vector icon instances.

A symbol-only sprite does not display an atlas when opened as an ordinary image. Render selected symbols with `<use>`; the commitments preview includes a visible three-icon sheet.

## Template usage

```html
<svg width="112" height="112" viewBox="0 0 128 128" aria-hidden="true" focusable="false">
  <use href="{{ "images/hardwired-icons.svg" | relURL }}#commitment-efficacy"></use>
</svg>
<span>Efficacy</span>
```

For physical skills, use `viewBox="0 0 24 24"` and set the SVG's CSS `color` to the desired stroke color. Keep descriptive labels in HTML. Icons without an equivalent nearby label need their own accessible name. Hugo's `relURL` preserves the GitHub Pages project subpath. Static preview pages use relative paths to the same sprite.

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
