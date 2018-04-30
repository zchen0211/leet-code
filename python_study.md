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