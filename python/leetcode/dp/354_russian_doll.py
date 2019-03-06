"""
354. Russian Doll Envelopes (Hard)

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

"""
Sort the array. Ascend on width and descend on height if width are same.
Find the longest increasing subsequence based on height.

Since the width is increasing, we only need to consider height.
[3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]
"""

class Solution(object):
  def maxEnvelopes(self, envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    # sort first
    n = len(envelopes)
    if n == 0: return 0
    envelopes = [tuple(item) for item in envelopes]

    # step 0: sort by width, (decreasing in height s.t.)
    envelopes.sort(cmp = lambda a,b: -1 if a[0]<b[0] or (a[0]==b[0] and a[1]>b[1]) else 1)
    print envelopes

    # step 1: find the longest increasing subsequence
    result = [0] * n
    result[0] = envelopes[0][1]
    nums = [item[1] for item in envelopes]
    print nums
    cnt = 1
    for item in nums:
      idx = bsearch(result, cnt, item)
      print cnt, idx, item
      if idx == cnt:
        result[idx] = item
        cnt += 1
      elif result[idx] > item:
        result[idx] = item
      print result
    return cnt 

def bsearch(nums, len_, val):
    print 'search', val, nums[len_-1]
    if val > nums[len_-1]: return len_
    # find first num >= val
    start = 0
    end = len_
    mid = (start + end)/2
    while start < end:
      mid = (start + end) /2
      if nums[mid] == val: return mid
      elif nums[mid] < val:
        start = mid + 1
      else: # nums[mid] > val
        end = mid
    mid = min(len_-1, max(start, end))
    if nums[mid] >= val:
      return mid
    else:
      return mid+1

if __name__ == "__main__":
  a = Solution()
  # print a.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) 
  print a.maxEnvelopes([[10,17],[10,19],[16,2],[19,18],[5,6]]) 
