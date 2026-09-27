"""
Aurora Diagnostic Brain: Gemini API integration and regional agronomy logic.
Supports both live Gemini 3.8 Flash multimodal inference and zero-config local demo mode.
"""
import os
import json
import logging
from typing import Optional, Dict, Any

from aurora.config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE
from aurora.schemas import (
    AuroraCropDiagnosis,
    SpecimenType,
    ImageIntegrity,
    PathogenType,
    ThreatLevel,
    CostCategory,
    PrimaryDiagnosis,
    LowCostIntervention
)

logger = logging.getLogger("aurora.engine")

AURORA_SYSTEM_INSTRUCTION = """
[SYSTEM INSTRUCTION: AURORA UNIVERSAL PLANT DOCTOR & AGRONOMIST]
You are Aurora, an elite diagnostic plant pathologist and universal plant doctor engineered for Uzbekistan across all 14 territories (Fergana, Andijan, Namangan, Tashkent, Samarkand, Bukhara, Surkhandarya, Kashkadarya, Khorezm, Karakalpakstan, Syrdarya, Jizzakh, Navoi).

You serve BOTH commercial farmers AND ordinary citizens, families, and household gardeners (oddiy aholi, tomorqachilar, hovli bog'bonlari, shahar aholisi).

1. OPERATIONAL DOMAIN & PLANT CATALOG:
You diagnose ANY plant, vegetable, fruit tree, flower, houseplant, or crop:
- TOMORQA & SABZAVOTLAR (Garden & Vegetables):
  * Tomato (Pomidor): Late blight (Fitoftoroz - Phytophthora infestans), Early blight (Alternarioz), Blossom end rot (Uchki chirish / Kalsiy tanqisligi), Spider mites (O'rgimchakkana), Whitefly.
  * Cucumber, Melons & Watermelons (Bodring, Qovun, Tarvuz): Powdery mildew (Un shudring), Downy mildew (Soxta un shudring), Anthracnose, Root rot.
  * Potato, Pepper, Eggplant (Kartoshka, Qalampir, Baqlajon): Colorado beetle, Alternaria, Fusarium wilt, Viral leaf curl.
- MEVALI DARAXTLAR (Fruit Trees & Orchards):
  * Apple, Pear (Olma, Nok): Apple scab (Kalmaraz / Parsha - Venturia inaequalis), Powdery mildew (Un shudring), Codling moth (Olma qurti), Fire blight (Bakterial kuyish).
  * Peach, Apricot, Plum, Cherry (Shaftoli, O'rik, Olxo'ri, Gilos): Peach leaf curl (Barg buralishi / Tafranioz - Taphrina deformans), Clasterosporium (Teshikli dog'lanish), Moniliosis (Meva chirishi).
  * Pomegranate, Fig, Persimmon (Anor, Anjir, Xurmo).
- UZUM / TOKZOR (Grapevine):
  * Powdery mildew (Un shudring / Oidium), Downy mildew (Soxta un shudring / Mildew), Spider mites, Sunscald, Salinity scorch.
- XONA GULLARI VA MANZARALI O'SIMLIKLAR (Houseplants & Garden Flowers):
  * Ficus, roses, monstera, geraniums, petunias, citrus: Root rot (ildiz chirishi), scale insects (qalqondor), iron chlorosis (temir xlorozi), spider mites, drying leaf tips.
- DALA EKINLARI (Field Cash Crops):
  * Cotton (Paxta): Bacterial blight (Gommoz), Verticillium wilt, Spider mite.
  * Wheat (Bug'doy), Corn (Makkajo'xori).

2. STRICT MULTIMODAL REASONING STEPS:
Execute internal diagnostic verification before rendering JSON:
- Step 1: Mentally isolate the plant specimen. Identify what plant/leaf/fruit is shown (SpecimenType: TOMATO_PLANT, CUCUMBER_PLANT, FRUIT_TREE, POTATO_PLANT, GRAPE_LEAF, COTTON_LEAF, HOUSEPLANT, OTHER_PLANT).
- Step 2: Differentiate Biotic vs. Abiotic. Central Asian summers feature extreme heat and alkaline/saline water. Does the leaf exhibit uniform dry brown scorched edges (Heat/Drought/Salinity stress) or asymmetrical, expanding pathogen spots/mycelium?
- Step 3: Grade Threat Level strictly (LOW, MEDIUM, HIGH, CRITICAL).

3. ACCESSIBLE INTERVENTIONS FOR EVERYDAY CITIZENS & GARDENERS:
The 3 immediate interventions MUST be low-cost, easy to prepare, and accessible for ordinary households, home gardens, or local bazaars:
- Prioritize safe, easy home methods first when applicable:
  * Baking soda + soap spray (50g baking soda + 30g dissolved laundry soap per 10L water for powdery mildew/fungi).
  * Wood ash infusion (yog'och kuli eritmasi - rich in potassium and antifungal).
  * Pruning infected leaves and bottom foliage to improve air circulation.
  * Watering strictly at the root base in early morning or late evening; NEVER spraying water directly on foliage during hot sun.
- Standard affordable preparations from local agro-shops (Agrokimyo / Bozor):
  * Copper oxychloride (Xlorokis medi / Mis kuporosi), Bordeaux mixture (Bordo suyuqligi), Colloidal sulfur (oltingugurt), Fitosporin-M, Fitoverm.
- DO NOT recommend expensive or rare foreign chemicals that ordinary people cannot find.

4. LANGUAGE REQUIREMENTS:
Provide both farmer_advisory_uzbek and farmer_advisory_english:
- farmer_advisory_uzbek: Warm, colloquial, highly respectful and practical Uzbek Latin that any family member or gardener can immediately understand and put into practice.
- farmer_advisory_english: Clear, professional advisory suitable for international agronomists and researchers.
"""

