"""
518. Coin Change 2 (Medium)

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
"""

class Solution(object):
  def change(self, amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    coins.sort()
    n_coins = len(coins)
    item = tuple([0]*n_coins)
    tmp_set = set()
    tmp_set.add(item)
    result = [tmp_set]
    print result[0]
    for i in range(1, amount+1):
      tmp_set = set()
      for j in range(n_coins):
        if i-coins[j]>=0 and len(result[i-coins[j]]) > 0:
          for item in result[i-coins[j]]:
            # get current solution, turn to list, +1, turn to tuple, add
            # print item
            tmp = list(item)
            tmp[j] += 1
            tmp_set.add(tuple(tmp))
      result.append(tmp_set)
      print i, result[i]
    return len(result[-1])

  def solution2(self, amount, coins):
    if amount == 0: return 1
    if len(coins) == 0: return 0
    coins.sort()
    result = [0]*(amount+1)
    i = 0
    while i <= amount:
      result[i] = 1
      i += coins[0]

    for item in coins[1:]:
      i = item
      while i<=amount:
        result[i] += result[i-item]
        i += 1
    return result[-1]

if __name__ == '__main__':
  a = Solution()
  print a.change(5, [1,2,5])
  print a.solution2(500, [1,2,5])
  # print a.change(3, [2])
  # print a.change(10, [10])
