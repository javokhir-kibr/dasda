/**
 * AURORA CLIENT ENGINE — 5-PAGE AGRITECH SUITE ($10M DESIGN)
 * Tabs:
 * 1. AI Diagnostika (Foliar Scanner & HUD)
 * 2. AI Dala Agronomi (Live Consultation Chat)
 * 3. Kasalliklar Ensiklopediyasi (Catalog & Calendars)
 * 4. Fitomonitoring Xaritasi (14 Regions & Climate Alerts)
 * 5. Tahlillar Tarixi & Dalolatnoma (Audit History & PDF Print)
 */

// I18N DICTIONARY
const I18N = {
  uz: {
    subtitle: "Aholi tomorqasi, mevali daraxtlar, sabzavot va ekinlar uchun AI tabib",
    navSections: "BO'LIMLAR",
    tabScanner: "Diagnostika",
    tabScannerSub: "O'simlik tahlili",
    tabAgronomist: "O'simliklar Tabibi",
    tabAgronomistSub: "Agro-maslahat chat",
    tabCatalog: "Kasalliklar Katalogi",
    tabCatalogSub: "Ensiklopedik baza",
    tabMonitoring: "Fitoxarita",
    tabMonitoringSub: "14 viloyat monitoringi",
    tabHistory: "Tarix & Hisobot",
    tabHistorySub: "Tahlillar arxivi",
    themeBtn: "Mavzu",
    cropLabel: "O'simlik yoki ekin turi:",
    cropAuto: "Avtomatik aniqlash (Har qanday o'simlik, daraxt, gul yoki sabzavot)",
    cropTomato: "Pomidor & Sabzavotlar (Tomorqa ekinlari)",
    cropCucumber: "Bodring & Poliz ekinlari (Qovun, Tarvuz)",
    cropFruitTree: "Mevali daraxtlar (Olma, Shaftoli, O'rik, Gilos, Anor)",
    cropPotato: "Kartoshka, Baqlajon & Qalampir",
    cropHouseplant: "Xona gullari & Manzarali o'simliklar",
    cropGrape: "Uzum / Tokzor (Vitis vinifera)",
    cropCotton: "Paxta / G'oza (Dala ekini)",
    samplesHeading: "O'simlik namunalarini tezkor tekshirish (Live Benchmarks):",
    samplesHint: "Bitta bosishda 80ms tahlil",
    dropzonePrompt: "O'simlik, meva, gul yoki barg fotosuratini yuklang",
    dropzoneSub: "Tomorqa, mevali daraxt, sabzavot, gul yoki ekin fotosuratini to'g'ridan-to'g'ri oling",
    btnCapture: "Rasm yuklash / Suratga olish",
    claheLabel: "Quyosh nuri va soyaning ta'sirini kamaytirish (CLAHE Filter)",
    btnCompare: "Filtr taqqoslash",
    btnDiagnose: "Tahlil qilish (Analyze Specimen)",
    threatLevel: "BIOLOGIK XAVF DARAJASI (THREAT LEVEL):",
    confidence: "AI ISHONCH KO'RSATKICHI:",
    advisoryTitle: "Mutaxassis xulosasi va maslahati:",
    voiceReadBtn: "Tinglash",
    abioticHeading: "Kuyish va Issiq Urishidan Farqlash (Diagnostic Reasoning):",
    biomarkersHeading: "Aniqlangan patologik belgilar (Visual Biomarkers):",
    interventionsHeading: "Zudlik Bilan Amalga Oshiriladigan 3 Ta Qulay Chora:",
    interventionsSub: "Oddiy, arzon va uyda yoki eng yaqin do'konda topiladigan choralar",
    differentialLabel: "Ehtimoliy o'xshash kasallik (Differential Diagnosis):",
    askBannerTitle: "Ushbu kasallik bo'yicha qo'shimcha savolingiz bormi?",
    askBannerSub: "O'simliklar tabibi bilan bevosita onlayn suhbatlashing",
    askBannerBtn: "Tabibga savol berish",
    footerNote: "O'zbekiston aholisi, tomorqa egalari va dehqonlar uchun xalqona ishlab chiqilgan",
    modalTitle: "Quyosh nuri va soya filtrini taqqoslash (CLAHE vs Raw)",
    rawLabel: "Asl fotosurat (Dala nurlari va qattiq soya):",
    claheLabelModal: "CLAHE filtri (Yorug'lik normallashgan):",
    claheActiveNotice: "Filtr faol: Fotosurat quyosh nuri va soyaning ta'siridan avtomatik tozalanadi.",
    modalProceed: "Tahlilni boshlash (Diagnostika) →",
    modalClose: "✕ Oynani yopish",
    blurSharp: "Aniqlik: A'lo ✓",
    blurBlurry: "Diqqat: Xira tasvir",
    glareNormal: "Yorug'lik: Optimal ✓",
    glareExcess: "Quyosh nuri: CLAHE bilan to'g'rilandi ✓",
    analyzing: "O'simlik tahlil qilinmoqda...",
    chatTitle: "Aurora O'simliklar Tabibi (AI Maslahatchi)",
    chatSubtitle: "Tomorqa, bog'dorchilik, xona gullari va dehqonchilik bo'yicha 24/7 onlayn konsultatsiya",
    chatPlaceholder: "O'simlik yoki daraxt haqida savol bering (masalan: Pomidor barglari qorayib quryapti, nima qilay?)...",
    chatWelcome: "<strong>Assalomu alaykum, aziz yurtdoshim! Xush kelibsiz!</strong><p>Men Aurora — o'simliklar shifokori va bosh agronomiman. Hovlingizdagi mevali daraxtlar (olma, shaftoli, uzum), tomorqadagi sabzavotlar (pomidor, bodring), xona gullari yoki ekinlaringizdagi har qanday kasallik va parvarish bo'yicha yordam berishga tayyorman. Savolingizni bemalol yozing!</p>",
    catalogTitle: "O'simliklar va Bog' Kasalliklari Ensiklopediyasi",
    catalogSubtitle: "Tomorqa sabzavotlari, mevali daraxtlar, tokzor va dala ekinlari spravochnigi",
    filterAll: "Barchasi",
    filterVeg: "Sabzavotlar",
    filterFruit: "Mevali daraxtlar",
    filterCotton: "Paxta",
    filterGrape: "Uzum",
    monitoringTitle: "O'zbekiston Fitomonitoring Xaritasi (14 Hudud)",
    monitoringSubtitle: "Real vaqt rejimida viloyatlar bo'yicha kasallik tarqalish xavfi va ob-havo ogohlantirishlari",
    monitoringBadge: "● JONLI MONITORING",
    historyTitle: "O'simliklar Tahlili Tarixi & Xulosa",
    historySubtitle: "Sessiyada o'tkazilgan tahlillar va chop etiladigan fitosanitar dalolatnoma",
    btnPrintReport: "Xulosani Chop Etish (PDF)",
    emptyHistory: "Hozircha hech qanday tahlil o'tkazilmadi. Diagnostika bo'limida o'simlik suratini tahlil qiling."
  },
  en: {
    subtitle: "Universal AI Plant Doctor & Agronomist for Gardens, Trees, Vegetables & Crops",
    navSections: "SECTIONS",
    tabScanner: "Diagnostics",
    tabScannerSub: "Plant Pathology",
    tabAgronomist: "Plant Doctor",
    tabAgronomistSub: "AI Garden & Crop Chat",
    tabCatalog: "Disease Catalog",
    tabCatalogSub: "Plant Encyclopedia",
    tabMonitoring: "Phytomap",
    tabMonitoringSub: "14-Region Monitoring",
    tabHistory: "Audit & Report",
    tabHistorySub: "Audit & Archives",
    themeBtn: "Theme",
    cropLabel: "Target Plant / Crop Selection:",
    cropAuto: "Auto-detect (Any Plant, Tree, Flower or Crop)",
    cropTomato: "Tomato & Backyard Vegetables",
    cropCucumber: "Cucumber, Melons & Squash",
    cropFruitTree: "Fruit Trees (Apple, Peach, Apricot, Cherry)",
    cropPotato: "Potato, Eggplant & Peppers",
    cropHouseplant: "Houseplants & Ornamental Flowers",
    cropGrape: "Grapevine Foliage (Vitis vinifera)",
    cropCotton: "Cotton Foliage (Gossypium)",
    samplesHeading: "Live Plant & Crop Benchmarks:",
    samplesHint: "1-Click Instant Sub-100ms Inference",
    dropzonePrompt: "Upload or capture plant, fruit, flower, or leaf photo",
    dropzoneSub: "Snap a clear photo of any diseased garden vegetable, fruit tree, flower, or crop",
    btnCapture: "Upload Photo / Camera Capture",
    claheLabel: "Suppress solar glare & shadow clipping (CLAHE Filter)",
    btnCompare: "Compare Filter",
    btnDiagnose: "Analyze Plant Specimen",
    threatLevel: "BIOLOGICAL THREAT VECTOR:",
    confidence: "AI DIAGNOSTIC CERTAINTY:",
    advisoryTitle: "Plant Doctor Field Advisory:",
    voiceReadBtn: "Listen",
    abioticHeading: "Pathogen vs Heat/Water Stress Reasoning:",
    biomarkersHeading: "Identified Pathological Biomarkers:",
    interventionsHeading: "3 Immediate Low-Cost Actionable Field Steps:",
    interventionsSub: "Household & generic remedies accessible in local markets or home",
    differentialLabel: "Differential Diagnosis (Lookalike Condition):",
    askBannerTitle: "Do you have further questions on this diagnosis?",
    askBannerSub: "Consult directly with our autonomous plant doctor",
    askBannerBtn: "Ask Plant Doctor",
    footerNote: "Engineered for households, gardeners, and growers across Uzbekistan",
    modalTitle: "Solar Glare & Shadow Filter Comparison (CLAHE vs Raw)",
    rawLabel: "Raw Upload (With midday sun and harsh shadows):",
    claheLabelModal: "CLAHE Enhanced (Normalized contrast matrix):",
    claheActiveNotice: "Filter active: Midday solar glare and shadows are automatically normalized.",
    modalProceed: "Run Diagnostic Analysis →",
    modalClose: "✕ Close Window",
    blurSharp: "Sharpness: Optimal ✓",
    blurBlurry: "Warning: Blurry Image",
    glareNormal: "Lighting: Optimal ✓",
    glareExcess: "Solar Glare: Normalized by CLAHE ✓",
    analyzing: "Scanning & Analyzing Plant Specimen...",
    chatTitle: "Aurora Plant Doctor & Senior Agronomist",
    chatSubtitle: "24/7 autonomous consultation tailored to home gardens, trees, flowers & crops",
    chatPlaceholder: "Ask about any plant, tree, or vegetable (e.g. how to treat tomato late blight?)...",
    chatWelcome: "<strong>Welcome, esteemed grower & plant lover!</strong><p>I am Aurora, Chief Plant Doctor and Senior Agronomist. I am ready to assist you 24/7 with backyard fruit trees (apple, peach, grape), vegetables (tomatoes, cucumbers), indoor flowers, or field crops. Ask any plant care or disease question!</p>",
    catalogTitle: "Plant, Garden & Orchard Disease Encyclopedia",
    catalogSubtitle: "Field reference for backyard vegetables, fruit orchards, vineyards, and cash crops",
    filterAll: "All",
    filterVeg: "Vegetables",
    filterFruit: "Fruit Trees",
    filterCotton: "Cotton",
    filterGrape: "Grape",
    monitoringTitle: "Uzbekistan Phytomonitoring Map (14 Territories)",
    monitoringSubtitle: "Real-time territorial epidemic risk levels and microclimate alerts",
    monitoringBadge: "● LIVE MONITORING",
    historyTitle: "Plant Audit History & Certificate",
    historySubtitle: "Diagnostic session logs and printable phytosanitary acts",
    btnPrintReport: "Print Certificate (PDF)",
    emptyHistory: "No diagnostic scans recorded yet. Scan a plant specimen in Diagnostics."
  }
};

