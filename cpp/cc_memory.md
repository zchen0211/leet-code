# Memory Management

## Stack and Heap
- how to create objects only on class or heap? (http://www.cnblogs.com/chio/archive/2007/10/23/934335.html)

## memory library
```cpp
#include <memory>
void * memcpy ( void * destination, const void * source, size_t num );

// e.g., copy 4 items of type T
// b + 5 will be 5th element since T* b;
std::memcpy(a, b + 5, 4*sizeof(T));
```