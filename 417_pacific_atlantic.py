"""
417. Pacific Atlantic Water Flow (Medium)

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

class Solution(object):
  def pacificAtlantic(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(matrix)
    if m == 0: return []
    n = len(matrix[0])
    if n == 0: return []

    pacific = set()
    stack = [(0,0)]
    for i in range(m):
      stack.append((i,0))
      pacific.add((i,0))
    for i in range(n):
      stack.append((0,i))
      pacific.add((0,i))

    while(stack):
      i, j = stack.pop()
      if (i,j) not in pacific:
        pacific.add((i,j))
      # top
      if i>0 and (i-1,j) not in pacific and matrix[i-1][j]>=matrix[i][j]:
        pacific.add((i-1,j))
        stack.append((i-1,j))
      # bottom
      if i<m-1 and (i+1,j) not in pacific and matrix[i+1][j]>=matrix[i][j]:
        pacific.add((i+1,j))
        stack.append((i+1,j))
      # left
      if j>0 and (i,j-1) not in pacific and matrix[i][j-1]>=matrix[i][j]:
        pacific.add((i,j-1))
        stack.append((i,j-1))
      # right
      if j<n-1 and (i,j+1) not in pacific and matrix[i][j+1]>=matrix[i][j]:
        pacific.add((i,j+1))
        stack.append((i,j+1))
    print pacific
    print (1,2) in pacific
    atlantic = set()
    stack = []
    for i in range(m):
      stack.append((i,n-1))
      atlantic.add((i,n-1))
    for i in range(n):
      stack.append((m-1,i))
      atlantic.add((m-1,i))

    while(stack):
      i, j = stack.pop()
      if (i,j) not in atlantic:
        atlantic.add((i,j))
      # top
      if i>0 and (i-1,j) not in atlantic and matrix[i-1][j]>=matrix[i][j]:
        atlantic.add((i-1,j))
        stack.append((i-1,j))
      # bottom
      if i<m-1 and (i+1,j) not in atlantic and matrix[i+1][j]>=matrix[i][j]:
        atlantic.add((i+1,j))
        stack.append((i+1,j))
      # left
      if j>0 and (i,j-1) not in atlantic and matrix[i][j-1]>=matrix[i][j]:
        atlantic.add((i,j-1))
        stack.append((i,j-1))
      # right
      if j<n-1 and (i,j+1) not in atlantic and matrix[i][j+1]>=matrix[i][j]:
        atlantic.add((i,j+1))
        stack.append((i,j+1))
    print atlantic
    print (1,2) in atlantic
    result = atlantic.intersection(pacific)
    result = list(result)
    result = [[item[0],item[1]] for item in result]
    return result

if __name__ == '__main__':
  a = Solution()
  # print a.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
  print a.pacificAtlantic([[1, 2, 3, 4, 5],
[16,17,18,19,6],
[15,24,25,20,7],
[14,23,22,21,8],
[13,12,11,10,9]])
