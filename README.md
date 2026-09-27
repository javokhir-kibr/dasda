# 🌿 Project Aurora — Autonomous Agritech Vision Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688.svg)](https://fastapi.tiangolo.com)
[![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%20API-4285F4.svg)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-Proprietary-green.svg)](#)

**Project Aurora** is an enterprise-grade foliar pathogen diagnostics and agricultural intelligence platform custom-engineered for Uzbekistan's arid and saline agricultural basins (Fergana, Bukhara, Samarkand, Kashkadarya, Surkhandarya, etc.).

---

## 🚀 Key Features

1. **Autonomous Foliar Diagnostics (Sub-100ms Inference):**
   - High-throughput computer vision analysis of cotton (*Gossypium hirsutum*) and grape (*Vitis vinifera*) pathology.
   - Distinct classification of biotic pathogens (bacterial blight, verticillium wilt, powdery mildew, downy mildew, spider mites) vs abiotic stresses (salinity necrosis, midday thermal solar scorch).

2. **Adaptive Contrast Normalization (CLAHE Vision Core):**
   - Contrast Limited Adaptive Histogram Equalization suppresses intense Central Asian midday solar glare and high-contrast canopy shadows.

3. **Autonomous Senior Field Agronomist (AI Chat):**
   - 24/7 bilingual (Uzbek / English) conversational advisory grounded in Uzbek agro-climatic zones, local chemical formulations (O'zagrokimyohimoya), and cost-effective cultural remedies.

4. **14-Territory Dynamic Phytomonitoring Map:**
   - Real-time epidemic risk indices, temperature, humidity, and microclimate pathogen advisories across all 12 regions, Karakalpakstan, and Tashkent.

5. **Agronomic Disease Encyclopedia & Field Certificate Printing:**
   - Offline-capable knowledge base covering visual markers, biology, and verified dosages.
   - 1-click printable farmer phytosanitary audit certificate (PDF format).

6. **Ultra-HD 4K Photographic Assets & Vector UI:**
   - High-resolution documentary photography (`images/`) and pure vector SVG interface with zero cartoon emojis.

---

## 🛠️ Quick Launch

### Prerequisites
- Python 3.10 or higher
- Google Gemini API Key ([Get your free key here](https://aistudio.google.com/)) *(Optional: runs in demo benchmark mode without an API key)*

---

### 🪟 Windows Mode (1-Click Launch)

#### Option A: Double-Click Batch File (Easiest)
Simply double-click **`run.bat`** in File Explorer (or run from CMD):
```cmd
run.bat
```
* **Auto-detects Python**, creates `.venv`, installs requirements, initializes `.env`, and **automatically launches your browser** at `http://localhost:8000`.

#### Option B: PowerShell
Right-click **`run.ps1`** -> "Run with PowerShell", or run in a terminal:
```powershell
.\run.ps1
```
*(Supports `-Port 8080`, `-Reload`, and `-NoBrowser` parameters)*

---

### 🌐 Web Publishing & Cloud Deployments

Project Aurora is fully production-ready and configured for instant web publishing on any cloud host:

#### 1. Render (1-Click Deployment)
- Connect this repository to [Render](https://render.com).
- Render automatically detects the included [`render.yaml`](file:///c:/Users/QE670%20zd/Downloads/Tree-Aurora-main/Tree-Aurora-main/tree%20Ai/render.yaml) blueprint.
- Add `GEMINI_API_KEY` under Environment Variables in the Render dashboard.

#### 2. Railway (Zero-Config)
- Connect the repository to [Railway](https://railway.app).
- Railway auto-builds using the included [`railway.json`](file:///c:/Users/QE670%20zd/Downloads/Tree-Aurora-main/Tree-Aurora-main/tree%20Ai/railway.json) & [`Procfile`](file:///c:/Users/QE670%20zd/Downloads/Tree-Aurora-main/Tree-Aurora-main/tree%20Ai/Procfile).
- Add `GEMINI_API_KEY` under Railway Variables.

#### 3. Docker / Google Cloud Run / AWS App Runner
```bash
# Build the production Docker container
docker build -t aurora-vision .

# Run locally or deploy to container registry
docker run -d -p 8000:8000 --env-file .env --name aurora-app aurora-vision
```
*Note: The containerized `main.py` dynamically binds to `$PORT` required by Cloud Run, Render, and Heroku.*

---

### 🐧 Linux & macOS Launch
```bash
chmod +x run.sh
./run.sh
```
Server starts at `http://localhost:8000`.

---

## 🧪 Verification & Automated Tests

To run the complete test suite:
```bash
source .venv/bin/activate
PYTHONPATH=. pytest tests/test_aurora.py -v
```
All 14 automated unit and integration tests verify:
- Preprocessor contrast enhancement and blur detection
- Gemini AI diagnostic inference and prompt grounding
- Agronomist chat consultation
- Phytosanitary map and disease catalog API endpoints
- Static image serving and error handling

---

## 📁 Repository Structure

```
.
├── aurora/                   # Core Python backend engine
│   ├── api.py                # FastAPI endpoints & routing
│   ├── agronomy_data.py      # Disease catalog & territorial risk database
│   ├── config.py             # App configuration & environment loader
│   ├── engine.py             # Vision diagnostics & Gemini LLM agent
│   ├── preprocessor.py       # CLAHE contrast normalization & quality checks
│   ├── samples/              # High-definition reference benchmark specimens
│   ├── samples_generator.py  # Benchmark asset generator
│   └── schemas.py            # Pydantic data schemas & response models
├── images/                   # 4K resolution field photography & official logo
├── static/                   # Production Web UI (HTML5, modern CSS, vanilla JS)
│   ├── index.html            # Single-page enterprise dashboard
│   ├── styles.css            # Dark/light theme styles & vector SVG rules
│   └── app.js                # Frontend client logic & bilingual localization
├── tests/                    # Automated pytest test suite
│   └── test_aurora.py
├── .env.example              # Environment variable template
├── .gitignore                # Production git ignore configuration
├── Dockerfile                # Production container specification with dynamic PORT
├── Procfile                  # Cloud web process entrypoint (Render/Railway/Heroku)
├── railway.json              # Railway deployment specification
├── render.yaml               # Render 1-click blueprint specification
├── main.py                   # Production ASGI application entrypoint & CLI
├── requirements.txt          # Python dependencies
├── run.bat                   # 🪟 Windows 1-click batch launcher (auto browser)
├── run.ps1                   # 🪟 Windows PowerShell launcher
└── run.sh                    # 🐧 Linux/macOS automated setup & launch script
```

---

## 🔒 Security Notice

Never commit your `.env` file containing the `GEMINI_API_KEY` to public version control. The included `.gitignore` protects secrets from accidental commits.
