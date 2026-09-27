@echo off
title Project Aurora - Agritech Vision Engine

echo =====================================================================
echo       Project Aurora - Autonomous Agritech Vision Engine
echo                      (Windows Launch Mode)
echo =====================================================================
echo.

cd /d "%~dp0"

:: 1. Search for Python
set "PY_CMD="

python --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PY_CMD=python"
    goto :PYTHON_FOUND
)

py -3 --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PY_CMD=py -3"
    goto :PYTHON_FOUND
)

py --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PY_CMD=py"
    goto :PYTHON_FOUND
)

for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*") do (
    if exist "%%D\python.exe" (
        set "PY_CMD=%%D\python.exe"
        goto :PYTHON_FOUND
    )
)

for /d %%D in ("C:\Program Files\Python3*") do (
    if exist "%%D\python.exe" (
        set "PY_CMD=%%D\python.exe"
        goto :PYTHON_FOUND
    )
)

for /d %%D in ("C:\Python3*") do (
    if exist "%%D\python.exe" (
        set "PY_CMD=%%D\python.exe"
        goto :PYTHON_FOUND
    )
)

echo [!] Python 3.10+ was not found on your Windows computer.
echo.
echo Please install Python using one of these quick options:
echo   1. Official Installer: https://www.python.org/downloads/
echo      * IMPORTANT: Check 'Add python.exe to PATH' during setup!
echo   2. Or install via Windows Terminal / PowerShell:
echo      winget install Python.Python.3.11
echo.
echo Opening Python download page in your browser...
start https://www.python.org/downloads/
echo.
pause
exit /b 1

:PYTHON_FOUND
echo [*] Detected Python engine: %PY_CMD%
%PY_CMD% --version

:: 2. Environment file check (.env)
if not exist .env (
    if exist .env.example (
        echo [*] Initializing .env configuration from .env.example...
        copy /y .env.example .env >nul
        echo [*] Created .env configuration file.
    )
)

:: 3. Virtual environment management
if not exist .venv\Scripts\activate.bat (
    echo [*] Creating virtual environment in .venv...
    %PY_CMD% -m venv .venv
    if errorlevel 1 (
        echo [!] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo [*] Virtual environment created successfully.
    
    echo [*] Installing dependencies from requirements.txt...
    call .venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo [!] Error installing dependencies.
        pause
        exit /b 1
    )
) else (
    call .venv\Scripts\activate.bat
)

:: 4. Verify benchmark sample images
if not exist aurora\samples\cotton_bacterial_blight.jpg (
    echo [*] Generating diagnostic specimen assets...
    python aurora\samples_generator.py
)

:: 5. Launch Application
echo.
echo [*] Launching Project Aurora Server and Dashboard...
python main.py %*

if errorlevel 1 (
    echo.
    echo [!] Server exited with an error code.
    pause
)
