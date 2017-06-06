'''
463. Island Perimeter (Easy)

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''


class Solution(object):
  def islandPeri(self, grid):
    if grid is None or grid[0] is None:
      return 0
    h = len(grid)
    w = len(grid[0])
    cnt = 0
    for hi in range(h):
      for wi in range(w):
        if grid[hi][wi] == 1:
          if hi == 0 or grid[hi-1][wi] == 0:
            cnt += 1
          if wi == 0 or grid[hi][wi-1] == 0:
            cnt += 1
          if hi == h-1 or grid[hi+1][wi] == 0:
            cnt += 1
          if wi == w-1 or grid[hi][wi+1] == 0:
            cnt += 1
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.islandPeri([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]])
