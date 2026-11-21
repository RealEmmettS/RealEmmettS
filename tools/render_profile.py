"""Render the GitHub profile artwork with Python and Pillow."""

from hashlib import sha256
from io import BytesIO
from json import load
from math import cos, hypot, sin
from pathlib import Path
from urllib.request import urlopen

from PIL import Image, ImageDraw, ImageFont


ASSETS = Path(__file__).resolve().parents[1] / "assets"
CATALOG_URL = "https://cdn.shaughv.com/tree.json"
FOREST = (32, 79, 32)
CREAM = (245, 224, 197)
# Published, non-prerelease GitHub releases from June 1 through November 20, 2026.
MONTHS = ("JUN", "JUL", "AUG", "SEP", "OCT", "NOV")
RELEASES = {
    "TR-300": (2, 7, 1, 1, 0, 1),
    "ND-300": (11, 11, 0, 1, 0, 1),
    "SD-300": (0, 11, 0, 4, 0, 0),
}


def font_bytes(catalog, family, face_file):
    face = next(face for face in catalog["fonts"][family]["details"]["faces"]
                if face["file"] == face_file)
    asset = catalog["tree"]["fonts"][family]
    for part in face["file"].split("/"):
        asset = asset[part]
    with urlopen(asset["url"], timeout=20) as response:
        data = response.read()
    if sha256(data).hexdigest() != face["sha256"]:
        raise ValueError(f"CDN digest mismatch for {face_file}")
    return data


def font(data, size):
    return ImageFont.truetype(BytesIO(data), size)


def save_palette(mask, name, background=FOREST, ink=CREAM):
    image = mask.point([0] * 128 + [1] * 128).convert("P")
    image.putpalette([*background, *ink] + [0] * 762)
    image.save(ASSETS / f"{name}.png", bits=1, optimize=True)


def masthead(makira, mono, serif):
    mask = Image.new("L", (1200, 408))
    draw = ImageDraw.Draw(mask)
    metadata = font(mono, 20)
    draw.text((42, 45), "SHAUGHV  /  INDEPENDENT WORK", font=metadata, fill=255, anchor="ls")
    draw.line((42, 66, 1158, 66), fill=255, width=2)

    display = font(makira, 114)
    for baseline, line in ((183, "EMMETT"), (289, "SHAUGHNESSY")):
        draw.text((37, baseline), line, font=display, fill=255, anchor="ls")

    draw.line((42, 328, 1158, 328), fill=255, width=2)
    draw.text((41, 380), "Digital craftsman", font=font(serif, 40), fill=255, anchor="ls")

    # A sampled contour field, inspired by the CDN's dithered ambient background.
    center_x, center_y = 1017, 193
    for y in range(83, 309, 5):
        for x in range(879, 1159, 5):
            dx, dy = (x - center_x) / 134, (y - center_y) / 103
            radius = hypot(dx, dy)
            signal = cos(25 * (radius + .06 * sin(8 * dx + 4 * dy) + .10 * dx * dy))
            if radius < 1.03 and signal > -.45 + radius * .66:
                diameter = 2 + round(2 * (1 - radius))
                draw.rectangle((x, y, x + diameter, y + diameter), fill=255)
    for x in (879, 1158):
        for y in (88, 304):
            draw.line((x - 6, y, x + 6, y), fill=255, width=2)
            draw.line((x, y - 6, x, y + 6), fill=255, width=2)

    save_palette(mask, "masthead-light", CREAM, FOREST)
    save_palette(mask, "masthead-dark")


def contact_buttons(mono, theme, paper, ink):
    for slug, label, width in (("portfolio", "Portfolio", 106),
                               ("resume", "Résumé", 92),
                               ("email", "Email me", 94)):
        primary = slug == "portfolio"
        image = Image.new("RGB", (width * 3, 132), ink if primary else paper)
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, image.width - 1, 131), outline=ink, width=4)
        draw.text((image.width / 2, 67), label, font=font(mono, 42),
                  fill=paper if primary else ink, anchor="mm")
        image.save(ASSETS / f"{slug}-{theme}.png", optimize=True)


