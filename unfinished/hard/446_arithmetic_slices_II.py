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

class Solution(object):
  def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    n = len(A)
    if n <= 2: return 0
    stat = {2*A[1]-A[0]: 1}
    cnt = 0
    for i in range(2, n):
      item = A[i]
      print item, 'before', stat
      if item in stat: cnt+= stat[item]
      for j in range(i-1,-1,-1):
        new_item = item*2 - A[j]
        if new_item not in stat: stat[new_item] = 1+stat[item]
        else: stat[new_item] += 1+stat[item]
      print item, 'after', stat
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.numberOfArithmeticSlices([2,4,6,8])
