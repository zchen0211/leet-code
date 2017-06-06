"""
442. Find All Duplicates in an Array (Medium)

Given an array of integers, 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

class Solution(object):
  def findDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    n = len(nums)
    for tmp in nums:
      tmp = abs(tmp) - 1
      if nums[tmp] < 0: result.append(tmp+1)
      else: nums[tmp] = -nums[tmp]
    return result


if __name__ == '__main__':
  a = Solution()
  print a.findDuplicates([4,3,2,7,8,2,3,1])