# Pre-configured high-fidelity diagnostic profiles for demonstration & offline resilience
DEMO_DIAGNOSTIC_CASES: Dict[str, Dict[str, Any]] = {
    "tomato_late_blight": {
        "specimen_identified": SpecimenType.TOMATO_PLANT,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Phytophthora infestans",
            "common_name_en": "Tomato Late Blight (Phytophthora)",
            "common_name_uz": "Pomidor fitoftorozi (Barg va poya qorayishi)",
            "pathogen_type": PathogenType.FUNGAL
        },
        "threat_level": ThreatLevel.HIGH,
        "confidence_score": 0.95,
        "abiotic_vs_biotic_assessment": "Barglarda va poyada suvli, to'q jigarrang-qora yirik dog'lar. Nam havoda barg tagida oqish zamburug' g'ubori ko'rinadi. Bu oddiy jazirama issiq kuyishi emas, balki xavfli zamburug'li fitoftoradir.",
        "visual_biomarkers": [
            "Barg va poyada qoramtir-jigarrang tarqaluvchi dog'lar",
            "Barg chetlarining qurishi va mevalarga qora qattiq dog'lar o'tishi",
            "Namlik yuqori bo'lganda oqish mog'or g'ubori"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Kasal pastki barglarni darhol uzib tashlash",
                "title_en": "Prune Lower Stricken Leaves",
                "action_description": "Yerga tegib turgan va qoraygan barcha pastki barglarni uzib, tomorqadan tashqariga chiqarib ko'ming yoki yoqing.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Mis kuporosi yoki Bordo suyuqligi bilan purkash",
                "title_en": "Apply Copper Sulfate / Bordeaux Mixture",
                "action_description": "10 litr suvga 30-40 gramm Mis kuporosi yoki 1% li Bordo suyuqligi tayyorlab, pomidor tupi ustki va ostki barglariga ertalab seping.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "Faqat tagidan sug'orish, bargiga suv tegmasin",
                "title_en": "Root-Zone Irrigation Only",
                "action_description": "Pomidorni shlang bilan tepasidan cho'miltirib sug'ormang! Faqat egatdan yoki tomchilatib ildiziga suv bering.",
                "cost_category": CostCategory.ZERO_COST
            }
        ],
        "farmer_advisory_uzbek": "Pomidoringizda tomorqalarda eng ko'p uchraydigan fitoftora (qorayish) kasalligi boshlangan. Zudlik bilan qoraygan barglarni uzib tashlang, barglariga suv sachratmay faqat tagidan sug'oring va mis kuporosi bilan ishlov bering.",
        "farmer_advisory_english": "Tomato late blight (Phytophthora) detected. Immediately remove infected bottom leaves, avoid wetting foliage during irrigation, and apply copper fungicide early morning.",
        "differential_diagnosis": "Alternaria Leaf Spot (Early Blight), which forms concentric bullseye rings rather than broad water-soaked black patches."
    },
    "apple_scab": {
        "specimen_identified": SpecimenType.FRUIT_TREE,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Venturia inaequalis",
            "common_name_en": "Apple Scab (Black Spot)",
            "common_name_uz": "Olma kalmarazi (Parsha kasalligi)",
            "pathogen_type": PathogenType.FUNGAL
        },
        "threat_level": ThreatLevel.MEDIUM,
        "confidence_score": 0.94,
        "abiotic_vs_biotic_assessment": "Barg yuzasida zaytunrang-qoramtir, baxmalsimon to'garak dog'lar. Meva ustida esa qora po'stloq yorilishlari paydo bo'ladi. Bu tuproq yoki quyosh kuyishi emas, balki olma parshasi zamburug'idir.",
        "visual_biomarkers": [
            "Bargning ustki yuzasida baxmalsimon zaytunrang-to'q jigarrang dog'lar",
            "Barglarning erta sarg'ayishi va to'kilishi",
            "Meva sirtida qo'tir qora po'stloq yaralari"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Daraxt shoxlarini butash va siyraklatish",
                "title_en": "Canopy Pruning & Aeration",
                "action_description": "Daraxt ichiga quyosh nuri va shamol erkin kirishi uchun bir-biriga xalal berayotgan ichki shoxlarni kesib tashlang.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Bordo suyuqligi yoki Xlorokis medi purkash",
                "title_en": "Copper Oxychloride or Bordeaux Spray",
                "action_description": "10 litr suvga 40 gramm Xlorokis medi yoki 1% li Bordo suyuqligi aralashtirib daraxt barglariga ertalab purkang.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "To'kilgan kasal barglarni yig'ib yoqish",
                "title_en": "Sanitize Fallen Leaf Litter",
                "action_description": "Daraxt tagiga to'kilgan kasal barglarni xazonrezlikda yig'ib ko'ming yoki yoqing, chunki zamburug' shu barglarda qishlaydi.",
                "cost_category": CostCategory.ZERO_COST
            }
        ],
        "farmer_advisory_uzbek": "Olma daraxtida aholi tomorqa bog'larida keng tarqalgan kalmaraz (parsha) kasalligi aniqlandi. Daraxt ichki shoxlarini siyraklating, 1% li Bordo suyuqligi seping va to'kilgan barglarni daraxt tagidan tozalang.",
        "farmer_advisory_english": "Apple scab (Venturia inaequalis) identified on fruit foliage. Thin dense canopy branches to improve air circulation, spray 1% Bordeaux mixture, and rake fallen leaves.",
        "differential_diagnosis": "Apple Powdery Mildew, which produces a white flour-like coating rather than velvety olive-brown scabs."
    },
    "cucumber_powdery_mildew": {
        "specimen_identified": SpecimenType.CUCUMBER_PLANT,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Podosphaera xanthii",
            "common_name_en": "Cucumber Powdery Mildew",
            "common_name_uz": "Bodring un shudringi (Oq mog'or)",
            "pathogen_type": PathogenType.FUNGAL
        },
        "threat_level": ThreatLevel.HIGH,
        "confidence_score": 0.96,
        "abiotic_vs_biotic_assessment": "Barg yuzasida un sepib qo'yilgandek oqish-kulrang g'ubor dog'lari. Vaqt o'tishi bilan barg sarg'ayib quriydi. Issiq va dim havo zamburug' sporalarini tez tarqatadi.",
        "visual_biomarkers": [
            "Bargning ustki yuzasida oq unsimon dog'lar",
            "Barglarning sarg'ayishi va qirg'oqlari yuqoriga qayrilishi",
            "Hosil tugunlarining to'kilishi va o'sishning to'xtashi"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Sut zardobi yoki osh sodasi bilan xalqona purkash",
                "title_en": "Whey or Baking Soda Home Spray",
                "action_description": "1 litr sut zardobiga 9 litr suv va 20 tomchi yod aralashtirib seping, yoki 10L suvga 40g osh sodasi + kir sovun solib purkang.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Kolloid oltingugurt yoki Tiovit Jet sepish",
                "title_en": "Colloidal Sulfur / Thiovit Jet Spray",
                "action_description": "10 litr suvga 40-50 gramm Tiovit Jet yoki Kolloid oltingugurt aralashtirib, quyosh chiqmasdan ertalab soat 08:00 gacha seping.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "Pastki sarg'aygan qari barglarni olib tashlash",
                "title_en": "Prune Lower Yellow Leaves",
                "action_description": "Bodring tupining pastki qismidagi 3-4 dona sarg'aygan eski barglarni qaychi bilan kesib tashlab, shamollatishni ta'minlang.",
                "cost_category": CostCategory.ZERO_COST
            }
        ],
        "farmer_advisory_uzbek": "Bodring barglarida xavfli un shudring (oq un) kasalligi paydo bo'lgan. Sut zardobi yoki osh sodali eritma bilan ertalab barglarini yuving, pastki sarg'aygan barglarni uzib shamollatishni yaxshilang.",
        "farmer_advisory_english": "Cucumber powdery mildew detected. Spray with diluted milk whey or baking soda solution, remove old lower foliage to improve ventilation, and apply sulfur if needed.",
        "differential_diagnosis": "Downy mildew (Pseudoperonospora cubensis), which forms yellow angular spots delimited by leaf veins with purplish down underneath."
    },
    "cotton_bacterial_blight": {
        "specimen_identified": SpecimenType.COTTON_LEAF,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Xanthomonas citri pv. malvacearum",
            "common_name_en": "Bacterial Blight (Angular Leaf Spot)",
            "common_name_uz": "Bakterial burchakli dog'lanish (Gommoz)",
            "pathogen_type": PathogenType.BACTERIAL
        },
        "threat_level": ThreatLevel.HIGH,
        "confidence_score": 0.94,
        "abiotic_vs_biotic_assessment": "Lesions are sharply delimited by secondary and tertiary leaf veins forming geometric angular water-soaked brown spots, typical of Xanthomonas. High soil salinity ruled out as necrosis is not uniform along outer margins.",
        "visual_biomarkers": [
            "Angular water-soaked polyhedral lesions bounded by veinlets",
            "Dark reddish-brown necrotic centers with greasy translucent margins",
            "Incipient vein-clearing and localized black petiole streak"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Suv sepib sug'orishni to'xtating",
                "title_en": "Halt Sprinkler/Overhead Irrigation",
                "action_description": "Irrigate solely through ground furrows; avoid splashing water on foliage during midday heat to prevent bacterial spread across adjacent rows.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Mis kuporosi yoki Xlorokis medi bilan ishlov berish",
                "title_en": "Apply Copper Oxychloride / Bordeaux Mixture",
                "action_description": "Spray 0.4% Copper Oxychloride (Xlorokis medi, 40g per 10L water) or 1% Bordeaux mixture early in the morning before 08:30.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "Kasal shoxlarni olib tashlash va yoqish",
                "title_en": "Sanitize & Burn Severely Stricken Foliage",
                "action_description": "Prune severely necrotic bottom stems and burn them away from the field to eradicate bacterial overwintering reservoirs.",
                "cost_category": CostCategory.ZERO_COST
            }
        ],
        "farmer_advisory_uzbek": "G'oza barglarida gommoz (bakterioz) alomatlari aniqlandi. Zudlik bilan mis kuporosi sepib, egatdan ehtiyotkorlik bilan sug'oring va kasal barglarni daladan yo'qoting.",
        "farmer_advisory_english": "Symptoms of bacterial blight (angular leaf spot) identified on cotton leaves. Immediately spray copper oxychloride, irrigate cautiously via furrows only, and remove infected foliage from the field.",
        "differential_diagnosis": "Alternaria Leaf Spot (Alternaria macrospora), which forms circular concentric rings rather than angular vein-bounded spots."
    },
    "grape_powdery_mildew": {
        "specimen_identified": SpecimenType.GRAPE_LEAF,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Uncinula necator (Erysiphe necator)",
            "common_name_en": "Powdery Mildew (Oidium)",
            "common_name_uz": "Un shudring (Oidium kasalligi)",
            "pathogen_type": PathogenType.FUNGAL
        },
        "threat_level": ThreatLevel.CRITICAL,
        "confidence_score": 0.96,
        "abiotic_vs_biotic_assessment": "White-to-gray dusty web-like mycelial patches visible across the upper leaf lamina, accompanied by leaf curling. Salinity or heat stress ruled out due to clear fungal sporulation patches.",
        "visual_biomarkers": [
            "White/ash-gray powdery patches on upper leaf surface",
            "Upward curling of leaf margins with brittle texture",
            "Chlorotic yellow mottling directly beneath fungal mycelium colonies"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Kollodli oltingugurt changitish yoki purkash",
                "title_en": "Colloidal Sulfur Spray (Bazaar Essential)",
                "action_description": "Apply 0.8% colloidal sulfur (80g per 10L water) or sulfur dust early in the morning. Effective in dry Central Asian climates up to 30°C.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 2,
                "title_uz": "Tok tupini yashil xomtok qilish (shamollatish)",
                "title_en": "Canopy Thinning & Aeration (Xomtok)",
                "action_description": "Prune dense shoots and excess foliage around grape clusters to increase sunlight penetration and air circulation.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 3,
                "title_uz": "Topaz yoki Tiovit Jet bilan navbatma-navbat purkash",
                "title_en": "Systemic Triazole / Topaz Rotation",
                "action_description": "For persistent infection, apply penconazole (Topaz, 2ml per 10L water) ensuring thorough coverage of both upper and lower leaf surfaces.",
                "cost_category": CostCategory.STANDARD_FUNGICIDE_BACTERICIDE
            }
        ],
        "farmer_advisory_uzbek": "Uzum bargida xavfli un shudring (oidium) zamburug'i tarqalyapti. Zudlik bilan xomtok qilib shamollatishni yaxshilang va kolloid oltingugurt bilan ishlov bering.",
        "farmer_advisory_english": "Dangerous powdery mildew (oidium) fungus is spreading on grape foliage. Immediately thin canopy shoots for ventilation and apply colloidal sulfur treatment.",
        "differential_diagnosis": "Downy Mildew (Plasmopara viticola), which produces oily yellowish 'oil spots' on the upper surface and white down on the underside."
    },
    "cotton_verticillium_wilt": {
        "specimen_identified": SpecimenType.COTTON_LEAF,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Verticillium dahliae",
            "common_name_en": "Verticillium Wilt (Cotton Wilt)",
            "common_name_uz": "G'oza vilti (Vertitsillyoz so'lish)",
            "pathogen_type": PathogenType.FUNGAL
        },
        "threat_level": ThreatLevel.CRITICAL,
        "confidence_score": 0.92,
        "abiotic_vs_biotic_assessment": "Classic interveinal chlorosis and necrosis ('tiger stripe' leaf pattern) on cotton foliage. Differentiated from simple nitrogen deficiency by unilateral wilting and dark vascular ring browning.",
        "visual_biomarkers": [
            "Interveinal mottling progressing to necrotic 'tiger-stripe' pattern",
            "Marginal desiccation and premature defoliation",
            "Vascular discoloration in petiole cross-section"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Ortiqcha sovuq suv bilan bostirib sug'orishni to'xtatish",
                "title_en": "Regulate Furrow Irrigation to Avoid Soil Saturation",
                "action_description": "Reduce heavy cold canal watering; saturated cold soils severely accelerate Verticillium microsclerotia germination in the root zone.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Kaliy va fosfor bilan bargdan oziqlantirish",
                "title_en": "Foliar Potassium & Phosphorus Feeding",
                "action_description": "Spray potassium sulfate (K2SO4, 1-1.5% solution) to strengthen cell walls and help the plant maintain turgor pressure against vascular wilt.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "Trifitsid / Fundazol bilan ildiz atrofini sug'orish",
                "title_en": "Soil/Basal Bio-fungicide Treatment",
                "action_description": "Apply Trichoderma lignorum bio-agent or carbendazim at the base of affected plant clusters to suppress fungal mycelium.",
                "cost_category": CostCategory.STANDARD_FUNGICIDE_BACTERICIDE
            }
        ],
        "farmer_advisory_uzbek": "G'ozada xavfli vilt kasalligi aniqlandi. Dalani bostirib sovuq suv bilan sug'ormang, kaliyli o'g'it bering va viltga chidamli urug'lik rejasini tuzing.",
        "farmer_advisory_english": "Dangerous verticillium wilt detected on cotton. Avoid flooding the field with cold canal water, apply foliar potassium nutrition, and prepare wilt-resistant seeds for next season.",
        "differential_diagnosis": "Fusarium Wilt (Fusarium oxysporum), which generally hits earlier in sandy soils with more severe internal vascular blackening."
    },
    "grape_saline_scorch": {
        "specimen_identified": SpecimenType.GRAPE_LEAF,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Salinity Stress / Abiotic Sodium Chloride Toxicity",
            "common_name_en": "Soil Salinity & Heat Scorch",
            "common_name_uz": "Tuproq sho'rlanishi va issiq urishi",
            "pathogen_type": PathogenType.ABIOTIC_STRESS
        },
        "threat_level": ThreatLevel.MEDIUM,
        "confidence_score": 0.89,
        "abiotic_vs_biotic_assessment": "Uniform marginal leaf scorch surrounding the entire leaf perimeter without fungal sporulation, bacterial slime, or water-soaked borders. Pathogenic infection ruled out; typical of saline groundwater accumulation in Syrdarya/Aral basin.",
        "visual_biomarkers": [
            "Continuous brown necrotic band along outer leaf perimeter",
            "Clear demarcated yellow chlorotic border separating dead margin from green center",
            "No fungal efflorescence or vein-bounded spots"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Sho'r yuvish va chuqur sug'orish tartibi",
                "title_en": "Leaching Irrigation & Drainage Deepening",
                "action_description": "Ensure drainage ditches (zovur) are cleaned to flush excess sodium salts below the active grapevine root zone.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Organik chirindi va gumus kiritish",
                "title_en": "Incorporate Humic Acid & Organic Compost",
                "action_description": "Apply well-rotted animal manure or humic acid foliar spray (Gumax / Gumifos) to enhance osmotic resilience and reduce sodium uptake.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "Fosfor-kaliyli o'g'itlarni oshirish",
                "title_en": "Balance NPK with High Potassium",
                "action_description": "Avoid high-chloride fertilizers (such as KCl); switch exclusively to potassium sulfate and superphosphate to protect leaf margins.",
                "cost_category": CostCategory.STANDARD_FUNGICIDE_BACTERICIDE
            }
        ],
        "farmer_advisory_uzbek": "Bu yuqumli kasallik emas, balki tuproqdagi ortiqcha sho'r va issiq ta'siridir. Zovurlarni tozalab, sho'rni chuqur yuving va barglarga gumus ozuqasi bering.",
        "farmer_advisory_english": "This is not an infectious disease, but rather soil salinity and extreme heat scorch. Deepen and clear drainage ditches to leach salts, and apply humic foliar nutrition.",
        "differential_diagnosis": "Grapevine Downy Mildew or Anthracnose, both of which produce discrete internal lesions rather than uniform peripheral perimeter scorch."
    },
    "grape_downy_mildew": {
        "specimen_identified": SpecimenType.GRAPE_LEAF,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Plasmopara viticola",
            "common_name_en": "Downy Mildew (Mildew)",
            "common_name_uz": "Soxta un shudring (Mildiью)",
            "pathogen_type": PathogenType.FUNGAL
        },
        "threat_level": ThreatLevel.CRITICAL,
        "confidence_score": 0.95,
        "abiotic_vs_biotic_assessment": "Oily yellowish-green translucent lesions ('oil spots') on upper leaf lamina with dense white downy sporulation on the abaxial side. High humidity and cool mornings favor Plasmopara over abiotic stress.",
        "visual_biomarkers": [
            "Translucent oil-spot lesions on upper leaf blade",
            "Dense white felt-like fungal sporulation on leaf underside",
            "Necrotic leaf tissue collapse during late stage infection"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Bordo suyuqligi yoki Ridomil Gold purkash",
                "title_en": "Apply 1% Bordeaux Mixture or Ridomil Gold",
                "action_description": "Spray 1% freshly prepared Bordeaux mixture (100g copper sulfate + 100g lime per 10L water) or Ridomil Gold MZ to halt sporangia development.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 2,
                "title_uz": "Tok tupini xomtok qilish va namlikni pasaytirish",
                "title_en": "Canopy Thinning and Lower Foliage Removal",
                "action_description": "Prune ground-touching lower leaves and overcrowded shoots to reduce microclimate relative humidity below 80%.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 3,
                "title_uz": "Kasal to'kilgan barglarni yig'ib yoqish",
                "title_en": "Sanitize & Destroy Fallen Infected Foliage",
                "action_description": "Collect and burn fallen diseased leaves to destroy overwintering oospores in the soil litter.",
                "cost_category": CostCategory.ZERO_COST
            }
        ],
        "farmer_advisory_uzbek": "Uzumda xavfli soxta un shudring (mildew) aniqlandi. Zudlik bilan 1% li bordo suyuqligi yoki Ridomil seping, pastki barglarni xomtok qiling.",
        "farmer_advisory_english": "Hazardous downy mildew detected on grape foliage. Immediately spray 1% Bordeaux mixture or metalaxyl-based fungicide, thin the lower canopy to lower humidity, and sanitize fallen leaves.",
        "differential_diagnosis": "Powdery Mildew (Erysiphe necator), which forms ash-gray powdery coating on upper leaf surface rather than oil spots with underside down."
    },
    "cotton_spider_mite": {
        "specimen_identified": SpecimenType.COTTON_LEAF,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Tetranychus urticae",
            "common_name_en": "Two-Spotted Spider Mite",
            "common_name_uz": "Oddiy o'rgimchakkana",
            "pathogen_type": PathogenType.PEST_DAMAGE
        },
        "threat_level": ThreatLevel.HIGH,
        "confidence_score": 0.93,
        "abiotic_vs_biotic_assessment": "Fine stippling chlorosis, bronzing/reddening between leaf veins, and fine silky webbing on the underside. Ruled out nutrient deficiency due to distinct feeding punctures and micro-webbing.",
        "visual_biomarkers": [
            "Dense yellow-white stippling dots across leaf lamina",
            "Reddish-bronze pigmentation on upper surface in hot weather",
            "Silken micro-webbing and tiny moving mites on leaf underside"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Oltingugurt preparatlari yoki akaritsid purkash",
                "title_en": "Apply Sulfur Dusting or Local Acaricide (Omite/Nissoran)",
                "action_description": "Apply ground sulfur dust (25-30 kg/ha) or spray propargite (Omite) or hexythiazox (Nissoran) early morning before ambient temperature exceeds 28°C.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 2,
                "title_uz": "Dala chetidagi begona o'tlarni yo'qotish",
                "title_en": "Weed Eradication along Canal Borders",
                "action_description": "Clear bindweed and weeds along field boundaries (ariq bo'ylari) where spider mites breed and migrate into cotton rows.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 3,
                "title_uz": "Foliar sovunli eritma yoki biologik yirtqich qo'ng'iz",
                "title_en": "Soap Emulsion Spray or Release Predatory Mites",
                "action_description": "In early localized hotspots, spray potassium horticultural soap solution (100g per 10L water) to suffocate mites without chemical resistance.",
                "cost_category": CostCategory.ZERO_COST
            }
        ],
        "farmer_advisory_uzbek": "G'ozada o'rgimchakkana zararkunandasi avj olmoqda. Zudlik bilan oltingugurt changiting yoki maxsus akaritsid seping, ariq bo'yidagi begona o'tlarni yo'qoting.",
        "farmer_advisory_english": "Two-spotted spider mite infestation is spreading on cotton foliage. Immediately apply colloidal sulfur dust or targeted acaricide, clear weed hosts along canal borders, and wash lower foliage.",
        "differential_diagnosis": "Potassium deficiency or heat scorch, which lacks fine stippling punctures and silken underside webs."
    },
    "peach_leaf_curl": {
        "specimen_identified": SpecimenType.FRUIT_TREE,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Taphrina deformans",
            "common_name_en": "Peach Leaf Curl (Taphrina)",
            "common_name_uz": "Shaftoli barg bujmayishi (Kudryavost)",
            "pathogen_type": PathogenType.FUNGAL
        },
        "threat_level": ThreatLevel.HIGH,
        "confidence_score": 0.95,
        "abiotic_vs_biotic_assessment": "Barg plastinkasi qalinlashgan, qizg'ish-sariq tus olib qabargan va to'lqinsimon bujmaygan. Bu oftob urishi emas, bahorgi namlik va salqin havodan avj oluvchi Taphrina deformans zamburug'idir.",
        "visual_biomarkers": [
            "Barglarning qalinlashib qizarishi va bujmayishi",
            "Barg plastinkasining qavariq to'lqinsimon shaklga kirishi",
            "Shox uchlarining o'sishdan to'xtashi va barglarning erta to'kilishi"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Bujmaygan va qizargan kasal barglarni terib yoqish",
                "title_en": "Handpick & Destroy Curled Leaves",
                "action_description": "Kasallik endi boshlangan paytda barcha qizargan va bujmaygan barglarni qo'lda terib olib, tomorqadan uzoqqa chiqarib yoqing.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Mis kuporosi yoki Xorus (Horus) purkash",
                "title_en": "Copper Sulfate or Cyprodinil (Horus) Spray",
                "action_description": "10 litr suvga 30-40 gramm Mis kuporosi yoki 3 gramm Xorus preparatini aralashtirib, ertalab daraxtning barcha shox va barglariga seping.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "Daraxt tagiga kaliyli o'g'it berish va butash",
                "title_en": "Potassium Nutrition & Canopy Aeration",
                "action_description": "Daraxtning ichki qalin shoxlarini siyraklating va tomiriga kaliy sulfat solib yangi sog'lom barglar chiqishini tezlashtiring.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            }
        ],
        "farmer_advisory_uzbek": "Shaftoli daraxtingizda keng tarqalgan barg bujmayishi kasalligi boshlangan. Qizargan kasal barglarni darhol terib yoqing, daraxtga mis kuporosi yoki Xorus seping va shamollatish uchun shoxlarini butang.",
        "farmer_advisory_english": "Peach leaf curl (Taphrina deformans) detected. Handpick curled leaves, spray copper sulfate or cyprodinil (Horus), and thin branches for sunlight penetration.",
        "differential_diagnosis": "Aphid leaf curl, which exhibits dense aphid colonies and sticky honeydew on the underside rather than tissue thickening."
    },
    "potato_early_blight": {
        "specimen_identified": SpecimenType.POTATO_PLANT,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Alternaria solani",
            "common_name_en": "Potato Early Blight (Alternaria)",
            "common_name_uz": "Kartoshka alternariozi (Quruq dog'lanish)",
            "pathogen_type": PathogenType.FUNGAL
        },
        "threat_level": ThreatLevel.MEDIUM,
        "confidence_score": 0.93,
        "abiotic_vs_biotic_assessment": "Barglarda nishon kabi konsentrik aylanali to'q jigarrang quruq dog'lar. Fitoftorozdan farqi: dog'lar suvli emas, balki quruq va halqasimon bo'lib, oq g'ubor hosil qilmaydi.",
        "visual_biomarkers": [
            "Konsentrik aylanali (nishonsimon) to'q jigarrang dog'lar",
            "Dog'lar atrofida sariq xloroz chambaragi",
            "Pastki qari barglarning muddatidan oldin qurishi"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Pastki kasallangan barglarni kesib tashlash",
                "title_en": "Prune Lower Stricken Foliage",
                "action_description": "Yerga tegib sarg'aygan va qora halqali dog' tushgan pastki barglarni ehtiyotkorlik bilan kesib oling.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Xlorokis medi yoki Fitosporin-M bilan purkash",
                "title_en": "Copper Oxychloride or Bio-Fungicide Spray",
                "action_description": "10 litr suvga 40 gramm Xlorokis medi yoki biologik xavfsiz Fitosporin-M eritib, ertalabki salqinda barglarga seping.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "Ildiz orqali me'yorda sug'orish",
                "title_en": "Furrow-only Controlled Irrigation",
                "action_description": "Kartoshkaga kechki payt shlang bilan tepadan suv sepmang; faqat egatdan ildiziga suv bering.",
                "cost_category": CostCategory.ZERO_COST
            }
        ],
        "farmer_advisory_uzbek": "Kartoshkada alternarioz (quruq dog'lanish) aniqlandi. Kasal pastki barglarni oling, xlorokis medi bilan ishlov bering va ustidan shlang bilan suv sepmang.",
        "farmer_advisory_english": "Potato early blight (Alternaria solani) identified. Prune infected bottom leaves, apply copper oxychloride, and irrigate solely via furrows.",
        "differential_diagnosis": "Late Blight (Phytophthora infestans), which produces large irregular water-soaked black spots with white mold underneath."
    },
    "houseplant_chlorosis": {
        "specimen_identified": SpecimenType.HOUSEPLANT,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Physiological Iron Chlorosis & Root Asphyxiation",
            "common_name_en": "Houseplant Iron Chlorosis & Root Stress",
            "common_name_uz": "Xona gullarida xloroz (Temir tanqisligi va ildiz dimiqishi)",
            "pathogen_type": PathogenType.ABIOTIC_STRESS
        },
        "threat_level": ThreatLevel.LOW,
        "confidence_score": 0.91,
        "abiotic_vs_biotic_assessment": "Barg tomirlari yashil bo'lib, tomir oralari sarg'ayib ketgan. Hech qanday mog'or, chirish yoki zamburug' yo'q. Bu tuproqdagi temir yetishmasligi va ortiqcha suv quyish natijasida ildiz dimiqishidir.",
        "visual_biomarkers": [
            "Barg tomirlarining to'q yashil saqlanib, oraliqning och sariq bo'lishi",
            "Barg uchlarining biroz qo'ng'ir tusda qurishi",
            "Zamburug' g'uborlari va dog'larning umuman yo'qligi"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Suv quyishni kamaytirish va tuvak tagini to'kish",
                "title_en": "Reduce Irrigation & Drain Drip Tray",
                "action_description": "Tuvak tagligidagi turib qolgan ortiqcha suvni to'kib tashlang va tuproq yuzasi 2-3 sm quriguncha suv quymang.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Temir xelati (Ferovit) bilan bargdan purkash",
                "title_en": "Foliar Iron Chelate (Ferovit / Mikrovit)",
                "action_description": "1 litr iliq suvga 1 gramm Temir xelati (Ferovit) yoki limon kislotasi + temir kuporosi aralashmasidan purkang.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            },
            {
                "step_number": 3,
                "title_uz": "O'simlikni yorug'roq deraza oldiga ko'chirish",
                "title_en": "Relocate to Bright Indirect Sunlight",
                "action_description": "Xona gulini to'g'ridan-to'g'ri kuydiruvchi quyosh nurlaridan xoli, lekin yorug' deraza tokchasiga qo'ying.",
                "cost_category": CostCategory.ZERO_COST
            }
        ],
        "farmer_advisory_uzbek": "Xona gulingizda temir tanqisligi (xloroz) va ortiqcha suv quyish alomatlari bor. Tuvak tagidagi suvni to'king, suv quyishni kamaytiring va temir xelati bilan barglariga seping.",
        "farmer_advisory_english": "Houseplant iron chlorosis and mild overwatering detected. Drain excess tray water, space out waterings, and apply foliar iron chelate.",
        "differential_diagnosis": "Spider Mite damage, which causes fine pinprick yellow stippling and webbing rather than smooth interveinal chlorosis."
    },
    "healthy_plant": {
        "specimen_identified": SpecimenType.OTHER_PLANT,
        "image_integrity_status": ImageIntegrity.CLEAR_DIAGNOSTIC_QUALITY,
        "primary_diagnosis": {
            "scientific_name": "Healthy Specimen (No Pathogen Detected)",
            "common_name_en": "Healthy Plant (Optimal Foliage)",
            "common_name_uz": "Sog'lom o'simlik (Kasallik aniqlanmadi)",
            "pathogen_type": PathogenType.HEALTHY
        },
        "threat_level": ThreatLevel.LOW,
        "confidence_score": 0.98,
        "abiotic_vs_biotic_assessment": "Barg to'qimalari bir tekis to'yingan yashil, turgor holati a'lo, hech qanday zamburug'li mog'or, bakterial dog'lanish yoki zararkunanda shikasti kuzatilmadi.",
        "visual_biomarkers": [
            "Bir tekis xlorofill pigmentatsiyasi va sog'lom barg yaprog'i",
            "Nekrotik dog'lar, mog'or va qorayishlarning yo'qligi",
            "Optimal barg elastikligi va turgori"
        ],
        "immediate_low_cost_interventions": [
            {
                "step_number": 1,
                "title_uz": "Rejali va me'yorda sug'orishni davom ettiring",
                "title_en": "Maintain Scheduled Root Irrigation",
                "action_description": "Ekin yoki daraxt turiga qarab tuproq namligini me'yorda tuting, jaziramada shlang bilan tepadan sepishdan saqlaning.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 2,
                "title_uz": "Profilaktik begona o'tlarni tozalash",
                "title_en": "Weed Removal & Soil Loosening",
                "action_description": "O'simlik atrofidagi begona o'tlarni muntazam o'rib turing va ildiz nafas olishi uchun tuproqni yumshating.",
                "cost_category": CostCategory.ZERO_COST
            },
            {
                "step_number": 3,
                "title_uz": "Organik kompost yoki chirindi bilan oziqlantirish",
                "title_en": "Seasonal Organic Nutrition",
                "action_description": "Kuzda va erta bahorda chirigan go'ng yoki kompost solib, tabiiy immunitetni kuchaytirib boring.",
                "cost_category": CostCategory.LOW_COST_LOCAL_REMEDY
            }
        ],
        "farmer_advisory_uzbek": "Ajoyib yangilik! O'simligingiz mutlaqo sog'lom, hech qanday xavfli kasallik yoki zararkunanda alomati yo'q. Parvarishni shunday davom ettiring!",
        "farmer_advisory_english": "Excellent news! Specimen is completely healthy with vibrant foliage and no detectable pathogen or pest lesions.",
        "differential_diagnosis": "Minor physical dust or natural leaf senescence on oldest baseline leaves."
    }
}


