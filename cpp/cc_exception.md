# Exceptions

# to quit a program
- abort
```cpp
#include <cstdlib>
// will output sth like
// [1]    47294 abort      ./program
std::abort();
```
- exit
```cpp
exit(1);
```

# catch exceptions
- try, catch pair
```cpp
try { // start of try block
    z = hmean(x, y);
} catch (const char * s) {
	// start of exception handler
    std::cout << s << std::endl;
    std::cout << "Enter a new pair of numbers: ";
    continue;
}
```
- raise an exception by throw
```cpp
double func(float a, float b) {
  if (a == -b)
    throw "bad hmean() arguments: a = -b not allowed";
  return 2.0 * a * b / (a + b);
}
```
