'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''

class Solution(object):
  def maximalSquare(self, matrix):
    '''
    :type matrix: List[List[str]]
    :rtype: int
    '''
    h = len(matrix)
    if h == 0:
      return 0
    w = len(matrix[0])
    if w == 0:
      return 0
    A = []
    for i in range(h):
      A.append([0]*w)

    for i in range(h):
      for j in range(w):
        if matrix[i][j] == '1':
          if i == 0 or j == 0:
            A[i][j] = 1
          else:
            A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
      #  print A[i][j],
      # print 'new_line'
    A = [max(item) for item in A]
    return max(A) ** 2


if __name__ == '__main__':
  a = Solution()
  print a.maximalSquare([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]])
  print a.maximalSquare(["0001","1101","1111","0111","0111"])
