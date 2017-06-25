'''
164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

'''
import collections

class Solution(object):
  def maximumGap(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n < 2: return 0
    stat = collections.Counter(nums)

    min_ = min(stat.keys())
    max_ = max(stat.keys())
    curr = min_
    best = 0
    for i in range(min_+1, max_+1):
      if i in stat:
        best = max(best, i-curr)
        curr = i
    return best


if __name__ == '__main__':
  a = Solution()
  # print a.maximumGap([1,7,2, 15])
  print a.maximumGap([1,10000000])
