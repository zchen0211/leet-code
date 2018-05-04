# Python Environment

## Variables
```python
a = None
del a
```
- Check all variables in the memory
```python
print(dir())
```
- Local and global variables in the current scope
```python
globals()
locals()
```

## Check Modules inside a Class
- dir() to check a class
```python
lis = [1, 2, 3]
dir(lis) # check all 
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# same as above
dir(list)
```

## Parse from os.envirson
- A bash run like:
```bash
root=xxx game=elfgames.go.game model_file=elfgames.go.df_model3 python3 -u df_selfplay.py
```
- library os will parse environment variables as strings, envs will be a dictrionary:
```python
import os
envs = os.environ

# we will have
envs["root"] = "xxx"
envs["game"] = "elfgames.go.game"
...
```

## Dispatch a module from command line
```python
import argh

# declaring:

def echo(text):
    "Returns given word as is."
    return text

def greet(name, greeting='Hello'):
    "Greets the user with given name. The greeting is customizable."
    return greeting + ', ' + name

# assembling:

parser = argh.ArghParser()
parser.add_commands([echo, greet])

# dispatching:

if __name__ == '__main__':
    parser.dispatch()
```

## Load Modules by Name
- python 3.6 importlib library
```python
import importlib
module = importlib.import_module("argparse")

# module is now numpy
module = importlib.import_module("numpy")
module.zeros([2, 4])
```

## import
- Good articles: https://www.cnblogs.com/kungfupanda/p/5257174.html
	* import a module (file), .py .pyo .pyc .pyd .so .dll
```python
# module: foo.py
# if all is defined, only modules with in can be imported
__all__ = [ 'bar', 'spam' ]
```
after first import, .py file will be written in a .pyc
	* import a package (a directory with __init__.py) all the __init__.py along the path will be run
- sys.path and sys.modules
```python
import sys

sys.path # a list of all pathes to find modules
sys.modules # all modules loaded including builtins
```