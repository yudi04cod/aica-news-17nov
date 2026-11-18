"""Draw the 17 November 2026 world-news front page (1024x1024 PNG).

Flat vector-style newspaper page: masthead + six story panels, each with a
simple drawn scene (flat shapes only) and a short factual headline.
Written by hand for the make.fun news-image-20261117 competition.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def scene_bridge(d, x, y, w, h):
    sky = (176, 216, 240)
    d.rectangle([x, y, x + w, y + h], fill=sky)
    d.rectangle([x, y + h * 0.62, x + w, y + h], fill=(38, 110, 160))
    # bridge deck, left span intact, right span collapsed into the sea
    d.rectangle([x + 10, y + 58, x + w * 0.55, y + 74], fill=(60, 60, 66))
    d.polygon([(x + w * 0.55, y + 58), (x + w * 0.72, y + 96),
               (x + w * 0.78, y + 96), (x + w * 0.62, y + 58)],
              fill=(60, 60, 66))
    d.rectangle([x + w * 0.80, y + 58, x + w - 10, y + 74], fill=(60, 60, 66))
    for px in (x + 40, x + w * 0.30, x + w * 0.88):
        d.rectangle([px, y + 20, px + 8, y + 58], fill=(60, 60, 66))
    # explosion burst where the span broke
    cx, cy = x + w * 0.66, y + 52
    for r, c in ((34, (255, 140, 0)), (22, (255, 200, 40)), (12, (255, 240, 120))):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    d.rectangle([x + w * 0.60, y + 96, x + w * 0.70, y + 100], fill=(200, 200, 200))


def scene_tanker(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 214, 150))
    d.rectangle([x, y + h * 0.66, x + w, y + h], fill=(24, 90, 130))
    # tanker hull
    d.polygon([(x + 30, y + 78), (x + w - 30, y + 78), (x + w - 55, y + 108),
               (x + 55, y + 108)], fill=(150, 30, 25))
    d.rectangle([x + 70, y + 52, x + 150, y + 78], fill=(200, 200, 200))
    d.rectangle([x + 165, y + 58, x + 175, y + 78], fill=(60, 60, 60))
    # fire + smoke
    cx, cy = x + w * 0.72, y + 58
    for r, c in ((30, (255, 120, 0)), (19, (255, 190, 30)), (10, (255, 240, 130))):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    for sx, sy, sr in ((x + w * 0.72, y + 22, 16), (x + w * 0.80, y + 12, 12)):
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(90, 90, 90))
    # second distant tanker
    d.rectangle([x + w - 120, y + 92, x + w - 20, y + 102], fill=(120, 30, 25))


def scene_flags(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(150, 195, 235))
    d.rectangle([x, y + h * 0.78, x + w, y + h], fill=(90, 140, 90))
    # US flag
    fx, fy, fw, fh = x + 30, y + 18, 170, 90
    for i in range(7):
        d.rectangle([fx, fy + i * fh // 7, fx + fw, fy + (i + 1) * fh // 7],
                    fill=(178, 34, 52) if i % 2 == 0 else (255, 255, 255))
    d.rectangle([fx, fy, fx + fw * 0.4, fy + fh * 0.55], fill=(30, 50, 110))
    d.rectangle([fx, fy + fh, fx + 6, y + h - 4], fill=(70, 70, 70))
    # Philippine flag
    px, py = x + w - 210, y + 18
    d.polygon([(px, py), (px + 170, py), (px, py + 90)], fill=(255, 255, 255))
    d.polygon([(px, py), (px + 170, py), (px + 170, py + 45), (px, py + 45)],
              fill=(0, 56, 168))
    d.polygon([(px, py + 45), (px + 170, py + 45), (px + 170, py + 90),
               (px, py + 90)], fill=(206, 17, 38))
    d.rectangle([px, py + 90, px + 6, y + h - 4], fill=(70, 70, 70))
    # sun
    d.ellipse([x + w // 2 - 14, y + 14, x + w // 2 + 14, y + 42], fill=(255, 200, 40))


def scene_bank(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(210, 225, 235))
    # bank building
    d.rectangle([x + 30, y + 30, x + 190, y + 118], fill=(240, 240, 235))
    d.polygon([(x + 20, y + 30), (x + 110, y + 6), (x + 200, y + 30)],
              fill=(30, 60, 110))
    for cx in (x + 50, x + 90, x + 130, x + 170):
        d.rectangle([cx, y + 42, cx + 12, y + 100], fill=(30, 60, 110))
    d.rectangle([x + 30, y + 100, x + 190, y + 118], fill=(30, 60, 110))
    # phone with error
    d.rounded_rectangle([x + w - 130, y + 12, x + w - 30, y + 118],
                        radius=12, fill=(20, 20, 25))
    d.rectangle([x + w - 118, y + 26, x + w - 42, y + 96], fill=(255, 255, 255))
    d.line([x + w - 108, y + 40, x + w - 52, y + 82], fill=(200, 0, 0), width=10)
    d.line([x + w - 52, y + 40, x + w - 108, y + 82], fill=(200, 0, 0), width=10)


def scene_rocket(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(18, 24, 60))
    for sx, sy in ((x + 40, y + 20), (x + w - 50, y + 30), (x + 90, y + 60),
                   (x + w - 90, y + 70), (x + w // 2, y + 14)):
        d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 255, 255))
    # rocket body, tilted and breaking apart
    cx, cy = x + w // 2, y + 52
    d.polygon([(cx - 16, cy - 26), (cx + 16, cy - 26), (cx + 10, cy + 30),
               (cx - 10, cy + 30)], fill=(240, 240, 240))
    d.polygon([(cx - 16, cy - 26), (cx + 16, cy - 26), (cx, cy - 52)],
              fill=(230, 60, 40))
    d.polygon([(cx - 26, cy + 30), (cx - 10, cy + 30), (cx - 14, cy + 52)],
              fill=(230, 60, 40))
    # explosion + falling satellites
    for r, c in ((18, (255, 140, 0)), (11, (255, 210, 60))):
        d.ellipse([cx - r, cy + 42 - r, cx + r, cy + 42 + r], fill=c)
    for sx, sy in ((x + 60, y + 96), (x + w - 70, y + 100), (x + w - 130, y + 86)):
        d.rectangle([sx - 10, sy - 4, sx + 10, sy + 4], fill=(180, 200, 230))
        d.rectangle([sx - 4, sy - 10, sx + 4, sy + 10], fill=(180, 200, 230))


def scene_border(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 220, 200))
    d.rectangle([x, y + h * 0.72, x + w, y + h], fill=(120, 140, 100))
    # fence posts and wire
    for px in range(x + 16, x + w - 8, 44):
        d.rectangle([px, y + 22, px + 8, y + 100], fill=(70, 70, 70))
    for wy in (y + 30, y + 52, y + 74, y + 94):
        d.line([x + 10, wy, x + w - 10, wy], fill=(70, 70, 70), width=4)
    for bx in range(x + 24, x + w - 10, 30):
        d.line([bx, y + 30, bx + 14, y + 52], fill=(70, 70, 70), width=3)
    # Estonian flag colours on a sign
    d.rectangle([x + w // 2 - 90, y + 88, x + w // 2 + 90, y + 112],
                fill=(255, 255, 255), outline=(0, 0, 0), width=3)
    d.rectangle([x + w // 2 - 84, y + 92, x + w // 2 + 84, y + 99],
                fill=(0, 114, 206))
    d.rectangle([x + w // 2 - 84, y + 99, x + w // 2 + 84, y + 105],
                fill=(0, 0, 0))
    d.rectangle([x + w // 2 - 84, y + 105, x + w // 2 + 84, y + 108],
                fill=(255, 255, 255))


PANELS = [
    ("UKRAINE STRIKES KERCH BRIDGE",
     "A road span to Crimea collapses; Russia hits Kyiv's Dnipro bridges.",
     scene_bridge),
    ("TANKERS HIT BY MINES NEAR HORMUZ",
     "Tankers strike mines and catch fire; USS Theodore Roosevelt arrives.",
     scene_tanker),
    ("TRUMP IN MANILA",
     "Trump arrives for the ASEAN summit; Xi-Trump-Putin meet Thursday.",
     scene_flags),
    ("JPMORGAN OUTAGE",
     "A software bug — not a cyberattack — hits online banking and Zelle.",
     scene_bank),
    ("VULCAN ROCKET FAILS",
     "A ULA Vulcan rocket fails in flight, destroying 40 Amazon Leo satellites.",
     scene_rocket),
    ("ESTONIA TO SHUT RUSSIA BORDER",
     "Estonia closes all Russia border crossings from 1 December.",
     scene_border),
]


def main():
    img = Image.new("RGB", (W, H), (247, 243, 232))
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([6, 6, W - 7, H - 7], outline=(20, 20, 30), width=4)

    # ---- masthead ----
    d.rectangle([14, 14, W - 15, 196], fill=(18, 28, 58))
    title = font(SERIF, 44)
    d.text((W // 2, 52), "THE WORLD IN ONE PICTURE", font=title,
           fill=(247, 243, 232), anchor="ma")
    d.rectangle([W // 2 - 330, 92, W // 2 + 330, 94], fill=(200, 160, 60))
    date = font(BOLD, 52)
    d.text((W // 2, 138), "TUESDAY 17 NOVEMBER 2026", font=date,
           fill=(255, 205, 70), anchor="ma")
    sub = font(REG, 22)
    d.text((W // 2, 208), "Six stories that defined the day — from Kyiv to Hormuz, "
           "Manila to the Atlantic", font=sub, fill=(40, 40, 40), anchor="ma")

    # ---- story grid: 2 columns x 3 rows ----
    gx, gy = 22, 234
    pw, ph = 480, 246
    gapx, gapy = 20, 10
    hf = font(BOLD, 30)
    bf = font(REG, 20)
    for i, (headline, body, scene) in enumerate(PANELS):
        col, row = i % 2, i // 2
        x = gx + col * (pw + gapx)
        y = gy + row * (ph + gapy)
        d.rectangle([x, y, x + pw, y + ph], fill=(255, 255, 255),
                    outline=(20, 20, 30), width=2)
        scene(d, x + 2, y + 2, pw - 4, 112)
        d.line([x, y + 114, x + pw, y + 114], fill=(200, 160, 60), width=3)
        lines = wrap(d, headline, hf, pw - 24)
        ty = y + 124
        for ln in lines[:2]:
            d.text((x + 12, ty), ln, font=hf, fill=(15, 15, 20))
            ty += 32
        blines = wrap(d, body, bf, pw - 24)
        ty = y + 124 + 32 * len(lines[:2]) + 4
        for ln in blines[:2]:
            d.text((x + 12, ty), ln, font=bf, fill=(50, 50, 55))
            ty += 24

    # (no footer line: the grid ends just above the frame)
    img.save("entry.png", optimize=True)


if __name__ == "__main__":
    main()
