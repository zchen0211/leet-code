"""
427. Construct Quad Tree (Easy)

We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:

The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.

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


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        self.integral_histogram(grid)
        len_ = len(grid)
        n = self.helper(grid, 0, len_ - 1, 0, len_ - 1)
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
            val_sum = self.sums[x_max][y_max] - self.sums[x_min - 1][y_max]
        else:
            val_sum = (
                self.sums[x_max][y_max]
                - self.sums[x_min - 1][y_max]
                - self.sums[x_max][y_min - 1]
                + self.sums[x_min - 1][y_min - 1]
            )
        if val_sum == (x_max - x_min + 1) * (y_max - y_min + 1):
            return Node(True, True, None, None, None, None)
        elif val_sum == 0:
            return Node(False, True, None, None, None, None)
        else:
            x_half = (x_min + x_max) // 2
            y_half = (y_min + y_max) // 2
            n1 = self.helper(grid, x_min, x_half, y_min, y_half)
            n2 = self.helper(grid, x_min, x_half, y_half + 1, y_max)
            n3 = self.helper(grid, x_half + 1, x_max, y_min, y_half)
            n4 = self.helper(grid, x_half + 1, x_max, y_half + 1, y_max)
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
                    self.sums[i][j] = self.sums[i][j - 1] + grid[i][j]
                elif j == 0:
                    self.sums[i][j] = self.sums[i - 1][j] + grid[i][j]
                else:
                    self.sums[i][j] = (
                        self.sums[i - 1][j]
                        + self.sums[i][j - 1]
                        - self.sums[i - 1][j - 1]
                        + grid[i][j]
                    )
        return


if __name__ == "__main__":
    a = Solution()
    # array = [[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1]]
    array = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ]
    a.construct(array)
