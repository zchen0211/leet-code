'''
343. Integer Break (Medium)
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
'''

class Solution(object):
  def integerBreak(self, n):
    result = [1, 1, 1, 2]
    if n <= 3:
      return result[n]
    for k in range(4, n+1):
      tmp1 = result[k-2] * 2
      tmp2 = result[k-3] * 3
      tmp3 = (k-2) * 2
      tmp4 = (k-3) * 3
      # print tmp1, tmp2, 
      result.append(max(tmp1, tmp2, tmp3, tmp4))
    print result
    return result[-1]


if __name__ == '__main__':
  a = Solution()
  print a.integerBreak(10)
