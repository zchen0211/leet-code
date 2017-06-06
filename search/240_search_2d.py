'''
240. Search a 2D Matrix II (Medium)

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

class Solution(object):
  def searchMatrix(self, matrix, target):
    m = len(matrix)
    if m == 0:
      return False
    n = len(matrix[0])
    if n == 0:
      return False
    i, j = 0, n-1
    while(j>=0 and i<=m-1):
      if matrix[i][j] == target:
        return True
      elif target < matrix[i][j]:
        j -= 1
      else:
        i += 1
    return False
    

if __name__ == '__main__':
  a = Solution()
  print a.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]], 20)

