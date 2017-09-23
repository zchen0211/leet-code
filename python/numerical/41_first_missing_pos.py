'''
41. First Missing Positive (Hard)

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 1
        for i in range(n):
			nums[i] = max(nums[i], 0)

        i = 0
        while i < n:
          k = nums[i]
          while k > 0 and k <= n:
              tmp = nums[k-1] # save the number first
              nums[k-1] = -1
              k = tmp
          i += 1
          print nums
        i = 0
        while i < n:
          if nums[i] != -1: return i + 1
          i += 1
        return n + 1


if __name__ == "__main__":
    a = Solution()
    print a.firstMissingPositive([1,2,0])
    print a.firstMissingPositive([0,1,2])
    print a.firstMissingPositive([1,2])
    print a.firstMissingPositive([3,4,-1,1])
