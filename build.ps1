Write-Host "[*] Building CSEG3053 Cybersecurity Threat Engine (Pure C17)..." -ForegroundColor Cyan
if (-not (Test-Path "bin")) {
    New-Item -ItemType Directory -Path "bin" | Out-Null
}

$coreSrcs = @(
    "src/core/metrics.c",
    "src/core/data_generator.c",
    "src/unit2_divide_conquer.c",
    "src/unit3_greedy.c",
    "src/unit4_dp.c",
    "src/unit5_backtracking_bb.c",
    "src/unit6_flow_string_crt.c"
)

Write-Host "Compiling bin/soc_engine.exe..." -ForegroundColor Yellow
& gcc -std=c17 -Wall -Wextra -O2 -Iinclude $coreSrcs src/main.c -o bin/soc_engine.exe
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to build bin/soc_engine.exe"
    exit $LASTEXITCODE
}

Write-Host "Compiling bin/test_all.exe..." -ForegroundColor Yellow
& gcc -std=c17 -Wall -Wextra -O2 -Iinclude $coreSrcs tests/test_all.c -o bin/test_all.exe
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to build bin/test_all.exe"
    exit $LASTEXITCODE
}

Write-Host "[+] All targets built successfully in bin/" -ForegroundColor Green
