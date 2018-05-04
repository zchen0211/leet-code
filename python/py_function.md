# Python Function

## Arguments Parsing
- \*args and \*\*kwargs: both can parse indefinite number of arguments; the former parses a tuple and the latter parses a dictionary:
```python
def foo(*args, **kwargs):
    print 'args = ', args
    print 'kwargs = ', kwargs
    print '---------------------------------------'

if __name__ == '__main__':
  foo(1,2,3,4) # args = (1, 2, 3, 4), kwargs =  {} 

  foo(a=1,b=2,c=3) # args =  (), kwargs =  {'a': 1, 'c': 3, 'b': 2} 

  foo(1,2,3,4, a=1,b=2,c=3) # args =  (1, 2, 3, 4), kwargs =  {'a': 1, 'c': 3, 'b': 2} 
    
  foo('a', 1, None, a=1, b='2', c=3) # args =  ('a', 1, None), kwargs =  {'a': 1, 'c': 3, 'b': '2'} 
```

## functools
- Partially customize arguments
```
import functools

my_func = functools.partial(func, arg=...,)
my_func(input) # func(input, arg=...)
```

## Lambda Function
```python
g = lambda x: x ** 2
g(8)
```

## Map and Reduce
```python
# map to [1, 2, 3]
map(len, ['a', 'aa', 'aaa'])
```
