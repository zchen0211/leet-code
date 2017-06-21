"""
498. Diagonal Traverse (Medium)

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:
Note:
The total number of elements of the given matrix will not exceed 10,000.
"""

class Solution(object):
  def findDiagonalOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    m = len(matrix)
    if m == 0: return []
    n = len(matrix[0])
    if n == 0: return []

    flag = True
    result = [matrix[0][0]]
    curr_sum = 1
    while curr_sum <= m+n-2:
      if flag:
        # if flag, [0][i] -> [i][0]
        i = max(0, curr_sum-n+1)
        while i<=min(curr_sum, m-1):
          j = curr_sum - i
          # if i>=0 and i<m and j>=0 and j<n:
          result.append(matrix[i][j])
          i += 1
      else:
        # else, [i][0] -> [0][i]
        i = min(curr_sum, m-1)
        while i>=max(0, curr_sum-n+1):
          j = curr_sum - i
          # if i>=0 and i<m and j>=0 and j<n:
          result.append(matrix[i][j])
          i -= 1

      flag = not flag
      curr_sum += 1
      # print result

    return result


if __name__ == '__main__':
  a = Solution()
  print a.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) 
  print a.findDiagonalOrder([[1],[2],[3]]) 
