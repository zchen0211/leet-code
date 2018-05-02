# STL Library

## Introduction
- Standard Template Library (stl). It provides four components called algorithms, containers, functions, and iterators.
- 13 headers
```cpp
<algorithm>
<functional>
<iterator>
<vector><list><map><deque><queue><set><stack>
<memory>
<numeric>
<utility>
```
- Good articls: http://www.cnblogs.com/CnZyy/p/3317999.html

## Algorithm and Functional
- Good summary: http://huqunxing.site/2016/09/29/C++STL%E8%AF%A6%E8%A7%A3%E4%B9%8B%E7%AE%97%E6%B3%95/
- Sorting
```cpp
std::sort(a.begin(), a.end());
std::sort(a.begin(), a.begin()+4);
```
- Stat
```cpp
std::min();
std::max();
```

## Algorithm