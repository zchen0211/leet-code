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

## Operators
- Override class operators
```python
class x(object):
  def __init__(self):

  def __add__(self, other):

x + y # x.__add__() willl be called
```
- Other operations
```python
x - y # => x.__sub__()
x * y # => x.__mul__()
x // y # => x.__floordiv__()
x / y # => x.__div__()

x < y # => x.__lt__(y)
x < y # => x.__le__(y)
x == y # => x.__eq__(y)

+= # object.__iadd__(self, other)
-= # object.__isub__(self, other)
*= # object.__imul__(self, other)
/= # object.__idiv__(self, other)

iter(x) # => x.__iter__()
next(x) # => x.__next__()
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