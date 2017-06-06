'''
304. Range Sum Query 2D - Immutable (Medium)

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 <= row2 and col1 <= col2.
'''

class NumMatrix(object):
  def __init__(self, matrix):
    h = len(matrix)
    if h == 0: return
    w = len(matrix[0])
    if w == 0: return
    self.cumul = []
    for i in range(h):
      self.cumul.append([0]*w)

    for i in range(h):
      for j in range(w):
        if i==0 and j==0:
          self.cumul[i][j] = matrix[0][0]
        if i==0 and j>0: self.cumul[i][j] = self.cumul[i][j-1]+matrix[0][j]
        if j==0 and i>0: self.cumul[i][j] = self.cumul[i-1][j]+matrix[i][0]
        if i>0 and j>0:
          self.cumul[i][j] = self.cumul[i-1][j]+self.cumul[i][j-1]-self.cumul[i-1][j-1]+matrix[i][j]
        print i, j, self.cumul # self.cumul[i][j]
    print self.cumul


  def sumRegion(self, row1, col1, row2, col2):
    if row1 == 0 and col1==0: return self.cumul[row2][col2]
    elif row1 == 0: return self.cumul[row2][col2] - self.cumul[row2][col1-1]
    elif col1 == 0: return self.cumul[row2][col2] - self.cumul[row1-1][col2]
    else:
      return self.cumul[row2][col2] - self.cumul[row1-1][col2] - self.cumul[row2][col1-1] + self.cumul[row1-1][col1-1]


if __name__ == '__main__':
  a = NumMatrix([[1,2],[3,4]])
  '''a = NumMatrix([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])'''
  print a.cumul
