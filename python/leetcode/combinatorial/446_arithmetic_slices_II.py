'''
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 <= P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k >= 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 <= N <= 1000. The output is guaranteed to be less than 231-1.


Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
'''

from collections import defaultdict

class Solution(object):
  def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    # correct logic, but will TLE
    n = len(A)
    if n <= 2: return 0

    matrix2 = {} # (end, d) -> cnt (with only 2 numbers)
    matrix3 = {} # (end, d) -> at least 3 numbers
    matrix2[(A[1], A[1]-A[0])] = 1
    
    for i in range(2, n):
      # A[i] given
      # if matrix2 and matrix3 forms arithmetic slices
      new_matrix = {}
      for item in matrix2:
        end, d = item
        if end + d == A[i]:
          if (A[i],d) not in new_matrix:
            new_matrix[(A[i],d)] = matrix2[(end,d)]
          else:
            new_matrix[(A[i],d)] += matrix2[(end,d)]
      for item in matrix3:
        end, d = item
        if end + d == A[i]:
          if (A[i],d) not in new_matrix:
            new_matrix[(A[i],d)] = matrix3[(end,d)]
          else:
            new_matrix[(A[i],d)] += matrix3[(end,d)]
          # new_matrix[(A[i],d)] = new_matrix.get((A[i], d), 0) + 1
      for item in new_matrix:
        if item not in matrix3: matrix3[item] = new_matrix[item]
        else: matrix3[item] += new_matrix[item]  
      # add (A[j], A[i]) j<i in marix2
      for j in range(i):
        item = (A[i], A[i]-A[j])
        if item not in matrix2: matrix2[item] = 1
        else: matrix2[item] += 1
    return sum(matrix3.values())

  def solution2(self, A):
    total = 0
    n = len(A)
    dp = []
    for i in range(n):
      dp.append({})
    # dp[i]: a dictionary from int to int
    # dp[i][k]: 
    # until A[i], how many sequences ends with A[i], has Arith diff k
    # dp = [defaultdict(int) for item in A]
    print 'init', dp
    for i in xrange(len(A)):
        for j in xrange(i):
            dp[i][A[i] - A[j]] = dp[i].get(A[i]-A[j], 0) + 1
            if A[i]-A[j] in dp[j]:
                dp[i][A[i] - A[j]] += dp[j][A[i]-A[j]]
                total += dp[j][A[i]-A[j]]
        print dp, total
    return total

if __name__ == '__main__':
  a = Solution()
  """
  print a.numberOfArithmeticSlices([2,4,6])
  print a.solution2([2,4,6])
  print a.numberOfArithmeticSlices([2,4,6,8])
  print a.solution2([2,4,6,8])
  print a.numberOfArithmeticSlices([2,4,6,8,10])
  """
  # print a.solution2([2,4,6,8,10])
  # print a.solution2([2,3,4,5,6])
  arr = [1,2,3,1,2,3,4]
  print a.solution2(arr)
