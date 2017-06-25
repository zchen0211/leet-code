'''
371. Sum of Two Integers (Easy)

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''

# take-away:
# 1. a & b carry
# 2. a ^ b add
class Solution(object):
  def Helper(self, a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    Mask = 0xFFFFFFFF
    cnt = 0
    while(b!=0):
      a, b = (a^b)&Mask, ((a&b)<<1)&Mask
      print a,b
      cnt += 1

    if a<MAX:
      return a
    else:
      return ~(a^Mask)


  def getSum(self, a, b):
    return self.Helper(a,b)


if __name__ == '__main__':
  a = Solution()
  print 'result: ', a.getSum(-14,16)
