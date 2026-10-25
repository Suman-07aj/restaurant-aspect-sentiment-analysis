# Aspect-Based Sentiment Analysis - Restaurant Reviews
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Aspect-Based Sentiment Analysis" -ForegroundColor Cyan
Write-Host "Restaurant Reviews" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Step 1: Preprocessing data..." -ForegroundColor Yellow
py src/data/preprocess.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error in preprocessing" -ForegroundColor Red
    pause
    exit 1
}

Write-Host ""
Write-Host "Step 2: Training baseline model..." -ForegroundColor Yellow
py src/baseline.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error in baseline training" -ForegroundColor Red
    pause
    exit 1
}

Write-Host ""
Write-Host "Step 3: Training transformer model (optional)..." -ForegroundColor Yellow
py src/transformer.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "Warning: Transformer training failed or was skipped" -ForegroundColor DarkYellow
    Write-Host "The application will still work with the baseline model" -ForegroundColor DarkYellow
}

Write-Host ""
Write-Host "Step 4: Starting Streamlit application..." -ForegroundColor Green
Write-Host ""
py -m streamlit run app.py
