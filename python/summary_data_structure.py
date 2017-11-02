import collections
import sys

# Bit Manipulation
a = 0b110 # 0b prefix to use binary
b = 0x123 # 0x start to use 16-base
a ^ b # to compute add without carry
(a & b) << 1 # to compute carry

# String
s = 'abccccxxx'
s.find('x') # first occurence
s.lower()
s.upper()
s.count('aaa') # count non-overlapping
s.split()
s.replace()
' '.join(s_list) # will remove extra spaces!!! :)

# Array sorting
arr.sort(key= lambda x: x[0])
arr.sort(key= lambda x: (x[0],x[1]))
arr.sort(key= len)
reversed(arr)

# stack
# implemented as a list
stack = [1]
stack.pop() # rightmost
# stack with minimum/maximum/... query, keep a record

# Queue
queue = collections.deque()
queue.append(1) # append rightmost
queue.appendleft(1) # append leftmost
queue.clear()
queue.count(1) # how many times 1 appears
queue.pop() # pop from rightmost
queue.popleft() # pop from left

# Stack with Queues: O(n) time push to reverse the list as stack
q = collections.deque()
q.append(val) # append new
for i in range(cnt-1):
  v = q.popleft()
  q.append(v)
# then it is in good order now

# Queues with Stacks
in_stack = [] # always push
out_stack = [] # always pop
# move if required

# Priority Queue
# Implemented by Heap
import Queue
q = Queue.PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
print q.get() # will be 1 (smallest first)
q.qsize()
q.empty()

# Implemented in heapq
import heapq

q = []
q.heappush(q, (0, [1,2,3,...])
item = q.heappop(q)

# (Binary) Heap
# Binomial Heap (To make Union efficient)
# Recursive, B_k has 2**k nodes, height k
# C(k, i) nodes at depth i
# Root has degree k (larger than any other nodes)
# Members: parent, key, degree, child, sibling
# Fibonacci Heaps

# For binary, binomial, Fibonacci heaps
# Make-heap O(1) / O(1) / O(1)
# Insert, O(log n) / O(log n) / O(1)
# Minimum, O(1) / O(log n) / O(1)
# Extract-min, delete and return min O(log n) / O(log n) / O(log n)
# Union(H1, H2) O(n) / O(log n) / O(1)
# decrease key(H, x, k) O(log n) / O(log n) / O(1)
# delete O(log n) / O(log n) / O(log n)
# All Heaps are not designed for Search

# Data Structures for Disjoint sets 
# (S1, S2, ...), each one with a representative
# Make-set
# Union(x, y)
# Find-Set(x)
# Linked-list, representative: first node
# Weighted Union: Always append shor to longer lists when union
# Disjoint-set forest:
# Heuristic 1: Union by rank (root with smaller rank points to root with larger rank)
# Heuristic 2: path compression

# iterator

# string technqiues:
s_split = s.split(' ') # split into a list of substr
s_strip = s.strip() # strip multi-spaces into one
s_strip = s.replace(' ', '') # stripping all spaces

# maxint, minint
print sys.maxint
print -sys.maxint

# Tree related

# BST:
# search: O(log(N)) just go left/right if larger/smaller
# insert: always at leaf
# delete:

# Red-Black Tree
# Members: key(x), color(x), left(x), right(x), parent(x)
# 1. Every node is either red or black.
# 2. Every leaf (NIL) is black.
# 3. If a node is red, then both its children are black.
# 4. Every simple path from a node to a descendant leaf contains the same number of black nodes.
# Lemma 14.1 A red-black tree with n internal nodes has height at most 2*lg(n + 1).
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

# Trie
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

# Sement-Tree (store ops of an interval, really good problem 307, 308)
