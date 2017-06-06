'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
import collections

class Solution(object):
  def numIslands(self, grid):
    tmp = 2
    h = len(grid)
    if h==0:
      return 0
    w = len(grid[0])
    if w==0:
      return 0
            
    grid = [list(item) for item in grid]
    print grid
    # bfs
    cnt = 0
    tmp_q = collections.deque()
    for i in range(h):
      for j in range(w):
        # mark all as str(tmp)
        if grid[i][j]=='1':
          grid[i][j] = str(tmp)
          tmp_q.append([i,j])
          while(len(tmp_q)>0):
            # leftpop, mark it, append
            ii, jj = tmp_q.popleft()
            cnt += 1
            print cnt, ii, jj
            grid[ii][jj] = str(tmp)
            # left
            if ii>0 and grid[ii-1][jj]=='1':
              grid[ii-1][jj] = str(tmp)
              tmp_q.append([ii-1, jj])
            if ii!=h-1 and grid[ii+1][jj]=='1':
              grid[ii+1][jj] = str(tmp)
              tmp_q.append([ii+1,jj])
            if jj>0 and grid[ii][jj-1]=='1':
              grid[ii][jj-1] = str(tmp)
              tmp_q.append([ii, jj-1])
            if jj!=w-1 and grid[ii][jj+1]=='1':
              grid[ii][jj+1] = str(tmp)
              tmp_q.append([ii, jj+1])
          tmp += 1
    
    print 'grid after'
    for item in grid:
      print item

    return tmp-2


if __name__ == '__main__':
  a = Solution()
  # print a.numIslands(["11110","11010","11000","00000"])
  # print a.numIslands(['11000', '11000','00100','00011'])
  print a.numIslands(["11111011111111101011","01111111111110111110","10111001101111111111","11110111111111111111","10011111111111111111","10111111011101110111","01111111111101101111","11111111111101111011","11111111110111111111","11111111111111111111","01111111011111111111","11111111111111111111","11111111111111111111","11111011111110111111","10111110111011110111","11111111111101111110","11111111111110111100","11111111111111111111","11111111111111111111","11111111111111111111"])
  
