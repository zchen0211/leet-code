'''
218. The Skyline Problem (Hard)

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''

"""
Divide and Conquer
A Simple Solution is to initialize skyline or result as empty, then one by one add buildings to skyline. A building is added by first finding the overlapping strip(s). If there are no overlapping strips, the new building adds new strip(s). If overlapping strip is found, then height of the existing strip may increase. Time complexity of this solution is O(n2)

We can find Skyline in Θ(nLogn) time using Divide and Conquer. The idea is similar to Merge Sort, divide the given set of buildings in two subsets. Recursively construct skyline for two halves and finally merge the two skylines.

How to Merge two Skylines?
The idea is similar to merge of merge sort, start from first strips of two skylines, compare x coordinates. Pick the strip with smaller x coordinate and add it to result. The height of added strip is considered as maximum of current heights from skyline1 and skyline2.
Example to show working of merge:

  Height of new Strip is always obtained by takin maximum of following
     (a) Current height from skyline1, say 'h1'.  
     (b) Current height from skyline2, say 'h2'
  h1 and h2 are initialized as 0. h1 is updated when a strip from
  SkyLine1 is added to result and h2 is updated when a strip from 
  SkyLine2 is added.
 
  Skyline1 = {(1, 11),  (3, 13),  (9, 0),  (12, 7),  (16, 0)}
  Skyline2 = {(14, 3),  (19, 18), (22, 3), (23, 13),  (29, 0)}
  Result = {}
  h1 = 0, h2 = 0
 
  Compare (1, 11) and (14, 3).  Since first strip has smaller left x,
  add it to result and increment index for Skyline1. 
  h1 = 11, New Height  = max(11, 0)   
  Result =   {(1, 11)}

  Compare (3, 13) and (14, 3). Since first strip has smaller left x,
  add it to result and increment index for Skyline1
  h1 = 13, New Height =  max(13, 0)
  Result =  {(1, 11), (3, 13)}   
  
  Similarly (9, 0) and (12, 7) are added.
  h1 = 7, New Height =  max(7, 0) = 7
  Result =   {(1, 11), (3, 13), (9, 0), (12, 7)}

  Compare (16, 0) and (14, 3). Since second strip has smaller left x, 
  it is added to result.
  h2 = 3, New Height =  max(7, 3) = 7
  Result =   {(1, 11), (3, 13), (9, 0), (12, 7), (14, 7)}

  Compare (16, 0) and (19, 18). Since first strip has smaller left x, 
  it is added to result.
  h1 = 0, New Height =  max(0, 3) = 3
  Result =   {(1, 11), (3, 13), (9, 0), (12, 7), (14, 3), (16, 3)}

Since Skyline1 has no more items, all remaining items of Skyline2 
are added 
  Result =   {(1, 11), (3, 13), (9, 0), (12, 7), (14, 3), (16, 3), 
              (19, 18), (22, 3), (23, 13), (29, 0)}

One observation about above output is, the strip (16, 3) is redundant
(There is already an strip of same height). We remove all redundant 
strips. 
  Result =   {(1, 11), (3, 13), (9, 0), (12, 7), (14, 3), (19, 18), 
              (22, 3), (23, 13), (29, 0)}

In below code, redundancy is handled by not appending a strip if the 
previous strip in result has same height.
"""

import Queue
import heapq

class Solution(object):
  def getSkyline(self, buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    # sort it first
    buildings.sort(key=tuple)
    n = len(buildings)

    if n == 0: return []

    x1, x2, y = buildings[0]
    critical = [[x1, y], [x2,0]]
    cri_id = 0
 
    for i in range(1,n):
      # new building
      x1, x2, y = buildings[i]

      # update critical point
      cri_n = len(critical)
      while cri_id<cri_n and x1>critical[cri_id][0]:
        cri_id += 1

      # cases:
      if cri_id == n: # current building right of all buildings seen
        critical.append([x1,y])
        critical.append([x2,0])
      else:
        new_id = cri_id
        while new_id != len(critical) and critical[new_id][0] < x2:
          old_x, old_y = critical[new_id]
          if y > old_y: # covers it, update
            critical[new_id] = [old_x, y]
          new_id += 1
        print 'new_id', new_id
        # finishing:
        if new_id == len(critical):
          critical.append([x2,0])
        elif critical[new_id][1] < y and x2 != critical[new_id][0]: # previous y_<y, update
          critical.insert(new_id, [x2, critical[new_id-1][1]])

        # starting:
        # insert before cri_id, if it is critical
        old_x, old_y = critical[cri_id]
        if x1 == old_x:
          critical[cri_id] = [old_x, max(y, old_y)]
        elif y>critical[cri_id-1][1]:
          critical.insert(cri_id, [x1, y])
      print i, critical
    print 'critical', critical
    result = []
    result.append([critical[0][0], critical[0][1]])
    for i in range(1, len(critical)):
      x, y = critical[i]
      if y != result[-1][1]:
        result.append([x,y])
    return result

  def solve(self, buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    # Correct Solution, but will TLE
    # sort it first
    buildings.sort(key=tuple)
    n = len(buildings)

    if n == 0: return []

    critical = []
    for item in buildings:
      x1, x2, y = item
      critical.append(x1)
      critical.append(x2)
    critical = list(set(critical))
    critical.sort()
    c_n = len(critical)
    critical_y = [0] * c_n

    c_i = 0   
 
    for item in buildings:
      x1, x2, y = item
      i = c_i
      flag = True
      while i < c_n:
        if critical[i] < x1:
          i += 1
          continue
        elif critical[i]>= x1 and critical[i]<x2:
          if flag:
            c_i = i
            flag = False
          critical_y[i] = max(critical_y[i], y)
          i += 1
        else: # critical[i] >= x2:
          break
    print critical
    print critical_y

    result = []
    for i in range(c_n):
      if len(result)==0 or critical_y[i] != result[-1][1]:
        result.append([critical[i], critical_y[i]])
    return result

  def solve2(self, buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    # Correct Solution, but will TLE
    # sort it first
    buildings.sort(key=tuple)
    n = len(buildings)

    if n == 0: return []

    critical = []
    for item in buildings:
      x1, x2, y = item
      critical.append(x1)
      critical.append(x2)
    critical = list(set(critical))
    critical.sort()
    c_n = len(critical)
    critical_y = [0] * c_n
    active_set = Queue.PriorityQueue()
    active_set.put((buildings[0][1], 0))
    new_id = 1

    for i in range(c_n):
      x = critical[x]
      # update active_set
      # remove used ones
      while active_set.qsize() > 0:
        x2, i = active_set.get()
        if x2 > x:
          active_set.put((x2, i))
          break

      # add new ones
      while new_id<n and buildings[new_id][0] <= x:
        if buildings[new_id][1] > x:
          active_set.append(new_id)
        new_id += 1

    for i in range(c_n):
      if len(result)==0 or critical_y[i] != result[-1][1]:
        result.append([critical[i], critical_y[i]])
    return result

  def solve4(self, buildings):
    events = []
    for item in buildings:
      Li, Ri, Hi = item
      events.append((Li, -Hi, Ri))
      events.append((Ri, 0, None))

    events.sort()

    ret = [[0, 0]] # [Li, Hi]
    hp = [(0, float('inf'))] # [Hi, Ri]

    for item in events:
      Li, NegH, Ri = item
      while Li >= hp[0][1]:
        heapq.heappop(hp)
      if NegH < 0:
        heapq.heappush(hp, (NegH, Ri))
      if ret[-1][1] != -hp[0][0]:
        ret.append([Li, -hp[0][0]])
      print 'l, h, r', item
      print 'heap', hp
      print 'ret', ret
      print ''
    return ret[1:]

  def solve3(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # AC
        # organize skyline potentials in 
        # left, -h, right
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        
        # res: results to return [L, H]
        # hp: heap to keep record of (-h, R) as a priority queue
        res, hp = [[0, 0]], [(0, float("inf"))]
        
        for x, negH, R in events:
            # safe to remove, since all remaing has larger L
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            # if not an ending potential, added to heap
            if negH: 
                heapq.heappush(hp, (negH, R))
            # if condition to tackle corner case: h1 = h2
            # if the new one has exactly the same height
            # record it and add to the system
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]

if __name__ == '__main__':
  a = Solution()
  # a.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12]])
  print a.solve([ [2, 9, 10], [3, 7, 15], [5, 12, 12]])
  # print a.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])
  # print a.solve([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])
  # print a.getSkyline([[1,2,1],[1,2,3]])
  # print a.getSkyline([[1,2,1],[1,2,2],[1,2,3]])
  # print a.getSkyline([[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]])
  # print a.solve([[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]])
  print a.solve4([ [2, 9, 10], [3, 7, 15], [5, 12, 12]])
  print a.solve3([ [2, 9, 10], [3, 7, 15], [5, 12, 12]])
