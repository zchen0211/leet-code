"""
693. Binary Number with Alternating Bits (Easy)

Given a positive integer, check whether it has alternating bits or not.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111
"""

class Solution(object):
  def hasAlternatingBits(self, n):
    """
    :type n: int
    :rtype: bool
    """
    x = []
    while n > 0:
      x.append(n%2)
      n /= 2
    print x

    for i in range(len(x)-1):
      if x[i] == x[i+1]:
        return False
    return True


if __name__ == "__main__":
  a = Solution()
  print a.hasAlternatingBits(5)
  print a.hasAlternatingBits(7)
  print a.hasAlternatingBits(10)
  print a.hasAlternatingBits(4)
