"""
Agronomy Knowledge Base & Regional Phytosanitary Monitoring for Uzbekistan.
Contains comprehensive Uzbek and English foliar disease catalog, 14-region monitoring data,
and common agronomist Q&A knowledge base.
"""
from typing import List, Dict, Any

# Complete Universal Disease & Pest Catalog for Uzbekistan (Vegetables, Fruit Trees, Grapes & Cotton)
DISEASE_CATALOG: List[Dict[str, Any]] = [
    {
        "id": "tomato_late_blight",
        "crop": "Pomidor & Sabzavotlar",
        "crop_en": "Tomato & Backyard Vegetables",
        "name_uz": "Pomidor fitoftorozi (Qorayish kasalligi)",
        "name_en": "Tomato Late Blight (Phytophthora)",
        "scientific_name": "Phytophthora infestans",
        "pathogen_type": "Zamburug'li",
        "pathogen_type_en": "Fungal",
        "threat_level": "HIGH",
        "image_url": "/images/tomato_late_blight.jpg",
        "visual_signs_uz": "Barg, poya va yashil pomidor mevasida qoramtir-jigarrang, suvli yirik dog'lar. Nam havoda barg tagida oqish zamburug' g'ubori ko'rinadi.",
        "visual_signs_en": "Dark brown-black water-soaked lesions spreading across leaves, stems and green fruits with white sporulation on undersides.",
        "causes_uz": "Sernam havo, kechki va kunduzgi haroratning keskin farqi, pomidorni ustidan sepib sug'orish.",
        "causes_en": "High humidity, fluctuating day/night temperatures, overhead hose watering.",
        "calendar_season_uz": "Iyun — Sentyabr oylari (hosil tugish davri)",
        "calendar_season_en": "June — September (fruiting period)",
        "recommended_dosage_uz": "10 litr suvga 40 gramm Mis kuporosi yoki Ridomil Gold (10L ga 25g). Yoki xalqona usul: 10L ga 50g osh sodasi + 30g kir sovun.",
        "recommended_dosage_en": "Copper Oxychloride 40g per 10L water or Ridomil Gold (25g per 10L). Alternatively: 50g baking soda + 30g soap per 10L.",
        "cultural_remedies_uz": [
            "Pomidor tubidagi yerga tegib turgan pastki sarg'aygan barglarni uzib tashlash",
            "Shlang bilan tepasidan emas, faqat egatdan yoki tomchilatib ildiziga suv quyish",
            "Kasal meva va barglarni darhol uzib tomorqadan chiqarib yoqish"
        ],
        "cultural_remedies_en": [
            "Prune all ground-touching lower leaves for aeration",
            "Water solely at the soil base, avoid wetting foliage",
            "Promptly discard infected fruits and leaves away from the garden"
        ]
    },
    {
        "id": "cucumber_powdery_mildew",
        "crop": "Bodring & Poliz",
        "crop_en": "Cucumber & Melons",
        "name_uz": "Bodring un shudringi (Oq mog'or)",
        "name_en": "Cucumber Powdery Mildew",
        "scientific_name": "Podosphaera xanthii",
        "pathogen_type": "Zamburug'li",
        "pathogen_type_en": "Fungal",
        "threat_level": "HIGH",
        "image_url": "/images/cucumber_powdery_mildew.jpg",
        "visual_signs_uz": "Barglarning ustki qismida oq un sepilgandek dog'lar, barglarning tez sarg'ayishi va qovjirab qurishi.",
        "visual_signs_en": "Ash-white talcum powder-like fungal spots covering the upper leaf blade, leading to premature yellowing and desiccation.",
        "causes_uz": "Issiq va dim havo (issiqxona yoki qalin ekilgan tomorqa), shamollatish yetishmasligi.",
        "causes_en": "Warm humid microclimate, dense unpruned planting, poor airflow.",
        "calendar_season_uz": "May — Avgust oylari",
        "calendar_season_en": "May — August",
        "recommended_dosage_uz": "1 litr sut zardobiga 9 litr suv + 20 tomchi yod (xalqona toza usul). Yoki 10 litrga 30-40g Kolloid oltingugurt (Tiovit Jet).",
        "recommended_dosage_en": "1L milk whey + 9L water + 20 drops iodine (household organic remedy). Or 30-40g Colloidal Sulfur (Thiovit Jet) per 10L.",
        "cultural_remedies_uz": [
            "Bodring palagini ko'tarib iplarga bog'lash (vertikal o'stirish)",
            "Pastki eskirgan va sarg'aygan barglarni uzib shamollatishni oshirish",
            "Kechki salqinda emas, faqat ertalab sug'orish"
        ],
        "cultural_remedies_en": [
            "Trellis vines vertically to keep foliage off the ground",
            "Prune aged lower leaves to boost airflow",
            "Irrigate only in the morning hours"
        ]
    },
    {
        "id": "apple_scab",
        "crop": "Mevali daraxtlar (Olma)",
        "crop_en": "Fruit Trees (Apple)",
        "name_uz": "Olma kalmarazi (Parsha kasalligi)",
        "name_en": "Apple Scab (Venturia)",
        "scientific_name": "Venturia inaequalis",
        "pathogen_type": "Zamburug'li",
        "pathogen_type_en": "Fungal",
        "threat_level": "MEDIUM",
        "image_url": "/images/apple_scab.jpg",
        "visual_signs_uz": "Bargda zaytunrang-jigarrang baxmalsimon to'garak dog'lar, meva sirtida qora po'stloq yaralari va mevaning yorilib xunuk bo'lib qolishi.",
        "visual_signs_en": "Olive-green to velvety dark brown circular lesions on leaves, scabby corky spots and fruit distortion on apples.",
        "causes_uz": "Bahorgi nam yomg'irli ob-havo, daraxt shoxlarining qalinlashib quyosh kirmasligi.",
        "causes_en": "Prolonged wet spring weather, overcrowded canopy preventing sunlight penetration.",
        "calendar_season_uz": "Aprel — Iyul oylari (shox yozish va meva tugish)",
        "calendar_season_en": "April — July (leaf flush and fruit sizing)",
        "recommended_dosage_uz": "1% li Bordo suyuqligi (100g mis kuporosi + 100g ohak / 10L suv) yoki Skor (10L ga 2ml). Ertalab shamolsiz havoda.",
        "recommended_dosage_en": "1% Bordeaux mixture or Difenoconazole (Skor, 2ml per 10L water). Spray in early morning without wind.",
        "cultural_remedies_uz": [
            "Daraxt ichki shoxlarini xazonrezlikda va erta bahorda butab, quyosh tushishini ta'minlash",
            "Daraxt tagidagi to'kilgan kasal barglarni yig'ib ko'mish",
            "Daraxt tanasini erta bahor va kuzda ohak bilan oqlash"
        ],
        "cultural_remedies_en": [
            "Annual canopy thinning to allow light and wind penetration",
            "Rake and compost/bury fallen leaf litter",
            "Whitewash trunks with lime in early spring and autumn"
        ]
    },
    {
        "id": "peach_leaf_curl",
        "crop": "Mevali daraxtlar (Shaftoli)",
        "crop_en": "Fruit Trees (Peach)",
        "name_uz": "Shaftoli barg buralishi (Tafranioz)",
        "name_en": "Peach Leaf Curl (Taphrina)",
        "scientific_name": "Taphrina deformans",
        "pathogen_type": "Zamburug'li",
        "pathogen_type_en": "Fungal",
        "threat_level": "HIGH",
        "image_url": "/images/peach_leaf_curl.jpg",
        "visual_signs_uz": "Barglarning qizg'ish-sarg'ish rangga kirib, burishib-go'shtdor bo'lib qalinlashishi va to'kilib ketishi.",
        "visual_signs_en": "Leaves become severely distorted, puckered, thickened, turning reddish-yellow before premature dropping.",
        "causes_uz": "Erta bahordagi salqin va seryog'in havo, kurtak yorilishi davrida zamburug' faollashishi.",
        "causes_en": "Cold, wet early spring weather triggering overwintered blastospores.",
        "calendar_season_uz": "Mart oxiri — May oylari",
        "calendar_season_en": "Late March — May",
        "recommended_dosage_uz": "Kurtak yozilishidan oldin 3% li Bordo suyuqligi bilan 'ko'kartirib' yuvish. Barg chiqqandan keyin Xoruz (10L ga 3g).",
        "recommended_dosage_en": "3% Bordeaux mixture dormant spray before bud break; Cyprodinil (Chorus, 3g per 10L) after leaf emergence.",
        "cultural_remedies_uz": [
            "Burishgan kasal barglarni erta bosqichda qo'lda uzib yoqish",
            "Daraxtni erta bahorda kuchli sanitariya butashdan o'tkazish",
            "Daraxt ostini begona o'tlardan toza saqlash"
        ],
        "cultural_remedies_en": [
            "Hand-pick early curled leaves before sporulation",
            "Rigorous early spring sanitary pruning",
            "Keep the tree base weed-free"
        ]
    },
    {
        "id": "cotton_bacterial_blight",
        "crop": "Paxta (G'oza)",
        "crop_en": "Cotton (Gossypium)",
        "name_uz": "Bakterial burchakli dog'lanish (Gommoz)",
        "name_en": "Bacterial Blight (Angular Leaf Spot)",
        "scientific_name": "Xanthomonas citri pv. malvacearum",
        "pathogen_type": "Bakterial",
        "pathogen_type_en": "Bacterial",
        "threat_level": "HIGH",
        "image_url": "/images/cotton_bacterial_blight.jpg",
        "visual_signs_uz": "Barg tomirlari bilan chegaralangan burchakli, suvli to'q-jigarrang dog'lar. Keyinchalik qorayib quriydi va poya bo'ylab qora chiziqlar hosil qiladi.",
        "visual_signs_en": "Angular water-soaked dark brown spots sharply delimited by leaf veinlets. Lesions turn black and dry out, forming petiole streaks.",
        "causes_uz": "Yomg'irdan keyingi yuqori harorat (28-35°C), ortiqcha sepib sug'orish, chigitning zararlangan bo'lishi.",
        "causes_en": "Post-rain high temperatures (28-35°C), excessive sprinkler irrigation, contaminated seed stock.",
        "calendar_season_uz": "Iyun — Avgust oylari (shonalash va gullash davri)",
        "calendar_season_en": "June — August (squaring and flowering period)",
        "recommended_dosage_uz": "10 litr suvga 40-50 gramm Mis kuporosi yoki Xlorokis medi (0.4% eritma). 1 gektarga 250-300 litr eritma hisobida.",
        "recommended_dosage_en": "Copper Oxychloride 40-50g per 10L water (0.4% solution). 250-300L working solution per hectare.",
        "cultural_remedies_uz": [
            "Egatlab sug'orishga o'tish, barglarga suv sachratmaslik",
            "Zararlangan pastki shox va barglarni daladan chiqarib yoqish",
            "Kuzda chuqur haydash (zyab) va chigitni ekishdan oldin dorilash"
        ],
        "cultural_remedies_en": [
            "Switch strictly to furrow irrigation, avoid splashing water onto foliage",
            "Prune and destroy infected bottom branches outside field boundaries",
            "Deep autumn plowing and certified fungicide seed treatment prior to sowing"
        ]
    },
    {
        "id": "cotton_verticillium_wilt",
        "crop": "Paxta (G'oza)",
        "crop_en": "Cotton (Gossypium)",
        "name_uz": "G'oza vilti (Vertitsillyoz so'lish)",
        "name_en": "Verticillium Wilt (Tiger-stripe)",
        "scientific_name": "Verticillium dahliae",
        "pathogen_type": "Zamburug'li",
        "pathogen_type_en": "Fungal",
        "threat_level": "CRITICAL",
        "image_url": "/images/cotton_verticillium_wilt.jpg",
        "visual_signs_uz": "Barg tomirlari oralig'ida sariq-jigarrang dog'lar (yo'lbars terisi nusxasi), barg chetlari quriydi, poya kesilganda qora-jigarrang tomir halqasi ko'rinadi.",
        "visual_signs_en": "Interveinal yellow-brown chlorotic mottling ('tiger-stripe' pattern), marginal necrosis, internal xylem vascular browning on stem cross-section.",
        "causes_uz": "Tuproqda mikrosklerotsiylarning to'planishi, zax yerlar, ortiqcha sovuq daryo suvi bilan bostirib sug'orish.",
        "causes_en": "Accumulation of soil microsclerotia, waterlogged fields, flood irrigation with cold snowmelt river water.",
        "calendar_season_uz": "Iyul — Sentyabr oylari (ko'sak tugish va pishish davri)",
        "calendar_season_en": "July — September (boll formation and maturation)",
        "recommended_dosage_uz": "Bargdan kaliy sulfat (K2SO4, 1.5% eritma) bilan oziqlantirish. Ildizga bio-preparatlardan Triyodermin yoki Trichoderma suspenziyasi.",
        "recommended_dosage_en": "Foliar potassium sulfate (K2SO4, 1.5% solution). Apply Trichoderma bio-fungicide suspension into root zone.",
        "cultural_remedies_uz": [
            "Sovuq daryo suvi bilan ko'llatib sug'orishdan qat'iy saqlanish",
            "Kaliy va fosfor o'g'itlari ulushini oshirib, o'simlik immunitetini ko'tarish",
            "Viltga chidamli g'oza navlarini ekish va almashlab ekishni yo'lga qo'yish"
        ],
        "cultural_remedies_en": [
            "Avoid flooding fields with cold snowmelt canal water",
            "Increase potassium and phosphorus fertilization ratios to strengthen vascular immunity",
            "Adopt wilt-tolerant certified varieties and crop rotation with legumes or wheat"
        ]
    },
    {
        "id": "grape_powdery_mildew",
        "crop": "Uzum (Tokzor)",
        "crop_en": "Grapevine (Vitis vinifera)",
        "name_uz": "Un shudring (Oidium kasalligi)",
        "name_en": "Powdery Mildew (Oidium)",
        "scientific_name": "Uncinula necator (Erysiphe necator)",
        "pathogen_type": "Zamburug'li",
        "pathogen_type_en": "Fungal",
        "threat_level": "CRITICAL",
        "image_url": "/images/grape_powdery_mildew.jpg",
        "visual_signs_uz": "Bargning ustki yuzasida oqish-kulrang unsimon qoplama, barglarning yuqoriga qayrilishi, g'ujumlar yorilib urug'i ko'rinib qolishi.",
        "visual_signs_en": "Ash-gray powdery fungal mycelium covering upper leaf surface, upward leaf cupping, berry splitting exposing seeds.",
        "causes_uz": "Issiq va quruq havo (25-32°C), tok tupining qalinlashib quyosh kirmasligi, shamollatish yetarli emasligi.",
        "causes_en": "Warm arid weather (25-32°C), overcrowded shaded canopy, poor aeration.",
        "calendar_season_uz": "May — Avgust oylari (shona va g'ujum kattalashishi)",
        "calendar_season_en": "May — August (flowering and berry sizing stage)",
        "recommended_dosage_uz": "10 litr suvga 80 gramm Kolloid oltingugurt yoki 2 ml Topaz (Penkonazol). Ertalab soat 08:30 gacha ishlov berish.",
        "recommended_dosage_en": "Colloidal sulfur 80g per 10L water or penconazole (Topaz) 2ml per 10L water. Apply early morning before 08:30.",
        "cultural_remedies_uz": [
            "Tokni zudlik bilan yashil xomtok qilish, ortiqcha novda va barglarni olib tashlash",
            "Boshok va shingillarga quyosh nuri va shamol tushishini ta'minlash",
            "Muntazam oltingugurt changitish profilaktikasini o'tkazish"
        ],
        "cultural_remedies_en": [
            "Immediately perform green canopy pruning (xomtok) to eliminate excess dense foliage",
            "Ensure direct sunlight penetration and unrestricted airflow across grape clusters",
            "Maintain preventive early season sulfur dusting"
        ]
    },
    {
        "id": "grape_downy_mildew",
        "crop": "Uzum (Tokzor)",
        "crop_en": "Grapevine (Vitis vinifera)",
        "name_uz": "Soxta un shudring (Mildiью)",
        "name_en": "Downy Mildew (Mildew)",
        "scientific_name": "Plasmopara viticola",
        "pathogen_type": "Zamburug'li",
        "pathogen_type_en": "Fungal",
        "threat_level": "HIGH",
        "image_url": "/images/grape_downy_mildew.jpg",
        "visual_signs_uz": "Barg ustida yog'li sariq dog'lar ('moyli dog'lar'), barg tagida esa nam havoda oqish paxmoq momiq paydo bo'lishi.",
        "visual_signs_en": "Translucent yellowish 'oil spots' on upper leaf blade, accompanied by dense white downy sporulation on the underside in humid conditions.",
        "causes_uz": "Baqamti yomg'ir va yuqori nisbiy namlik (>80%), past joylashgan tokzorlar.",
        "causes_en": "Prolonged rainfall combined with high relative humidity (>80%), low-lying unventilated vineyard rows.",
        "calendar_season_uz": "Aprel oxiri — Iyun (bahorgi sernam davr)",
        "calendar_season_en": "Late April — June (humid spring vegetative flush)",
        "recommended_dosage_uz": "1% li Bordo suyuqligi (100g mis kuporosi + 100g ohak / 10L suv) yoki Ridomil Gold (10L ga 25g).",
        "recommended_dosage_en": "1% Bordeaux mixture (100g copper sulfate + 100g lime per 10L water) or Ridomil Gold MZ (25g per 10L water).",
        "cultural_remedies_uz": [
            "Tokning yerga tegib turgan pastki barglarini uzib tashlash",
            "Tuproqni yumshatib, namlikni me'yorida ushlash",
            "Kasal to'kilgan barglarni yig'ib yoqish"
        ],
        "cultural_remedies_en": [
            "Strip all ground-touching low hanging foliage",
            "Maintain clean cultivated soil beneath grape trellises",
            "Rake and destroy fallen autumn leaf litter"
        ]
    },
    {
        "id": "cotton_spider_mite",
        "crop": "Paxta (G'oza)",
        "crop_en": "Cotton (Gossypium)",
        "name_uz": "Oddiy o'rgimchakkana",
        "name_en": "Two-spotted Spider Mite",
        "scientific_name": "Tetranychus urticae",
        "pathogen_type": "Zararkunanda",
        "pathogen_type_en": "Pest Damage",
        "threat_level": "HIGH",
        "image_url": "/images/cotton_spider_mite.jpg",
        "visual_signs_uz": "Barg orqasida nozik to'r, barg sathida mayda oq-sariq nuqtalar, keyinchalik barg qizarib qo'ng'ir rangga kiradi va to'kiladi.",
        "visual_signs_en": "Fine silken micro-webbing on leaf underside, dense yellow punctate feeding scars, foliage turns bronze/red and desiccates.",
        "causes_uz": "Quruq va jazirama issiq havo (>35°C), chang bosishi, ariq bo'yidagi begona o'tlar.",
        "causes_en": "Extreme arid heat (>35°C), dusty road proximity, uncontrolled ditch-bank weeds harboring mite colonies.",
        "calendar_season_uz": "Iyun — Avgust (yozgi qurg'oqchilik davri)",
        "calendar_season_en": "June — August (midsummer drought stress period)",
        "recommended_dosage_uz": "Omayt (10L ga 15-20ml) yoki Nissoran (10L ga 5-7g). Shuningdek 0.5% li oltingugurt kukuni bilan changitish.",
        "recommended_dosage_en": "Propargite (Omite, 15-20ml per 10L) or hexythiazox (Nissoran, 5-7g per 10L). Alternatively ground sulfur dusting.",
        "cultural_remedies_uz": [
            "Dala atrofi va ariq yoqalaridagi begona o'tlarni yo'qotish",
            "Dalani changdan himoya qilish uchun chetki qatorlarni suv bilan yuvish",
            "Biologik usulda yirtqich kanalar (Fitoseyulus) tarqatish"
        ],
        "cultural_remedies_en": [
            "Eradicate bindweed and wild vegetation along irrigation canals and field borders",
            "Rinse roadside border rows to suppress dust deposition",
            "Release biological predatory mites (Phytoseiulus persimilis) in localized outbreak spots"
        ]
    },
    {
        "id": "grape_saline_scorch",
        "crop": "Uzum va Paxta",
        "crop_en": "Grape & Cotton",
        "name_uz": "Tuproq sho'rlanishi va issiq urishi",
        "name_en": "Soil Salinity & Heat Scorch",
        "scientific_name": "Abiotic Sodium/Chloride Stress",
        "pathogen_type": "Abiotik stress",
        "pathogen_type_en": "Abiotic Stress",
        "threat_level": "MEDIUM",
        "image_url": "/images/grape_saline_scorch.jpg",
        "visual_signs_uz": "Barg chetlari bo'ylab bir tekis doirasimon kuygan jigarrang hoshiya, oraliq sarg'ish chiziq. Mog'or yoki bakteriya shillig'i umuman yo'q.",
        "visual_signs_en": "Uniform marginal perimeter necrotic scorch bordering the leaf circumference, yellow transitional halo, absence of fungal or bacterial signs.",
        "causes_uz": "Orolbo'yi va Mirzacho'l sizot suvlarining ko'tarilishi, qattiq bug'lanish natijasida natriy tuzlarining to'planishi.",
        "causes_en": "Elevated saline groundwater table in Aral/Mirzachul basins, high evapotranspiration and sodium chloride toxicity.",
        "calendar_season_uz": "Iyul — Avgust oylari (40-45°C jazirama issiqda)",
        "calendar_season_en": "July — August (during 40-45°C extreme heat spells)",
        "recommended_dosage_uz": "Gumusli o'g'itlar (Gumimat, Gumimax) bilan bargdan purkash. Kaliy sulfat 1% eritma.",
        "recommended_dosage_en": "Foliar humic acid fertilizers (Gumimax) and 1% Potassium Sulfate foliar spray.",
        "cultural_remedies_uz": [
            "Zovurlarni (kollektor-drenaj tarmoqlarini) chuqurlashtirib tozalash",
            "Kuz-qish oylarida sho'r yuvish ishlarini me'yorida o'tkazish",
            "Xlorli o'g'itlardan (masalan, kaliy xlorid) butunlay voz kechish"
        ],
        "cultural_remedies_en": [
            "Deepen and clean collector-drainage network (zovur) to lower water table below 2m",
            "Perform scheduled winter leaching irrigation with adequate outflow",
            "Strictly avoid potassium chloride fertilizers; use potassium sulfate only"
        ]
    }
]

