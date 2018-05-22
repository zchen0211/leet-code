# Pybind

## Installation
- Make pybind11 folder in the same directory together with the codes:
```cmake
cmake_minimum_required(VERSION 2.8.12)
project(example)

add_subdirectory(pybind11)
pybind11_add_module(example example.cc)
```
- In *Linux*, if pybind is installed by apt-get, we can directly do
```cmake
find_package(pybind11)
```