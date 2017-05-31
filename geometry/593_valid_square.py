"""
593. Valid Square (Medium)

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""
import collections

class Solution(object):
  def validSquare(self, p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    dis12 = self.distance(p1, p2)
    dis13 = self.distance(p1, p3)
    dis14 = self.distance(p1, p4)
    dis23 = self.distance(p2, p3)
    dis24 = self.distance(p2, p4)
    dis34 = self.distance(p3, p4)

    dis_stat = collections.Counter([dis12,dis13,dis14,dis23,dis24,dis34]) 
    dis_stat = dict(dis_stat)
    
    if len(dis_stat.keys()) == 2:
      max_ = max(dis_stat.keys())
      min_ = min(dis_stat.keys())
      if dis_stat[max_]==2 and dis_stat[min_]==4 and max_==2*min_:
        return True
    return False


  def distance(self, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1-x2)**2 + (y1-y2)**2

if __name__ == '__main__':
  a = Solution()
  # print a.validSquare([0,0],[1,1],[1,0],[0,2])
  print a.validSquare([0,0],[-1,0],[1,0],[0,1])
