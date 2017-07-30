cmake_minimum_required(VERSION 3.7)
project(hello_world)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp review1.h review1.cpp review2.h review2.cpp review3.h review3.cpp dma.h dma.cpp class_template.h friends.h friends.cpp nesting_template.h functor.h cast.h io_test.h os_test.h maco_test.h eigen_test.h)
add_executable(hello ${SOURCE_FILES})