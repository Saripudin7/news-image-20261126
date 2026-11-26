"""Render the 26 November 2026 world-news infographic (1024x1024 PNG).

Drawn entirely with Pillow primitives: no image files, no network.
Deterministic: fixed layout, fixed fonts, no timestamps, no randomness.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (247, 243, 234)
NAVY = (20, 33, 61)
NAVY_LIGHT = (31, 48, 84)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
MUTED = (96, 96, 96)
CARD = (255, 255, 255)
CARD_LINE = (214, 206, 190)
FOOTER_BG = (20, 33, 61)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF = FONT_DIR + "DejaVuSerif-Bold.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"
SANS_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_icon(draw, kind, cx, cy, r, color):
    """Small pictogram drawn from primitives, centred at (cx, cy)."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    w = (255, 255, 255)
    if kind == "tariff":
        # three rising bars with a % sign feel
        base = cy + r - 12
        for i, h in enumerate((14, 22, 30)):
            x0 = cx - 22 + i * 15
            draw.rectangle([x0, base - h, x0 + 10, base], fill=w)
        draw.line([cx - 26, base - 34, cx + 26, base - 34], fill=w, width=3)
    elif kind == "rate":
        # rising line chart with arrowhead
        pts = [(cx - 24, cy + 16), (cx - 8, cy + 2), (cx + 6, cy + 8), (cx + 24, cy - 16)]
        draw.line(pts, fill=w, width=4, joint="curve")
        draw.polygon([(cx + 24, cy - 16), (cx + 12, cy - 16), (cx + 24, cy - 4)], fill=w)
    elif kind == "space":
        # ringed planet
        draw.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=w)
        draw.ellipse([cx - 26, cy - 6, cx + 26, cy + 6], outline=w, width=3)
        draw.ellipse([cx + 18, cy - 26, cx + 22, cy - 22], fill=w)
    elif kind == "drone":
        # warning triangle with exclamation
        draw.polygon([(cx, cy - 24), (cx + 24, cy + 18), (cx - 24, cy + 18)], fill=w)
        draw.rectangle([cx - 2, cy - 12, cx + 2, cy + 6], fill=color)
        draw.ellipse([cx - 3, cy + 11, cx + 3, cy + 17], fill=color)
    elif kind == "pin":
        # location pin
        draw.ellipse([cx - 15, cy - 22, cx + 15, cy + 8], fill=w)
        draw.polygon([(cx - 15, cy + 2), (cx + 15, cy + 2), (cx, cy + 26)], fill=w)
        draw.ellipse([cx - 6, cy - 13, cx + 6, cy - 1], fill=color)
    elif kind == "balloon":
        # parade balloon with string
        draw.ellipse([cx - 16, cy - 24, cx + 16, cy + 4], fill=w)
        draw.polygon([(cx - 6, cy + 4), (cx + 6, cy + 4), (cx, cy + 12)], fill=w)
        draw.line([cx, cy + 12, cx + 4, cy + 26], fill=w, width=3)


STORIES = [
    {
        "num": "1",
        "tag": "TRADE  ·  USA",
        "color": (176, 58, 48),
        "icon": "tariff",
        "headline": "US proposes sweeping new tariffs on 14 partners",
        "body": "Washington targets China, Japan and the EU over excess factory capacity, in its biggest tariff move since the midterms.",
        "date": "Proposed 25 Nov · lead story 26 Nov",
        "source": "Reuters, AP",
    },
    {
        "num": "2",
        "tag": "ECONOMY  ·  SOUTH KOREA",
        "color": (34, 112, 74),
        "icon": "rate",
        "headline": "Bank of Korea lifts its rate to 3.25%",
        "body": "Seoul resumes tightening after an October pause, as a chip-led export boom keeps growth brisk and inflation above target.",
        "date": "26 Nov",
        "source": "Reuters",
    },
    {
        "num": "3",
        "tag": "SPACE  ·  CHINA",
        "color": (43, 72, 150),
        "icon": "space",
        "headline": "First Pakistani astronaut reaches Tiangong",
        "body": "Shenzhou-24 docks with China's space station carrying Muhammad Zeeshan Ali, the first foreign visitor to Tiangong.",
        "date": "Launched & docked 25 Nov",
        "source": "Reuters, NASA Spaceflight",
    },
    {
        "num": "4",
        "tag": "CONFLICT  ·  SUDAN",
        "color": (146, 74, 28),
        "icon": "drone",
        "headline": "RSF drone strikes kill 19 civilians in Blue Nile",
        "body": "Drones hit three neighbourhoods in Damazin and struck a dam and power sites in Roseires, a rights group says.",
        "date": "Strikes 24 Nov · reported 25 Nov",
        "source": "Reuters",
    },
    {
        "num": "5",
        "tag": "MIDDLE EAST  ·  GAZA",
        "color": (112, 48, 96),
        "icon": "pin",
        "headline": "Two Hamas security chiefs killed in 24 hours",
        "body": "Israeli strikes kill Mohammad Abuelouf and his family in Gaza City, a day after the group's security chief died.",
        "date": "25 Nov",
        "source": "Reuters, BBC",
    },
    {
        "num": "6",
        "tag": "CULTURE  ·  USA",
        "color": (178, 128, 20),
        "icon": "balloon",
        "headline": "Macy's Thanksgiving parade postponed — a first",
        "body": "Storm winds push the 100th-anniversary parade in New York from Thursday to Saturday, organisers say.",
        "date": "Announced 25 Nov · parade day 26 Nov",
        "source": "AP",
    },
]

