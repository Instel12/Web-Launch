@echo off
python --version >nul 2>&1
if %errorlevel% == 0 (
    ipconfig
    start "" "main.py"
) else (
    echo Python is not installed. Please install it here: https://python.org/
    :loop
    goto loop
)
