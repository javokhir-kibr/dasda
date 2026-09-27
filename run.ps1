# Project Aurora — Windows PowerShell Launcher
param (
    [int]$Port = 8000,
    [string]$Hostname = "0.0.0.0",
    [switch]$Reload,
    [switch]$NoBrowser
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ScriptDir

Write-Host "=====================================================================" -ForegroundColor Green
Write-Host "      Project Aurora - Autonomous Agritech Vision Engine            " -ForegroundColor Cyan
Write-Host "                     (Windows PowerShell Mode)                       " -ForegroundColor DarkGray
Write-Host "=====================================================================" -ForegroundColor Green
Write-Host ""

# 1. Detect Python
$PythonCmd = $null
$PythonArgs = @()

# Test 'py -3'
try {
    $ver = & py -3 --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        $PythonCmd = "py"
        $PythonArgs = @("-3")
    }
} catch {}

# Test 'python'
if (-not $PythonCmd) {
    try {
        $ver = & python --version 2>&1
        if ($LASTEXITCODE -eq 0 -and $ver -match "Python\s+3\.") {
            $PythonCmd = "python"
            $PythonArgs = @()
        }
    } catch {}
}

# Test standard Windows installation paths
if (-not $PythonCmd) {
    $searchPaths = @(
        "$env:LOCALAPPDATA\Programs\Python\Python3*\python.exe",
        "C:\Program Files\Python3*\python.exe",
        "C:\Program Files (x86)\Python3*\python.exe"
    )
    foreach ($p in $searchPaths) {
        $candidate = Get-Item $p -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($candidate) {
            $PythonCmd = $candidate.FullName
            $PythonArgs = @()
            break
        }
    }
}

if (-not $PythonCmd) {
    Write-Host "[!] Python 3.10+ was not found on your system." -ForegroundColor Red
    Write-Host "    Install from: https://www.python.org/downloads/ (check 'Add python.exe to PATH')" -ForegroundColor Yellow
    Write-Host "    Or run: winget install Python.Python.3.11" -ForegroundColor Yellow
    exit 1
}

Write-Host "[*] Detected Python: $PythonCmd $PythonArgs" -ForegroundColor Cyan

# 2. Check .env
if (-not (Test-Path ".env")) {
    if (Test-Path ".env.example") {
        Write-Host "[*] Creating .env from .env.example..." -ForegroundColor DarkYellow
        Copy-Item ".env.example" ".env"
    }
}

# 3. Virtual Environment
$venvPython = Join-Path $ScriptDir ".venv\Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
    Write-Host "[*] Creating virtual environment (.venv)..." -ForegroundColor Yellow
    & $PythonCmd $PythonArgs -m venv .venv
    
    Write-Host "[*] Installing dependencies..." -ForegroundColor Yellow
    & $venvPython -m pip install --upgrade pip
    & $venvPython -m pip install -r requirements.txt
    Write-Host "[OK] Dependencies installed." -ForegroundColor Green
}

# 4. Generate sample assets if missing
if (-not (Test-Path "aurora\samples\cotton_bacterial_blight.jpg")) {
    Write-Host "[*] Generating synthetic diagnostic specimens..." -ForegroundColor DarkCyan
    & $venvPython "aurora\samples_generator.py"
}

# 5. Launch main application
$appArgs = @("main.py", "--host", $Hostname, "--port", $Port)
if ($Reload) { $appArgs += "--reload" }
if ($NoBrowser) { $appArgs += "--no-browser" } else { $appArgs += "--open-browser" }

Write-Host ""
Write-Host "[*] Starting Project Aurora on http://${Hostname}:${Port}..." -ForegroundColor Green
& $venvPython $appArgs