# Real-time Phytosanitary & Risk Data for all 14 territories of Uzbekistan
PHYTOSANITARY_MAP_DATA: List[Dict[str, Any]] = [
    {
        "region_id": "andijan",
        "region_name": "Andijon viloyati",
        "region_name_en": "Andijan Region",
        "coords": "40.7821° N, 72.3442° E",
        "dominant_crops": "Paxta, Sabzavot, Bog'dorchilik",
        "dominant_crops_en": "Cotton, Vegetables, Orchards",
        "risk_level": "MEDIUM",
        "active_threat": "G'oza gommozi (Bakterioz)",
        "active_threat_en": "Cotton Bacterial Blight",
        "humidity": "62%",
        "temperature": "32°C",
        "advice_uz": "Egatlab sug'orishga e'tibor qarating, ortiqcha zaxlatishdan saqlaning.",
        "advice_en": "Focus on furrow irrigation; prevent waterlogging and leaf splashing."
    },
    {
        "region_id": "fergana",
        "region_name": "Farg'ona viloyati",
        "region_name_en": "Fergana Region",
        "coords": "40.3842° N, 71.7843° E",
        "dominant_crops": "Paxta, Bog'dorchilik, Uzumchilik (Oltiariq)",
        "dominant_crops_en": "Cotton, Horticulture, Vineyards",
        "risk_level": "HIGH",
        "active_threat": "Uzum un shudringi (Oidium) va Vilt",
        "active_threat_en": "Grape Powdery Mildew & Wilt",
        "humidity": "68%",
        "temperature": "33°C",
        "advice_uz": "Tokzorlarda shoshilinch xomtok o'tkazib, kolloid oltingugurt seping.",
        "advice_en": "Conduct urgent green canopy pruning and apply colloidal sulfur."
    },
    {
        "region_id": "namangan",
        "region_name": "Namangan viloyati",
        "region_name_en": "Namangan Region",
        "coords": "40.9983° N, 71.6726° E",
        "dominant_crops": "Bog'dorchilik, Uzum, Paxta (Pop, Chust)",
        "dominant_crops_en": "Orchards, Vineyards, Cotton",
        "risk_level": "LOW",
        "active_threat": "Oddiy o'rgimchakkana",
        "active_threat_en": "Two-spotted Spider Mite",
        "humidity": "48%",
        "temperature": "34°C",
        "advice_uz": "Dala atrofidagi begona o'tlarni tozalang va chang ko'tarilishini kamaytiring.",
        "advice_en": "Eradicate field margin weeds and minimize roadside dust settlement."
    },
    {
        "region_id": "tashkent_region",
        "region_name": "Toshkent viloyati",
        "region_name_en": "Tashkent Region",
        "coords": "41.2213° N, 69.8597° E",
        "dominant_crops": "Uzum (Parkent), Sabzavot, Paxta (Quyi Chirchiq)",
        "dominant_crops_en": "Grapevines (Parkent), Vegetables, Cotton",
        "risk_level": "MEDIUM",
        "active_threat": "Tok mildiьюsi va kulrang chirish",
        "active_threat_en": "Grape Downy Mildew & Botrytis",
        "humidity": "70%",
        "temperature": "31°C",
        "advice_uz": "Tog'oldi zonalarida yomg'irdan so'ng Bordo suyuqligi bilan profilaktika qiling.",
        "advice_en": "Spray Bordeaux mixture in foothill zones immediately following seasonal rain."
    },
    {
        "region_id": "tashkent_city",
        "region_name": "Toshkent shahri (Agro-hudud)",
        "region_name_en": "Tashkent City (Suburban Agro)",
        "coords": "41.3111° N, 69.2797° E",
        "dominant_crops": "Issiqxona xo'jaliklari, ko'chatchilik",
        "dominant_crops_en": "Greenhouse Horticulture, Nurseries",
        "risk_level": "LOW",
        "active_threat": "Oq qanot va shira",
        "active_threat_en": "Whiteflies & Aphids",
        "humidity": "50%",
        "temperature": "33°C",
        "advice_uz": "Issiqxona havosi haroratini 28°C dan oshirmaslik uchun soyabon to'rlardan foydalaning.",
        "advice_en": "Use greenhouse shade netting to keep internal temperatures below 28°C."
    },
    {
        "region_id": "samarkand",
        "region_name": "Samarqand viloyati",
        "region_name_en": "Samarkand Region",
        "coords": "39.6542° N, 66.9597° E",
        "dominant_crops": "Kishmishbop uzumchilik (Bulung'ur, Ishtixon), Paxta",
        "dominant_crops_en": "Table/Raisin Grapes, Cotton",
        "risk_level": "HIGH",
        "active_threat": "Oidium (Un shudring) va Klaster vilti",
        "active_threat_en": "Powdery Mildew & Cluster Wilt",
        "humidity": "55%",
        "temperature": "35°C",
        "advice_uz": "Uzum mevalari tushishidan oldin Tiovit Jet yoki Topaz bilan ishlov berish zarur.",
        "advice_en": "Treat vineyards with Thiovit Jet or Topaz before berry bunch closure."
    },
    {
        "region_id": "bukhara",
        "region_name": "Buxoro viloyati",
        "region_name_en": "Bukhara Region",
        "coords": "39.7681° N, 64.4556° E",
        "dominant_crops": "Paxta, Ipakchilik, Qorako'lchilik ekinlari",
        "dominant_crops_en": "Cotton, Sericulture, Forage",
        "risk_level": "HIGH",
        "active_threat": "Tuproq sho'rlanishi va Fuzarioz so'lish",
        "active_threat_en": "Soil Salinity & Fusarium Wilt",
        "humidity": "38%",
        "temperature": "39°C",
        "advice_uz": "Kollektor-zovur suvlarini chuqur haydash bilan tozalang, kaliyli o'g'it bering.",
        "advice_en": "Flush collector drainage channels and supply supplementary potassium fertilizers."
    },
    {
        "region_id": "navoiy",
        "region_name": "Navoiy viloyati",
        "region_name_en": "Navoi Region",
        "coords": "40.0844° N, 65.3792° E",
        "dominant_crops": "Paxta (Karmana, Qiziltepa), Uzumchilik",
        "dominant_crops_en": "Cotton, Vineyard horticulture",
        "risk_level": "MEDIUM",
        "active_threat": "Issiq urishi va o'rgimchakkana",
        "active_threat_en": "Heat Stress & Spider Mites",
        "humidity": "35%",
        "temperature": "40°C",
        "advice_uz": "Qator oralariga kechqurun salqin suv yurgizing, garmsel ta'sirini kamaytiring.",
        "advice_en": "Run evening furrow irrigation to cool soil profile and reduce arid wind shock."
    },
    {
        "region_id": "jizzakh",
        "region_name": "Jizzax viloyati",
        "region_name_en": "Jizzakh Region",
        "coords": "40.1158° N, 67.8422° E",
        "dominant_crops": "Mirzacho'l paxtachiligi, g'allachilik",
        "dominant_crops_en": "Cotton clusters, Cereals",
        "risk_level": "MEDIUM",
        "active_threat": "G'oza bakterial dog'lanishi",
        "active_threat_en": "Cotton Bacterial Blight",
        "humidity": "45%",
        "temperature": "36°C",
        "advice_uz": "Fosforli o'g'itlar bilan qo'shimcha oziqlantiring, begona o'tlar qoldirmang.",
        "advice_en": "Side-dress with phosphorus and maintain strict weed sanitation."
    },
    {
        "region_id": "sirdaryo",
        "region_name": "Sirdaryo viloyati",
        "region_name_en": "Syrdarya Region",
        "coords": "40.5011° N, 68.7842° E",
        "dominant_crops": "Paxtachilik klasterlari (Sayxunobod, Boyovut)",
        "dominant_crops_en": "Cotton Clusters, Alfalfa",
        "risk_level": "HIGH",
        "active_threat": "Tuproq sho'rlanishi va Vertitsillyoz",
        "active_threat_en": "Soil Salinity & Verticillium Wilt",
        "humidity": "52%",
        "temperature": "37°C",
        "advice_uz": "Sho'r yuvish drenajlarini qayta ko'rikdan o'tkazing, biologik gumus sepishni yo'lga qo'ying.",
        "advice_en": "Inspect drainage outfalls and apply biological humic soil restorers."
    },
    {
        "region_id": "kashkadarya",
        "region_name": "Qashqadaryo viloyati",
        "region_name_en": "Kashkadarya Region",
        "coords": "38.8606° N, 65.7891° E",
        "dominant_crops": "Yirik paxtachilik (Qarshi, Koson, Nishon)",
        "dominant_crops_en": "Large-scale Cotton & Wheat",
        "risk_level": "HIGH",
        "active_threat": "O'rgimchakkana va G'oza tunlami",
        "active_threat_en": "Spider Mites & Cotton Bollworm",
        "humidity": "36%",
        "temperature": "39°C",
        "advice_uz": "Triyoxogramma va oltinko'z entomofaglarini zudlik bilan dalaga tarqating.",
        "advice_en": "Release Trichogramma and Chrysoperla beneficial insects across cotton rows."
    },
    {
        "region_id": "surkhandarya",
        "region_name": "Surxondaryo viloyati",
        "region_name_en": "Surkhandarya Region",
        "coords": "37.9409° N, 67.5709° E",
        "dominant_crops": "Yupqa tolali paxta, erta pishar uzum, anor",
        "dominant_crops_en": "Fine-staple Cotton, Early Grapes, Pomegranate",
        "risk_level": "MEDIUM",
        "active_threat": "Quyosh kuyishi va Antraknoz",
        "active_threat_en": "Solar Scorch & Anthracnose",
        "humidity": "42%",
        "temperature": "41°C",
        "advice_uz": "Kunduzgi 11:00 dan 17:00 gacha sug'orishni qat'iy to'xtating, tomchilatib sug'orishdan foydalaning.",
        "advice_en": "Halt surface water flow between 11:00-17:00; use drip lines where available."
    },
    {
        "region_id": "khorezm",
        "region_name": "Xorazm viloyati",
        "region_name_en": "Khorezm Region",
        "coords": "41.5562° N, 60.6313° E",
        "dominant_crops": "Paxta (Shovot, Yangibozor), polizchilik",
        "dominant_crops_en": "Cotton, Melons, Rice",
        "risk_level": "HIGH",
        "active_threat": "Xloridli sho'rlanish va Alternarioz",
        "active_threat_en": "Chloride Salinity & Alternaria",
        "humidity": "60%",
        "temperature": "36°C",
        "advice_uz": "Sho'r yuvishdan keyin organik chirindi soling va mis saqlovchi preparatlar bilan ishlang.",
        "advice_en": "Supplement with organic compost after leaching; apply copper preventative sprays."
    },
    {
        "region_id": "karakalpakstan",
        "region_name": "Qoraqalpog'iston Respublikasi",
        "region_name_en": "Republic of Karakalpakstan",
        "coords": "43.7683° N, 59.0214° E",
        "dominant_crops": "Paxta (To'rtko'l, Ellikqala, Beruniy)",
        "dominant_crops_en": "Northern Cotton, Sorghum",
        "risk_level": "CRITICAL",
        "active_threat": "Orol dengizi chang-tuz bo'roni va Qurg'oqchilik stressi",
        "active_threat_en": "Aral Dust-Salt Storms & Severe Drought",
        "humidity": "34%",
        "temperature": "38°C",
        "advice_uz": "Antistress moddalar (Epin-Ekstra, Gumax) va tomchilatib sug'orish bilan o'simlik turgorini saqlang.",
        "advice_en": "Apply anti-stress bio-stimulants (Epin, humic acid) to protect cellular turgor."
    }
]

