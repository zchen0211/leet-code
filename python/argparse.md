# Parsing Arguments

## sys.argv
```python
import sys
sys.argv[0] # xxx.py
sys.argv[1] # ...
```

## argparse
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