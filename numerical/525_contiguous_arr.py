"""
525. Contiguous Array (Medium)

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

class Solution(object):
  def findMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    cnt = 0
    stat = {0:[0]}
    for i in range(len(nums)):
      if nums[i] == 0: cnt += 1
      else: cnt -= 1
      if cnt in stat:
        stat[cnt].append(i+1)
      else:
        stat[cnt] = [i+1]
    print stat
    max_ = 0
    for k in stat.keys():
      if len(stat[k]) >=2:
        max_ = max(max_, max(stat[k]) - min(stat[k]))
    return max_


if __name__ == '__main__':
  a = Solution()
  print a.findMaxLength([0,1])
  print a.findMaxLength([0,1,0])
  print a.findMaxLength([0,1,0,1])