# Agronomist Fallback Knowledge Base for Common Questions in Uzbek
COMMON_AGRO_QA_UZ: Dict[str, str] = {
    "mis kuporosi": (
        "🌱 **Mis kuporosi (Mis sulfat) bilan to'g'ri ishlash qoidasi:**\n\n"
        "1. **Miyori:** 10 litr suvga 40-50 gramm mis kuporosi solinadi (0.4-0.5% li eritma).\n"
        "2. **Qo'llash vaqti:** Ertalab soat 06:00 dan 09:00 gacha yoki kechki 18:00 dan so'ng. Quyosh tikkaga kelganda aslo sepmang, bargni kuydiradi!\n"
        "3. **Tavsiya:** Gommoz, zang va chirishga qarshi a'lo samara beradi. Metall idishda emas, faqat plastmassa yoki yog'och idishda eritish kerak."
    ),
    "vilt": (
        "🌿 **G'ozada Vilt (so'lish) kasalligiga qarshi amaliy choralar:**\n\n"
        "1. **Sug'orish:** Ortiqcha sovuq daryo suvi bilan bostirib sug'orishni darhol to'xtating! Zax yerda vilt 3 baravar tez rivojlanadi.\n"
        "2. **Oziqlantirish:** Bargdan kaliy sulfat (K2SO4, 1-1.5%) seping. Kaliy o'simlik tomir to'qimasini qalinlashtiradi.\n"
        "3. **Biologik himoya:** Har bir gektarga 2-3 litr Trixodermin yoki Trichoderma bio-preparatlarini ariq orqali oqizing.\n"
        "4. **Kuzgi tadbir:** Kuzda chuqur haydash o'tkazib, keyingi yilga chidamli 'Buxoro-6' yoki 'Sulton' kabi navlarni eking."
    ),
    "un shudring": (
        "🍇 **Uzumda Un shudring (Oidium) bilan kurashish:**\n\n"
        "1. **Shoshilinch yordam:** Kolloid oltingugurt (10 litr suvga 80-100 gramm) bilan tok tupining ustki va pastki barglarini yaxshilab yuving.\n"
        "2. **Xomtok:** Zudlik bilan yashil xomtok qilib, ortiqcha novdalarni olib tashlang. Tok shamollashi va quyosh nuri tushishi shart!\n"
        "3. **Kuchli zararlanganda:** Tizimli preparatlardan 'Topaz' (10L suvga 2.5ml) yoki 'Tiovit Jet' (10L suvga 50g) seping."
    ),
    "sug'orish": (
        "💧 **O'zbekiston sharoitida to'g'ri sug'orish me'yori:**\n\n"
        "1. **Vaqti:** Yoz oylarida sug'orishni faqat kechki 19:00 dan ertalab 08:00 gacha o'tkazish kerak.\n"
        "2. **Tuproq harorati:** Qizib turgan tuproqqa sovuq suv berilsa, ildiz bo'g'zi kasallanadi va vilt kuchayadi.\n"
        "3. **Egatlab sug'orish:** Suvni har bir egatga sekin, bir tekis oqizish va barglarga sachratmaslik kerak."
    ),
    "sho'r": (
        "🧂 **Sho'rlangan yerlarda ekinlarni asrash yo'llari:**\n\n"
        "1. **Zovurlarni tozalash:** Drenaj (zovur) suvining sathi yer sathidan kamida 1.8-2 metr chuqurlikda bo'lishi kerak.\n"
        "2. **Organika:** Gektariga kamida 20-25 tonna chirigan go'ng yoki gumus moddalari solish natriy tuzlarining zaharini bog'laydi.\n"
        "3. **O'g'it:** Xlorli kaliydan qat'iy saqlaning, faqat kaliy sulfat va ammiakli selitradan foydalaning."
    ),
    "pomidor": (
        "🍅 **Tomorqada Pomidorni fitoftora va kasalliklardan asrash sirlari:**\n\n"
        "1. **Barglarni tozalash:** Pomidor tupi tagidagi yerga tegib turgan barcha pastki barglarni uzib tashlang. Tuproqdagi zamburug' birinchi bo'lib shu barglarga o'tadi.\n"
        "2. **To'g'ri sug'orish:** Pomidorni kechasi shlang bilan tepasidan cho'miltirib sug'ormang! Suvni faqat egatdan yoki ildiziga sekin oqizing.\n"
        "3. **Xalqona va arzon himoya:** 10 litr suvga 1 litr sut zardobi yoki 50g osh sodasi + 30g kir sovun eritib seping. Kuchli kasallikda Mis kuporosi (10L ga 30-40g) yoki Ridomil Gold seping.\n"
        "4. **Uchki chirish (meva tagi qorayishi):** Bu kalsiy yetishmasligidir. 10 litr suvga 20-30g kalsiy selitrasi solib bargdan seping."
    ),
    "bodring": (
        "🥒 **Bodringda oq un (un shudring) va sarg'ayishga qarshi xalqona chora:**\n\n"
        "1. **Sut zardobi va yod (100% toza usul):** 1 litr sut zardobiga 9 litr suv va 20 tomchi dorixona yodini qo'shib, ertalab bodring barglariga seping. Zamburug'ni bir kunda to'xtatadi!\n"
        "2. **Shamollatish:** Bodring palagini yerda yoyilib yotishiga yo'l qo'ymang, ipga ko'taring va pastki sarg'aygan barglarni olib tashlang.\n"
        "3. **Agro-vosita:** Agar un shudring ko'payib ketgan bo'lsa, 'Tiovit Jet' yoki Kolloid oltingugurt (10L ga 40g) seping."
    ),
    "olma": (
        "🍎 **Olma va mevali daraxtlarni parsha (kalmaraz) va qurtlardan asrash:**\n\n"
        "1. **Bahorgi va kuzgi profilaktika:** Erta bahorda kurtak yozishidan oldin 3% li Bordo suyuqligi bilan daraxtni 'ko'kartirib' yuving.\n"
        "2. **Yozgi parvarish:** Parsha paydo bo'lsa, 1% li Bordo suyuqligi yoki 'Skor' (10L ga 2ml) preparatini ertalab seping.\n"
        "3. **Olma qurtiga qarshi:** Meva tugilgach 'Koragen' yoki 'Karate' bilan o'z vaqtida dori sepilsa, meva qurtlamaydi.\n"
        "4. **Agrotexnika:** Daraxt shoxlarini ichini ochib butang, quyosh va shamol daraxt ichiga yetib borishi shart!"
    ),
    "shaftoli": (
        "🍑 **Shaftolida barg buralishi (tafranioz) va zararkunandalar:**\n\n"
        "1. **Eng asosiy muddat:** Shaftoli kurtagi bo'rtganda (hali barg yozmasdan) 3% li Bordo suyuqligi yoki Mis xloroksidi bilan yuvish shart! Barg chiqqandan keyin bu kasallikni to'xtatish qiyin bo'ladi.\n"
        "2. **Barg yozganda:** 'Skor' (10L ga 2ml) yoki 'Xoruz' (10L ga 3-4g) seping.\n"
        "3. **Qo'lda tozalash:** Burishib qizargan barglarni qo'lda uzib, tomorqadan tashqariga chiqarib yoqing."
    ),
    "gul": (
        "🌸 **Xona gullari va hovli gullarini parvarishlash:**\n\n"
        "1. **Barglar sarg'ayishi:** Ko'p hollarda ortiqcha suv quyishdan (ildiz chirishidan) yoki temir yetishmasligidan bo'ladi. Idish tagidagi likopchada suv to'planib qolmasin.\n"
        "2. **Oq mayda hasharot yoki o'rgimchakkana:** Oddiy kir sovunni suvda eritib (1 litr suvga 10-15g) barglarini latta bilan arting yoki 'Fitoverm' seping.\n"
        "3. **Oziqlantirish:** Bahor va yozda har 2 haftada bir marta kompleks universal o'g'it yoki yog'och kuli damlamasi bilan oziqlantiring."
    ),
    "tomorqa": (
        "🏡 **Aholi tomorqasida ekinlarni sog'lom o'stirish oltin qoidalari:**\n\n"
        "1. **Almashlab ekish:** Pomidor yoki kartoshkani har yili bir joyga ekmang! Ulardan keyin piyoz, sarimsoq yoki dukkakli ekinlar eking.\n"
        "2. **Tabiiy o'g'it:** Bahorda chirigan go'ng yoki bio-gumus solish tuproq unumdorligini 2 baravar oshiradi.\n"
        "3. **Suv rejimi:** Yozgi 40 daraja jaziramada kunduzi soat 11:00 dan 17:00 gacha aslo suv quymang! Faqat erta tongda yoki quyosh botgach sug'oring."
    )
}

