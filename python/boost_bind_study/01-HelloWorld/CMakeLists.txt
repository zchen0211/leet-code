cmake_minimum_required(VERSION 3.5)
PYTHON_ADD_MODULE(hello hello.cpp)
FILE(COPY hello.py DESTINATION .)
ADD_TEST(01-HelloWorld hello.py)
