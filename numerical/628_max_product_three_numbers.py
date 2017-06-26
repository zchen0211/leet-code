"""
628. Maximum Product of Three Numbers (Easy)

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

class Solution(object):
  def maximumProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n <= 2: return 0
    max_ = nums[:3]
    min_ = nums[:3]
    for i in range(3, n):
      if nums[i] > min(max_):
        tmp = min(max_)
        max_.remove(tmp)
        max_.append(nums[i])
      if nums[i] < max(min_):
        tmp = max(min_)
        min_.remove(tmp)
        min_.append(nums[i])
    min_.sort()
    max_.sort()
    return max(max_[0]*max_[1]*max_[2], min_[0]*min_[1]*max_[2])
