"""
Generates high-fidelity sample leaf images representing typical Uzbek crop pathology.
"""
import os
import math
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SAMPLES_DIR = Path(__file__).resolve().parent / "samples"
SAMPLES_DIR.mkdir(parents=True, exist_ok=True)


def generate_cotton_bacterial_blight() -> Image.Image:
    """Creates a synthetic cotton leaf with angular, water-soaked brown lesions."""
    w, h = 800, 800
    # Background: dry sandy/loam soil
    soil = np.random.randint(140, 180, (h, w, 3), dtype=np.uint8)
    soil[:, :, 0] += 25  # warm brown tint
    soil[:, :, 2] -= 15
    img = Image.fromarray(soil).filter(ImageFilter.GaussianBlur(3))
    draw = ImageDraw.Draw(img)

    # 3-lobed cotton leaf outline
    leaf_pts = [
        (400, 720), (380, 600), (280, 560), (180, 480), (150, 360),
        (230, 320), (280, 260), (350, 220), (400, 100), (450, 220),
        (520, 260), (570, 320), (650, 360), (620, 480), (520, 560),
        (420, 600), (400, 720)
    ]
    draw.polygon(leaf_pts, fill=(54, 115, 45), outline=(35, 80, 28))

    # Leaf veins
    vein_color = (80, 155, 60)
    draw.line([(400, 680), (400, 110)], fill=vein_color, width=4)
    draw.line([(400, 500), (230, 320)], fill=vein_color, width=3)
    draw.line([(400, 500), (570, 320)], fill=vein_color, width=3)
    draw.line([(400, 350), (280, 260)], fill=vein_color, width=2)
    draw.line([(400, 350), (520, 260)], fill=vein_color, width=2)

    # Angular Bacterial Blight lesions (angular dark brown spots bounded by veins)
    lesions = [
        [(360, 320), (390, 310), (385, 340), (355, 350)],
        [(420, 280), (450, 270), (445, 305), (415, 310)],
        [(410, 380), (440, 370), (435, 410), (405, 415)],
        [(320, 390), (350, 380), (345, 420), (315, 425)],
        [(460, 340), (490, 335), (480, 370), (455, 375)],
        [(290, 340), (320, 330), (315, 365), (285, 370)],
        [(380, 220), (410, 210), (405, 250), (375, 255)]
    ]
    for poly in lesions:
        # Greasy halo
        halo = [(x + np.random.randint(-4, 4), y + np.random.randint(-4, 4)) for x, y in poly]
        draw.polygon(halo, fill=(150, 140, 30))
        draw.polygon(poly, fill=(75, 30, 18), outline=(45, 18, 10))

    return img


def generate_grape_powdery_mildew() -> Image.Image:
    """Creates a synthetic grape leaf with white-gray powdery patches (Oidium)."""
    w, h = 800, 800
    # Vineyard background (greenish shadow)
    bg = np.full((h, w, 3), (90, 110, 75), dtype=np.uint8)
    img = Image.fromarray(bg)
    draw = ImageDraw.Draw(img)

    # Palmate 5-lobed grape leaf
    pts = [
        (400, 700), (370, 620), (250, 600), (180, 500), (160, 380),
        (230, 340), (220, 220), (320, 220), (350, 140), (400, 110),
        (450, 140), (480, 220), (580, 220), (570, 340), (640, 380),
        (620, 500), (550, 600), (430, 620), (400, 700)
    ]
    draw.polygon(pts, fill=(62, 130, 50), outline=(40, 95, 30))

    # Palmate main veins radiating from petiole
    vein_color = (95, 165, 75)
    for target in [(400, 110), (220, 220), (580, 220), (160, 380), (640, 380)]:
        draw.line([(400, 670), target], fill=vein_color, width=4)

    # White powdery mildew patches (soft blurred white/ash-gray circles)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    o_draw = ImageDraw.Draw(overlay)
    patches = [
        (380, 260, 60), (460, 310, 75), (320, 340, 50), (400, 420, 90),
        (490, 430, 55), (270, 420, 65), (370, 510, 70)
    ]
    for px, py, r in patches:
        # Yellow chlorotic ring beneath mycelium
        o_draw.ellipse([px - r - 15, py - r - 15, px + r + 15, py + r + 15], fill=(210, 200, 70, 110))
        # Powdery white center
        o_draw.ellipse([px - r, py - r, px + r, py + r], fill=(235, 240, 245, 210))

    overlay = overlay.filter(ImageFilter.GaussianBlur(12))
    img.paste(overlay, (0, 0), overlay)
    return img


