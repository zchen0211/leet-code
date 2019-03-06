"""
464. Can I Win (Medium)

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""

"""
Memoization: 
time complexity: O(2^n)
no state kept: O(n!)
Solution 2: faster with bit operation
"""

import timeit

class Solution(object):
  def solution2(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        d = collections.defaultdict(bool)
        
        def helper(k, M, desiredTotal):
            if k in d:
                return d[k]
            if desiredTotal <= 0:
                return False
            for i in xrange(M, 0, -1):
                if k&(1<<i) == 0:  
                    if not helper(k+(1<<i), M, desiredTotal - i):
                        d[k] = True
                        return True
            d[k] = False
            return False
        return helper(0, maxChoosableInteger, desiredTotal)
 
  def canIWin(self, maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    n = maxChoosableInteger
    if n*(n+1) < desiredTotal: return False
    curr = [True] * n
    # key = self.bool_to_int(curr)
    table = {}
    result = self.helper(table, curr, desiredTotal, n)
    print table
    return result

  def helper(self, table, curr, total, n):
    # case 1: already checked
    key = tuple(curr)
    if tuple(curr) in table:
      return table[tuple(curr)]
    # base case 2: achievable by select the largest number
    # curr = self.int_to_bool(key, n)
    # print 'current', curr

    # memoized dp
    for i in range(n-1,-1,-1):
      if curr[i] == True:
        # print 'total', total, 'i+1', i+1, curr
        curr[i] = False
        if total-i-1>0:
          result = self.helper(table, curr, total-i-1, n)
          # print table
        else:
          result = False
        curr[i] = True
        if not result:
          table[key] = True
          return True
    table[key] = False
    # print table
    return False


if __name__ == '__main__':
  start = timeit.timeit()
  a = Solution()
  print a.canIWin(5,6) 
  end = timeit.timeit()
  print end-start
