"""
491. Increasing Subsequences (Medium)

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""

class Solution(object):
  def findSubsequences(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    n = len(nums)
    if n <= 1: return []
    if n == 2:
      if nums[0] <= nums[1]: return [[nums[0], nums[1]]]
      else: return []
    # n >=3 case
    result = self.findSubsequences(nums[:-1])
    print result
    new_result = []
    for item in nums[:-1]:
      if item <= nums[-1]:
        new_result.append([item, nums[-1]])
    for item in result:
      new_result.append(item)
      print 'item', item
      if item[-1] <= nums[-1]:
        print 'item', item
        new_item = [i for i in item]
        print 'new item', new_item
        new_item.append(nums[-1])
        new_result.append(new_item)
    print new_result
    new_result = [tuple(item) for item in new_result]
    new_result = list(set(new_result))
    new_result = [list(item) for item in new_result]
    return new_result


if __name__ == '__main__':
  a = Solution()
  # print a.findSubsequences([4,6,7,7])
  print a.findSubsequences([1,1,1]) 
