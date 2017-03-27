'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''

class Solution(object):
  def isUgly(self, num):
    while(num>1):
      prev_num = num
      if num % 2 == 0:
        num /= 2
      if num % 3 == 0:
        num /= 3
      if num % 5 == 0:
        num /= 5
      if num == prev_num: # can't be divided by any
        return False
    return True


if __name__ == '__main__':
  a = Solution()
  print a.isUgly(6)
  print a.isUgly(8)
  print a.isUgly(14)
