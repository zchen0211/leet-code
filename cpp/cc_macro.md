# Macro

## Directly replace the codes when compiling, no ";" in definition
```cpp
#define square(x) x*x
float tmp = square(3+3); // will be 3+3*3+3

#define square(x) (x*x) // better
```

## Special Macros: ##, # and #@
```cpp
#define CONN(x, y) x##y
#define ToChar(x) #@x
#define ToStr(x) #x

Conn(c, out) << "test"; // cout << "test";
```

## if macro
```cpp
#ifdef
#ifndef
#else
#elif
#endif
```
- Avoid multiple definitions:
```cpp
#ifndef FILE_H
#define FILE_H

// similar effect
pragma once
```

## Other special macros
```cpp
__LINE__
__FILE__
__DATE__
__TIME__
```

## Varidic Special macros
```cpp
##__VA_ARGS__
#define debug(...) printf(##__VA_ARGS__)
```