def generate_cotton_verticillium_wilt() -> Image.Image:
    """Creates a synthetic cotton leaf exhibiting tiger-stripe interveinal chlorosis."""
    w, h = 800, 800
    bg = np.full((h, w, 3), (165, 150, 125), dtype=np.uint8)
    img = Image.fromarray(bg)
    draw = ImageDraw.Draw(img)

    leaf_pts = [
        (400, 720), (380, 600), (280, 560), (180, 480), (150, 360),
        (230, 320), (280, 260), (350, 220), (400, 100), (450, 220),
        (520, 260), (570, 320), (650, 360), (620, 480), (520, 560),
        (420, 600), (400, 720)
    ]
    draw.polygon(leaf_pts, fill=(70, 125, 50), outline=(45, 90, 30))

    # Tiger stripe interveinal necrosis bands
    stripes = [
        [(340, 240), (380, 260), (370, 300), (310, 270)],
        [(460, 240), (420, 260), (430, 300), (490, 270)],
        [(250, 350), (330, 360), (320, 410), (230, 390)],
        [(550, 350), (470, 360), (480, 410), (570, 390)],
        [(300, 450), (380, 460), (360, 510), (280, 490)],
        [(500, 450), (420, 460), (440, 510), (520, 490)]
    ]
    for s in stripes:
        # Yellow chlorosis border
        draw.polygon(s, fill=(205, 175, 40))
        # Necrotic brown center
        center = [(int(x * 0.95 + 400 * 0.05), int(y * 0.95 + 400 * 0.05)) for x, y in s]
        draw.polygon(center, fill=(105, 50, 20))

    # Veins stay greenish
    vein_color = (60, 140, 45)
    draw.line([(400, 680), (400, 110)], fill=vein_color, width=4)
    draw.line([(400, 500), (230, 320)], fill=vein_color, width=3)
    draw.line([(400, 500), (570, 320)], fill=vein_color, width=3)

    return img


def generate_grape_saline_scorch() -> Image.Image:
    """Creates a synthetic grape leaf showing marginal perimeter scorch from salinity/heat."""
    w, h = 800, 800
    bg = np.full((h, w, 3), (170, 160, 135), dtype=np.uint8)
    img = Image.fromarray(bg)
    draw = ImageDraw.Draw(img)

    # Base grape leaf points
    pts = [
        (400, 700), (370, 620), (250, 600), (180, 500), (160, 380),
        (230, 340), (220, 220), (320, 220), (350, 140), (400, 110),
        (450, 140), (480, 220), (580, 220), (570, 340), (640, 380),
        (620, 500), (550, 600), (430, 620), (400, 700)
    ]
    # Outer scorched perimeter
    draw.polygon(pts, fill=(90, 45, 20), outline=(60, 30, 12))

    # Yellow transition zone
    inner_pts_yellow = [
        (int(x * 0.92 + 400 * 0.08), int(y * 0.92 + 400 * 0.08)) for x, y in pts
    ]
    draw.polygon(inner_pts_yellow, fill=(200, 185, 45))

    # Healthy green center
    inner_pts_green = [
        (int(x * 0.84 + 400 * 0.16), int(y * 0.84 + 400 * 0.16)) for x, y in pts
    ]
    draw.polygon(inner_pts_green, fill=(65, 135, 52))

    # Main veins
    vein_color = (95, 170, 75)
    for target in [(400, 150), (250, 250), (550, 250), (200, 390), (600, 390)]:
        draw.line([(400, 650), target], fill=vein_color, width=3)

    return img


def generate_tomato_late_blight() -> Image.Image:
    """Creates a synthetic tomato leaf with spreading dark Phytophthora water-soaked spots."""
    w, h = 800, 800
    # Rich garden soil background
    soil = np.random.randint(70, 110, (h, w, 3), dtype=np.uint8)
    soil[:, :, 0] += 30
    soil[:, :, 1] += 15
    img = Image.fromarray(soil).filter(ImageFilter.GaussianBlur(3))
    draw = ImageDraw.Draw(img)

    # Serrated compound tomato leaf leaflet
    pts = [
        (400, 700), (370, 580), (330, 520), (260, 480), (290, 420),
        (220, 370), (270, 310), (320, 260), (360, 210), (400, 110),
        (440, 210), (480, 260), (530, 310), (580, 370), (510, 420),
        (540, 480), (470, 520), (430, 580), (400, 700)
    ]
    draw.polygon(pts, fill=(45, 120, 40), outline=(25, 75, 22))

    # Leaf veins
    vein_color = (70, 150, 55)
    draw.line([(400, 680), (400, 120)], fill=vein_color, width=4)
    draw.line([(400, 500), (260, 480)], fill=vein_color, width=3)
    draw.line([(400, 500), (540, 480)], fill=vein_color, width=3)
    draw.line([(400, 380), (270, 310)], fill=vein_color, width=2)
    draw.line([(400, 380), (530, 310)], fill=vein_color, width=2)

    # Late blight dark water-soaked spreading lesions
    blight_spots = [
        (330, 420, 65),
        (440, 350, 55),
        (380, 240, 45),
        (470, 460, 50),
        (280, 360, 40)
    ]
    for cx, cy, r in blight_spots:
        # Translucent pale water halo
        draw.ellipse([cx - r - 8, cy - r - 8, cx + r + 8, cy + r + 8], fill=(130, 145, 60))
        # Dark necrotic center
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(42, 28, 20), outline=(25, 15, 10))
        # White fuzzy sporulation fringe
        draw.arc([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], start=45, end=220, fill=(225, 230, 220), width=3)

    return img


