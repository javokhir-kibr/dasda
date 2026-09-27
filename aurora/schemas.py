"""
Pydantic data models and schemas for Project Aurora.
"""
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class SpecimenType(str, Enum):
    TOMATO_PLANT = "TOMATO_PLANT"
    CUCUMBER_PLANT = "CUCUMBER_PLANT"
    FRUIT_TREE = "FRUIT_TREE"
    POTATO_PLANT = "POTATO_PLANT"
    GRAPE_LEAF = "GRAPE_LEAF"
    COTTON_LEAF = "COTTON_LEAF"
    HOUSEPLANT = "HOUSEPLANT"
    OTHER_PLANT = "OTHER_PLANT"
    NON_VEGETATION = "NON_VEGETATION"


class ImageIntegrity(str, Enum):
    CLEAR_DIAGNOSTIC_QUALITY = "CLEAR_DIAGNOSTIC_QUALITY"
    EXCESSIVE_GLARE = "EXCESSIVE_GLARE"
    PARTIALLY_BLURRED = "PARTIALLY_BLURRED"
    SOIL_DOMINATED_BACKGROUND = "SOIL_DOMINATED_BACKGROUND"
    INSUFFICIENT_DETAIL = "INSUFFICIENT_DETAIL"


class PathogenType(str, Enum):
    BACTERIAL = "BACTERIAL"
    FUNGAL = "FUNGAL"
    VIRAL = "VIRAL"
    PEST_DAMAGE = "PEST_DAMAGE"
    ABIOTIC_STRESS = "ABIOTIC_STRESS"
    HEALTHY = "HEALTHY"


class ThreatLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class CostCategory(str, Enum):
    ZERO_COST = "ZERO_COST"
    LOW_COST_LOCAL_REMEDY = "LOW_COST_LOCAL_REMEDY"
    STANDARD_FUNGICIDE_BACTERICIDE = "STANDARD_FUNGICIDE_BACTERICIDE"


class PrimaryDiagnosis(BaseModel):
    scientific_name: str = Field(description="Scientific Latin classification of pathogen or physiological disorder")
    common_name_en: str = Field(description="Standard English agricultural common name")
    common_name_uz: str = Field(description="Uzbek language common name widely recognized by local dehqons")
    pathogen_type: PathogenType = Field(description="Broad category of disease or stress")


class LowCostIntervention(BaseModel):
    step_number: int = Field(ge=1, le=3, description="Ordinal priority sequence (1 to 3)")
    title_uz: str = Field(description="Actionable title in Uzbek Latin script")
    title_en: str = Field(description="Actionable title in English")
    action_description: str = Field(description="Clear, low-cost practical instruction tailored for Central Asian farmers")
    cost_category: CostCategory = Field(description="Economic burden tier of this intervention")


class AuroraCropDiagnosis(BaseModel):
    specimen_identified: SpecimenType = Field(description="Identified plant host or non-vegetation flag")
    image_integrity_status: ImageIntegrity = Field(description="Quality assessment of field photography")
    primary_diagnosis: PrimaryDiagnosis = Field(description="Detailed disease or health status classification")
    threat_level: ThreatLevel = Field(description="Urgency tier based on pathogen virulence and infection extent")
    confidence_score: float = Field(ge=0.0, le=1.0, description="Confidence certainty score between 0.0 and 1.0")
    abiotic_vs_biotic_assessment: str = Field(description="Reasoning separating environmental/salinity/heat factors from fungal/bacterial vectors")
    visual_biomarkers: List[str] = Field(description="Specific physical symptoms observed on the leaf surface")
    immediate_low_cost_interventions: List[LowCostIntervention] = Field(
        min_length=3, max_length=3,
        description="Exactly 3 localized, immediate, low-cost intervention steps"
    )
    farmer_advisory_uzbek: str = Field(description="Compassionate, plain-language 2-sentence summary in Uzbek Latin")
    farmer_advisory_english: Optional[str] = Field(default=None, description="Compassionate, plain-language 2-sentence summary in English")
    differential_diagnosis: str = Field(description="Secondary possible diagnosis or lookalike condition")


class PreprocessingMetrics(BaseModel):
    blur_score: float = Field(description="Laplacian variance sharpness score")
    is_blurry: bool = Field(description="True if blur score is below threshold")
    glare_ratio: float = Field(description="Percentage of pixels in over-exposed/glare condition")
    has_excessive_glare: bool = Field(description="True if glare ratio exceeds threshold")
    original_size: List[int] = Field(description="Original width, height")
    processed_size: List[int] = Field(description="Processed width, height")
    clahe_applied: bool = Field(default=True, description="Whether CLAHE histogram equalization was applied")


class DiagnosticApiResponse(BaseModel):
    success: bool = True
    diagnosis: AuroraCropDiagnosis
    metrics: PreprocessingMetrics
    latency_ms: float
    mode: str = Field(description="'live' if generated via Gemini API, or 'demo' if synthetic fallback")
    crop_hint: Optional[str] = None
    region: Optional[str] = None
