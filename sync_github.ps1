param (
    [string]$Message = "chore(sync): update repository and weekly milestones"
)

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host " Syncing CSEG3053 Cybersecurity Threat Engine to GitHub " -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

git add .
git commit -m $Message
git push origin main

Write-Host "[+] Synchronized successfully to GitHub!" -ForegroundColor Green
