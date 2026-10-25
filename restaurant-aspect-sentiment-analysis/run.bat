@echo off
echo ========================================
echo Aspect-Based Sentiment Analysis
echo Restaurant Reviews
echo ========================================
echo.

echo Step 1: Preprocessing data...
py src/data/preprocess.py
if %errorlevel% neq 0 (
    echo Error in preprocessing
    pause
    exit /b 1
)

echo.
echo Step 2: Training baseline model...
py src/baseline.py
if %errorlevel% neq 0 (
    echo Error in baseline training
    pause
    exit /b 1
)

echo.
echo Step 3: Training transformer model (optional - takes time)...
echo Note: This step can take 10-30 minutes on CPU
echo Press Ctrl+C to skip if needed
py src/transformer.py
if %errorlevel% neq 0 (
    echo Warning: Transformer training failed or was skipped
    echo The application will still work with the baseline model
)

echo.
echo Step 4: Starting Streamlit application...
echo.
py -m streamlit run app.py

pause
