'''
436. Find Right Interval (Medium)

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
'''

# Definition for an interval.
class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

class Solution(object):
  def findRightInterval(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[int]
    """
    n = len(intervals)
    if n == 1: return [-1]

    arr = []
    for i in range(n):
      arr.append((intervals[i].start, i))
    arr.sort(key= lambda item: item[0])
    print arr
    # contains (start, id)
    result = []
    for interv in intervals:
      result.append(self.helper(arr, interv.end))
    return result

  def helper(self, arr, item):
    # return id s.t. arr[id] >= item
    # else return -1
    n = len(arr)
    start = 0
    end = n
    while(start < end):
      mid = (start+end)/2
      if item > arr[mid][0]:
        start = mid+1
      elif item < arr[mid][0]:
        end = mid
      else: # item == arr[mid][1]
        return arr[mid][1]
    if end == n or start>end: return -1
    else: return arr[start][1]


if __name__ == '__main__':
  a = Solution()
  int1 = Interval(1,4)
  int2 = Interval(2,3)
  int3 = Interval(3,4)
  print a.findRightInterval([int1, int2, int3])
