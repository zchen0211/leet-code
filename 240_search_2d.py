'''
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
    i, j = 0, 0
    while(i<m and j<n):
      if matrix[i][j] > target:
        break
      if matrix[i][j] == target:
        return True
      else: # matrix too small
        if i==m-1 and j==n-1:
          return False
        elif i<m-1 and j<n-1:
          i, j = i+1, j+1
        elif i==m-1 and j<n-1:
          j += 1
        elif j==n-1 and i<m-1:
          i += 1
    # search in matrix[0..i][j]
    st = 0
    end = i
    while(st<end):
      mid = (st+end)/2
      if matrix[mid][j] == target:
        return True
      elif matrix[mid][j] < target:
        st = mid+1
      elif matrix[mid][j] > target:
        end = mid-1
    if st>0 and st<=i and matrix[st][j] == target:
      return True
    if end>0 and end<=i and matrix[end][j] == target:
      return True
    # search in matrix[i][0..j]
    st = 0
    end = j
    while(st<end):
      mid = (st+end)/2
      if matrix[i][mid] == target:
        return True
      elif matrix[i][mid] < target:
        st = mid+1
      elif matrix[i][mid] > target:
        end = mid-1
    if st>0 and st<=j and matrix[i][st] == target:
      return True
    if end>0 and end<=j and matrix[i][end] == target:
      return True
    return False


if __name__ == '__main__':
  a = Solution()
  print a.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]], 20)

