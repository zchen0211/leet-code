"""
407. Trapping Rain Water II (Hard)

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
"""

import Queue

class Solution(object):
  def trapRainWater(self, heightMap):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    m = len(heightMap)
    if m == 0: return 0
    n = len(heightMap[0])
    if n == 0: return 0
    q = Queue.PriorityQueue()
    visited = []
    for i in range(m):
      tmpv = [False] * n
      visited.append(tmpv)

    for i in range(n):
      q.put((heightMap[0][i], 0, i))
      q.put((heightMap[m-1][i], m-1, i))
      visited[0][i] = True
      visited[m-1][i] = True

    for i in range(m):
      q.put((heightMap[i][0], i, 0))
      q.put((heightMap[i][n-1], i, n-1))
      visited[i][0] = True
      visited[i][n-1] = True

    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    result = 0
    while not q.empty():
      h, i, j = q.get()
      print 'h', h, 'i', i, 'j', j,
      for ii, jj in dirs:
        tmpi = i + ii
        tmpj = j + jj
        if tmpi >= 0 and tmpi < m and tmpj >=0 and tmpj < n and not visited[tmpi][tmpj]:
          visited[tmpi][tmpj] = True
          result += max(0, h-heightMap[tmpi][tmpj])
          q.put((max(h, heightMap[tmpi][tmpj]), tmpi, tmpj))
      print 'result', result
    return result


if __name__ == "__main__":
  a = Solution()
  array = [[1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]]

  print a.trapRainWater(array)