def pantry(makira, mono, serif):
    image = Image.new("RGB", (1080, 384), FOREST)
    draw = ImageDraw.Draw(image)
    label = font(mono, 26)
    draw.text((35, 22), "iOS  /  GROCERIES", font=label, fill=CREAM, anchor="lt")
    draw.line((35, 65, 1044, 65), fill=CREAM, width=2)

    # Use visible glyph bounds so the descender of the g clears the serif capitals.
    lines = (("Magic", font(makira, 90)), ("Pantry 2", font(serif, 90)))
    heights = [face.getbbox(word, anchor="lt")[3] for word, face in lines]
    gap = 5
    top = (66 + 309 - sum(heights) - gap) // 2
    for (word, face), height in zip(lines, heights):
        draw.text((35, top), word, font=face, fill=CREAM, anchor="lt")
        top += height + gap

    draw.line((35, 309, 530, 309), fill=CREAM, width=2)
    draw.text((36, 328), "VIEW ON THE APP STORE", font=label, fill=CREAM, anchor="lt")
    draw.line([(474, 341), (513, 341), (500, 328)], fill=CREAM, width=3)
    draw.line([(513, 341), (500, 354)], fill=CREAM, width=3)

    draw.rounded_rectangle((562, 29, 1042, 416), radius=34, fill=FOREST, outline=CREAM, width=3)
    with Image.open(Path(__file__).with_name("pantry-screen.png")) as screen:
        mask = Image.new("L", screen.size)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, screen.width - 1, screen.height + 40),
                                                radius=27, fill=255)
        image.paste(screen, (569, 36), mask)
    image.save(ASSETS / "magic-pantry.png", optimize=True)


def release_chart(makira, mono, theme, paper, ink):
    image = Image.new("RGB", (1080, 372), paper)
    draw = ImageDraw.Draw(image)
    draw.text((35, 30), "Qube TX", font=font(makira, 61), fill=ink, anchor="lt")
    draw.text((1040, 45), "RELEASE HISTORY", font=font(mono, 27), fill=ink, anchor="rt")
    draw.line((36, 103, 1044, 103), fill=ink, width=2)
    columns = [202 + index * (949 - 202) / len(MONTHS) for index in range(len(MONTHS))]
    for month, x in zip(MONTHS, columns):
        draw.text((x, 122), month, font=font(mono, 23), fill=ink, anchor="lt")
        for y in range(159, 321, 10):
            draw.point((int(x), y), fill=ink)

    for row, (tool, counts) in enumerate(RELEASES.items()):
        y = 186 + 63 * row
        draw.text((36, y), tool, font=font(mono, 30), fill=ink, anchor="lm")
        draw.text((1040, y), str(sum(counts)), font=font(makira, 40), fill=ink, anchor="rm")
        for x, count in zip(columns, counts):
            for square in range(count):
                left = x + (square % 7) * 16
                top = y - 6 + (square // 7) * 16
                draw.rectangle((left, top, left + 11, top + 11), fill=ink)
    draw.line((36, 342, 1044, 342), fill=ink, width=2)
    image.save(ASSETS / f"releases-{theme}.png", optimize=True)


def type_specimen(makira, mono, serif, theme, paper, ink):
    image = Image.new("RGB", (1080, 310), paper)
    draw = ImageDraw.Draw(image)
    rows = (("SANS", "Makira", makira, "Aa"),
            ("MONO", "Geist Mono", mono, "01"),
            ("SERIF", "Geist Serif", serif, "&"))
    for row, (label, name, face, glyph) in enumerate(rows):
        y = 19 + 99 * row
        draw.text((35, y + 21), label, font=font(mono, 22), fill=ink, anchor="lt")
        draw.text((184, y), name, font=font(face, 66), fill=ink, anchor="lt")
        draw.text((1044, y + 12), glyph, font=font(face, 58), fill=ink, anchor="rt")
        if row < len(rows) - 1:
            draw.line((35, y + 81, 1045, y + 81), fill=ink, width=2)
    image.save(ASSETS / f"type-{theme}.png", optimize=True)


def main():
    ASSETS.mkdir(exist_ok=True)
    with urlopen(CATALOG_URL, timeout=20) as response:
        catalog = load(response)
    makira = font_bytes(catalog, "makira", "otf/Makira-Black.otf")
    mono = font_bytes(catalog, "geist-mono", "otf/GeistMono-Regular.otf")
    serif = font_bytes(catalog, "geist-serif", "ttf/GeistSerif-Regular.ttf")
    masthead(makira, mono, serif)
    pantry(makira, mono, serif)
    for theme, paper, ink in (("light", CREAM, FOREST), ("dark", FOREST, CREAM)):
        contact_buttons(mono, theme, paper, ink)
        release_chart(makira, mono, theme, paper, ink)
        type_specimen(makira, mono, serif, theme, paper, ink)


if __name__ == "__main__":
    main()
