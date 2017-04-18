'''
compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
'''

class Solution(object):
  def coinChange(self, coins, amount):
    result = [0]
    coins.sort()
    n = 1
    while(n<=amount):
      res = n+1
      for coin in coins:
        if n-coin>=0 and result[n-coin] != -1:
          res = min(res, result[n-coin]+1)
      if res == n+1:
        result.append(-1)
      else:
        result.append(res)
      n += 1
    return result[-1]


if __name__ == '__main__':
  a = Solution()
  print a.coinChange([1,2,5], 11)    
  print a.coinChange([2], 3)    