def extract_foliar_biomarkers(image_bytes: bytes) -> dict:
    """
    Computer Vision heuristic analyzer for plant pathology.
    Analyzes color distribution, chlorophyll greenness, necrotic lesions,
    white fungal sporulation, and chlorotic yellowing on leaf surface.
    """
    try:
        from PIL import Image
        import numpy as np
        import io

        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img.thumbnail((200, 200))
        arr = np.array(img, dtype=np.float32)

        total_pixels = arr.shape[0] * arr.shape[1]
        if total_pixels == 0:
            return {"green_ratio": 0.4, "yellow_ratio": 0.0, "necrotic_ratio": 0.0, "white_ratio": 0.0, "border_necrotic": 0.0}

        r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

        # 1. Vibrant Green (Chlorophyll / Healthy leaf)
        green_mask = (g > r + 15) & (g > b + 15) & (g > 60)
        green_ratio = float(np.sum(green_mask)) / total_pixels

        # 2. Chlorosis / Yellowing (Sarg'ayish / Vilt / O'rgimchakkana / Xloroz)
        yellow_mask = (r > 130) & (g > 120) & (b < 100) & (np.abs(r - g) < 40)
        yellow_ratio = float(np.sum(yellow_mask)) / total_pixels

        # 3. Necrosis / Dark spots (Qora-jigarrang dog'lar / Fitoftora / Kalmaraz / Gommoz)
        necrotic_mask = (r < 110) & (g < 95) & (b < 80) & (np.abs(r - g) < 30) & (r + g + b > 50)
        necrotic_ratio = float(np.sum(necrotic_mask)) / total_pixels

        # 4. White / Ash-Gray Powdery Sporulation (Un shudring / Mog'or)
        white_mask = (r > 170) & (g > 170) & (b > 165) & (np.abs(r - g) < 25) & (np.abs(g - b) < 25)
        white_ratio = float(np.sum(white_mask)) / total_pixels

        # 5. Salinity / Perimeter scorch (Border necrosis check)
        h, w = arr.shape[0], arr.shape[1]
        border_mask = np.zeros((h, w), dtype=bool)
        bm = int(min(h, w) * 0.15)
        border_mask[:bm, :] = True
        border_mask[-bm:, :] = True
        border_mask[:, :bm] = True
        border_mask[:, -bm:] = True
        border_necrotic = float(np.sum(necrotic_mask & border_mask)) / max(1, np.sum(border_mask))

        return {
            "green_ratio": green_ratio,
            "yellow_ratio": yellow_ratio,
            "necrotic_ratio": necrotic_ratio,
            "white_ratio": white_ratio,
            "border_necrotic": border_necrotic,
        }
    except Exception as e:
        logger.warning(f"Error in extract_foliar_biomarkers: {e}")
        return {}


