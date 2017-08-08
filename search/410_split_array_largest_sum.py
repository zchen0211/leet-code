"""
410. Split Array Largest Sum (Hard)

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 <= n <= 1000
1 <= m <= min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

class Solution(object):
  def splitArray(self, nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    min_ = max(nums)
    max_ = sum(nums)+1
    i = 0
    while min_ < max_:
      mid = (min_ + max_)/2
      print min_, max_, mid
      if self.solve(nums, m, mid):
        max_ = mid
        print True
      else:
        min_ = mid+1
        print False
      i += 1
      if i == 10: break
    return min_
        
  def solve(self, nums, m, max_):
    i = 0
    n = len(nums)
    mi = 0
    curr = 0
    while i < n:
      if curr + nums[i] <= max_:
        curr += nums[i]
      else:
        mi += 1
        curr = nums[i]
      print i, nums[i], mi
      i += 1
      if mi >= m: return False
    return True


if __name__ == "__main__":
  a = Solution()
  print a.splitArray([7,2,5,10,8], 2)
  # print a.solve([7,2,5,10,8], 2, 17)

