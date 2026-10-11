#!/usr/bin/env python3
"""Rebuild vector skill artwork from the original illustrated PNG sheet.

Optional authoring tool: requires Pillow 12.3 and VTracer 0.6.15.
The normal sprite/export builder only uses Python's standard library.
The source PNG is read without modification.
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
NAMES = (
    "cardio", "stamina", "strength", "flexibility", "power",
    "speed", "coordination", "agility", "balance", "accuracy",
)


def tag(name):
    return f"{{{NS}}}{name}"


source = Image.open(ROOT / "static/images/motifs/physical-skills-sprite.png").convert("RGBA")
sprite = ET.Element(tag("svg"))
for index, name in enumerate(NAMES):
    column, row = index % 5, index // 5
    cell = source.crop((
        round(column * source.width / 5), round(row * source.height / 2),
        round((column + 1) * source.width / 5), round((row + 1) * source.height / 2),
    ))
    # Classify the two illustration colors, excluding low-alpha edge noise.
    # This gives the SVG exact brand colors without changing the PNG master.
    pixels = []
    for red, green, blue, alpha in cell.get_flattened_data():
        if alpha < 180:
            pixels.append((0, 0, 0, 0))
        elif red < 120 and blue > green and blue > 60:
            pixels.append(BLUE)
        elif red > 180 and 100 < green < 215 and blue < 180:
            pixels.append(PEACH)
        else:
            pixels.append((0, 0, 0, 0))
    cell.putdata(pixels)
    bounds = cell.getbbox()
    if bounds is None:
        raise ValueError(f"No illustration found for {name}")
    cell = cell.crop(bounds)
    buffer = BytesIO()
    cell.save(buffer, format="PNG")
    vector = vtracer.convert_raw_image_to_svg(
        buffer.getvalue(), img_format="png", colormode="color",
        hierarchical="cutout", mode="spline", filter_speckle=12,
        color_precision=8, layer_difference=1, corner_threshold=75,
        length_threshold=8, max_iterations=10, splice_threshold=45,
        path_precision=1,
    )
    traced = ET.fromstring(vector)
    scale = 100 / max(cell.size)
    x = 64 - cell.width * scale / 2
    y = 64 - cell.height * scale / 2
    symbol = ET.SubElement(sprite, tag("symbol"), {
        "id": f"skill-{name}", "viewBox": "0 0 128 128",
    })
    group = ET.SubElement(symbol, tag("g"), {
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
    print(f"{name}: {len(group)} vector paths")

ET.indent(sprite, space="  ")
output = ROOT / "assets/images/physical-skills-icons.svg"
output.write_text(ET.tostring(sprite, encoding="unicode") + "\n")
print(f"Saved ten vector illustrations to {output.relative_to(ROOT)}.")
