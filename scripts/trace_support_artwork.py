#!/usr/bin/env python3
"""Trace the original access illustrations into three additional SVG sources.

Optional authoring tool: requires Pillow 12.3 and VTracer 0.6.15.
The standard-library sprite builder consumes the saved SVGs without these tools.
Existing PNG masters and the original sixteen vectors are never written here.
"""
from io import BytesIO
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image
import vtracer

ROOT = Path(__file__).resolve().parent.parent
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
BLUE = (44, 93, 117, 255)
PEACH = (249, 182, 137, 255)
ICONS = (
    ("support-move-your-way", "access-move-your-way", "Move Your Way",
     "A sketched barbell with a rising arrow and peach grip and motion accents."),
    ("support-scholarships-available", "access-scholarships", "Scholarships Available",
     "An open hand supports a gym access card with a peach heart and three visit marks."),
    ("support-coach-who-cares", "access-coach-cares", "A Coach Who Cares",
     "Two equal-sized people are linked by a curved line beneath a peach heart."),
)


def tag(name):
    return f"{{{NS}}}{name}"


for name, source_name, label, description in ICONS:
    artwork = Image.open(ROOT / f"assets/images/motifs/{source_name}.png").convert("RGBA")
    pixels = []
    for red, green, blue, alpha in artwork.get_flattened_data():
        if alpha < 180:
            pixels.append((0, 0, 0, 0))
        elif red < 120 and blue > green and blue > 60:
            pixels.append(BLUE)
        elif red > 180 and 100 < green < 215 and blue < 180:
            pixels.append(PEACH)
        else:
            pixels.append((0, 0, 0, 0))
    artwork.putdata(pixels)
    bounds = artwork.getbbox()
    if bounds is None:
        raise ValueError(f"No illustration found for {name}")
    artwork = artwork.crop(bounds)
    buffer = BytesIO()
    artwork.save(buffer, format="PNG")
    traced = ET.fromstring(vtracer.convert_raw_image_to_svg(
        buffer.getvalue(), img_format="png", colormode="color",
        hierarchical="cutout", mode="spline", filter_speckle=12,
        color_precision=8, layer_difference=1, corner_threshold=75,
        length_threshold=8, max_iterations=10, splice_threshold=45,
        path_precision=1,
    ))
    scale = 100 / max(artwork.size)
    x = 64 - artwork.width * scale / 2
    y = 64 - artwork.height * scale / 2
    svg = ET.Element(tag("svg"), {
        "viewBox": "0 0 128 128", "width": "128", "height": "128",
        "role": "img", "aria-labelledby": f"{name}-title {name}-description",
    })
    ET.SubElement(svg, tag("title"), {"id": f"{name}-title"}).text = label
    ET.SubElement(svg, tag("desc"), {"id": f"{name}-description"}).text = description
    group = ET.SubElement(svg, tag("g"), {
        "transform": f"translate({x:.3f} {y:.3f}) scale({scale:.5f})",
    })
    for shape in traced:
        if shape.tag != tag("path"):
            continue
        color = shape.get("fill", "").upper()
        if color not in ("#2C5D75", "#F9B689"):
            raise ValueError(f"Unexpected trace color for {name}: {color}")
        shape.set("fill", color)
        group.append(shape)
    ET.indent(svg, space="  ")
    output = ROOT / f"assets/images/motifs/{name}.svg"
    output.write_text(ET.tostring(svg, encoding="unicode") + "\n")
    print(f"{name}: {len(group)} paths, {output.stat().st_size} bytes")
