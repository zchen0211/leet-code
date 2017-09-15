'''
15. 3Sum (Medium)

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        i = 0
        n = len(nums)
        print nums
        
        i = 0
        while i < n - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j = i + 1
            k = n - 1
            while j < k:
                if j != i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if k != n - 1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ > 0:
                    k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
            i += 1
        return result