def generate_apple_scab() -> Image.Image:
    """Creates an apple leaf with velvety dark olive-green to black parsha scab spots."""
    w, h = 800, 800
    orchard_bg = np.random.randint(90, 130, (h, w, 3), dtype=np.uint8)
    orchard_bg[:, :, 1] += 20
    img = Image.fromarray(orchard_bg).filter(ImageFilter.GaussianBlur(3))
    draw = ImageDraw.Draw(img)

    # Oval serrated apple leaf
    pts = [
        (400, 710), (350, 610), (290, 500), (260, 380), (290, 260),
        (340, 180), (400, 110), (460, 180), (510, 260), (540, 380),
        (510, 500), (450, 610), (400, 710)
    ]
    draw.polygon(pts, fill=(50, 130, 45), outline=(30, 80, 25))

    # Midrib and lateral veins
    draw.line([(400, 690), (400, 120)], fill=(80, 160, 60), width=4)
    for y in range(220, 600, 70):
        draw.line([(400, y), (300, y - 40)], fill=(75, 155, 55), width=2)
        draw.line([(400, y), (500, y - 40)], fill=(75, 155, 55), width=2)

    # Velvety olive/dark scabs (parsha)
    scabs = [
        (360, 320, 35), (430, 410, 42), (340, 460, 30),
        (450, 280, 38), (380, 530, 32), (420, 210, 25)
    ]
    for cx, cy, r in scabs:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(48, 55, 30), outline=(25, 30, 15))
        # Velvety textured inner blotches
        draw.ellipse([cx - r//2, cy - r//2, cx + r//2, cy + r//2], fill=(30, 35, 18))

    return img


def generate_cucumber_powdery_mildew() -> Image.Image:
    """Creates a cucumber leaf with talcum-white powdery mildew spots."""
    w, h = 800, 800
    greenhouse_bg = np.random.randint(110, 140, (h, w, 3), dtype=np.uint8)
    greenhouse_bg[:, :, 1] += 25
    img = Image.fromarray(greenhouse_bg).filter(ImageFilter.GaussianBlur(3))
    draw = ImageDraw.Draw(img)

    # Angular 5-lobed cucumber leaf
    pts = [
        (400, 720), (320, 610), (220, 530), (180, 390), (250, 320),
        (310, 230), (400, 120), (490, 230), (550, 320), (620, 390),
        (580, 530), (480, 610), (400, 720)
    ]
    draw.polygon(pts, fill=(58, 145, 50), outline=(35, 95, 30))

    # Palmate veins radiating from base
    vein_color = (90, 180, 75)
    for target in [(400, 130), (310, 230), (490, 230), (220, 530), (580, 530)]:
        draw.line([(400, 660), target], fill=vein_color, width=3)

    # Talcum powder white blotches
    mildew_patches = [
        (350, 330, 48), (440, 290, 55), (320, 450, 60),
        (460, 420, 52), (390, 520, 45), (410, 210, 38)
    ]
    for cx, cy, r in mildew_patches:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(225, 235, 220), outline=(190, 205, 185))
        draw.ellipse([cx - r//2, cy - r//2, cx + r//2, cy + r//2], fill=(245, 250, 245))

    return img


def build_sample_assets():
    """Generates and writes all sample images to disk."""
    images_dir = SAMPLES_DIR.parent.parent / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    samples = [
        ("tomato_late_blight.jpg", generate_tomato_late_blight()),
        ("apple_scab.jpg", generate_apple_scab()),
        ("cucumber_powdery_mildew.jpg", generate_cucumber_powdery_mildew()),
        ("cotton_bacterial_blight.jpg", generate_cotton_bacterial_blight()),
        ("grape_powdery_mildew.jpg", generate_grape_powdery_mildew()),
        ("cotton_verticillium_wilt.jpg", generate_cotton_verticillium_wilt()),
        ("grape_saline_scorch.jpg", generate_grape_saline_scorch()),
    ]
    for filename, image in samples:
        path = SAMPLES_DIR / filename
        image.save(path, format="JPEG", quality=90)
        # Also copy to images_dir so Web UI serves them directly
        if images_dir.exists():
            img_path = images_dir / filename
            image.save(img_path, format="JPEG", quality=90)
        print(f"Generated sample: {path}")


if __name__ == "__main__":
    build_sample_assets()
