"""
188. Best Time to Buy and Sell Stock IV (Hard)

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.
"""

class Solution(object):
  def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n <= 1 or k == 0: return 0

    # dp: 
    # base(i,j,1) = max(prices[i:j]) - min(prices[i:j])
    if k <= n/2:
      result = []
      for i in range(k+1):
        result.append([0]*n)

      for i in range(1, k+1):
        tmpmax = -prices[0]
        for j in range(1, n):
          result[i][j] = max(result[i][j-1], prices[j]+tmpmax)
          tmpmax = max(tmpmax, result[i-1][j-1] - prices[j])
        print i, result
      return result[k][n-1] 
    # base(i,j,n) = max_m(base(i,k,m) + base(k+1,j,n-m))
    else:
      result = 0
      for i in range(1,n):
        if prices[i] > prices[i-1]:
          result += prices[i] - prices[i-1]
      return result


if __name__ == "__main__":
  a = Solution()
  # print a.maxProfit(2, [0,3,0,4,7,8,2,5])
  print a.maxProfit(2, [3,2,6,5,0,3])
