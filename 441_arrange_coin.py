import math


class Solution(object):
  def arrangeCoins(self, n):
    i = int(math.floor(math.sqrt(n*2) - 1))
    while( i*(i+1)/2 <=n):
      i += 1
    if i*(i+1) <= n:
      return i
    else:
      return i-1


if __name__ == '__main__':
  a = Solution()
  print a.arrangeCoins(5)
  print a.arrangeCoins(8)

