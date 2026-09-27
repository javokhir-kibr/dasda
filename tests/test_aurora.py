"""
Test suite for Project Aurora: Crop Disease Detection Platform.
"""
import io
import pytest
import numpy as np
from PIL import Image, ImageFilter
from fastapi.testclient import TestClient

from aurora.config import SAMPLES_DIR
from aurora.schemas import (
    AuroraCropDiagnosis,
    SpecimenType,
    ThreatLevel,
    PathogenType,
    CostCategory
)
from aurora.preprocessor import (
    detect_blur,
    detect_glare,
    apply_clahe_numpy,
    process_uploaded_image
)
from aurora.engine import diagnose_field_image
from aurora.api import app

client = TestClient(app)


def test_detect_blur():
    """Verify Laplacian variance correctly flags blurred vs sharp images."""
    # Create sharp synthetic checkerboard
    sharp = np.zeros((200, 200), dtype=np.uint8)
    sharp[::10, :] = 255
    sharp[:, ::10] = 255
    var_sharp, is_blurry_sharp = detect_blur(sharp)
    assert not is_blurry_sharp
    assert var_sharp > 80.0

    # Create heavily blurred image
    pil_blur = Image.fromarray(sharp).filter(ImageFilter.GaussianBlur(15))
    var_blur, is_blurry_blur = detect_blur(np.array(pil_blur))
    assert is_blurry_blur
    assert var_blur < 80.0


def test_detect_glare():
    """Verify glare detector captures washed out high-noon sunlight."""
    # Normal image
    normal = np.full((100, 100), 128, dtype=np.uint8)
    glare_ratio, has_glare = detect_glare(normal)
    assert not has_glare
    assert glare_ratio == 0.0

    # Blinding glare image (>15% pixels with value 250)
    washed = np.full((100, 100), 120, dtype=np.uint8)
    washed[:30, :] = 255  # 30% glare
    glare_ratio, has_glare = detect_glare(washed)
    assert has_glare
    assert glare_ratio >= 0.25


def test_clahe_enhancement():
    """Verify CLAHE array output stays bounded and equalizes contrast."""
    luminance = np.random.randint(50, 150, (120, 120), dtype=np.uint8)
    enhanced = apply_clahe_numpy(luminance, grid_size=(4, 4), clip_limit=2.5)
    assert enhanced.shape == luminance.shape
    assert enhanced.dtype == np.uint8
    assert enhanced.max() <= 255
    assert enhanced.min() >= 0


def test_process_uploaded_image():
    """Verify preprocessing correctly downscales and generates metrics."""
    # Large 2000x2000 image
    large = Image.new("RGB", (2000, 1500), color=(60, 140, 50))
    buf = io.BytesIO()
    large.save(buf, format="JPEG")
    raw_bytes = buf.getvalue()

    compressed, processed_img, metrics = process_uploaded_image(raw_bytes, enable_clahe=True)
    assert len(compressed) < len(raw_bytes)
    assert max(metrics.processed_size) <= 1280
    assert metrics.original_size == [2000, 1500]
    assert metrics.clahe_applied is True


def test_engine_demo_diagnosis():
    """Verify diagnosis engine returns valid structured diagnosis."""
    dummy_bytes = b"fake_leaf_image_bytes"
    diagnosis, mode = diagnose_field_image(
        image_bytes=dummy_bytes,
        crop_hint="COTTON",
        region="Fergana Valley",
        force_demo=True
    )
    assert isinstance(diagnosis, AuroraCropDiagnosis)
    assert diagnosis.specimen_identified == SpecimenType.COTTON_LEAF
    assert diagnosis.threat_level in [ThreatLevel.HIGH, ThreatLevel.CRITICAL]
    assert len(diagnosis.immediate_low_cost_interventions) == 3
    assert diagnosis.confidence_score >= 0.80
    assert "Xanthomonas" in diagnosis.primary_diagnosis.scientific_name
    assert mode == "demo"


