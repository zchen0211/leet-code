'''
391. Perfect Rectangle (Hard)

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
'''

"""
math problem:
1.a all internal points shared by 2 or 4;
1.b all corners should be 1;
2. sum should be equal to overall area
"""

class Solution(object):
  def solution2(self, rectangles):
    n = len(rectangles)
    pt_record = {}
    x_min, y_min, x_max, y_max = None, None, None, None
    area_sum = 0
    for i in range(n):
      tmp = rectangles[i]
      x1, y1, x2, y2 = tmp
      if x_min is None: x_min = x1
      else: x_min = min(x_min, x1)
      if y_min is None: y_min = y1
      else: y_min = min(y_min, y1)
      if x_max is None: x_max = x2
      else: x_max = max(x_max, x2)
      if y_max is None: y_max = y2
      else: y_max = max(y_max, y2)
      if (x1,y1) not in pt_record:
        pt_record[(x1,y1)] = 1
      else:
        pt_record[(x1,y1)] += 1
      if (x2,y2) not in pt_record:
        pt_record[(x2,y2)] = 1
      else:
        pt_record[(x2,y2)] += 1
      if (x1,y2) not in pt_record:
        pt_record[(x1,y2)] = 1
      else:
        pt_record[(x1,y2)] += 1
      if (x2,y1) not in pt_record:
        pt_record[(x2,y1)] = 1
      else:
        pt_record[(x2,y1)] += 1
      area_sum += (x2-x1)*(y2-y1)
    print area_sum
    print x_min, x_max, y_min, y_max
    # check condition 1: area_sum
    if area_sum != (x_max-x_min)*(y_max-y_min):
      return False
    # check condition 2: point intersect
    for k in pt_record.keys():
      x, y = k
      if x==x_min and y==y_min:
        if pt_record[k]!=1: return False
      elif x==x_min and y==y_max:
        if pt_record[k]!=1: return False
      elif x==x_max and y==y_min:
        if pt_record[k]!=1: return False
      elif x==x_max and y==y_max:
        if pt_record[k]!=1: return False
      elif pt_record[k] % 2 != 0:
        print 'break', k
        return False
    return True

  def isRectangleCover(self, rectangles):
    """
    :type rectangles: List[List[int]]
    :rtype: bool
    """
    n = len(rectangles)
    # check intersect
    for i in range(n):
      for j in range(i+1, n):
        rect1 = rectangles[i]
        rect2 = rectangles[j]
        if self.intersect(rect1, rect2):
          print 'rect1', rect1
          print 'rect2', rect2
          print 'intersect!'
          return False
    # check area and area_sum
    tmp = rectangles[0]
    x_min, y_min, x_max, y_max = tmp
    area_sum = (x_max-x_min)*(y_max-y_min)
    print 'rect', tmp, 'area', area_sum
    for i in range(1, n):
      tmp = rectangles[i]
      x1, y1, x2, y2 = tmp
      area_sum += (x2-x1) * (y2-y1)
      print 'rect', tmp, 'area', area_sum
      x_min = min(x_min, x1)
      x_max = max(x_max, x2) 
      y_min = min(y_min, y1)
      y_max = max(y_max, y2)
    print 'area sum:', area_sum
    print x_min, x_max, y_min, y_max
    return area_sum == (x_max-x_min)*(y_max-y_min)

  def intersect(self, rect1, rect2):
    # return True if rect1 and rect2 intersects
    # just neighbor: False
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    center1 = [x1+x2, y1+y2] # missing /2 to avoid float problem
    center2 = [x3+x4, y3+y4]
    diff_x = center1[0] - center2[0]
    diff_y = center1[1] - center2[1]
    diff_x = max(diff_x, -diff_x)
    diff_y = max(diff_y, -diff_y)
    edge_x1 = x2 - x1
    edge_x2 = x4 - x3
    edge_y1 = y2 - y1
    edge_y2 = y4 - y3
    if diff_x < (edge_x1+edge_x2) and diff_y < (edge_y1+edge_y2):
      return True
    else:
      return False

if __name__ == '__main__':
  a = Solution()
  print a.solution2([
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]])
  print a.solution2([
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]])
