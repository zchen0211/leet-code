"""
361. Bomb Enemy (Medium)

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""

class Solution(object):
  def maxKilledEnemies(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    if m == 0: return 0
    n = len(grid[0])
    if n == 0: return 0

    hori = []
    for i in range(m):
      hori.append([0] * n)

    for i in range(m):
      # left to right
      for j in range(n):
        if grid[i][j] == "E":
          if j == 0: hori[i][j] = 1
          else: hori[i][j] = hori[i][j-1] + 1
        elif grid[i][j] == '0':
          if j > 0: hori[i][j] = hori[i][j-1]
      # right to left
      for j in range(n-2, -1, -1):
        if grid[i][j] != "W" and grid[i][j+1] != "W":
          hori[i][j] = hori[i][j+1]
    print hori
    
    vert = []
    for i in range(m):
      vert.append([0] * n)

    for i in range(n):
      # up to down
      for j in range(m):
        if grid[j][i] == "E":
          if j == 0: vert[j][i] = 1
          else: vert[j][i] = vert[j-1][i] + 1
        elif grid[j][i] == '0':
          if j > 0: vert[j][i] = vert[j-1][i]
      # right to left
      for j in range(m-2, -1, -1):
        if grid[j][i] != "W" and grid[j+1][i] != "W":
          vert[j][i] = vert[j+1][i]
    print vert

    ret = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == "0":
          ret = max(ret, hori[i][j] + vert[i][j])
    return ret

if __name__ == "__main__":
  a = Solution()
  # arr = [['0','E','0','0'],['E','0','W','E'],['0','E','0','0']]
  arr = [["E", '0', 'E', 'W', 'E']]
  print a.maxKilledEnemies(arr)
