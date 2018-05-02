# Iterator and Generators

## Iterator
- Good articles: http://www.codeceo.com/article/python-iterable-and-iterator.html, https://blog.csdn.net/bitcarmanlee/article/details/51335055
* Iterables: list, tuple, str, dict, set; non-iterables: int;
* Iterators: actually called in looping python objects:
```python
a = [1, 2, 3]
it = a.__iter__()
it.next() # 1
it.next() # 2
it.next() # 3
it.next() # StopIteration

# example 2
def my_for_loop(some_iterable):
  my_iter = some_iterable.__iter__()
  while True:
    try:
      print my_iter.next()
    except StopIteration:
      break
my_for_loop([1,2,3])
```
  * Make a class iterable: define __iter__() or __getitem__():
```python
# example 1:
class StrIterable(object):
  def __init__(self, val):
    self.val = val

  # method 1: define __iter__
  def __iter__(self): # iter(xxx) will call this funciton
    return iter(self.val)

  # method 2: define __getitem__
  # if both __getitem__ and __iter__ exist, __iter__ will override
  def __getitem__(self, index):
    return self.val[index]
```
```python
# example 2: both iterable and the iterator
class FibIterable:
  def __init__(self,iLast=1,iSecondLast=0,iMax=50):
    self.iLast = iLast 
    self.iSecondLast = iSecondLast
    self.iMax = iMax  #cutoff

  def __iter__(self):
    # because the object is both the iterable and the iterator
    return self
 
  def next(self):
    iNext = self.iLast + self.iSecondLast
    if iNext > self.iMax:
      raise StopIteration()
    self.iSecondLast = self.iLast
    self.iLast = iNext
    return iNext

o = FibIterable()
for i in o:
    print(i)
```
 * Make a class iterator: __iter__() returns self, next or __next__() required to generate the next value, and raise StopIteration when done.
 - Iterator examples:
```python
# example 1
def my_for_loop(some_iterable):
  my_iter = some_iterable.__iter__()
  while True:
    try:
      print my_iter.next()
    except StopIteration:
      break
```
```python
# example 2
class yrange:
  def __init__(self, n):
    self.i = 0
    self.n = n

  def __iter__(self):
    # Notice that the __iter__ method returned self. It need not be the case always.
    return self

  def next(self):
    if self.i < self.n:
      i = self.i
      self.i += 1
      return i
    else:
      raise StopIteration()

y = yrange(3)
for i in range(3):
  print y.next()
print list(yrange(5))
print sum(yrange(5))

# example 3
class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
y = yrange(5)
print list(y)  # [0, 1, 2, 3, 4]
print list(y)  # []
z = zrange(5)
print list(z)  # [0, 1, 2, 3, 4]
print list(z)  # [0, 1, 2, 3, 4]

# example 4
class reverse_iter:
  def __init__(self, init_list):
    self.data_list = init_list
    self.i = len(self.data_list) - 1

  def __iter__(self):
    return self

  def next(self):
    if self.i >= 0:
      i = self.data_list[self.i]
      self.i -= 1
      return i
    else:
      raise StopIteration()

it = reverse_iter([1, 2, 3, 4])
```

## Generator
- type generator
```python
def yrange(n):
  i = 0
  while i < n:
    yield i
    i += 1
y = yrange(3) # type generator

# method 1:
y.next() # 0
y.next() # 1

# method 2:
list(y) # [0,1,2]
list(y) # []
```
- Generator Example 2:
```python
def foo():
  print "begin"
  for i in range(3):
    print "before yield", i
    yield i
    print "after yield", i
  print "end"

f = foo()
print f.next()
print f.next()
print f.next()
# print f.next() # will raise StopIteration() exception
```
- Generator Example 3:
```python
def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

print take(5, squares()) # prints [1, 4, 9, 16, 25]
```