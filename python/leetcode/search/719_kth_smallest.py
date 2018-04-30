"""
719. Find K-th Smallest Pair Distance (Hard)

Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""

class Solution(object):
  def smallestDistancePair(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    n = len(nums)
    nums.sort()

    min_, max_ = 0, nums[-1] - nums[0]
    while min_ < max_:
      print 'loop again'
      mid = (min_ + max_) / 2
      print 'min_, max_, mid', min_, max_, mid
      cnt, closest = self.cnt_diff(nums, mid)
      print 'mid, cnt, closest', mid, cnt, closest
      if cnt < k:
        min_ = mid + 1
      elif cnt == k:
        min_ = mid
        break
      else:
        max_ = mid

    # need to find the diff closest to mid
    print 'break out', min_
    _, closest = self.cnt_diff(nums, min_)
    return closest

  def cnt_diff(self, nums, target):
    # return how many diffs <= target
    print 'target', target
    accu = 0
    i, j = 0, 1
    n = len(nums)
    closest = 0
    while i < n:
      # locate j
      while j < n and nums[j] - nums[i] <= target:
        j += 1
      j = max(i, j-1)
      print i, j, nums[i], nums[j]
      # if nums[j] - nums[i] > target:
      accu += j - i
      if target - closest > target - (nums[j] - nums[i]):
        closest = nums[j] - nums[i]
      i += 1
    print 'accu, closest', accu, closest
    return accu, closest

if __name__ == "__main__":
  a = Solution()
  print a.smallestDistancePair([1,300,1], 2)
  # print a.smallestDistancePair([62, 100, 4], 2)