let currentLang = "uz";
let currentTheme = "dark";
let currentFile = null;
let currentPreviewData = null;
let isCurrentSample = false;
let currentSampleId = null;
let lastDiagnosis = null;
let lastDiagnosisPayload = null;
let scanHistory = [];
let diseaseCatalogData = [];
let phytosanitaryRegionsData = [];
let activeCatalogFilter = "ALL";

// DOM Elements
const fileInput = document.getElementById("fileInput");
const dropZone = document.getElementById("dropZone");
const dropContent = document.getElementById("dropContent");
const previewWrapper = document.getElementById("previewWrapper");
const previewImage = document.getElementById("previewImage");
const resetBtn = document.getElementById("resetBtn");
const selectFileBtn = document.getElementById("selectFileBtn");
const diagnoseBtn = document.getElementById("diagnoseBtn");
const diagnoseBtnText = document.getElementById("diagnoseBtnText");
const diagnoseSpinner = document.getElementById("diagnoseSpinner");
const resultsCard = document.getElementById("resultsCard");
const cropSelect = document.getElementById("cropSelect");
const regionSelect = document.getElementById("regionSelect");
const claheToggle = document.getElementById("claheToggle");
const blurIndicator = document.getElementById("blurIndicator");
const glareIndicator = document.getElementById("glareIndicator");
const compareBtn = document.getElementById("compareBtn");
const compareModal = document.getElementById("compareModal");
const modalCloseBtn = document.getElementById("modalCloseBtn");
const modalCloseBtnBottom = document.getElementById("modalCloseBtnBottom");
const modalProceedBtn = document.getElementById("modalProceedBtn");
const rawPreviewModal = document.getElementById("rawPreviewModal");
const clahePreviewModal = document.getElementById("clahePreviewModal");
const langToggle = document.getElementById("langToggle");
const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");
const samplesGrid = document.getElementById("samplesGrid");

