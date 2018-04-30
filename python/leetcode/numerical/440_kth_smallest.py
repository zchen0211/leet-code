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
    prefix = 0
    cnt = 0
    while True:
      if prefix == 0: start = 1
      else: start = 0
      for i in range(start, 10):
        tmp = self.cnt_start(n, prefix*10+i)
        if k > tmp: k -= tmp
        else: break
      prefix = prefix * 10 + i
      if k == 1: return prefix
      k -= 1 # if not prefix itself
      # print 'start with', i
      print 'prefix', prefix, 'k', k
      cnt += 1
      if cnt == 10: break

  # def helper(self, n, i, k):

  def cnt_start(self, n, prefix):
    # how many numbers <=n and starts with prefix
    if n < prefix: return 0
    tmp = n
    while tmp/10 >= prefix: tmp /= 10
    print tmp, prefix
    if tmp != prefix: # not starting with prefix
      # count
      base = 1
      cnt = 0
      while prefix*base < n:
        cnt += base
        base *= 10
      return cnt
    else: # starting with prefix
      base = 1
      cnt = 0
      while n/base != prefix:
        cnt += base
        base *= 10
      print cnt
      return cnt+ n%base+1


if __name__ == '__main__':
  a = Solution()
  print a.findKthNumber(1000,300)
  # print a.cnt_start(22,2)
