@echo off

echo MGD Documentation Build (Windows)
echo Checking Python virtual environment...
echo.

set "VENV_DIR=mkenv"
set "PYTHON_EXE=%VENV_DIR%\Scripts\python.exe"
set "PIP_EXE=%VENV_DIR%\Scripts\pip.exe"

if exist "%PYTHON_EXE%" (
    echo Python venv found. Building documentation...
    "%PYTHON_EXE%" build.py
    set EXIT_CODE=%ERRORLEVEL%
) else (
    echo ⚠ ERROR: Python venv not found at %PYTHON_EXE%
    echo Copy/paste the following: python -m venv mkenv && call mkenv\Scripts\activate.bat
    pause
    exit /b 1
)

if not "%EXIT_CODE%"=="0" (
    echo.
    echo Build failed with exit code %EXIT_CODE%
    pause
    exit /b %EXIT_CODE%
)

echo.
echo Build completed successfully!
pause
