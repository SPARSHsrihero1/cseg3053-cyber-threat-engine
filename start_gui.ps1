Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Launching CSEG3053 Cybersecurity Threat Engine SOC GUI   " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "Starting local GUI web server on http://localhost:8080 ..." -ForegroundColor Green

python gui/server.py
