# Hand-drawn physical skill motifs

The user requested a sprite sheet representing all ten skills in their mural photograph. The supplied spelling “strenght” is interpreted as “strength.” The artwork is a new illustration inspired by the reference, not a reproduction of the mural photograph.

## Files and use

- `assets/images/physical-skills-icons.svg`: SVG symbol sprite containing all ten vector skill motifs (`#skill-cardio` through `#skill-accuracy`), styled with `stroke="currentColor"`.
- `static/images/physical-skills-icons.svg`: static copy for direct web referencing.
- `static/downloads/physical-skills-icons.svg`: downloadable vector asset for stakeholders and designers.
- `layouts/partials/svg-skills-sprite.html`: Hugo partial embedding the vector symbol sprite into `baseof.html` for universal, subpath-safe `<use href="#skill-...">` usage.
- `layouts/partials/training-wall.html`: site component integrating all ten physical skills cards into the mural training wall on Home and Adaptive CrossFit pages.
- `static/images/motifs/physical-skills-sprite.png`: transparent PNG, 1983 × 793 pixels, raster sprite sheet.
- `static/images/motifs/physical-skills.css`: classes for selecting each raster cell with CSS background positioning.
- `static/motifs-preview/index.html`: labeled responsive preview, reachable at `/motifs-preview/` under the site's base path.

Five columns and two rows, read left to right. Row one: cardio, stamina, strength, flexibility, power. Row two: speed, coordination, agility, balance, accuracy. The generated dimensions produce nominal cells of 396.6 × 396.5 pixels. CSS preserves that ratio, uses `background-size: 500% 200%`, and positions columns at 0%, 25%, 50%, 75%, and 100%, with rows at 0% and 100%.

| Skill | Motif | CSS class suffix |
| --- | --- | --- |
| Cardio | Heart with heartbeat | cardio |
| Stamina | Battery with infinity loop | stamina |
| Strength | Loaded barbell | strength |
| Flexibility | Bending resistance band with arc | flexibility |
| Power | Kettlebell with burst marks | power |
| Speed | Stopwatch with motion lines | speed |
| Coordination | Three balls linked by arrows | coordination |
| Agility | Cones with zigzag route | agility |
| Balance | Centered wobble board | balance |
| Accuracy | Target with arrow | accuracy |

The requested palette is slate blue `#2C5D75` and peach `#F9B689`. Generated artwork may include slight color variation and antialiased edges. Use the motifs on light surfaces; the blue strokes lose contrast on a blue surface. No skill name is baked into the image. Labels remain HTML text. The drawings are symbolic and do not assume an athlete can walk, run, or stand.

```html
<!-- Resolve this stylesheet through Hugo's relURL when used in a template. -->
<link rel="stylesheet" href="{{ "images/motifs/physical-skills.css" | relURL }}">
<span class="skill-motif skill-motif--strength"
      style="--motif-size: 96px" aria-hidden="true"></span>
<span>Strength</span>
```

When the motif communicates information without nearby equivalent text, give it `role="img"` and an appropriate `aria-label` instead of `aria-hidden`. These are static illustrations; no animation is included. The set is packaged for site use and preview, without changing the main site pages.

## Generation record

Validation: the saved sheet is byte-identical to the generated RGBA PNG. Alpha ranges from 0 to 255, corners are transparent, and all ten cells contain visible artwork. The labeled preview was visually inspected at 1440px; each CSS class selects the intended motif. At 320px mobile width, all ten motifs remain present, the sprite sheet loads, and there is no horizontal overflow. The background selector updates its visual state and `aria-pressed` values. The Hugo build using the GitHub Pages base path passed; internal links/assets resolved across ten generated HTML pages. These are targeted asset/preview checks, not a full accessibility audit.

Mode: built-in image generation tool, transparent background enabled. One new illustration generated; no paid API/CLI fallback. Source output: `exec-a63371a0-2715-446a-843d-9071ffe74cb9.png`. The final sheet is an unchanged copy of that output. The requested ideal dimensions were 2500 × 1000; the tool returned 1983 × 793. CSS uses the returned dimensions.

### Final prompt

+Create a finished transparent PNG sprite sheet of TEN DISTINCT hand-drawn fitness skill motifs for the Hardwired NWA adaptive fitness website. Mural-inspired felt-tip marker doodles: confident slightly imperfect strokes, gently uneven curves, casual gym whiteboard sketches, simple readable silhouettes, never polished generic stock icons. Color palette: main thick strokes slate blue #2C5D75, small warm peach #F9B689 accents. No black, no white fills, no grey paper. True transparent alpha background everywhere outside the colored marks. Minimal two-color art. No shadows, no realistic surfaces.
MANDATORY ATLAS GEOMETRY: wide landscape canvas at exactly a 5:2 aspect ratio, ideally 2500x1000 pixels. FIVE equal square columns by TWO equal square rows; every cell same size, each motif centered in its own cell. Each motif fits within the central 65% of its cell, generous completely transparent equal padding on all sides. NO lines dividing cells. NO background panels. NO text, letters, labels, numbers, legends, captions or watermarks anywhere. Exactly one motif per cell, no spill across cell boundaries. Even visual weight and stroke thickness throughout; recognizable at 64px.
MANDATORY POSITIONS, left to right:
TOP ROW:
1 CARDIO: simple outlined heart with a small heartbeat zigzag drawn across it; tiny peach pulse accent.
2 STAMINA: simple battery outline containing a continuous infinity loop, two tiny peach endurance ticks; endurance rather than sprinting.
3 STRENGTH: hand-sketched horizontal loaded barbell, two plates at each end, small peach grip mark.
4 FLEXIBILITY: supple curving resistance band making one broad bending S curve, a small curved peach arrow indicating range of motion; no human silhouette required.
5 POWER: kettlebell with three bold radiating peach burst marks above it, explosive force.
BOTTOM ROW:
6 SPEED: simple stopwatch with three horizontal motion streaks to its left, small peach clock hand.
7 COORDINATION: three small circular balls connected by looping orbital arrows, one ball peach, two blue; coordinated movement, no atom nucleus.
8 AGILITY: three small training cones with one clear peach zigzag route threading between them, change of direction.
9 BALANCE: a horizontal wobble board on a small curved fulcrum, centered and stable, small peach level indicator above, no person.
10 ACCURACY: hand-drawn concentric target with a single arrow hitting the peach center from upper right.
The whole collection should feel drawn by one coach on the gym wall, friendly and energetic, suited to an inclusive adaptive fitness community. Symbols must work without assuming athletes walk, run or stand. Do not add the logo or any text. Transparent PNG sprite sheet, clean edges, sharp large-resolution line art.
