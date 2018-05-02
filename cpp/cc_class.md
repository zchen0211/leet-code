# Classes

## Constructors
- A good article (http://www.cnblogs.com/chio/archive/2007/10/20/931043.html):
```cpp
Position(const Position&) = default;
Position& operator=(const Position&) = default;
Position(const Position&) = delete;
Position& operator=(const Position&) = delete;
```
- The **explicit** specifier specifies that a constructor or conversion function (since C++11) doesn't allow implicit conversions or copy-initialization. It may only appear within the decl-specifier-seq of the declaration of such a function within its class definition.
```cpp
struct A {
  A(int) { }
  explicit A(int, int) {}
};
A a1 = 1; // OK
A a2 = {1, 2}; // error
```

## Inheritance
- Multiple inheritance:
```cpp
class CRectangle: public CPolygon, public COutput;
```
- Virtual Inheritance:
```cpp
class A;
class B : public virtual A;
class C : public virtual A;
// members of A will only have 1 copy
class D : public B, public C;
```
- Override: signature must match! basic class member function must be virtual!
```cpp
struct A {
  virtual void foo(); // must be virtual to be overriden
  void bar();
}
struct B : A {
  void foo() const override; // Error: B::foo does not override A::foo
                               // (signature mismatch)
  // OK: B::foo overrides A::foo
  // could also be virtual void foo() override;
  void foo() override; 
  void bar() override; // Error: A::bar is not virtual
};
```

## Friend
```cpp
class B;
class A {
	friend rtype func(); // allow private members' access
	friend class B; // allow access to val
private:
	type val;
};
class B {
	void func(A a); // access to a.val allowed
};
```