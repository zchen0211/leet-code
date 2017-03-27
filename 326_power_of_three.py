'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
'''

class Solution(object):
  def isPowerOfThree(self, n):
    #
    if n <= 0:
      return False
    while(n>1):
      if n % 3 == 0:
        n /= 3
      else:
        return False
    return True


if __name__ == '__main__':
  a = Solution()
  print a.isPowerOfThree(2)
