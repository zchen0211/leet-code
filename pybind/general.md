# Pybind

## Installation
- Make pybind11 folder together with the codes;
- Add directory to enable find-package to work
```cmake
cmake_minimum_required(VERSION 2.8.12)
project(example)

add_subdirectory(pybind11)
find_package(pybind11)
pybind11_add_module(example example.cc)
```