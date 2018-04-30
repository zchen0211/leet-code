# Python Study

## Class and OO Design
- Class
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

## Decorator
- Some good materials: http://www.cnblogs.com/SeasonLee/articles/1719444.html, https://www.cnblogs.com/cicaday/p/python-decorator.html
- A wrapper on a function:
```python
def debug(func):
    def wrapper(*args, **kwargs):  # fit any arguments passing
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(*args, **kwargs)
    return wrapper  # return

@debug
def say(something):
    print "hello {}!".format(something)
```
- Decorator with arguments:
```python
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print "say {}!".format(something)

# equal to
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)

if __name__ == '__main__':
    say('hello')
    do("my work")
```

## Parsing Arguments
- Some good materials https://blog.csdn.net/lis_12/article/details/54618868
- argparse package
```python
import argparse

parser = argparse.ArgumentParser()
```
-- Positional arguments (will throw error if missing)
```python
# positional parameters
parser.add_argument("echo")
```
-- Optional arguments (will throw error if missing)
```python
# 
parser.add_argument('-a', '--age')
```
-- Parsing
```python
# Parse the command line as default
args = parser.parse_args()
# Parse a list of string
args = parser.parse_args("--l 1 xxx".split())
```
-- Return a namespace class
```python
>>> args
Namespace(x='1', y='2')
```