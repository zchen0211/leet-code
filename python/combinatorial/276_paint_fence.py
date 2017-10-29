"""
276. Paint Fence (Easy)

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
"""

class Solution(object):
  def numWays(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if k == 0: return 0
    if n == 0: return 0

    A = [k]
    B = [0]

    for i in range(n-1):
      tmpA = A[-1] * (k-1) + B[-1] * (k-1)
      tmpB = A[-1]
      A.append(tmpA)
      B.append(tmpB)
    return A[-1] + B[-1]


if __name__ == "__main__":
  a = Solution()
  print a.numWays(5,4)
