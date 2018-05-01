# Some Basic Libraries in Python

## math library
- math functions
```python
import math

print math.sin(1.)
print math.asin(1.)
```
- others including tan, tanh, pi, nan, cos, acos, ...

## os library
- Run a system call command
```python
os.system('ls')
os.system('mkdir today')
os.system('rm -r today')
```
- Some supports to file systems
```python
print os.listdir('.')
print os.getcwd()
```
- os.path to handle files
```python
print os.path.isfile('os_test.py')
print os.path.isdir('basic.py')

fname = os.path.join(os.getcwd(), 'os_test.py')
print '%s is a file: %r' % (fname, os.path.isfile(fname))

if not os.path.exists('today'):
  os.makedirs('today')
os.rmdir('today')
os.remove() # to remove a file
shutil.rmtree() # to rm recursively
```

## system library
```python
import sys
import time

for i in range(5):
  print i,
  # comment the next line will buffer the output
  # wait 5 sec and print 0...4 simulteneously
  sys.stdout.flush()
  time.sleep(1)
```