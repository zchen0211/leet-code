import collections
import sys

# Array sorting
arr.sort(key= lambda x: x[0])
arr.sort(key= lambda x: (x[0],x[1]))

# stack
# implemented as a list
stack = [1]
stack.pop() # rightmost

# Queue
queue = collections.deque()
queue.append(1) # append rightmost
queue.appendleft(1) # append leftmost
queue.clear()
queue.count(1) # how many times 1 appears
queue.pop() # pop from rightmost
queue.popleft() # pop from left
# Priority Queue

# heap

# iterator

# string technqiues:
s_split = s.split(' ') # split into a list of substr
s_strip = s.strip() # strip multi-spaces into one
s_strip = s.replace(' ', '') # stripping all spaces

# maxint, minint
print sys.maxint
print -sys.maxint
