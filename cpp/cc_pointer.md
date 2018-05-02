# Smart pointer

## unique pointer
```cpp
unique_ptr<T> abc;
abc.reset(new abc()); // has to be new, shouldn't be passed
abc.get();

auto instance = make_unique<T>(xxx);
auto instance = unique_ptr<T>(new T(xxx));
```

## rvalue reference
```cpp
// constructor
MyString(MyString&& str) {
 _len = str._len; _data = str._data;
}

std::move(T&& t)
```

## shared_ptr: can't use multiple shared_ptr pointing to a same raw pointer, otherwise problem when destruction.
```cpp
auto p = shared_ptr<T>(new T(xxx));
auto p = make_shared<T>(xxx);

p.reset(new T());
p.reset();
```