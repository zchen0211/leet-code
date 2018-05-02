# C++ Study

## All keywords identifiers
```cpp
asm, auto, bool, break, case, catch, char, class, const, const_cast, continue, default, delete, do, double, dynamic_cast, else, enum, explicit, export, extern, false, float, for, friend, goto, if, inline, int, long, mutable, namespace, new, operator, private, protected, public, register, reinterpret_cast, return, short, signed, sizeof, static, static_cast, struct, switch, template, this, throw, true, try, typedef, typeid, typename, union, unsigned, using, virtual, void, volatile, wchar_t, while 
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

## Namespace
- Define:
```cpp
namespace minigo {}
```

## Memory Management
- Stack and Heap: how to create objects only on class or heap? (http://www.cnblogs.com/chio/archive/2007/10/23/934335.html)