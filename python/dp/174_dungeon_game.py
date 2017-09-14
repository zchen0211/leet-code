"""
174. Dungeon Game (Hard)

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""
class Solution(object):
  def calculateMinimumHP(self, dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    # most important: starting from right most
    # each point (i,j), required
    m = len(dungeon)
    if m == 0: return 0
    n = len(dungeon[0])
    if n == 0: return 0

    print m,n
    tmp = [abs(dungeon[i][j]) for i in range(m) for j in range(n)]
    print tmp
    tmp = sum(tmp) + 1
    matrix = []
    for i in range(m):
      matrix.append([tmp] * n)
    # for i in range(m+1):
    #   matrix[n][i] = 1
    # for i in range(n+1):
    #   matrix[i][m] = 1
    print 'init: ', matrix
    for i in range(m-1, -1, -1):
      for j in range(n-1, -1, -1):
        if i == m-1 and j == n-1:
          matrix[i][j] = 1 + max(-dungeon[m-1][n-1], 0)
        if i != m-1:
          matrix[i][j] = min(max(1,matrix[i+1][j]-dungeon[i][j]), matrix[i][j])
        if j != n-1:
          matrix[i][j] = min(max(1,matrix[i][j+1]-dungeon[i][j]), matrix[i][j])
    print matrix
    return matrix[0][0]


if __name__ == "__main__":
  a = Solution()
  # arr = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
  # arr = [[2],[1]]
  arr = [[0,-3]]
  print a.calculateMinimumHP(arr)
