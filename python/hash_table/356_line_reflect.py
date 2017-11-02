"""
356. Line Reflection (Medium)

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?
"""

class Solution(object):
  def isReflected(self, points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    n = len(points)
    if n == 0: return True
    # sum_ = sum([item[0] for item in points])
    sum_ = min([item[0] for item in points]) + max([item[0] for item in points])

    # get statistics
    stat = set() # {}
    for point in points:
      x, y = point
      stat.add((x,y)) # = stat.get((x,y), 0) + 1
    for k in stat: #.keys():
      x1, y = k
      x2 = sum_ - x1
      if (x2, y) not in stat: # or stat[(x2,y)] != cnt1:
        return False
    return True


if __name__ == "__main__":
  a = Solution()
  print a.isReflected([[1,1],[-1,1]])
  print a.isReflected([[1,1],[-1,-1]])
