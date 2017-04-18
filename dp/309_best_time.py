'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''

class Solution(object):
  def maxProfit(self, prices):
    n = len(prices)
    if n <= 1: return 0

    max_val = max(prices)

    b_buy = max(-prices[1], -prices[0])
    b_sell = max(0, prices[1]-prices[0])
    prev_buy = -prices[0]
    prev_sell = 0

    i = 2
    while(i<n):
      print b_buy, b_sell, prev_buy, prev_sell
      prev_buy, prev_sell, b_buy, b_sell = b_buy, b_sell, max(prev_sell-prices[i], b_buy), max(b_buy+prices[i], b_sell)
      i += 1
    return b_sell

if __name__ == '__main__':
  a = Solution()
  print a.maxProfit([1,2,3,0,2])
  # print a.maxProfit([2,1,4])
