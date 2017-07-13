"""
308. Range Sum Query 2D - Mutable (Hard)

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
 

Note:

The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 <= row2 and col1 <= col2.
"""
'''
class SegTreeNode(object):
  def __init__(self, left, right, up, down, val):
    self.left = left
    self.right = right
    self.up = up
    self.down = down
    self.val = val
    self.lu = None
    self.ld = None
    self.ru = None
    self.rd = None
'''

class NumMatrix(object):
  def __init__(self, matrix):
    m = len(matrix)
    n = len(matrix[0])
    self.matrix = matrix
    self.tree = []
    for i in range(m+1):
      self.tree.append([0]*(n+1))
    # update

  def update(self, row, col, val):
    m = len(matrix)
    n = len(matrix[0])
    delta = val - self.matrix[row][col]
    self.matrix[row][col] += delta
    i = row + 1
    while i <= m:
      j = col + 1
      while j <= n:
        self.tree[i][j] += delta
        j += j & (-j)
      i += i & (-i) 

  def sumRegion(self, row1, col1, row2, col2):
    r1 = self.helper_sum(row2, col2)
    r2 = self.helper_sum(row1-1, col2)
    r3 = self.helper_sum(row2, col1-1)
    r4 = self.helper_sum(row1-1, col1-1)
    return r1+r4-r2-r3

  def helper_sum(self, row, col):
    sum_ = 0
    i = row + 1
    while i >= 0:
      j = col + 1
      while j >= 0:
        sum_ += self.tree[i][j]
        j -= j & (-j)
      i -= i & (-i)
    return sum_
