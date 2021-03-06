# Basic Data-Structures Study

## Basics
- Everything is an object
```python
isinstance(3, object)  # True, everything in python is an object
isinstance(None, object)  # True
id(b)  # id of an object
b.__sizeof__()
```
- Boolean Operation:
```python
any([True, True, False])  # True
all([True, True, False])  # False
```

## Bit Manipulation
```python
a = 0b110 # 0b prefix to use binary
b = 0x123 # 0x start to use 16-base
a ^ b # to compute add without carry
(a & b) << 1 # to compute carry
```

## Integer
```python
import sys
print(sys.maxint)
print(-sys.maxint)
```

## String
- Basic string op:
```python
s = 'abccccxxx'
s.find('x') # first occurence
s.lower()
s.upper()
s.count('aaa') # count non-overlapping
s.replace()
' '.join(s_list) # will remove extra spaces!!!
```
- Split and handle spaces:
```python
s.split()
s_split = s.split(' ') # split into a list of substr
s_strip = s.strip() # strip multi-spaces into one
s_strip = s.replace(' ', '') # stripping all spaces
```
- ASCII number and ch
```python
ord('a')  # 97
chr(97)  # 'a'
```
- Decode Chinese characters
```python
# decode Chinese
print(r'\xd5'.decode('gbk'))
```

## List
- Basic Ops
```python
a = [1,2,3,4,5]
del a[0:3]  # a=[4,5] now
a.pop()  # return the last element, remove it from the list
a = range(0, 5)
a.pop(3)  # return the 4th, remove it, default last
a.reverse()
# remove the first 4, if no 4 in the array will raise error
a.remove(4) 
a.count(5)  # how many 5 are there in the list
a = range(0,5)
b = range(5,10)
# zip return a list of tuple pairs [(0,5), (1,6), ...]
for x, y in zip(a,b):
  print x,y
```
- To generate a List:
```python
[x for x in a if x>3]
[(x,y) for x in (1,2,3) for y in [3,1,4] if x!=y]
```
- Sorting
```python
a.sort(cmp=None, key=None, reverse=False)
arr.sort(key= lambda x: x[0])
arr.sort(key= lambda x: (x[0],x[1]))
arr.sort(key= len)
reversed(arr)
```

## Tuple
- Generally unmodifiable:
```python
a = (1,2,3)
a = (a, 'abc')
a = 1,2 # packing
x, y = a # unpacking
```
- named tuple in collections
```python
import collections

ColTest = collections.namedtuple('ColTest', 'a, b, c')
result = ColTest(1, 2, 3)
# a, b, c are 1, 2, 3 respectively
a, b, c = result

Color = collections.namedtuple("Color", ["hue", "saturation", "luminosity"])
pixel = Color(170, 0.1, 0.6)
if pixel.saturation >= 0.5:
  print("Whew, that is bright!")
if pixel.luminosity >= 0.5:
  print("Wow, that is light!")
```

## Set
- Basic Ops:
```python
print type({1,2,3}) # will be set
a = set()
a = set({'a', 'b', 'c'})
a = set(['a', 'b', 'c'])
print 'a' in a
```
- Modifiers
```python
a.add('r')
a.remove('a')
a.discard('b')
a.pop() # randomly pop out an element
```

## Dictionary
- Basics:
```python
a = {'1':'a', '2':'b', '3':'c'}
a.get('1') # save as a[1]
del a['1']
a.popitem() # randomly remove one and return it
b = a.copy() # otherwise, b=a will be the same dict
```
- Keys, Values, and K-V pairs:
```python
a.keys()
a.values()
a.items()  # a list of tuple pairs of k,v
for k,v in a.items():
  print k,v
```
- defaultdict
```python
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
  d[k].append(v)

print d.items()
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

s = 'mississippi'
d = defaultdict(int)
for k in s:
  d[k] += 1

print d.items()
# [('i', 4), ('p', 2), ('s', 4), ('m', 1)]
```

## Counter
```python
from collections import Counter
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
  cnt[word] += 1
# counter type containing a dictionary
print cnt
print cnt['red']
print cnt['purple'] # 0
cnt['red'] = 0 # does not remove it
del cnt['blue'] # remove

c = collections.Counter(a=4, b=2, c=0, d=-2)
print list(c.elements())
# ['a', 'a', 'a', 'a', 'b', 'b']
print c.keys()
print c.values()

print collections.Counter('abracadabra').most_common(3)
# [('a', 5), ('r', 2), ('b', 2)]

# Counter minus
a = collections.Counter('abc')
b = collections.Counter('bcd')
print 'diff:', a-b
```

## Stack
- Stack is implemented by list in Python:
```python
stack = [1]
stack.pop() # rightmost
# stack with minimum/maximum/... query, keep a record
```
- Implement a Queue with stacks
```python
in_stack = [] # always push
out_stack = [] # always pop
# move if required
```

## Queue
- Collections library
```python
import collections

queue = collections.deque()
item = queue.append(1) # append rightmost
item = queue.appendleft(1) # append leftmost
queue.clear()
queue.count(1) # how many times 1 appears
queue.pop() # pop from rightmost
```
- Implement a Stack with Queues: O(n) time push to reverse the list as stack
```python
q = collections.deque()
q.append(val) # append new
for i in range(cnt-1):
  v = q.popleft()
  q.append(v)
# then it is in good order now
```

## Priority Queue: heap inside
- Implemented in Queue
```python
import Queue
q = Queue.PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
print q.get() # will be 1 (smallest first)
q.qsize()
q.empty()
```
- Implemented in heapq
```python
import heapq

q = []
q.heappush(q, (0, [1,2,3,...])
item = q.heappop(q)
```

## Trie
```python
class TrieNode():
  def __init__(self):
    self.child = {} # char to other TrieNode
    self.is_end = False

class Trie(object):
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for c in word:
      if c not in node.child:
        node.child[c] = TrieNode()
      node = node.child[c]
    node.is_end = True
```
