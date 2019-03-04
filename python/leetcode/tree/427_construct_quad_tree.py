"""
427. Construct Quad Tree
Easy

We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:

It can be divided according to the definition above:


The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.


Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
"""

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        self.integral_histogram(grid)

    def helper(self, grid, x_min, x_max, y_min, y_max):
    	if x_min == x_max and y_min == y_max:
    		val = grid[x_min][x_max] == 1

    		n = Node(val, True, None, None, None, None)
    		return n
    	# check if all nodes are of the same value
    	if x_min == 0 and y_min == 0:
    		val_sum = self.sums[x_max][y_max]
    	elif x_min == 0:
    		val_sum = self.sums[x_max][y_max] - self.sums[x_max][y_min - 1]
    	elif y_min == 0:
    		val_sum = self.sums[x_max][y_max] - self.sums[x_min-1][y_max]
    	else:
    		val_sum = self.sums[x_max][y_max] - self.sums[x_min-1][y_max] - self.sums[x_max][y_min-1] + self.sums[x_min-1][y_min-1]
    	if val_sum == (x_max - x_min + 1) * (y_max - y_min + 1):
    		return Node(True, True, None, None, None, None)
    	elif val_sum == 0:
    		return Node(False, True, None, None, None, None)
    	else:
    		x_half = (x_min + x_max) // 2
    		y_half = (y_min + y_max) // 2
    		n1 = self.helper(grid, x_min, x_half, y_min, y_half)
    		n2 = self.helper(grid, x_half+1, x_max, y_min, y_half)
    		n3 = self.helper(grid, x_min, x_half, y_half+1, y_max)
    		n4 = self.helper(grid, x_half+1, x_max, y_half+1, y_max)
    		return Node(False, False, n1, n2, n3, n4)


    def integral_histogram(self, grid):
    	len_ = len(grid)
    	self.sums = []
    	for i in range(len_):
    		self.sums.append([0] * len_)

    	for i in range(len_):
    		for j in range(len_):
    			if i == 0 and j == 0:
    				self.sums[i][j] = grid[i][j]
    			elif i == 0:
    				self.sums[i][j] = sums[i][j-1] + grid[i][j]
    			elif j == 0:
    				self.sums[i][j] = sums[i-1][j] + grid[i][j]
    			else:
    				self.sums[i][j] = sums[i-1][j] + sims[i][j-1] - sums[i-1][j-1] + grid[i][j]
    	return

