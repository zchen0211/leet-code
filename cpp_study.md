# C++ Study

## 1. Template
- Suggest not split declaration and implementation into .h and .cc;
- template class
```cpp
template<T>
class A {
};
```
- default template
```cpp
template <class T, class F=less<T>>
```
- function template:
```cpp
template<T>
T add(T& a, T& b);
// Compiler can infer type
int x = add(2, 3); // correct 
float y = add(2., 3.); //correct
add(2, 3.); // error, can't infer type
add<float>(2, 3.); // correct
```
- template function in a template class
```cpp
template <T>
class A {
  template<S>
  func(xxx) {}
};
A<T> a;
A<T> *b;
a.template func(xxx);
b->template func(xxx);
```
- template in template
```cpp
template<template<class> class T, class S>
void f(T<S> value); // template in template function

template<template<class> class T>
class ABC {
  template<S>
  ABC(T<S>);
};
```
- variadic template
```cpp
template <typename... Args>
option(Args&& args)
```

## Smart pointer
- unique pointer
```cpp
unique_ptr<T> abc;
abc.reset(new abc()); // has to be new, shouldn't be passed
abc.get();

auto instance = make_unique<T>(xxx);
auto instance = unique_ptr<T>(new T(xxx));
```
- rvalue reference
```cpp
// constructor
MyString(MyString&& str) {
 _len = str._len; _data = str._data;
}

std::move(T&& t)
```
- shared_ptr: can't use multiple shared_ptr pointing to a same raw pointer, otherwise problem when destruction.
```cpp
auto p = shared_ptr<T>(new T(xxx));
auto p = make_shared<T>(xxx);

p.reset(new T());
p.reset();
```

## lambda function
```cpp
[](int x, int y) {return x + y;}
[](int& x) {++x;}
[]() {global_x++;}
[]{global_x++;}

[&](){} // all by reference
[=] // all by value
[x, &y] // x by value, y by referenc
[&, x]
[=, &z]

[&, value, this] // make every member under this available
```
- Together with std::function:
```cpp
auto func = [&](int x) {...;}
void (*func_ptr)(int) = func;
func_ptr(4);

std::function<int()> func([](){xxxx; return 1;});

template<class R, class... Args>
class function<R(Args)>;
```