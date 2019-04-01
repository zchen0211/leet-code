'''
201. Bitwise AND of Numbers Range (Medium)

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''

"""
bit and, so if there is one '0', this digit will be '0'.
go through and find the digit with only 1.
"""

class Solution(object):
  def rangeBitwiseAnd(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    result = 0
    i = 0 # ith
    while(n>0):
      # ith-digit
      if m%2 == 1 and n%2==1 and m==n:
        result += 2**i
      m = m//2
      n = n//2
      i += 1
    return result


if __name__ == '__main__':
  a = Solution()
  print a.rangeBitwiseAnd(6,7)
