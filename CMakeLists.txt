cmake_minimum_required(VERSION 3.16)
project(CyberThreatEngine C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

if(MSVC)
    add_compile_options(/W4 /O2)
else()
    add_compile_options(-Wall -Wextra -O2)
endif()

include_directories(include)

set(CORE_SOURCES
    src/core/metrics.c
    src/core/data_generator.c
    src/unit2_divide_conquer.c
    src/unit3_greedy.c
    src/unit4_dp.c
    src/unit5_backtracking_bb.c
    src/unit6_flow_string_crt.c
)

# Main Executable
add_executable(soc_engine
    ${CORE_SOURCES}
    src/main.c
)

# Test Executable
add_executable(test_all
    ${CORE_SOURCES}
    tests/test_all.c
)

set_target_properties(soc_engine PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin")
set_target_properties(test_all PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin")

enable_testing()
add_test(NAME AllUnitTests COMMAND test_all)
