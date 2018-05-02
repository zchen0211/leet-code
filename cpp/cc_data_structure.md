# Containers and Iterators

## General Iterators
- http://www.cnblogs.com/chio/archive/2007/10/31/944122.html
- General members
```cpp
#include <iterator>
std::begin();
std::end();
```

## General Containers
- Capacity
```cpp
bool empty() const noexcept;
size_type size() const noexcept;
```
- General modifiers:
```cpp
// both push_back and emplace_back available in vector, list, deque
// string only has push_back
void push_back(const value_type& val);
void push_back();
template<class... Args>
void emplace_back(Args&&... args);

// unordered_map, set, vector
clear();
```
- General iterators available in vector, array, unordered_map, set
```cpp
T* begin();
T* end();
T* cbegin(); // const iterator
T* cend();
```
- Other general functions:
```cpp
T* data();
```

## Arrays
- array: no size change
```cpp
std::array<T, kN> arr; // can't change size
```
- Vector
```cpp
#include <vector>
std::vector<T> arr;

void push_back(const value_type& val);
void push_back();
template<class... Args>
void emplace_back(Args&&... args);

insert(int index, T& );

resize(int );
```

## Hash Map Style
- General
```cpp
size_type max_size() const noexcept;

/* Element lookup */
iterator find ( const key_type& k );
const_iterator find ( const key_type& k ) const;
size_type count ( const key_type& k ) const;

/* Modifiers */
// generally, emplace(T1&&, T2&&)
template <class... Args>
pair<iterator, bool> emplace ( Args&&... args );
// insert(std::make_pair<T1, T2>(val1, val2));
pair<iterator,bool> insert ( const value_type& val );
erase(); // erase by key
clear();
swap();
```
- unordered_map
```cpp
#include <unordered_map>
unordered_map<int, char> map;

/* Element access */
mapped_type& operator[] ( const key_type& k );
mapped_type& operator[] ( key_type&& k );
mapped_type& at ( const key_type& k );
const mapped_type& at ( const key_type& k ) const;

/* Element lookup */
// auto item = map.find(key);
// item.first, item.second for key, value
iterator find ( const key_type& k );
const_iterator find ( const key_type& k ) const;
// 1 if existing, 0 otherwise
size_type count ( const key_type& k ) const;

/* Modifiers */
// generally, emplace(T1&&, T2&&)
template <class... Args>
pair<iterator, bool> emplace ( Args&&... args );
// insert(std::make_pair<T1, T2>(val1, val2));
pair<iterator,bool> insert ( const value_type& val );
// erase by key, iterator or range
erase();
```
- set
```cpp
#include <set>

set<int> a;
```

## List
- A queue
```cpp
#include <list>
list<T> a;
```
- Access
```
a.top(); a.top() -= 5;
a.back();
```
- Modifier
```cpp
a.insert(iterator pos, const T& value);
a.push_back(const T& value);
a.push_back(T&& value);
```

## stack and queue
- General
```cpp
/* Modifier */
// e.g. a.push(5);
void push (const value_type& val);
void push (value_type&& val);
template <class... Args> void emplace (Args&&... args);

void pop();
```
- Stack: LIFO
```cpp
#include <stack>
stack<int> a;

// Access
T& top(); // a.top() -= 5;
```
- Queue: FIFO
```cpp
#include <queue>
queue<T> my_q;

// Access
// e.g. myqueue.front() -= myqueue.back();
// first item
reference& front();
const_reference& front() const;
// last item
reference& back();
const_reference& back() const;
```
- Priority Queue
```cpp
#include <queue>
std::priority_queue<T> a;

// Access
T& top(); // a.top() -= 5;
```
