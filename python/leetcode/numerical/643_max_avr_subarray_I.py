"""
643. Maximum Average Subarray I (Easy)

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        n = len(nums)
        max_ = sum(nums[:k])
        curr = max_
        while i < n - k:
            curr -= nums[i]
            curr += nums[i + k]
            max_ = max(max_, curr)
            i += 1
        result = float(max_) / k
        return result
