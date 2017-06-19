"""
625. Minimum Factorization (Medium)

Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
Input:

48 
Output:
68
Example 2
Input:

15
Output:
35
"""

class Solution(object):
  def smallestFactorization(self, a):
    """
    :type a: int
    :rtype: int
    """
    if a<10: return a
        
    stat, flag = self.factor(a)
    if not flag: return 0
    result = ''
    i = 9
    while i>1:
      if i in stat:
        result = str(i)*stat[i] + result
      i -= 1
    result = int(result)
    if result <= 2147483647: return result
    else: return 0

  def factor(self, a):
    stat = {}
    i = 9
    while i>1:
      if a % i == 0:
        stat[i] = 0
        while a % i == 0:
          a /= i
          stat[i] += 1
        i -= 1
    if a != 1: flag = False
    else: flag = True
    return stat, flag

