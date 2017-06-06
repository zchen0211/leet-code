'''
201. Bitwise AND of Numbers Range (Medium)

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''

class Solution(object):
  def rangeBitwiseAnd(self, m, n):
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
