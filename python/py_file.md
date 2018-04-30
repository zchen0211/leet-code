# Python File Operation

## Read and Write
- File writing:
```python
with open('abc.txt', 'w') as f:
  f.write('0123456789abcdef\n')
  data = 'xxxyyy\n'
  f.writelines(data)
  f.write('1357\n')
  f.write('w')
  f.seek(5)     # Go to the 6th byte in the file
  # change the 6th char ('5' in our example) to 'x'
  f.write('x')
  # f.seek(-3, 2) # Go to the 3rd byte before the end
  # f.write('y')
```
- File reading:
```python
with open('abc.txt') as f:
  size = 2
  print f.read(size) # '01'
  print f.readline() # '234...ef'
  print f.readlines() # return a list of strings, containing '\n' in each element
  print f.read(1) # Will print nothing, since readlines() reach ends
  f.close()

f = open('abc.txt', 'r+')
print 'print each line!'
for line in f:
  print line
```

## File operation
- To delete this file
```python
os.remove('abc.txt')
```
- with the shutil library:
```python
shutil.copyfile('basic_file.py', 'test.py')
shutil.move('test.py', 'test1.py')
shutil.copy('test1.py', 'test2.py')
if not os.path.exists('./test'):
  os.mkdir('./test')
# will raise error for moving, if test1.py already exists in the target folder
shutil.move('test1.py', './test/')
shutil.move('test2.py', './test/test2.py')

shutil.rmtree('./test')
```

## Pickle Library
- pickle write:
```python
import cPickle as pickle

data = {'1':1, '2':2}
with open('meta', 'wb') as fo:
  pickle.dump(data, fo, protocol=pickle.HIGHEST_PROTOCOL)
```
- pickle read:
```python
fo = open('meta', 'r')
data = pickle.load(fo)
print data
fo.close()
```

## Simple Numpy Op
```python
data = np.load('meta') # same as pickle load
```

## JSON File
- Read a JSON file:
```python
import json
fn = './results/test.json'
# data = json.load(open(fn, 'r'))
```
- Write a JSON file:
```python
import json
with open('data.json', 'w') as f:
  json.dump(tmp_data, f)
```