# Basic Data-Structures Study

## Bit Manipulation
```python
a = 0b110 # 0b prefix to use binary
b = 0x123 # 0x start to use 16-base
a ^ b # to compute add without carry
(a & b) << 1 # to compute carry
```

## integer
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

## Binary Heap, Fibonacci heaps
 1. Binomial Heap (To make Union efficient)
 2. Recursive, B_k has 2**k nodes, height k
 3. C(k, i) nodes at depth i
 4. Root has degree k (larger than any other nodes)
 5. Members: parent, key, degree, child, sibling
 6. Fibonacci Heaps
 7. Make-heap O(1) / O(1) / O(1)
 8. Insert, O(log n) / O(log n) / O(1)
 9. Minimum, O(1) / O(log n) / O(1)
 10. Extract-min, delete and return min O(log n) / O(log n) / O(log n)
 11. Union(H1, H2) O(n) / O(log n) / O(1)
 12. decrease key(H, x, k) O(log n) / O(log n) / O(1)
 13. delete O(log n) / O(log n) / O(log n)
 14. All Heaps are not designed for Search

## Data Structures for Disjoint sets
 1. (S1, S2, ...), each one with a representative
 2. Make-set
 3. Union(x, y)
 4. Find-Set(x)
 5. Linked-list, representative: first node
 6. Weighted Union: Always append shor to longer lists when union
 7. Disjoint-set forest:
 8. Heuristic 1: Union by rank (root with smaller rank points to root with larger rank)
 9. Heuristic 2: path compression

## Tree related
### BST:
  1. search: O(log(N)) just go left/right if larger/smaller
  2. insert: always at leaf
  3. delete:

### Red-Black Tree:
 1. Members: key(x), color(x), left(x), right(x), parent(x)
 2. Every node is either red or black.
 3. Every leaf (NIL) is black.
 4. If a node is red, then both its children are black.
 5. Every simple path from a node to a descendant leaf contains the same number of black nodes.
 6. Lemma 14.1 A red-black tree with n internal nodes has height at most 2*lg(n + 1).
```python
##  Left/right rotate
#    y         x
#  x   z <-> a   y
# a b           b z
##  Insert: insert a red node, then adjust until all properties are met
# case 1: property 3 violated (recolor)
# case 2: rotate left
# case 3: rotate right
# other structures: AVL tree, may require O(log n) rotations
# 2-3 Tree (Hopcroft)
# B-Tree
# i-th order statistics
# augment RB-tree with size(x)

# B-trees
# better at mimizing disk I/O operations
```
### Sement-Tree (store ops of an interval, really good problem 307, 308)