// Multi-page navigation elements
const navTabs = document.querySelectorAll(".nav-tab");
const tabPanes = document.querySelectorAll(".tab-pane");

// Chat elements
const chatForm = document.getElementById("chatForm");
const chatInput = document.getElementById("chatInput");
const chatMessages = document.getElementById("chatMessages");
const quickPromptBtns = document.querySelectorAll(".quick-prompt-btn");
const askAgronomistShortcut = document.getElementById("askAgronomistShortcut");
const voiceReadBtn = document.getElementById("voiceReadBtn");

// Catalog & Monitoring elements
const catalogGrid = document.getElementById("catalogGrid");
const filterBtns = document.querySelectorAll(".filter-btn");
const monitoringGrid = document.getElementById("monitoringGrid");
const historyList = document.getElementById("historyList");
const emptyHistoryMsg = document.getElementById("emptyHistoryMsg");
const printReportBtn = document.getElementById("printReportBtn");

// Initialize on DOM Ready
function initAurora() {
  initTheme();
  loadHealthStatus();
  loadApiKeyStatus();
  loadSampleCases();
  loadCatalog();
  loadPhytosanitaryMap();
  bindEvents();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initAurora);
} else {
  initAurora();
}

// Theme Management
function initTheme() {
  const saved = localStorage.getItem("aurora-theme") || "dark";
  setTheme(saved);
}

function setTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("aurora-theme", theme);
  if (themeIcon) {
    if (theme === "dark") {
      themeIcon.innerHTML = `<svg class="ctrl-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`;
    } else {
      themeIcon.innerHTML = `<svg class="ctrl-icon-svg" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
    }
  }
}

function toggleTheme() {
  const next = currentTheme === "dark" ? "light" : "dark";
  setTheme(next);
}

function bindEvents() {
  // Navigation Tabs Switching
  navTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const targetTab = tab.getAttribute("data-tab");
      switchTab(targetTab);
    });
  });

  // Theme switcher
  themeToggle.addEventListener("click", toggleTheme);

  // File upload
  selectFileBtn.addEventListener("click", () => fileInput.click());
  fileInput.addEventListener("change", handleFileSelect);

  // Clicking anywhere inside dropzone opens file dialog
  dropZone.addEventListener("click", (e) => {
    if (e.target.closest("#resetBtn") || !previewWrapper.classList.contains("hidden")) return;
    fileInput.click();
  });

  // Drag & drop
  dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("dragover");
  });
  dropZone.addEventListener("dragleave", () => dropZone.classList.remove("dragover"));
  dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("dragover");
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0], true, false);
    }
  });

  // Reset
  resetBtn.addEventListener("click", resetUpload);

  // Diagnose trigger
  diagnoseBtn.addEventListener("click", runDiagnosis);

  // Filter comparison modal logic
  compareBtn.addEventListener("click", () => {
    if (currentPreviewData && currentPreviewData.raw_preview) {
      rawPreviewModal.src = currentPreviewData.raw_preview;
      clahePreviewModal.src = currentPreviewData.enhanced_preview;
      compareModal.classList.remove("hidden");
      compareModal.style.display = "flex";
    } else if (currentFile) {
      rawPreviewModal.src = URL.createObjectURL(currentFile);
      clahePreviewModal.src = URL.createObjectURL(currentFile);
      compareModal.classList.remove("hidden");
      compareModal.style.display = "flex";
    }
  });

  function closeCompareModal() {
    compareModal.classList.add("hidden");
    compareModal.style.display = "none";
  }

  modalCloseBtn.addEventListener("click", closeCompareModal);
  if (modalCloseBtnBottom) {
    modalCloseBtnBottom.addEventListener("click", closeCompareModal);
  }

  if (modalProceedBtn) {
    modalProceedBtn.addEventListener("click", () => {
      closeCompareModal();
      runDiagnosis();
    });
  }

  // Close modal on outside backdrop click
  compareModal.addEventListener("click", (e) => {
    if (e.target === compareModal) {
      closeCompareModal();
    }
  });

  // Close modal on Escape key press
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeCompareModal();
    }
  });

  // Live CLAHE toggle: switches preview on the fly
  claheToggle.addEventListener("change", () => {
    if (currentPreviewData && previewImage) {
      if (claheToggle.checked && currentPreviewData.enhanced_preview) {
        previewImage.src = currentPreviewData.enhanced_preview;
      } else if (currentFile) {
        previewImage.src = URL.createObjectURL(currentFile);
      }
    }
  });

  // Region change updates HUD GPS coordinates if present
  if (regionSelect) {
    regionSelect.addEventListener("change", handleRegionChange);
    handleRegionChange();
  }

  // Language toggle
  langToggle.addEventListener("click", toggleLanguage);

  // Agronomist Chat
  chatForm.addEventListener("submit", handleChatSubmit);
  quickPromptBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const q = currentLang === "en"
        ? (btn.getAttribute("data-q-en") || btn.getAttribute("data-q"))
        : (btn.getAttribute("data-q-uz") || btn.getAttribute("data-q"));
      chatInput.value = q;
      handleChatSubmit(new Event("submit"));
    });
  });

  // Ask Agronomist Shortcut
  if (askAgronomistShortcut) {
    askAgronomistShortcut.addEventListener("click", () => {
      switchTab("tab-agronomist");
      if (lastDiagnosis) {
        if (currentLang === "en") {
          const dName = lastDiagnosis.primary_diagnosis.common_name_en;
          chatInput.value = `My crop was diagnosed with ${dName}. What is the most effective low-cost local remedy?`;
        } else {
          const dName = lastDiagnosis.primary_diagnosis.common_name_uz;
          chatInput.value = `Mening ekinimda ${dName} aniqlandi. Bunga qarshi eng arzon va tez samara beradigan chorani ayting?`;
        }
        chatInput.focus();
      }
    });
  }

  // Voice Read
  if (voiceReadBtn) {
    voiceReadBtn.addEventListener("click", speakAdvisory);
  }

  // Catalog Filters
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const f = btn.getAttribute("data-filter");
      activeCatalogFilter = f;
      renderCatalog(f);
    });
  });

  // Print Report
  if (printReportBtn) {
    printReportBtn.addEventListener("click", () => window.print());
  }

  // API Key Modal
  const apiKeyToggleBtn = document.getElementById("apiKeyToggleBtn");
  const apiKeyModal = document.getElementById("apiKeyModal");
  const apiKeyModalCloseBtn = document.getElementById("apiKeyModalCloseBtn");
  const apiKeyCancelBtn = document.getElementById("apiKeyCancelBtn");
  const apiKeySaveBtn = document.getElementById("apiKeySaveBtn");
  const apiKeyInput = document.getElementById("apiKeyInput");
  const apiKeySaveStatus = document.getElementById("apiKeySaveStatus");

  function openApiKeyModal() {
    if (apiKeyModal) {
      apiKeyModal.classList.remove("hidden");
      apiKeyModal.style.display = "flex";
      if (apiKeyInput) apiKeyInput.focus();
    }
  }

  function closeApiKeyModal() {
    if (apiKeyModal) {
      apiKeyModal.classList.add("hidden");
      apiKeyModal.style.display = "none";
      if (apiKeySaveStatus) apiKeySaveStatus.style.display = "none";
    }
  }

  if (apiKeyToggleBtn) apiKeyToggleBtn.addEventListener("click", openApiKeyModal);
  if (apiKeyModalCloseBtn) apiKeyModalCloseBtn.addEventListener("click", closeApiKeyModal);
  if (apiKeyCancelBtn) apiKeyCancelBtn.addEventListener("click", closeApiKeyModal);

  if (apiKeySaveBtn) {
    apiKeySaveBtn.addEventListener("click", async () => {
      const key = apiKeyInput.value.trim();
      if (!key) {
        alert("Iltimos, API kalitini kiriting.");
        return;
      }
      apiKeySaveBtn.disabled = true;
      apiKeySaveBtn.textContent = "Saqlanmoqda...";
      try {
        const res = await fetch("/api/set-api-key", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ api_key: key })
        });
        const d = await res.json();
        if (res.ok) {
          apiKeySaveStatus.style.display = "block";
          apiKeySaveStatus.style.color = "#10b981";
          apiKeySaveStatus.textContent = "✓ " + d.message;
          await loadApiKeyStatus();
          setTimeout(() => {
            closeApiKeyModal();
            apiKeySaveBtn.disabled = false;
            apiKeySaveBtn.textContent = "Saqlash & Faollashtirish ✓";
          }, 1200);
        } else {
          throw new Error(d.detail || "Xatolik yuz berdi");
        }
      } catch (err) {
        apiKeySaveStatus.style.display = "block";
        apiKeySaveStatus.style.color = "#ef4444";
        apiKeySaveStatus.textContent = "Xato: " + err.message;
        apiKeySaveBtn.disabled = false;
        apiKeySaveBtn.textContent = "Saqlash & Faollashtirish ✓";
      }
    });
  }
}

// Check and update Gemini API Key status indicator
async function loadApiKeyStatus() {
  try {
    const res = await fetch("/api/api-key-status");
    if (!res.ok) return;
    const data = await res.json();
    const dot = document.getElementById("apiKeyDot");
    const text = document.getElementById("apiKeyStatusText");
    if (dot && text) {
      if (data.configured) {
        dot.style.background = "#10b981";
        text.textContent = currentLang === "en" ? "Gemini AI (Active ✓)" : "Gemini AI (Faol ✓)";
      } else {
        dot.style.background = "#f59e0b";
        text.textContent = currentLang === "en" ? "Connect Gemini AI" : "AI Kaliti (Sozlash)";
      }
    }
  } catch (e) {
    console.warn("Could not check API key status:", e);
  }
}

// Tab Switching
function switchTab(tabId) {
  navTabs.forEach((t) => {
    if (t.getAttribute("data-tab") === tabId) {
      t.classList.add("active");
    } else {
      t.classList.remove("active");
    }
  });

  tabPanes.forEach((pane) => {
    if (pane.id === tabId) {
      pane.classList.remove("hidden");
      pane.classList.add("active");
    } else {
      pane.classList.add("hidden");
      pane.classList.remove("active");
    }
  });

  window.scrollTo({ top: 0, behavior: "smooth" });
}

function handleRegionChange() {
  // Region changed callback
}

// Health status check
async function loadHealthStatus() {
  try {
    await fetch("/api/health");
  } catch (err) {
    console.warn("Health check error:", err);
  }
}

// Load sample cases
async function loadSampleCases() {
  try {
    const res = await fetch("/api/sample-cases");
    const data = await res.json();
    samplesGrid.innerHTML = "";

    data.cases.forEach((item) => {
      const el = document.createElement("div");
      el.className = "sample-item";
      el.innerHTML = `
        <img class="sample-thumb" src="${item.image_url}" alt="${item.title_en}" />
        <div class="sample-info">
          <h4>${currentLang === "uz" ? item.title_uz : item.title_en}</h4>
          <span class="sample-tag tag-${item.expected_threat.toLowerCase()}">${item.expected_threat}</span>
        </div>
      `;
      el.addEventListener("click", () => loadSampleIntoWorkspace(item));
      samplesGrid.appendChild(el);
    });
  } catch (err) {
    console.error("Failed to load sample cases:", err);
  }
}

// Handle clicking a sample case
async function loadSampleIntoWorkspace(sample) {
  try {
    currentSampleId = sample.id;
    cropSelect.value = sample.crop;
    const res = await fetch(sample.image_url);
    const blob = await res.blob();
    const file = new File([blob], `${sample.id}.jpg`, { type: "image/jpeg" });
    handleFile(file, true, true);
  } catch (err) {
    console.error("Error loading sample:", err);
  }
}

function handleFileSelect(e) {
  if (e.target.files && e.target.files[0]) {
    currentSampleId = null;
    handleFile(e.target.files[0], true, false);
  }
}

function handleFile(file, autoRun = false, isSample = false) {
  currentFile = file;
  isCurrentSample = isSample;
  if (!isSample) {
    currentSampleId = null;
  }

  const objectUrl = URL.createObjectURL(file);
  previewImage.src = objectUrl;
  dropContent.classList.add("hidden");
  previewWrapper.classList.remove("hidden");
  diagnoseBtn.disabled = false;

  fetchPreflightQuality(file, autoRun);
}

async function fetchPreflightQuality(file, autoRun = false) {
  try {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/api/preprocess-preview", {
      method: "POST",
      body: formData
    });
    const data = await res.json();
    currentPreviewData = data;
    compareBtn.style.display = "inline-flex";

    // If CLAHE is toggled ON, show enhanced image directly on workspace preview
    if (claheToggle.checked && data.enhanced_preview) {
      previewImage.src = data.enhanced_preview;
    }

    const metrics = data.metrics;
    if (metrics.is_blurry) {
      blurIndicator.textContent = I18N[currentLang].blurBlurry;
      blurIndicator.className = "badge-tag badge-err";
    } else {
      blurIndicator.textContent = `${I18N[currentLang].blurSharp} (${metrics.blur_score})`;
      blurIndicator.className = "badge-tag badge-ok";
    }

    if (metrics.has_excessive_glare) {
      glareIndicator.textContent = `${I18N[currentLang].glareExcess} (${(metrics.glare_ratio * 100).toFixed(1)}%)`;
      glareIndicator.className = "badge-tag badge-warn";
    } else {
      glareIndicator.textContent = I18N[currentLang].glareNormal;
      glareIndicator.className = "badge-tag badge-ok";
    }

    if (autoRun) {
      runDiagnosis();
    }
  } catch (err) {
    console.warn("Preflight check failed:", err);
    if (autoRun) {
      runDiagnosis();
    }
  }
}

function resetUpload() {
  currentFile = null;
  currentPreviewData = null;
  isCurrentSample = false;
  currentSampleId = null;
  fileInput.value = "";
  previewImage.src = "";
  previewWrapper.classList.add("hidden");
  previewWrapper.classList.remove("scanning");
  dropContent.classList.remove("hidden");
  resultsCard.classList.add("hidden");
  diagnoseBtn.disabled = true;
  compareBtn.style.display = "none";
  compareModal.classList.add("hidden");
  compareModal.style.display = "none";
}

async function runDiagnosis() {
  if (!currentFile) return;

  // Always dismiss comparison modal if open
  compareModal.classList.add("hidden");
  compareModal.style.display = "none";

  diagnoseBtn.disabled = true;
  diagnoseSpinner.classList.remove("hidden");
  diagnoseBtnText.textContent = I18N[currentLang].analyzing;
  previewWrapper.classList.add("scanning");

  try {
    const formData = new FormData();
    formData.append("file", currentFile);
    formData.append("crop_hint", cropSelect.value);
    formData.append("region", regionSelect ? regionSelect.value : "Uzbekistan");
    formData.append("enable_clahe", claheToggle.checked);
    formData.append("force_demo", isCurrentSample);
    if (currentSampleId) {
      formData.append("sample_id", currentSampleId);
    }

    const res = await fetch("/api/diagnose", {
      method: "POST",
      body: formData
    });

    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || "Diagnosis failed");
    }

    const payload = await res.json();
    lastDiagnosis = payload.diagnosis;
    lastDiagnosisPayload = payload;
    renderDiagnosis(payload);
    addToHistory(payload);
  } catch (err) {
    alert("Diagnoz xatosi: " + err.message);
  } finally {
    diagnoseBtn.disabled = false;
    diagnoseSpinner.classList.add("hidden");
    diagnoseBtnText.textContent = I18N[currentLang].btnDiagnose;
    previewWrapper.classList.remove("scanning");
  }
}

function renderDiagnosis(data) {
  const diag = data.diagnosis;
  resultsCard.classList.remove("hidden");

  // Smooth scroll into results HUD
  resultsCard.scrollIntoView({ behavior: "smooth", block: "start" });

  // Threat Level Badge
  const threatPill = document.getElementById("threatPill");
  threatPill.textContent = diag.threat_level;
  threatPill.className = `threat-pill threat-${diag.threat_level}`;

  // Confidence Meter
  const confPct = Math.round(diag.confidence_score * 100);
  document.getElementById("confValue").textContent = `${confPct}%`;
  document.getElementById("confBarFill").style.width = `${confPct}%`;

  // Host & Pathogen Chips
  document.getElementById("pathogenType").textContent = diag.primary_diagnosis.pathogen_type;
  document.getElementById("hostCropChip").textContent = diag.specimen_identified.replace("_", " ");
  
  if (currentLang === "en") {
    document.getElementById("diseaseNameUz").textContent = diag.primary_diagnosis.common_name_en;
    document.getElementById("diseaseScientific").textContent = diag.primary_diagnosis.scientific_name;
    document.getElementById("diseaseNameEn").textContent = diag.primary_diagnosis.common_name_uz;
    document.getElementById("advisoryUzText").textContent = diag.farmer_advisory_english || diag.farmer_advisory_uzbek;
    document.getElementById("modeBadge").textContent = data.mode === "live" ? "ENGINE: LIVE AI" : "ENGINE: READY";
    document.getElementById("qualityStatusBadge").textContent = "STATUS: OPTIMAL";
  } else {
    document.getElementById("diseaseNameUz").textContent = diag.primary_diagnosis.common_name_uz;
    document.getElementById("diseaseScientific").textContent = diag.primary_diagnosis.scientific_name;
    document.getElementById("diseaseNameEn").textContent = diag.primary_diagnosis.common_name_en;
    document.getElementById("advisoryUzText").textContent = diag.farmer_advisory_uzbek;
    document.getElementById("modeBadge").textContent = data.mode === "live" ? "TIZIM: JONLI" : "TIZIM: TAYYOR";
    document.getElementById("qualityStatusBadge").textContent = "HOLAT: MAQBUL";
  }

  // Abiotic vs Biotic Reasoning
  document.getElementById("abioticAssessment").textContent = diag.abiotic_vs_biotic_assessment;

  // Visual Biomarkers
  const biomarkersList = document.getElementById("biomarkersList");
  biomarkersList.innerHTML = "";
  diag.visual_biomarkers.forEach((marker) => {
    const span = document.createElement("span");
    span.className = "biomarker-tag";
    span.textContent = marker;
    biomarkersList.appendChild(span);
  });

  // 3 Immediate Interventions
  const interventionsList = document.getElementById("interventionsList");
  interventionsList.innerHTML = "";
  diag.immediate_low_cost_interventions.forEach((step) => {
    const card = document.createElement("div");
    card.className = "step-card";
    const title = currentLang === "uz" ? step.title_uz : step.title_en;
    card.innerHTML = `
      <div class="step-num">${step.step_number}</div>
      <div class="step-content">
        <h5>${title}</h5>
        <p>${step.action_description}</p>
        <span class="cost-tag cost-${step.cost_category}">${formatCostCategory(step.cost_category)}</span>
      </div>
    `;
    interventionsList.appendChild(card);
  });

  // Differential Diagnosis
  document.getElementById("differentialText").textContent = diag.differential_diagnosis;

  // Latency
  const latencyBadge = document.getElementById("latencyBadge");
  if (latencyBadge) {
    latencyBadge.innerHTML = `
      <svg class="metric-icon-svg" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
      </svg>
      <span id="latencyVal">${data.latency_ms} ms</span>
    `;
  }
}

function formatCostCategory(cat) {
  const map = {
    ZERO_COST: currentLang === "uz" ? "BEPUL (0 SO'M)" : "ZERO COST (CULTURAL)",
    LOW_COST_LOCAL_REMEDY: currentLang === "uz" ? "ARZON / MAHALLIY BOZOR" : "LOW-COST BAZAAR REMEDY",
    STANDARD_FUNGICIDE_BACTERICIDE: currentLang === "uz" ? "STANDART PREPARAT" : "STANDARD TREATMENT"
  };
  return map[cat] || cat;
}

// Speak Advisory via Web Speech Synthesis
function speakAdvisory() {
  if (!('speechSynthesis' in window)) {
    alert("Brauzeringiz ovozli eshittirishni qo'llab-quvvatlamaydi.");
    return;
  }
  const text = document.getElementById("advisoryUzText").textContent;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "uz-UZ";
  utterance.rate = 0.95;
  window.speechSynthesis.speak(utterance);
}

// ==========================================================================
// AI AGRONOMIST CHAT
// ==========================================================================
async function handleChatSubmit(e) {
  e.preventDefault();
  const q = chatInput.value.trim();
  if (!q) return;

  // Add user bubble
  appendChatBubble("user", q);
  chatInput.value = "";

  // Add typing bubble
  const typingText = currentLang === "en" ? "Agronomist is analyzing..." : "Agronom tahlil qilmoqda...";
  const typingBubble = appendChatBubble(
    "assistant",
    `<span class="typing-bubble"><span class="typing-dots"><span></span><span></span><span></span></span><span>${typingText}</span></span>`
  );

  try {
    const cropHint = cropSelect.value;
    const diseaseHint = lastDiagnosis
      ? (currentLang === "en" ? lastDiagnosis.primary_diagnosis.common_name_en : lastDiagnosis.primary_diagnosis.common_name_uz)
      : null;

    const res = await fetch("/api/agronomist-chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: q,
        crop: cropHint,
        disease: diseaseHint,
        lang: currentLang
      })
    });

    const data = await res.json();
    typingBubble.innerHTML = formatMarkdownText(data.answer);
  } catch (err) {
    typingBubble.textContent = currentLang === "en"
      ? "An error occurred. Please try again."
      : "Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.";
  }
}

function appendChatBubble(role, content) {
  const msgEl = document.createElement("div");
  msgEl.className = `chat-msg msg-${role}`;
  if (role === "assistant") {
    const avatar = document.createElement("img");
    avatar.className = "msg-avatar-img";
    avatar.src = "/images/agronomist_avatar.jpg";
    avatar.alt = "Aurora Dala Agronomi";
    msgEl.appendChild(avatar);
  }
  const bubble = document.createElement("div");
  bubble.className = "msg-bubble";
  bubble.innerHTML = formatMarkdownText(content);
  msgEl.appendChild(bubble);
  chatMessages.appendChild(msgEl);
  chatMessages.scrollTop = chatMessages.scrollHeight;
  return bubble;
}

function formatMarkdownText(text) {
  if (!text) return "";
  return text
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/\n\n/g, "<p></p>")
    .replace(/\n/g, "<br/>");
}

// ==========================================================================
// DISEASE ENCYCLOPEDIA CATALOG
// ==========================================================================
async function loadCatalog() {
  try {
    const res = await fetch("/api/disease-catalog");
    const data = await res.json();
    diseaseCatalogData = data.catalog;
    renderCatalog(activeCatalogFilter);
  } catch (err) {
    console.error("Error loading catalog:", err);
  }
}

function renderCatalog(filter) {
  if (!catalogGrid) return;
  activeCatalogFilter = filter || activeCatalogFilter || "ALL";
  catalogGrid.innerHTML = "";

  const items = diseaseCatalogData.filter((item) => {
    if (activeCatalogFilter === "ALL") return true;
    return (
      item.crop.includes(activeCatalogFilter) ||
      (item.crop_en && item.crop_en.toLowerCase().includes(activeCatalogFilter.toLowerCase()))
    );
  });

  const isEn = currentLang === "en";

  items.forEach((item) => {
    const card = document.createElement("div");
    card.className = "catalog-card";
    const name = isEn ? (item.name_en || item.name_uz) : item.name_uz;
    const cropText = isEn ? (item.crop_en || item.crop) : item.crop;
    const signs = isEn ? (item.visual_signs_en || item.visual_signs_uz) : item.visual_signs_uz;
    const season = isEn ? (item.calendar_season_en || item.calendar_season_uz) : item.calendar_season_uz;
    const dosage = isEn ? (item.recommended_dosage_en || item.recommended_dosage_uz) : item.recommended_dosage_uz;
    const signsLabel = isEn ? "Symptoms:" : "Belgilari:";
    const seasonSvg = `<svg class="inline-cat-svg" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>`;
    const seasonLabel = isEn ? `${seasonSvg} Season:` : `${seasonSvg} Mavsum:`;
    const dosageLabel = isEn ? "Recommended treatment:" : "Tavsiya me'yori:";

    const imgHtml = item.image_url
      ? `<div class="catalog-thumb-wrap"><img class="catalog-thumb" src="${item.image_url}" alt="${name}" loading="lazy" /></div>`
      : "";

    card.innerHTML = `
      ${imgHtml}
      <div class="catalog-card-header">
        <span class="crop-badge">${cropText}</span>
        <span class="threat-pill threat-${item.threat_level}" style="font-size: 10px; padding: 2px 8px;">${item.threat_level}</span>
      </div>
      <h4>${name}</h4>
      <p class="scientific-name-sm mono">${item.scientific_name}</p>
      <div class="catalog-info-row">
        <p><strong>${signsLabel}</strong> ${signs}</p>
        <span class="calendar-strip">${seasonLabel} ${season}</span>
        <div class="dosage-callout">
          <strong>${dosageLabel}</strong> ${dosage}
        </div>
      </div>
    `;
    catalogGrid.appendChild(card);
  });
}

// ==========================================================================
// PHYTOSANITARY MAP & CLIMATE RISKS
// ==========================================================================
async function loadPhytosanitaryMap() {
  try {
    const res = await fetch("/api/phytosanitary-map");
    const data = await res.json();
    phytosanitaryRegionsData = data.regions;
    renderPhytosanitaryMap(phytosanitaryRegionsData);
  } catch (err) {
    console.error("Error loading map data:", err);
  }
}

function renderPhytosanitaryMap(regions) {
  if (!monitoringGrid) return;
  const data = regions || phytosanitaryRegionsData;
  if (!data || data.length === 0) return;
  monitoringGrid.innerHTML = "";

  const isEn = currentLang === "en";

  data.forEach((reg) => {
    const card = document.createElement("div");
    card.className = "region-risk-card";
    const regionName = isEn ? (reg.region_name_en || reg.region_name) : reg.region_name;
    const threat = isEn ? (reg.active_threat_en || reg.active_threat) : reg.active_threat;
    const advice = isEn ? (reg.advice_en || reg.advice_uz) : reg.advice_uz;
    const humidityLabel = isEn ? "Humidity:" : "Namlik:";

    card.innerHTML = `
      <div class="region-top">
        <span class="region-name-txt">${regionName}</span>
        <span class="risk-pill risk-${reg.risk_level}">${reg.risk_level}</span>
      </div>
      <div class="region-weather mono">
        <span>
          <svg class="inline-weather-svg" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/>
          </svg>
          ${reg.temperature}
        </span>
        <span>
          <svg class="inline-weather-svg" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/>
          </svg>
          ${humidityLabel} ${reg.humidity}
        </span>
      </div>
      <p class="region-threat-alert">
        <svg class="inline-alert-svg" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
          <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
          <line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>
        </svg>
        ${threat}
      </p>
      <p class="region-advice">${advice}</p>
    `;
    card.addEventListener("click", () => {
      if (regionSelect) {
        regionSelect.value = reg.region_name;
        handleRegionChange();
      }
      switchTab("tab-scanner");
    });
    monitoringGrid.appendChild(card);
  });
}

// ==========================================================================
// SCAN HISTORY & REPORT AUDIT
// ==========================================================================
function addToHistory(payload) {
  const diag = payload.diagnosis;
  const item = {
    id: Date.now(),
    crop: payload.crop_hint || diag.specimen_identified,
    disease_uz: diag.primary_diagnosis.common_name_uz,
    disease_en: diag.primary_diagnosis.common_name_en,
    threat: diag.threat_level,
    confidence: Math.round(diag.confidence_score * 100),
    time: new Date().toLocaleTimeString(),
    date: new Date().toLocaleDateString()
  };

  scanHistory.unshift(item);
  renderHistory();
}

function renderHistory() {
  if (!historyList) return;
  if (scanHistory.length === 0) {
    if (emptyHistoryMsg) emptyHistoryMsg.style.display = "block";
    return;
  }
  if (emptyHistoryMsg) emptyHistoryMsg.style.display = "none";

  historyList.innerHTML = "";
  const isEn = currentLang === "en";
  const confText = isEn ? "Certainty" : "Ishonch";

  scanHistory.forEach((item) => {
    const card = document.createElement("div");
    card.className = "history-item-card";
    const title = isEn ? (item.disease_en || item.disease_uz) : item.disease_uz;
    card.innerHTML = `
      <div class="hist-left">
        <div>
          <h4 class="hist-title">${title}</h4>
          <p class="hist-meta mono">${item.crop} • ${item.date} ${item.time}</p>
        </div>
      </div>
      <div style="text-align: right;">
        <span class="threat-pill threat-${item.threat}" style="font-size: 10px; padding: 3px 8px;">${item.threat}</span>
        <p class="hist-meta mono" style="margin-top: 4px;">${item.confidence}% ${confText}</p>
      </div>
    `;
    historyList.appendChild(card);
  });
}

// ==========================================================================
// REGIONS TRANSLATION & LANGUAGE TOGGLE
// ==========================================================================
const REGION_I18N = {
  "andijan": { uz: "Andijon viloyati (Andijan)", en: "Andijan Region" },
  "bukhara": { uz: "Buxoro viloyati (Bukhara)", en: "Bukhara Region" },
  "fergana": { uz: "Farg'ona viloyati (Fergana)", en: "Fergana Region" },
  "jizzakh": { uz: "Jizzax viloyati (Jizzakh)", en: "Jizzakh Region" },
  "khorezm": { uz: "Xorazm viloyati (Khorezm)", en: "Khorezm Region" },
  "namangan": { uz: "Namangan viloyati (Namangan)", en: "Namangan Region" },
  "navoiy": { uz: "Navoiy viloyati (Navoi)", en: "Navoi Region" },
  "kashkadarya": { uz: "Qashqadaryo viloyati (Kashkadarya)", en: "Kashkadarya Region" },
  "karakalpakstan": { uz: "Qoraqalpog'iston Respublikasi", en: "Republic of Karakalpakstan" },
  "samarkand": { uz: "Samarqand viloyati (Samarkand)", en: "Samarkand Region" },
  "sirdaryo": { uz: "Sirdaryo viloyati (Syrdarya)", en: "Syrdarya Region" },
  "surkhandarya": { uz: "Surxondaryo viloyati (Surkhandarya)", en: "Surkhandarya Region" },
  "tashkent_region": { uz: "Toshkent viloyati", en: "Tashkent Region" },
  "tashkent_city": { uz: "Toshkent shahri (Agro-voha)", en: "Tashkent City (Suburban)" }
};

function toggleLanguage() {
  currentLang = currentLang === "uz" ? "en" : "uz";
  const flagBadge = langToggle.querySelector(".flag-badge");
  if (flagBadge) {
    flagBadge.textContent = currentLang.toUpperCase();
  }
  const langName = langToggle.querySelector(".lang-name");
  if (langName) {
    langName.textContent = currentLang === "uz" ? "O'zbekcha" : "English";
  }

  // Update all [data-i18n] text nodes
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (I18N[currentLang] && I18N[currentLang][key]) {
      const textSpan = el.querySelector("span[id$='Text']") || el.querySelector(".btn-label");
      if (textSpan) {
        textSpan.textContent = I18N[currentLang][key];
      } else if (el.querySelector(".label-icon")) {
        const iconSpan = el.querySelector(".label-icon").outerHTML;
        el.innerHTML = `${iconSpan} ${I18N[currentLang][key]}`;
      } else if (el.querySelector("svg")) {
        const svgHtml = el.querySelector("svg").outerHTML;
        el.innerHTML = `${svgHtml} <span>${I18N[currentLang][key]}</span>`;
      } else {
        el.textContent = I18N[currentLang][key];
      }
    }
  });

  // Localize crop select dropdown options
  const cropMap = {
    AUTO: "cropAuto",
    TOMATO: "cropTomato",
    CUCUMBER: "cropCucumber",
    FRUIT_TREE: "cropFruitTree",
    POTATO: "cropPotato",
    HOUSEPLANT: "cropHouseplant",
    GRAPE: "cropGrape",
    COTTON: "cropCotton"
  };
  Array.from(cropSelect.options).forEach((opt) => {
    const i18nKey = cropMap[opt.value];
    if (i18nKey && I18N[currentLang] && I18N[currentLang][i18nKey]) {
      opt.textContent = I18N[currentLang][i18nKey];
    }
  });

  // Localize region select options if present
  if (regionSelect) {
    Array.from(regionSelect.options).forEach((opt) => {
      const val = opt.value.toLowerCase();
      for (const [key, names] of Object.entries(REGION_I18N)) {
        if (val.includes(key) || val.includes(names.uz.toLowerCase().substring(0, 5))) {
          opt.textContent = names[currentLang];
          break;
        }
      }
    });
  }

  // Localize quick prompt buttons
  document.querySelectorAll(".quick-prompt-btn").forEach((btn) => {
    const q = currentLang === "en" ? btn.getAttribute("data-q-en") : btn.getAttribute("data-q-uz");
    const lbl = currentLang === "en" ? btn.getAttribute("data-lbl-en") : btn.getAttribute("data-lbl-uz");
    if (q) btn.setAttribute("data-q", q);
    const lblSpan = btn.querySelector(".quick-lbl");
    if (lblSpan && lbl) {
      lblSpan.textContent = lbl;
    } else if (lbl) {
      btn.textContent = lbl;
    }
  });

  // Localize chat input placeholder & welcome greeting
  if (chatInput) chatInput.placeholder = I18N[currentLang].chatPlaceholder;
  const welcomeBubble = document.getElementById("chatWelcomeBubble");
  if (welcomeBubble) welcomeBubble.innerHTML = I18N[currentLang].chatWelcome;

  // Re-render dynamic elements
  loadSampleCases();
  renderCatalog(activeCatalogFilter);
  renderPhytosanitaryMap(phytosanitaryRegionsData);
  renderHistory();
  if (lastDiagnosisPayload) {
    renderDiagnosis(lastDiagnosisPayload);
  }
}
