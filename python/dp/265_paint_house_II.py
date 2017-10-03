"""
265. Paint House II (Hard)

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
"""

import heapq

class Solution(object):
  def minCostII(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    n = len(costs)
    if n == 0: return 0
    k = len(costs[0])
    if k == 0: return 0

    result = []
    for i in range(n): result.append([0] * k)
    print 'result', result
    # init
    heap1 = []
    for i in range(k):
      result[0][i] = costs[0][i]
      heapq.heappush(heap1, costs[0][i])
    heap2 = []
    print heap1, heap2, result

    for i in range(1, n):
      for j in range(k):
        if heap1[0] != result[i-1][j]:
          result[i][j] = heap1[0] + costs[i][j]
        else:
          min_ = heapq.heappop(heap1)
          result[i][j] = heap1[0] + costs[i][j]
          heapq.heappush(heap1, min_)
        heapq.heappush(heap2, result[i][j])
      print heap1, heap2, result
      heap1, heap2 = heap2, []
    return min(result[-1])


if __name__ == "__main__":
  a = Solution()
  costs = [[1,5, 3],[2,9,4]]
  print a.minCostII(costs)
