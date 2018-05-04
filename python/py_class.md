# Class and Object-Oriented Design

## Class
```python
class Date(object):
  def __init__(self, ...):
```
- classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities: classmethod must have a reference to a class object as the first parameter, whereas staticmethod can have no parameters at all.
```python
@classmethod
def from_string(cls, date_as_string):

@staticmethod
def is_date_valid(date_as_string):
```
- Access a member:
```python
class test(object):
  def method(self, ...):
    ...

obj = test()
func = getattr(obj, "method")
result = func(args)

func = getattr(self, "method")
```

## Magic Methods
- Good summaries: https://rszalski.github.io/magicmethods/, 
- Constructors
```python
def __new__(cls, ...):
def __init__(self, ...):
# Be careful, however, as there is no guarantee that __del__ will be executed if the object is still alive when the interpreter exits
def __del__(self):
```
- Comparison
```python
def __cmp__(self, other): # behavior of < > = 
__eq__(self, other): # ==
__ne__(self, other): # !=
__lt__(self, other): # <
__gt__(self, other): # >
__le__(self, other): # <=
__ge__(self, other): # >=
```
- Numeric Magic:
    - Unary operators
```python
def __pos__(self): # +obj
def __neg__(self): # -obj
def __abs__(self): # abs(obj)
def __invert__(self): # ~obj
def __round__(self, n): # round(obj)
def __floor__(self): # math.floor(obj)
def __ceil__(self): # math.ceil(obj)
def __trunc__(self): # math.trunc(obj)
```
    - binary operators
```python
def __add__(self, other): # +
def __sub__(self, other): # -
def __mul__(self, other): # *
def __floordiv__(self, other): # //
def __div__(self, other): # /
def __truediv__(self, other): # from __future__ import division
def __mod__(self, other): # %
def __divmod__(self, other): # divmod()
def __pow__(self, other): # ** 
def __lshift__(self, other): # <<
def __rshift__(self, other): # >>
def __and__(self, other): # &
def __or__(self, other): # |
def __xor__(self, other): # ^
```
    - reflected operators:
```python
__radd__(self, other)
__rsub__(self, other)
__rmul__(self, other)
__rfloordiv__(self, other)
__rdiv__(self, other)
__rtruediv__(self, other)
__rmod__(self, other)
__rdivmod__(self, other)
__rpow__
__rlshift__(self, other)
__rrshift__(self, other)
__rand__(self, other)
__ror__(self, other)
__rxor__(self, other)
```
    - Augmented operatos:
```python
__iadd__(self, other) # +=
__isub__(self, other) # -=
__imul__(self, other) # *=
__ifloordiv__(self, other) # //=
__idiv__(self, other) # /=
__itruediv__(self, other)
__imod__(self, other) # 
__ipow__(self, other) # **=
__ilshift__(self, other) # <<= operator.
__irshift__(self, other) # >>= operator.
__iand__(self, other) # &= operator.
__ior__(self, other) # |= operator.
__ixor__(self, other) # ^=
```
    - Type conversion
```python
__int__(self)
__long__(self)
__float__(self)
__complex__(self)
__oct__(self)
__hex__(self)
__index__(self)
__trunc__(self)
__coerce__(self, other)
```
- Representing Class
```python
__str__(self): # str()
__repr__(self):
__format__(self, formatstr): # "Hello, {0:abc}!".format(a) will call a.__format__("abc")
__hash__(self): # hash(obj)
__nonzero__(self): # bool(obj)
__dir__(self): # dir(obj), usually unnecessary
__sizeof__(self): # sys.getsizeof(obj)
```
- Attribute
```python
__getattr__(self, name)
__setattr__(self, name, value)
__delattr__(self, name)
__getattribute__(self, name)
```
- Custom Sequences
```python
__len__(self)
__getitem__(self, key)
__setitem__(self, key, value)
__delitem__(self, key)
__iter__(self):
__next__(self): # x.next()
__reversed__(self): # reversed(obj)
__contains__(self, item): # item in obj
__missing__(self, key)
```
- Context
```python
__enter__(self): # with
__exit__(self, exception_type, exception_value, traceback)
```
- Abstract Base Classes
```python
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
```
- Copy
```python
__copy__(self): # copy.copy(obj)
__deepcopy__(self, memodict={}): # copy.deepcopy()
```
- Examples
```python
class Point3D(object):
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c
    def __repr__(self):
        return "Point3D(%d, %d, %d)" % (self.x, self.y, self.z)
    def __str__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print `my_point` # __repr__ gets called automatically
print my_point # __str__ gets called automatically
```
- Other operations
```python
x - y # x.__sub__()
x * y # x.__mul__()
x // y # x.__floordiv__()
x / y # x.__div__()

+= # object.__iadd__(self, other)
-= # object.__isub__(self, other)
*= # object.__imul__(self, other)
/= # object.__idiv__(self, other)

iter(x) # => x.__iter__()
len(x) # x.__len__()
item in x # => x.__contains__(item)
```


## Inheritance
- Base class:
```python
# base class as object to use super() in derived class
class Dog(object):
  kind = 'canine'

  def __init__(self, name='default'):
    print 'Call base class initializer!'
    self.name = name

  def greet(self):
    print 'hello world'

  # definition of various magical method
  def __str__(self):
    return self.name + ' fun'

  def __eq__(self, y):
    return len(self.name) == len(y.name)

dog = class_test.Dog('my dog')
dog.kind
type(class_test.Dog.greet) # instancemethod
type(dog.greet) # instancemethod
 
# reload str() function
print str(dog) # "my dog fun"

# reload == 
dog2 = class_test.Dog('dog ll')
dog == dog2 # True, b/c the reloaded __eq__
```
- Derived class:
```python
class Derived_Dog(Dog):
  nickname = 'Yang_Yi'

  def __init__(self, name=None, nickname=None):
  	# can be written as super().__init__()
    super(Derived_Dog, self).__init__(name=name)
    self.name = name
    self.nickname = nickname

# Will call base class __init__
dog3 = class_test.Derived_Dog(name='dog', nickname='Wang Jiang')
dog3.greet() # call the basic one
dog3.kind # Canine form base class
# call class shared attribute
class_test.Derived_Dog.nickname # "Yang_Yi"
# call instance specific
print dog3.nickname # will be "Wang Jiang", override original one
```