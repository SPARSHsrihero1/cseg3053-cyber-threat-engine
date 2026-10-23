@echo off
setlocal
echo ========================================================
echo  Syncing CSEG3053 Cybersecurity Threat Engine to GitHub
echo ========================================================

set MSG=%~1
if "%MSG%"=="" set MSG=chore(sync): update repository and weekly milestones

git add .
git commit -m "%MSG%"
git push origin main

echo [+] Synchronized to https://github.com/SPARSHsrihero1/cseg3053-cyber-threat-engine
