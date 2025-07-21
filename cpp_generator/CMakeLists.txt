cmake_minimum_required(VERSION 3.10)
project(CC_Generator)

find_package(Curses REQUIRED)
include_directories(${CURSES_INCLUDE_DIR})

add_executable(cc_generator main.cpp)
target_link_libraries(cc_generator ${CURSES_LIBRARIES})
