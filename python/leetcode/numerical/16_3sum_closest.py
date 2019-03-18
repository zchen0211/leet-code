"""
16. 3Sum Closest (Medium)

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        result = sum(nums[0:3])

        i = 0
        while i < n - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j, k = i + 1, n - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if k != n - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                tmp = nums[i] + nums[j] + nums[k]
                if abs(tmp - target) < abs(result - target):
                    result = tmp
                if tmp > target:
                    k -= 1
                elif tmp < target:
                    j += 1
                else:
                    return target
            i += 1
        return result
