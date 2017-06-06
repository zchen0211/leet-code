'''
169. Majority Element (Easy)

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if num == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    num = nums[i]
                    cnt = 1
        return num
