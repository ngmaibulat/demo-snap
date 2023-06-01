cmake_minimum_required(VERSION 3.0)  # Minimum required CMake version

set(CMAKE_CXX_STANDARD 20)  # Use C++20
set(CMAKE_CXX_STANDARD_REQUIRED ON)  # Require C++20

project(Salam)  # Project name

# Add the executable target
add_executable(salam-c main.cpp)
