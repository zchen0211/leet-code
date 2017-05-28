'''
1. Two Sum (Easy)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        rec = {} # map num to index
        for i in range(len(nums)):
            # find solution
            if rec.has_key(target-nums[i]):
                return [rec[target-nums[i]], i]
            else:
                rec[nums[i]] = i


if __name__ == '__main__':
  a = Solution()
  print a.twoSum([2,7,11,15], 9)
