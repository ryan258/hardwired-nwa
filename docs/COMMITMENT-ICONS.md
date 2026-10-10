# Our Commitments SVG icons

The user clarified the SVG expansion with an “Our Commitments” reference containing Safety, Efficacy, and Efficiency. This set supplies those three icons. The reference's “need new copy” annotations are not treated as approved organization statements; the artwork preview uses only the supplied labels and descriptions of the symbols.

## Canonical assets

| Label | Artwork | Editable SVG source |
| --- | --- | --- |
| Safety | Shield with a check | `assets/images/motifs/commitment-safety.svg` |
| Efficacy | Target with an arrow | `assets/images/motifs/commitment-efficacy.svg` |
| Efficiency | Circular arrow with a lightning bolt | `assets/images/motifs/commitment-efficiency.svg` |

All three are authored directly as SVG vector geometry, with no raster image or background fill. Each uses a 128 × 128 viewBox, blue `#2C5D75` outlines at 4.6 units and peach `#F9B689` accents at 5 units. Safety and efficiency retain the gently asymmetric marker style. Efficacy was revised to two concentric circular arcs centered at (64, 66), with radii 43 and 25 and matching gaps for the arrow. The arrow ends at the shared center without crossing either ring. Editable SVGs retain their titles and descriptions.

## Shared sprite and preview

- `static/images/hardwired-icons.svg`: the single optimized web sprite for all 14 icon symbols. Commitment IDs are `commitment-safety`, `commitment-efficacy`, and `commitment-efficiency`.
- `/commitments-preview/`: responsive artwork review page displaying the three commitments from that shared file, plus examples at 32, 64, and 112px. Its download link supplies the complete sprite.

The previous standalone web downloads and separate commitment sprite have been removed. Editable SVG sources remain in `assets/images/motifs/`.

Regenerate the shared sprite after editing source artwork:

```sh
python3 scripts/build_svg_sprite.py
```

The preview is a standalone design review page. It adds no organization commitments or training claims to the site's main pages.

## Template use

Display the shared sprite through `<use>`, rather than an image element. With equivalent text nearby, mark the SVG decorative:

```html
<svg width="112" height="112" viewBox="0 0 128 128" aria-hidden="true">
  <use href="{{ "images/hardwired-icons.svg" | relURL }}#commitment-safety"></use>
</svg>
<span>Safety</span>
```

Keep the visible text label in HTML. If there is no nearby equivalent label, give the icon an accessible name instead of hiding it. Use light backgrounds to retain the blue-and-peach appearance.

## Verification

Current consolidation and rendering checks are recorded in `docs/SVG-SPRITE.md`. The preview remains a design review surface; the main site has not been given new commitments copy.
