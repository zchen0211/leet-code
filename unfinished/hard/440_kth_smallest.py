"""
440. K-th Smallest in Lexicographical Order (Hard)

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 <= k <= n <= 10**9.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""

class Solution(object):
  def findKthNumber(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    for i in range(1, 10):
      tmp = self.cnt_start(n, i)
      if k > tmp:
        k -= tmp
      else: break
    print 'start with', i

  def helper(self, n, i, k):

  def cnt_start(self, n, i):
    # first digit is not i
    tmp = n
    while tmp>=10: tmp /= 10
    if tmp != i:
      # count
      base = 1
      cnt = 0
      while i*base < n:
        cnt += base
        base *= 10
      return cnt
    else:
      base = 1
      cnt = 0
      while n/base != i:
        cnt += base
        base *= 10
      return cnt+ n%base+1


if __name__ == '__main__':
  a = Solution()
  print a.findKthNumber(13,6)
  # print a.cnt_start(103,2)
