"""
454. 4Sum II (Medium)

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

"""
Solution:
brute-force: O(ABC), b/c check D can be reduced to constant by hash table

double hash-table:
O(AB) or O(CD)
"""

class Solution(object):
  def fourSumCount(self, A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    hash_AB = {}
    for i in A:
      for j in B:
        if i+j not in hash_AB:
          hash_AB[i+j] = 1
        else:
          hash_AB[i+j] += 1

    hash_CD = {}
    for i in C:
      for j in D:
        if i+j not in hash_CD:
          hash_CD[i+j] = 1
        else:
          hash_CD[i+j] += 1

    result = 0
    for k in hash_AB:
      if -k in hash_CD:
        result += hash_AB[k] * hash_CD[-k]
    return result


if __name__ == '__main__':
  a = Solution()
  print a.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])