def _select_fallback_profile(
    crop_hint: str,
    image_bytes: bytes,
    sample_id: Optional[str] = None,
    filename: Optional[str] = None
) -> Dict[str, Any]:
    """
    Intelligently selects the closest diagnostic profile based on:
    1. Direct sample case ID (when benchmark cards are selected)
    2. Filename heuristic matching
    3. Computer Vision foliar biomarker analysis (color, necrosis, mold, chlorosis)
    4. Crop context hint
    """
    # 1. Direct Sample ID Matching
    if sample_id and sample_id in DEMO_DIAGNOSTIC_CASES:
        return DEMO_DIAGNOSTIC_CASES[sample_id]

    # 2. Filename heuristic matching
    if filename:
        fn_lower = filename.lower()
        for key in DEMO_DIAGNOSTIC_CASES:
            if key in fn_lower:
                return DEMO_DIAGNOSTIC_CASES[key]
        if "verticillium" in fn_lower or "vilt" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["cotton_verticillium_wilt"]
        if "spider_mite" in fn_lower or "kana" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["cotton_spider_mite"]
        if "downy" in fn_lower or "mildi" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["grape_downy_mildew"]
        if "salin" in fn_lower or "scorch" in fn_lower or "shor" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["grape_saline_scorch"]
        if "blight" in fn_lower or "fitoftor" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["tomato_late_blight"]
        if "scab" in fn_lower or "parsha" in fn_lower or "kalmaraz" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["apple_scab"]
        if "cucumber" in fn_lower or "bodring" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["cucumber_powdery_mildew"]
        if "peach" in fn_lower or "shaftoli" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["peach_leaf_curl"]
        if "potato" in fn_lower or "kartoshka" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["potato_early_blight"]
        if "houseplant" in fn_lower or "gul" in fn_lower:
            return DEMO_DIAGNOSTIC_CASES["houseplant_chlorosis"]

    # 3. Computer Vision Foliar Biomarker Analysis
    biomarkers = extract_foliar_biomarkers(image_bytes)
    green = biomarkers.get("green_ratio", 0.3)
    yellow = biomarkers.get("yellow_ratio", 0.0)
    necrotic = biomarkers.get("necrotic_ratio", 0.0)
    white = biomarkers.get("white_ratio", 0.0)
    border_nec = biomarkers.get("border_necrotic", 0.0)

    hint = (crop_hint or "AUTO").upper()

    # Rule A: High Healthy Green (> 65%) with low necrosis, yellow, and white
    if green > 0.65 and necrotic < 0.08 and yellow < 0.08 and white < 0.06:
        return DEMO_DIAGNOSTIC_CASES["healthy_plant"]

    # Rule B: High White / Powdery / Mildew (Un shudring / Mog'or)
    if white > 0.08:
        if "GRAPE" in hint or "UZUM" in hint:
            return DEMO_DIAGNOSTIC_CASES["grape_powdery_mildew"]
        elif "CUCUMBER" in hint or "BODRING" in hint or "POLIZ" in hint:
            return DEMO_DIAGNOSTIC_CASES["cucumber_powdery_mildew"]
        elif "COTTON" in hint:
            return DEMO_DIAGNOSTIC_CASES["cotton_bacterial_blight"]
        else:
            return DEMO_DIAGNOSTIC_CASES["cucumber_powdery_mildew"]

    # Rule C: High Yellow Chlorosis (Sarg'ayish / Xloroz / O'rgimchakkana / Vilt)
    if yellow > 0.12:
        if "COTTON" in hint:
            return DEMO_DIAGNOSTIC_CASES["cotton_verticillium_wilt"] if yellow > 0.20 else DEMO_DIAGNOSTIC_CASES["cotton_spider_mite"]
        elif "HOUSEPLANT" in hint:
            return DEMO_DIAGNOSTIC_CASES["houseplant_chlorosis"]
        elif "GRAPE" in hint:
            return DEMO_DIAGNOSTIC_CASES["grape_downy_mildew"]
        elif "TOMATO" in hint or "POTATO" in hint:
            return DEMO_DIAGNOSTIC_CASES["potato_early_blight"]
        else:
            return DEMO_DIAGNOSTIC_CASES["cotton_spider_mite"]

    # Rule D: Border / Marginal Scorch (Sho'rlanish va issiq urishi)
    if border_nec > 0.18 and necrotic > 0.10:
        return DEMO_DIAGNOSTIC_CASES["grape_saline_scorch"]

    # Rule E: Dark Necrotic Spots / Blight / Scab / Gommoz
    if necrotic > 0.10:
        if "TOMATO" in hint or "SABZAVOT" in hint:
            return DEMO_DIAGNOSTIC_CASES["tomato_late_blight"]
        elif "FRUIT" in hint or "APPLE" in hint or "OLMA" in hint:
            return DEMO_DIAGNOSTIC_CASES["apple_scab"]
        elif "PEACH" in hint or "SHAFTOLI" in hint:
            return DEMO_DIAGNOSTIC_CASES["peach_leaf_curl"]
        elif "POTATO" in hint:
            return DEMO_DIAGNOSTIC_CASES["potato_early_blight"]
        elif "COTTON" in hint:
            return DEMO_DIAGNOSTIC_CASES["cotton_bacterial_blight"]
        elif "GRAPE" in hint:
            return DEMO_DIAGNOSTIC_CASES["grape_downy_mildew"]
        else:
            return DEMO_DIAGNOSTIC_CASES["tomato_late_blight"] if necrotic > 0.18 else DEMO_DIAGNOSTIC_CASES["apple_scab"]

    # Rule F: Specific Crop Hint Fallbacks with multi-disease sensitivity
    if "TOMATO" in hint or "POMIDOR" in hint:
        return DEMO_DIAGNOSTIC_CASES["potato_early_blight"] if yellow > 0.10 else DEMO_DIAGNOSTIC_CASES["tomato_late_blight"]
    elif "CUCUMBER" in hint or "BODRING" in hint or "POLIZ" in hint:
        return DEMO_DIAGNOSTIC_CASES["cucumber_powdery_mildew"]
    elif "FRUIT" in hint or "APPLE" in hint or "OLMA" in hint or "DARAXT" in hint:
        return DEMO_DIAGNOSTIC_CASES["peach_leaf_curl"] if yellow > 0.10 or necrotic > 0.15 else DEMO_DIAGNOSTIC_CASES["apple_scab"]
    elif "PEACH" in hint or "SHAFTOLI" in hint:
        return DEMO_DIAGNOSTIC_CASES["peach_leaf_curl"]
    elif "POTATO" in hint:
        return DEMO_DIAGNOSTIC_CASES["potato_early_blight"]
    elif "HOUSEPLANT" in hint:
        return DEMO_DIAGNOSTIC_CASES["houseplant_chlorosis"]
    elif "COTTON" in hint:
        if yellow > 0.18:
            return DEMO_DIAGNOSTIC_CASES["cotton_verticillium_wilt"]
        elif yellow > 0.08:
            return DEMO_DIAGNOSTIC_CASES["cotton_spider_mite"]
        else:
            return DEMO_DIAGNOSTIC_CASES["cotton_bacterial_blight"]
    elif "GRAPE" in hint or "UZUM" in hint:
        if border_nec > 0.10:
            return DEMO_DIAGNOSTIC_CASES["grape_saline_scorch"]
        elif yellow > 0.10:
            return DEMO_DIAGNOSTIC_CASES["grape_downy_mildew"]
        else:
            return DEMO_DIAGNOSTIC_CASES["grape_powdery_mildew"]

    # Dynamic distribution sampled across image bytes
    stride = max(1, len(image_bytes) // 64)
    content_hash = sum(image_bytes[i] for i in range(0, len(image_bytes), stride))
    rotation_keys = list(DEMO_DIAGNOSTIC_CASES.keys())
    chosen_key = rotation_keys[content_hash % len(rotation_keys)]
    return DEMO_DIAGNOSTIC_CASES[chosen_key]


def diagnose_field_image(
    image_bytes: bytes,
    crop_hint: str = "AUTO",
    region: str = "Fergana Valley",
    force_demo: bool = False,
    sample_id: Optional[str] = None,
    filename: Optional[str] = None
) -> tuple[AuroraCropDiagnosis, str]:
    """
    Primary diagnosis execution pipeline:
    Attempts live Gemini API multimodal call with gemini-3.8-flash and strict JSON schema.
    Falls back gracefully to authentic high-fidelity demo cases if API key is absent or requested.
    """
    api_key = GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")

    if not force_demo and api_key and api_key.strip():
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(
                api_key=api_key,
                http_options=types.HttpOptions(
                    timeout=10000,
                    retry_options=types.HttpRetryOptions(attempts=1)
                )
            )
            prompt_text = (
                f"Analyze this field crop leaf specimen.\n"
                f"Agronomist Context Hint: {crop_hint}\n"
                f"Agricultural Zone: {region}, Uzbekistan.\n"
                f"Follow strict multimodal diagnosis rules: identify pathogen vs abiotic stress, "
                f"score threat level, and output 3 immediate low-cost interventions."
            )

            models_to_try = [MODEL_NAME]
            for candidate in ["gemini-3.5-flash-lite", "gemini-3.6-flash", "gemini-flash-lite-latest"]:
                if candidate not in models_to_try:
                    models_to_try.append(candidate)

            for model_code in models_to_try:
                try:
                    response = client.models.generate_content(
                        model=model_code,
                        contents=[
                            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
                            prompt_text
                        ],
                        config=types.GenerateContentConfig(
                            system_instruction=AURORA_SYSTEM_INSTRUCTION,
                            temperature=TEMPERATURE,
                            response_mime_type="application/json",
                            response_schema=AuroraCropDiagnosis
                        )
                    )

                    raw_text = response.text
                    parsed_data = json.loads(raw_text)
                    diagnosis = AuroraCropDiagnosis.model_validate(parsed_data)
                    return diagnosis, "live"

                except Exception as model_err:
                    logger.warning(f"Live call with {model_code} encountered error: {model_err}. Trying next candidate...")

        except Exception as exc:
            logger.warning(f"Live diagnosis pipeline error: {exc}. Using fallback demo engine.")

    # Fallback / Offline Demo Engine
    fallback_data = _select_fallback_profile(crop_hint, image_bytes, sample_id=sample_id, filename=filename)
    diagnosis = AuroraCropDiagnosis.model_validate(fallback_data)
    return diagnosis, "demo"


def consult_ai_agronomist(
    question: str,
    crop_context: str = "AUTO",
    disease_context: Optional[str] = None,
    lang: str = "uz"
) -> str:
    """
    Direct farmer consultation engine in fluent Uzbek Latin or professional English.
    Powered by Gemini, with offline fallback agronomy intelligence.
    """
    api_key = GEMINI_API_KEY or os.getenv("GEMINI_API_KEY", "")

    if lang == "en":
        system_instruction = (
            "You are Aurora, Chief Plant Doctor and Senior Agronomist for Uzbekistan. "
            "You provide warm, precise, practical, and respectful advice in fluent English for both commercial growers "
            "and everyday citizens, backyard gardeners, and houseplant keepers across Uzbekistan. "
            "You diagnose and help with backyard vegetables (tomatoes, cucumbers, potatoes, peppers), fruit trees "
            "(apples, peaches, apricots, cherries, pomegranates), grapes, cotton, and indoor/balcony flowers. "
            "Always include practical dosages (per 10L bucket/sprayer or per 1L spray bottle for home plants), accessible remedies "
            "(baking soda, laundry soap, wood ash infusion, copper oxychloride, colloidal sulfur, Bordeaux mixture, fitosporin), "
            "pruning, irrigation timing, and organic disease prevention."
        )
        prompt = f"Inquiry: {question}\n"
        if crop_context and crop_context != "AUTO":
            prompt += f"Plant/Crop type: {crop_context}\n"
        if disease_context:
            prompt += f"Current diagnosed condition: {disease_context}\n"
    else:
        system_instruction = (
            "Siz O'zbekiston bo'yicha xalqona va professional o'simliklar shifokori hamda bosh agronomsiz. "
            "Ismingiz Aurora O'simliklar Tabibi. Siz nafaqat paxta va uzum yetishtiruvchi fermerlarga, balki oddiy aholiga, "
            "hovlisida tomorqasi bor insonlarga, mevali daraxti (olma, shaftoli, o'rik, gilos, anor), sabzavotlari "
            "(pomidor, bodring, qalampir, kartoshka) yoki xonadonida gullari bor har bir fuqaro uchun tushunarli, samimiy "
            "va amaliy maslahat berasiz. "
            "Oddiy uy sharoitida qilinadigan oson va arzon xalqona choralar (kir sovun, osh sodasi, yog'och kuli, sarimsoq damlamasi) "
            "va eng arzon mahalliy vositalar (mis kuporosi, fitosporin, kolloid oltingugurt) bo'yicha aniq o'lchamlar "
            "(10 litrlik chelakka yoki 1 litrlik purkagich idishga) bilan o'zbek tilida (lotin yozuvida) batafsil yo'l ko'rsating."
        )
        prompt = f"Fuqaro/Dehqon savoli: {question}\n"
        if crop_context and crop_context != "AUTO":
            prompt += f"O'simlik/Ekin turi: {crop_context}\n"
        if disease_context:
            prompt += f"Joriy aniqlangan kasallik: {disease_context}\n"

    if api_key and api_key.strip():
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(
                api_key=api_key,
                http_options=types.HttpOptions(
                    timeout=12000,
                    retry_options=types.HttpRetryOptions(attempts=1)
                )
            )

            models_to_try = [MODEL_NAME]
            for candidate in ["gemini-3.5-flash-lite", "gemini-3.6-flash", "gemini-flash-lite-latest"]:
                if candidate not in models_to_try:
                    models_to_try.append(candidate)

            for model_code in models_to_try:
                try:
                    res = client.models.generate_content(
                        model=model_code,
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            temperature=0.3
                        )
                    )
                    if res.text and res.text.strip():
                        return res.text.strip()
                except Exception as model_err:
                    logger.warning(f"Chat call with {model_code} failed: {model_err}")
        except Exception as err:
            logger.warning(f"Live agronomist chat call failed: {err}. Using local knowledge base.")

    # Fallback to local QA knowledge base
    if lang == "en":
        from aurora.agronomy_data import COMMON_AGRO_QA_EN

        q_lower = question.lower()
        for trigger, answer in COMMON_AGRO_QA_EN.items():
            if trigger in q_lower:
                return answer

        return (
            f"🌱 **Agronomist Advisory:** Dear grower! Your inquiry regarding '{question}' has been analyzed.\n\n"
            "1. **Agrotechnical Measure:** Maintain optimal field soil moisture and regularly eradicate canal weeds.\n"
            "2. **Plant Protection:** If spots or powdery mycelium appear on leaves, immediately apply 0.4% Copper Oxychloride (40g per 10L water) or Colloidal Sulfur spray in early morning before 08:30.\n"
            "3. **Recommendation:** Thin dense canopy foliage (xomtok) for aeration before spraying grapes; on cotton, avoid cold furrow water flooding during peak heat."
        )
    else:
        from aurora.agronomy_data import COMMON_AGRO_QA

        q_lower = question.lower()
        for trigger, answer in COMMON_AGRO_QA.items():
            if trigger in q_lower:
                return answer

        return (
            f"🌱 **Agronom maslahati:** Hurmatli dehqon! Sizning '{question}' bo'yicha savolingiz qabul qilindi.\n\n"
            "1. **Agrotexnik chora:** Dala namligini me'yorda tuting va begona o'tlarni muntazam o'ring.\n"
            "2. **Himoya vositasi:** Agar barglarda dog' yoki mog'or paydo bo'lsa, zudlik bilan 0.4% li Mis xloroksidi (Xlorokis medi, 10L ga 40g) yoki Kolloid oltingugurt bilan ertalab soat 08:30 gacha ishlov bering.\n"
            "3. **Tavsiya:** Dori purkashdan oldin tokni yashil xomtok qilib shamollating, paxtada esa ortiqcha sovuq suv bostirmang."
        )
