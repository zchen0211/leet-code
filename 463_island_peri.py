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
