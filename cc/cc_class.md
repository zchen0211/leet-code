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

// example 2
class MyClass {
public:
  explicit MyClass( int num );
};
MyClass obj = 10; // error, b/c explit
// otherwise, will be MyClass tmp(10); obj = tmp;
```

## private, protected and public
- The difference between private and protected comes into play only within classes derived from the base class;
- Members of a derived class can access protected members of a base class directly, but they can't directly access private members of the base class.
```cpp
class Base {
 public:
  int publicMember; // Everything that is aware of Base is also aware that Base contains publicMember.
 protected:
  int protectedMember; // Only the children (and their children) are aware that Base contains protectedMember.
 private:
  int privateMember; // No one but Base is aware of privateMember.
};
```
- Inheritance: if not specified, regard as private inheritance
```cpp
public Base {
  public: int a;
  protected: int b;
  private: int c;
}

// a public, b protected, c invisible
class derived1 : public base {}

// a protected, b protected, c invisible
class derived2 : protected base {}

// a private, b private, c invisible
class derived3 : private base {}
```

## inline

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
- If a method in a base class will be redefined in a derived class, you should make it virtual.
- If the method should not be redefined, you should make it nonvirtual.


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