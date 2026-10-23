@echo off
echo [*] Building CSEG3053 Cybersecurity Threat Engine (Pure C17)...
if not exist "bin" mkdir bin

gcc -std=c17 -Wall -Wextra -O2 -Iinclude src\core\metrics.c src\core\data_generator.c src\unit2_divide_conquer.c src\unit3_greedy.c src\unit4_dp.c src\unit5_backtracking_bb.c src\unit6_flow_string_crt.c src\main.c -o bin\soc_engine.exe
if %ERRORLEVEL% NEQ 0 (
    echo [!] Build failed for bin\soc_engine.exe
    exit /b %ERRORLEVEL%
)

gcc -std=c17 -Wall -Wextra -O2 -Iinclude src\core\metrics.c src\core\data_generator.c src\unit2_divide_conquer.c src\unit3_greedy.c src\unit4_dp.c src\unit5_backtracking_bb.c src\unit6_flow_string_crt.c tests\test_all.c -o bin\test_all.exe
if %ERRORLEVEL% NEQ 0 (
    echo [!] Build failed for bin\test_all.exe
    exit /b %ERRORLEVEL%
)

echo [+] Build completed successfully in bin\
