# Class and Object-Oriented Design

## Some good articles
- https://blog.csdn.net/brucewong0516/article/details/79154837

## Try to run something, except to catch an exception, break to quit, finally will always be executed
```python
try:
  x = int(raw_input("please input a number: "))
except ValueError:
  print 'Oops! Not a valid number. Try again...'
  break
# to catch multiple exceptions
except (EOFError,ZeroDivisionError,NameError,TypeError):
  pass
finally:
  print("something")
```
- Raise to invoke an exception:
```python
raise ArithmeticError
```
- Base classes of all exceptions:
```python
Exception # all exceptions
AttributeError # error when getting an attribute
IOError # e.g., can't open a file
IndexError # index not existing
KeyError # key not existing
NameError # variable not found
SyntaxError # code in wrong format
TypeError
ValueError
ZeroDivisionError
```
- Customize an exception
```python
class SomeCustomException(Exception):
    pass
```
