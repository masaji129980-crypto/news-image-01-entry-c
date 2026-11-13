#!/usr/bin/env python3
"""Draw 'Chips Fall, Talks Rise' — 13 November 2026 world news in one image.
Entirely code-drawn with Pillow: simple iconic shapes + short text labels.
Left: Nvidia chip crash. Right: Dublin peace talks. 1024x1024 PNG."""
from PIL import Image, ImageDraw, ImageFont
import math

W = H = 1024
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def f(size, bold=False):
    return ImageFont.truetype(FONTB if bold else FONT, size)

img = Image.new("RGB", (W, H), (18, 22, 34))
d = ImageDraw.Draw(img)

# ---- top banner ----
d.rectangle([0, 0, W, 92], fill=(10, 12, 20))
d.text((512, 46), "13 NOVEMBER 2026", font=f(40, True), fill=(255, 255, 255), anchor="mm")
d.rectangle([0, 92, W, 98], fill=(255, 200, 40))

# ---- divider ----
d.rectangle([508, 98, 516, H], fill=(255, 255, 255))

# ================= LEFT: CHIPS FALL =================
d.rectangle([0, 98, 508, H], fill=(28, 16, 22))
d.text((254, 150), "CHIPS FALL", font=f(52, True), fill=(255, 84, 84), anchor="mm")
d.text((254, 205), "NVIDIA  -14%", font=f(34, True), fill=(255, 255, 255), anchor="mm")
d.text((254, 245), "Huang resigns", font=f(26), fill=(255, 190, 190), anchor="mm")
d.text((254, 278), "Wall Street falls", font=f(26), fill=(255, 190, 190), anchor="mm")

# microchip icon
cx, cy = 254, 430
d.rounded_rectangle([cx-95, cy-75, cx+95, cy+75], radius=18, fill=(60, 60, 90), outline=(150, 180, 255), width=4)
d.rounded_rectangle([cx-55, cy-45, cx+55, cy+45], radius=10, fill=(30, 160, 90))
d.text((cx, cy), "NVDA", font=f(34, True), fill=(255, 255, 255), anchor="mm")
for i in range(-2, 3):
    x = cx + i * 38
    d.line([(x, cy-75), (x, cy-105)], fill=(150, 180, 255), width=6)
    d.line([(x, cy+75), (x, cy+105)], fill=(150, 180, 255), width=6)
    y = cy + i * 30
    d.line([(cx-95, y), (cx-125, y)], fill=(150, 180, 255), width=6)
    d.line([(cx+95, y), (cx+125, y)], fill=(150, 180, 255), width=6)

# falling red chart
chart = [(40, 620), (110, 640), (170, 630), (230, 690), (290, 730), (350, 720), (410, 800), (470, 870)]
d.rectangle([30, 600, 480, 900], fill=(40, 22, 30), outline=(120, 40, 50), width=2)
for x in range(60, 480, 40):
    d.line([(x, 610), (x, 890)], fill=(70, 35, 45), width=1)
d.line(chart, fill=(255, 60, 60), width=8, joint="curve")
for (x, y) in chart:
    d.ellipse([x-7, y-7, x+7, y+7], fill=(255, 60, 60))
d.polygon([(455, 855), (478, 875), (450, 892)], fill=(255, 60, 60))
d.text((255, 930), "shares plunge", font=f(26), fill=(255, 120, 120), anchor="mm")
d.text((255, 968), "amid scandal", font=f(26), fill=(255, 120, 120), anchor="mm")

# ================= RIGHT: TALKS RISE =================
d.rectangle([516, 98, W, H], fill=(16, 44, 60))
d.text((770, 150), "TALKS RISE", font=f(52, True), fill=(90, 220, 160), anchor="mm")
d.text((770, 205), "Dublin peace talks", font=f(30, True), fill=(255, 255, 255), anchor="mm")
d.text((770, 245), "US envoys meet Zelensky", font=f(26), fill=(190, 235, 210), anchor="mm")
d.text((770, 278), "Europe backs talks", font=f(26), fill=(190, 235, 210), anchor="mm")

# stylised map (Europe-ish blob) with a Dublin marker
d.ellipse([560, 330, 980, 560], fill=(24, 90, 70), outline=(120, 220, 180), width=3)
d.polygon([(600, 420), (660, 380), (740, 400), (800, 370), (880, 400), (920, 450), (860, 500), (760, 520), (660, 500), (600, 470)], fill=(46, 140, 100))
d.ellipse([640, 380, 672, 412], fill=(255, 220, 60), outline=(255, 255, 255), width=3)
d.text((700, 396), "DUBLIN", font=f(28, True), fill=(255, 255, 255), anchor="lm")

# peace dove (simple white bird shape)
bx, by = 770, 640
d.ellipse([bx-90, by-30, bx+90, by+30], fill=(255, 255, 255))          # body
d.ellipse([bx+55, by-55, bx+115, by+5], fill=(255, 255, 255))          # head
d.polygon([(bx+100, by-45), (bx+130, by-35), (bx+100, by-25)], fill=(255, 180, 40))  # beak
d.ellipse([bx+78, by-42, bx+92, by-28], fill=(20, 20, 20))            # eye
d.polygon([(bx-60, by-25), (bx-20, by-110), (bx+30, by-35)], fill=(240, 240, 240), outline=(200, 200, 200))  # raised wing
d.polygon([(bx-85, by-5), (bx-150, by-35), (bx-145, by+5), (bx-90, by+15)], fill=(230, 230, 230))  # tail
# olive branch
d.line([(bx+95, by-30), (bx+150, by-15)], fill=(60, 160, 80), width=5)
d.ellipse([bx+130, by-28, bx+150, by-8], fill=(60, 180, 90))
d.ellipse([bx+145, by-18, bx+165, by+2], fill=(60, 180, 90))

# handshake (two clasped hands, simplified)
hx, hy = 770, 800
d.rounded_rectangle([hx-170, hy-45, hx+170, hy+45], radius=22, fill=(245, 220, 190), outline=(180, 140, 100), width=3)
d.line([(hx-60, hy-45), (hx-60, hy+45)], fill=(180, 140, 100), width=3)
d.line([(hx, hy-45), (hx, hy+45)], fill=(180, 140, 100), width=3)
d.line([(hx+60, hy-45), (hx+60, hy+45)], fill=(180, 140, 100), width=3)
d.polygon([(hx-170, hy-45), (hx-110, hy-45), (hx-140, hy+45), (hx-170, hy+45)], fill=(200, 160, 120))
d.polygon([(hx+170, hy-45), (hx+110, hy-45), (hx+140, hy+45), (hx+170, hy+45)], fill=(220, 180, 140))
d.text((770, 890), "handshake for peace", font=f(26), fill=(190, 235, 210), anchor="mm")
d.text((770, 968), "hope rises", font=f(26, True), fill=(90, 220, 160), anchor="mm")

# ---- bottom strip ----
d.rectangle([0, 990, W, H], fill=(10, 12, 20))
d.text((512, 1007), "ONE DAY  •  TWO STORIES", font=f(20), fill=(200, 200, 200), anchor="mm")

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png")
