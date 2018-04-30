# Basic Data-Structures Study

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

## List
```python
arr.sort(key= lambda x: x[0])
arr.sort(key= lambda x: (x[0],x[1]))
arr.sort(key= len)
reversed(arr)
```

## iterator

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
