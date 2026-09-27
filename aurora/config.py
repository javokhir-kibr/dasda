"""
Configuration module for Project Aurora.
"""
import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
SAMPLES_DIR = BASE_DIR / "aurora" / "samples"
IMAGES_DIR = BASE_DIR / "images"

# Load .env if present
ENV_FILE = BASE_DIR / ".env"
if ENV_FILE.exists():
    with open(ENV_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                k_clean = k.strip()
                v_clean = v.strip()
                if not os.environ.get(k_clean):
                    os.environ[k_clean] = v_clean

# Gemini API configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = os.getenv("AURORA_GEMINI_MODEL", "gemini-3.5-flash-lite")
TEMPERATURE = float(os.getenv("AURORA_TEMPERATURE", "0.10"))

# Server & Deployment configuration
PORT = int(os.getenv("PORT", "8000"))
HOST = os.getenv("HOST", "0.0.0.0")

# Field image processing thresholds
MAX_IMAGE_DIMENSION = int(os.getenv("MAX_IMAGE_DIMENSION", "1280"))
WEBP_QUALITY = int(os.getenv("WEBP_QUALITY", "85"))
BLUR_THRESHOLD = float(os.getenv("BLUR_THRESHOLD", "80.0"))  # Laplacian variance
GLARE_PIXEL_THRESHOLD = int(os.getenv("GLARE_PIXEL_THRESHOLD", "245"))
GLARE_AREA_RATIO_THRESHOLD = float(os.getenv("GLARE_AREA_RATIO_THRESHOLD", "0.15"))

# Uzbekistan All 14 Administrative & Agricultural Regions
SUPPORTED_REGIONS = [
    {"id": "andijan", "name_uz": "Andijon viloyati", "name_en": "Andijan Region", "coords": "40.7821° N, 72.3442° E"},
    {"id": "fergana", "name_uz": "Farg'ona viloyati", "name_en": "Fergana Region", "coords": "40.3842° N, 71.7843° E"},
    {"id": "namangan", "name_uz": "Namangan viloyati", "name_en": "Namangan Region", "coords": "40.9983° N, 71.6726° E"},
    {"id": "tashkent_region", "name_uz": "Toshkent viloyati", "name_en": "Tashkent Region", "coords": "41.2213° N, 69.8597° E"},
    {"id": "tashkent_city", "name_uz": "Toshkent shahri (Agro-voha)", "name_en": "Tashkent City (Suburban)", "coords": "41.3111° N, 69.2797° E"},
    {"id": "samarkand", "name_uz": "Samarqand viloyati", "name_en": "Samarkand Region", "coords": "39.6542° N, 66.9597° E"},
    {"id": "bukhara", "name_uz": "Buxoro viloyati", "name_en": "Bukhara Region", "coords": "39.7681° N, 64.4556° E"},
    {"id": "navoiy", "name_uz": "Navoiy viloyati", "name_en": "Navoi Region", "coords": "40.0844° N, 65.3792° E"},
    {"id": "jizzakh", "name_uz": "Jizzax viloyati", "name_en": "Jizzakh Region", "coords": "40.1158° N, 67.8422° E"},
    {"id": "sirdaryo", "name_uz": "Sirdaryo viloyati", "name_en": "Syrdarya Region", "coords": "40.5011° N, 68.7842° E"},
    {"id": "kashkadarya", "name_uz": "Qashqadaryo viloyati", "name_en": "Kashkadarya Region", "coords": "38.8606° N, 65.7891° E"},
    {"id": "surkhandarya", "name_uz": "Surxondaryo viloyati", "name_en": "Surkhandarya Region", "coords": "37.9409° N, 67.5709° E"},
    {"id": "khorezm", "name_uz": "Xorazm viloyati", "name_en": "Khorezm Region", "coords": "41.5562° N, 60.6313° E"},
    {"id": "karakalpakstan", "name_uz": "Qoraqalpog'iston Respublikasi", "name_en": "Republic of Karakalpakstan", "coords": "43.7683° N, 59.0214° E"}
]

SUPPORTED_CROPS = [
    {"code": "AUTO", "name_en": "Auto-Detect (Any Plant, Tree, Flower or Crop)", "name_uz": "Avtomatik aniqlash (Har qanday o'simlik, daraxt, gul yoki ekin)"},
    {"code": "TOMATO", "name_en": "Tomato & Backyard Vegetables (Pomidor, Bodring, Qalampir)", "name_uz": "Tomorqa & Sabzavotlar (Pomidor, Bodring, Qalampir)"},
    {"code": "FRUIT_TREE", "name_en": "Fruit Trees (Apple, Peach, Apricot, Cherry, Pomegranate)", "name_uz": "Mevali daraxtlar (Olma, Shaftoli, O'rik, Gilos, Anor)"},
    {"code": "POTATO", "name_en": "Potato, Eggplant & Legumes", "name_uz": "Kartoshka, Baqlajon va Dukkaklilar"},
    {"code": "GRAPE", "name_en": "Grapes & Vineyards", "name_uz": "Uzum / Tokzor"},
    {"code": "HOUSEPLANT", "name_en": "Houseplants, Balcony & Ornamental Flowers", "name_uz": "Xona gullari va manzarali o'simliklar"},
    {"code": "COTTON", "name_en": "Cotton (Commercial Field Crop)", "name_uz": "Paxta / G'oza"}
]


def update_gemini_api_key(new_key: str) -> bool:
    """Updates runtime GEMINI_API_KEY and persists to .env file."""
    global GEMINI_API_KEY
    clean_key = new_key.strip()
    GEMINI_API_KEY = clean_key
    os.environ["GEMINI_API_KEY"] = clean_key

    try:
        env_lines = []
        if ENV_FILE.exists():
            with open(ENV_FILE, "r", encoding="utf-8") as f:
                env_lines = f.readlines()
        found = False
        new_lines = []
        for line in env_lines:
            if line.strip().startswith("GEMINI_API_KEY="):
                new_lines.append(f"GEMINI_API_KEY={clean_key}\n")
                found = True
            else:
                new_lines.append(line)
        if not found:
            new_lines.append(f"GEMINI_API_KEY={clean_key}\n")

        with open(ENV_FILE, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        return True
    except Exception:
        return False

