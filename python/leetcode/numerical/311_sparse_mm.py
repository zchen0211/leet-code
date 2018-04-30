"""
311. Sparse Matrix Multiplication (Medium)

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

class Solution(object):
  def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(A)
    if m == 0: return []
    k = len(A[0])
    if k == 0: return []
    n = len(B[0])

    result = [] # m * n
    for i in range(m):
      result.append([0] * n)

    # record non-zeros
    A_ = []
    for i in range(m):
      tmp = {}
      for j in range(k):
        if A[i][j] != 0:
          tmp[j] = A[i][j]
      A_.append(tmp)

    B_ = []
    for i in range(n):
      tmp = {}
      for j in range(k):
        if B[j][i] != 0:
          tmp[j] = B[j][i]
      B_.append(tmp)
    print A_
    print B_
    # multiplication
    for i in range(m):
      for j in range(n):
        # non-zeros
        for k in A_[i].keys():
          if k in B_[j].keys():
            result[i][j] += A_[i][k] * B_[j][k]
    return result


if __name__ == "__main__":
  a = Solution()
  A = [[ 1, 0, 0], [-1, 0, 3]]
  B = [[ 7, 0, 0 ], [ 0, 0, 0 ], [ 0, 0, 1 ]]
  print a.multiply(A, B)
