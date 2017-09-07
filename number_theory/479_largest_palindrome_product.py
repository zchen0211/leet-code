"""
479. Largest Palindrome Product (Easy)

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
"""

class Solution(object):
  def largestPalindrome(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1: return 9

    upper = 10 ** n - 1
    lower = 10 ** (n-1)

    found = False
    large = upper ** 2
    first_half = large / (10**n)
    palin = 0
    # print upper, lower, first_half
    while not found:
      # create num
      palin = int(str(first_half) + str(first_half)[::-1])

      # print first_half, palin
      # obtainable?
      i = upper
      while i >= lower:
        if i * i < palin: break
        if palin % i == 0:
          found = True
          break
        i -= 1

      first_half -= 1

    palin = palin % 1337
    return palin

if __name__ == "__main__":
  a = Solution()
  for i in range(1, 9):
    print i, a.largestPalindrome(i)