# Agronomist Fallback Knowledge Base for Common Questions in English
COMMON_AGRO_QA_EN: Dict[str, str] = {
    "copper": (
        "🌱 **Proper Application of Copper Sulfate & Copper Oxychloride:**\n\n"
        "1. **Dosage:** Dissolve 40-50 grams of Copper Oxychloride per 10 Liters of water (0.4-0.5% solution).\n"
        "2. **Timing:** Spray exclusively in early morning hours (06:00 to 09:00) or evening after 18:00. Never spray during peak midday solar exposure to avoid severe leaf scorch.\n"
        "3. **Target Conditions:** Highly effective against Bacterial Blight (Gommoz), Anthracnose, and Downy Mildew. Prepare only in plastic containers."
    ),
    "wilt": (
        "🌿 **Field Protocol for Cotton Verticillium Wilt:**\n\n"
        "1. **Irrigation:** Immediately halt flood irrigation with cold river water; waterlogged cold soils accelerate Verticillium fungal penetration.\n"
        "2. **Foliar Nutrition:** Spray 1.0-1.5% Potassium Sulfate (K2SO4). Potassium thickens xylem cell walls and impedes fungal vascular occlusion.\n"
        "3. **Biological Control:** Inject 2-3 liters/ha of Trichoderma bio-fungicide suspension through furrow water.\n"
        "4. **Crop Rotation:** Implement 3-year rotations with alfalfa and winter cereals to exhaust soil microsclerotia."
    ),
    "powdery": (
        "🍇 **Managing Grapevine Powdery Mildew (Oidium):**\n\n"
        "1. **Immediate Intervention:** Thoroughly spray with Colloidal Sulfur (80-100g per 10L water) or Thiovit Jet covering both upper and lower leaf surfaces.\n"
        "2. **Canopy Pruning (Xomtok):** Promptly thin dense shoots and sucker leaves to restore airflow and sunlight penetration.\n"
        "3. **Curative Spray:** In established infections, apply systemic Triazole fungicides such as Topaz (2.5ml per 10L water)."
    ),
    "mildew": (
        "🍇 **Managing Grapevine Powdery & Downy Mildew:**\n\n"
        "1. **Immediate Intervention:** Thoroughly spray with Colloidal Sulfur or Bordeaux mixture covering both leaf surfaces.\n"
        "2. **Canopy Pruning:** Promptly thin dense shoots and sucker leaves to restore airflow and sunlight penetration.\n"
        "3. **Systemic Rotation:** Apply Ridomil Gold for downy mildew or Topaz for powdery mildew."
    ),
    "irrigation": (
        "💧 **Optimal Irrigation Best Practices:**\n\n"
        "1. **Timing:** During summer, schedule irrigation exclusively between 19:00 in the evening and 08:00 in the morning.\n"
        "2. **Thermal Shock:** Applying cold snowmelt water to hot midday soil induces root collar shock and accelerates wilt.\n"
        "3. **Furrow Method:** Use slow, uniform furrow infiltration; never splash ditch water directly onto plant foliage."
    ),
    "salinity": (
        "🧂 **Combating Soil Salinity & Osmotic Stress:**\n\n"
        "1. **Drainage Maintenance:** Deepen drainage canals (zovur) to maintain water table depth below 1.8-2.0 meters.\n"
        "2. **Organic Amendment:** Apply 20-25 t/ha of well-rotted manure or humic acids to bind sodium ions and rebuild soil structure.\n"
        "3. **Fertilizer Selection:** Strictly avoid Potassium Chloride (MOP); utilize only Potassium Sulfate (SOP) and ammonium nitrate."
    ),
    "tomato": (
        "🍅 **Backyard Tomato Care & Blight Prevention:**\n\n"
        "1. **Prune Bottom Foliage:** Strip all lower leaves touching the soil surface; fungal spores migrate from soil splash.\n"
        "2. **Irrigation Technique:** Never spray overhead hoses on tomato foliage; irrigate strictly at the root base early morning.\n"
        "3. **Remedies:** Spray 0.4% Copper Oxychloride (40g/10L) or bio-fungicide Fitosporin. For mild mildew, mix 50g baking soda + 30g soap in 10L water."
    ),
    "cucumber": (
        "🥒 **Managing Cucumber Powdery Mildew in Greenhouses & Gardens:**\n\n"
        "1. **Milk Whey Remedy (Organic):** Mix 1 part milk whey (or milk) with 9 parts water and 20 drops of iodine. Spray morning hours.\n"
        "2. **Canopy Aeration:** Trellis vines vertically and thin old yellowed leaves at the base.\n"
        "3. **Fungicide:** Apply Thiovit Jet (Colloidal Sulfur, 40g per 10L water) early morning before heat exceeds 28°C."
    ),
    "apple": (
        "🍎 **Managing Apple Scab & Fruit Orchard Pests:**\n\n"
        "1. **Early Spring:** Apply 3% dormant Bordeaux mixture before bud break.\n"
        "2. **Active Growth:** Spray Difenoconazole (Skor, 2ml/10L) or 1% Bordeaux mixture on leaves.\n"
        "3. **Sanitation:** Thin overcrowded inner branches and rake/burn fallen leaves in autumn."
    ),
    "garden": (
        "🏡 **Backyard Vegetable Garden & Household Crop Guidelines:**\n\n"
        "1. **Crop Rotation:** Never plant tomatoes or potatoes in the exact same plot every consecutive year; rotate with onions or greens.\n"
        "2. **Organic Soil Health:** Enrich soil with composted manure or vermicompost in early spring.\n"
        "3. **Water Management:** Avoid irrigation during midday solar peaks (11:00 to 17:00); water strictly at sunrise or after sunset."
    )
}

# Alias for backwards compatibility
COMMON_AGRO_QA = COMMON_AGRO_QA_UZ
