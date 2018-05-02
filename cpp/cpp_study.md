# C++ Study

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

