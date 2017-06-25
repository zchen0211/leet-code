'''
576. Out of Boundary Paths (Hard)

There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 10**9 + 7.

Example 1:
Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:
Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:
Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
'''

class Solution(object):
  def findPaths(self, m, n, N, i, j):
    """
    :type m: int
    :type n: int
    :type N: int
    :type i: int
    :type j: int
    :rtype: int
    """
    if N == 0: return 0
    # create an m x n matrix
    matrix = []
    for ii in range(m):
      matrix.append([0]*n)
    # initialize
    for ii in range(n): matrix[0][ii] += 1
    for ii in range(n): matrix[m-1][ii] += 1
    for ii in range(m): matrix[ii][0] += 1
    for ii in range(m): matrix[ii][n-1] += 1
    # new_matrix for update
    new_matrix = []
    for ii in range(m):
      new_matrix.append([0]*n)
    cnt = matrix[i][j]
    for step in range(N-1):
      new_matrix, matrix = self.update(matrix, new_matrix, m, n)
      cnt += matrix[i][j]
      cnt = cnt  % (10**9+7)
    return cnt


  def update(self, matrix, new_matrix, m, n):
    for i in range(m):
      for j in range(n):
        new_matrix[i][j] = 0
        if i>0: new_matrix[i][j] += matrix[i-1][j] % (10**9+7)
        if i<m-1: new_matrix[i][j] += matrix[i+1][j] % (10**9+7)
        if j>0: new_matrix[i][j] += matrix[i][j-1] % (10**9+7)
        if j<n-1: new_matrix[i][j] += matrix[i][j+1] % (10**9+7)
    return matrix, new_matrix


if __name__ == '__main__':
  a = Solution()
  print a.findPaths(1, 3, 3, 0, 1)
  print a.findPaths(2, 2, 2, 0, 0)