def test_api_health_endpoint():
    """Verify GET /api/health."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "Project Aurora" in data["platform"]


def test_api_sample_cases():
    """Verify GET /api/sample-cases lists 4 regional field cases."""
    response = client.get("/api/sample-cases")
    assert response.status_code == 200
    data = response.json()
    assert len(data["cases"]) >= 4
    case_ids = [c["id"] for c in data["cases"]]
    assert "cotton_bacterial_blight" in case_ids
    assert "grape_powdery_mildew" in case_ids


def test_api_sample_image():
    """Verify GET /api/sample-image/{sample_id} delivers valid JPEG."""
    response = client.get("/api/sample-image/cotton_bacterial_blight")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    assert len(response.content) > 1000


def test_api_diagnose_endpoint():
    """Verify POST /api/diagnose with realistic field sample."""
    sample_path = SAMPLES_DIR / "cotton_bacterial_blight.jpg"
    with open(sample_path, "rb") as f:
        file_bytes = f.read()

    response = client.post(
        "/api/diagnose",
        files={"file": ("sample.jpg", file_bytes, "image/jpeg")},
        data={
            "crop_hint": "COTTON",
            "region": "Fergana Valley",
            "enable_clahe": "true",
            "force_demo": "true"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "diagnosis" in data
    assert data["diagnosis"]["primary_diagnosis"]["common_name_en"] == "Bacterial Blight (Angular Leaf Spot)"
    assert len(data["diagnosis"]["immediate_low_cost_interventions"]) == 3
    assert data["metrics"]["clahe_applied"] is True
    assert data["latency_ms"] > 0


def test_api_disease_catalog():
    """Verify GET /api/disease-catalog returns rich foliar encyclopedia."""
    response = client.get("/api/disease-catalog")
    assert response.status_code == 200
    data = response.json()
    assert "catalog" in data
    assert len(data["catalog"]) >= 6
    for item in data["catalog"]:
        assert "id" in item
        assert "crop" in item
        assert "name_uz" in item
        assert "pathogen_type" in item
        assert "threat_level" in item
        assert "recommended_dosage_uz" in item
        assert isinstance(item["cultural_remedies_uz"], list)


def test_api_phytosanitary_map():
    """Verify GET /api/phytosanitary-map delivers data for all 14 Uzbekistan regions."""
    response = client.get("/api/phytosanitary-map")
    assert response.status_code == 200
    data = response.json()
    assert "regions" in data
    assert len(data["regions"]) == 14
    region_ids = [r["region_id"] for r in data["regions"]]
    assert "fergana" in region_ids
    assert "andijan" in region_ids
    assert "samarkand" in region_ids
    assert "karakalpakstan" in region_ids
    for r in data["regions"]:
        assert "region_name" in r
        assert "risk_level" in r
        assert "advice_uz" in r
        assert "temperature" in r


def test_api_agronomist_chat_success():
    """Verify POST /api/agronomist-chat provides natural Uzbek agronomy advice."""
    response = client.post(
        "/api/agronomist-chat",
        json={
            "question": "Paxtada gommoz kasalligiga qarshi qanday dori tavsiya qilasiz?",
            "crop": "COTTON",
            "disease": "Bacterial Blight"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["answer"], str)
    assert len(data["answer"]) > 20


def test_api_agronomist_chat_empty_validation():
    """Verify POST /api/agronomist-chat rejects empty questions with 400 error."""
    response = client.post(
        "/api/agronomist-chat",
        json={"question": "   ", "crop": "COTTON"}
    )
    assert response.status_code == 400
    assert "bo'sh" in response.json()["detail"]


def test_api_preprocess_preview():
    """Verify POST /api/preprocess-preview generates side-by-side CLAHE preview."""
    sample_path = SAMPLES_DIR / "cotton_bacterial_blight.jpg"
    with open(sample_path, "rb") as f:
        file_bytes = f.read()

    response = client.post(
        "/api/preprocess-preview",
        files={"file": ("sample.jpg", file_bytes, "image/jpeg")}
    )
    assert response.status_code == 200
    data = response.json()
    assert "metrics" in data
    assert "raw_preview" in data
    assert "enhanced_preview" in data
    assert data["raw_preview"].startswith("data:image/jpeg;base64,")
    assert data["enhanced_preview"].startswith("data:image/jpeg;base64,")


def test_engine_tomato_diagnosis():
    """Verify diagnosis engine handles household tomatoes (pomidor fitoftoroz)."""
    diagnosis, mode = diagnose_field_image(
        image_bytes=b"fake_tomato_leaf",
        crop_hint="TOMATO",
        force_demo=True
    )
    assert diagnosis.specimen_identified == SpecimenType.TOMATO_PLANT
    assert "Phytophthora" in diagnosis.primary_diagnosis.scientific_name
    assert "fitoftor" in diagnosis.primary_diagnosis.common_name_uz.lower()
    assert len(diagnosis.immediate_low_cost_interventions) == 3
    # Check that accessible home remedies are included
    remedy_titles = [i.title_uz.lower() for i in diagnosis.immediate_low_cost_interventions]
    assert any("mis kuporosi" in t or "bordo" in t or "sut zardobi" in t or "uzib" in t for t in remedy_titles)


def test_engine_apple_scab_diagnosis():
    """Verify diagnosis engine handles orchard fruit trees (olma kalmarazi / parsha)."""
    diagnosis, mode = diagnose_field_image(
        image_bytes=b"fake_apple_leaf",
        crop_hint="FRUIT_TREE",
        force_demo=True
    )
    assert diagnosis.specimen_identified == SpecimenType.FRUIT_TREE
    assert "Venturia" in diagnosis.primary_diagnosis.scientific_name
    assert "Parsha" in diagnosis.primary_diagnosis.common_name_uz or "Kalmaraz" in diagnosis.primary_diagnosis.common_name_uz


def test_api_household_sample_cases():
    """Verify sample cases include tomatoes, apples, and cucumbers for ordinary citizens."""
    response = client.get("/api/sample-cases")
    assert response.status_code == 200
    cases = response.json()["cases"]
    case_ids = [c["id"] for c in cases]
    assert "tomato_late_blight" in case_ids
    assert "apple_scab" in case_ids
    assert "cucumber_powdery_mildew" in case_ids


def test_api_agronomist_chat_tomato_tomorqa():
    """Verify chat advisor answers household tomato questions with accessible remedies."""
    response = client.post(
        "/api/agronomist-chat",
        json={
            "question": "Hovlidagi pomidorlarim fitoftoroz bo'lib barglari qorayib ketyapti, uy sharoitida qanday davolasa bo'ladi?",
            "crop": "TOMATO"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert len(data["answer"]) > 30


def test_distinct_sample_diagnoses():
    """Verify that DIFFERENT samples return DIFFERENT, DISTINCT diagnoses instead of identical fallback."""
    # Create valid JPEG bytes
    dummy_img = Image.new("RGB", (100, 100), color=(40, 130, 40))
    buf = io.BytesIO()
    dummy_img.save(buf, format="JPEG")
    valid_bytes = buf.getvalue()

    # 1. Cotton Verticillium Wilt vs Bacterial Blight
    res_wilt = client.post(
        "/api/diagnose",
        files={"file": ("leaf.jpg", valid_bytes, "image/jpeg")},
        data={"crop_hint": "COTTON", "sample_id": "cotton_verticillium_wilt"}
    )
    res_blight = client.post(
        "/api/diagnose",
        files={"file": ("leaf.jpg", valid_bytes, "image/jpeg")},
        data={"crop_hint": "COTTON", "sample_id": "cotton_bacterial_blight"}
    )
    assert res_wilt.status_code == 200
    assert res_blight.status_code == 200
    name_wilt = res_wilt.json()["diagnosis"]["primary_diagnosis"]["scientific_name"]
    name_blight = res_blight.json()["diagnosis"]["primary_diagnosis"]["scientific_name"]
    assert name_wilt != name_blight
    assert "Verticillium" in name_wilt
    assert "Xanthomonas" in name_blight

    # 2. Grape Downy Mildew vs Powdery Mildew vs Saline Scorch
    res_downy = client.post(
        "/api/diagnose",
        files={"file": ("leaf.jpg", valid_bytes, "image/jpeg")},
        data={"crop_hint": "GRAPE", "sample_id": "grape_downy_mildew"}
    )
    res_powdery = client.post(
        "/api/diagnose",
        files={"file": ("leaf.jpg", valid_bytes, "image/jpeg")},
        data={"crop_hint": "GRAPE", "sample_id": "grape_powdery_mildew"}
    )
    res_saline = client.post(
        "/api/diagnose",
        files={"file": ("leaf.jpg", valid_bytes, "image/jpeg")},
        data={"crop_hint": "GRAPE", "sample_id": "grape_saline_scorch"}
    )
    assert res_downy.status_code == 200
    assert res_powdery.status_code == 200
    assert res_saline.status_code == 200
    p_downy = res_downy.json()["diagnosis"]["primary_diagnosis"]["scientific_name"]
    p_powdery = res_powdery.json()["diagnosis"]["primary_diagnosis"]["scientific_name"]
    p_saline = res_saline.json()["diagnosis"]["primary_diagnosis"]["scientific_name"]
    assert p_downy != p_powdery
    assert p_powdery != p_saline
    assert "Plasmopara" in p_downy
    assert "Uncinula" in p_powdery
    assert "Salinity" in p_saline


def test_api_key_status_and_update():
    """Verify API key configuration endpoints."""
    # Check status endpoint
    res = client.get("/api/api-key-status")
    assert res.status_code == 200
    data = res.json()
    assert "configured" in data
    assert "model" in data

    # Update API key endpoint
    res_set = client.post(
        "/api/set-api-key",
        json={"api_key": "AIzaSyTestKey1234567890TestKey"}
    )
    assert res_set.status_code == 200
    assert res_set.json()["status"] == "success"

    # Verify status reflects configured
    res_after = client.get("/api/api-key-status")
    assert res_after.json()["configured"] is True
    assert "AIza" in res_after.json()["masked_key"]

    # Clean up and reset API key to empty
    client.post("/api/set-api-key", json={"api_key": ""})