TICKER = (
    "ALSO TODAY  —  Malaysia sues Google for $146m over YouTube content  •  "
    "North Korea expels Swiss envoy  •  Bangladesh raises garment wage 36%  •  "
    "S&P puts Nvidia on downgrade watch  •  SHEIN pays $100m FTC fine"
)


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    f_mast = font(SERIF, 54)
    f_date = font(SANS_BOLD, 26)
    f_sub = font(SANS, 19)
    f_tag = font(SANS_BOLD, 15)
    f_head = font(SANS_BOLD, 23)
    f_body = font(SANS, 17)
    f_meta = font(SANS, 14)
    f_tick = font(SANS_BOLD, 16)
    f_src = font(SANS, 14)

    # ---- header band ----
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 152], fill=GOLD)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_mast)
    d.text(((W - tw) / 2, 14), title, font=f_mast, fill=(255, 255, 255))
    date = "THURSDAY  26  NOVEMBER  2026"
    dw = d.textlength(date, font=f_date)
    d.text(((W - dw) / 2, 82), date, font=f_date, fill=GOLD)
    sub = "Six stories that defined the day — as reported on 26 November 2026"
    sw = d.textlength(sub, font=f_sub)
    d.text(((W - sw) / 2, 116), sub, font=f_sub, fill=(205, 210, 224))

    # ---- story grid: 2 cols x 3 rows ----
    gx, gy = 16, 168
    pw, ph = 488, 240
    gap = 16
    for i, s in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = gx + col * (pw + gap)
        y0 = gy + row * (ph + gap)
        x1, y1 = x0 + pw, y0 + ph
        color = s["color"]

        d.rectangle([x0, y0, x1, y1], fill=CARD, outline=CARD_LINE, width=2)
        d.rectangle([x0, y0, x1, y0 + 7], fill=color)

        # number badge + icon
        d.ellipse([x0 + 16, y0 + 22, x0 + 52, y0 + 58], fill=color)
        num = s["num"]
        nw = d.textlength(num, font=f_tag)
        d.text((x0 + 34 - nw / 2, y0 + 30), num, font=f_tag, fill=(255, 255, 255))
        draw_icon(d, s["icon"], x0 + 86, y0 + 40, 26, color)

        # tag line
        d.text((x0 + 128, y0 + 28), s["tag"], font=f_tag, fill=color)

        # headline (max 2 lines)
        hl = wrap(d, s["headline"], f_head, pw - 32)
        hy = y0 + 76
        for line in hl[:2]:
            d.text((x0 + 16, hy), line, font=f_head, fill=INK)
            hy += 28

        # body (max 3 lines)
        bl = wrap(d, s["body"], f_body, pw - 32)
        by = hy + 6
        for line in bl[:3]:
            d.text((x0 + 16, by), line, font=f_body, fill=(52, 52, 52))
            by += 23

        # date + source at card bottom
        d.line([x0 + 16, y1 - 34, x1 - 16, y1 - 34], fill=CARD_LINE, width=1)
        d.text((x0 + 16, y1 - 26), s["date"], font=f_meta, fill=MUTED)
        src = "Source: " + s["source"]
        swd = d.textlength(src, font=f_meta)
        d.text((x1 - 16 - swd, y1 - 26), src, font=f_meta, fill=MUTED)

    # ---- footer: ticker + sources ----
    fy = gy + 3 * ph + 2 * gap + 8  # 936
    d.rectangle([0, fy, W, H], fill=FOOTER_BG)
    tl = wrap(d, TICKER, f_tick, W - 32)
    ty = fy + 12
    for line in tl:
        d.text((16, ty), line, font=f_tick, fill=(255, 255, 255))
        ty += 22
    src_line = ("Sources: Reuters, AP, Yonhap, Bloomberg.  Events happened or were first "
                "reported on 26 Nov 2026, or late 25 Nov UTC (26 Nov in Asia).")
    sl = wrap(d, src_line, f_src, W - 32)
    sy = ty + 6
    for line in sl:
        d.text((16, sy), line, font=f_src, fill=(170, 178, 196))
        sy += 18

    return img


if __name__ == "__main__":
    render().save("entry.png")
