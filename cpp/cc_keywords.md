# All Keywords

- A good summary: https://blog.csdn.net/fyl_csdn/article/details/44905211, https://blog.csdn.net/scmuzi18/article/details/53696778
- 63 classic keywords in c++98/03.
```cpp
asm, auto, bool, break, case, catch, char, class, const, const_cast, continue, default, delete, do, double, dynamic_cast, else, enum, explicit, export, extern, false, float, for, friend, goto, if, inline, int, long, mutable, namespace, new, operator, private, protected, public, register, reinterpret_cast, return, short, signed, sizeof, static, static_cast, struct, switch, template, this, throw, true, try, typedef, typeid, typename, union, unsigned, using, virtual, void, volatile, wchar_t, while 
```
- New keywords in C++11
```cpp
alignas, alignof, char16_t, char32_t, constexpr, decltype, noexcept, nullptr, static_assert, thread_local, auto
```


## auto
To automatically infer variable type
```cpp
```

## boolean
```cpp
bool, true, false
```

## cast
```cpp
const_cast; dynamic_cast; reinterpret_cast; static_cast;
```

## char
```cpp
char; wchar_t
```

## class related
```cpp
explicit
friend
```
- override (since c++11)

## control flow
```cpp
break; cotinue; goto;
```
- switch
```cpp
switch; case; default;
```

## execution
```cpp
asm
```
- volatile: tell compiler not to optimize this part (https://www.cnblogs.com/yc_sunniwell/archive/2010/07/14/1777432.html)
```cpp
int i = 10;
int a = i;
// always 10
printf("i = %d", a);

// change i without telling compiler
__asm {
 mov dword ptr [ebp-4], 20h
}
int b = i;
// compiler optimize
// debug mode: 32, release mode: 10
printf("i = %d", b);
```
- const: https://www.cnblogs.com/wintergrass/archive/2011/04/15/2015020.html
```cpp
/* usage 1: const on var */
const int a = 10; // int const a=10;
const int arr[3] = {1,2,3}; // same asint const arr[3] = {1,2,3};

/* usage 2: const on pointer and ref */
// const left of *, const var
// const right of *, cont pointer
const int* a = &var; // pointer to constant var
int const *a = &var; // a is a pointer to the constant variable
int* const a = &var; // a is a constant pointer to the (non-constant) variable
const int* const a = &var; // a constant pointer to the constant variable

int const &a=x;
const int &a=x;
int &const a=x;

/* usage 3: const in function */
func(const T* a); func(const T& a);
const func(const T a);
const Rational operator*(const Rational& lhs, const Rational& rhs) {
return Rational(lhs.numerator() * rhs.numerator(),
lhs.denominator() * rhs.denominator());
}
// avoid the following case
Rational a,b;
Radional c;
(a*b) = c;

/* usage 4: const in class */
class test {
 public:
  // 
  static int const gVar;

  // correct
  test(int size) : SIZE(size) {}

  // A "const function", denoted with the keyword const after a function declaration, makes it a compiler error for this class function to change a member variable of the class. However, reading of a class variables is ok inside of the function, but writing inside of this function will generate a compiler error.
  int getx() const {
  	x++; // wrong
  	return x; // OK
  }

 private:
  // correct from c++11
  const int SIZE = 100;
  int x;
}
```
- mutable: always mutable, override const
```cpp
struct test {
  int a;
  mutable int b;
};
const test a;
a.a = 11; // error
a.b = 22; // OK
```

## exception
```cpp
catch; throw; try;
```

## operator
```cpp
new, delete
```

## type
```cpp
struct, class, union
typedef
```