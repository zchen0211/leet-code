
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        self.integral_histogram(grid)
        len_ = len(grid)
        n = self.helper(grid, 0, len_-1, 0, len_-1)
        return n

    def helper(self, grid, x_min, x_max, y_min, y_max_):
    	if len_ == 1:
    		val = grid[x_min][y_min] == 1

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
    		n2 = self.helper(grid, x_min, x_half, y_half+1, y_max)
    		n3 = self.helper(grid, x_half+1, x_max, y_min, y_half)
    		n4 = self.helper(grid, x_half+1, x_max, y_half+1, y_max)
    		n = Node(False, False, n1, n2, n3, n4)
    		return n


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
    				self.sums[i][j] = self.sums[i][j-1] + grid[i][j]
    			elif j == 0:
    				self.sums[i][j] = self.sums[i-1][j] + grid[i][j]
    			else:
    				self.sums[i][j] = self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1] + grid[i][j]
    	return
        

if __name__ == "__main__":
	a = Solution()
	# array = [[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1]]
	array = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
	a.construct(array)