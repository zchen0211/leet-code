# C++ Study

## template
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
T add(T& a, T& b)
```
-- Compiler can infer type, so correct for add(2, 3) and add(2., 3.);
-- wrong for add(2, 3.5), should be add<float>(2, 3.5)
