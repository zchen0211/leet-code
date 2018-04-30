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
