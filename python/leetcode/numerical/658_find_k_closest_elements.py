"""
658. Find K Closest Elements (Medium)

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
"""

class Solution(object):
  def solve2(self, arr, k, x):
    n = len(arr)
    if x <= arr[0]:
      return arr[:k]
    if x >= arr[-1]:
      return arr[-k:]
    print "in total ", n, " elements" 
    # st_ to st_+k-1
    st = 0
    end = n
    # step 1: find x first
    while st < end:
      mid = (st+end)/2
      if arr[mid] == x:
        break
      elif arr[mid] > x:
        end = mid - 1
      else:
        st = mid + 1
    # step 2: append
    small = []
    large = []
    id1, id2, id3 = max(0, mid-1), mid, min(mid+1, n-1)
    dis1, dis2, dis3 = abs(x-arr[id1]), abs(x-arr[id2]), abs(x-arr[id3])
    min_dis = min(dis1, dis2, dis3)
    if min_dis == dis1: id_ = id1
    elif min_dis == dis2: id_ = id2
    else: id_ = id3

    small.append(arr[id_])
    id1, id2 = id_-1, id_+1
    while len(small) + len(large) < k:
      if id2 >= n or abs(arr[id1]-x) <= abs(arr[id2]-x):
        small.append(arr[id1])
        id1 -= 1
      else:
        large.append(arr[id2])
        id2 += 1
    print small, large
    return small[::-1]+large 



  def findClosestElements(self, arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    n = len(arr)
    if x <= arr[0]:
      return arr[:k]
    if x >= arr[-1]:
      return arr[-k:]
    print "in total ", n, " elements" 
    # st_ to st_+k-1
    st = 0
    end = n
    # step 1: find x first
    while st < end:
      mid = (st+end)/2
      if arr[mid] == x:
        break
      elif arr[mid] > x:
        end = mid - 1
      else:
        st = mid + 1
    print st, end, mid, arr[st], arr[end], arr[mid]

    best, best_dis = 0, (abs(arr[0]-x), abs(arr[k-1]-x))
    # extreme case 1: all small
    if arr[mid] > x:
      mid -= 1
    tmp = max(mid-k+1, 0)
    tmp_dis = (abs(arr[tmp]-x), abs(arr[tmp+k-1]-x))
    if self.compare(tmp_dis, best_dis) == 1:
      best, best_dis = tmp, tmp_dis
    print arr[best:best+k], best_dis
    # extreme case 2: all big
    if arr[mid] < x:
      mid += 1
    tmp = min(mid, n-k)
    tmp_dis = (abs(arr[tmp]-x), abs(arr[tmp+k-1]-x))
    if self.compare(tmp_dis, best_dis):
      best, best_dis = tmp, tmp_dis
    print 'current best, ', arr[best:best+k], best_dis
 
    st = 0
    end = min(mid+1, n-k)
    print "search space: ", st, end
    st_last = -1
    end_last = -1
    while st < end:
      st_last, end_last = st, end
      st_ = (st+end)/2
      end_ = st_+k-1
      # if k >= n:
      print arr[st_:st_+k]       
      if abs(arr[st_]-x) <= abs(arr[end_]-x):
        end = st_
      else:
        st = st_
      if st == st_last and end == end_last:
        break
    tmp = st_
    tmp_dis = abs(arr[tmp]-x), abs(arr[tmp+k-1]-x)
    if self.compare(tmp_dis, best_dis)==1 or (tmp_dis==best_dis and tmp<best):
      best, best_dis = tmp, tmp_dis

    return arr[best:best+k]

  def compare(self, n1_, n2_):
    if max(n1_) == max(n2_) and min(n1_) and min(n2_):
      return 0
    elif max(n1_) < max(n2_): 
      return 1
    elif max(n1_) == max(n2_) and max(n2_) == min(n2_) and min(n1_)<min(n2_):
      return 1
    elif max(n1_) == min(n2_) and min(n1_) > min(n2_):
      return -1


if __name__ == "__main__":
  a = Solution()
  # print a.findClosestElements([0,0,1,2,3,3,4,7,7,8], 2, 6)
  print a.solve2([0,0,1,2,3,3,4,7,7,8], 2, 6)
  # print a.findClosestElements([1,2,5,5,6,6,7,7,8,9], 7, 7)
  print a.solve2([1,2,5,5,6,6,7,7,8,9], 7, 7)
  # print a.findClosestElements([1,2,3,4,5], 2, 4)
  print a.solve2([1,2,3,4,5], 2, 4)
  # print a.findClosestElements([1,2,3,4,5], 4, -1)
  print a.solve2([1,2,3,4,5], 4, -1)
  arr = [0,1,2,2,5,5,7,9,11,11,13,16,16,17,17,17,17,20,21,21,22,23,25,30,30,31,32,32,32,34,34,38,38,39,39,41,41,42,43,44,46,47,48,48,48,49,50,52,54,54,57,57,58,59,59,60,61,63,63,63,63,64,64,64,67,68,71,72,72,73,75,76,76,77,78,78,79,83,83,83,83,84,85,86,90,91,92,93,93,94,96,96,96,97,98,98,98,98,98,99]
  # print a.findClosestElements(arr, 94, 47)
  print a.solve2(arr, 94, 47)
