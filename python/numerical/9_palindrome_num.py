'''
9. Palindrome Number (Easy)

Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0: return False
        y = 0
        x_ = x
        while x > 0:
            tmp = x % 10
            y = y * 10 + tmp
            if y > 2 ** 31 - 1: return False
            x = x / 10
    return y == x_
