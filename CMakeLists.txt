cmake_minimum_required(VERSION 3.5)

#
# PROPERTIES
#
project(bjournal VERSION 1.0)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED True)
configure_file(include/config.h.in 
    "${CMAKE_CURRENT_SOURCE_DIR}/include/config.h")

#
# EXECUTABLE
#
add_executable(bjournal
    "${CMAKE_CURRENT_SOURCE_DIR}/src/main.c"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/atom.c")
target_include_directories(bjournal PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}/include")
set_target_properties(bjournal
    PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/bin")

# 
# TESTING
#
add_executable(bjournal_test
    "${CMAKE_CURRENT_SOURCE_DIR}/test/main.c")
target_include_directories(bjournal_test PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}/include")
set_target_properties(bjournal_test
    PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/bin")
enable_testing()
add_test(
    NAME bjournal_tests
    COMMAND $<TARGET_FILE:bjournal_test>
    )
