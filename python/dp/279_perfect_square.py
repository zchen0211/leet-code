'''
279. Perfect Squares (Medium)

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''
import math

class Solution(object):
  def numSquares(self, n):
    cnt = [n] * (n+1)
    cnt[1] = 1

    i = 2
    while(i<=n):
      # check if perfect square
      k = int(math.sqrt(i))
      if k*k == i:
        cnt[i] = 1
      else:
        for j in range(1,k+1):
          cnt[i] = min(cnt[i], 1+cnt[i-j*j])
      # update with minimum
      i += 1
    print cnt
    return cnt[-1]


if __name__ == '__main__':
  a = Solution()
  print a.numSquares(12)
  print a.numSquares(13)
  
