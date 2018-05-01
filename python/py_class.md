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