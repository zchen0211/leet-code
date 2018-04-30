"""
296. Best Meeting Point (Hard)

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.
"""

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0

        pts = []
        for i in range(m):
          for j in range(n):
            if grid[i][j] == 1: pts.append([i,j])
        
        if len(pts) == 0: return 0

        xs = [item[0] for item in pts]
        xs.sort()
        midx = xs[(len(pts)-1)/2]

        ys = [item[1] for item in pts]
        ys.sort()
        midy = ys[(len(pts)-1)/2]
        print midx, midy
        result = 0
        for item in pts:
          result += abs(item[0] - midx)
          result += abs(item[1] - midy)
        return result
