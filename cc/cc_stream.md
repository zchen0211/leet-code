# Streams
- A very good summary: http://www.cnblogs.com/renyuan/p/4132801.html

## iostream
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

## fstream
- ifstream derived from istream, ostream from ofstream, fstream from iostream;
```cpp
#include <fstream>
std::ofstream myfile;
```