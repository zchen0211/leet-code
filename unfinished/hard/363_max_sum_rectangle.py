"""
363. Max Sum of Rectangle No Larger Than K (Hard)

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""

class Solution(object):
  def maxSumSubmatrix(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    # statistics of matrix
    m = len(matrix)
    if m == 0: return 0
    n = len(matrix[0])
    if n == 0: return 0
    
    stat = []
    for i in range(m):
      stat.append([0]*n)

    for i in range(n):
      if i== 0 and j==0: stat[i][j] == matrix[ 
