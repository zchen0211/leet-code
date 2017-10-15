"""
698. Partition to K Equal Sum Subsets (Medium)

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""

class Solution(object):
  def canPartitionKSubsets(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k == 1: return True
    total = sum(nums)
    if total % k != 0: return False
    target = total / k
    sums = [0] * k
    nums.sort(reverse=True)
    result = self.helper(nums, sums, k, target, 0)
    return result

  def helper(self, nums, sums, k, target, index):
    n = len(nums)
    if n == index:
      for item in sums:
        if item != target: return False
      return True
    for i in range(k):
      if nums[index] + sums[i] > target:
        continue
      sums[i] += nums[index]
      if self.helper(nums, sums, k, target, index+1):
        return True
      sums[i] -= nums[index]
    return False


if __name__ == "__main__":
  a = Solution()
  arr = [7628,3147,7137,2578,7742,2746,4264,7704,9532,9679,8963,3223,2133,7792,5911,3979]
  k = 6
  # print a.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
  # print a.canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 5)
  print a.canPartitionKSubsets(arr, 6)
