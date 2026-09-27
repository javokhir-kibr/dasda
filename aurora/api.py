"""
FastAPI REST Application and Orchestration Gateway for Project Aurora.
"""
import io
import time
import base64
from pathlib import Path
from typing import Optional, List
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from PIL import Image

from aurora.config import (
    STATIC_DIR,
    SAMPLES_DIR,
    IMAGES_DIR,
    GEMINI_API_KEY,
    MODEL_NAME,
    SUPPORTED_REGIONS,
    SUPPORTED_CROPS
)
from pydantic import BaseModel
from aurora.schemas import (
    DiagnosticApiResponse,
    PreprocessingMetrics,
    AuroraCropDiagnosis
)
from aurora.preprocessor import process_uploaded_image, enhance_field_image
from aurora.engine import diagnose_field_image, DEMO_DIAGNOSTIC_CASES, consult_ai_agronomist
from aurora.agronomy_data import DISEASE_CATALOG, PHYTOSANITARY_MAP_DATA


class AgronomistChatRequest(BaseModel):
    question: str
    crop: Optional[str] = "AUTO"
    disease: Optional[str] = None
    lang: Optional[str] = "uz"

app = FastAPI(
    title="Project Aurora: Crop Pathology Engine",
    description="Autonomous rapid crop disease diagnostic platform for Uzbekistan (Cotton & Grapes).",
    version="1.0.0"
)

# Enable CORS for mobile apps, PWAs, and local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_no_cache_headers(request, call_next):
    response = await call_next(request)
    if request.url.path.endswith((".js", ".css", ".html")) or request.url.path == "/":
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response


@app.get("/api/health")
async def health_check():
    """System health check and active configuration status."""
    import os
    from aurora.config import GEMINI_API_KEY as CFG_KEY
    key = os.getenv("GEMINI_API_KEY") or CFG_KEY or ""
    has_api_key = bool(key and key.strip())
    return {
        "status": "healthy",
        "platform": "Project Aurora",
        "engine": MODEL_NAME,
        "gemini_api_key_configured": has_api_key,
        "mode": "live_ready" if has_api_key else "demo_ready",
        "supported_crops": SUPPORTED_CROPS,
        "supported_regions": SUPPORTED_REGIONS
    }


@app.get("/api/sample-cases")
async def list_sample_cases():
    """Returns available Uzbek agricultural test cases."""
    cases = [
        {
            "id": "tomato_late_blight",
            "title_en": "Tomato Late Blight (Phytophthora)",
            "title_uz": "Pomidor fitoftorozi (Qorayish kasalligi)",
            "crop": "TOMATO",
            "image_url": "/images/tomato_late_blight.jpg",
            "expected_threat": "HIGH"
        },
        {
            "id": "apple_scab",
            "title_en": "Apple Scab (Venturia Black Spot)",
            "title_uz": "Olma kalmarazi (Parsha dog'lari)",
            "crop": "FRUIT_TREE",
            "image_url": "/images/apple_scab.jpg",
            "expected_threat": "MEDIUM"
        },
        {
            "id": "cucumber_powdery_mildew",
            "title_en": "Cucumber Powdery Mildew (White Mold)",
            "title_uz": "Bodring un shudringi (Oq mog'or)",
            "crop": "CUCUMBER",
            "image_url": "/images/cucumber_powdery_mildew.jpg",
            "expected_threat": "HIGH"
        },
        {
            "id": "cotton_bacterial_blight",
            "title_en": "Cotton Angular Leaf Spot (Bacterial Blight)",
            "title_uz": "G'oza gommozi (Burchakli bakterial dog'lanish)",
            "crop": "COTTON",
            "image_url": "/images/cotton_bacterial_blight.jpg",
            "expected_threat": "HIGH"
        },
        {
            "id": "cotton_verticillium_wilt",
            "title_en": "Cotton Verticillium Wilt (Tiger-stripe)",
            "title_uz": "G'oza vertitsillyoz vilti (So'lish)",
            "crop": "COTTON",
            "image_url": "/images/cotton_verticillium_wilt.jpg",
            "expected_threat": "CRITICAL"
        },
        {
            "id": "grape_powdery_mildew",
            "title_en": "Grapevine Powdery Mildew (Oidium)",
            "title_uz": "Uzum un shudringi (Oidium zamburug'i)",
            "crop": "GRAPE",
            "image_url": "/images/grape_powdery_mildew.jpg",
            "expected_threat": "CRITICAL"
        },
        {
            "id": "grape_downy_mildew",
            "title_en": "Grapevine Downy Mildew (Mildew)",
            "title_uz": "Uzum soxta un shudringi (Mildiью)",
            "crop": "GRAPE",
            "image_url": "/images/grape_downy_mildew.jpg",
            "expected_threat": "HIGH"
        },
        {
            "id": "cotton_spider_mite",
            "title_en": "Cotton Two-spotted Spider Mite",
            "title_uz": "G'oza o'rgimchakkanasi (Zararkunanda)",
            "crop": "COTTON",
            "image_url": "/images/cotton_spider_mite.jpg",
            "expected_threat": "HIGH"
        },
        {
            "id": "grape_saline_scorch",
            "title_en": "Grape Soil Salinity & Heat Scorch",
            "title_uz": "Uzum tuproq sho'rlanishi va issiq urishi",
            "crop": "GRAPE",
            "image_url": "/images/grape_saline_scorch.jpg",
            "expected_threat": "MEDIUM"
        }
    ]
    return {"cases": cases}


