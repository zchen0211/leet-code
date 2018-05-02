# C++ Study

## All key words identifiers
```cpp
asm, auto, bool, break, case, catch, char, class, const, const_cast, continue, default, delete, do, double, dynamic_cast, else, enum, explicit, export, extern, false, float, for, friend, goto, if, inline, int, long, mutable, namespace, new, operator, private, protected, public, register, reinterpret_cast, return, short, signed, sizeof, static, static_cast, struct, switch, template, this, throw, true, try, typedef, typeid, typename, union, unsigned, using, virtual, void, volatile, wchar_t, while 
```

## Functions
- How a function is called?
```cpp
int __stdcall function(int a,int b);
int __cdecl function(int a,int b);
```
- Overloading:
```cpp
int operate(int a, int b);
float operate(float a, float b);
```
- inline: less overhead than regular call

## Random Number Generators
```cpp
#include <random>
// random seed by Mersenne Twister algorithm
std::mt19937 impl_;

float x = std::uniform_real_distribution<float>(0, 1)(impl_);

std::gamma_distribution<float> distribution(alpha);
sample = distribution(impl_);
```

## Classes
- Constructors, a good article (http://www.cnblogs.com/chio/archive/2007/10/20/931043.html):
```cpp
Position(const Position&) = default;
Position& operator=(const Position&) = default;
Position(const Position&) = delete;
Position& operator=(const Position&) = delete;
```
- Multiple inheritance:
```cpp
class CRectangle: public CPolygon, public COutput;
```
- Virtual Inheritance:
```cpp
class A;
class B : public virtual A;
class C : public virtual A;
// members of A will only have 1 copy
class D : public B, public C;
```
- Friend:
```cpp
class B;
class A {
	friend rtype func(); // allow private members' access
	friend class B; // allow access to val
private:
	type val;
};
class B {
	void func(A a); // access to a.val allowed
};
```

## Specializers
- Constant and Volatile:
```cpp
const
constexpr
volatile
```
- static: static objects will be on heap rather than stack;
```cpp
static
```
- explicit:
```cpp
class MyClass {
public:
  explicit MyClass( int num );
};
MyClass obj = 10; // error, b/c explit
// otherwise, will be MyClass tmp(10); obj = tmp;
```
- Class members:
```cpp
inline

private:
protected:
public:
```
- Extern (some good links: https://www.cnblogs.com/yc_sunniwell/archive/2010/07/14/1777431.html):
```cpp
// use C in C++ to avoid problems in compiling
extern "C" {}
```
- Others:
```cpp
noexcept
```

## Polymorphism
- Overriding operators:
```cpp
Group& operator[](int id) {return group_[id];}
std::vector::operator =(const vector& x);
```
- Abstract Class
```cpp
class xxx {
	virtual void area() = 0;
};
```

## Template
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

## Namespace
- Define:
```cpp
namespace minigo {}
```

## Macro
- Directly replace the codes when compiling, no ";" in definition
```cpp
#define square(x) x*x
float tmp = square(3+3); // will be 3+3*3+3

#define square(x) (x*x) // better
```
- Special Macros: ##, # and #@
```cpp
#define CONN(x, y) x##y
#define ToChar(x) #@x
#define ToStr(x) #x

Conn(c, out) << "test"; // cout << "test";
```
- if macro
```cpp
#ifdef
#ifndef
#else
#elif
#endif
```
- Other special macros
```cpp
__LINE__
__FILE__
__DATE__
__TIME__
```
- Varidic Special macros
```cpp
##__VA_ARGS__
#define debug(...) printf(##__VA_ARGS__)
```

## Streams
- A very good summary: http://www.cnblogs.com/renyuan/p/4132801.html
- C-style, can't print a class;
```cpp
printf("%dxxx", t);
scanf("%d", t);
```
- C++ Style, can overload operators for own class:
-- iostream derived from istream and ostream, the following three are all global instances of iostream class:
```cpp
cin >>
cout <<
cerr <<
```
-- Can overload to define output of a specific class;
```cpp
std::ostream& operator<<(std::ostream& os, Color color) {
	return os << "xxx";
}
```
- ifstream derived from istream, ostream from ofstream, fstream from iostream;
```cpp
#include <fstream>
std::ofstream myfile;
```

## Memory Management
- Stack and Heap: how to create objects only on class or heap? (http://www.cnblogs.com/chio/archive/2007/10/23/934335.html)