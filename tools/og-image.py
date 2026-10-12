"""Draw docs/og-image.png (1200x630), the picture link previews show. Run it again if the name or text changes.

    python tools/og-image.py

Needs Pillow. Uses Segoe UI from C:/Windows/Fonts, falling back to Pillow's default font.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

NAME = "Mjønes Consulting"
LINE = "Software development and IT consulting"
ORGNR = "Org. no. 937 553 196, Norway"

BG = "#09090b"
SURFACE = "#18181b"
LINE_COLOUR = "#3f3f46"
TEXT = "#f4f4f5"
MUTED = "#a1a1aa"
ACCENT = "#7dd3fc"

FONTS = Path("C:/Windows/Fonts")


def font(name: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype(str(FONTS / name), size)
    except OSError:
        return ImageFont.load_default(size)


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "docs" / "og-image.png"
    img = Image.new("RGB", (1200, 630), BG)
    draw = ImageDraw.Draw(img)

    # The monogram, as in favicon.svg, scaled from its 32-unit box to 128 px
    x0, y0, s = 96, 112, 4
    draw.rounded_rectangle((x0, y0, x0 + 32 * s, y0 + 32 * s), radius=7 * s, fill=SURFACE, outline=LINE_COLOUR, width=2)
    points = [(9, 22), (9, 10), (16, 18), (23, 10), (23, 22)]
    draw.line([(x0 + px * s, y0 + py * s) for px, py in points], fill=ACCENT, width=10, joint="curve")
    for px, py in (points[0], points[-1]):
        cx, cy = x0 + px * s, y0 + py * s
        draw.ellipse((cx - 5, cy - 5, cx + 5, cy + 5), fill=ACCENT)

    draw.text((96, 300), NAME, font=font("segoeuib.ttf", 84), fill=TEXT)
    draw.text((96, 410), LINE, font=font("segoeui.ttf", 40), fill=MUTED)
    draw.text((96, 490), ORGNR, font=font("segoeui.ttf", 32), fill=MUTED)

    img.save(out, optimize=True)
    print(out)


if __name__ == "__main__":
    main()