@app.get("/api/sample-image/{sample_id}")
async def get_sample_image(sample_id: str):
    """Serves sample image files from images directory or fallback samples."""
    file_path = IMAGES_DIR / f"{sample_id}.jpg"
    if not file_path.exists():
        file_path = SAMPLES_DIR / f"{sample_id}.jpg"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Sample image not found")
    return FileResponse(file_path, media_type="image/jpeg")


@app.get("/api/disease-catalog")
def get_disease_catalog():
    """Returns comprehensive foliar disease encyclopedia for Uzbekistan crops."""
    return {"catalog": DISEASE_CATALOG}


@app.get("/api/phytosanitary-map")
def get_phytosanitary_map():
    """Returns live disease risk levels and agro-climatic alerts for all 14 regions."""
    return {"regions": PHYTOSANITARY_MAP_DATA}


@app.post("/api/agronomist-chat")
def chat_with_agronomist(req: AgronomistChatRequest):
    """
    Direct farmer consultation with Aurora AI Agronomist in natural Uzbek.
    Returns tailored cultural & chemical remediation steps.
    """
    if not req.question or not req.question.strip():
        raise HTTPException(status_code=400, detail="Savol matni bo'sh bo'lmasligi kerak.")

    advice = consult_ai_agronomist(
        question=req.question.strip(),
        crop_context=req.crop or "AUTO",
        disease_context=req.disease,
        lang=req.lang or "uz"
    )
    return {"status": "success", "answer": advice}


@app.post("/api/preprocess-preview")
def preprocess_preview(
    file: UploadFile = File(...)
):
    """
    Returns side-by-side base64 images of the raw upload versus the CLAHE
    enhanced version, along with blur variance and solar glare ratios.
    """
    contents = file.file.read()
    raw_img = Image.open(io.BytesIO(contents)).convert("RGB")
    enhanced_img = enhance_field_image(raw_img)

    _, _, metrics = process_uploaded_image(contents, enable_clahe=True)

    # Encode raw preview
    buf_raw = io.BytesIO()
    raw_img.thumbnail((600, 600))
    raw_img.save(buf_raw, format="JPEG", quality=80)
    raw_b64 = base64.b64encode(buf_raw.getvalue()).decode("utf-8")

    # Encode enhanced preview
    buf_enh = io.BytesIO()
    enhanced_img.thumbnail((600, 600))
    enhanced_img.save(buf_enh, format="JPEG", quality=80)
    enh_b64 = base64.b64encode(buf_enh.getvalue()).decode("utf-8")

    return {
        "metrics": metrics,
        "raw_preview": f"data:image/jpeg;base64,{raw_b64}",
        "enhanced_preview": f"data:image/jpeg;base64,{enh_b64}"
    }


class ApiKeyUpdateRequest(BaseModel):
    api_key: str


@app.get("/api/api-key-status")
def get_api_key_status():
    import os
    from aurora.config import GEMINI_API_KEY, MODEL_NAME
    key_val = os.getenv("GEMINI_API_KEY") or GEMINI_API_KEY or ""
    is_configured = bool(key_val and key_val.strip())
    masked = f"{key_val[:4]}...{key_val[-4:]}" if is_configured and len(key_val) > 8 else ""
    return {
        "configured": is_configured,
        "masked_key": masked,
        "model": MODEL_NAME
    }


@app.post("/api/set-api-key")
def set_api_key(req: ApiKeyUpdateRequest):
    from aurora.config import update_gemini_api_key
    success = update_gemini_api_key(req.api_key)
    if not success:
        raise HTTPException(status_code=500, detail="API kalitini saqlashda xatolik yuz berdi.")
    return {"status": "success", "message": "API kaliti muvaffaqiyatli saqlandi va Jonli AI faollashtirildi!"}


@app.post("/api/diagnose", response_model=DiagnosticApiResponse)
def run_diagnosis(
    file: UploadFile = File(...),
    crop_hint: str = Form("AUTO"),
    region: str = Form("Fergana Valley"),
    enable_clahe: bool = Form(True),
    force_demo: bool = Form(False),
    sample_id: Optional[str] = Form(None)
):
    """
    Main diagnostic endpoint:
    Processes raw field image, applies CLAHE / blur checks, invokes Gemini API
    with strict JSON output schema, and returns actionable diagnosis.
    """
    start_time = time.perf_counter()

    try:
        raw_bytes = file.file.read()
        if not raw_bytes:
            raise HTTPException(status_code=400, detail="Uploaded file is empty.")

        # 1. Edge & Field Preprocessing
        processed_bytes, _, metrics = process_uploaded_image(
            raw_bytes,
            enable_clahe=enable_clahe
        )

        # 2. Vision & Diagnostic Engine (Gemini 3.8 Flash / Computer Vision Dynamic Engine)
        diagnosis, mode = diagnose_field_image(
            image_bytes=processed_bytes,
            crop_hint=crop_hint,
            region=region,
            force_demo=force_demo,
            sample_id=sample_id,
            filename=file.filename
        )

        latency = round((time.perf_counter() - start_time) * 1000.0, 1)

        return DiagnosticApiResponse(
            success=True,
            diagnosis=diagnosis,
            metrics=metrics,
            latency_ms=latency,
            mode=mode,
            crop_hint=crop_hint,
            region=region
        )

    except HTTPException:
        raise
    except Exception as exc:
        latency = round((time.perf_counter() - start_time) * 1000.0, 1)
        raise HTTPException(status_code=500, detail=f"Diagnostic error: {str(exc)}")


# Mount images directory (logo & foliar pathology specimens)
if IMAGES_DIR.exists():
    app.mount("/images", StaticFiles(directory=IMAGES_DIR), name="images")

# Mount static web app
if STATIC_DIR.exists():
    app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
